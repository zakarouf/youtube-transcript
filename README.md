# Youtube Transcript Reader

Extracts transcript from youtube videos. 

## Usage

In order to get the transcript run
```sh
python3 transcript.py {COMMANDS}
```
On the terminal with the gollowing commands as specified below.

### Commands

##### `-h` `--help`

Prints out help message
```sh
python3 transcript.py -h
```

##### `-i` `--video_id`

Insert a video id to be processed
```sh
python3 transcript.py -i Tz0dq2krCW8
```

##### `-v` `--video`

Insert a video link
```sh
python3 transcript.py -v https://www.youtube.com/watch?v=Tz0dq2krCW8
```

##### `-w` `--onlywords`

Out only the text data

```sh
python3 transcript.py -w -i Tz0dq2krCW8
```

##### `-o` `--outfile`

Write to a file

```sh
python3 transcript.py -w -i Tz0dq2krCW8 -o ts.txt
```
> Will create a new file ts.txt and with the transcript data  written there.

If this option in not used, the output data will be printed on stdout.


