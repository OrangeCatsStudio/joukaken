import os

work_id = "p_2"
unchecked_filepath = "./" + work_id + "_unchecked.html"

checked_filepath = os.rename(unchecked_filepath, "./"+work_id+".html")