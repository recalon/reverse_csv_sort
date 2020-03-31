## Introduction

This application is a brief exercise in Docker-hosted apps. Apart from bare basics, it is also an exercise in file i/o 
as it pertains to Docker containers.

## How to use

To run the service, from the project root directory run `docker-compose up -d`. To rebuild the app with changes to the
processor run with the `--build` flag. Once the service is running copying CSV files into the input directory 
`data/inputs` or saving edits to files already in the input directory will trigger the sorting logic.

This application was developed without access to Docker Desktop for Windows. It has only been tested for *nix systems.

## Outputs

The application will produce 2 output files into the `data/outputs` directory for each input file processed. One output
will have reverse-**sorted and preserved** lines, and are identifiable by the "_sorted_lines" suffix in the filename's 
first dot-separated component. The other output will be **flattened to a single line and sorted** in reverse.
