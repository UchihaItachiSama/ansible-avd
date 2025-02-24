# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: arista/bugexposure.v1/bugexposure.proto, arista/bugexposure.v1/services.gen.proto
# plugin: python-aristaproto
# This file has been @generated

from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Dict,
    List,
    Optional,
)

import aristaproto
import grpclib
from aristaproto.grpc.grpclib_server import ServiceBase

from .... import fmp as ___fmp__
from ... import (
    subscriptions as __subscriptions__,
    time as __time__,
)


if TYPE_CHECKING:
    import grpclib.server
    from aristaproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class Acknowledgement(aristaproto.Enum):
    """
    Acknowledgement is an enumeration key
     for a BugExposure model that defines
     the acknowledgement state for the
     computed bugs
    """

    UNSPECIFIED = 0
    """Unacknowledged and acknowledged bugs will be computed"""

    UNACKNOWLEDGED = 1
    """Only unacknowledged bugs will be computed"""

    ACKNOWLEDGED = 2
    """Only acknowledged bugs will be computed"""


class HighestExposure(aristaproto.Enum):
    """
    HighestExposure is an enumeration
     that defines the options for
     highest exposure
    """

    UNSPECIFIED = 0
    """
    If not given this will be the default value
     and it will compute devices with
     any highest exposure
    """

    NONE = 1
    """Not exposed to bugs"""

    LOW = 2
    """Highest exposure is to a low priority bug"""

    HIGH = 3
    """Highest exposure is to a high priority bug"""


@dataclass(eq=False, repr=False)
class BugExposureKey(aristaproto.Message):
    """
    BugExposureKey is the key type for
     BugExposure model
    """

    device_id: Optional[str] = aristaproto.message_field(
        1, wraps=aristaproto.TYPE_STRING
    )
    """device_id is the device ID"""

    acknowledgement: "Acknowledgement" = aristaproto.enum_field(2)
    """
    acknowledgement is one of the options for
     Acknowledgement enum
    """


@dataclass(eq=False, repr=False)
class BugExposure(aristaproto.Message):
    """
    BugExposure is the state model that represents
     the exposure a device has to bugs
    """

    key: "BugExposureKey" = aristaproto.message_field(1)
    """
    BugExposureKey is the key of
     BugExposure
    """

    bug_ids: "___fmp__.RepeatedInt32" = aristaproto.message_field(2)
    """
    bug_ids is a list of bug alerts affecting the device
     with type Bug
    """

    cve_ids: "___fmp__.RepeatedInt32" = aristaproto.message_field(3)
    """
    cve_ids is a list of bug alerts affecting the device
     with type CVE
    """

    bug_count: Optional[int] = aristaproto.message_field(
        4, wraps=aristaproto.TYPE_INT32
    )
    """
    bug_count is the number of bug alerts
     with type Bug
    """

    cve_count: Optional[int] = aristaproto.message_field(
        5, wraps=aristaproto.TYPE_INT32
    )
    """
    cve_count is the number of bug alerts
     with type CVE
    """

    highest_bug_exposure: "HighestExposure" = aristaproto.enum_field(6)
    """
    highest_bug_exposure is the highest exposure
     with type Bug
    """

    highest_cve_exposure: "HighestExposure" = aristaproto.enum_field(7)
    """
    highest_cve_exposure is the highest exposure
     with type CVE
    """


@dataclass(eq=False, repr=False)
class MetaResponse(aristaproto.Message):
    time: datetime = aristaproto.message_field(1)
    """
    Time holds the timestamp of the last item included in the metadata calculation.
    """

    type: "__subscriptions__.Operation" = aristaproto.enum_field(2)
    """
    Operation indicates how the value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """

    count: Optional[int] = aristaproto.message_field(3, wraps=aristaproto.TYPE_UINT32)
    """
    Count is the number of items present under the conditions of the request.
    """


@dataclass(eq=False, repr=False)
class BugExposureRequest(aristaproto.Message):
    key: "BugExposureKey" = aristaproto.message_field(1)
    """
    Key uniquely identifies a BugExposure instance to retrieve.
     This value must be populated.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the time for which you are interested in the data.
     If no time is given, the server will use the time at which it makes the request.
    """


@dataclass(eq=False, repr=False)
class BugExposureResponse(aristaproto.Message):
    value: "BugExposure" = aristaproto.message_field(1)
    """
    Value is the value requested.
     This structure will be fully-populated as it exists in the datastore. If
     optional fields were not given at creation, these fields will be empty or
     set to default values.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time carries the (UTC) timestamp of the last-modification of the
     BugExposure instance in this response.
    """


