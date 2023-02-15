# ShakemapValidation

## What is the purpose?
This is a test repo to store code to validate shakemaps.

It is mainly driven by the python invoke module.


## How to run it?
To test the validation:

```
invoke validate_java
```

(Only tested under linux with invoke, wget, java & maven installed).

## Background

This validation is the very same as we use in our riesgos repositories.
This way we can make sure that the resampled shakemaps are validated
the very same way as our gfz-command-line-tool-repository does.
