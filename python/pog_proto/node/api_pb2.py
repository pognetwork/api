# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enode/api.proto\x12\x03\x41PI\"\x07\n\x05\x45mpty\"\xfb\x02\n\x0bTransaction\x12)\n\x06txOpen\x18\x05 \x01(\x0b\x32\x17.API.Transaction.TxOpenH\x00\x12)\n\x06txSend\x18\x06 \x01(\x0b\x32\x17.API.Transaction.TxSendH\x00\x12+\n\x07txClaim\x18\x07 \x01(\x0b\x32\x18.API.Transaction.TxClaimH\x00\x12\x31\n\ntxDelegate\x18\x08 \x01(\x0b\x32\x1b.API.Transaction.TxDelegateH\x00\x1a(\n\x06TxOpen\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.API.AccountType\x1a\x38\n\x06TxSend\x12\x10\n\x08receiver\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x1a$\n\x07TxClaim\x12\x19\n\x11sendTransactionID\x18\x01 \x01(\x0c\x1a$\n\nTxDelegate\x12\x16\n\x0erepresentative\x18\x01 \x01(\x0c\x42\x06\n\x04\x64\x61ta\"Y\n\x05\x42lock\x12 \n\x06header\x18\x01 \x01(\x0b\x32\x10.API.BlockHeader\x12\x1c\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0e.API.BlockData\x12\x10\n\x08\x62lock_id\x18\x03 \x01(\x0c\":\n\x08RawBlock\x12 \n\x06header\x18\x01 \x01(\x0b\x32\x10.API.BlockHeader\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"F\n\x0b\x42lockHeader\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x11\n\tpublicKey\x18\x05 \x01(\x0c\x12\x11\n\ttimestamp\x18\x07 \x01(\x04\"\xaf\x01\n\tBlockData\x12\"\n\x07version\x18\x01 \x01(\x0e\x32\x11.API.BlockVersion\x12#\n\rsignatureType\x18\x02 \x01(\x0e\x32\x0c.API.SigType\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x04\x12\x0e\n\x06height\x18\x05 \x01(\x04\x12\x10\n\x08previous\x18\x06 \x01(\x0c\x12&\n\x0ctransactions\x18\x07 \x03(\x0b\x32\x10.API.Transaction**\n\x0b\x41\x63\x63ountType\x12\x0b\n\x07Managed\x10\x00\x12\x0e\n\nAutonomous\x10\x01*\x16\n\x07SigType\x12\x0b\n\x07\x45\x64\x32\x35\x35\x31\x39\x10\x00*\x16\n\x0c\x42lockVersion\x12\x06\n\x02V1\x10\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'node.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACCOUNTTYPE._serialized_start=815
  _ACCOUNTTYPE._serialized_end=857
  _SIGTYPE._serialized_start=859
  _SIGTYPE._serialized_end=881
  _BLOCKVERSION._serialized_start=883
  _BLOCKVERSION._serialized_end=905
  _EMPTY._serialized_start=23
  _EMPTY._serialized_end=30
  _TRANSACTION._serialized_start=33
  _TRANSACTION._serialized_end=412
  _TRANSACTION_TXOPEN._serialized_start=230
  _TRANSACTION_TXOPEN._serialized_end=270
  _TRANSACTION_TXSEND._serialized_start=272
  _TRANSACTION_TXSEND._serialized_end=328
  _TRANSACTION_TXCLAIM._serialized_start=330
  _TRANSACTION_TXCLAIM._serialized_end=366
  _TRANSACTION_TXDELEGATE._serialized_start=368
  _TRANSACTION_TXDELEGATE._serialized_end=404
  _BLOCK._serialized_start=414
  _BLOCK._serialized_end=503
  _RAWBLOCK._serialized_start=505
  _RAWBLOCK._serialized_end=563
  _BLOCKHEADER._serialized_start=565
  _BLOCKHEADER._serialized_end=635
  _BLOCKDATA._serialized_start=638
  _BLOCKDATA._serialized_end=813
# @@protoc_insertion_point(module_scope)
