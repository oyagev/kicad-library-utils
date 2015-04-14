
KiCad utilities
===============

## schlib directory

**schlib.py**: A python class to parse Schematic Libraries Files Format of the KiCad.


**checklib.py**: Such script invokes each checkrule script testing the requested libraries.


**checkrule3_x.py**: Each checkrule script checks your correspondent rule and prints out a report informing what is in disagreement with the [KiCad Library Convention](https://github.com/KiCad/kicad-library/wiki/Kicad-Library-Convention).


**fix-pins.py**: Such script was created in order to help the adaptation of the already existing library files to the KiCad Library Convention. It tests some cases of x/y "wrong" pins positions and try to fix them if they pass in the checking of some prerequisites. The description of the cases are explained in the head of the script file.

**test_schlib.sh**: A shell script used to validate the generation of files of the schlib class.

## sch directory

**sch.py**: A python class to parse Schematic Files Format of the KiCad.

**test_sch.sh**: A shell script used to validate the generation of files of the sch class.

**add_part_number.py**: This script is used to add/edit part numbers fields in the schematic files.

**update_footprints.py**: This script updates the footprints fields of sch files using a csv as input.


How to use
==========

## Schematic Library Checker

    # first get into schlib directory
    cd schlib
    
    # run the script passing the files to be checked
    ./checklib.py path_to_lib1 path_to_lib2
    
    # run the following command to see other options
    ./checklib.py -h

## Adding Part Number (PN) to Schematic Files

    # first get into sch directory
    cd sch
    
    # use the following command to add empty "MPN" fields in the schematic files
    ./add_part_number.py path_to_sch1 path_to_sch2
    
    # use the following command to add/edit the PN field using the passed csv file
    # the default behaviour is search for "Reference(s)" and "MPN" columns in the csv
    # the BOM generated by bom_csv_grouped_by_value plugin can be used after
    # manually add the MPN field in the Collated Components section (for example)
    ./add_part_number.py --bom-csv=path_to_bom_csv path_to_sch_files/*.sch
    
    # run the following command to see other options
    ./checklib.py -h