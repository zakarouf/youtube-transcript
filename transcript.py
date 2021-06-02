from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtube_transcript_api._errors import TranscriptsDisabled

import sys, argparse

def getTranscript(vidID: str):
    data = yta.get_transcript(vidID)
    
    text :list[str] = []
    start :list[float] = []
    duration :list[float] = []

    for segments in data:
        text.append(segments['text'])
        start.append(segments['start'])
        duration.append(segments['duration'])

    return text, start, duration

def getTextWordCount(text) -> int:
    wc = 0
    for i in text:
        wc += len(i.split(' '))

    return wc

def print_out(args, text, start, duration):
    
    if args.onlywords:
        for i in text:
            print(i, end=" ")


def write_out(args, text, start, duration):

    if args.onlywords:
        with open(args.outfile, "w") as fp:
            fp.writelines(text)


def main_process_video_id(args, vid):
    data_text, data_start, data_duration = getTranscript(vid)
    
    if args.outfile == "":
        print_out(args, data_text, data_start, data_duration)

    print("Word Count: ", getTextWordCount(data_text))


def get_video_id_from_url(vid_url) -> str:
    try:
        index = vid_url.index("?v=")
        index += 3
        vid_id = vid_url[index:]
        return vid_id
    except:
        print(vid_url, "is not a valid Youtube Video URL.")
        return ""


def main(def_args=sys.argv[1:]):
    args = arguments_parse(def_args)

    if args.video_id != "":
        main_process_video_id(args, args.video_id)
    elif args.video != "":
        vid_id = get_video_id_from_url(args.video)
        main_process_video_id(args, vid_id)
    else:
        print("No Video Option Given")


def arguments_parse(argsval):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--video_id',
                        required=False, default="", type=str,
                        help="""Gets Video ID""")

    parser.add_argument('-v', '--video',
                        required=False, default="", type=str,
                        help="""Insert Video Link""")

    parser.add_argument('-o', '--outfile',
                        required=False, default="", type=str,
                        help="""Write to a file""")

    parser.add_argument('-w', '--onlywords',
                        required=False, action='store_true', default=False,
                        help="""Get only words, any other data such as timpstamp is discarded""")

    return parser.parse_args(argsval)


if __name__ == '__main__':
    main()
