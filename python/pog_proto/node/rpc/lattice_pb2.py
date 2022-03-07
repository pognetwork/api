# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node/rpc/lattice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from node import api_pb2 as node_dot_api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16node/rpc/lattice.proto\x12\x07LATTICE\x1a\x0enode/api.proto\"!\n\x0e\x42\x61lanceRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"\x1f\n\x0c\x42\x61lanceReply\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04\"6\n\x12\x42lockHeightRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0f\n\x07getNext\x18\x02 \x01(\x08\"&\n\x10\x42lockHeightReply\x12\x12\n\nnextHeight\x18\x01 \x01(\x04\"8\n\x12VotingPowerRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x11\n\tgetActive\x18\x02 \x01(\x08\"!\n\x10VotingPowerReply\x12\r\n\x05power\x18\x01 \x01(\r\" \n\x10\x42lockByIDRequest\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\"+\n\x0e\x42lockByIDReply\x12\x19\n\x05\x62lock\x18\x01 \x01(\x0b\x32\n.API.Block\"\"\n\x0f\x44\x65legateRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"(\n\rDelegateReply\x12\x17\n\x0f\x64\x65legateAddress\x18\x01 \x01(\x0c\"/\n\x11PendingBlockReply\x12\x1a\n\x06\x62locks\x18\x01 \x03(\x0b\x32\n.API.Block\"?\n\x15UnacknowledgedTXReply\x12&\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x10.API.Transaction\"&\n\rTXByIDRequest\x12\x15\n\rtransactionID\x18\x01 \x01(\x0c\"4\n\x0bTXByIDReply\x12%\n\x0btransaction\x18\x01 \x01(\x0b\x32\x10.API.Transaction\"1\n\x10TXByIndexRequest\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\r\n\x05index\x18\x02 \x01(\x04\"7\n\x0eTXByIndexReply\x12%\n\x0btransaction\x18\x01 \x01(\x0b\x32\x10.API.Transaction\"\x07\n\x05\x45mpty2\xe6\x04\n\x07Lattice\x12<\n\nGetBalance\x12\x17.LATTICE.BalanceRequest\x1a\x15.LATTICE.BalanceReply\x12H\n\x0eGetBlockHeight\x12\x1b.LATTICE.BlockHeightRequest\x1a\x19.LATTICE.BlockHeightReply\x12H\n\x0eGetVotingPower\x12\x1b.LATTICE.VotingPowerRequest\x1a\x19.LATTICE.VotingPowerReply\x12\x42\n\x0cGetBlockByID\x12\x19.LATTICE.BlockByIDRequest\x1a\x17.LATTICE.BlockByIDReply\x12?\n\x0bGetDelegate\x12\x18.LATTICE.DelegateRequest\x1a\x16.LATTICE.DelegateReply\x12>\n\x10GetPendingBlocks\x12\x0e.LATTICE.Empty\x1a\x1a.LATTICE.PendingBlockReply\x12\x45\n\x13GetUnacknowledgedTX\x12\x0e.LATTICE.Empty\x1a\x1e.LATTICE.UnacknowledgedTXReply\x12\x39\n\tGetTXByID\x12\x16.LATTICE.TXByIDRequest\x1a\x14.LATTICE.TXByIDReply\x12\x42\n\x0cGetTXByIndex\x12\x19.LATTICE.TXByIndexRequest\x1a\x17.LATTICE.TXByIndexReplyb\x06proto3')



_BALANCEREQUEST = DESCRIPTOR.message_types_by_name['BalanceRequest']
_BALANCEREPLY = DESCRIPTOR.message_types_by_name['BalanceReply']
_BLOCKHEIGHTREQUEST = DESCRIPTOR.message_types_by_name['BlockHeightRequest']
_BLOCKHEIGHTREPLY = DESCRIPTOR.message_types_by_name['BlockHeightReply']
_VOTINGPOWERREQUEST = DESCRIPTOR.message_types_by_name['VotingPowerRequest']
_VOTINGPOWERREPLY = DESCRIPTOR.message_types_by_name['VotingPowerReply']
_BLOCKBYIDREQUEST = DESCRIPTOR.message_types_by_name['BlockByIDRequest']
_BLOCKBYIDREPLY = DESCRIPTOR.message_types_by_name['BlockByIDReply']
_DELEGATEREQUEST = DESCRIPTOR.message_types_by_name['DelegateRequest']
_DELEGATEREPLY = DESCRIPTOR.message_types_by_name['DelegateReply']
_PENDINGBLOCKREPLY = DESCRIPTOR.message_types_by_name['PendingBlockReply']
_UNACKNOWLEDGEDTXREPLY = DESCRIPTOR.message_types_by_name['UnacknowledgedTXReply']
_TXBYIDREQUEST = DESCRIPTOR.message_types_by_name['TXByIDRequest']
_TXBYIDREPLY = DESCRIPTOR.message_types_by_name['TXByIDReply']
_TXBYINDEXREQUEST = DESCRIPTOR.message_types_by_name['TXByIndexRequest']
_TXBYINDEXREPLY = DESCRIPTOR.message_types_by_name['TXByIndexReply']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
BalanceRequest = _reflection.GeneratedProtocolMessageType('BalanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEREQUEST,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.BalanceRequest)
  })
_sym_db.RegisterMessage(BalanceRequest)

BalanceReply = _reflection.GeneratedProtocolMessageType('BalanceReply', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.BalanceReply)
  })
_sym_db.RegisterMessage(BalanceReply)

BlockHeightRequest = _reflection.GeneratedProtocolMessageType('BlockHeightRequest', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEIGHTREQUEST,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.BlockHeightRequest)
  })
