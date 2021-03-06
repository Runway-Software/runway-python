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

def build_deletebyset_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners")

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


def build_list_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_deletebyid_request(
    runnerid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/{runnerId}")
    path_format_arguments = {
        "runnerId": _SERIALIZER.url("runnerid", runnerid, 'str'),
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


def build_load_request(
    runnerid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/{runnerId}")
    path_format_arguments = {
        "runnerId": _SERIALIZER.url("runnerid", runnerid, 'str'),
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


def build_begindissolverunners_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/dissolve")

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


def build_completedissolverunner_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/dissolved")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_querybygroupid_request(
    groupid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/group/{groupId}")
    path_format_arguments = {
        "groupId": _SERIALIZER.url("groupid", groupid, 'str'),
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


def build_querybyip_request(
    ipaddress,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/ip/{ipAddress}")
    path_format_arguments = {
        "ipAddress": _SERIALIZER.url("ipaddress", ipaddress, 'str'),
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


def build_gettags_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/tags")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/query")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if contenttype is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("contenttype", contenttype, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_count_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/count")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_countquery_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/count/query")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if contenttype is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("contenttype", contenttype, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_getqueryschema_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/query/schema")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_savequerytoset_request(
    setid,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/api/v2/runners/query/set/{setId}")
    path_format_arguments = {
        "setId": _SERIALIZER.url("setid", setid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if contenttype is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("contenttype", contenttype, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class runnerOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~runway.sdk.PyRunway`'s
        :attr:`runner` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace
    def deletebyset(
        self,
        setrequest,  # type: "_models.idRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """deletebyset.

        :param setrequest:
        :type setrequest: ~runway.sdk.models.idRequest
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

        contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

        _json = self._serialize.body(setrequest, 'idRequest')

        request = build_deletebyset_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.deletebyset.metadata['url'],
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

    deletebyset.metadata = {'url': "/api/v2/runners"}  # type: ignore


    @distributed_trace
    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.queryResponseOfIRunnerQueryView"
        """list.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryResponseOfIRunnerQueryView, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryResponseOfIRunnerQueryView
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryResponseOfIRunnerQueryView"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_request(
            template_url=self.list.metadata['url'],
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

        deserialized = self._deserialize('queryResponseOfIRunnerQueryView', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': "/api/v2/runners"}  # type: ignore


    @distributed_trace
    def deletebyid(
        self,
        runnerid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """deletebyid.

        :param runnerid:
        :type runnerid: str
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

        
        request = build_deletebyid_request(
            runnerid=runnerid,
            template_url=self.deletebyid.metadata['url'],
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

    deletebyid.metadata = {'url': "/api/v2/runners/{runnerId}"}  # type: ignore


    @distributed_trace
    def load(
        self,
        runnerid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.runwayRunner"
        """load.

        :param runnerid:
        :type runnerid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: runwayRunner, or the result of cls(response)
        :rtype: ~runway.sdk.models.runwayRunner
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.runwayRunner"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_load_request(
            runnerid=runnerid,
            template_url=self.load.metadata['url'],
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

        deserialized = self._deserialize('runwayRunner', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    load.metadata = {'url': "/api/v2/runners/{runnerId}"}  # type: ignore


    @distributed_trace
    def begindissolverunners(
        self,
        request,  # type: "_models.dissolveRunnersRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """begindissolverunners.

        :param request:
        :type request: ~runway.sdk.models.dissolveRunnersRequest
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json", "text/json", and "application/*+json". Default value is "application/json".
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

        contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

        _json = self._serialize.body(request, 'dissolveRunnersRequest')

        request = build_begindissolverunners_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.begindissolverunners.metadata['url'],
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

    begindissolverunners.metadata = {'url': "/api/v2/runners/dissolve"}  # type: ignore


    @distributed_trace
    def completedissolverunner(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """completedissolverunner.

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

        
        request = build_completedissolverunner_request(
            template_url=self.completedissolverunner.metadata['url'],
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

    completedissolverunner.metadata = {'url': "/api/v2/runners/dissolved"}  # type: ignore


    @distributed_trace
    def querybygroupid(
        self,
        groupid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.queryRunnersResponse"
        """querybygroupid.

        :param groupid:
        :type groupid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryRunnersResponse, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryRunnersResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryRunnersResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_querybygroupid_request(
            groupid=groupid,
            template_url=self.querybygroupid.metadata['url'],
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

        deserialized = self._deserialize('queryRunnersResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    querybygroupid.metadata = {'url': "/api/v2/runners/group/{groupId}"}  # type: ignore


    @distributed_trace
    def querybyip(
        self,
        ipaddress,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.queryRunnersResponse"
        """querybyip.

        :param ipaddress:
        :type ipaddress: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryRunnersResponse, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryRunnersResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryRunnersResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_querybyip_request(
            ipaddress=ipaddress,
            template_url=self.querybyip.metadata['url'],
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

        deserialized = self._deserialize('queryRunnersResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    querybyip.metadata = {'url': "/api/v2/runners/ip/{ipAddress}"}  # type: ignore


    @distributed_trace
    def gettags(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.tagView"]
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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

    gettags.metadata = {'url': "/api/v2/runners/tags"}  # type: ignore


    @distributed_trace
    def query(
        self,
        query,  # type: "_models.query"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.queryResponseOfIRunnerQueryView"
        """query.

        :param query:
        :type query: ~runway.sdk.models.query
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryResponseOfIRunnerQueryView, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryResponseOfIRunnerQueryView
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryResponseOfIRunnerQueryView"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        contenttype = kwargs.pop('contenttype', "application/json")  # type: Optional[str]

        _json = self._serialize.body(query, 'query')

        request = build_query_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.query.metadata['url'],
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

        deserialized = self._deserialize('queryResponseOfIRunnerQueryView', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query.metadata = {'url': "/api/v2/runners/query"}  # type: ignore


    @distributed_trace
    def count(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """count.

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

        
        request = build_count_request(
            template_url=self.count.metadata['url'],
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

    count.metadata = {'url': "/api/v2/runners/count"}  # type: ignore


    @distributed_trace
    def countquery(
        self,
        query,  # type: "_models.query"
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """countquery.

        :param query:
        :type query: ~runway.sdk.models.query
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

        _json = self._serialize.body(query, 'query')

        request = build_countquery_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.countquery.metadata['url'],
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

    countquery.metadata = {'url': "/api/v2/runners/count/query"}  # type: ignore


    @distributed_trace
    def getqueryschema(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.iFilterProperty"]
        """getqueryschema.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of iFilterProperty, or the result of cls(response)
        :rtype: list[~runway.sdk.models.iFilterProperty]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.iFilterProperty"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_getqueryschema_request(
            template_url=self.getqueryschema.metadata['url'],
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

        deserialized = self._deserialize('[iFilterProperty]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    getqueryschema.metadata = {'url': "/api/v2/runners/query/schema"}  # type: ignore


    @distributed_trace
    def savequerytoset(
        self,
        setid,  # type: str
        query,  # type: "_models.query"
        **kwargs  # type: Any
    ):
        # type: (...) -> int
        """savequerytoset.

        :param setid:
        :type setid: str
        :param query:
        :type query: ~runway.sdk.models.query
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

        _json = self._serialize.body(query, 'query')

        request = build_savequerytoset_request(
            setid=setid,
            contenttype=contenttype,
            json=_json,
            template_url=self.savequerytoset.metadata['url'],
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

    savequerytoset.metadata = {'url': "/api/v2/runners/query/set/{setId}"}  # type: ignore

