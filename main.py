import os
import shutil
import sys

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(f"Error creating output directory {output_dir}: {e}", file=sys.stderr)
        sys.exit(1)

    src = "entry.png"
    dst = os.path.join(output_dir, "entry.png")
    
    if not os.path.exists(src):
        print(f"Error: Source file {src} does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        shutil.copy(src, dst)
        print(f"Successfully copied {src} to {dst}")
    except Exception as e:
        print(f"Error copying {src} to {dst}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

