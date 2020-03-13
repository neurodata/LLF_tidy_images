
for f in ../datasets_tmpORIGINAL/*; do
    find $f -type f -regex ".*\(jpg\)" | head -50 | xargs  cp -t ../datasets_check/
done
