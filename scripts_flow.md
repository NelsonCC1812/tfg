# Scripts flow


| step  | script               | in filename        | out filename    | explanation                                |
| :---: | :------------------- | :----------------- | :-------------- | :----------------------------------------- |
|   -   | test_data.ipynb      | -                  | -               | Test some operations                       |
|   0   | xls_joiner.ipynb     | SABI_Export_N.xlsx | joined.xlsx     | Join XLSs in a single file                 |
|   1   | db_reader.ipynb      | joined.xlsx        | formatted.xlsx  | Reads original source and formats the data |
|   2   | calc_columns.ipynb   | formatted.xlsx     | calculated.xlsx | Calcs all columns needed                   |
|   3   | filter_indexes.ipynb | calculated.xlsx    | filtered.xlsx   | Filters columns needed                     |
|   4   | reorder_data.ipynb   | filtered.xlsx      | product.xlsx    | Reorder the data to feed the ia            |
|  ->   | aicode.ipynb         | product.xlsx       |                 | The ia                                     |