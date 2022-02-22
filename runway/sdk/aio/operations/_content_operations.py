# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.7.6, generator: @autorest/python@5.12.6)
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
from ...operations._content_operations import build_download_public_file_request, build_download_request, build_get_public_downloads_request, build_get_public_file_info_request, build_upload_request, build_version_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ContentOperations:
    """ContentOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~Runway.Python.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def version(
        self,
        **kwargs: Any
    ) -> "_models.VersionResponse":
        """version.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VersionResponse, or the result of cls(response)
        :rtype: ~Runway.Python.models.VersionResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VersionResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_version_request(
            platform=self._config.platform,
            template_url=self.version.metadata['url'],
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

        deserialized = self._deserialize('VersionResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    version.metadata = {'url': "/api/v2/content/version"}  # type: ignore


    @distributed_trace_async
    async def download_public_file(
        self,
        key: Optional[str] = None,
        id: Optional[str] = None,
        **kwargs: Any
    ) -> IO:
        """download_public_file.

        :param key:
        :type key: str
        :param id:
        :type id: str
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

        
        request = build_download_public_file_request(
            key=key,
            platform=self._config.platform,
            id=id,
            template_url=self.download_public_file.metadata['url'],
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

    download_public_file.metadata = {'url': "/api/v2/content/public"}  # type: ignore


    @distributed_trace_async
    async def get_public_downloads(
        self,
        **kwargs: Any
    ) -> List["_models.ContentView"]:
        """get_public_downloads.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ContentView, or the result of cls(response)
        :rtype: list[~Runway.Python.models.ContentView]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.ContentView"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_public_downloads_request(
            template_url=self.get_public_downloads.metadata['url'],
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

        deserialized = self._deserialize('[ContentView]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_public_downloads.metadata = {'url': "/api/v2/content/public/available"}  # type: ignore


    @distributed_trace_async
    async def get_public_file_info(
        self,
        key: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.ContentInfo":
        """get_public_file_info.

        :param key:
        :type key: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentInfo, or the result of cls(response)
        :rtype: ~Runway.Python.models.ContentInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ContentInfo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_public_file_info_request(
            key=key,
            platform=self._config.platform,
            template_url=self.get_public_file_info.metadata['url'],
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

        deserialized = self._deserialize('ContentInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_public_file_info.metadata = {'url': "/api/v2/content/public/info"}  # type: ignore


    @distributed_trace_async
    async def upload(
        self,
        **kwargs: Any
    ) -> "_models.IdResponse":
        """upload.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IdResponse, or the result of cls(response)
        :rtype: ~Runway.Python.models.IdResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.IdResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_upload_request(
            template_url=self.upload.metadata['url'],
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

        deserialized = self._deserialize('IdResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload.metadata = {'url': "/api/v2/content"}  # type: ignore


    @distributed_trace_async
    async def download(
        self,
        content_id: str,
        **kwargs: Any
    ) -> IO:
        """download.

        :param content_id:
        :type content_id: str
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

        
        request = build_download_request(
            content_id=content_id,
            template_url=self.download.metadata['url'],
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

    download.metadata = {'url': "/api/v2/content/{contentId}"}  # type: ignore

