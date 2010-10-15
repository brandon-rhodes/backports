# -*- coding: utf-8 -*-
from distutils.core import setup
setup(name='backports',
      version='1.0',
      description='Namespace for backported Python features',
      long_description=u"""\
A few minutes ago,
my fingers were poised for a moment above the keyboard
as I prepared to backport the essential ``match_hostname()`` function
(without which the Secure Sockets Layer is not actually *secure!*)
from the Python 3.2 version of the ``ssl`` Standard Library
to earlier versions of Python.
Suddenly, I paused: what would I call the new distribution
that I created in the Package Index to hold this small function?

It seemed a shame to consume an entire top-level name
in the Package Index for what is, after all, a stopgap measure
until older versions of Python are one day retired.

And so I conceived this ``backports`` namespace package.
It reserves a namespace beneath which we can happy place
all of the various features that we want to cut-and-paste
from later Python versions.
I hope that this will provide two benefits:

1. It should provide greater sanity, and a bit more organization,
   in the Package Index.

2. When you are ready to port a Python application
   to a new version of Python,
   you can search the code for any ``import`` statements
   that name a ``backports`` package,
   and remove the backports for features that have now “arrived”
   in the version of Python to which you are upgrading.

I have considered calling for all ``backports`` packages
to issue a warning upon import if they detect that they are
running under a version of Python that has now gained the feature
they offer, but I think that will be unkind to actual users,
since the most widespread versions of Python today still
display warnings by default.

An issue on which I am undecided is whether a ``backports`` package,
if it finds itself on a modern enough version of Python,
should simply import the “real” version of its feature
from the Standard Library instead of offering the replacement.
My guess is that this is *not* a good idea,
because if — for some reason — an incompatibility crops up
bewteen the tweaked code in a backport
and the official code in the modern Standard Library,
then it would be nice for developers using the backport
to be faced with that breakage when they themselves
try removing the backport,
instead of being faced with it simply because a user
tries running their program on more modern version of Python.

""",
      author='Brandon Craig Rhodes',
      author_email='brandon@rhodesmill.org',
      url='http://bitbucket.org/brandon/backports',
      packages=['backports'],
      )
