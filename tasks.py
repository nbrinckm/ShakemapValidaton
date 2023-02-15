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

@invoke.task(pre=[download_example_file, download_schema])
def validate_cli():
    input_file = "example_out_shakemap_correlated.xml"
    schema_file = "shakemap.xsd"

    invoke.run(f"xmllint --noout --schema {schema_file} {input_file}")

@invoke.task
def compile_java_validator():
    if not pathlib.Path("javavalidator/target/gfz-riesgos-xml-validator-1.0-SNAPSHOT.jar").exists():
        invoke.run("cd javavalidator && mvn clean package")

@invoke.task(pre=[download_example_file, download_schema, compile_java_validator])
def validate_java():
    input_file = "example_out_shakemap_correlated.xml"
    schema_file = "shakemap.xsd"

    invoke.run(f"java -jar javavalidator/target/gfz-riesgos-xml-validator-1.0-SNAPSHOT.jar {schema_file} {input_file}")

@invoke.task
def clean():
    for filename in ["example_out_shakemap_correlated.xml", "shakemap.xsd", "javavalidator/target/gfz-riesgos-xml-validator-1.0-SNAPSHOT.jar"]:
        path = pathlib.Path(filename)
        if path.exists():
            path.unlink()

