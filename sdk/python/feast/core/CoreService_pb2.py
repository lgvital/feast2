# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/CoreService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.core import FeatureSet_pb2 as feast_dot_core_dot_FeatureSet__pb2
from feast.core import Store_pb2 as feast_dot_core_dot_Store__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/CoreService.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=_b('\n\nfeast.coreB\020CoreServiceProtoZ/github.com/gojek/feast/sdk/go/protos/feast/core'),
  serialized_pb=_b('\n\x1c\x66\x65\x61st/core/CoreService.proto\x12\nfeast.core\x1a\x1b\x66\x65\x61st/core/FeatureSet.proto\x1a\x16\x66\x65\x61st/core/Store.proto\"F\n\x14GetFeatureSetRequest\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\"D\n\x15GetFeatureSetResponse\x12+\n\x0b\x66\x65\x61ture_set\x18\x01 \x01(\x0b\x32\x16.feast.core.FeatureSet\"\xa5\x01\n\x16ListFeatureSetsRequest\x12\x39\n\x06\x66ilter\x18\x01 \x01(\x0b\x32).feast.core.ListFeatureSetsRequest.Filter\x1aP\n\x06\x46ilter\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x01 \x01(\t\x12\x1b\n\x13\x66\x65\x61ture_set_version\x18\x02 \x01(\t\"G\n\x17ListFeatureSetsResponse\x12,\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32\x16.feast.core.FeatureSet\"a\n\x11ListStoresRequest\x12\x34\n\x06\x66ilter\x18\x01 \x01(\x0b\x32$.feast.core.ListStoresRequest.Filter\x1a\x16\n\x06\x46ilter\x12\x0c\n\x04name\x18\x01 \x01(\t\"6\n\x12ListStoresResponse\x12 \n\x05store\x18\x01 \x03(\x0b\x32\x11.feast.core.Store\"E\n\x16\x41pplyFeatureSetRequest\x12+\n\x0b\x66\x65\x61ture_set\x18\x01 \x01(\x0b\x32\x16.feast.core.FeatureSet\"\xb3\x01\n\x17\x41pplyFeatureSetResponse\x12+\n\x0b\x66\x65\x61ture_set\x18\x01 \x01(\x0b\x32\x16.feast.core.FeatureSet\x12:\n\x06status\x18\x02 \x01(\x0e\x32*.feast.core.ApplyFeatureSetResponse.Status\"/\n\x06Status\x12\r\n\tNO_CHANGE\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"\x1c\n\x1aGetFeastCoreVersionRequest\".\n\x1bGetFeastCoreVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\"6\n\x12UpdateStoreRequest\x12 \n\x05store\x18\x01 \x01(\x0b\x32\x11.feast.core.Store\"\x95\x01\n\x13UpdateStoreResponse\x12 \n\x05store\x18\x01 \x01(\x0b\x32\x11.feast.core.Store\x12\x36\n\x06status\x18\x02 \x01(\x0e\x32&.feast.core.UpdateStoreResponse.Status\"$\n\x06Status\x12\r\n\tNO_CHANGE\x10\x00\x12\x0b\n\x07UPDATED\x10\x01\"$\n\x14\x43reateProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x17\n\x15\x43reateProjectResponse\"%\n\x15\x41rchiveProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x18\n\x16\x41rchiveProjectResponse\"\x15\n\x13ListProjectsRequest\"(\n\x14ListProjectsResponse\x12\x10\n\x08projects\x18\x01 \x03(\t2\xa2\x06\n\x0b\x43oreService\x12\x66\n\x13GetFeastCoreVersion\x12&.feast.core.GetFeastCoreVersionRequest\x1a\'.feast.core.GetFeastCoreVersionResponse\x12T\n\rGetFeatureSet\x12 .feast.core.GetFeatureSetRequest\x1a!.feast.core.GetFeatureSetResponse\x12Z\n\x0fListFeatureSets\x12\".feast.core.ListFeatureSetsRequest\x1a#.feast.core.ListFeatureSetsResponse\x12K\n\nListStores\x12\x1d.feast.core.ListStoresRequest\x1a\x1e.feast.core.ListStoresResponse\x12Z\n\x0f\x41pplyFeatureSet\x12\".feast.core.ApplyFeatureSetRequest\x1a#.feast.core.ApplyFeatureSetResponse\x12N\n\x0bUpdateStore\x12\x1e.feast.core.UpdateStoreRequest\x1a\x1f.feast.core.UpdateStoreResponse\x12T\n\rCreateProject\x12 .feast.core.CreateProjectRequest\x1a!.feast.core.CreateProjectResponse\x12W\n\x0e\x41rchiveProject\x12!.feast.core.ArchiveProjectRequest\x1a\".feast.core.ArchiveProjectResponse\x12Q\n\x0cListProjects\x12\x1f.feast.core.ListProjectsRequest\x1a .feast.core.ListProjectsResponseBO\n\nfeast.coreB\x10\x43oreServiceProtoZ/github.com/gojek/feast/sdk/go/protos/feast/coreb\x06proto3')
  ,
  dependencies=[feast_dot_core_dot_FeatureSet__pb2.DESCRIPTOR,feast_dot_core_dot_Store__pb2.DESCRIPTOR,])



_APPLYFEATURESETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='feast.core.ApplyFeatureSetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CHANGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=839,
  serialized_end=886,
)
_sym_db.RegisterEnumDescriptor(_APPLYFEATURESETRESPONSE_STATUS)

_UPDATESTORERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='feast.core.UpdateStoreResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CHANGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1136,
  serialized_end=1172,
)
_sym_db.RegisterEnumDescriptor(_UPDATESTORERESPONSE_STATUS)


_GETFEATURESETREQUEST = _descriptor.Descriptor(
  name='GetFeatureSetRequest',
  full_name='feast.core.GetFeatureSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='feast.core.GetFeatureSetRequest.project', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.GetFeatureSetRequest.name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.core.GetFeatureSetRequest.version', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=167,
)


_GETFEATURESETRESPONSE = _descriptor.Descriptor(
  name='GetFeatureSetResponse',
  full_name='feast.core.GetFeatureSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set', full_name='feast.core.GetFeatureSetResponse.feature_set', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=237,
)


_LISTFEATURESETSREQUEST_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='feast.core.ListFeatureSetsRequest.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='feast.core.ListFeatureSetsRequest.Filter.project', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_set_name', full_name='feast.core.ListFeatureSetsRequest.Filter.feature_set_name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_set_version', full_name='feast.core.ListFeatureSetsRequest.Filter.feature_set_version', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=405,
)

_LISTFEATURESETSREQUEST = _descriptor.Descriptor(
  name='ListFeatureSetsRequest',
  full_name='feast.core.ListFeatureSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='feast.core.ListFeatureSetsRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTFEATURESETSREQUEST_FILTER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=405,
)


_LISTFEATURESETSRESPONSE = _descriptor.Descriptor(
  name='ListFeatureSetsResponse',
  full_name='feast.core.ListFeatureSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_sets', full_name='feast.core.ListFeatureSetsResponse.feature_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=478,
)


_LISTSTORESREQUEST_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='feast.core.ListStoresRequest.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.ListStoresRequest.Filter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=577,
)

_LISTSTORESREQUEST = _descriptor.Descriptor(
  name='ListStoresRequest',
  full_name='feast.core.ListStoresRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='feast.core.ListStoresRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTSTORESREQUEST_FILTER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=577,
)


_LISTSTORESRESPONSE = _descriptor.Descriptor(
  name='ListStoresResponse',
  full_name='feast.core.ListStoresResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store', full_name='feast.core.ListStoresResponse.store', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=633,
)


_APPLYFEATURESETREQUEST = _descriptor.Descriptor(
  name='ApplyFeatureSetRequest',
  full_name='feast.core.ApplyFeatureSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set', full_name='feast.core.ApplyFeatureSetRequest.feature_set', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=704,
)


_APPLYFEATURESETRESPONSE = _descriptor.Descriptor(
  name='ApplyFeatureSetResponse',
  full_name='feast.core.ApplyFeatureSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set', full_name='feast.core.ApplyFeatureSetResponse.feature_set', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='feast.core.ApplyFeatureSetResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APPLYFEATURESETRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=707,
  serialized_end=886,
)


_GETFEASTCOREVERSIONREQUEST = _descriptor.Descriptor(
  name='GetFeastCoreVersionRequest',
  full_name='feast.core.GetFeastCoreVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=888,
  serialized_end=916,
)


