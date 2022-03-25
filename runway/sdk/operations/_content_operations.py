# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.7.6, generator: @autorest/python@5.14.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_version_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    platform = kwargs.pop('platform', None)  # type: Optional[Union[str, "_models.enum6"]]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/content/version")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if platform is not None:
        _query_parameters['platform'] = _SERIALIZER.query("platform", platform, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_downloadpublicfile_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    key = kwargs.pop('key', None)  # type: Optional[str]
    platform = kwargs.pop('platform', None)  # type: Optional[Union[str, "_models.enum6"]]
    id = kwargs.pop('id', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/content/public")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if key is not None:
        _query_parameters['key'] = _SERIALIZER.query("key", key, 'str')
    if platform is not None:
        _query_parameters['platform'] = _SERIALIZER.query("platform", platform, 'str')
    if id is not None:
        _query_parameters['id'] = _SERIALIZER.query("id", id, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_getpublicdownloads_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json, text/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/content/public/available")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_getpublicfileinfo_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    key = kwargs.pop('key', None)  # type: Optional[str]
    platform = kwargs.pop('platform', None)  # type: Optional[Union[str, "_models.enum6"]]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/content/public/info")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if key is not None:
        _query_parameters['key'] = _SERIALIZER.query("key", key, 'str')
    if platform is not None:
        _query_parameters['platform'] = _SERIALIZER.query("platform", platform, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_upload_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/content")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_download_request(
    contentid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/content/{contentId}")
    path_format_arguments = {
        "contentId": _SERIALIZER.url("contentid", contentid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class contentOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~runway.sdk.PyRunway`'s
        :attr:`content` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace
    def version(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.versionResponse"
        """version.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: versionResponse, or the result of cls(response)
        :rtype: ~runway.sdk.models.versionResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.versionResponse"]
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('versionResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    version.metadata = {'url': "/api/v2/content/version"}  # type: ignore


    @distributed_trace
    def downloadpublicfile(
        self,
        key=None,  # type: Optional[str]
        id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """downloadpublicfile.

        :param key:  Default value is None.
        :type key: str
        :param id:  Default value is None.
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

        
        request = build_downloadpublicfile_request(
            key=key,
            platform=self._config.platform,
            id=id,
            template_url=self.downloadpublicfile.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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

    downloadpublicfile.metadata = {'url': "/api/v2/content/public"}  # type: ignore


    @distributed_trace
    def getpublicdownloads(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.contentView"]
        """getpublicdownloads.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of contentView, or the result of cls(response)
        :rtype: list[~runway.sdk.models.contentView]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.contentView"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_getpublicdownloads_request(
            template_url=self.getpublicdownloads.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('[contentView]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    getpublicdownloads.metadata = {'url': "/api/v2/content/public/available"}  # type: ignore


    @distributed_trace
    def getpublicfileinfo(
        self,
        key=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.contentInfo"
        """getpublicfileinfo.

        :param key:  Default value is None.
        :type key: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: contentInfo, or the result of cls(response)
        :rtype: ~runway.sdk.models.contentInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.contentInfo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_getpublicfileinfo_request(
            key=key,
            platform=self._config.platform,
            template_url=self.getpublicfileinfo.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('contentInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    getpublicfileinfo.metadata = {'url': "/api/v2/content/public/info"}  # type: ignore


    @distributed_trace
    def upload(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.idResponse"
        """upload.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: idResponse, or the result of cls(response)
        :rtype: ~runway.sdk.models.idResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.idResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_upload_request(
            template_url=self.upload.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('idResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload.metadata = {'url': "/api/v2/content"}  # type: ignore


    @distributed_trace
    def download(
        self,
        contentid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """download.

        :param contentid:
        :type contentid: str
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
            contentid=contentid,
            template_url=self.download.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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

