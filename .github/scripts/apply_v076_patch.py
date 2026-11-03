"""Apply the Study Ink v0.7.6 color picker patch to the v0.7.5 source."""
from pathlib import Path
import base64
import gzip
import subprocess

root = Path(__file__).resolve().parents[2]
source = root / ".github/patches/v076-color-picker.patch.gz.b64"
patch = root / ".github/patches/.v076-working.patch"

if not (root / "lib/screens/editor_screen.dart").is_file():
    raise SystemExit("Study Ink base source was not extracted before patching")

patch.write_bytes(gzip.decompress(base64.b64decode(source.read_text().strip())))
try:
    subprocess.run(["git", "apply", "--check", str(patch)], cwd=root, check=True)
    subprocess.run(["git", "apply", str(patch)], cwd=root, check=True)
    version = (root / "pubspec.yaml").read_text()
    if "version: 0.7.6+13" not in version:
        raise SystemExit("Unexpected Study Ink version after applying patch")
    if not (root / "lib/widgets/ink_tool_button.dart").is_file():
        raise SystemExit("Missing new color picker control")
    print("Applied Study Ink v0.7.6 color picker patch")
finally:
    patch.unlink(missing_ok=True)
