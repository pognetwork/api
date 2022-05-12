# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node/rpc/lattice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from node import api_pb2 as node_dot_api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16node/rpc/lattice.proto\x12\x07LATTICE\x1a\x0enode/api.proto\"$\n\x13\x42lockSpamIndexReply\x12\r\n\x05value\x18\x01 \x01(\x02\"c\n\x10GetBlocksRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x1f\n\x06sortBy\x18\x03 \x01(\x0e\x32\x0f.LATTICE.sortBy\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0c\",\n\x0eGetBlocksReply\x12\x1a\n\x06\x62locks\x18\x01 \x03(\x0b\x32\n.API.Block\"!\n\x0e\x42\x61lanceRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"\x1f\n\x0c\x42\x61lanceReply\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04\"6\n\x12\x42lockHeightRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0f\n\x07getNext\x18\x02 \x01(\x08\"&\n\x10\x42lockHeightReply\x12\x12\n\nnextHeight\x18\x01 \x01(\x04\"8\n\x12VotingPowerRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x11\n\tgetActive\x18\x02 \x01(\x08\"!\n\x10VotingPowerReply\x12\r\n\x05power\x18\x01 \x01(\x04\" \n\x10\x42lockByIDRequest\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\"+\n\x0e\x42lockByIDReply\x12\x19\n\x05\x62lock\x18\x01 \x01(\x0b\x32\n.API.Block\"\"\n\x0f\x44\x65legateRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"(\n\rDelegateReply\x12\x17\n\x0f\x64\x65legateAddress\x18\x01 \x01(\x0c\"/\n\x11PendingBlockReply\x12\x1a\n\x06\x62locks\x18\x01 \x03(\x0b\x32\n.API.Block\"?\n\x15UnacknowledgedTXReply\x12&\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x10.API.Transaction\"&\n\rTXByIDRequest\x12\x15\n\rtransactionID\x18\x01 \x01(\x0c\"4\n\x0bTXByIDReply\x12%\n\x0btransaction\x18\x01 \x01(\x0b\x32\x10.API.Transaction\"1\n\x10TXByIndexRequest\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\r\n\x05index\x18\x02 \x01(\x04\"7\n\x0eTXByIndexReply\x12%\n\x0btransaction\x18\x01 \x01(\x0b\x32\x10.API.Transaction\"\x07\n\x05\x45mpty*!\n\x06sortBy\x12\x08\n\x04\x64\x61ta\x10\x00\x12\r\n\tdata_desc\x10\x01\x32\x97\x06\n\x07Lattice\x12<\n\nGetBalance\x12\x17.LATTICE.BalanceRequest\x1a\x15.LATTICE.BalanceReply\x12H\n\x0eGetBlockHeight\x12\x1b.LATTICE.BlockHeightRequest\x1a\x19.LATTICE.BlockHeightReply\x12H\n\x0eGetVotingPower\x12\x1b.LATTICE.VotingPowerRequest\x1a\x19.LATTICE.VotingPowerReply\x12\x42\n\x0cGetBlockByID\x12\x19.LATTICE.BlockByIDRequest\x1a\x17.LATTICE.BlockByIDReply\x12?\n\x0bGetDelegate\x12\x18.LATTICE.DelegateRequest\x1a\x16.LATTICE.DelegateReply\x12>\n\x10GetPendingBlocks\x12\x0e.LATTICE.Empty\x1a\x1a.LATTICE.PendingBlockReply\x12?\n\tGetBlocks\x12\x19.LATTICE.GetBlocksRequest\x1a\x17.LATTICE.GetBlocksReply\x12\x45\n\x13GetUnacknowledgedTX\x12\x0e.LATTICE.Empty\x1a\x1e.LATTICE.UnacknowledgedTXReply\x12\x39\n\tGetTXByID\x12\x16.LATTICE.TXByIDRequest\x1a\x14.LATTICE.TXByIDReply\x12\x42\n\x0cGetTXByIndex\x12\x19.LATTICE.TXByIndexRequest\x1a\x17.LATTICE.TXByIndexReply\x12@\n\x11GetBlockSpamIndex\x12\r.API.RawBlock\x1a\x1c.LATTICE.BlockSpamIndexReply\x12,\n\x0bSubmitBlock\x12\r.API.RawBlock\x1a\x0e.LATTICE.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'node.rpc.lattice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SORTBY._serialized_start=975
  _SORTBY._serialized_end=1008
  _BLOCKSPAMINDEXREPLY._serialized_start=51
  _BLOCKSPAMINDEXREPLY._serialized_end=87
  _GETBLOCKSREQUEST._serialized_start=89
  _GETBLOCKSREQUEST._serialized_end=188
  _GETBLOCKSREPLY._serialized_start=190
  _GETBLOCKSREPLY._serialized_end=234
  _BALANCEREQUEST._serialized_start=236
  _BALANCEREQUEST._serialized_end=269
  _BALANCEREPLY._serialized_start=271
  _BALANCEREPLY._serialized_end=302
  _BLOCKHEIGHTREQUEST._serialized_start=304
  _BLOCKHEIGHTREQUEST._serialized_end=358
  _BLOCKHEIGHTREPLY._serialized_start=360
  _BLOCKHEIGHTREPLY._serialized_end=398
  _VOTINGPOWERREQUEST._serialized_start=400
  _VOTINGPOWERREQUEST._serialized_end=456
  _VOTINGPOWERREPLY._serialized_start=458
  _VOTINGPOWERREPLY._serialized_end=491
  _BLOCKBYIDREQUEST._serialized_start=493
  _BLOCKBYIDREQUEST._serialized_end=525
  _BLOCKBYIDREPLY._serialized_start=527
  _BLOCKBYIDREPLY._serialized_end=570
  _DELEGATEREQUEST._serialized_start=572
  _DELEGATEREQUEST._serialized_end=606
  _DELEGATEREPLY._serialized_start=608
  _DELEGATEREPLY._serialized_end=648
  _PENDINGBLOCKREPLY._serialized_start=650
  _PENDINGBLOCKREPLY._serialized_end=697
  _UNACKNOWLEDGEDTXREPLY._serialized_start=699
  _UNACKNOWLEDGEDTXREPLY._serialized_end=762
  _TXBYIDREQUEST._serialized_start=764
  _TXBYIDREQUEST._serialized_end=802
  _TXBYIDREPLY._serialized_start=804
  _TXBYIDREPLY._serialized_end=856
  _TXBYINDEXREQUEST._serialized_start=858
  _TXBYINDEXREQUEST._serialized_end=907
  _TXBYINDEXREPLY._serialized_start=909
  _TXBYINDEXREPLY._serialized_end=964
  _EMPTY._serialized_start=966
  _EMPTY._serialized_end=973
  _LATTICE._serialized_start=1011
  _LATTICE._serialized_end=1802
# @@protoc_insertion_point(module_scope)
