# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.7.6, generator: @autorest/python@5.14.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._tag_operations import build_addtags_request, build_deletetags_request, build_gettags_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class tagOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~runway.sdk.aio.PyRunway`'s
        :attr:`tag` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def addtags(
        self,
        request: "_models.tagRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> IO:
        """addtags.

        :param request:
        :type request: ~runway.sdk.models.tagRequest
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

        _json = self._serialize.body(request, 'tagRequest')

        request = build_addtags_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.addtags.metadata['url'],
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

    addtags.metadata = {'url': "/api/v2/tags"}  # type: ignore


    @distributed_trace_async
    async def deletetags(
        self,
        request: "_models.tagRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> IO:
        """deletetags.

        :param request:
        :type request: ~runway.sdk.models.tagRequest
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

        _json = self._serialize.body(request, 'tagRequest')

        request = build_deletetags_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.deletetags.metadata['url'],
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

    deletetags.metadata = {'url': "/api/v2/tags"}  # type: ignore


    @distributed_trace_async
    async def gettags(
        self,
        **kwargs: Any
    ) -> List["_models.tagView"]:
        """gettags.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of tagView, or the result of cls(response)
        :rtype: list[~runway.sdk.models.tagView]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.tagView"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_gettags_request(
            template_url=self.gettags.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('[tagView]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    gettags.metadata = {'url': "/api/v2/tags"}  # type: ignore

