# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: purchase.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='purchase.proto',
  package='Sanguo.protocol.purchase',
  serialized_pb='\n\x0epurchase.proto\x12\x18Sanguo.protocol.purchase\"\xc0\x01\n\x14PurchaseStatusNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12M\n\x06status\x18\x02 \x03(\x0b\x32=.Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus\x12\x1b\n\x13yueka_remained_days\x18\x03 \x02(\x05\x1a+\n\x0ePurchaseStatus\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x66irst\x18\x02 \x02(\x08\"%\n\x12GetProductsRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"\xae\x01\n\x13GetProductsResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12G\n\x08products\x18\x03 \x03(\x0b\x32\x35.Sanguo.protocol.purchase.GetProductsResponse.Product\x1a\x30\n\x07Product\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0b\n\x03\x64\x65s\x18\x03 \x02(\t\"E\n\x10\x42uyVerityRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07\x63har_id\x18\x02 \x02(\x05\x12\x0f\n\x07receipt\x18\x03 \x02(\t\"R\n\x11\x42uyVerityResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tadd_sycee\x18\x04 \x01(\x05\"@\n\x1bPurchase91GetOrderIdRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x10\n\x08goods_id\x18\x02 \x02(\x05\"N\n\x1cPurchase91GetOrderIdResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x10\n\x08order_id\x18\x03 \x01(\t\"+\n\x18Purchase91ConfirmRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"\xdd\x01\n\x19Purchase91ConfirmResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12[\n\x06reason\x18\x03 \x01(\x0e\x32K.Sanguo.protocol.purchase.Purchase91ConfirmResponse.Purchase91FailureReason\x12\x10\n\x08goods_id\x18\x04 \x01(\x05\"3\n\x17Purchase91FailureReason\x12\x0b\n\x07WAITING\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02')



_PURCHASE91CONFIRMRESPONSE_PURCHASE91FAILUREREASON = _descriptor.EnumDescriptor(
  name='Purchase91FailureReason',
  full_name='Sanguo.protocol.purchase.Purchase91ConfirmResponse.Purchase91FailureReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=972,
  serialized_end=1023,
)


_PURCHASESTATUSNOTIFY_PURCHASESTATUS = _descriptor.Descriptor(
  name='PurchaseStatus',
  full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus.first', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=194,
  serialized_end=237,
)

_PURCHASESTATUSNOTIFY = _descriptor.Descriptor(
  name='PurchaseStatusNotify',
  full_name='Sanguo.protocol.purchase.PurchaseStatusNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.status', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yueka_remained_days', full_name='Sanguo.protocol.purchase.PurchaseStatusNotify.yueka_remained_days', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PURCHASESTATUSNOTIFY_PURCHASESTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=237,
)


_GETPRODUCTSREQUEST = _descriptor.Descriptor(
  name='GetProductsRequest',
  full_name='Sanguo.protocol.purchase.GetProductsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.GetProductsRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=239,
  serialized_end=276,
)


_GETPRODUCTSRESPONSE_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='Sanguo.protocol.purchase.GetProductsResponse.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.purchase.GetProductsResponse.Product.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Sanguo.protocol.purchase.GetProductsResponse.Product.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='des', full_name='Sanguo.protocol.purchase.GetProductsResponse.Product.des', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=405,
  serialized_end=453,
)

_GETPRODUCTSRESPONSE = _descriptor.Descriptor(
  name='GetProductsResponse',
  full_name='Sanguo.protocol.purchase.GetProductsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.GetProductsResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.GetProductsResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='products', full_name='Sanguo.protocol.purchase.GetProductsResponse.products', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETPRODUCTSRESPONSE_PRODUCT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=279,
  serialized_end=453,
)


_BUYVERITYREQUEST = _descriptor.Descriptor(
  name='BuyVerityRequest',
  full_name='Sanguo.protocol.purchase.BuyVerityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.BuyVerityRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_id', full_name='Sanguo.protocol.purchase.BuyVerityRequest.char_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='Sanguo.protocol.purchase.BuyVerityRequest.receipt', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=455,
  serialized_end=524,
)


_BUYVERITYRESPONSE = _descriptor.Descriptor(
  name='BuyVerityResponse',
  full_name='Sanguo.protocol.purchase.BuyVerityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.BuyVerityResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.BuyVerityResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Sanguo.protocol.purchase.BuyVerityResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_sycee', full_name='Sanguo.protocol.purchase.BuyVerityResponse.add_sycee', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=526,
  serialized_end=608,
)


_PURCHASE91GETORDERIDREQUEST = _descriptor.Descriptor(
  name='Purchase91GetOrderIdRequest',
  full_name='Sanguo.protocol.purchase.Purchase91GetOrderIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.Purchase91GetOrderIdRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='Sanguo.protocol.purchase.Purchase91GetOrderIdRequest.goods_id', index=1,
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
  serialized_start=610,
  serialized_end=674,
)


