# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.7.6, generator: @autorest/python@5.14.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional, Union

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models
from ._configuration import PyRunwayConfiguration
from .operations import accountAssetOperations, assetOperations, authenticationOperations, clientOperations, connectionOperations, contentOperations, endpointAssetOperations, enrollmentOperations, groupOperations, invitationOperations, jobOperations, jobThreadOperations, logsOperations, remoteShellOperations, repositoryOperations, resultsOperations, roleOperations, runnerOperations, setOperations, tagOperations, userOperations

class PyRunway:    # pylint: disable=too-many-instance-attributes
    """PyRunway.

    :ivar account_asset: accountAssetOperations operations
    :vartype account_asset: runway.sdk.aio.operations.accountAssetOperations
    :ivar asset: assetOperations operations
    :vartype asset: runway.sdk.aio.operations.assetOperations
    :ivar authentication: authenticationOperations operations
    :vartype authentication: runway.sdk.aio.operations.authenticationOperations
    :ivar client: clientOperations operations
    :vartype client: runway.sdk.aio.operations.clientOperations
    :ivar connection: connectionOperations operations
    :vartype connection: runway.sdk.aio.operations.connectionOperations
    :ivar content: contentOperations operations
    :vartype content: runway.sdk.aio.operations.contentOperations
    :ivar endpoint_asset: endpointAssetOperations operations
    :vartype endpoint_asset: runway.sdk.aio.operations.endpointAssetOperations
    :ivar enrollment: enrollmentOperations operations
    :vartype enrollment: runway.sdk.aio.operations.enrollmentOperations
    :ivar group: groupOperations operations
    :vartype group: runway.sdk.aio.operations.groupOperations
    :ivar invitation: invitationOperations operations
    :vartype invitation: runway.sdk.aio.operations.invitationOperations
    :ivar job: jobOperations operations
    :vartype job: runway.sdk.aio.operations.jobOperations
    :ivar job_thread: jobThreadOperations operations
    :vartype job_thread: runway.sdk.aio.operations.jobThreadOperations
    :ivar logs: logsOperations operations
    :vartype logs: runway.sdk.aio.operations.logsOperations
    :ivar remote_shell: remoteShellOperations operations
    :vartype remote_shell: runway.sdk.aio.operations.remoteShellOperations
    :ivar repository: repositoryOperations operations
    :vartype repository: runway.sdk.aio.operations.repositoryOperations
    :ivar results: resultsOperations operations
    :vartype results: runway.sdk.aio.operations.resultsOperations
    :ivar role: roleOperations operations
    :vartype role: runway.sdk.aio.operations.roleOperations
    :ivar runner: runnerOperations operations
    :vartype runner: runway.sdk.aio.operations.runnerOperations
    :ivar set: setOperations operations
    :vartype set: runway.sdk.aio.operations.setOperations
    :ivar tag: tagOperations operations
    :vartype tag: runway.sdk.aio.operations.tagOperations
    :ivar user: userOperations operations
    :vartype user: runway.sdk.aio.operations.userOperations
    :param platform:  Default value is None.
    :type platform: str or ~runway.sdk.models.enum6
    :param base_url: Service URL. Default value is "https://portal.runway.host".
    :type base_url: str
    """

    def __init__(
        self,
        platform: Optional[Union[str, "_models.enum6"]] = None,
        base_url: str = "https://portal.runway.host",
        **kwargs: Any
    ) -> None:
        self._config = PyRunwayConfiguration(platform=platform, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.account_asset = accountAssetOperations(self._client, self._config, self._serialize, self._deserialize)
        self.asset = assetOperations(self._client, self._config, self._serialize, self._deserialize)
        self.authentication = authenticationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.client = clientOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection = connectionOperations(self._client, self._config, self._serialize, self._deserialize)
        self.content = contentOperations(self._client, self._config, self._serialize, self._deserialize)
        self.endpoint_asset = endpointAssetOperations(self._client, self._config, self._serialize, self._deserialize)
        self.enrollment = enrollmentOperations(self._client, self._config, self._serialize, self._deserialize)
        self.group = groupOperations(self._client, self._config, self._serialize, self._deserialize)
        self.invitation = invitationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job = jobOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job_thread = jobThreadOperations(self._client, self._config, self._serialize, self._deserialize)
        self.logs = logsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.remote_shell = remoteShellOperations(self._client, self._config, self._serialize, self._deserialize)
        self.repository = repositoryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.results = resultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.role = roleOperations(self._client, self._config, self._serialize, self._deserialize)
        self.runner = runnerOperations(self._client, self._config, self._serialize, self._deserialize)
        self.set = setOperations(self._client, self._config, self._serialize, self._deserialize)
        self.tag = tagOperations(self._client, self._config, self._serialize, self._deserialize)
        self.user = userOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "PyRunway":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
