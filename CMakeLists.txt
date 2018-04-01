cmake_minimum_required(VERSION 3.1.0)
project(tag)
set (CMAKE_CXX_STANDARD 11)
include_directories(apriltag_lib)
file(GLOB SOURCES apriltag/main.cpp)
link_directories(apriltag_lib)
find_package(OpenCV REQUIRED)
add_executable(tag ${SOURCES}) 
target_link_libraries(tag ${OpenCV_LIBS} apriltag)

# for mac add 
# export DYLD_LIBRARY_PATH="your lib directory path":"$DYLD_LIBRARY_PATH"
# in bashrc
