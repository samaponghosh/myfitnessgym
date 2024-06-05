# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/gesture_recognizer/proto/gesture_recognizer_graph_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2
from mediapipe.tasks.cc.vision.gesture_recognizer.proto import hand_gesture_recognizer_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_gesture__recognizer_dot_proto_dot_hand__gesture__recognizer__graph__options__pb2
from mediapipe.tasks.cc.vision.hand_landmarker.proto import hand_landmarker_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__landmarker_dot_proto_dot_hand__landmarker__graph__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/vision/gesture_recognizer/proto/gesture_recognizer_graph_options.proto',
  package='mediapipe.tasks.vision.gesture_recognizer.proto',
  syntax='proto2',
  serialized_pb=_b('\nYmediapipe/tasks/cc/vision/gesture_recognizer/proto/gesture_recognizer_graph_options.proto\x12/mediapipe.tasks.vision.gesture_recognizer.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\x1a^mediapipe/tasks/cc/vision/gesture_recognizer/proto/hand_gesture_recognizer_graph_options.proto\x1aSmediapipe/tasks/cc/vision/hand_landmarker/proto/hand_landmarker_graph_options.proto\"\xd2\x03\n\x1dGestureRecognizerGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12o\n\x1dhand_landmarker_graph_options\x18\x02 \x01(\x0b\x32H.mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions\x12\x81\x01\n%hand_gesture_recognizer_graph_options\x18\x03 \x01(\x0b\x32R.mediapipe.tasks.vision.gesture_recognizer.proto.HandGestureRecognizerGraphOptions2}\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xde\xe1\xb9\xe4\x01 \x01(\x0b\x32N.mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptionsB_\n9com.google.mediapipe.tasks.vision.gesturerecognizer.protoB\"GestureRecognizerGraphOptionsProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_vision_dot_gesture__recognizer_dot_proto_dot_hand__gesture__recognizer__graph__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__landmarker_dot_proto_dot_hand__landmarker__graph__options__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GESTURERECOGNIZERGRAPHOPTIONS = _descriptor.Descriptor(
  name='GestureRecognizerGraphOptions',
  full_name='mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hand_landmarker_graph_options', full_name='mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptions.hand_landmarker_graph_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hand_gesture_recognizer_graph_options', full_name='mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptions.hand_gesture_recognizer_graph_options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptions.ext', index=0,
      number=479097054, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=924,
)

_GESTURERECOGNIZERGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
_GESTURERECOGNIZERGRAPHOPTIONS.fields_by_name['hand_landmarker_graph_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__landmarker_dot_proto_dot_hand__landmarker__graph__options__pb2._HANDLANDMARKERGRAPHOPTIONS
_GESTURERECOGNIZERGRAPHOPTIONS.fields_by_name['hand_gesture_recognizer_graph_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_vision_dot_gesture__recognizer_dot_proto_dot_hand__gesture__recognizer__graph__options__pb2._HANDGESTURERECOGNIZERGRAPHOPTIONS
DESCRIPTOR.message_types_by_name['GestureRecognizerGraphOptions'] = _GESTURERECOGNIZERGRAPHOPTIONS

GestureRecognizerGraphOptions = _reflection.GeneratedProtocolMessageType('GestureRecognizerGraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _GESTURERECOGNIZERGRAPHOPTIONS,
  __module__ = 'mediapipe.tasks.cc.vision.gesture_recognizer.proto.gesture_recognizer_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptions)
  ))
_sym_db.RegisterMessage(GestureRecognizerGraphOptions)

_GESTURERECOGNIZERGRAPHOPTIONS.extensions_by_name['ext'].message_type = _GESTURERECOGNIZERGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_GESTURERECOGNIZERGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n9com.google.mediapipe.tasks.vision.gesturerecognizer.protoB\"GestureRecognizerGraphOptionsProto'))
# @@protoc_insertion_point(module_scope)
