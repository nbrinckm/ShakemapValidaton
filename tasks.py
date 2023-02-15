import pathlib
import invoke

# call it with 'invoke download_example_file' on the shell.
@invoke.task
def download_example_file():
    url = "https://github.com/HugoRosero/ShakeMapSampler/raw/main/testinputs/example_out_shakemap_correlated.xml"
    output_file = pathlib.Path(pathlib.Path(url).name)
    if not output_file.exists():
        invoke.run(f"wget {url}")


@invoke.task
def download_schema():
    url = "https://raw.githubusercontent.com/riesgos/gfz-command-line-tool-repository/master/src/main/resources/org/n52/gfz/riesgos/validators/xml/shakemap.xsd"
    output_file = pathlib.Path(pathlib.Path(url).name)
    if not output_file.exists():
        invoke.run(f"wget {url}")
