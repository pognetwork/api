# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enode/api.proto\x12\x03\x41PI\"\x07\n\x05\x45mpty\"\xfb\x02\n\x0bTransaction\x12)\n\x06txOpen\x18\x05 \x01(\x0b\x32\x17.API.Transaction.TxOpenH\x00\x12)\n\x06txSend\x18\x06 \x01(\x0b\x32\x17.API.Transaction.TxSendH\x00\x12+\n\x07txClaim\x18\x07 \x01(\x0b\x32\x18.API.Transaction.TxClaimH\x00\x12\x31\n\ntxDelegate\x18\x08 \x01(\x0b\x32\x1b.API.Transaction.TxDelegateH\x00\x1a(\n\x06TxOpen\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.API.AccountType\x1a\x38\n\x06TxSend\x12\x10\n\x08receiver\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x1a$\n\x07TxClaim\x12\x19\n\x11sendTransactionID\x18\x01 \x01(\x0c\x1a$\n\nTxDelegate\x12\x16\n\x0erepresentative\x18\x01 \x01(\x0c\x42\x06\n\x04\x64\x61ta\"Y\n\x05\x42lock\x12 \n\x06header\x18\x01 \x01(\x0b\x32\x10.API.BlockHeader\x12\x1c\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0e.API.BlockData\x12\x10\n\x08\x62lock_id\x18\x03 \x01(\x0c\":\n\x08RawBlock\x12 \n\x06header\x18\x01 \x01(\x0b\x32\x10.API.BlockHeader\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"F\n\x0b\x42lockHeader\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x11\n\tpublicKey\x18\x05 \x01(\x0c\x12\x11\n\ttimestamp\x18\x07 \x01(\x04\"\xaf\x01\n\tBlockData\x12\"\n\x07version\x18\x01 \x01(\x0e\x32\x11.API.BlockVersion\x12#\n\rsignatureType\x18\x02 \x01(\x0e\x32\x0c.API.SigType\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x04\x12\x0e\n\x06height\x18\x05 \x01(\x04\x12\x10\n\x08previous\x18\x06 \x01(\x0c\x12&\n\x0ctransactions\x18\x07 \x03(\x0b\x32\x10.API.Transaction**\n\x0b\x41\x63\x63ountType\x12\x0b\n\x07Managed\x10\x00\x12\x0e\n\nAutonomous\x10\x01*\x16\n\x07SigType\x12\x0b\n\x07\x45\x64\x32\x35\x35\x31\x39\x10\x00*\x16\n\x0c\x42lockVersion\x12\x06\n\x02V1\x10\x00\x62\x06proto3')

_ACCOUNTTYPE = DESCRIPTOR.enum_types_by_name['AccountType']
AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
_SIGTYPE = DESCRIPTOR.enum_types_by_name['SigType']
SigType = enum_type_wrapper.EnumTypeWrapper(_SIGTYPE)
_BLOCKVERSION = DESCRIPTOR.enum_types_by_name['BlockVersion']
BlockVersion = enum_type_wrapper.EnumTypeWrapper(_BLOCKVERSION)
Managed = 0
Autonomous = 1
Ed25519 = 0
V1 = 0


