# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ophion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ophion.proto',
  package='ophion',
  syntax='proto3',
  serialized_pb=_b('\n\x0cophion.proto\x12\x06ophion\x1a\x1cgoogle/protobuf/struct.proto\"3\n\nGraphQuery\x12%\n\x05query\x18\x01 \x03(\x0b\x32\x16.ophion.GraphStatement\"\xa4\x04\n\x0eGraphStatement\x12\x0b\n\x01V\x18\x01 \x01(\tH\x00\x12\x0b\n\x01\x45\x18\x02 \x01(\tH\x00\x12\x0f\n\x05label\x18\x03 \x01(\tH\x00\x12#\n\x03has\x18\x04 \x01(\x0b\x32\x14.ophion.HasStatementH\x00\x12\x0c\n\x02\x61s\x18\x05 \x01(\tH\x00\x12\x0c\n\x02in\x18\x06 \x01(\tH\x00\x12\r\n\x03out\x18\x07 \x01(\tH\x00\x12\x10\n\x06inEdge\x18\x08 \x01(\tH\x00\x12\x11\n\x07outEdge\x18\t \x01(\tH\x00\x12\x12\n\x08inVertex\x18\n \x01(\tH\x00\x12\x13\n\toutVertex\x18\x0b \x01(\tH\x00\x12)\n\x06select\x18\x0c \x01(\x0b\x32\x17.ophion.SelectStatementH\x00\x12)\n\x06values\x18\r \x01(\x0b\x32\x17.ophion.SelectStatementH\x00\x12\x0f\n\x05limit\x18\x0e \x01(\x03H\x00\x12\x0f\n\x05\x63ount\x18\x0f \x01(\tH\x00\x12\x10\n\x06import\x18\x32 \x01(\tH\x00\x12\"\n\x03map\x18\x33 \x01(\x0b\x32\x13.ophion.SingleArityH\x00\x12#\n\x04\x66old\x18\x34 \x01(\x0b\x32\x13.ophion.DoubleArityH\x00\x12\x0e\n\x04\x61\x64\x64V\x18\x64 \x01(\tH\x00\x12+\n\x08property\x18\x65 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x0e\n\x04\x61\x64\x64\x45\x18\x66 \x01(\tH\x00\x12\x0c\n\x02to\x18g \x01(\tH\x00\x12\x0e\n\x04\x64rop\x18h \x01(\tH\x00\x42\x0b\n\tstatement\"B\n\x0bSingleArity\x12\r\n\x05\x66irst\x18\x02 \x01(\t\x12$\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x16.ophion.GraphStatement\"R\n\x0b\x44oubleArity\x12\r\n\x05\x66irst\x18\x02 \x01(\t\x12\x0e\n\x06second\x18\x03 \x01(\t\x12$\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x16.ophion.GraphStatement\"+\n\x0cHasStatement\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06within\x18\x02 \x03(\t\"!\n\x0fSelectStatement\x12\x0e\n\x06labels\x18\x01 \x03(\t\"Q\n\x06Vertex\x12\x0b\n\x03gid\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"h\n\x04\x45\x64ge\x12\x0b\n\x03gid\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\n\n\x02in\x18\x03 \x01(\t\x12\x0b\n\x03out\x18\x04 \x01(\t\x12+\n\nproperties\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xc3\x01\n\x0bQueryResult\x12)\n\x06struct\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12 \n\x06vertex\x18\x02 \x01(\x0b\x32\x0e.ophion.VertexH\x00\x12\x1c\n\x04\x65\x64ge\x18\x03 \x01(\x0b\x32\x0c.ophion.EdgeH\x00\x12\x13\n\tint_value\x18\x04 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x05 \x01(\x01H\x00\x12\x13\n\tstr_value\x18\x06 \x01(\tH\x00\x42\x08\n\x06result\"Q\n\tResultRow\x12\"\n\x05value\x18\x01 \x01(\x0b\x32\x13.ophion.QueryResult\x12 \n\x03row\x18\x02 \x03(\x0b\x32\x13.ophion.QueryResultb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GRAPHQUERY = _descriptor.Descriptor(
  name='GraphQuery',
  full_name='ophion.GraphQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='ophion.GraphQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=105,
)


