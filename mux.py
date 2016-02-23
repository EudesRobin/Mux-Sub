#!/usr/bin/python
# -*- coding: utf-8 -*-

def mux(dir,mkvmerge):
    import glob, os, re, sys
    
    if os.path.isdir(dir):
        sub = sorted(glob.glob(os.path.join(dir,"*.srt")),key=str.lower)
        vid = sorted(glob.glob(os.path.join(dir,"*.mkv")),key=str.lower)
        
        # check if the directory contains the right files
        if len(sub)!=len(vid):
            print('missing subtitle or video file')
            sys.exit(1)
            
        # we are ready to mux theses files
        else:
            # output dir name
            result = re.split('([S][0-9]{1,2}.)+',os.path.basename(dir),flags=re.IGNORECASE)
            if len(result)!=3:
                print('Regex fail to split folder name in 3 parts : title_serie - saison - tech/team ')
                return sys.exit(1)
                
            outputdir = os.path.join(os.path.dirname(dir),result[0]+result[1]+'VOSTFR.'+result[2])
            
            # creation output dir
            if not os.path.exists(outputdir):
                os.makedirs(outputdir)
                print(outputdir +' created')
            else:
                print(outputdir+' already existing')
            
            # we can proceed...
            for itemvid,itemsub in zip(vid,sub):
                # output file name 
                result = re.split('([S][0-9]{1,2}[E][0-9]{1,2}.)+',os.path.basename(itemvid),flags=re.IGNORECASE)
                if len(result)!=3:
                    print('Regex fail to split video filename in 3 parts : title_serie - saison - tech/team ')
                    sys.exit(1)
               
                outputfile = os.path.join(outputdir,result[0]+result[1]+'VOSTFR.'+result[2])
                
                # mux
                if os.path.exists(outputfile):
                    print(os.path.basename(outputfile)+' skipped, already existing')
                else:
                    opt_original = '--no-global-tags'
                    opt_sub= '--language 0:fre --default-track 0:yes'
                    os.system(mkvmerge+' --output'+' "'+outputfile+'" '+opt_original+' "'+itemvid+'" '+opt_sub+' "'+itemsub+'" ')
                    
            return 0
    else:
        print("the submited path is not a directory")
        return sys.exit(1)

        
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
            os.system('python mux.py -h')
            sys.exit(0)
    except getopt.GetoptError:
        os.system('python mux.py -h')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print('Usage : mux.py [options]\n-d [--directory] <path to directory containing srt subtitles and mkv videos>\nNote: Double quotes arond the path are recommanded, to avoid any troubles with spaces.\n-h [--help] will print this help')
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

