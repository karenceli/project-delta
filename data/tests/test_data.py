from __future__ import absolute_import, division, print_function

import os, tempfile, urllib

from .. import data


def test_check_hashes():
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(b'Some data')
        temp.flush()
        fname = temp.name
        d = {fname: "5b82f8bf4df2bfb0e66ccaa7306fd024"}
        assert data.check_hashes(d)
        d = {fname: "4b82f8bf4df2bfb0e66ccaa7306fd024"}
        assert not data.check_hashes(d)

def test_make_hash_dict():
    l = "http://www.jarrodmillman.com/rcsds/_downloads/ds107_sub001_highres.nii"
    urllib.request.urlretrieve(l, filename = "ds107_sub001_highres.nii")
    hash_O = data.make_hash_dict(".")["./ds107_sub001_highres.nii"]
    hash_E = "fd733636ae8abe8f0ffbfadedd23896c"
    assert hash_O == hash_E
    os.remove("ds107_sub001_highres.nii")