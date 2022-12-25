
# Yotube  downloader
download songs and videos from Yotube with **one click**

with this tipe of script you can download songs directly from youtube 


## Examples

#### Download a song:
    yt_download.py -s "url_of_the_song"
 
#### Download a list of songs:
    yt_download.py -l "path_of_the_file.txt" 

#### Download a list of songs and put in a specific folder:
    yt_download.py -l "path_of_the_file.txt" -d "destination_folder"
## Documentation

|Name           |Parameter | Type     | Description                           |
| :--------     | :------- | :------- | :-------------------------            |
|Song           | `-s` | `url`  | download a song from a url                  |
|List of songs  | `-l` | `path` | download a list of songs from a **list of url** in a .txt file   |
|Destination    | `-d` | `path` | destination path of the downloaded files (defoult location is the same path of the script)              |



## Future features

1) Add video download support (single / list of url)

2) Search by the name of the song / video as well as with the url

3) make an online verion of this script
## Authors

- [@AestheticOrigami](https://github.com/AestheticOrigami)

