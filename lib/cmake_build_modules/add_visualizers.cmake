message(STATUS "Adding target_sources() in add_visualizers.cmake")
target_sources(my::lib INTERFACE ${CMAKE_CURRENT_LIST_DIR}/../visualizers/my/lib.natvis)
