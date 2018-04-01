rm -rf -r release
mkdir release
cd release
export DYLD_LIBRARY_PATH="$PWD/../apriltag_lib":"$DYLD_LIBRARY_PATH"
cmake ..
make
./tag