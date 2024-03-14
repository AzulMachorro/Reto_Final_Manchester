// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msgs_clase:msg/Sphere.idl
// generated code does not contain a copyright notice

#ifndef MSGS_CLASE__MSG__DETAIL__SPHERE__BUILDER_HPP_
#define MSGS_CLASE__MSG__DETAIL__SPHERE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msgs_clase/msg/detail/sphere__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msgs_clase
{

namespace msg
{

namespace builder
{

class Init_Sphere_radius
{
public:
  explicit Init_Sphere_radius(::msgs_clase::msg::Sphere & msg)
  : msg_(msg)
  {}
  ::msgs_clase::msg::Sphere radius(::msgs_clase::msg::Sphere::_radius_type arg)
  {
    msg_.radius = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msgs_clase::msg::Sphere msg_;
};

class Init_Sphere_center
{
public:
  Init_Sphere_center()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Sphere_radius center(::msgs_clase::msg::Sphere::_center_type arg)
  {
    msg_.center = std::move(arg);
    return Init_Sphere_radius(msg_);
  }

private:
  ::msgs_clase::msg::Sphere msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::msgs_clase::msg::Sphere>()
{
  return msgs_clase::msg::builder::Init_Sphere_center();
}

}  // namespace msgs_clase

#endif  // MSGS_CLASE__MSG__DETAIL__SPHERE__BUILDER_HPP_
