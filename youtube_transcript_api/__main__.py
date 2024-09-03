import sys

import logging

from youtube_transcript_api._cli import YouTubeTranscriptCli


def main():
    logging.basicConfig()

    print(YouTubeTranscriptCli(sys.argv[1:]).run())


if __name__ == '__main__':
    main()
