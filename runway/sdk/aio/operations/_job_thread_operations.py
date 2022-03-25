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
from ...operations._job_thread_operations import build_count_request, build_countquery_request, build_deletebyid_request, build_deletebyjob_request, build_downloadresultforthread_request, build_getautospawnthreads_request, build_getlastlogforthread_request, build_getnodenameforthread_request, build_getqueryschema_request, build_gettags_request, build_getthreadsforjob_request, build_list_request, build_load_request, build_query_request, build_savequerytoset_request, build_stepjobthread_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class jobThreadOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~runway.sdk.aio.PyRunway`'s
        :attr:`job_thread` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def deletebyid(
        self,
        threadid: str,
        **kwargs: Any
    ) -> IO:
        """deletebyid.

        :param threadid:
        :type threadid: str
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
            threadid=threadid,
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

    deletebyid.metadata = {'url': "/api/v2/threads/{threadId}"}  # type: ignore


    @distributed_trace_async
    async def load(
        self,
        threadid: str,
        **kwargs: Any
    ) -> "_models.runwayJobThread":
        """load.

        :param threadid:
        :type threadid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: runwayJobThread, or the result of cls(response)
        :rtype: ~runway.sdk.models.runwayJobThread
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.runwayJobThread"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_load_request(
            threadid=threadid,
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

        deserialized = self._deserialize('runwayJobThread', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    load.metadata = {'url': "/api/v2/threads/{threadId}"}  # type: ignore


    @distributed_trace_async
    async def deletebyjob(
        self,
        jobid: str,
        **kwargs: Any
    ) -> IO:
        """deletebyjob.

        :param jobid:
        :type jobid: str
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

        
        request = build_deletebyjob_request(
            jobid=jobid,
            template_url=self.deletebyjob.metadata['url'],
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

    deletebyjob.metadata = {'url': "/api/v2/threads/job/{jobId}"}  # type: ignore


    @distributed_trace_async
    async def getthreadsforjob(
        self,
        jobid: str,
        **kwargs: Any
    ) -> List["_models.runwayJobThread"]:
        """getthreadsforjob.

        :param jobid:
        :type jobid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of runwayJobThread, or the result of cls(response)
        :rtype: list[~runway.sdk.models.runwayJobThread]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.runwayJobThread"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_getthreadsforjob_request(
            jobid=jobid,
            template_url=self.getthreadsforjob.metadata['url'],
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

        deserialized = self._deserialize('[runwayJobThread]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    getthreadsforjob.metadata = {'url': "/api/v2/threads/job/{jobId}"}  # type: ignore


    @distributed_trace_async
    async def getautospawnthreads(
        self,
        **kwargs: Any
    ) -> List["_models.threadView"]:
        """getautospawnthreads.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of threadView, or the result of cls(response)
        :rtype: list[~runway.sdk.models.threadView]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.threadView"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_getautospawnthreads_request(
            template_url=self.getautospawnthreads.metadata['url'],
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

        deserialized = self._deserialize('[threadView]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    getautospawnthreads.metadata = {'url': "/api/v2/threads/auto"}  # type: ignore


    @distributed_trace_async
    async def downloadresultforthread(
        self,
        threadid: str,
        **kwargs: Any
    ) -> IO:
        """downloadresultforthread.

        :param threadid:
        :type threadid: str
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

        
        request = build_downloadresultforthread_request(
            threadid=threadid,
            template_url=self.downloadresultforthread.metadata['url'],
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

    downloadresultforthread.metadata = {'url': "/api/v2/threads/{threadId}/lastresult"}  # type: ignore


    @distributed_trace_async
    async def getlastlogforthread(
        self,
        threadid: str,
        **kwargs: Any
    ) -> IO:
        """getlastlogforthread.

        :param threadid:
        :type threadid: str
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

        
        request = build_getlastlogforthread_request(
            threadid=threadid,
            template_url=self.getlastlogforthread.metadata['url'],
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

    getlastlogforthread.metadata = {'url': "/api/v2/threads/{threadId}/lastlog"}  # type: ignore


    @distributed_trace_async
    async def getnodenameforthread(
        self,
        threadid: str,
        **kwargs: Any
    ) -> str:
        """getnodenameforthread.

        :param threadid:
        :type threadid: str
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

        
        request = build_getnodenameforthread_request(
            threadid=threadid,
            template_url=self.getnodenameforthread.metadata['url'],
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

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    getnodenameforthread.metadata = {'url': "/api/v2/threads/{threadId}/nodename"}  # type: ignore


    @distributed_trace_async
    async def stepjobthread(
        self,
        request: "_models.stepThreadRequest",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> IO:
        """stepjobthread.

        :param request:
        :type request: ~runway.sdk.models.stepThreadRequest
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

        _json = self._serialize.body(request, 'stepThreadRequest')

        request = build_stepjobthread_request(
            contenttype=contenttype,
            json=_json,
            template_url=self.stepjobthread.metadata['url'],
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

    stepjobthread.metadata = {'url': "/api/v2/threads/step"}  # type: ignore


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

    gettags.metadata = {'url': "/api/v2/threads/tags"}  # type: ignore


    @distributed_trace_async
    async def list(
        self,
        **kwargs: Any
    ) -> "_models.queryResponseOfIJobThreadQueryView":
        """list.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryResponseOfIJobThreadQueryView, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryResponseOfIJobThreadQueryView
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryResponseOfIJobThreadQueryView"]
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

        deserialized = self._deserialize('queryResponseOfIJobThreadQueryView', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': "/api/v2/threads"}  # type: ignore


    @distributed_trace_async
    async def query(
        self,
        query: "_models.query",
        *,
        contenttype: Optional[str] = "application/json",
        **kwargs: Any
    ) -> "_models.queryResponseOfIJobThreadQueryView":
        """query.

        :param query:
        :type query: ~runway.sdk.models.query
        :keyword contenttype: Body Parameter content-type. Possible values are "application/json" or
         None. Default value is "application/json".
        :paramtype contenttype: str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/*+json". Default value is "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: queryResponseOfIJobThreadQueryView, or the result of cls(response)
        :rtype: ~runway.sdk.models.queryResponseOfIJobThreadQueryView
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.queryResponseOfIJobThreadQueryView"]
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

        deserialized = self._deserialize('queryResponseOfIJobThreadQueryView', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query.metadata = {'url': "/api/v2/threads/query"}  # type: ignore


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

    count.metadata = {'url': "/api/v2/threads/count"}  # type: ignore


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

    countquery.metadata = {'url': "/api/v2/threads/count/query"}  # type: ignore


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

    getqueryschema.metadata = {'url': "/api/v2/threads/query/schema"}  # type: ignore


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

    savequerytoset.metadata = {'url': "/api/v2/threads/query/set/{setId}"}  # type: ignore

