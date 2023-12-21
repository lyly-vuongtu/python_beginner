
cmake_minimum_required(VERSION 3.12)
project(my_project)

add_subdirectory(path/to/pybind11)
add_executable(my_executable src/main.cpp)

target_link_libraries(my_executable PRIVATE pybind11::module)