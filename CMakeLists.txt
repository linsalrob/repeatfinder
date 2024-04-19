cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX VERSION ${SKBUILD_PROJECT_VERSION})

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

python_add_library(PyRepeatFinder MODULE src/repeatFinder.cpp WITH_SOABI)

install(TARGETS PyRepeatFinder DESTINATION .)
