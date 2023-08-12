cmake_minimum_required(VERSION 3.16 FATAL_ERROR)
project(cpp_yolo)

set(tf_DIR  /usr/local/include/tensorflow)
set(Torch_DIR /home/erdem/libtorch)
# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}  -std=c++11 -lm -ldl" )

find_package(ament_cmake REQUIRED)
# find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(Torch REQUIRED)


add_executable(cpp_yolo src/main.cpp)
target_link_libraries( cpp_yolo "${TORCH_LIBRARIES}" ${OpenCV_LIBS} )

set_property(TARGET cpp_yolo PROPERTY CXX_STANDARD 17)
ament_target_dependencies(cpp_yolo rclcpp std_msgs  sensor_msgs) 
ament_export_dependencies(Torch)


if(BUILD_TESTING)
  #file(GLOB TORCH_DLLS "${TORCH_INSTALL_PREFIX}/lib/*.dll")
  find_package(ament_lint_auto REQUIRED)

  ament_lint_auto_find_test_dependencies()
endif()
install(TARGETS
  cpp_yolo
  DESTINATION lib/${PROJECT_NAME})

ament_package()
