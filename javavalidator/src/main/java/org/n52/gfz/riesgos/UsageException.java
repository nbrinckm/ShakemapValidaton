package org.n52.gfz.riesgos;

public class UsageException extends RuntimeException {
    public UsageException(String reason) {
        super(reason);
    }

    public UsageException(Throwable reason) {
        super(reason);
    }
}
