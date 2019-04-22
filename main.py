import os

# Constants.
out_format = ".mp4"

# Builds the convert portion of "script.sh".
def build_convert():
  result = ""
  beginning = "ffmpeg -i"
  in_path = "convert/in/"
  out_path = "convert/out/"
  files = os.listdir(in_path)
  files.reverse()
  line = ""
  for filename in files:
    line = beginning+" "+in_path+filename+" "+out_path+filename+out_format
    result = result+line+"\n"
  return(result)

# Builds "merge_list.txt". Returns True if there are files to merge.
def build_merge():
  merge_list = open("merge_list.txt", "w")
  in_path = "merge/in/"
  files = os.listdir(in_path)
  files.reverse()
  result = ""
  for filename in files:
    result = result+"file \'"+in_path+filename+"\'\n"
  merge_list.write(result)
  merge_list.close()
  if(len(files) < 2):
    print("Please supply at least two video files in "+in_path+".")
    return(False)
  else:
    return(True)

# Builds "script.sh" based on the contents of "convert/in" and "merge/in".
def build_script_sh():
  convert = build_convert()
  if(build_merge()):
    merge = "ffmpeg -f concat -i merge_list.txt -c copy merge/out/out.mp4"
  else:
    merge = ""
  result = convert+"\n"+merge
  script = open("script.sh", "w")
  script.write(result)
  script.close()

# Ronseal.
def run():
  build_script_sh()
  os.system("./script.sh")

# Run.
run()
