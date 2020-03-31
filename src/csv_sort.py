import csv
import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


app_dir = "/reverse_csv_sort/"


def handle_new(event):
    path, file = event.src_path.rsplit("/", 1)

    print(f"path: {path}   file: {file}")

    handle_csv(file)


def handle_modify(event):
    if type(event) is not "FileModifiedEvent":
        return
    print(f"modify event: {event}")


def handle_csv(filename):
    csv_sorted = sort_csv(filename)

    write_to_output_files(csv_sorted, *build_export_filenames(filename))


def do_nothing(event):
    print(f"doing nothing with {event}")
    return None


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


def write_to_output_files(data, filename_lines, filename_flat):
    if not data:
        return

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


def sort_csv(file):
    print()
    sorted_rows = []
    in_path = f"{app_dir}in/{file}"

    try:
        with open(in_path, "r+") as i_f:
            csv_r = csv.reader(i_f)
            for f_row in csv_r:
                sorted_rows.append(sorted(f_row, reverse=True))
    except FileNotFoundError as e:
        print(f"{e}\nfile {file} not found; skipping")

    return sorted_rows


if __name__ == "__main__":
    print("starting script")
    listener = PatternMatchingEventHandler(
        "*",
        ".gitignore"
    )
    print("listener created")

    listener.on_moved = do_nothing
    listener.on_deleted = do_nothing
    listener.on_created = handle_new
    listener.on_modified = handle_modify
    print("listener configured")

    fs_observer = Observer()
    fs_observer.schedule(listener, f"{app_dir}/in")
    print("observer created, starting")

    fs_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        fs_observer.stop()
        fs_observer.join()

    print("exiting")
