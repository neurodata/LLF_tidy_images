
#find ./big12_ORIGINAL/Cars -regex ".*\(jpg\)" -exec identify {} \; | awk '{print $3}' | sed "s/x/,"

find ../big12_ORIGINAL/Cars -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./Cars_sizes.csv
find ../big12_ORIGINAL/101_ObjectCategories -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./101_Object_sizes.csv
find ../big12_ORIGINAL/fgvc-aircraft-2013b -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./fgvc_sizes.csv
find ../big12_ORIGINAL/Pets -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./Pets_sizes.csv
find ../big12_ORIGINAL/birdsnap -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./birdsnap_sizes.csv
find ../big12_ORIGINAL/Flowers -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./Flowers_sizes.csv
find ../big12_ORIGINAL/SUN397 -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./SUN397_sizes.csv
find ../big12_ORIGINAL/dtd -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./dtd_sizes.csv
find ../big12_ORIGINAL/food-101 -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./food101_sizes.csv
find ../big12_ORIGINAL/VOCdevkit -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $3}' | sed "s/x/,/" > ./VOCdevkit_sizes.csv