_GETFEASTCOREVERSIONRESPONSE = _descriptor.Descriptor(
  name='GetFeastCoreVersionResponse',
  full_name='feast.core.GetFeastCoreVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.core.GetFeastCoreVersionResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=918,
  serialized_end=964,
)


_UPDATESTOREREQUEST = _descriptor.Descriptor(
  name='UpdateStoreRequest',
  full_name='feast.core.UpdateStoreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store', full_name='feast.core.UpdateStoreRequest.store', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=966,
  serialized_end=1020,
)


_UPDATESTORERESPONSE = _descriptor.Descriptor(
  name='UpdateStoreResponse',
  full_name='feast.core.UpdateStoreResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store', full_name='feast.core.UpdateStoreResponse.store', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='feast.core.UpdateStoreResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATESTORERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1023,
  serialized_end=1172,
)


_CREATEPROJECTREQUEST = _descriptor.Descriptor(
  name='CreateProjectRequest',
  full_name='feast.core.CreateProjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.CreateProjectRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1174,
  serialized_end=1210,
)


_CREATEPROJECTRESPONSE = _descriptor.Descriptor(
  name='CreateProjectResponse',
  full_name='feast.core.CreateProjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1212,
  serialized_end=1235,
)


_ARCHIVEPROJECTREQUEST = _descriptor.Descriptor(
  name='ArchiveProjectRequest',
  full_name='feast.core.ArchiveProjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.ArchiveProjectRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1237,
  serialized_end=1274,
)


_ARCHIVEPROJECTRESPONSE = _descriptor.Descriptor(
  name='ArchiveProjectResponse',
  full_name='feast.core.ArchiveProjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1276,
  serialized_end=1300,
)


_LISTPROJECTSREQUEST = _descriptor.Descriptor(
  name='ListProjectsRequest',
  full_name='feast.core.ListProjectsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1302,
  serialized_end=1323,
)


_LISTPROJECTSRESPONSE = _descriptor.Descriptor(
  name='ListProjectsResponse',
  full_name='feast.core.ListProjectsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='projects', full_name='feast.core.ListProjectsResponse.projects', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1325,
  serialized_end=1365,
)

_GETFEATURESETRESPONSE.fields_by_name['feature_set'].message_type = feast_dot_core_dot_FeatureSet__pb2._FEATURESET
_LISTFEATURESETSREQUEST_FILTER.containing_type = _LISTFEATURESETSREQUEST
_LISTFEATURESETSREQUEST.fields_by_name['filter'].message_type = _LISTFEATURESETSREQUEST_FILTER
_LISTFEATURESETSRESPONSE.fields_by_name['feature_sets'].message_type = feast_dot_core_dot_FeatureSet__pb2._FEATURESET
_LISTSTORESREQUEST_FILTER.containing_type = _LISTSTORESREQUEST
_LISTSTORESREQUEST.fields_by_name['filter'].message_type = _LISTSTORESREQUEST_FILTER
_LISTSTORESRESPONSE.fields_by_name['store'].message_type = feast_dot_core_dot_Store__pb2._STORE
_APPLYFEATURESETREQUEST.fields_by_name['feature_set'].message_type = feast_dot_core_dot_FeatureSet__pb2._FEATURESET
_APPLYFEATURESETRESPONSE.fields_by_name['feature_set'].message_type = feast_dot_core_dot_FeatureSet__pb2._FEATURESET
_APPLYFEATURESETRESPONSE.fields_by_name['status'].enum_type = _APPLYFEATURESETRESPONSE_STATUS
_APPLYFEATURESETRESPONSE_STATUS.containing_type = _APPLYFEATURESETRESPONSE
_UPDATESTOREREQUEST.fields_by_name['store'].message_type = feast_dot_core_dot_Store__pb2._STORE
_UPDATESTORERESPONSE.fields_by_name['store'].message_type = feast_dot_core_dot_Store__pb2._STORE
_UPDATESTORERESPONSE.fields_by_name['status'].enum_type = _UPDATESTORERESPONSE_STATUS
_UPDATESTORERESPONSE_STATUS.containing_type = _UPDATESTORERESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureSetRequest'] = _GETFEATURESETREQUEST
DESCRIPTOR.message_types_by_name['GetFeatureSetResponse'] = _GETFEATURESETRESPONSE
DESCRIPTOR.message_types_by_name['ListFeatureSetsRequest'] = _LISTFEATURESETSREQUEST
DESCRIPTOR.message_types_by_name['ListFeatureSetsResponse'] = _LISTFEATURESETSRESPONSE
DESCRIPTOR.message_types_by_name['ListStoresRequest'] = _LISTSTORESREQUEST
DESCRIPTOR.message_types_by_name['ListStoresResponse'] = _LISTSTORESRESPONSE
DESCRIPTOR.message_types_by_name['ApplyFeatureSetRequest'] = _APPLYFEATURESETREQUEST
DESCRIPTOR.message_types_by_name['ApplyFeatureSetResponse'] = _APPLYFEATURESETRESPONSE
DESCRIPTOR.message_types_by_name['GetFeastCoreVersionRequest'] = _GETFEASTCOREVERSIONREQUEST
DESCRIPTOR.message_types_by_name['GetFeastCoreVersionResponse'] = _GETFEASTCOREVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['UpdateStoreRequest'] = _UPDATESTOREREQUEST
DESCRIPTOR.message_types_by_name['UpdateStoreResponse'] = _UPDATESTORERESPONSE
DESCRIPTOR.message_types_by_name['CreateProjectRequest'] = _CREATEPROJECTREQUEST
DESCRIPTOR.message_types_by_name['CreateProjectResponse'] = _CREATEPROJECTRESPONSE
DESCRIPTOR.message_types_by_name['ArchiveProjectRequest'] = _ARCHIVEPROJECTREQUEST
DESCRIPTOR.message_types_by_name['ArchiveProjectResponse'] = _ARCHIVEPROJECTRESPONSE
DESCRIPTOR.message_types_by_name['ListProjectsRequest'] = _LISTPROJECTSREQUEST
DESCRIPTOR.message_types_by_name['ListProjectsResponse'] = _LISTPROJECTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeatureSetRequest = _reflection.GeneratedProtocolMessageType('GetFeatureSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEATURESETREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.GetFeatureSetRequest)
  })
