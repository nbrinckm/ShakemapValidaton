import pathlib
import invoke
import requests

# call it with 'invoke download_example_file' on the shell.
@invoke.task
def download_example_file():
    url = "https://github.com/HugoRosero/ShakeMapSampler/raw/main/testinputs/example_out_shakemap_correlated.xml"
    output_file = pathlib.Path(pathlib.Path(url).name)
    if not output_file.exists():
        resp = requests.get(url)
        resp.raise_for_status()

        with output_file.open("wb") as outfile:
            outfile.write(resp.content)

