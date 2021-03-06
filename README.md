[![Build Status](https://travis-ci.org/EudesRobin/Mux-Sub.svg?branch=master)](https://travis-ci.org/EudesRobin/Mux-Sub)

Mux all season episodes with subtitles files
============================================

**Author :**
Robin Eudes

----------

> A simple python script to mux episodes with their associated subtitle file, using mkvmerge.

---------- 

Requirements
------------
- Python binaries in your PATH (I used Python 3.5.1)
- Mkvmerge binary in your PATH


How to use it
----------
    Usage : mux.py [options]
    -d [--directory] <path to directory containing subtitles and videos>
    Note: Double quotes arond the path are recommanded, to avoid any troubles with spaces.
    -h [--help] will print this help


Video files and subtitle files are sorted in lexical order, no case sensitive, in 2 separated lists. You can name them as your wish. Just know that for each mux loop iteration, the script will take the current item in both lists.

eg. The first subtitle will be mux with the first video file, and so on. 

You can check log file to be sure that the right files have been muxed together.

Supported formats
-----------------
- .srt or .ass subtitles files
- .mkv ; .avi ; .mp4 ; .ts video files

The output file will always be .mkv

Exemple
-------
    $>python mux.py -d "C:\TV\My.tv_serie.S01.1080p.WEB-DL-Team"
    C:\TV\My.tv_serie.S01.VOSTFR.1080p.WEB-DL-Team created
    mkvmerge v8.9.0 ('Father Daughter') 64bit
    'C:\TV\My.tv_serie.S01.1080p.WEB-DL-Team\My.tv_serie.S01E01.1080p.WEB-DL-Team.mkv': Using the demultiplexer for the format 'Matroska'.
    'C:\TV\My.tv_serie.S01.1080p.WEB-DL-Team\My.tv_serie.S01E01.1080p.WEB-DL-Team.srt': Using the demultiplexer for the format 'SRT subtitles'.
    'C:\TV\My.tv_serie.S01.1080p.WEB-DL-Team\My.tv_serie.S01E01.1080p.WEB-DL-Team.mkv' track 0: Using the output module for the format 'AVC/h.264'.
    'C:\TV\My.tv_serie.S01.1080p.WEB-DL-Team\My.tv_serie.S01E01.1080p.WEB-DL-Team.mkv' track 1: Using the output module for the format 'AC-3'.
    'C:\TV\My.tv_serie.S01.1080p.WEB-DL-Team\My.tv_serie.S01E01.1080p.WEB-DL-Team.mkv' track 2: Using the output module for the format 'text subtitles'.
    'C:\TV\My.tv_serie.S01.1080p.WEB-DL-Team\My.tv_serie.S01E01.1080p.WEB-DL-Team.srt' track 0: Using the output module for the format 'text subtitles'.
    The file 'C:\TV\My.tv_serie.S01.VOSTFR.1080p.WEB-DL-Team\My.tv_serie.S01E01.VOSTFR.1080p.WEB-DL-Team.mkv' has been opened for writing.
    Progress: 100%
    The cue entries (the index) are being written...
    Muxing took 26 seconds.

    C:\TV
    ├───My.tv_serie.S01.1080p.WEB-DL-Team
    │   ├───My.tv_serie.S01E01.1080p.WEB-DL-Team.mkv
    │   └───My.tv_serie.S01E01.1080p.WEB-DL-Team.srt
    │
    └───My.tv_serie.S01.VOSTFR.1080p.WEB-DL-Team
    	├───My.tv_serie.S01E01.VOSTFR.1080p.WEB-DL-Team.mkv
		└───log.txt

Docker container
-------
### Default behaviour (-d [--directory] option)
    `docker run --rm -v /patent_dir/:/usr/src/mux-mkv_srt/source/ benoitbrayer/mux-mkv_srt`

parent_dir: The parent directory of My.tv_serie.S01.1080p.WEB-DL-Team directory

    `docker run -v ~/My.tv_serie.S01.1080p.WEB-DL-Team directory/..:/usr/src/mux-mkv_srt/source/ benoitbrayer/mux-mkv_srt`

This syntax is ok too.

### Any other behaviour (Example using -h [--help] option)
    `docker run benoitbrayer/mux-mkv_srt -h`

Links
-------
- [Download Python](https://www.python.org/downloads/)
- [Download MkvToolnix](https://mkvtoolnix.download/downloads.html)
- [mkvmerge documentation](https://mkvtoolnix.download/doc/mkvmerge.html)
- [Docker](https://www.docker.com/)

License
-------
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.fr.html)
