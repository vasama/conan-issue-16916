cmake_minimum_required(VERSION 3.24)
project(app)

find_package(my-lib REQUIRED)
add_executable(app main.cpp)
target_link_libraries(app PRIVATE my::lib)
