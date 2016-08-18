## bash scripts

Flatten file structure and prepend directory names to file name:

`$ find */ -type f -exec bash -c 'file=${1#./}; mv "$file" "${file//\//_}"' _ '{}' \;`

Create thumbnails from videos - ffmpeg script - create a thumbs directory and run from there:

`for file in ../*.mp4; do filename=$(basename "$file"); filename=${filename%.*}; ffmpeg -i "$file" -ss 3 -vf "select=gt(scene\,0.4),scale=iw*min(256/iw\,256/ih):ih*min(256/iw\,256/ih), pad=256:256:(256-iw*min(256/iw\,256/ih))/2:(256-ih*min(256/iw\,256/ih))/2" -frames:v 5 -vsync vfr "${filename}_thumb_%02d.jpg"; if [ ! -f $filename"_thumb"01.jpg” ]; then ffmpeg -i $file -ss 3 -vf "thumbnail,scale=iw*min(256/iw\,256/ih):ih*min(256/iw\,256/ih), pad=256:256:(256-iw*min(256/iw\,256/ih))/2:(256-ih*min(256/iw\,256/ih))/2" -frames:v 1 "${filename}_thumb_01.jpg" -n; fi; done`
