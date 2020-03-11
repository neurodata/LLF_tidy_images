
for f in ../datasets_ORIGINAL/*; do
    find $f -type f -regex ".*\(jpg\)" | head -50 | xargs cp -t ../datasets_tmp/
done