_sym_db.RegisterMessage(GetFeatureSetRequest)

GetFeatureSetResponse = _reflection.GeneratedProtocolMessageType('GetFeatureSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEATURESETRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.GetFeatureSetResponse)
  })
_sym_db.RegisterMessage(GetFeatureSetResponse)

ListFeatureSetsRequest = _reflection.GeneratedProtocolMessageType('ListFeatureSetsRequest', (_message.Message,), {

  'Filter' : _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
    'DESCRIPTOR' : _LISTFEATURESETSREQUEST_FILTER,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.ListFeatureSetsRequest.Filter)
    })
  ,
  'DESCRIPTOR' : _LISTFEATURESETSREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ListFeatureSetsRequest)
  })
_sym_db.RegisterMessage(ListFeatureSetsRequest)
_sym_db.RegisterMessage(ListFeatureSetsRequest.Filter)

ListFeatureSetsResponse = _reflection.GeneratedProtocolMessageType('ListFeatureSetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFEATURESETSRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ListFeatureSetsResponse)
  })
_sym_db.RegisterMessage(ListFeatureSetsResponse)

ListStoresRequest = _reflection.GeneratedProtocolMessageType('ListStoresRequest', (_message.Message,), {

  'Filter' : _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
    'DESCRIPTOR' : _LISTSTORESREQUEST_FILTER,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.ListStoresRequest.Filter)
    })
  ,
  'DESCRIPTOR' : _LISTSTORESREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ListStoresRequest)
  })
_sym_db.RegisterMessage(ListStoresRequest)
_sym_db.RegisterMessage(ListStoresRequest.Filter)

ListStoresResponse = _reflection.GeneratedProtocolMessageType('ListStoresResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSTORESRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ListStoresResponse)
  })
_sym_db.RegisterMessage(ListStoresResponse)

ApplyFeatureSetRequest = _reflection.GeneratedProtocolMessageType('ApplyFeatureSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPLYFEATURESETREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ApplyFeatureSetRequest)
  })
_sym_db.RegisterMessage(ApplyFeatureSetRequest)

ApplyFeatureSetResponse = _reflection.GeneratedProtocolMessageType('ApplyFeatureSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYFEATURESETRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ApplyFeatureSetResponse)
  })
_sym_db.RegisterMessage(ApplyFeatureSetResponse)

GetFeastCoreVersionRequest = _reflection.GeneratedProtocolMessageType('GetFeastCoreVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTCOREVERSIONREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.GetFeastCoreVersionRequest)
  })
