import csv
import os


app_dir = "/tmp/reverse_string_sort/"


def build_export_filenames(fn):
    split_filename = fn.split('.')
    if split_filename[0] == "input":  # keeping as close as possible to the specified input.csv > output.csv scheme
        split_filename[0] = "output"
    else:
        split_filename[0] += "_sorted"

    """Build  and return output filenames"""
    if len(split_filename) > 1 and split_filename[-1] != "csv":
        split_filename[-1] = "csv"
    return [
        ".".join(
            [
                split_filename[0] + '_lines',
                *split_filename[1:]
            ]
        ) if len(split_filename) > 1 else (split_filename[0] + "_lines.csv"),
        ".".join(
            [
                split_filename[0] + '_flat',
                *split_filename[1:]
            ]
        ) if len(split_filename) > 1 else (split_filename[0] + "_flat.csv")
    ]


def write_to_output_files(data, filename_flat, filename_lines):
    """Build absolute paths for output files"""
    out_path_lines = f"{app_dir}out/{filename_lines}"
    out_path_flat = f"{app_dir}out/{filename_flat}"

    """Write to output files"""
    with open(out_path_lines, "w+") as o_f:
        print(f"writing to {filename_lines}...")
        csv_w = csv.writer(o_f)
        for row in data:
            csv_w.writerow(row)
    with open(out_path_flat, "w+") as o_f:
        print(f"writing to {filename_flat}...")
        csv_w = csv.writer(o_f)
        csv_w.writerow(sorted(sum(data, []), reverse=True))

    print(f"processed {filename}")


if __name__ == "__main__":
    """Header"""
    print("\n\n\n============\nStart sort\n============")

    """Load files for processing from the input directory"""
    filenames = os.listdir(f"{app_dir}in/")

    """Check that there are files at all"""
    if not filenames:
        print(f"Script requires CSV files to have been placed in {app_dir}in/ from data/inputs.")
        # no need for an exit condition - the rest of the code will not execute without filenames

    """Process CSVs for sorting"""
    for filename in filenames:
        print(f"processing {filename}...")

        if filename.startswith(".git"):
            print(f"file {filename} is a git file; skipping...")
            continue

        """Sort rows in input CSV"""
        sorted_rows = []
        in_path = f"{app_dir}in/{filename}"
        try:
            with open(in_path, "r") as i_f:
                csv_r = csv.reader(i_f)
                for f_row in csv_r:
                    sorted_rows.append(sorted(f_row, reverse=True))
        except FileNotFoundError as e:
            print(f"{e}\n{filename} input missing; skipping")
            continue

        """Parse input filename into output filename bases"""
        formatted_filename_lines, formatted_filename_flat = build_export_filenames(filename)

        write_to_output_files(sorted_rows, formatted_filename_flat, formatted_filename_lines)
