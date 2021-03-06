# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mail.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import world_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mail.proto',
  package='Sanguo.protocol.mail',
  serialized_pb='\n\nmail.proto\x12\x14Sanguo.protocol.mail\x1a\x0bworld.proto\"\x9e\x01\n\x04Mail\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\t\x12\x10\n\x08has_read\x18\x04 \x02(\x08\x12\x10\n\x08start_at\x18\x05 \x02(\x05\x12\x10\n\x08max_days\x18\x06 \x02(\x05\x12\x35\n\nattachment\x18\x07 \x01(\x0b\x32!.Sanguo.protocol.world.Attachment\"H\n\nMailNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12)\n\x05mails\x18\x02 \x03(\x0b\x32\x1a.Sanguo.protocol.mail.Mail\".\n\x0fOpenMailRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"0\n\x10OpenMailResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"0\n\x11\x44\x65leteMailRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"2\n\x12\x44\x65leteMailResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"3\n\x14GetAttachmentRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"l\n\x15GetAttachmentResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x35\n\nattachment\x18\x03 \x01(\x0b\x32!.Sanguo.protocol.world.Attachment')




_MAIL = _descriptor.Descriptor(
  name='Mail',
  full_name='Sanguo.protocol.mail.Mail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.mail.Mail.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Sanguo.protocol.mail.Mail.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='Sanguo.protocol.mail.Mail.content', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_read', full_name='Sanguo.protocol.mail.Mail.has_read', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_at', full_name='Sanguo.protocol.mail.Mail.start_at', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_days', full_name='Sanguo.protocol.mail.Mail.max_days', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attachment', full_name='Sanguo.protocol.mail.Mail.attachment', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=50,
  serialized_end=208,
)


_MAILNOTIFY = _descriptor.Descriptor(
  name='MailNotify',
  full_name='Sanguo.protocol.mail.MailNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.mail.MailNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mails', full_name='Sanguo.protocol.mail.MailNotify.mails', index=1,
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
  extension_ranges=[],
  serialized_start=210,
  serialized_end=282,
)


_OPENMAILREQUEST = _descriptor.Descriptor(
  name='OpenMailRequest',
  full_name='Sanguo.protocol.mail.OpenMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.mail.OpenMailRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.mail.OpenMailRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=284,
  serialized_end=330,
)


_OPENMAILRESPONSE = _descriptor.Descriptor(
  name='OpenMailResponse',
  full_name='Sanguo.protocol.mail.OpenMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.mail.OpenMailResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.mail.OpenMailResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=332,
  serialized_end=380,
)


_DELETEMAILREQUEST = _descriptor.Descriptor(
  name='DeleteMailRequest',
  full_name='Sanguo.protocol.mail.DeleteMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.mail.DeleteMailRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.mail.DeleteMailRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=382,
  serialized_end=430,
)


_DELETEMAILRESPONSE = _descriptor.Descriptor(
  name='DeleteMailResponse',
  full_name='Sanguo.protocol.mail.DeleteMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.mail.DeleteMailResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.mail.DeleteMailResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=432,
  serialized_end=482,
)


_GETATTACHMENTREQUEST = _descriptor.Descriptor(
  name='GetAttachmentRequest',
  full_name='Sanguo.protocol.mail.GetAttachmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.mail.GetAttachmentRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.mail.GetAttachmentRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=484,
  serialized_end=535,
)


_GETATTACHMENTRESPONSE = _descriptor.Descriptor(
  name='GetAttachmentResponse',
  full_name='Sanguo.protocol.mail.GetAttachmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.mail.GetAttachmentResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.mail.GetAttachmentResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attachment', full_name='Sanguo.protocol.mail.GetAttachmentResponse.attachment', index=2,
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
  extension_ranges=[],
  serialized_start=537,
  serialized_end=645,
)

_MAIL.fields_by_name['attachment'].message_type = world_pb2._ATTACHMENT
_MAILNOTIFY.fields_by_name['mails'].message_type = _MAIL
_GETATTACHMENTRESPONSE.fields_by_name['attachment'].message_type = world_pb2._ATTACHMENT
DESCRIPTOR.message_types_by_name['Mail'] = _MAIL
DESCRIPTOR.message_types_by_name['MailNotify'] = _MAILNOTIFY
DESCRIPTOR.message_types_by_name['OpenMailRequest'] = _OPENMAILREQUEST
DESCRIPTOR.message_types_by_name['OpenMailResponse'] = _OPENMAILRESPONSE
DESCRIPTOR.message_types_by_name['DeleteMailRequest'] = _DELETEMAILREQUEST
DESCRIPTOR.message_types_by_name['DeleteMailResponse'] = _DELETEMAILRESPONSE
DESCRIPTOR.message_types_by_name['GetAttachmentRequest'] = _GETATTACHMENTREQUEST
DESCRIPTOR.message_types_by_name['GetAttachmentResponse'] = _GETATTACHMENTRESPONSE

class Mail(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.Mail)

class MailNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAILNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.MailNotify)

class OpenMailRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPENMAILREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.OpenMailRequest)

class OpenMailResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPENMAILRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.OpenMailResponse)

class DeleteMailRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DELETEMAILREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.DeleteMailRequest)

class DeleteMailResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DELETEMAILRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.DeleteMailResponse)

class GetAttachmentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETATTACHMENTREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.GetAttachmentRequest)

class GetAttachmentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETATTACHMENTRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.mail.GetAttachmentResponse)


# @@protoc_insertion_point(module_scope)
