#!/bin/bash

if [ $# -eq 0 ]; then 
    python /usr/src/mux-mkv_srt/mux.py -d /usr/src/mux-mkv_srt/source/*
else
    echo $@
    python /usr/src/mux-mkv_srt/mux.py $@ 
fi
