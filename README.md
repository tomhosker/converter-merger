# Converter-Merger

This is a facility for converting and/or merging video files *in bulk*, using FFmpeg (and a bit of Python).

## Getting Started

### Installation

One will need to have FFmpeg and Python -- Python2 seems to be sufficient -- in order run the code here properly.

### Running

Place the files to be converted in `.../converter-merger/convert/in` and those to be merged in `.../converter-merger/merge/in`. Then run the program using `python main.py`.

You should then find the converted files in `.../converter-merger/convert/out` and the merged video at `.../converter-merger/merge/out/out.mp4`.

## Known Issues

While perfectly safe -- any input files are untouched -- the merger portion of this facility can produced unpredictable, particularly when said input files are in different aspect ratios, etc.