_GRAPHSTATEMENT = _descriptor.Descriptor(
  name='GraphStatement',
  full_name='ophion.GraphStatement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='V', full_name='ophion.GraphStatement.V', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='E', full_name='ophion.GraphStatement.E', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='ophion.GraphStatement.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has', full_name='ophion.GraphStatement.has', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='as', full_name='ophion.GraphStatement.as', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in', full_name='ophion.GraphStatement.in', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out', full_name='ophion.GraphStatement.out', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inEdge', full_name='ophion.GraphStatement.inEdge', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outEdge', full_name='ophion.GraphStatement.outEdge', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inVertex', full_name='ophion.GraphStatement.inVertex', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outVertex', full_name='ophion.GraphStatement.outVertex', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='select', full_name='ophion.GraphStatement.select', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='ophion.GraphStatement.values', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='ophion.GraphStatement.limit', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='ophion.GraphStatement.count', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='import', full_name='ophion.GraphStatement.import', index=15,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='ophion.GraphStatement.map', index=16,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fold', full_name='ophion.GraphStatement.fold', index=17,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addV', full_name='ophion.GraphStatement.addV', index=18,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='ophion.GraphStatement.property', index=19,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addE', full_name='ophion.GraphStatement.addE', index=20,
      number=102, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='ophion.GraphStatement.to', index=21,
      number=103, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='ophion.GraphStatement.drop', index=22,
      number=104, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='statement', full_name='ophion.GraphStatement.statement',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=108,
  serialized_end=656,
)


_SINGLEARITY = _descriptor.Descriptor(
  name='SingleArity',
  full_name='ophion.SingleArity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='ophion.SingleArity.first', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='ophion.SingleArity.body', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=658,
  serialized_end=724,
)


_DOUBLEARITY = _descriptor.Descriptor(
  name='DoubleArity',
  full_name='ophion.DoubleArity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='ophion.DoubleArity.first', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='second', full_name='ophion.DoubleArity.second', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='ophion.DoubleArity.body', index=2,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=726,
  serialized_end=808,
)


_HASSTATEMENT = _descriptor.Descriptor(
  name='HasStatement',
  full_name='ophion.HasStatement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ophion.HasStatement.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='within', full_name='ophion.HasStatement.within', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=810,
  serialized_end=853,
)


_SELECTSTATEMENT = _descriptor.Descriptor(
  name='SelectStatement',
  full_name='ophion.SelectStatement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='ophion.SelectStatement.labels', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=888,
)


_VERTEX = _descriptor.Descriptor(
  name='Vertex',
  full_name='ophion.Vertex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='ophion.Vertex.gid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='ophion.Vertex.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='ophion.Vertex.properties', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=890,
  serialized_end=971,
)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='ophion.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='ophion.Edge.gid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='ophion.Edge.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in', full_name='ophion.Edge.in', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out', full_name='ophion.Edge.out', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='ophion.Edge.properties', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=973,
  serialized_end=1077,
)


_QUERYRESULT = _descriptor.Descriptor(
  name='QueryResult',
  full_name='ophion.QueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='struct', full_name='ophion.QueryResult.struct', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertex', full_name='ophion.QueryResult.vertex', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edge', full_name='ophion.QueryResult.edge', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='ophion.QueryResult.int_value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='ophion.QueryResult.float_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_value', full_name='ophion.QueryResult.str_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='result', full_name='ophion.QueryResult.result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1080,
  serialized_end=1275,
)


_RESULTROW = _descriptor.Descriptor(
  name='ResultRow',
  full_name='ophion.ResultRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ophion.ResultRow.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='ophion.ResultRow.row', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1277,
  serialized_end=1358,
)

