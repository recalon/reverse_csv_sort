## Introduction

This application is a brief exercise in Docker-hosted apps. Apart from bare basics, it is also an exercise in file i/o 
as it pertains to Docker containers.

## How to use

To run the application place all CSVs to be sorted in the `data/inputs` directory, then run `execute.sh`.

On a Windows 
system you will need to run the bash script from a Docker Terminal session, and the code should live somewhere inside 
your C:\Users directory to play nicely with Docker (developed against Docker Toolbox due to lack of Docker Desktop).

## Outputs

The application will produce 2 output files for each input file into the `data/outputs` directory. One output will have reverse-**sorted and preserved** 
lines, and are identifiable by the "_sorted_lines" suffix in the filename's first dot-separated component. The other 
output will be **flattened to a single line and sorted** in reverse.
