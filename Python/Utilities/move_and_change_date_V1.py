import os
from datetime import datetime

# folder paths
source_folder = "C:\\WordCloud"
destination_folder = "C:\WordCloud\Wordcloud_dated"

# get a list of files in the source folder
files = os.listdir(source_folder)

# check if there are any files in the source folder
if len(files) > 0:
    # get the current date and time
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d-%H-%M-%S")

    # move the first file in the list to the destination folder
    # and add the date string to the file name
    os.rename(os.path.join(source_folder, files[0]), os.path.join(destination_folder, f"{files[0]}_{date_string}"))