_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_TRANSACTION = DESCRIPTOR.message_types_by_name['Transaction']
_TRANSACTION_TXOPEN = _TRANSACTION.nested_types_by_name['TxOpen']
_TRANSACTION_TXSEND = _TRANSACTION.nested_types_by_name['TxSend']
_TRANSACTION_TXCLAIM = _TRANSACTION.nested_types_by_name['TxClaim']
_TRANSACTION_TXDELEGATE = _TRANSACTION.nested_types_by_name['TxDelegate']
_BLOCK = DESCRIPTOR.message_types_by_name['Block']
_RAWBLOCK = DESCRIPTOR.message_types_by_name['RawBlock']
_BLOCKHEADER = DESCRIPTOR.message_types_by_name['BlockHeader']
_BLOCKDATA = DESCRIPTOR.message_types_by_name['BlockData']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
    'DESCRIPTOR': _EMPTY,
    '__module__': 'node.api_pb2'
    # @@protoc_insertion_point(class_scope:API.Empty)
})
_sym_db.RegisterMessage(Empty)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {

    'TxOpen': _reflection.GeneratedProtocolMessageType('TxOpen', (_message.Message,), {
        'DESCRIPTOR': _TRANSACTION_TXOPEN,
        '__module__': 'node.api_pb2'
        # @@protoc_insertion_point(class_scope:API.Transaction.TxOpen)
    }),

    'TxSend': _reflection.GeneratedProtocolMessageType('TxSend', (_message.Message,), {
        'DESCRIPTOR': _TRANSACTION_TXSEND,
        '__module__': 'node.api_pb2'
        # @@protoc_insertion_point(class_scope:API.Transaction.TxSend)
    }),

    'TxClaim': _reflection.GeneratedProtocolMessageType('TxClaim', (_message.Message,), {
        'DESCRIPTOR': _TRANSACTION_TXCLAIM,
        '__module__': 'node.api_pb2'
        # @@protoc_insertion_point(class_scope:API.Transaction.TxClaim)
    }),

    'TxDelegate': _reflection.GeneratedProtocolMessageType('TxDelegate', (_message.Message,), {
        'DESCRIPTOR': _TRANSACTION_TXDELEGATE,
        '__module__': 'node.api_pb2'
        # @@protoc_insertion_point(class_scope:API.Transaction.TxDelegate)
    }),
    'DESCRIPTOR': _TRANSACTION,
    '__module__': 'node.api_pb2'
    # @@protoc_insertion_point(class_scope:API.Transaction)
})
_sym_db.RegisterMessage(Transaction)
_sym_db.RegisterMessage(Transaction.TxOpen)
_sym_db.RegisterMessage(Transaction.TxSend)
_sym_db.RegisterMessage(Transaction.TxClaim)
_sym_db.RegisterMessage(Transaction.TxDelegate)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
    'DESCRIPTOR': _BLOCK,
    '__module__': 'node.api_pb2'
    # @@protoc_insertion_point(class_scope:API.Block)
})
_sym_db.RegisterMessage(Block)

RawBlock = _reflection.GeneratedProtocolMessageType('RawBlock', (_message.Message,), {
    'DESCRIPTOR': _RAWBLOCK,
    '__module__': 'node.api_pb2'
    # @@protoc_insertion_point(class_scope:API.RawBlock)
})
_sym_db.RegisterMessage(RawBlock)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), {
    'DESCRIPTOR': _BLOCKHEADER,
    '__module__': 'node.api_pb2'
    # @@protoc_insertion_point(class_scope:API.BlockHeader)
})
_sym_db.RegisterMessage(BlockHeader)

BlockData = _reflection.GeneratedProtocolMessageType('BlockData', (_message.Message,), {
    'DESCRIPTOR': _BLOCKDATA,
    '__module__': 'node.api_pb2'
    # @@protoc_insertion_point(class_scope:API.BlockData)
})
_sym_db.RegisterMessage(BlockData)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ACCOUNTTYPE._serialized_start = 815
    _ACCOUNTTYPE._serialized_end = 857
    _SIGTYPE._serialized_start = 859
    _SIGTYPE._serialized_end = 881
    _BLOCKVERSION._serialized_start = 883
    _BLOCKVERSION._serialized_end = 905
    _EMPTY._serialized_start = 23
    _EMPTY._serialized_end = 30
    _TRANSACTION._serialized_start = 33
    _TRANSACTION._serialized_end = 412
    _TRANSACTION_TXOPEN._serialized_start = 230
    _TRANSACTION_TXOPEN._serialized_end = 270
    _TRANSACTION_TXSEND._serialized_start = 272
    _TRANSACTION_TXSEND._serialized_end = 328
    _TRANSACTION_TXCLAIM._serialized_start = 330
    _TRANSACTION_TXCLAIM._serialized_end = 366
    _TRANSACTION_TXDELEGATE._serialized_start = 368
    _TRANSACTION_TXDELEGATE._serialized_end = 404
    _BLOCK._serialized_start = 414
    _BLOCK._serialized_end = 503
    _RAWBLOCK._serialized_start = 505
    _RAWBLOCK._serialized_end = 563
    _BLOCKHEADER._serialized_start = 565
    _BLOCKHEADER._serialized_end = 635
    _BLOCKDATA._serialized_start = 638
    _BLOCKDATA._serialized_end = 813
# @@protoc_insertion_point(module_scope)