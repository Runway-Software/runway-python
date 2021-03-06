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
from ...operations._role_operations import build_count_request, build_countquery_request, build_create_request, build_deletebyid_request, build_deletebyset_request, build_getqueryschema_request, build_gettags_request, build_list_request, build_load_request, build_query_request, build_savequerytoset_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class roleOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~runway.sdk.aio.PyRunway`'s
        :attr:`role` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def deletebyset(
        self,
        setrequest: "_models.idRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> IO:
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

        _json = self._serialize.body(setrequest, 'idRequest')

        request = build_deletebyset_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.deletebyset.metadata['url'],
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

    deletebyset.metadata = {'url': "/api/v2/roles"}  # type: ignore


    @distributed_trace_async
    async def create(
        self,
        request: "_models.createRoleRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> "_models.idResponse":
        """create.

        :param request:
        :type request: ~runway.sdk.models.createRoleRequest
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
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

        _json = self._serialize.body(request, 'createRoleRequest')

        request = build_create_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.create.metadata['url'],
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

        deserialized = self._deserialize('idResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': "/api/v2/roles"}  # type: ignore


    @distributed_trace_async
    async def list(
        self,
        **kwargs: Any
    ) -> "_models.queryResponseOfIRoleView":
        """list.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryResponseOfIRoleView, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryResponseOfIRoleView
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryResponseOfIRoleView"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_request(
            template_url=self.list.metadata['url'],
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

        deserialized = self._deserialize('queryResponseOfIRoleView', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': "/api/v2/roles"}  # type: ignore


    @distributed_trace_async
    async def deletebyid(
        self,
        roleid: str,
        **kwargs: Any
    ) -> IO:
        """deletebyid.

        :param roleid:
        :type roleid: str
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
            roleid=roleid,
            template_url=self.deletebyid.metadata['url'],
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

    deletebyid.metadata = {'url': "/api/v2/roles/{roleId}"}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        roleid: str,
        request: "_models.updateRoleRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> IO:
        """update.

        :param roleid:
        :type roleid: str
        :param request:
        :type request: ~runway.sdk.models.updateRoleRequest
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

        _json = self._serialize.body(request, 'updateRoleRequest')

        request = build_update_request(
            roleid=roleid,
            contenttype=contenttype,
            json=_json,
            template_url=self.update.metadata['url'],
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

    update.metadata = {'url': "/api/v2/roles/{roleId}"}  # type: ignore


    @distributed_trace_async
    async def load(
        self,
        roleid: str,
        **kwargs: Any
    ) -> "_models.runwayRole":
        """load.

        :param roleid:
        :type roleid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: runwayRole, or the result of cls(response)
        :rtype: ~runway.sdk.models.runwayRole
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.runwayRole"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_load_request(
            roleid=roleid,
            template_url=self.load.metadata['url'],
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

        deserialized = self._deserialize('runwayRole', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    load.metadata = {'url': "/api/v2/roles/{roleId}"}  # type: ignore


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

    gettags.metadata = {'url': "/api/v2/roles/tags"}  # type: ignore


    @distributed_trace_async
    async def query(
        self,
        query: "_models.query",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> "_models.queryResponseOfIRoleView":
        """query.

        :param query:
        :type query: ~runway.sdk.models.query
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryResponseOfIRoleView, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryResponseOfIRoleView
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryResponseOfIRoleView"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _json = self._serialize.body(query, 'query')

        request = build_query_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.query.metadata['url'],
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

        deserialized = self._deserialize('queryResponseOfIRoleView', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query.metadata = {'url': "/api/v2/roles/query"}  # type: ignore


    @distributed_trace_async
    async def count(
        self,
        **kwargs: Any
    ) -> int:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
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

    count.metadata = {'url': "/api/v2/roles/count"}  # type: ignore


    @distributed_trace_async
    async def countquery(
        self,
        query: "_models.query",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> int:
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

        _json = self._serialize.body(query, 'query')

        request = build_countquery_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.countquery.metadata['url'],
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

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    countquery.metadata = {'url': "/api/v2/roles/count/query"}  # type: ignore


    @distributed_trace_async
    async def getqueryschema(
        self,
        **kwargs: Any
    ) -> List["_models.iFilterProperty"]:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
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

    getqueryschema.metadata = {'url': "/api/v2/roles/query/schema"}  # type: ignore


    @distributed_trace_async
    async def savequerytoset(
        self,
        setid: str,
        query: "_models.query",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> int:
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

        _json = self._serialize.body(query, 'query')

        request = build_savequerytoset_request(
            setid=setid,
            contenttype=contenttype,
            json=_json,
            template_url=self.savequerytoset.metadata['url'],
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

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    savequerytoset.metadata = {'url': "/api/v2/roles/query/set/{setId}"}  # type: ignore

