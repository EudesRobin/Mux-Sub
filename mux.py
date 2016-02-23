#!/usr/bin/python
# -*- coding: utf-8 -*-

def mux(dir,mkvmerge):
    import glob, os
    
    if os.path.isdir(dir):
        sub = sorted(glob.glob(os.path.join(dir,"*.srt")),key=str.lower)
        vid = sorted(glob.glob(os.path.join(dir,"*.mkv")),key=str.lower)
        
        # check if the directory contains the right files
        if len(sub)!=len(vid):
            print('missing subtitle or video file')
            sys.exit(1)
            
        # we are ready to mux theses files
        else:

            if not os.path.exists(dir+'_vostfr'):
                os.makedirs(dir+'_vostfr')
            else:
                print(dir+'_vostfr already existing')
            
            for itemvid,itemsub in zip(vid,sub):
                output_filepath = os.path.join(dir+'_vostfr',os.path.splitext(os.path.basename(itemvid))[0]+'_vostfr.mkv')
                if os.path.exists(output_filepath):
                    print(os.path.basename(output_filepath)+' skipped, already existing')
                else:
                    opt_original = '--no-global-tags'
                    opt_sub= '--language 0:fre --default-track 0:yes'
                    os.system(mkvmerge+' --output'+' "'+output_filepath+'" '+opt_original+' "'+itemvid+'" '+opt_sub+' "'+itemsub+'" ')
                    
            return 0
    else:
        print("the submited path is not a directory")
        return system.exit(1)

        
# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python/377028#377028
# Test if executable exists in Path
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

if __name__ == "__main__":
    import sys, getopt, os

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hd:",["--directory"])
        if len(sys.argv)==1:
            print('Usage :\nmux.py -d <directory containing subtitles and mkv videos>')
            sys.exit(0)
    except getopt.GetoptError:
        print('mux.py -d <directory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('mux.py -d <directory containing subtitles and mkv videos>')
            sys.exit()
        elif opt in ("-d", "--directory"):
            # define which executable call...
            executable = {'nt' : "mkvmerge.exe",
                       'posix' : "mkvmerge",
            }
            mkvmerge = executable[os.name]
            
            if which(mkvmerge) is None:
                print('mkvmerge executable not found in your path')
                sys.exit(1)
            else:
                mux(os.path.normpath(arg),mkvmerge)
            
	# end arg loop