_GRAPHQUERY.fields_by_name['query'].message_type = _GRAPHSTATEMENT
_GRAPHSTATEMENT.fields_by_name['has'].message_type = _HASSTATEMENT
_GRAPHSTATEMENT.fields_by_name['select'].message_type = _SELECTSTATEMENT
_GRAPHSTATEMENT.fields_by_name['values'].message_type = _SELECTSTATEMENT
_GRAPHSTATEMENT.fields_by_name['map'].message_type = _SINGLEARITY
_GRAPHSTATEMENT.fields_by_name['fold'].message_type = _DOUBLEARITY
_GRAPHSTATEMENT.fields_by_name['property'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['V'])
_GRAPHSTATEMENT.fields_by_name['V'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['E'])
_GRAPHSTATEMENT.fields_by_name['E'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['label'])
_GRAPHSTATEMENT.fields_by_name['label'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['has'])
_GRAPHSTATEMENT.fields_by_name['has'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['as'])
_GRAPHSTATEMENT.fields_by_name['as'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['in'])
_GRAPHSTATEMENT.fields_by_name['in'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['out'])
_GRAPHSTATEMENT.fields_by_name['out'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['inEdge'])
_GRAPHSTATEMENT.fields_by_name['inEdge'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['outEdge'])
_GRAPHSTATEMENT.fields_by_name['outEdge'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['inVertex'])
_GRAPHSTATEMENT.fields_by_name['inVertex'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['outVertex'])
_GRAPHSTATEMENT.fields_by_name['outVertex'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['select'])
_GRAPHSTATEMENT.fields_by_name['select'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['values'])
_GRAPHSTATEMENT.fields_by_name['values'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['limit'])
_GRAPHSTATEMENT.fields_by_name['limit'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['count'])
_GRAPHSTATEMENT.fields_by_name['count'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['import'])
_GRAPHSTATEMENT.fields_by_name['import'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['map'])
_GRAPHSTATEMENT.fields_by_name['map'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['fold'])
_GRAPHSTATEMENT.fields_by_name['fold'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['addV'])
_GRAPHSTATEMENT.fields_by_name['addV'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['property'])
_GRAPHSTATEMENT.fields_by_name['property'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['addE'])
_GRAPHSTATEMENT.fields_by_name['addE'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['to'])
_GRAPHSTATEMENT.fields_by_name['to'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_GRAPHSTATEMENT.oneofs_by_name['statement'].fields.append(
  _GRAPHSTATEMENT.fields_by_name['drop'])
_GRAPHSTATEMENT.fields_by_name['drop'].containing_oneof = _GRAPHSTATEMENT.oneofs_by_name['statement']
_SINGLEARITY.fields_by_name['body'].message_type = _GRAPHSTATEMENT
_DOUBLEARITY.fields_by_name['body'].message_type = _GRAPHSTATEMENT
_VERTEX.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_EDGE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_QUERYRESULT.fields_by_name['struct'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_QUERYRESULT.fields_by_name['vertex'].message_type = _VERTEX
_QUERYRESULT.fields_by_name['edge'].message_type = _EDGE
_QUERYRESULT.oneofs_by_name['result'].fields.append(
  _QUERYRESULT.fields_by_name['struct'])
_QUERYRESULT.fields_by_name['struct'].containing_oneof = _QUERYRESULT.oneofs_by_name['result']
_QUERYRESULT.oneofs_by_name['result'].fields.append(
  _QUERYRESULT.fields_by_name['vertex'])
_QUERYRESULT.fields_by_name['vertex'].containing_oneof = _QUERYRESULT.oneofs_by_name['result']
_QUERYRESULT.oneofs_by_name['result'].fields.append(
  _QUERYRESULT.fields_by_name['edge'])
_QUERYRESULT.fields_by_name['edge'].containing_oneof = _QUERYRESULT.oneofs_by_name['result']
_QUERYRESULT.oneofs_by_name['result'].fields.append(
  _QUERYRESULT.fields_by_name['int_value'])
_QUERYRESULT.fields_by_name['int_value'].containing_oneof = _QUERYRESULT.oneofs_by_name['result']
_QUERYRESULT.oneofs_by_name['result'].fields.append(
  _QUERYRESULT.fields_by_name['float_value'])
_QUERYRESULT.fields_by_name['float_value'].containing_oneof = _QUERYRESULT.oneofs_by_name['result']
_QUERYRESULT.oneofs_by_name['result'].fields.append(
  _QUERYRESULT.fields_by_name['str_value'])
_QUERYRESULT.fields_by_name['str_value'].containing_oneof = _QUERYRESULT.oneofs_by_name['result']
_RESULTROW.fields_by_name['value'].message_type = _QUERYRESULT
_RESULTROW.fields_by_name['row'].message_type = _QUERYRESULT
DESCRIPTOR.message_types_by_name['GraphQuery'] = _GRAPHQUERY
DESCRIPTOR.message_types_by_name['GraphStatement'] = _GRAPHSTATEMENT
DESCRIPTOR.message_types_by_name['SingleArity'] = _SINGLEARITY
DESCRIPTOR.message_types_by_name['DoubleArity'] = _DOUBLEARITY
DESCRIPTOR.message_types_by_name['HasStatement'] = _HASSTATEMENT
DESCRIPTOR.message_types_by_name['SelectStatement'] = _SELECTSTATEMENT
DESCRIPTOR.message_types_by_name['Vertex'] = _VERTEX
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['QueryResult'] = _QUERYRESULT
DESCRIPTOR.message_types_by_name['ResultRow'] = _RESULTROW

GraphQuery = _reflection.GeneratedProtocolMessageType('GraphQuery', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHQUERY,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.GraphQuery)
  ))
