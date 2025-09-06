# Scripts flow


| step  | script                                               | in filename                                       | out filename                                      | explanation                                |
| :---: | :--------------------------------------------------- | :------------------------------------------------ | :------------------------------------------------ | :----------------------------------------- |
|   -   | [test_data.ipynb](scripts/test_data.ipynb)           | -                                                 | -                                                 | Test some operations                       |
|   0   | xls_joiner.ipynb                                     | SABI_Export_N.xlsx                                | [joined.xlsx](data/original/joined.xlsx)          | Join XLSs in a single file                 |
|   1   | [db_reader.ipynb](scripts/db_reader.ipynb)           | [joined.xlsx](data/original/joined.xlsx)          | [formatted.xlsx](data/processed/formatted.xlsx)   | Reads original source and formats the data |
|   2   | [calc_columns.ipynb](scripts/calc_columns.ipynb)     | [formatted.xlsx](data/processed/formatted.xlsx)   | [calculated.xlsx](data/processed/calculated.xlsx) | Calcs all columns needed                   |
|   3   | [filter_indexes.ipynb](scripts/filter_indexes.ipynb) | [calculated.xlsx](data/processed/calculated.xlsx) | [filtered.xlsx](data/processed/filtered.xlsx)     | Filters columns needed                     |
|   4   | [reorder_data.ipynb](scripts/reorder_data.ipynb)     | [filtered.xlsx](data/processed/filtered.xlsx)     | [product.xlsx](data/product/product.xlsx)         | Reorder the data to feed the ia            |
|  ->   | [aicode.ipynb](aicode.ipynb)                         | [product.xlsx](data/product/product.xlsx)         | -                                                 | The ia                                     |