ffmpeg -i convert/in/sample.wmv convert/out/sample.wmv.mp4

ffmpeg -f concat -i merge_list.txt -c copy merge/out/out.mp4