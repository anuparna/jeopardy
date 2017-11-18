# Jeopardy!

A web-application built on Jeopardy!, a popular American game show.<br/> The project presents a web-interface to search questions based on the game-show.

There are 3 questions we focus on:<b>
  
1. Which jeopardy questions were asked during a final round?
2. Which jeopardy questions were answered by Ken Jennings? 
3. Which jeopardy questions were answered by Brad Rutter?


NOTE: Ken Jennings is a contestant with a longest winning streak and Brad Rutter is a contestant with a highest earning. 

## Dataset
Dataset presents Jeopardy! games from 18 different seasons starting from Season 16 to Season 33. <br/>
There are around ~ 230 games in each season. <br/>
The dataset consists of 5 CSV files available at <a href="https://github.com/anuparna/jeopardy/tree/master/dataset">here</a>.<br/>
Path: ```jeopardy/dataset```

Entity Relationship Diagram is avalable <a href="https://raw.githubusercontent.com/anuparna/jeopardy/master/docs/ER_Diagram.pdf">here</a>.

## System Architecture
![System Architecture](https://raw.githubusercontent.com/anuparna/jeopardy/master/docs/system_architecture.jpg)

## Usage
```
python3 jeopardy/src/data_parsing_reconfiguration/generate_jeopardy_sql_files.py -h

usage: generate_jeopardy_sql_files.py -i=INPUT_CONFIG_FILE -o=
                                      OUTPUT_CONFIG_FILE [-h]

optional arguments:
  -h, --help            This Python script reads CSV files and creates .sql
                        files to insert in database. The project is meant to
                        be used for creating a Jeopardy database.

required named arguments:
  -i INPUT_CONFIG_FILE, --input_config INPUT_CONFIG_FILE
                        Input Configuration file provides details of the
                        locations of the required CSV files.                        

  -o OUTPUT_CONFIG_FILE, --output_config OUTPUT_CONFIG_FILE
                        Output Configuration file provides details of the
                        locations of the generated .sql files containing
                        insert statements for the Jeopardy database tables.
```
Sample INPUT_CONFIG_FILE available <a href="https://raw.githubusercontent.com/anuparna/jeopardy/master/src/data_parsing_reconfiguration/input_config.ini">here</a>.<br/>
 Sample OUTPUT_CONFIG_FILE available <a href="https://raw.githubusercontent.com/anuparna/jeopardy/master/src/data_parsing_reconfiguration/output_config.ini">here</a>.