_sym_db.RegisterMessage(GraphQuery)

GraphStatement = _reflection.GeneratedProtocolMessageType('GraphStatement', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHSTATEMENT,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.GraphStatement)
  ))
_sym_db.RegisterMessage(GraphStatement)

SingleArity = _reflection.GeneratedProtocolMessageType('SingleArity', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEARITY,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.SingleArity)
  ))
_sym_db.RegisterMessage(SingleArity)

DoubleArity = _reflection.GeneratedProtocolMessageType('DoubleArity', (_message.Message,), dict(
  DESCRIPTOR = _DOUBLEARITY,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.DoubleArity)
  ))
_sym_db.RegisterMessage(DoubleArity)

HasStatement = _reflection.GeneratedProtocolMessageType('HasStatement', (_message.Message,), dict(
  DESCRIPTOR = _HASSTATEMENT,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.HasStatement)
  ))
_sym_db.RegisterMessage(HasStatement)

SelectStatement = _reflection.GeneratedProtocolMessageType('SelectStatement', (_message.Message,), dict(
  DESCRIPTOR = _SELECTSTATEMENT,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.SelectStatement)
  ))
_sym_db.RegisterMessage(SelectStatement)

Vertex = _reflection.GeneratedProtocolMessageType('Vertex', (_message.Message,), dict(
  DESCRIPTOR = _VERTEX,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.Vertex)
  ))
_sym_db.RegisterMessage(Vertex)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
  DESCRIPTOR = _EDGE,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.Edge)
  ))
_sym_db.RegisterMessage(Edge)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESULT,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.QueryResult)
  ))
_sym_db.RegisterMessage(QueryResult)

ResultRow = _reflection.GeneratedProtocolMessageType('ResultRow', (_message.Message,), dict(
  DESCRIPTOR = _RESULTROW,
  __module__ = 'ophion_pb2'
  # @@protoc_insertion_point(class_scope:ophion.ResultRow)
  ))
_sym_db.RegisterMessage(ResultRow)


# @@protoc_insertion_point(module_scope)