_sym_db.RegisterMessage(GetFeastCoreVersionRequest)

GetFeastCoreVersionResponse = _reflection.GeneratedProtocolMessageType('GetFeastCoreVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTCOREVERSIONRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.GetFeastCoreVersionResponse)
  })
_sym_db.RegisterMessage(GetFeastCoreVersionResponse)

UpdateStoreRequest = _reflection.GeneratedProtocolMessageType('UpdateStoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTOREREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.UpdateStoreRequest)
  })
_sym_db.RegisterMessage(UpdateStoreRequest)

UpdateStoreResponse = _reflection.GeneratedProtocolMessageType('UpdateStoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTORERESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.UpdateStoreResponse)
  })
_sym_db.RegisterMessage(UpdateStoreResponse)

CreateProjectRequest = _reflection.GeneratedProtocolMessageType('CreateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.CreateProjectRequest)
  })
_sym_db.RegisterMessage(CreateProjectRequest)

CreateProjectResponse = _reflection.GeneratedProtocolMessageType('CreateProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.CreateProjectResponse)
  })
_sym_db.RegisterMessage(CreateProjectResponse)

ArchiveProjectRequest = _reflection.GeneratedProtocolMessageType('ArchiveProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _ARCHIVEPROJECTREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ArchiveProjectRequest)
  })
_sym_db.RegisterMessage(ArchiveProjectRequest)

ArchiveProjectResponse = _reflection.GeneratedProtocolMessageType('ArchiveProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _ARCHIVEPROJECTRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ArchiveProjectResponse)
  })
_sym_db.RegisterMessage(ArchiveProjectResponse)

ListProjectsRequest = _reflection.GeneratedProtocolMessageType('ListProjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTSREQUEST,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ListProjectsRequest)
  })
_sym_db.RegisterMessage(ListProjectsRequest)

ListProjectsResponse = _reflection.GeneratedProtocolMessageType('ListProjectsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTSRESPONSE,
  '__module__' : 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.ListProjectsResponse)
  })
_sym_db.RegisterMessage(ListProjectsResponse)


DESCRIPTOR._options = None

_CORESERVICE = _descriptor.ServiceDescriptor(
  name='CoreService',
  full_name='feast.core.CoreService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1368,
  serialized_end=2170,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeastCoreVersion',
    full_name='feast.core.CoreService.GetFeastCoreVersion',
    index=0,
    containing_service=None,
    input_type=_GETFEASTCOREVERSIONREQUEST,
    output_type=_GETFEASTCOREVERSIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFeatureSet',
    full_name='feast.core.CoreService.GetFeatureSet',
    index=1,
    containing_service=None,
    input_type=_GETFEATURESETREQUEST,
    output_type=_GETFEATURESETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListFeatureSets',
    full_name='feast.core.CoreService.ListFeatureSets',
    index=2,
    containing_service=None,
    input_type=_LISTFEATURESETSREQUEST,
    output_type=_LISTFEATURESETSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListStores',
    full_name='feast.core.CoreService.ListStores',
    index=3,
    containing_service=None,
    input_type=_LISTSTORESREQUEST,
    output_type=_LISTSTORESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyFeatureSet',
    full_name='feast.core.CoreService.ApplyFeatureSet',
    index=4,
    containing_service=None,
    input_type=_APPLYFEATURESETREQUEST,
    output_type=_APPLYFEATURESETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateStore',
    full_name='feast.core.CoreService.UpdateStore',
    index=5,
    containing_service=None,
    input_type=_UPDATESTOREREQUEST,
    output_type=_UPDATESTORERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateProject',
    full_name='feast.core.CoreService.CreateProject',
    index=6,
    containing_service=None,
    input_type=_CREATEPROJECTREQUEST,
    output_type=_CREATEPROJECTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ArchiveProject',
    full_name='feast.core.CoreService.ArchiveProject',
    index=7,
    containing_service=None,
    input_type=_ARCHIVEPROJECTREQUEST,
    output_type=_ARCHIVEPROJECTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListProjects',
    full_name='feast.core.CoreService.ListProjects',
    index=8,
    containing_service=None,
    input_type=_LISTPROJECTSREQUEST,
    output_type=_LISTPROJECTSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CORESERVICE)

DESCRIPTOR.services_by_name['CoreService'] = _CORESERVICE

# @@protoc_insertion_point(module_scope)
