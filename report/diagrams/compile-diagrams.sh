for filename in *.svg
do
    output=$(basename $filename ".svg")
    echo $output
    inkscape $filename --export-png="$output.png"
done