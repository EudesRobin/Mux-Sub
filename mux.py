#!/usr/bin/python
# -*- coding: utf-8 -*-

# Global imports
import os, sys

def mux(dir,mkvmerge):
    import glob, re, subprocess
    
    if os.path.isdir(dir):
        sub = []
        sub.extend(glob.glob(os.path.join(dir,"*.srt")))
        sub.extend(glob.glob(os.path.join(dir,"*.ass")))
        sub = sorted(sub,key=str.lower)
        
        vid = []
        vid.extend(glob.glob(os.path.join(dir,"*.mkv")))
        vid.extend(glob.glob(os.path.join(dir,"*.mp4")))
        vid.extend(glob.glob(os.path.join(dir,"*.avi")))
        vid.extend(glob.glob(os.path.join(dir,"*.ts")))
        vid = sorted(vid,key=str.lower)
        
        # check if the directory contains the right files
        if len(sub)!=len(vid):
            uprint('missing subtitle or video file')
            sys.exit(1)
        
        # we are ready to mux theses files
        else:
            # output dir name
            outputdirwithdot = re.sub(' ', '.', os.path.basename(dir))  
            resultsplit = re.split('([S][0-9]{1,2}.)+',outputdirwithdot,flags=re.IGNORECASE)
            if len(resultsplit)!=3:
                uprint('Regex fail to split folder name in 3 parts : title_serie - saison - tech/team ')
                return sys.exit(1)
            
            outputdir = os.path.join(os.path.dirname(dir),resultsplit[0]+resultsplit[1]+'VOSTFR.'+resultsplit[2])
            
            # creation output dir
            if not os.path.exists(outputdir):
                os.makedirs(outputdir)
                uprint(outputdir +' created')
            else:
                uprint(outputdir+' already existing')
            
            # a simple log file 
            log = open(os.path.join(outputdir,"log.txt"),'a')
            # we can proceed...
            for itemvid,itemsub in zip(vid,sub):
                # output file name
                resultwithdot = re.sub('\s', '.', os.path.basename(itemvid)) 
                resultsplit = re.split('([S][0-9]{1,2}[E][0-9]{1,2}.)+',resultwithdot,flags=re.IGNORECASE)
                if len(resultsplit)!=3:
                    uprint('Regex fail to split video filename in 3 parts : title_serie - saison/episode - tech/team ')
                    sys.exit(1)
                
                outputfile = os.path.splitext(os.path.join(outputdir,resultsplit[0]+resultsplit[1]+'VOSTFR.'+resultsplit[2]))[0]+'.mkv'
                
                # mux
                if os.path.exists(outputfile):
                    uprint(os.path.basename(outputfile)+' skipped, already existing')
                else:
                    opt_original = '--no-global-tags'
                    opt_sub= '--language 0:fre --default-track 0:yes'
                    uprint('working on '+outputfile)
                    result = subprocess.check_output(mkvmerge+' --output'+' "'+outputfile+'" '+opt_original+' "'+itemvid+'" '+opt_sub+' "'+itemsub+'" ', shell=True, stderr=subprocess.STDOUT)
                    clean_res = re.sub('(Progress: [0-9]{1,2}%(\r\n|\r|\n))|(\r)|(^\n$)', '', result.decode("utf-8"))
                    uprint(clean_res,file=log)
                    
            log.close()    
            return 0
    else:
        uprint("the submited path is not a directory")
        return sys.exit(1)

        
# https://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined/29988426#29988426
# to avoid UnicodeEncodeError with windows terminal...
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='replace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

        
# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python/377028#377028
# Test if executable exists in Path
def which(program):
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
    import getopt

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
                uprint('mkvmerge executable not found in your path')
                sys.exit(1)
            else:
                mux(os.path.normpath(arg),mkvmerge)
            
	# end arg loop

