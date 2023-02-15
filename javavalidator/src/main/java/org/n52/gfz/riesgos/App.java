package org.n52.gfz.riesgos;

import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import javax.xml.XMLConstants;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class App {

    private final String pathToSchemaFile;
    private final String pathToXmlFile;

    private App(String[] args) {
        if (args.length < 2) {
            throw new UsageException("Usage: java -jar app.jar <pathToSchemaFile> <pathToXmlFile>");
        }
        pathToSchemaFile = args[0];
        pathToXmlFile = args[1];

    }

    private void run() {
        try {
            // It is basically the same handling as in
            // https://github.com/riesgos/gfz-command-line-tool-repository/blob/master/src/main/java/org/n52/gfz/riesgos/validators/XmlBindingWithAllowedSchema.java
            // (and also copied & pasted)
            final Source xmlFile = new StreamSource(new FileReader(this.pathToXmlFile));
            final SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
            final Schema schema = schemaFactory.newSchema(new File(this.pathToSchemaFile));
            final Validator validator = schema.newValidator();

            final List<SAXParseException> validationErrors = new ArrayList<>();

            // https://stackoverflow.com/a/11131775/2249798
            validator.setErrorHandler(new ErrorHandler() {
                @Override
                public void warning(final SAXParseException exception) {
                    validationErrors.add(exception);
                }

                @Override
                public void fatalError(final SAXParseException exception) {
                    validationErrors.add(exception);
                }

                @Override
                public void error(final SAXParseException exception) {
                    validationErrors.add(exception);
                }
            });

            validator.validate(xmlFile);

            if (validationErrors.isEmpty()) {
                System.out.println("No validation errors");
            } else {
                System.out.println("There are " + validationErrors.size() + " errors:");
                for (final SAXException error : validationErrors) {
                    error.printStackTrace();
                }
            }


        } catch (FileNotFoundException ex) {
            throw new UsageException(ex);
        } catch (SAXException ex) {
            throw new ValidationException(ex);
        } catch (IOException ex) {
            throw new ValidationException(ex);
        }

    }

    public static void main(String[] args) {
        final App app = new App(args);
        app.run();
    }
}