_sym_db.RegisterMessage(BlockHeightRequest)

BlockHeightReply = _reflection.GeneratedProtocolMessageType('BlockHeightReply', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEIGHTREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.BlockHeightReply)
  })
_sym_db.RegisterMessage(BlockHeightReply)

VotingPowerRequest = _reflection.GeneratedProtocolMessageType('VotingPowerRequest', (_message.Message,), {
  'DESCRIPTOR' : _VOTINGPOWERREQUEST,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.VotingPowerRequest)
  })
_sym_db.RegisterMessage(VotingPowerRequest)

VotingPowerReply = _reflection.GeneratedProtocolMessageType('VotingPowerReply', (_message.Message,), {
  'DESCRIPTOR' : _VOTINGPOWERREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.VotingPowerReply)
  })
_sym_db.RegisterMessage(VotingPowerReply)

BlockByIDRequest = _reflection.GeneratedProtocolMessageType('BlockByIDRequest', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKBYIDREQUEST,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.BlockByIDRequest)
  })
_sym_db.RegisterMessage(BlockByIDRequest)

BlockByIDReply = _reflection.GeneratedProtocolMessageType('BlockByIDReply', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKBYIDREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.BlockByIDReply)
  })
_sym_db.RegisterMessage(BlockByIDReply)

DelegateRequest = _reflection.GeneratedProtocolMessageType('DelegateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATEREQUEST,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.DelegateRequest)
  })
_sym_db.RegisterMessage(DelegateRequest)

DelegateReply = _reflection.GeneratedProtocolMessageType('DelegateReply', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATEREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.DelegateReply)
  })
_sym_db.RegisterMessage(DelegateReply)

PendingBlockReply = _reflection.GeneratedProtocolMessageType('PendingBlockReply', (_message.Message,), {
  'DESCRIPTOR' : _PENDINGBLOCKREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.PendingBlockReply)
  })
_sym_db.RegisterMessage(PendingBlockReply)

UnacknowledgedTXReply = _reflection.GeneratedProtocolMessageType('UnacknowledgedTXReply', (_message.Message,), {
  'DESCRIPTOR' : _UNACKNOWLEDGEDTXREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.UnacknowledgedTXReply)
  })
_sym_db.RegisterMessage(UnacknowledgedTXReply)

TXByIDRequest = _reflection.GeneratedProtocolMessageType('TXByIDRequest', (_message.Message,), {
  'DESCRIPTOR' : _TXBYIDREQUEST,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.TXByIDRequest)
  })
_sym_db.RegisterMessage(TXByIDRequest)

TXByIDReply = _reflection.GeneratedProtocolMessageType('TXByIDReply', (_message.Message,), {
  'DESCRIPTOR' : _TXBYIDREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.TXByIDReply)
  })
_sym_db.RegisterMessage(TXByIDReply)

TXByIndexRequest = _reflection.GeneratedProtocolMessageType('TXByIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _TXBYINDEXREQUEST,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.TXByIndexRequest)
  })
_sym_db.RegisterMessage(TXByIndexRequest)

TXByIndexReply = _reflection.GeneratedProtocolMessageType('TXByIndexReply', (_message.Message,), {
  'DESCRIPTOR' : _TXBYINDEXREPLY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.TXByIndexReply)
  })
_sym_db.RegisterMessage(TXByIndexReply)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'node.rpc.lattice_pb2'
  # @@protoc_insertion_point(class_scope:LATTICE.Empty)
  })
_sym_db.RegisterMessage(Empty)

_LATTICE = DESCRIPTOR.services_by_name['Lattice']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BALANCEREQUEST._serialized_start=51
  _BALANCEREQUEST._serialized_end=84
  _BALANCEREPLY._serialized_start=86
  _BALANCEREPLY._serialized_end=117
  _BLOCKHEIGHTREQUEST._serialized_start=119
  _BLOCKHEIGHTREQUEST._serialized_end=173
  _BLOCKHEIGHTREPLY._serialized_start=175
  _BLOCKHEIGHTREPLY._serialized_end=213
  _VOTINGPOWERREQUEST._serialized_start=215
  _VOTINGPOWERREQUEST._serialized_end=271
  _VOTINGPOWERREPLY._serialized_start=273
  _VOTINGPOWERREPLY._serialized_end=306
  _BLOCKBYIDREQUEST._serialized_start=308
  _BLOCKBYIDREQUEST._serialized_end=340
  _BLOCKBYIDREPLY._serialized_start=342
  _BLOCKBYIDREPLY._serialized_end=385
  _DELEGATEREQUEST._serialized_start=387
  _DELEGATEREQUEST._serialized_end=421
  _DELEGATEREPLY._serialized_start=423
  _DELEGATEREPLY._serialized_end=463
  _PENDINGBLOCKREPLY._serialized_start=465
  _PENDINGBLOCKREPLY._serialized_end=512
  _UNACKNOWLEDGEDTXREPLY._serialized_start=514
  _UNACKNOWLEDGEDTXREPLY._serialized_end=577
  _TXBYIDREQUEST._serialized_start=579
  _TXBYIDREQUEST._serialized_end=617
  _TXBYIDREPLY._serialized_start=619
  _TXBYIDREPLY._serialized_end=671
  _TXBYINDEXREQUEST._serialized_start=673
  _TXBYINDEXREQUEST._serialized_end=722
  _TXBYINDEXREPLY._serialized_start=724
  _TXBYINDEXREPLY._serialized_end=779
  _EMPTY._serialized_start=781
  _EMPTY._serialized_end=788
  _LATTICE._serialized_start=791
  _LATTICE._serialized_end=1405
# @@protoc_insertion_point(module_scope)