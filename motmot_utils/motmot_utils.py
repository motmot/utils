import os, sys, datetime
import subprocess # subprocess module included with python2.4, but should also be in current directory

def under_svn_control(path):
    version = get_svnversion(path)
    if version == 'exported':
        return False
    return True

def get_svnversion_persistent(store_path,version_str):
    svnversion = get_svnversion()
    save_version = True
    if svnversion == 'exported':
        save_version = False
        g={};l={}
        execfile(store_path,g,l)
        svnversion = l['__svnrev__'] # read from version file
        
    version = version_str%{'svnversion':svnversion}
    
    if save_version:
        fd = open(store_path,'wb')
        fd.write('#automatically generated on %s\n'%datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000"))
        fd.write('__svnrev__="%s"\n'%svnversion)
        fd.write('__version__="%s"\n'%version)
        fd.close()
    return version
    
def get_svnversion(path=None):
    if path is None:
        path = os.path.abspath(os.curdir)
    if sys.platform.startswith('win'):
        prog=r'C:\Program Files\Subversion\bin\svnversion.exe'
    else:
        # XXX should really search PATH for svnversion
        prog='/usr/bin/svnversion'
        if not os.path.exists(prog):
            prog='/usr/local/bin/svnversion'

    if not os.path.exists(prog):
        if os.path.exists( os.path.join(path,'.svn') ):
            import warnings
            warnings.warn("No svnversion program found at %s, pretending svnversion=1"%prog)
            return "1"
        else:
            return "exported"
    args = [prog,'-n','-c',path] # no newline, commited only
    #print ' '.join(args)
    res = subprocess.Popen(args,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           )
    if res.wait():
        errstr = res.stderr.read().strip()
        if errstr.endswith('not versioned, and not exported'):
            return 'not versioned, and not exported'
        raise RuntimeError('"%s" returned error: "%s"'%(' '.join(args),errstr))
                                                        
    val = res.stdout.read()
    colon_idx = val.find(':')
    if colon_idx != -1:
        val = val[colon_idx+1:]
    if val.endswith('M'):
        val = val[:-1]
    if val.endswith('S'):
        val = val[:-1]
    return val

def main():
    print 'SVN version:',get_svnversion()

if __name__=='__main__':
    main()