_PURCHASE91GETORDERIDRESPONSE = _descriptor.Descriptor(
  name='Purchase91GetOrderIdResponse',
  full_name='Sanguo.protocol.purchase.Purchase91GetOrderIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.Purchase91GetOrderIdResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.Purchase91GetOrderIdResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Sanguo.protocol.purchase.Purchase91GetOrderIdResponse.order_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=676,
  serialized_end=754,
)


_PURCHASE91CONFIRMREQUEST = _descriptor.Descriptor(
  name='Purchase91ConfirmRequest',
  full_name='Sanguo.protocol.purchase.Purchase91ConfirmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.Purchase91ConfirmRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=756,
  serialized_end=799,
)


_PURCHASE91CONFIRMRESPONSE = _descriptor.Descriptor(
  name='Purchase91ConfirmResponse',
  full_name='Sanguo.protocol.purchase.Purchase91ConfirmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.purchase.Purchase91ConfirmResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.purchase.Purchase91ConfirmResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='Sanguo.protocol.purchase.Purchase91ConfirmResponse.reason', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='Sanguo.protocol.purchase.Purchase91ConfirmResponse.goods_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PURCHASE91CONFIRMRESPONSE_PURCHASE91FAILUREREASON,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=802,
  serialized_end=1023,
)

_PURCHASESTATUSNOTIFY_PURCHASESTATUS.containing_type = _PURCHASESTATUSNOTIFY;
_PURCHASESTATUSNOTIFY.fields_by_name['status'].message_type = _PURCHASESTATUSNOTIFY_PURCHASESTATUS
_GETPRODUCTSRESPONSE_PRODUCT.containing_type = _GETPRODUCTSRESPONSE;
_GETPRODUCTSRESPONSE.fields_by_name['products'].message_type = _GETPRODUCTSRESPONSE_PRODUCT
_PURCHASE91CONFIRMRESPONSE.fields_by_name['reason'].enum_type = _PURCHASE91CONFIRMRESPONSE_PURCHASE91FAILUREREASON
_PURCHASE91CONFIRMRESPONSE_PURCHASE91FAILUREREASON.containing_type = _PURCHASE91CONFIRMRESPONSE;
DESCRIPTOR.message_types_by_name['PurchaseStatusNotify'] = _PURCHASESTATUSNOTIFY
DESCRIPTOR.message_types_by_name['GetProductsRequest'] = _GETPRODUCTSREQUEST
DESCRIPTOR.message_types_by_name['GetProductsResponse'] = _GETPRODUCTSRESPONSE
DESCRIPTOR.message_types_by_name['BuyVerityRequest'] = _BUYVERITYREQUEST
DESCRIPTOR.message_types_by_name['BuyVerityResponse'] = _BUYVERITYRESPONSE
DESCRIPTOR.message_types_by_name['Purchase91GetOrderIdRequest'] = _PURCHASE91GETORDERIDREQUEST
DESCRIPTOR.message_types_by_name['Purchase91GetOrderIdResponse'] = _PURCHASE91GETORDERIDRESPONSE
DESCRIPTOR.message_types_by_name['Purchase91ConfirmRequest'] = _PURCHASE91CONFIRMREQUEST
DESCRIPTOR.message_types_by_name['Purchase91ConfirmResponse'] = _PURCHASE91CONFIRMRESPONSE

class PurchaseStatusNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class PurchaseStatus(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PURCHASESTATUSNOTIFY_PURCHASESTATUS

    # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseStatusNotify.PurchaseStatus)
  DESCRIPTOR = _PURCHASESTATUSNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.PurchaseStatusNotify)

class GetProductsRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPRODUCTSREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.GetProductsRequest)

class GetProductsResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Product(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GETPRODUCTSRESPONSE_PRODUCT

    # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.GetProductsResponse.Product)
  DESCRIPTOR = _GETPRODUCTSRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.GetProductsResponse)

class BuyVerityRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYVERITYREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.BuyVerityRequest)

class BuyVerityResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYVERITYRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.BuyVerityResponse)

class Purchase91GetOrderIdRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASE91GETORDERIDREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.Purchase91GetOrderIdRequest)

class Purchase91GetOrderIdResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASE91GETORDERIDRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.Purchase91GetOrderIdResponse)

class Purchase91ConfirmRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASE91CONFIRMREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.Purchase91ConfirmRequest)

class Purchase91ConfirmResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURCHASE91CONFIRMRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.purchase.Purchase91ConfirmResponse)


# @@protoc_insertion_point(module_scope)
