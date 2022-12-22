# UP_data_clean_up
DESCRIPTION
- This program uses the pandas library in python to read the contents of an excel file, make some formatting changes and clean up outdated and bugged text formatting methods to their most recent HTML counterparts (as of summer 2022), then create a new copy of the original file that contains all of the original information, but with the updates in formatting made.

USAGE
- This program is run through the command line with the line "python data_clean_up_v1_5.py <filename>" but has a reminder of proper usage if this line is not input properly.
- The filename portion is to be filled with the name of the excel file that the user would like to be updated.

LIST OF FORMATTING CHANGES
- "--" to an em dash
- "@-" to an en dash
- "###" to "<i>"
- "#" to "</i>"
- Curly apostrophe to straight apostrophe
- Curly quotes to straight quotes]
- "â€¦" to an ellipsis
