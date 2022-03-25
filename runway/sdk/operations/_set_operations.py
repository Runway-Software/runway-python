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
    from typing import Any, Callable, Dict, IO, List, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_createset_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/sets")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_deleteset_request(
    setid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/sets/{setId}")
    path_format_arguments = {
        "setId": _SERIALIZER.url("setid", setid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_addtosetbyids_request(
    targetsetid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/sets/{targetSetId}/members")
    path_format_arguments = {
        "targetSetId": _SERIALIZER.url("targetsetid", targetsetid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if contenttype is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("contenttype", contenttype, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_removefromsetbyids_request(
    targetsetid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/sets/{targetSetId}/members")
    path_format_arguments = {
        "targetSetId": _SERIALIZER.url("targetsetid", targetsetid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if contenttype is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("contenttype", contenttype, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_addtosetbyset_request(
    targetsetid,  # type: str
    sourcesetid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/sets/{targetSetId}/members/set/{sourceSetId}")
    path_format_arguments = {
        "targetSetId": _SERIALIZER.url("targetsetid", targetsetid, 'str'),
        "sourceSetId": _SERIALIZER.url("sourcesetid", sourcesetid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_removefromsetbyset_request(
    targetsetid,  # type: str
    sourcesetid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/sets/{targetSetId}/members/set/{sourceSetId}")
    path_format_arguments = {
        "targetSetId": _SERIALIZER.url("targetsetid", targetsetid, 'str'),
        "sourceSetId": _SERIALIZER.url("sourcesetid", sourcesetid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_getmembercount_request(
    setid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json, text/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/sets/{setId}/count")
    path_format_arguments = {
        "setId": _SERIALIZER.url("setid", setid, 'str'),
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
class setOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~runway.sdk.PyRunway`'s
        :attr:`set` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace
    def createset(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.idResponse"
        """createset.

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

        
        request = build_createset_request(
            template_url=self.createset.metadata['url'],
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

    createset.metadata = {'url': "/api/v2/sets"}  # type: ignore


    @distributed_trace
    def deleteset(
        self,
        setid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """deleteset.

        :param setid:
        :type setid: str
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

        
        request = build_deleteset_request(
            setid=setid,
            template_url=self.deleteset.metadata['url'],
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

    deleteset.metadata = {'url': "/api/v2/sets/{setId}"}  # type: ignore


    @distributed_trace
    def addtosetbyids(
        self,
        targetsetid,  # type: str
        objectids,  # type: List[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """addtosetbyids.

        :param targetsetid:
        :type targetsetid: str
        :param objectids:
        :type objectids: list[str]
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[int]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

        _json = self._serialize.body(objectids, '[str]')

        request = build_addtosetbyids_request(
            targetsetid=targetsetid,
            contenttype=contenttype,
            json=_json,
            template_url=self.addtosetbyids.metadata['url'],
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

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    addtosetbyids.metadata = {'url': "/api/v2/sets/{targetSetId}/members"}  # type: ignore


    @distributed_trace
    def removefromsetbyids(
        self,
        targetsetid,  # type: str
        objectids,  # type: List[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """removefromsetbyids.

        :param targetsetid:
        :type targetsetid: str
        :param objectids:
        :type objectids: list[str]
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[int]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

        _json = self._serialize.body(objectids, '[str]')

        request = build_removefromsetbyids_request(
            targetsetid=targetsetid,
            contenttype=contenttype,
            json=_json,
            template_url=self.removefromsetbyids.metadata['url'],
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

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    removefromsetbyids.metadata = {'url': "/api/v2/sets/{targetSetId}/members"}  # type: ignore


    @distributed_trace
    def addtosetbyset(
        self,
        targetsetid,  # type: str
        sourcesetid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """addtosetbyset.

        :param targetsetid:
        :type targetsetid: str
        :param sourcesetid:
        :type sourcesetid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[int]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_addtosetbyset_request(
            targetsetid=targetsetid,
            sourcesetid=sourcesetid,
            template_url=self.addtosetbyset.metadata['url'],
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

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    addtosetbyset.metadata = {'url': "/api/v2/sets/{targetSetId}/members/set/{sourceSetId}"}  # type: ignore


    @distributed_trace
    def removefromsetbyset(
        self,
        targetsetid,  # type: str
        sourcesetid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """removefromsetbyset.

        :param targetsetid:
        :type targetsetid: str
        :param sourcesetid:
        :type sourcesetid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[int]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_removefromsetbyset_request(
            targetsetid=targetsetid,
            sourcesetid=sourcesetid,
            template_url=self.removefromsetbyset.metadata['url'],
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

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    removefromsetbyset.metadata = {'url': "/api/v2/sets/{targetSetId}/members/set/{sourceSetId}"}  # type: ignore


    @distributed_trace
    def getmembercount(
        self,
        setid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """getmembercount.

        :param setid:
        :type setid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[int]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_getmembercount_request(
            setid=setid,
            template_url=self.getmembercount.metadata['url'],
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

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    getmembercount.metadata = {'url': "/api/v2/sets/{setId}/count"}  # type: ignore

