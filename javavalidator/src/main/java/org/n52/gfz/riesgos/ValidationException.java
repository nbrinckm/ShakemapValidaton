package org.n52.gfz.riesgos;

public class ValidationException extends RuntimeException {
    public ValidationException(Throwable reason) {
        super(reason);
    }
}
