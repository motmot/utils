#################################################################################

# The contents of this file were originally taken from
# matplotlib. This original cod is reproduced and redistributed with
# fview under the terms of matplotlib's license.  This is the
# matplotlib license:

matplotlib_license = """

LICENSE AGREEMENT FOR MATPLOTLIB 0.90
--------------------------------------

1. This LICENSE AGREEMENT is between John D. Hunter ("JDH"), and the
Individual or Organization ("Licensee") accessing and otherwise using
matplotlib software in source or binary form and its associated
documentation.

2. Subject to the terms and conditions of this License Agreement, JDH
hereby grants Licensee a nonexclusive, royalty-free, world-wide license
to reproduce, analyze, test, perform and/or display publicly, prepare
derivative works, distribute, and otherwise use matplotlib 0.90
alone or in any derivative version, provided, however, that JDH's
License Agreement and JDH's notice of copyright, i.e., "Copyright (c)
2002-2005 John D. Hunter; All Rights Reserved" are retained in
matplotlib 0.90 alone or in any derivative version prepared by
Licensee.

3. In the event Licensee prepares a derivative work that is based on or
incorporates matplotlib 0.90 or any part thereof, and wants to
make the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to matplotlib 0.90.

4. JDH is making matplotlib 0.90 available to Licensee on an "AS
IS" basis.  JDH MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, JDH MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB 0.90
WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. JDH SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
0.90 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
MATPLOTLIB 0.90, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
relationship of agency, partnership, or joint venture between JDH and
Licensee.  This License Agreement does not grant permission to use JDH
trademarks or trade name in a trademark sense to endorse or promote
products or services of Licensee, or any third party.

8. By copying, installing or otherwise using matplotlib 0.90,
Licensee agrees to be bound by the terms and conditions of this License
Agreement.
"""

#################################################################################

import os, tempfile, pprint, warnings

def get_home():
    """Find user's home directory if possible.
    Otherwise raise error.

    :see:  http://mail.python.org/pipermail/python-list/2005-February/263921.html
    """
    path=''
    try:
        path=os.path.expanduser("~")
    except:
        pass
    if not os.path.isdir(path):
        for evar in ('HOME', 'USERPROFILE', 'TMP'):
            try:
                path = os.environ[evar]
                if os.path.isdir(path):
                    break
            except: pass
    if path:
        return path
    else:
        raise RuntimeError('please define environment variable $HOME')

def _is_writable_dir(p):
    """
    p is a string pointing to a putative writable dir -- return True p
    is such a string, else False
    """
    try: p + ''  # test is string like
    except TypeError: return False
    try:
        t = tempfile.TemporaryFile(dir=p)
        t.write('1')
        t.close()
    except OSError: return False
    else: return True

def get_configdir(dirname=None):
    """
    Return the string representing the configuration dir.  If it is the
    special string _default_, use $HOME/dirname.  s must be writable
    """
    h = get_home()
    if not _is_writable_dir(h):
        raise RuntimeError("'%s' is not a writable dir; you must set environment variable HOME to be a writable dir "%h)

    p = os.path.join(get_home(), dirname)

    if not _is_writable_dir(p):
        os.mkdir(p)

    return p

def rc_fname(must_already_exist=True,
             filename=None,
             dirname=None):
    """
    Return the path to the rc file

    Search order:

     * current working dir/filename
     * environ var $FILENAME/filename
     * $HOME/dirname/filename

    Standard naming convention:

     filename = 'yourapprc'
     dirname = '.yourapp'

    """

    home = get_home()

    fname = os.path.join( os.getcwd(), filename)
    if os.path.exists(fname): return fname

    if os.environ.has_key(filename.upper()):
        path =  os.environ[filename.upper()]
        if os.path.exists(path):
            fname = os.path.join(path, filename)
            if os.path.exists(fname):
                return fname

    fname = os.path.join(get_configdir(dirname), filename)
    if os.path.exists(fname):
        return fname
    
    if must_already_exist:
        return None
    else:
        return fname

def get_rc_params(fname,defaultParams):
    if fname is None or not os.path.exists(fname):
        message = 'could not find rc file; returning defaults'
        ret =  dict([ (key, val) for key, val in defaultParams.items()])
        warnings.warn(message)
        return ret
    fd = open(fname,'r')
    fcontents = fd.read()
    fd.close()
    defaults = defaultParams.copy()
    nl = eval(fcontents)
    defaults.update(nl)
    return defaults

def save_rc_params(fname,rc_params):
    fd = open(fname,'w')
    pprint.pprint(rc_params,fd)
