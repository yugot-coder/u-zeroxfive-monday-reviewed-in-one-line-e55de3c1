import hashlib, os, pathlib
TEXT = "1 star: Monday showed up at 6:58 a.m. uninvited, drank my motivation, booked 9 meetings before coffee, and still called itself a fresh start."
def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return pathlib.Path(out_dir) / "entry.txt"
    return pathlib.Path("/output/entry.txt")
def verify_written_bytes(back, data):
    if len(back) != len(data):
        raise SystemExit("read-back byte length mismatch")
    if back != data:
        raise SystemExit("read-back content mismatch")
    if hashlib.sha256(back).hexdigest() != hashlib.sha256(data).hexdigest():
        raise SystemExit("digest mismatch")
    if not (1 <= len(back.decode("utf-8")) <= 200):
        raise SystemExit("length out of gate")
def main():
    out = output_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    data = TEXT.encode("utf-8")
    out.write_bytes(data)
    back = out.read_bytes()
    verify_written_bytes(back, data)
if __name__ == "__main__":
    main()
