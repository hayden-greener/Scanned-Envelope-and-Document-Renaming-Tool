import os
from typing import Optional

def is_valid_jpg_file(filename: str) -> bool:
    return filename.lower().endswith(".jpg")

def extract_envelope_number(folder_name: str) -> Optional[str]:
    return folder_name if folder_name.isdigit() else None

def get_new_filename(original_name: str, envelope_number: str, batch_number: Optional[str] = None, scan_number: Optional[str] = None) -> str:
    if batch_number and scan_number:
        return f"envelope{envelope_number}_batch{batch_number}_scan{scan_number}_{original_name[3:11]}_{original_name[12:20]}.jpg"
    elif batch_number:
        return f"envelope{envelope_number}_batch{batch_number}_{original_name[3:11]}_{original_name[12:20]}.jpg"
    else:
        return f"envelope{envelope_number}_front_{original_name[3:11]}_{original_name[12:20]}.jpg"

def rename_files_in_folder(folder_path: str, envelope_number: str, batch_number: Optional[str] = None) -> None:
    print(f"Processing folder: {folder_path}")
    original_names_file = os.path.join(folder_path, f"original_names_envelope_{envelope_number}.txt")

    with open(original_names_file, "w") as file_handle:
        for filename in os.listdir(folder_path):
            if not is_valid_jpg_file(filename):
                continue

            original_name = filename
            if filename.startswith("img"):
                filename = filename[3:]

            if batch_number:
                scan_number = filename.split("_")[1].split(".")[0][-1]
                new_filename = get_new_filename(original_name, envelope_number, batch_number, scan_number)
            else:
                new_filename = get_new_filename(original_name, envelope_number)

            new_file_path = os.path.join(folder_path, new_filename)
            original_file_path = os.path.join(folder_path, original_name)
            os.rename(original_file_path, new_file_path)

            file_handle.write(f"{original_name} -> {new_filename}\n")
        file_handle.write("\n")

    print(f"Finished processing folder: {folder_path}")

def process_folder(folder_path: str, envelope_number: Optional[str] = None) -> None:
    if not os.path.isdir(folder_path):
        return

    if envelope_number is None:
        envelope_number = extract_envelope_number(os.path.basename(folder_path))

    if envelope_number:
        rename_files_in_folder(folder_path, envelope_number)

    for subfolder_name in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder_name)
        if os.path.isdir(subfolder_path):
            if subfolder_name.startswith("Batch"):
                batch_number = subfolder_name.split("Batch")[1]
                rename_files_in_folder(subfolder_path, envelope_number, batch_number)
            else:
                process_folder(subfolder_path, envelope_number)

def main() -> None:
    current_folder = os.getcwd()
    print(f"Current working directory: {current_folder}")

    for folder_name in os.listdir(current_folder):
        folder_path = os.path.join(current_folder, folder_name)
        if os.path.isdir(folder_path):
            process_folder(folder_path)

    print("File renaming completed.")

if __name__ == "__main__":
    main()