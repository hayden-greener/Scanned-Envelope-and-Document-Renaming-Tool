## Before
```
Before Folder Structure:
├── 1
│   ├── img01234567_20240309.jpg
│   ├── Batch1
│   │   ├── img01234567_20240309_1.jpg
│   │   └── img01234567_20240309_2.jpg
│   └── Batch2
│       ├── img01234567_20240309_1.jpg
│       └── img01234567_20240309_2.jpg
├── 2
│   ├── img98765432_20240309.jpg
│   └── Batch1
│       ├── img98765432_20240309_1.jpg
│       ├── img98765432_20240309_2.jpg
│       └── img98765432_20240309_3.jpg
└── 3
    ├── img13579246_20240309.jpg
    ├── Batch1
    │   ├── img13579246_20240309_1.jpg
    │   └── img13579246_20240309_2.jpg
    └── Batch2
        ├── img13579246_20240309_1.jpg
        ├── img13579246_20240309_2.jpg
        └── img13579246_20240309_3.jpg

```
## After
```
After Folder Structure:
├── 1
│   ├── envelope1_front_20240309_01234567.jpg
│   ├── original_names_envelope_1.txt
│   ├── Batch1
│   │   ├── envelope1_batch1_scan1_20240309_01234567.jpg
│   │   └── envelope1_batch1_scan2_20240309_01234567.jpg
│   └── Batch2
│       ├── envelope1_batch2_scan1_20240309_01234567.jpg
│       └── envelope1_batch2_scan2_20240309_01234567.jpg
├── 2
│   ├── envelope2_front_20240309_98765432.jpg
│   ├── original_names_envelope_2.txt
│   └── Batch1
│       ├── envelope2_batch1_scan1_20240309_98765432.jpg
│       ├── envelope2_batch1_scan2_20240309_98765432.jpg
│       └── envelope2_batch1_scan3_20240309_98765432.jpg
└── 3
    ├── envelope3_front_20240309_13579246.jpg
    ├── original_names_envelope_3.txt
    ├── Batch1
    │   ├── envelope3_batch1_scan1_20240309_13579246.jpg
    │   └── envelope3_batch1_scan2_20240309_13579246.jpg
    └── Batch2
        ├── envelope3_batch2_scan1_20240309_13579246.jpg
        ├── envelope3_batch2_scan2_20240309_13579246.jpg
        └── envelope3_batch2_scan3_20240309_13579246.jpg
```

## While Scanning

1. Create a separate folder for each envelope you scan. The folder name should be a number (e.g., "1", "2", "3", and so on).

2. Inside each envelope folder, save the scanned image of the front of the envelope.

3. Then for each document/paper inside the envelope, create subfolders named "Batch1", "Batch2", etc., inside the envelope folder.

4. Repeat these steps for each envelope you want to scan.

## Running the Renaming Script

1. Download the `main.py` file from the repository.

2. Place the `main.py` file in the same directory as your envelope folders.

3. **IMPORTANT:** Before running the script, make a copy of the envelope folders and apply the script to the copy, not the original folders. This is a safety precaution to ensure that your original files remain intact.

4. Open a terminal or command prompt and navigate to the directory containing the script.

5. Run the script using the following command:

```
python main.py
```


5. The script will process all the envelope folders and their subfolders in the current directory, renaming the files according to the following convention:
- Front envelope image: `envelope<envelope_number>_front_<date>_<time>.jpg`
- Document images: `envelope<envelope_number>_batch<batch_number>_scan<scan_number>_<date>_<time>.jpg`

6. The script will also create a text file named `original_names_envelope_<envelope_number>.txt` in each processed folder, listing the original and new filenames.

## Notes

- The script assumes that the original filenames follow the format `img<time>_<date>.jpg` or `<time>_<date>.jpg`. Files with other formats will be skipped.
