import hashlib, pathlib
TEXT = "1 star: Monday showed up at 6:58 a.m. uninvited, drank my motivation, booked 9 meetings before coffee, and still called itself a fresh start."
def main():
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    data = TEXT.encode("utf-8")
    out.write_bytes(data)
    back = out.read_bytes()
    if hashlib.sha256(back).hexdigest() != hashlib.sha256(data).hexdigest():
        raise SystemExit("digest mismatch")
    if not (1 <= len(back.decode("utf-8")) <= 200):
        raise SystemExit("length out of gate")
if __name__ == "__main__":
    main()