@dataclass(eq=False, repr=False)
class BugExposureStreamRequest(aristaproto.Message):
    partial_eq_filter: List["BugExposure"] = aristaproto.message_field(1)
    """
    PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.
     This requires all provided fields to be equal to the response.

     While transparent to users, this field also allows services to optimize internal
     subscriptions if filter(s) are sufficiently specific.
    """

    time: "__time__.TimeBounds" = aristaproto.message_field(3)
    """
    TimeRange allows limiting response data to within a specified time window.
     If this field is populated, at least one of the two time fields are required.

     For GetAll, the fields start and end can be used as follows:

       * end: Returns the state of each BugExposure at end.
         * Each BugExposure response is fully-specified (all fields set).
       * start: Returns the state of each BugExposure at start, followed by updates until now.
         * Each BugExposure response at start is fully-specified, but updates may be partial.
       * start and end: Returns the state of each BugExposure at start, followed by updates
         until end.
         * Each BugExposure response at start is fully-specified, but updates until end may
           be partial.

     This field is not allowed in the Subscribe RPC.
    """


@dataclass(eq=False, repr=False)
class BugExposureStreamResponse(aristaproto.Message):
    value: "BugExposure" = aristaproto.message_field(1)
    """
    Value is a value deemed relevant to the initiating request.
     This structure will always have its key-field populated. Which other fields are
     populated, and why, depends on the value of Operation and what triggered this notification.
    """

    time: datetime = aristaproto.message_field(2)
    """Time holds the timestamp of this BugExposure's last modification."""

    type: "__subscriptions__.Operation" = aristaproto.enum_field(3)
    """
    Operation indicates how the BugExposure value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """


class BugExposureServiceStub(aristaproto.ServiceStub):
    async def get_one(
        self,
        bug_exposure_request: "BugExposureRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "BugExposureResponse":
        return await self._unary_unary(
            "/arista.bugexposure.v1.BugExposureService/GetOne",
            bug_exposure_request,
            BugExposureResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_all(
        self,
        bug_exposure_stream_request: "BugExposureStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["BugExposureStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.bugexposure.v1.BugExposureService/GetAll",
            bug_exposure_stream_request,
            BugExposureStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def subscribe(
        self,
        bug_exposure_stream_request: "BugExposureStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["BugExposureStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.bugexposure.v1.BugExposureService/Subscribe",
            bug_exposure_stream_request,
            BugExposureStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def get_meta(
        self,
        bug_exposure_stream_request: "BugExposureStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MetaResponse":
        return await self._unary_unary(
            "/arista.bugexposure.v1.BugExposureService/GetMeta",
            bug_exposure_stream_request,
            MetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def subscribe_meta(
        self,
        bug_exposure_stream_request: "BugExposureStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["MetaResponse"]:
        async for response in self._unary_stream(
            "/arista.bugexposure.v1.BugExposureService/SubscribeMeta",
            bug_exposure_stream_request,
            MetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class BugExposureServiceBase(ServiceBase):

    async def get_one(
        self, bug_exposure_request: "BugExposureRequest"
    ) -> "BugExposureResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_all(
        self, bug_exposure_stream_request: "BugExposureStreamRequest"
    ) -> AsyncIterator["BugExposureStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe(
        self, bug_exposure_stream_request: "BugExposureStreamRequest"
    ) -> AsyncIterator["BugExposureStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_meta(
        self, bug_exposure_stream_request: "BugExposureStreamRequest"
    ) -> "MetaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe_meta(
        self, bug_exposure_stream_request: "BugExposureStreamRequest"
    ) -> AsyncIterator["MetaResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_one(
        self, stream: "grpclib.server.Stream[BugExposureRequest, BugExposureResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_one(request)
        await stream.send_message(response)

    async def __rpc_get_all(
        self,
        stream: "grpclib.server.Stream[BugExposureStreamRequest, BugExposureStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_all,
            stream,
            request,
        )

    async def __rpc_subscribe(
        self,
        stream: "grpclib.server.Stream[BugExposureStreamRequest, BugExposureStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe,
            stream,
            request,
        )

    async def __rpc_get_meta(
        self, stream: "grpclib.server.Stream[BugExposureStreamRequest, MetaResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_meta(request)
        await stream.send_message(response)

    async def __rpc_subscribe_meta(
        self, stream: "grpclib.server.Stream[BugExposureStreamRequest, MetaResponse]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe_meta,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/arista.bugexposure.v1.BugExposureService/GetOne": grpclib.const.Handler(
                self.__rpc_get_one,
                grpclib.const.Cardinality.UNARY_UNARY,
                BugExposureRequest,
                BugExposureResponse,
            ),
            "/arista.bugexposure.v1.BugExposureService/GetAll": grpclib.const.Handler(
                self.__rpc_get_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                BugExposureStreamRequest,
                BugExposureStreamResponse,
            ),
            "/arista.bugexposure.v1.BugExposureService/Subscribe": grpclib.const.Handler(
                self.__rpc_subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                BugExposureStreamRequest,
                BugExposureStreamResponse,
            ),
            "/arista.bugexposure.v1.BugExposureService/GetMeta": grpclib.const.Handler(
                self.__rpc_get_meta,
                grpclib.const.Cardinality.UNARY_UNARY,
                BugExposureStreamRequest,
                MetaResponse,
            ),
            "/arista.bugexposure.v1.BugExposureService/SubscribeMeta": grpclib.const.Handler(
                self.__rpc_subscribe_meta,
                grpclib.const.Cardinality.UNARY_STREAM,
                BugExposureStreamRequest,
                MetaResponse,
            ),
        }
