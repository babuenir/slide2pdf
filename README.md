# slide2pdf

slide2pdf is a command line tool to convert html slide presenation to portable 
document format (pdf).

### Installation

1. `git clone git@github.com:babuenir/slide2pdf.git`
2. `cd slide2pdf`
3. `python setup.py install`

or

```
  $ pip install slide2pdf
```

**Note**: Before installing this package please make sure that you have already 
installed **xdotool** _else_ install xdotool using `apt-get install xdotool`.

### Usage

```
  $ slide2pdf (-u <url>) [--height=<n>] [--width=<n>]

    Options:
      -h --help                show help
      -u --url URL             file-url path
      --height=<n>             window height [default: 1600]
      --width=<n>              window width [default: 1200]

  $ slide2pdf -u "file:///path/to/file.html"
```

### Reference
[https://www.youtube.com/watch?v=0KQcBa7X7zI&feature=youtu.be](https://www.youtube.com/watch?v=0KQcBa7X7zI&feature=youtu.be)

### License
MIT
