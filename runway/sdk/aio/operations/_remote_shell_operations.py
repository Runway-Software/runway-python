# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.7.6, generator: @autorest/python@5.14.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._remote_shell_operations import build_shellcancel_request, build_shellping_request, build_shellwrite_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class remoteShellOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~runway.sdk.aio.PyRunway`'s
        :attr:`remote_shell` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def shellwrite(
        self,
        request: "_models.remoteShellRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> str:
        """shellwrite.

        :param request:
        :type request: ~runway.sdk.models.remoteShellRequest
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _json = self._serialize.body(request, 'remoteShellRequest')

        request = build_shellwrite_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.shellwrite.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            deserialized = self._deserialize('str', pipeline_response)

        if response.status_code == 200:
            deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    shellwrite.metadata = {'url': "/api/v2/shell"}  # type: ignore


    @distributed_trace_async
    async def shellcancel(
        self,
        request: "_models.remoteShellDeleteRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> IO:
        """shellcancel.

        :param request:
        :type request: ~runway.sdk.models.remoteShellDeleteRequest
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _json = self._serialize.body(request, 'remoteShellDeleteRequest')

        request = build_shellcancel_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.shellcancel.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=True,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    shellcancel.metadata = {'url': "/api/v2/shell"}  # type: ignore


    @distributed_trace_async
    async def shellping(
        self,
        request: "_models.remoteShellPingRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> IO:
        """shellping.

        :param request:
        :type request: ~runway.sdk.models.remoteShellPingRequest
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _json = self._serialize.body(request, 'remoteShellPingRequest')

        request = build_shellping_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.shellping.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=True,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    shellping.metadata = {'url': "/api/v2/shell/ping"}  # type: ignore

