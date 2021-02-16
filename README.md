Introduction
------------

Sowsbetter is a script which automatically transcodes and uploads these
files to bemaniso.ws. 

The following command will scan through every FLAC you have ever
downloaded or uploaded (if it is in , determine which formats are needed, transcode
the FLAC to each needed format, and upload each format to bemaniso -- automatically.

    $ ./sowsbetter

Installation
------------

You're going to need to install a few dependencies before using
sowsbetter.

First and foremost, you will need Python 3.6 or newer.

Once you've got Python installed, you will need a few modules: mechanize,
mutagen, and requests. Try this:

    $ sudo pip3 install -r requirements.txt

	
If you are on a seedbox, or a system without root priviliages, try this:


    $ pip3 install --user -r requirements.txt


Furthermore, you need several external programs: mktorrent 1.1+, flac,
lame, and sox. The method of installing these programs varies
depending on your operating system, but if you're using something like
Ubuntu you can do this:

    # sudo aptitude install mktorrent flac lame sox
	

If you are on a seedbox and you lack the privilages to install packages,
you could contact your provider to have these packages installed.

At this point you may execute the following command:

    $ ./sowsbetter

And you will receive a notification stating that you should edit the
configuration file \~/.sowsbetter/config (if you're lucky).

Configuration
-------------

Open up the file `\~/.sowsbetter/config` in vim with `vim \~/.sowsbetter/config` . You're going to see something
like this:

    [bemaniso]
    username =
    password = 
    data_dir =
    output_dir =
    torrent_dir =
    formats = flac, v0, 320 
    media = sacd, soundboard, web, dvd, cd, dat, vinyl, blu-ray
    24bit_behaviour = 0
    tracker = https://bemaniso.ws:34443/
    api = https://bemaniso.ws
    mode = both
    source = SOWS
Press `ins` to edit it.
`username` and `password` are your bemaniso login credentials. 

`data_dir` is the directory where your downloads are stored. If you are using WSL use `/mnt/[drive letter]/[path to folder]`. 

`output_dir` is the directory where your transcodes will be created. If
the value is blank, `data_dir` will be used. You can also specify
per format values such as `output_dir_320` or `output_dir_v0`.

`torrent_dir` is the directory where torrents should be created (e.g.,
your watch directory). Same per format settings as output_dir apply.

`formats` is a list of formats that you'd like to support


`media` is a list of lossless media types you want to consider for
transcoding. The default value is all What.CD lossless formats, but if
you want to transcode only CD and vinyl media, for example, you would
set this to 'cd, vinyl'.

`24bit_behaviour` defines what happens when the program encounters a FLAC 
that it thinks is 24bits. If it is set to '2', every FLAC that has a bits-
per-sample property of 24 will be silently re-categorized. If it set to '1',
a prompt will appear. The default is '0' which ignores these occurrences.

`tracker` is the base url to use in the torrent files.

`api` is the base url to use for api requests.

`mode` is which list of torrents to search for candidates. One of:

 - `snatched` - Your snatched torrents.
 - `uploaded` - Your uploaded torrents.
 - `both`     - Your uploaded and snatched torrents.
 - `seeding`  - Better.php for your seeding torrents.
 - `all`      - All transcode sources above.
 - `none`     - Disable scraping.

 `source` is the source flag to put on created torrents, leave blank if you're
 running mktorrent 1.0.

You should end up with something like this:

    [bemaniso]
    username = User
    password = Pass123
    data_dir = /srv/downloads
    output_dir = /svr/output
    torrent_dir = /srv/torrents
    formats = flac, v0, 320
    media = cd, vinyl, web
    24bit_behaviour = 0
    tracker = https://bemaniso.ws:34443/
    api = https://bemaniso.ws
    mode = both
    source = SOWS

Press `esc`and type `:wq` to save and quit.   
Alright! Now you're ready to use sowsbetter.

Usage
-----

```
usage: sowsbetter [-h] [-s] [-j THREADS] [--config CONFIG] [--cache CACHE]
                     [-U] [-E] [--version] [-m MODE] [-S] [-t TOTP]
                     [-o SOURCE]
                     [release_urls [release_urls ...]]

positional arguments:
  release_urls          the URL where the release is located (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -s, --single          only add one format per release (useful for getting
                        unique groups) (default: False)
  -j THREADS, --threads THREADS
                        number of threads to use when transcoding (default: 7)
  --config CONFIG       the location of the configuration file (default:
                        ~/.sowsbetter/config)
  --cache CACHE         the location of the cache (default:
                        ~/.sowsbetter/cache)
  -U, --no-upload       don't upload new torrents (in case you want to do it
                        manually) (default: False)
  -E, --no-24bit-edit   don't try to edit 24-bit torrents mistakenly labeled
                        as 16-bit (default: False)
  --version             show program's version number and exit
  -m MODE, --mode MODE  mode to search for transcode candidates; snatched,
                        uploaded, both, seeding, or all (default: None)
  -S, --skip            treats a torrent as already processed (default: False)
  -t TOTP, --totp TOTP  time based one time password for 2FA (default: None)
  -o SOURCE, --source SOURCE
                        the value to put in the source flag in created
                        torrents (default: None)
```

Examples
--------

To transcode and upload every snatch you've ever downloaded along with all
your uploads (this may take a while):

    $ ./sowsbetter

To transcode and upload a specific release (provided you have already
downloaded the FLAC and it is located in your `data_dir`):

    $ ./sowsbetter https://bemaniso.ws/torrents.php?id=1000\&torrentid=1000000

Note that if you specify a particular release(s), sowsbetter will
ignore your configuration's media types and attempt to transcode the
releases you have specified regardless of their media type (so long as
they are lossless types).

Your first time running sowsbetter might take a while, but after it has
successfully gone through and checked everything, it'll go faster any
consecutive runs due to its caching method.

Troubleshooting
---------------
If you keep getting errors about incorrect/unacceptable tags, editi tagging.py and replace 
 ```if check_tracknumber_format:
        tracknumber = info['tracknumber'][0]
        if not valid_fractional_tag(tracknumber):
            return (False, '"%s" has a malformed tracknumber tag ("%s")' % (filename, tracknumber))
```
with


```#if check_tracknumber_format:
        #tracknumber = info['tracknumber'][0]
        #if not valid_fractional_tag(tracknumber):
            #return (False, '"%s" has a malformed tracknumber tag ("%s")' % (filename, tracknumber))
```	    


