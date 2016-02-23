Mux your serie subtitles - all season - in one call
========================================

**Author :**
Robin Eudes

----------

> A simple python script to mux season subtitles, using mkvmerge.

---------- 

How to use it
----------
    Usage : mux.py [options]
    -d [--directory] <path to directory containing srt subtitles and mkv videos>
    Note: Double quotes arond the path are recommanded, to avoid any troubles with spaces.
    -h [--help] will print this help

Exemple
-------
    $>mux.py -d "C:\TV\my_serie_season"
    C:\TV\my_serie_season_vostfr created
    mkvmerge v8.9.0 ('Father Daughter') 64bit
    'C:\TV\my_serie_season\my_episode_n.mkv': Using the demultiplexer for the format 'Matroska'.
    'C:\TV\my_serie_season\subtitle_n.srt': Using the demultiplexer for the format 'SRT subtitles'.
    'C:\TV\my_serie_season\my_episode_n.mkv' track 0: Using the output module for the format 'AVC/h.264'.
    'C:\TV\my_serie_season\my_episode_n.mkv' track 1: Using the output module for the format 'AC-3'.
    'C:\TV\my_serie_season\my_episode_n.mkv' track 2: Using the output module for the format 'text subtitles'.
    'C:\TV\my_serie_season\subtitle_n.srt' track 0: Using the output module for the format 'text subtitles'.
    The file 'C:\TV\my_serie_season_vostfr\my_episode_n_vostfr.mkv' has been opened for writing.
    Progress: 100%
    The cue entries (the index) are being written...
    Muxing took 23 seconds.

    C:\TV
    ├───my_serie_season
    │   ├───my_episode_n.mkv
    │   └───subtitle_n.srt
    │
    └───my_serie_season_vostfr
    	└───my_episode_n_vostfr.mkv
Links
-------
[mkvmerge documentation](https://mkvtoolnix.download/doc/mkvmerge.html)

License
-------
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.fr.html)