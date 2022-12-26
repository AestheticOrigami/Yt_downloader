# importing packages
from pytube import YouTube
import os
import time 
import  argparse,time

# url input from file list.txt

#start time
start_time = time.time()

prec=""
def single_download(url,destination=".\downloaded_songs"):
    yt=YouTube(url)
    try:
            video = yt.streams.filter(only_audio=True).first()
    except:
            print("\n"+"Error in downloading:: " + yt.title+"\n")
            return
                
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    try:
        os.rename(out_file, new_file)
    except:
        os.remove(out_file)
        print("song already downloaded:: " + yt.title)
    base,ext = os.path.splitext(out_file)

    print(yt.title + " has been successfully downloaded.")




def list_download(path,destination=".\downloaded_songs"):
    
    
    with open(path) as f:
        global prec
        lines = f.readlines()
        
        for line in lines:
            
            #check if line is duplicate
            if line==prec:
                print("duplicate line")
                
            prec=line
            if line.strip():
                single_download(line,destination)

            else:
                print("blank line")


def main():
    
    # Check for any flags first
    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--list", help="for list of song download")
    ap.add_argument("-s", "--single", help="for single song download.")
    ap.add_argument("-d", "--destination", help="destination folder")
    args = vars(ap.parse_args())

    if args["list"]:
        list_download(args["list"],args["destination"])
    elif args["single"]:
        single_download(args["single"],args["destination"])


def test_main():
    list_download("A:\github\yt_downloader\Yt_downloader\\try.txt")
if __name__ == '__main__':

    test_main()  
    