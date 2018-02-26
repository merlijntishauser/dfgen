# Gener8

CLI tool for generating CD related templates like Dockerfiles or kubernetes service templates

### CLI options
```
gener8 [OPTIONS] COMMAND [ARGS]...

  A little tool to generate commonly used ci/cd templates like Dockerfiles
  and kubernetes service definitions.

Options:
  -v, --verbose        enable/disable verbose messages
  -w, --write-to-file  write generated template to file
  -h, --help           Show this message and exit.

Commands:
  docker      Docker mode, this will create a Dockerfile
  kubernetes  Kubernetes mode
```

## Development
Gener8 uses Python3, it will break in python2.
Using a virtual environment is recommended.

## installing locally
```
pip install . --upgrae
```

### testing


### linting
Just running pylint will break on new python3 syntax, instead use:

```
python3 -m pylint <path>
```
or with reporting:
```
python3 -m pylint --reports=yes <path>
```

For pep8 compliance use 
```
pycodestyle --show-source --show-pep8
```
