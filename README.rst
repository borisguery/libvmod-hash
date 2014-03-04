============
vmod_hash
============

----------------------
Varnish Hash Module
----------------------

:Author: Boris Guéry
:Date: 2014-03-04
:Version: 1.0
:Manual section: 3

SYNOPSIS
========

import hash;

DESCRIPTION
===========

Easily retrieve `req.hash`

FUNCTIONS
=========

get_req_hash
-----

Prototype
        ::

                get_req_hash()
Return value
	STRING
Description
	Returns hash from previous `hash_data()` calls
Example
        ::

                set resp.http.X-Req-Hash = hash.get_req_hash();

INSTALLATION
============

The source tree is based on autotools to configure the building, and
does also have the necessary bits in place to do functional unit tests
using the varnishtest tool.

Make sure you have the according varnish source, on debian/ubuntu it may be retrieved
by running: `apt-get source varnish` (make sure you have added source repository in your `source.list`


Usage::

 ./autogen.sh
 ./configure VARNISHSRC=DIR [VMODDIR=DIR]

`VARNISHSRC` is the directory of the Varnish source tree for which to
compile your vmod. Both the `VARNISHSRC` and `VARNISHSRC/include`
will be added to the include search paths for your module.

Optionally you can also set the vmod install directory by adding
`VMODDIR=DIR` (defaults to the pkg-config discovered directory from your
Varnish installation).

Make targets:

* make         - builds the vmod
* make install - installs your vmod in `VMODDIR`
* make check   - runs the unit tests in ``src/tests/*.vtc``

In your VCL you could then use this vmod along the following lines::
        
        import hash;

        sub vcl_deliver {
                set resp.http.X-Req-Hash = hash.get_req_hash();
        }

COPYRIGHT
=========

This document is licensed under the same license as the
libvmod-hash project. See LICENSE for details.

* Copyright (c) 2014 Boris Guéry
