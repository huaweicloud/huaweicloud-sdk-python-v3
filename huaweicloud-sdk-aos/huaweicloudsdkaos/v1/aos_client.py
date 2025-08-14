# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaos'")


class AosClient(Client):
    def __init__(self):
        super(AosClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaos.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AosClient":
                raise TypeError("client type error, support client type is AosClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_private_provider(self, request):
        r"""创建私有provider

        创建私有provider（CreatePrivateProvider）
        
        创建一个私有的空provider。如果用户给予了provider_version和function_graph_urn，则在创建私有provider的同时，还会在私有provider下创建一个私有provider版本。
          * 私有provider允许用户将自定义的provider注册到RFS中，并仅提供给当前用户使用。
          * 如果同名私有provider在当前账户中已经存在，则会返回409。
          * 版本号遵循语义化版本号（Semantic Version），为用户自定义。
          * 在本API中，provider_version和function_graph_urn需要搭配使用，如果只指定其中一个参数，则会返回400。
          * 资源编排服务只会对function_graph_urn进行浅校验，如是否符合正则，是否仅指定为当前region等。并不会深度校验，即用户是否存在权限调用，是否真实存在等。
          * 该API会返回provider_source字段，该字段按照“huawei.com/private-provider/{provider_name}”的形式拼接。关于provider_name和provider_source字段在模板中的使用细节，详见下方描述中。
          * 如果用户期望使用名称中不含有大写英文的provider，可以按照如下展示将provider_source字段指定为模板中定义的required_providers中的source参数。
          * 如果用户期望使用名称含有大写英文的provider，需要将provider_name完全转化为小写英文创建。同时用户既可以在模板中使用API返回的provider_source参数，也可以在模板中以 “huawei.com/private-provider”为固定前缀，按照原含大写英文的provider_name，拼写provider_source参数。
          * 用户在使用该私有provider时，如果期望RFS使用委托调用FG以及OBS，可在创建私有provider时提供委托信息，该委托对私有provider下所有版本生效。provider_agency_name或provider_agency_urn二者最多只能提供一个，推荐用户在使用信任委托时给予provider_agency_urn，provider_agency_name只支持接收普通委托名称，如果给予了信任委托名称，则会在使用私有provider部署资源栈时失败。
        
        以HCL格式的模板为例，模板中引用私有provider的语法如下：
        &#x60;&#x60;&#x60;
        Provider \&quot;{provider_name}\&quot; {
          source &#x3D; \&quot;{provider_source}\&quot;
          version &#x3D; \&quot;{provider_version}\&quot;
        }
        &#x60;&#x60;&#x60;
        
        以JSON格式的模板为例，模板中引用私有provider的语法如下：
        &#x60;&#x60;&#x60;
        {
          \&quot;terraform\&quot;:{
            \&quot;required_providers\&quot;:[
              {
                \&quot;{provider_name}\&quot;:{
                  \&quot;source\&quot;:\&quot;{provider_source}\&quot;,
                  \&quot;version\&quot;:\&quot;{provider_version}\&quot;
                }
              }
            ]
          }
        }
        &#x60;&#x60;&#x60;
        
        RFS在支持用户使用FunctionGraph(以下简称：FG)的事件函数运行私有Provider时，定义了一套详细的对接规则，以实现RFS与私有Provider之间的成功交互。
        其中关于FG的事件函数使用，请参考官网文档： https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_02_1002.html。
        用户需要在提供的FG的事件函数方法中，按照如下规则实现一系列对应方法：
          1. 用户需要首先在FG中启动一个HTTP Server，用于接受来自RFS的HTTP请求，请求的Path固定为\&quot;/provider\&quot;，请求方法为\&quot;POST\&quot;。RFS规定了发送给FG的HTTP请求体，请求体格式如下所示：
                &#x60;&#x60;&#x60;
                {
                  \&quot;method_name\&quot;: String,
                  \&quot;request_data\&quot;: String,
                  \&quot;context\&quot;:{
                    \&quot;session_id\&quot;: String,
                    \&quot;config_data\&quot;: String
                  }
                }
                &#x60;&#x60;&#x60;
             用户提供的FG的事件函数需要能够接收如上请求。否则会调用私有Provider失败，导致资源编排失败。
          2. 下面对FG中如何使用请求体中的各个参数，以实现FG与RFS的成功交互做详细解释：
             \&quot;method_name\&quot;：RFS期望FG的事件函数中调用的私有provider的gRPC方法名。RFS会在请求体中，根据实际业务场景，每次从如下方法中选择一个进行传递。其中每个方法名需要与provider中原生的gRPC方法一一对应。在收到携带有某个方法名的请求后，FG的事件函数内能够调用对应的私有provider的原生gRPC方法，实现具体资源的处理逻辑。
             provider内提供的原生gRPC协议请参考：tfplugin5.proto和grpc_controller.proto。方法名列表如下：
                &#x60;&#x60;&#x60;
                tfplugin5.proto：
                  \&quot;/tfplugin5.Provider/GetSchema\&quot;
                  \&quot;/tfplugin5.Provider/PrepareProviderConfig\&quot;
                  \&quot;/tfplugin5.Provider/ValidateResourceTypeConfig\&quot;
                  \&quot;/tfplugin5.Provider/ValidateDataSourceConfig\&quot;
                  \&quot;/tfplugin5.Provider/UpgradeResourceState\&quot;
                  \&quot;/tfplugin5.Provider/Configure\&quot;
                  \&quot;/tfplugin5.Provider/ReadResource\&quot;
                  \&quot;/tfplugin5.Provider/PlanResourceChange\&quot;
                  \&quot;/tfplugin5.Provider/ApplyResourceChange\&quot;
                  \&quot;/tfplugin5.Provider/ImportResourceState\&quot;
                  \&quot;/tfplugin5.Provider/ReadDataSource\&quot;
                  \&quot;/tfplugin5.Provider/Stop\&quot;
                grpc_controller.proto：
                  \&quot;/plugin.GRPCController/Shutdown\&quot;
                &#x60;&#x60;&#x60;
             \&quot;request_data\&quot;：RFS传递给FG的事件函数中每个方法的请求内容。在每个方法的处理逻辑中，需要先将request_data中的数据使用base64解码，然后作为私有provider的gRPC方法的数据传入。
             \&quot;config_data\&quot;：用于自定义provider处理实际请求前的初始化，如果context中config_data非空，FG的事件函数需要先将config_data作为输入调用/tfplugin5.Provider/Configure方法，进行初始化，再根据method_name调用对应的方法获取响应。
             \&quot;session_id\&quot;：表示请求是否来自同一个模板中的同一批编排任务。session_id相同，表示请求来自同一个模板中的同一批编排任务。
             注意：用户启动的同一个provider进程不能接受多个来自RFS的请求。RFS推荐用户处理请求时，每次都启动新的进程处理相关请求。
          3. 在FG的事件函数中实现的请求响应按照固定格式进行返回，响应体的格式如下，成功响应码固定为200，任何其他响应码均视为失败请求，会导致资源编排失败。
                &#x60;&#x60;&#x60;
                {
                  \&quot;response_data\&quot;: String,
                  \&quot;error\&quot;: String
                }
                &#x60;&#x60;&#x60;
             \&quot;response_data\&quot;：调用私有provider的gRPC方法返回的内容。在FG的事件函数中，需要将gRPC方法返回的响应序列化后使用base64编码返回。
             \&quot;error\&quot;：调用gRPC方法返回的错误信息。
          4. 用户需要对FG事件函数进行异步配置，针对于不涉及资源操作的读相关的gRPC请求，RFS默认通过同步接口调用FG；针对于涉及资源操作的写相关的gRPC请求，RFS默认通过异步接口调用FG。
             以下gRPC请求默认同步调用：
                &#x60;&#x60;&#x60;
                tfplugin5.proto：
                  \&quot;/tfplugin5.Provider/GetSchema\&quot;
                  \&quot;/tfplugin5.Provider/PrepareProviderConfig\&quot;
                  \&quot;/tfplugin5.Provider/ValidateResourceTypeConfig\&quot;
                  \&quot;/tfplugin5.Provider/ValidateDataSourceConfig\&quot;
                  \&quot;/tfplugin5.Provider/UpgradeResourceState\&quot;
                  \&quot;/tfplugin5.Provider/Configure\&quot;
                  \&quot;/tfplugin5.Provider/ReadResource\&quot;
                  \&quot;/tfplugin5.Provider/ImportResourceState\&quot;
                  \&quot;/tfplugin5.Provider/ReadDataSource\&quot;
                &#x60;&#x60;&#x60;
             以下gRPC请求默认异步调用：
                &#x60;&#x60;&#x60;
                tfplugin5.proto：
                  \&quot;/tfplugin5.Provider/PlanResourceChange\&quot;
                  \&quot;/tfplugin5.Provider/ApplyResourceChange\&quot;
                  \&quot;/tfplugin5.Provider/Stop\&quot;
                grpc_controller.proto：
                  \&quot;/plugin.GRPCController/Shutdown\&quot;
                &#x60;&#x60;&#x60;
             目前FG异步配置的成功和失败时通知的目标服务只支持OBS，用户如果开启异步调用状态持久化，RFS会通过轮询FG获取函数异步调用请求列表来获取异步调用的状态，否则会轮询OBS是否存在异步调用结果来判断异步调用状态。
             对于同步调用，RFS阻塞等待FG返回调用结果；对于异步调用，RFS在判断异步调用结束后，获取OBS桶中的异步调用结果。
        
        **约束与限制：**
          1. 私有provider为用户自行定义，提供给RFS的provider插件，RFS不负责校验其内部逻辑是否正确。
          2. RFS不负责维护私有provider的生命周期。用户使用私有provider部署的资源栈，由于私有provider缺失或问题，导致资源栈无法继续部署管理的，RFS不负责提供解决方案。
          3. RFS不负责保障私有provider的信息安全。用户使用私有provider部署的资源栈，由于模板中存在敏感数据，进而导致敏感信息泄露给第三方相关资源的，RFS不承担其相关责任。
          4. 当前调用私有provider过程中增加了网络因素，因此使用私有provider部署的失败概率会增加。如果出现因网络原因导致的部署失败，可以增加重试操作。
          5. 当前RFS默认会同步调用在FG中定义的读相关gRPC请求，单次方法需要确保运行时间不超过30s，否则会极大增加失败概率。
          6. 当前仅支持在模板中固定私有provider版本，不支持&gt;,&gt;&#x3D;,&lt;,&lt;&#x3D;,~&gt;等定义宽松版本的表达式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateProvider
        :type request: :class:`huaweicloudsdkaos.v1.CreatePrivateProviderRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreatePrivateProviderResponse`
        """
        http_info = self._create_private_provider_http_info(request)
        return self._call_api(**http_info)

    def create_private_provider_invoker(self, request):
        http_info = self._create_private_provider_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_private_provider_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-providers",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_private_provider_version(self, request):
        r"""创建私有provider版本

        创建私有provider版本（CreatePrivateProviderVersion）
        
          * provider的版本号需遵循语义化版本号（Semantic Version），为用户自定义。
          * 如果provider_name和provider_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
          * 资源编排服务只会对function_graph_urn进行浅校验，如是否符合正则，是否仅指定为当前region等。并不会深度校验，即用户是否存在权限调用，是否真实存在等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateProviderVersion
        :type request: :class:`huaweicloudsdkaos.v1.CreatePrivateProviderVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreatePrivateProviderVersionResponse`
        """
        http_info = self._create_private_provider_version_http_info(request)
        return self._call_api(**http_info)

    def create_private_provider_version_invoker(self, request):
        http_info = self._create_private_provider_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_private_provider_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-providers/{provider_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateProviderVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider_name' in local_var_params:
            path_params['provider_name'] = local_var_params['provider_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_private_provider(self, request):
        r"""删除私有provider

        删除私有provider（DeletePrivateProvider）
        
        删除某个私有provider及私有provider下的所有provider版本。
        
          * 如果provider_name和provider_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        ** 请谨慎操作，删除私有provider将会删除该私有provider下的所有provider版本。 **
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateProvider
        :type request: :class:`huaweicloudsdkaos.v1.DeletePrivateProviderRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeletePrivateProviderResponse`
        """
        http_info = self._delete_private_provider_http_info(request)
        return self._call_api(**http_info)

    def delete_private_provider_invoker(self, request):
        http_info = self._delete_private_provider_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_private_provider_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-providers/{provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider_name' in local_var_params:
            path_params['provider_name'] = local_var_params['provider_name']

        query_params = []
        if 'provider_id' in local_var_params:
            query_params.append(('provider_id', local_var_params['provider_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_private_provider_version(self, request):
        r"""删除私有provider版本

        删除私有provider版本（DeletePrivateProviderVersion）
        
        删除某个私有provider版本
        
          * 如果provider_name和provider_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        **请谨慎操作**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateProviderVersion
        :type request: :class:`huaweicloudsdkaos.v1.DeletePrivateProviderVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeletePrivateProviderVersionResponse`
        """
        http_info = self._delete_private_provider_version_http_info(request)
        return self._call_api(**http_info)

    def delete_private_provider_version_invoker(self, request):
        http_info = self._delete_private_provider_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_private_provider_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-providers/{provider_name}/versions/{provider_version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateProviderVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider_name' in local_var_params:
            path_params['provider_name'] = local_var_params['provider_name']
        if 'provider_version' in local_var_params:
            path_params['provider_version'] = local_var_params['provider_version']

        query_params = []
        if 'provider_id' in local_var_params:
            query_params.append(('provider_id', local_var_params['provider_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_private_provider_versions(self, request):
        r"""列举私有provider版本

        列举私有provider版本（ListPrivateProviderVersions）
        
        列举所选择的私有provider中所有的provider版本信息。
        
          * 可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir数量须一致，否则返回400。如果未给予sort_key和sort_dir，则默认按照创建时间降序排序。
          * 如果provider_name和provider_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
          * 如果provider下不存在provider版本，则返回空list。
          * 如果provider不存在则返回404。
          * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateProviderVersions
        :type request: :class:`huaweicloudsdkaos.v1.ListPrivateProviderVersionsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListPrivateProviderVersionsResponse`
        """
        http_info = self._list_private_provider_versions_http_info(request)
        return self._call_api(**http_info)

    def list_private_provider_versions_invoker(self, request):
        http_info = self._list_private_provider_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_private_provider_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-providers/{provider_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateProviderVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider_name' in local_var_params:
            path_params['provider_name'] = local_var_params['provider_name']

        query_params = []
        if 'provider_id' in local_var_params:
            query_params.append(('provider_id', local_var_params['provider_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_private_providers(self, request):
        r"""列举私有provider

        列举私有provider（ListPrivateProviders）
        
        列举当前局点下用户所有的私有provider。
        
          * 可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir数量须一致，否则返回400。如果未给予sort_key和sort_dir，则默认按照创建时间降序排序。
          * 如果当前用户下没有任何私有provider，则返回空list。
          * 如果需要某个provider的所有版本信息，可以调用ListPrivateProviderVersions。
          * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateProviders
        :type request: :class:`huaweicloudsdkaos.v1.ListPrivateProvidersRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListPrivateProvidersResponse`
        """
        http_info = self._list_private_providers_http_info(request)
        return self._call_api(**http_info)

    def list_private_providers_invoker(self, request):
        http_info = self._list_private_providers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_private_providers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateProvidersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_provider_metadata(self, request):
        r"""获取私有provider元数据

        获取私有provider元数据（ShowPrivateProviderMetadata）
        
        获取某个私有provider的元数据信息
        
          * 具体返回的信息见ShowPrivateProviderMetadataResponseBody，如果想查看私有provider下全部provider版本，请调用ListPrivateProviderVersions。
          * 如果provider_name和provider_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateProviderMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateProviderMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateProviderMetadataResponse`
        """
        http_info = self._show_private_provider_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_private_provider_metadata_invoker(self, request):
        http_info = self._show_private_provider_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_provider_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-providers/{provider_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateProviderMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider_name' in local_var_params:
            path_params['provider_name'] = local_var_params['provider_name']

        query_params = []
        if 'provider_id' in local_var_params:
            query_params.append(('provider_id', local_var_params['provider_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_provider_version_metadata(self, request):
        r"""获取私有provider版本元数据

        获取私有provider版本元数据（ShowPrivateProviderVersionMetadata）
        
        获取某个私有provider版本的元数据信息
          
          * 具体返回信息见ShowPrivateProviderVersionMetadataResponseBody
          * 如果provider_name和provider_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateProviderVersionMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateProviderVersionMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateProviderVersionMetadataResponse`
        """
        http_info = self._show_private_provider_version_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_private_provider_version_metadata_invoker(self, request):
        http_info = self._show_private_provider_version_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_provider_version_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-providers/{provider_name}/versions/{provider_version}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateProviderVersionMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider_name' in local_var_params:
            path_params['provider_name'] = local_var_params['provider_name']
        if 'provider_version' in local_var_params:
            path_params['provider_version'] = local_var_params['provider_version']

        query_params = []
        if 'provider_id' in local_var_params:
            query_params.append(('provider_id', local_var_params['provider_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_private_provider_metadata(self, request):
        r"""更新私有provider元数据

        更新私有provider元数据（UpdatePrivateProviderMetadata）
        
        更新当前私有provider的元数据信息
        
          * 目前只支持更新私有provider的描述
          * 如果需要创建新的版本，请调用CreatePrivateProviderVersion
          * 更新为增量更新，即如果某个参数不提供，则保持原始值
          * 如果请求中没有需要被更新的参数，则返回400。注意：即使更新原始值和目标值一致也被认为是有效更新
          * 更新后私有provider的更新时间（update_time）也会被更新
          * 如果provider_name和provider_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateProviderMetadata
        :type request: :class:`huaweicloudsdkaos.v1.UpdatePrivateProviderMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdatePrivateProviderMetadataResponse`
        """
        http_info = self._update_private_provider_metadata_http_info(request)
        return self._call_api(**http_info)

    def update_private_provider_metadata_invoker(self, request):
        http_info = self._update_private_provider_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_private_provider_metadata_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/private-providers/{provider_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateProviderMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider_name' in local_var_params:
            path_params['provider_name'] = local_var_params['provider_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def apply_execution_plan(self, request):
        r"""执行执行计划

        执行执行计划（ApplyExecutionPlan）
        
        此API用于执行一个执行计划
        
        * 当执行请求接受后，执行计划状态将变为&#x60;APPLY_IN_PROGRESS&#x60;，后台会进行异步处理。
        * 当执行结束后，执行计划状态将变为&#x60;APPLIED&#x60;。
        * 用户可以调用GetStackMetadata查询资源栈的状态（status）来跟踪资源栈部署情况以及确认本次执行结果是否成功。
        * 执行执行计划时，用户将模板中定义的资源删除（包括Import定义的资源），会触发实际资源的删除。
        
        如果不希望通过执行计划进行部署操作，也可以选择调用DeployStack进行直接部署
        
        关于执行计划的过期失效：
          1. 如果指定资源栈下有多个执行计划，则在执行某个执行计划后（无论结果是否成功），剩余所有的执行计划将过期失效；
          2. 如果调用ApplyExecutionPlan时，指定的执行计划已经过期失效，则返回403
        
        如果资源栈状态处于非终态（即以&#x60;IN_PROGRESS&#x60;结尾，详细见下方）状态时，则不允许执行执行计划，并返回403。非终态状态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanResponse`
        """
        http_info = self._apply_execution_plan_http_info(request)
        return self._call_api(**http_info)

    def apply_execution_plan_invoker(self, request):
        http_info = self._apply_execution_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_execution_plan_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyExecutionPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_execution_plan(self, request):
        r"""创建执行计划

        创建执行计划（CreateExecutionPlan）
        
        此API用于在指定的资源栈下生成一个执行计划，执行计划描述了当前资源栈中记录的资源状态和模板描述的目的资源状态之间的区别（如，资源A将以以下配置文件生成，资源B将以下参数从XXX修改成YYY）
        
        调用此API触发创建执行计划之后，可以通过GetExecutionPlanMetadata来跟踪执行计划的状态
        当执行计划状态为&#x60;AVAILABLE&#x60;时，可以通过GetExecutionPlan获取本次执行计划的结果
        
        执行计划不会做过多深层的检查和校验，如用户是否有权限生成、修改资源等
        
        **注意：**
          * 创建执行计划时，指定的资源栈必须存在。如果指定的资源栈不存在，则返回404，用户可通过调用创建资源栈（CreateStack）API来创建资源栈。
          * 如果请求中不含有template_body和template_uri，则返回400
          * 如果资源栈进行了某次部署操作，则在该次部署操作前生成的执行计划将全部失效
          * 执行计划只代表生成时刻的结果，如果执行计划生成后，用户手动修改资源状态，则执行计划不会自动更新
          * 如果资源栈状态处于&#x60;DEPLOYMENT_IN_PROGRESS&#x60;、&#x60;ROLLBACK_IN_PROGRESS&#x60;、&#x60;DELETION_IN_PROGRESS&#x60;等状态时，则不允许创建执行计划，并返回403
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.CreateExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateExecutionPlanResponse`
        """
        http_info = self._create_execution_plan_http_info(request)
        return self._call_api(**http_info)

    def create_execution_plan_invoker(self, request):
        http_info = self._create_execution_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_execution_plan_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/execution-plans",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExecutionPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_execution_plan(self, request):
        r"""删除执行计划

        删除执行计划（DeleteExecutionPlan）
        
        删除指定的执行计划
        
        如果执行计划状态处于&#x60;CREATION_IN_PROGRESS&#x60;、&#x60;APPLY_IN_PROGRESS&#x60;状态时，则不允许删除并返回403
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.DeleteExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteExecutionPlanResponse`
        """
        http_info = self._delete_execution_plan_http_info(request)
        return self._call_api(**http_info)

    def delete_execution_plan_invoker(self, request):
        http_info = self._delete_execution_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_execution_plan_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteExecutionPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def estimate_execution_plan_price(self, request):
        r"""预估执行计划价格

        预估执行计划价格（EstimateExecutionPlanPrice）
        
        此API可以基于一份已有的执行计划中增量的资源进行询价，当前支持询价的计费模式有包周期计费、按需计费、免费，暂不支持其他形式的计费模式，例如竞价计费模式等。
        
        注：
          * 由于某些资源的属性值含有默认值，且该属性和询价参数相关。如果用户的模板中描述的资源没有声明这些属性，则询价结果可能存在偏差。
          * 询价结果仅为预估结果，具体请以实际为准。
          * 如果用户在模板中使用了depends_on参数，如A资源询价必要字段依赖于B资源的创建，则A资源不支持询价。
          * 暂不支持传入data sources的flavor.id的场景的询价。
          * 暂不支持镜像询价。
          * 如果A资源的询价必要字段设置了sensitive &#x3D; true，则A资源不支持询价。
          * 模板中询价的资源的个数是有限制的。当前一个模板中最多支持12个包周期计费资源和24个按需计费资源。
          * 支持询价的资源列表和询价必要参数
              * huaweicloud_cce_cluster: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_css_cluster:
                  * 支持的计费模式：按需
              * huaweicloud_evs_volume: 
                  * 支持的计费模式：包周期、按需
                  * 询价必要参数：size（磁盘规格）
              * huaweicloud_compute_instance: 
                  * 支持的计费模式：包周期、按需
                  * 询价必要参数：flavor_id（规格ID）、flavor_name（规格名称，flavor_id和flavor_name至少给出一个）、system_disk_size（系统磁盘大小）
              * huaweicloud_vpc_bandwidth:
                  * 支持的计费模式：按需
                  * 询价必要参数：charge_mode仅支持bandwidth
              * huaweicloud_vpc_eip: 
                  * 支持的计费模式：包周期、按需
                  * 询价必要参数：bandwidth.size（带宽大小）
              * huaweicloud_gaussdb_redis_instance: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_nat_gateway: 
                  * 支持的计费模式：按需
              * huaweicloud_rds_instance: 
                  * 支持的计费模式：包周期、按需
                  * 支持的数据库类型：MySQL、PostgreSQL、Microsoft SQL Server      
              * huaweicloud_sfs_turbo: 
                  * 支持的计费模式：按需
                  * 询价必要参数：share_type（文件系统类型）
              * huaweicloud_dms_kafka_instance: 
                  * 支持的计费模式：按需
                  * 询价必要参数：flavor_id（规格ID）、product_id（产品ID。flavor_id和product_id至少给出一个。）、storage_space（存储容量）
              * huaweicloud_dcs_instance: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_gaussdb_mysql_instance: 
                  * 支持的计费模式：包周期、按需
                  * 询价必要参数：proxy_node_number（代理节点数量）、volume_size（挂载卷的存储空间）
              * huaweicloud_vpc: 
                  * 支持的计费模式：免费
              * huaweicloud_drs_job: 
                  * 支持的计费模式：按需
              * huaweicloud_apig_instance: 
                  * 支持的计费模式：按需
              * huaweicloud_dms_rabbitmq_instance: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_hss_quota: 
                  * 支持的计费模式：包周期
              * huaweicloud_hss_host_protection: 
                  * 支持的计费模式：按需
              * huaweicloud_cbr_vault: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_cbh_instance: 
                  * 支持的计费模式：包周期
              * huaweicloud_cbh_ha_instance: 
                  * 支持的计费模式：包周期
              * huaweicloud_waf_cloud_instance: 
                  * 支持的计费模式：包周期
              * huaweicloud_lb_loadbalancer: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_elb_loadbalancer: 
                  * 支持的计费模式：按需
              * huaweicloud_modelarts_resource_pool: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_cnad_advanced_black_white_list: 
                  * 支持的计费模式：免费
              * huaweicloud_cnad_advanced_policy: 
                  * 支持的计费模式：免费
              * huaweicloud_cnad_advanced_protected_object: 
                  * 支持的计费模式：免费
              * huaweicloud_antiddos_basic: 
                  * 支持的计费模式：免费
              * huaweicloud_obs_bucket: 
                  * 支持的计费模式：免费
              * huaweicloud_obs_bucket_replication: 
                  * 支持的计费模式：免费
              * huaweicloud_workspace_desktop: 
                  * 支持的计费模式：按需
              * huaweicloud_dws_cluster: 
                  * 支持的计费模式：按需
              * huaweicloud_dws_ext_data_source: 
                  * 支持的计费模式：免费
              * huaweicloud_dws_snapshot: 
                  * 支持的计费模式：免费
              * huaweicloud_dds_instance: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_rds_read_replica_instance: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_cce_node: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_dms_rocketmq_instance: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_gaussdb_opengauss_instance: 
                  * 支持的计费模式：包周期、按需
              * huaweicloud_vpcep_endpoint: 
                  * 支持的计费模式：按需
              * huaweicloud_kms_key: 
                  * 支持的计费模式：按需
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateExecutionPlanPrice
        :type request: :class:`huaweicloudsdkaos.v1.EstimateExecutionPlanPriceRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.EstimateExecutionPlanPriceResponse`
        """
        http_info = self._estimate_execution_plan_price_http_info(request)
        return self._call_api(**http_info)

    def estimate_execution_plan_price_invoker(self, request):
        http_info = self._estimate_execution_plan_price_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _estimate_execution_plan_price_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}/prices",
            "request_type": request.__class__.__name__,
            "response_type": "EstimateExecutionPlanPriceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_execution_plan(self, request):
        r"""获取执行计划

        获取执行计划（GetExecutionPlan）
        
        此API用于获取指定执行计划的详细内容（即执行计划项目），用户可通过此API得知指定执行计划在执行后，资源栈中的资源会发生何种变化
        
        如果执行计划状态为&#x60;CREATION_IN_PROGRESS&#x60;或&#x60;CREATION_FAILED&#x60;，则不返回执行计划项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.GetExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetExecutionPlanResponse`
        """
        http_info = self._get_execution_plan_http_info(request)
        return self._call_api(**http_info)

    def get_execution_plan_invoker(self, request):
        http_info = self._get_execution_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_execution_plan_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}",
            "request_type": request.__class__.__name__,
            "response_type": "GetExecutionPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_execution_plan_metadata(self, request):
        r"""获取执行计划元数据

        获取执行计划元数据（GetExecutionPlanMetadata）
        
        该API可以获取指定执行计划的元数据，包括资源栈ID、资源栈名称、执行计划ID、执行计划名称、执行计划描述、执行计划的创建时间和执行时间、执行计划状态等信息。
        
        具体信息见GetExecutionPlanMetadataResponseBody。
        
        如果需要获取执行计划的具体内容，请调用GetExecutionPlan。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetExecutionPlanMetadata
        :type request: :class:`huaweicloudsdkaos.v1.GetExecutionPlanMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetExecutionPlanMetadataResponse`
        """
        http_info = self._get_execution_plan_metadata_http_info(request)
        return self._call_api(**http_info)

    def get_execution_plan_metadata_invoker(self, request):
        http_info = self._get_execution_plan_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_execution_plan_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "GetExecutionPlanMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_execution_plans(self, request):
        r"""列举执行计划

        列举执行计划（ListExecutionPlans）
        
        列举当前局点下用户指定资源栈下所有的执行计划
        
          * 默认按照生成时间降序排序，最新生成的在最前
          * 如果指定的资源栈下没有任何执行计划，则返回空list
          * 如果指定的资源栈不存在，则返回404
          * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        ListExecutionPlans返回的只有摘要信息（具体摘要信息见ListExecutionPlansResponseBody），如果用户需要详细的执行计划元数据请调用GetExecutionPlanMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExecutionPlans
        :type request: :class:`huaweicloudsdkaos.v1.ListExecutionPlansRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListExecutionPlansResponse`
        """
        http_info = self._list_execution_plans_http_info(request)
        return self._call_api(**http_info)

    def list_execution_plans_invoker(self, request):
        http_info = self._list_execution_plans_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_execution_plans_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/execution-plans",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionPlansResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_private_hook(self, request):
        r"""创建私有hook

        创建私有hook（CreatePrivateHook）
        
        创建一个带有初始默认版本的私有hook，创建私有hook的时候需要同时创建一个初始化的默认版本，不允许空私有hook的创建。
        设置配置(Configuration)后的私有hook才会在触发资源栈部署时生效，资源栈使用私有hook的默认版本。若创建私有hook时未指定配置项，则该私有hook在资源栈部署时不生效，后续可通过UpdatePrivateHook API更新配置。
        
          * 支持hook策略模板检验的资源栈服务API：
              CreateExecutionPlan
              ApplyExecutionPlan
              CreateStack
              DeployStack
              ContinueDeployStack
              DeleteStack
              DeleteStackEnhanced
          * 创建私有hook时指定的版本为初始默认版本。
          * 如果同名的私有hook在当前domain_id+region下已经存在，则会返回409。
          * 私有hook版本号遵循语义化版本号（Semantic Version），为用户自定义。
          * 资源编排服务会对私有hook进行校验，如文件大小，策略文件语法校验等。若存在错误，则会创建失败。
          * 当前仅支持部署资源前的检测，不支持部署资源过程中的检测。如果通过了部署资源前的检测，资源栈则会继续部署资源。反之会停止部署资源，并记录资源栈事件（stack events）。
          * 仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板(用户可以通过policy_uri或policy_body给予策略文件内容)。
          * 策略模板中的决策结果使用object类型的hook_result，hook_result所在包的包名必须使用policy。hook_result格式如下：
              &#x60;&#x60;&#x60;
              hook_result :&#x3D; {
                \&quot;is_passed\&quot;: Bool,
                \&quot;err_msg\&quot;: String,
              }
              &#x60;&#x60;&#x60;
            其中is_passed必选，err_msg可选。RFS通过查询policy.hook_result[is_passed]判断是否通过策略校验。
            * 如果policy.hook_result[is_passed]的结果是true，则表示通过策略校验，资源编排服务会继续部署资源。
            * 如果policy.hook_result[is_passed]的结果是false，则表示没有通过策略校验，资源编排服务会停止部署资源。并记录资源栈事件信息，信息的内容为policy.hook_result[err_msg]。如果没有设置err_msg，则资源栈事件信息内容为默认错误信息（校验私有hook失败）。
            * 如果没有使用policy.hook_result，则该策略不会生效，资源编排服务会继续部署资源。
          * 策略模板中不支持调用其他服务API等方式获取数据、不支持任何形式的网络访问、不支持以任何形式的自定义函数或者方法等、不支持读取本地文件以及系统操作。
        
        私有hook的策略模板语法如下：
        &#x60;&#x60;&#x60;
        package policy
        
        import rego.v1
        
        hook_result :&#x3D; {
          \&quot;is_passed\&quot;: input.message &#x3D;&#x3D; \&quot;world\&quot;,
          \&quot;err_msg\&quot;: \&quot;The error msg when private hook is not passed the validation\&quot;,
        }
        &#x60;&#x60;&#x60;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateHook
        :type request: :class:`huaweicloudsdkaos.v1.CreatePrivateHookRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreatePrivateHookResponse`
        """
        http_info = self._create_private_hook_http_info(request)
        return self._call_api(**http_info)

    def create_private_hook_invoker(self, request):
        http_info = self._create_private_hook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_private_hook_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-hooks",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_private_hook_version(self, request):
        r"""创建私有hook版本

        创建私有hook版本（CreatePrivateHookVersion）
        
        创建私有hook版本，创建私有hook版本后需要调用UpdatePrivateHook API设置为默认版本才能生效。
        
          * 版本号遵循语义化版本号（Semantic Version），为用户自定义。
          * 若hook_name和hook_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
          * 资源编排服务会对私有hook进行校验，如文件大小，策略文件语法校验等。若存在错误，则会创建失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateHookVersion
        :type request: :class:`huaweicloudsdkaos.v1.CreatePrivateHookVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreatePrivateHookVersionResponse`
        """
        http_info = self._create_private_hook_version_http_info(request)
        return self._call_api(**http_info)

    def create_private_hook_version_invoker(self, request):
        http_info = self._create_private_hook_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_private_hook_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-hooks/{hook_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateHookVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hook_name' in local_var_params:
            path_params['hook_name'] = local_var_params['hook_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_private_hook(self, request):
        r"""删除私有hook

        删除私有hook（DeletePrivateHook）
        
        删除某个私有hook以及私有hook下的全部hook版本
        
          * 默认版本只能调用本API删除，除默认版本外的其它版本可以调用DeletePrivateHookVersion API删除。
          * 若hook_name和hook_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        **请谨慎操作，删除私有hook将会删除该私有hook和该私有hook下的所有私有hook版本。**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateHook
        :type request: :class:`huaweicloudsdkaos.v1.DeletePrivateHookRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeletePrivateHookResponse`
        """
        http_info = self._delete_private_hook_http_info(request)
        return self._call_api(**http_info)

    def delete_private_hook_invoker(self, request):
        http_info = self._delete_private_hook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_private_hook_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-hooks/{hook_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hook_name' in local_var_params:
            path_params['hook_name'] = local_var_params['hook_name']

        query_params = []
        if 'hook_id' in local_var_params:
            query_params.append(('hook_id', local_var_params['hook_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_private_hook_version(self, request):
        r"""删除私有hook版本

        删除私有hook版本（DeletePrivateHookVersion）
        
        删除某个私有hook版本
        
          * 默认版本只能调用DeletePrivateHook API删除，除默认版本外的其它版本都可以调用本API删除。
          * 若hook_name和hook_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        **请谨慎操作**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateHookVersion
        :type request: :class:`huaweicloudsdkaos.v1.DeletePrivateHookVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeletePrivateHookVersionResponse`
        """
        http_info = self._delete_private_hook_version_http_info(request)
        return self._call_api(**http_info)

    def delete_private_hook_version_invoker(self, request):
        http_info = self._delete_private_hook_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_private_hook_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-hooks/{hook_name}/versions/{hook_version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateHookVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hook_name' in local_var_params:
            path_params['hook_name'] = local_var_params['hook_name']
        if 'hook_version' in local_var_params:
            path_params['hook_version'] = local_var_params['hook_version']

        query_params = []
        if 'hook_id' in local_var_params:
            query_params.append(('hook_id', local_var_params['hook_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_private_hooks(self, request):
        r"""列举私有hook

        列举私有hook（ListPrivateHooks）
        
        列举当前局点下用户所有的私有hook。
        
          * 可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir的数量须一致，否则返回400。若未给予sort_key和sort_dir，则默认按照创建时间降序排序。
          * 若当前用户没有任何私有hook，则返回空list。
          * 具体返回的信息见ListPrivateHooksResponseBody。
          * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateHooks
        :type request: :class:`huaweicloudsdkaos.v1.ListPrivateHooksRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListPrivateHooksResponse`
        """
        http_info = self._list_private_hooks_http_info(request)
        return self._call_api(**http_info)

    def list_private_hooks_invoker(self, request):
        http_info = self._list_private_hooks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_private_hooks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-hooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateHooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_hook_metadata(self, request):
        r"""获取私有hook元数据

        获取私有hook元数据（ShowPrivateHookMetadata）
        
        获取某个私有hook的元数据信息
        
          * 具体返回的信息见ShowPrivateHookMetadataResponseBody，若想查看私有hook下全部版本，请调用ListPrivateHookVersions。
          * 若hook_name和hook_id同时存在，则资源编排服务会检查两个是否匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateHookMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateHookMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateHookMetadataResponse`
        """
        http_info = self._show_private_hook_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_private_hook_metadata_invoker(self, request):
        http_info = self._show_private_hook_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_hook_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-hooks/{hook_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateHookMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hook_name' in local_var_params:
            path_params['hook_name'] = local_var_params['hook_name']

        query_params = []
        if 'hook_id' in local_var_params:
            query_params.append(('hook_id', local_var_params['hook_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_hook_version_metadata(self, request):
        r"""获取私有hook版本的元数据

        获取私有hook版本的元数据（ShowPrivateHookVersionMetadata）
        
        获取当前私有hook对应版本的元数据信息
        
          * 具体返回的信息见ShowPrivateHookVersionMetadataResponseBody。
          * 如果hook_name和hook_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateHookVersionMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateHookVersionMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateHookVersionMetadataResponse`
        """
        http_info = self._show_private_hook_version_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_private_hook_version_metadata_invoker(self, request):
        http_info = self._show_private_hook_version_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_hook_version_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-hooks/{hook_name}/versions/{hook_version}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateHookVersionMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hook_name' in local_var_params:
            path_params['hook_name'] = local_var_params['hook_name']
        if 'hook_version' in local_var_params:
            path_params['hook_version'] = local_var_params['hook_version']

        query_params = []
        if 'hook_id' in local_var_params:
            query_params.append(('hook_id', local_var_params['hook_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_hook_version_policy(self, request):
        r"""获取私有hook版本策略

        获取私有hook版本策略（ShowPrivateHookVersionPolicy）
        
        获取指定私有hook对应版本的策略。
        
          * 如果获取成功，则以临时重定向形式返回私有hook版本策略下载链接（OBS Pre Signed地址，有效期为5分钟），大多数的客户端会进行自动重定向并下载私有hook版本策略。
          * 如果未进行自动重定向，请参考HTTP的重定向规则获取私有hook版本策略下载链接，手动下载私有hook版本策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateHookVersionPolicy
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateHookVersionPolicyRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateHookVersionPolicyResponse`
        """
        http_info = self._show_private_hook_version_policy_http_info(request)
        return self._call_api(**http_info)

    def show_private_hook_version_policy_invoker(self, request):
        http_info = self._show_private_hook_version_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_hook_version_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-hooks/{hook_name}/versions/{hook_version}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateHookVersionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hook_name' in local_var_params:
            path_params['hook_name'] = local_var_params['hook_name']
        if 'hook_version' in local_var_params:
            path_params['hook_version'] = local_var_params['hook_version']

        query_params = []
        if 'hook_id' in local_var_params:
            query_params.append(('hook_id', local_var_params['hook_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Location", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_private_hook_metadata(self, request):
        r"""更新私有hook元数据

        更新私有hook元数据（UpdatePrivateHookMetadata）
        
        更新当前私有hook的元数据信息
        
          * 目前支持更新私有hook的描述、默认版本、配置。
          * 如果需要创建新的版本，请调用CreatePrivateHookVersion。
          * 更新为增量更新，即如果某个参数不提供，则保持原始值。
          * 如果请求中没有需要被更新的参数（如请求中没有任何内容，或仅有hook_id），则返回400。注意：即使更新原始值和目标值一致也被认为是有效更新
          * 更新后私有hook的更新时间（update_time）也会被更新
          * 若hook_name和hook_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateHookMetadata
        :type request: :class:`huaweicloudsdkaos.v1.UpdatePrivateHookMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdatePrivateHookMetadataResponse`
        """
        http_info = self._update_private_hook_metadata_http_info(request)
        return self._call_api(**http_info)

    def update_private_hook_metadata_invoker(self, request):
        http_info = self._update_private_hook_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_private_hook_metadata_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/private-hooks/{hook_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateHookMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hook_name' in local_var_params:
            path_params['hook_name'] = local_var_params['hook_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_private_module(self, request):
        r"""创建私有模块

        创建私有模块（CreatePrivateModule）
        
        创建一个空的私有模块。如果用户给予了module_version与module_uri，则在创建私有模块的同时，在私有模块下创建一个私有模块版本。
          * 模块允许用户将可复用的代码编辑在一起供模块使用。
          * 如果同名私有模块在当前账户中已经存在，则会返回失败。
          * 版本号遵循语义化版本号（Semantic Version），为用户自定义。
          * 资源编排服务只会对模块进行浅校验，如文件大小、是否可以解压、文件数量等。并不会深度校验，即不会做语法类校验。
        
        以HCL格式的模板为例，模板中引用私有模块的语法如下：
        &#x60;&#x60;&#x60;
        module \&quot;my_hello_word_module\&quot; {
          source &#x3D; \&quot;rf://rfs.{region_id}.myhuaweicloud.com/private/{domain_id}/{module_name}?version&#x3D;&#x3D;{module_version}\&quot;
        }
        &#x60;&#x60;&#x60;
        
        以JSON格式的模板为例，模板中引用私有模块的语法如下：
        &#x60;&#x60;&#x60;
        {
          \&quot;module\&quot;: {
            \&quot;my_hello_word_module\&quot;: {
              \&quot;source\&quot;: \&quot;rf://rfs.{region_id}.myhuaweicloud.com/private/{domain_id}/{module_name}?version&#x3D;&#x3D;{module_version}\&quot;
            }
          }
        }
        &#x60;&#x60;&#x60;
        对应上述两个例子中的模块链接（source字段的内容）可以调用ShowPrivateModuleVersionMetadata返回的module_source字段中获取
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateModule
        :type request: :class:`huaweicloudsdkaos.v1.CreatePrivateModuleRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreatePrivateModuleResponse`
        """
        http_info = self._create_private_module_http_info(request)
        return self._call_api(**http_info)

    def create_private_module_invoker(self, request):
        http_info = self._create_private_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_private_module_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-modules",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_private_module_version(self, request):
        r"""创建私有模块版本

        创建私有模块版本（CreatePrivateModuleVersion）
        
        创建新的私有模块版本
        
          * 模块的版本号需遵循语义化版本号（Semantic Version），为用户自定义。
          * 如果module_name和module_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
          * 资源编排服务只会对模块进行浅校验，如文件大小、是否可以解压、文件数量等。并不会深度校验，即不会做语法类校验。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateModuleVersion
        :type request: :class:`huaweicloudsdkaos.v1.CreatePrivateModuleVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreatePrivateModuleVersionResponse`
        """
        http_info = self._create_private_module_version_http_info(request)
        return self._call_api(**http_info)

    def create_private_module_version_invoker(self, request):
        http_info = self._create_private_module_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_private_module_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-modules/{module_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateModuleVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_private_module(self, request):
        r"""删除私有模块

        删除私有模块（DeletePrivateModule）
        
        删除某个私有模块以及私有模块下的全部模块版本
        
          * 如果module_name和module_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        **请谨慎操作，删除私有模块将会删除该私有模块下的所有的模块版本。**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateModule
        :type request: :class:`huaweicloudsdkaos.v1.DeletePrivateModuleRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeletePrivateModuleResponse`
        """
        http_info = self._delete_private_module_http_info(request)
        return self._call_api(**http_info)

    def delete_private_module_invoker(self, request):
        http_info = self._delete_private_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_private_module_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-modules/{module_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']

        query_params = []
        if 'module_id' in local_var_params:
            query_params.append(('module_id', local_var_params['module_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_private_module_version(self, request):
        r"""删除私有模块版本

        删除私有模块版本（DeletePrivateModuleVersion）
        
        删除某个私有模块版本
        
          * 如果module_name和module_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        **请谨慎操作**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateModuleVersion
        :type request: :class:`huaweicloudsdkaos.v1.DeletePrivateModuleVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeletePrivateModuleVersionResponse`
        """
        http_info = self._delete_private_module_version_http_info(request)
        return self._call_api(**http_info)

    def delete_private_module_version_invoker(self, request):
        http_info = self._delete_private_module_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_private_module_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-modules/{module_name}/versions/{module_version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateModuleVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']
        if 'module_version' in local_var_params:
            path_params['module_version'] = local_var_params['module_version']

        query_params = []
        if 'module_id' in local_var_params:
            query_params.append(('module_id', local_var_params['module_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_private_module_versions(self, request):
        r"""列举私有模块版本

        列举私有模块版本（ListPrivateModuleVersions）
        
        列举所选择的私有模块中所有的模块版本信息。
        
          * 可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir数量须一致，否则返回400。如果未给予sort_key和sort_dir，则默认按照创建时间降序排序。
          * 如果module_name和module_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
          * 如果模块不存在则返回404。
          * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        ListPrivateModuleVersions返回的只有摘要信息（具体摘要信息见ListPrivateModuleVersionsResponseBody），如果用户需要详细的模块版本元数据请调用ShowPrivateModuleVersionMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateModuleVersions
        :type request: :class:`huaweicloudsdkaos.v1.ListPrivateModuleVersionsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListPrivateModuleVersionsResponse`
        """
        http_info = self._list_private_module_versions_http_info(request)
        return self._call_api(**http_info)

    def list_private_module_versions_invoker(self, request):
        http_info = self._list_private_module_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_private_module_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-modules/{module_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateModuleVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']

        query_params = []
        if 'module_id' in local_var_params:
            query_params.append(('module_id', local_var_params['module_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_private_modules(self, request):
        r"""列举私有模块

        列举私有模块（ListPrivateModules）
        
        列举当前局点下用户所有的私有模块。
        
          * 可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir数量须一致，否则返回400。如果未给予sort_key和sort_dir，则默认按照创建时间降序排序。
          * 如果当前用户下没有任何私有模块，则返回空list。
          * 如果需要某个模块的所有版本信息，可以调用ListModuleVersions。
          * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        ListPrivateModules返回的只有摘要信息（具体摘要信息见ListPrivateModulesResponseBody），如果用户需要详细的模块元数据请调用ShowPrivateModuleMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateModules
        :type request: :class:`huaweicloudsdkaos.v1.ListPrivateModulesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListPrivateModulesResponse`
        """
        http_info = self._list_private_modules_http_info(request)
        return self._call_api(**http_info)

    def list_private_modules_invoker(self, request):
        http_info = self._list_private_modules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_private_modules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-modules",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateModulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_module_metadata(self, request):
        r"""获取私有模块元数据

        获取私有模块元数据（ShowPrivateModuleMetadata）
        
        获取当前私有模块的元数据信息
        
          * 具体返回的信息见ShowPrivateModuleMetadataResponseBody，如果想查看私有模块下全部模块版本，请调用ListPrivateModuleVersions。
          * 如果module_name和module_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateModuleMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateModuleMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateModuleMetadataResponse`
        """
        http_info = self._show_private_module_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_private_module_metadata_invoker(self, request):
        http_info = self._show_private_module_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_module_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-modules/{module_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateModuleMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']

        query_params = []
        if 'module_id' in local_var_params:
            query_params.append(('module_id', local_var_params['module_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_module_version_content(self, request):
        r"""获取私有模块版本内容

        获取私有模块版本内容（ShowPrivateModuleVersionContent）
        
        获取指定私有模块对应版本的内容。
        
          * 如果获取成功，则以临时重定向形式返回模块下载链接（OBS Pre Signed地址，有效期为5分钟），大多数的客户端会进行自动重定向并下载模块；
          * 如果未进行自动重定向，请参考HTTP的重定向规则获取模块下载链接，手动下载模块。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateModuleVersionContent
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateModuleVersionContentRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateModuleVersionContentResponse`
        """
        http_info = self._show_private_module_version_content_http_info(request)
        return self._call_api(**http_info)

    def show_private_module_version_content_invoker(self, request):
        http_info = self._show_private_module_version_content_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_module_version_content_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-modules/{module_name}/versions/{module_version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateModuleVersionContentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']
        if 'module_version' in local_var_params:
            path_params['module_version'] = local_var_params['module_version']

        query_params = []
        if 'module_id' in local_var_params:
            query_params.append(('module_id', local_var_params['module_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Location", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_module_version_metadata(self, request):
        r"""获取私有模块版本元数据

        获取私有模块版本元数据（ShowPrivateModuleVersionMetadata）
        
        获取当前私有模块对应的版本的元数据信息
        
          * 具体返回的信息见ShowPrivateModuleVersionMetadataResponseBody。
          * 如果module_name和module_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateModuleVersionMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowPrivateModuleVersionMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowPrivateModuleVersionMetadataResponse`
        """
        http_info = self._show_private_module_version_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_private_module_version_metadata_invoker(self, request):
        http_info = self._show_private_module_version_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_module_version_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-modules/{module_name}/versions/{module_version}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateModuleVersionMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']
        if 'module_version' in local_var_params:
            path_params['module_version'] = local_var_params['module_version']

        query_params = []
        if 'module_id' in local_var_params:
            query_params.append(('module_id', local_var_params['module_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_private_module_metadata(self, request):
        r"""更新私有模块元数据

        更新私有模块元数据（UpdatePrivateModuleMetadata）
        
        更新当前私有模块的元数据信息
        
          * 目前只支持更新私有模块的描述
          * 如果需要创建新的版本，请调用CreatePrivateModuleVersion
          * 更新为增量更新，即如果某个参数不提供，则保持原始值
          * 如果请求中没有需要被更新的参数，则返回400。注意：即使更新原始值和目标值一致也被认为是有效更新
          * 更新后私有模块的更新时间（update_time）也会被更新
          * 如果module_name和module_id同时存在，则资源编排服务会检查是否两个匹配，如果不匹配则会返回400。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateModuleMetadata
        :type request: :class:`huaweicloudsdkaos.v1.UpdatePrivateModuleMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdatePrivateModuleMetadataResponse`
        """
        http_info = self._update_private_module_metadata_http_info(request)
        return self._call_api(**http_info)

    def update_private_module_metadata_invoker(self, request):
        http_info = self._update_private_module_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_private_module_metadata_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/private-modules/{module_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateModuleMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'module_name' in local_var_params:
            path_params['module_name'] = local_var_params['module_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def continue_deploy_stack(self, request):
        r"""继续部署资源栈

        继续部署资源栈（ContinueDeployStack）
        
        此API用于继续部署一个已有的资源栈
        
        * 如果资源栈当前可以继续部署，即处于&#x60;DEPLOYMENT_FAILED&#x60;，则返回202与对应生成的deploymentId，否则将不允许继续部署并返回相应的错误码
        
        * 继续部署操作依然有可能部署失败，用户可以从ListStackEvents获取对应的log，解决后可再次调用此API触发继续部署
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ContinueDeployStack
        :type request: :class:`huaweicloudsdkaos.v1.ContinueDeployStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ContinueDeployStackResponse`
        """
        http_info = self._continue_deploy_stack_http_info(request)
        return self._call_api(**http_info)

    def continue_deploy_stack_invoker(self, request):
        http_info = self._continue_deploy_stack_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _continue_deploy_stack_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/continuations",
            "request_type": request.__class__.__name__,
            "response_type": "ContinueDeployStackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def continue_rollback_stack(self, request):
        r"""继续回滚资源栈

        继续回滚资源栈（ContinueRollbackStack）
        
        此API用于继续回滚一个已有的资源栈
        
        如果资源栈开启了自动回滚，在部署失败的时候则会自动回滚。但是自动回滚依然有可能失败，用户可以根据错误信息修复后，调用ContinueRollbackStack触发继续回滚，即重试回滚
        
        * 如果资源栈当前可以回滚，即处于&#x60;ROLLBACK_FAILED&#x60;，则返回202与对应生成的deploymentId，否则将不允许回滚并返回响应的错误码
        * 继续回滚也有可能会回滚失败。如果失败，用户可以从ListStackEvents获取对应的log，解决后可再次调用ContinueRollbackStack去继续触发回滚
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ContinueRollbackStack
        :type request: :class:`huaweicloudsdkaos.v1.ContinueRollbackStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ContinueRollbackStackResponse`
        """
        http_info = self._continue_rollback_stack_http_info(request)
        return self._call_api(**http_info)

    def continue_rollback_stack_invoker(self, request):
        http_info = self._continue_rollback_stack_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _continue_rollback_stack_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/rollbacks",
            "request_type": request.__class__.__name__,
            "response_type": "ContinueRollbackStackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_stack(self, request):
        r"""创建资源栈

        CreateStack用于生成一个资源栈
        
        * 当请求中不含有模板（template）、参数（vars）等信息，将生成一个无任何资源的空资源栈，返回资源栈ID（stack_id）
        * 当请求中携带了模板（template）、参数（vars）等信息，则会同时创建并部署资源栈，返回资源栈ID（stack_id）和部署ID（deployment_id）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStack
        :type request: :class:`huaweicloudsdkaos.v1.CreateStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateStackResponse`
        """
        http_info = self._create_stack_http_info(request)
        return self._call_api(**http_info)

    def create_stack_invoker(self, request):
        http_info = self._create_stack_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_stack_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stacks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_stack(self, request):
        r"""删除资源栈

        删除资源栈（DeleteStack）
        
        此API用于删除某个资源栈
        **请谨慎操作，删除资源栈将会删除与该资源栈相关的所有数据和资源，如：执行计划、资源栈事件、资源栈输出、资源等。**
        
        * 此API会触发删除资源栈，并以最终一致性删除所有数据（包括通过资源栈模板创建以及通过Import模块导入的已有资源），用户可以调用GetStackMetadata或ListStacks跟踪资源栈删除情况
        * 如果资源栈状态处于非终态（状态以&#x60;IN_PROGRESS&#x60;结尾）状态时，则不允许删除。包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        * 如果资源栈开启了删除保护，则不允许删除。用户可调用GetStackMetadata，查看返回中的&#x60;enable_deletion_protection&#x60;字段判断删除保护是否开启。用户可通过调用UpdateStack关闭删除保护。
        * 如果资源栈删除失败，可以根据StackEvents提示信息修复当前模板中的错误后，部署成功后再次删除资源栈。有以下两种方式触发部署：
          * 调用CreateExecutionPlan创建执行计划，执行计划创建成功后调用ApplyExecutionPlan部署资源栈。
          * 调用DeployStack部署资源栈
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStack
        :type request: :class:`huaweicloudsdkaos.v1.DeleteStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackResponse`
        """
        http_info = self._delete_stack_http_info(request)
        return self._call_api(**http_info)

    def delete_stack_invoker(self, request):
        http_info = self._delete_stack_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_stack_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_stack_enhanced(self, request):
        r"""条件删除资源栈

        条件删除资源栈（DeleteStackEnhanced）
        
        此API用于删除某个资源栈，可以选择是否保留资源。
        **请谨慎操作，删除资源栈将默认删除与该资源栈相关的所有数据，如：执行计划、资源栈事件、资源栈输出、资源等。**
        **如果希望删除资源栈保留资源，可以在请求中设置&#x60;retain_all_resources&#x60;对资源进行保留。
        
        * 此API会触发删除资源栈，并以最终一致性删除数据，用户可以调用GetStackMetadata或ListStacks跟踪资源栈删除情况。当删除完成后，被删除资源栈将不会在上述API中返回。
        * 如果资源栈状态处于非终态（状态以&#x60;IN_PROGRESS&#x60;结尾）状态时，则不允许删除。包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        * 如果资源栈开启了删除保护，则不允许删除。用户可调用GetStackMetadata，查看返回中的&#x60;enable_deletion_protection&#x60;字段判断删除保护是否开启。用户可通过调用UpdateStack关闭删除保护。
        * 如果资源栈删除失败，可以根据StackEvents提示信息修复当前模板中的错误后，部署成功后再次删除资源栈。有以下两种方式触发部署：
          * 调用CreateExecutionPlan创建执行计划，执行计划创建成功后调用ApplyExecutionPlan部署资源栈。
          * 调用DeployStack部署资源栈。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStackEnhanced
        :type request: :class:`huaweicloudsdkaos.v1.DeleteStackEnhancedRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackEnhancedResponse`
        """
        http_info = self._delete_stack_enhanced_http_info(request)
        return self._call_api(**http_info)

    def delete_stack_enhanced_invoker(self, request):
        http_info = self._delete_stack_enhanced_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_stack_enhanced_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/deletion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStackEnhancedResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def deploy_stack(self, request):
        r"""部署资源栈

        部署资源栈（DeployStack）
        
        此API用于部署一个已有的资源栈
        
        * 用户可以使用此API更新模板、参数等并触发一个新的部署
        
        * 此API会直接触发部署，如果用户希望先确认部署会发生的时间，请使用执行计划，即使用CreateExecutionPlan以创建执行计划、使用GetExecutionPlan以获取执行计划
        
        * 此API为全量API，即用户每次部署都需要给予所想要使用的template、vars的全量
        
        * 部署资源栈时，用户将模板中定义的资源删除（包括Import定义的资源），会触发实际资源的删除。建议通过CreateExecutionPlan查看模板修改后资源栈的部署行为，以避免误操作非预期资源
        
        * 当触发的部署失败时，如果资源栈开启了自动回滚，会触发自动回滚的流程，否则就会停留在部署失败时的状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeployStack
        :type request: :class:`huaweicloudsdkaos.v1.DeployStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeployStackResponse`
        """
        http_info = self._deploy_stack_http_info(request)
        return self._call_api(**http_info)

    def deploy_stack_invoker(self, request):
        http_info = self._deploy_stack_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _deploy_stack_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "DeployStackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_stack_metadata(self, request):
        r"""获取资源栈元数据

        获取资源栈元数据（GetStackMetadata）
        
        此API用于获取指定资源栈的元数据，包括资源栈ID、资源栈名称、资源栈描述、创建时间、更新时间、资源栈状态、委托授权等信息。
        
        具体信息见GetStackMetadataResponseBody。
        
        注：
        当资源栈状态处于非终态（即以&#x60;IN_PROGRESS&#x60;结尾，详细见下方）状态时，资源栈的元数据信息处于转变阶段，可能为部署前的状态，也可能为部署后的状态。
        只有当资源栈状态处于终态（即以&#x60;COMPLETE&#x60;或&#x60;FAILED&#x60;结尾，详细见下方）时，资源栈的元数据信息才是部署后的状态
        
        非终态状态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
        
        终态状态包括但不限于以下状态：
          * 生成空资源栈完成（CREATION_COMPLETE）
          * 部署失败（DEPLOYMENT_FAILED）
          * 部署完成（DEPLOYMENT_COMPLETE）
          * 回滚失败（ROLLBACK_FAILED）
          * 回滚完成（ROLLBACK_COMPLETE）
          * 删除失败（DELETION_FAILED）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetStackMetadata
        :type request: :class:`huaweicloudsdkaos.v1.GetStackMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetStackMetadataResponse`
        """
        http_info = self._get_stack_metadata_http_info(request)
        return self._call_api(**http_info)

    def get_stack_metadata_invoker(self, request):
        http_info = self._get_stack_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_stack_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "GetStackMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_stack_template(self, request):
        r"""获取资源栈模板

        获取资源栈模板（GetStackTemplate）
        
        此API用于获取资源栈最近一次部署终态使用的模板。
        
        注：
        当资源栈状态处于非终态（即以&#x60;IN_PROGRESS&#x60;结尾，详细见下方）状态时，资源栈处于转变阶段，此API获取资源栈上一次部署使用的模板。
        只有当资源栈状态处于终态（即以&#x60;COMPLETE&#x60;或&#x60;FAILED&#x60;结尾，详细见下方）时，此API获取当前最新一次部署使用的模板。CREATION_COMPLETE除外，此时资源栈没有模板，返回404，并提示模板不存在
        
        非终态状态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
        
        终态状态包括但不限于以下状态：
          * 生成空资源栈完成（CREATION_COMPLETE）
          * 部署失败（DEPLOYMENT_FAILED）
          * 部署完成（DEPLOYMENT_COMPLETE）
          * 回滚失败（ROLLBACK_FAILED）
          * 回滚完成（ROLLBACK_COMPLETE）
          * 删除失败（DELETION_FAILED）
        
        如果获取成功，则以临时重定向形式返回模板下载链接（OBS Pre Signed地址，有效期为5分钟），大多数的客户端会进行自动重定向并下载模板；
        如果未进行自动重定向，请参考HTTP的重定向规则获取模板下载链接，手动下载模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetStackTemplate
        :type request: :class:`huaweicloudsdkaos.v1.GetStackTemplateRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetStackTemplateResponse`
        """
        http_info = self._get_stack_template_http_info(request)
        return self._call_api(**http_info)

    def get_stack_template_invoker(self, request):
        http_info = self._get_stack_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_stack_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "GetStackTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'access_control_source_ips' in local_var_params:
            query_params.append(('access_control_source_ips', local_var_params['access_control_source_ips']))
            collection_formats['access_control_source_ips'] = 'multi'
        if 'access_control_source_vpc_ids' in local_var_params:
            query_params.append(('access_control_source_vpc_ids', local_var_params['access_control_source_vpc_ids']))
            collection_formats['access_control_source_vpc_ids'] = 'multi'

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Location", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stack_events(self, request):
        r"""列举资源栈事件

        列举资源栈事件（ListStackEvents）
        
        此API用于列举资源栈某一次或全部的部署事件
        
        * 如果给予deployment_id，则会将deployment_id作为查询条件，返回对应某一次部署的资源栈事件；如果不给予deployment_id，则返回全量的资源栈事件
        * 如果给定的deployment_id对应的部署不存在，则返回404
        * 可以使用filter作为过滤器，过滤出指定事件类型（event_type）、资源类型（resource_type）、资源名称（resource_name）的资源栈事件
        * 可以使用field选择数据应返回的属性，属性事件类型（event_type）不可配置，一定会返回，可选择的属性有逝去时间（elapsed_seconds）、事件消息（event_message）、 资源ID键（resource_id_key）、资源ID值（resource_id_value）、资源键（resource_key）、资源类型（resource_type）、资源名称（resource_name）和时间戳（timestamp）
        * 事件返回将以时间降序排列
        * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackEvents
        :type request: :class:`huaweicloudsdkaos.v1.ListStackEventsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackEventsResponse`
        """
        http_info = self._list_stack_events_http_info(request)
        return self._call_api(**http_info)

    def list_stack_events_invoker(self, request):
        http_info = self._list_stack_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stack_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListStackEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'deployment_id' in local_var_params:
            query_params.append(('deployment_id', local_var_params['deployment_id']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'field' in local_var_params:
            query_params.append(('field', local_var_params['field']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stack_outputs(self, request):
        r"""列举资源栈输出

        列举资源栈输出（ListStackOutputs）
        
        此API用于列举该资源栈的所有输出
        
        资源栈输出为用户在模板中定义的 output 语句块在部署结束后所产生的返回信息，用户可在部署结束后，调用此API获取其具体的输出信息
        
        当资源栈状态处于非终态（状态以&#x60;IN_PROGRESS&#x60;结尾）状态时，此API将返回空。非终态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        output为HCL官方定义的语法，其返回信息类似于常见编程语言中的返回值，详细定义请参考HCL官方的说明
        支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackOutputs
        :type request: :class:`huaweicloudsdkaos.v1.ListStackOutputsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackOutputsResponse`
        """
        http_info = self._list_stack_outputs_http_info(request)
        return self._call_api(**http_info)

    def list_stack_outputs_invoker(self, request):
        http_info = self._list_stack_outputs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stack_outputs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/outputs",
            "request_type": request.__class__.__name__,
            "response_type": "ListStackOutputsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stack_resources(self, request):
        r"""列举资源栈资源

        列举资源栈资源（ListStackResources）
        
        此API用于列举资源栈中当前管理的所有资源的信息
        
        当资源栈处于非终态时，仅输出资源栈下资源的简要信息，包含逻辑资源名称（logical_resource_name），逻辑资源类型（logical_resource_type），物理资源id（physical_resource_id），物理资源名称（physical_resource_name），资源状态（status）等信息；当资源栈处于终态时，将额外输出具体信息，如资源属性（resource_attributes）
        
        非终态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackResources
        :type request: :class:`huaweicloudsdkaos.v1.ListStackResourcesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackResourcesResponse`
        """
        http_info = self._list_stack_resources_http_info(request)
        return self._call_api(**http_info)

    def list_stack_resources_invoker(self, request):
        http_info = self._list_stack_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stack_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListStackResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stacks(self, request):
        r"""列举资源栈

        列举资源栈（ListStacks）
        
        此API用于列举当前局点下用户所有的资源栈
        
          * 默认按照生成时间降序排序，最新生成的在最前
          * 如果没有任何资源栈，则返回空list
          * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        ListStacks返回的只有摘要信息（具体摘要信息见ListStacksResponseBody），如果用户需要详细的资源栈元数据请调用GetStackMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStacks
        :type request: :class:`huaweicloudsdkaos.v1.ListStacksRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStacksResponse`
        """
        http_info = self._list_stacks_http_info(request)
        return self._call_api(**http_info)

    def list_stacks_invoker(self, request):
        http_info = self._list_stacks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stacks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stacks",
            "request_type": request.__class__.__name__,
            "response_type": "ListStacksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_stack(self, request):
        r"""更新资源栈

        更新资源栈（UpdateStack）
        
        更新资源栈的属性，该API可以根据用户给予的信息对资源栈的属性进行更新，可以更新资源栈的“description”、“enable_deletion_protection”、\&quot;enable_auto_rollback\&quot;、\&quot;agencies\&quot;四个属性中的一个或多个
        
        该API只会更新用户给予的信息中所涉及的字段；如果某字段未给予，则不会对该资源栈属性进行更新
        
        注：所有属性的更新都是覆盖式更新。即，所给予的参数将被完全覆盖至资源栈已有的属性上
        
        例如，如果要新增agencies，请通过GetStackMetadata获取该资源栈原有的agencies信息，将新旧agencies信息进行整合后再调用UpdateStack
        
        * 如果资源栈状态处于非终态（状态以&#x60;IN_PROGRESS&#x60;结尾）状态时，则不允许更新。包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        * 对于“enable_auto_rollback”属性从false到true的更新操作，资源栈状态判定将更加严格，在失败（状态以&#x60;_FAILED&#x60;结尾）状态时也不允许更新，包括但不限于以下状态：
          * 部署失败（DEPLOYMENT_FAILED）
          * 回滚失败（ROLLBACK_FAILED）
          * 删除失败（DELETION_FAILED）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStack
        :type request: :class:`huaweicloudsdkaos.v1.UpdateStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdateStackResponse`
        """
        http_info = self._update_stack_http_info(request)
        return self._call_api(**http_info)

    def update_stack_invoker(self, request):
        http_info = self._update_stack_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_stack_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/stacks/{stack_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_stack_instance(self, request):
        r"""创建资源栈实例

        创建资源栈实例（CreateStackInstance）
        
        此API用于在指定资源栈集下生成多个资源栈实例，并返回资源栈集操作ID（stack_set_operation_id）
        
        此API可以通过var_overrides参数，指定创建资源栈实例的参数值，进行参数覆盖。如果var_overrides参数未给予，则默认使用当前资源栈集中记录的参数进行部署，详见：var_overrides参数描述。
        
        通过DeployStackSet API更新资源栈集参数后，资源栈实例中已经被覆盖的参数不会被更新，仍然保留覆盖值。
        
        用户只能覆盖已经在资源栈集中记录的参数，如果用户想要增加可以覆盖的参数，需要先通过DeployStackSet API更新资源栈集记录的参数集合。
        
        * 用户可以根据资源栈集操作ID（stack_set_operation_id），通过ShowStackSetOperationMetadata API获取资源栈集操作状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStackInstance
        :type request: :class:`huaweicloudsdkaos.v1.CreateStackInstanceRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateStackInstanceResponse`
        """
        http_info = self._create_stack_instance_http_info(request)
        return self._call_api(**http_info)

    def create_stack_instance_invoker(self, request):
        http_info = self._create_stack_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_stack_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stack-sets/{stack_set_name}/stack-instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStackInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_stack_set(self, request):
        r"""创建资源栈集

        创建资源栈集（CreateStackSet）
        
        此API为同步API，用于生成一个空资源栈集，即不包含任何一个资源栈实例，并返回资源栈集ID（stack_set_id）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStackSet
        :type request: :class:`huaweicloudsdkaos.v1.CreateStackSetRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateStackSetResponse`
        """
        http_info = self._create_stack_set_http_info(request)
        return self._call_api(**http_info)

    def create_stack_set_invoker(self, request):
        http_info = self._create_stack_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_stack_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stack-sets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStackSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_stack_instance(self, request):
        r"""删除资源栈实例

        删除资源栈实例（DeleteStackInstance）
        
        此API用于删除指定资源栈集下指定局点（region）或指定成员账号（domain_id）的资源栈实例，并返回资源栈集操作ID（stack_set_operation_id）
        
        **请谨慎操作，删除资源栈实例将会删除与该资源栈实例相关的堆栈以及堆栈所管理的一切资源。**
        
        * 用户可以根据资源栈集操作ID（stack_set_operation_id），通过ShowStackSetOperationMetadata API获取资源栈集操作状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStackInstance
        :type request: :class:`huaweicloudsdkaos.v1.DeleteStackInstanceRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackInstanceResponse`
        """
        http_info = self._delete_stack_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_stack_instance_invoker(self, request):
        http_info = self._delete_stack_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_stack_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stack-sets/{stack_set_name}/stack-instances/deletion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStackInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_stack_instance_deprecated(self, request):
        r"""删除资源栈实例-已废弃

        删除资源栈实例-被废弃（DeleteStackInstanceDeprecated）
        
        此API用于删除指定资源栈集下指定局点（region）或指定成员账号（domain_id）的资源栈实例，并返回资源栈集操作ID（stack_set_operation_id）
        
        **请谨慎操作，删除资源栈实例将会删除与该资源栈实例相关的堆栈以及堆栈所管理的一切资源。**
        
        * 用户可以根据资源栈集操作ID（stack_set_operation_id），通过ShowStackSetOperationMetadata API获取资源栈集操作状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStackInstanceDeprecated
        :type request: :class:`huaweicloudsdkaos.v1.DeleteStackInstanceDeprecatedRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackInstanceDeprecatedResponse`
        """
        http_info = self._delete_stack_instance_deprecated_http_info(request)
        return self._call_api(**http_info)

    def delete_stack_instance_deprecated_invoker(self, request):
        http_info = self._delete_stack_instance_deprecated_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_stack_instance_deprecated_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/stack-sets/{stack_set_name}/stack-instances",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStackInstanceDeprecatedResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_stack_set(self, request):
        r"""删除资源栈集

        删除资源栈集（DeleteStackSet）
        
        **请谨慎操作，删除资源栈集将会删除与该资源栈集相关的所有数据，如：资源栈集操作、资源栈集操作事件等。**
        
        当且仅当指定的资源栈集满足以下所有条件时，资源栈集才能被成功删除，否则会报错：
          * 资源栈集下没有资源栈实例
          * 资源栈集状态处于空闲（&#x60;IDLE&#x60;）状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStackSet
        :type request: :class:`huaweicloudsdkaos.v1.DeleteStackSetRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackSetResponse`
        """
        http_info = self._delete_stack_set_http_info(request)
        return self._call_api(**http_info)

    def delete_stack_set_invoker(self, request):
        http_info = self._delete_stack_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_stack_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/stack-sets/{stack_set_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStackSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []
        if 'stack_set_id' in local_var_params:
            query_params.append(('stack_set_id', local_var_params['stack_set_id']))
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def deploy_stack_set(self, request):
        r"""部署资源栈集

        部署资源栈集（DeployStackSet）
        
        此API用于部署一个已有的资源栈集，并返回资源栈集操作ID（stack_set_operation_id）
        
        * 用户可以使用此API更新资源栈集的模板、参数并进行部署。
        
        * 此API会直接触发资源栈实例部署。用户既可以部署资源栈集下所有的资源栈实例，也可以部署指定资源栈实例。
        
        * 此API为全量API，即用户每次部署都需要给予所想要使用的template、vars的全量
        
        * 当触发的部署失败时，资源栈集不会自动回滚模板和参数，但部署失败的资源栈会根据资源栈的回滚配置决定是否进行回滚，已经部署成功的资源栈不会触发回滚。
        
        * 用户可以根据资源栈集操作ID（stack_set_operation_id），通过ShowStackSetOperationMetadata API获取资源栈集操作状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeployStackSet
        :type request: :class:`huaweicloudsdkaos.v1.DeployStackSetRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeployStackSetResponse`
        """
        http_info = self._deploy_stack_set_http_info(request)
        return self._call_api(**http_info)

    def deploy_stack_set_invoker(self, request):
        http_info = self._deploy_stack_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _deploy_stack_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stack-sets/{stack_set_name}/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "DeployStackSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stack_instances(self, request):
        r"""列举资源栈实例

        列举资源栈实例（ListStackInstances）
        
        此API用于列举指定资源栈集下指定局点（region）或指定成员账号（stack_domain_id）或全部资源栈实例
        
        * 可以使用filter作为过滤器，过滤出指定局点（region）或指定成员账号（stack_domain_id）下的资源栈实例
        * 可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir数量须一致，否则返回400。如果未给予sort_key和sort_dir，则默认按照创建时间降序排序。
        * 如果指定资源栈集下没有任何资源栈实例，则返回空list
        * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackInstances
        :type request: :class:`huaweicloudsdkaos.v1.ListStackInstancesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackInstancesResponse`
        """
        http_info = self._list_stack_instances_http_info(request)
        return self._call_api(**http_info)

    def list_stack_instances_invoker(self, request):
        http_info = self._list_stack_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stack_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/stack-sets/{stack_set_name}/stack-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListStackInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []
        if 'stack_set_id' in local_var_params:
            query_params.append(('stack_set_id', local_var_params['stack_set_id']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stack_set_operations(self, request):
        r"""列举资源栈集操作

        列举资源栈集操作（ListStackSetOperations）
        
        列举指定资源栈集下所有的资源栈集的操作。
        
        可以使用filter作为过滤器，过滤出指定操作状态（status）或操作类型（action）下的资源栈集操作。
        可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir数量须一致，否则返回400。如果未给予sort_key和sort_dir，则默认按照创建时间降序排序。
        如果指定资源栈集下没有任何资源栈集操作，则返回空list。
        支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackSetOperations
        :type request: :class:`huaweicloudsdkaos.v1.ListStackSetOperationsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackSetOperationsResponse`
        """
        http_info = self._list_stack_set_operations_http_info(request)
        return self._call_api(**http_info)

    def list_stack_set_operations_invoker(self, request):
        http_info = self._list_stack_set_operations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stack_set_operations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/stack-sets/{stack_set_name}/operations",
            "request_type": request.__class__.__name__,
            "response_type": "ListStackSetOperationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []
        if 'stack_set_id' in local_var_params:
            query_params.append(('stack_set_id', local_var_params['stack_set_id']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stack_sets(self, request):
        r"""列举资源栈集

        列举资源栈集（ListStackSets）
        
        此API用于列举当前用户（domain）当前局点（region）下全部资源栈集。
        
        * 可以使用filter作为过滤器，过滤出指定权限模型（permission_model）下的资源栈集。
        * 可以使用sort_key和sort_dir两个关键字对返回结果按创建时间（create_time）进行排序。给予的sort_key和sort_dir数量须一致，否则返回400。如果未给予sort_key和sort_dir，则默认按照创建时间降序排序。
        * 注意：目前暂时返回全量资源栈集信息，即不支持分页
        * 如果没有任何资源栈集，则返回空list
        * 支持分页返回。如果响应中存在next_marker，则表示实际总输出比当前响应中包含的输出多。在对请求的后续调用中，在请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackSets
        :type request: :class:`huaweicloudsdkaos.v1.ListStackSetsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackSetsResponse`
        """
        http_info = self._list_stack_sets_http_info(request)
        return self._call_api(**http_info)

    def list_stack_sets_invoker(self, request):
        http_info = self._list_stack_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stack_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/stack-sets",
            "request_type": request.__class__.__name__,
            "response_type": "ListStackSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_stack_instance(self, request):
        r"""获取资源栈实例

        获取资源栈实例（ShowStackInstance）
        
        用户可以使用此API获取资源栈实例的详细信息，包括关联资源栈名称与id，创建时间，参数覆盖等
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStackInstance
        :type request: :class:`huaweicloudsdkaos.v1.ShowStackInstanceRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowStackInstanceResponse`
        """
        http_info = self._show_stack_instance_http_info(request)
        return self._call_api(**http_info)

    def show_stack_instance_invoker(self, request):
        http_info = self._show_stack_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_stack_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/stack-sets/{stack_set_name}/stack-instances/{stack_instance_addr}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStackInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']
        if 'stack_instance_addr' in local_var_params:
            path_params['stack_instance_addr'] = local_var_params['stack_instance_addr']

        query_params = []
        if 'stack_set_id' in local_var_params:
            query_params.append(('stack_set_id', local_var_params['stack_set_id']))
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_stack_set_metadata(self, request):
        r"""获取资源栈集元数据

        获取资源栈集元数据（ShowStackSetMetadata）
        
        * 用户可以使用此API获取资源栈集的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStackSetMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowStackSetMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowStackSetMetadataResponse`
        """
        http_info = self._show_stack_set_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_stack_set_metadata_invoker(self, request):
        http_info = self._show_stack_set_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_stack_set_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/stack-sets/{stack_set_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStackSetMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []
        if 'stack_set_id' in local_var_params:
            query_params.append(('stack_set_id', local_var_params['stack_set_id']))
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_stack_set_operation_metadata(self, request):
        r"""获取资源栈集操作的元数据

        获取资源栈集操作元数据（ShowStackSetOperationMetadata）
        
        此API用于获取指定资源栈集操作的元数据，包括资源栈集操作ID、资源栈集ID、资源栈集名称、资源栈集操作状态、创建时间、更新时间、部署目标等信息。
        
        具体信息见ShowStackSetOperationMetadataResponseBody。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStackSetOperationMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowStackSetOperationMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowStackSetOperationMetadataResponse`
        """
        http_info = self._show_stack_set_operation_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_stack_set_operation_metadata_invoker(self, request):
        http_info = self._show_stack_set_operation_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_stack_set_operation_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/stack-sets/{stack_set_name}/operations/{stack_set_operation_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStackSetOperationMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']
        if 'stack_set_operation_id' in local_var_params:
            path_params['stack_set_operation_id'] = local_var_params['stack_set_operation_id']

        query_params = []
        if 'stack_set_id' in local_var_params:
            query_params.append(('stack_set_id', local_var_params['stack_set_id']))
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_stack_set_template(self, request):
        r"""获取资源栈集模板

        获取资源栈集模板（ShowStackSetTemplate）
        
        此API用于获取指定资源栈集的模板。
        
        如果获取成功，则以临时重定向形式返回模板下载链接（OBS Pre Signed地址，有效期为5分钟），大多数的客户端会进行自动重定向并下载模板；
        如果未进行自动重定向，请参考HTTP的重定向规则获取模板下载链接，手动下载模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStackSetTemplate
        :type request: :class:`huaweicloudsdkaos.v1.ShowStackSetTemplateRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowStackSetTemplateResponse`
        """
        http_info = self._show_stack_set_template_http_info(request)
        return self._call_api(**http_info)

    def show_stack_set_template_invoker(self, request):
        http_info = self._show_stack_set_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_stack_set_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/stack-sets/{stack_set_name}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStackSetTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []
        if 'stack_set_id' in local_var_params:
            query_params.append(('stack_set_id', local_var_params['stack_set_id']))
        if 'access_control_source_ips' in local_var_params:
            query_params.append(('access_control_source_ips', local_var_params['access_control_source_ips']))
            collection_formats['access_control_source_ips'] = 'multi'
        if 'access_control_source_vpc_ids' in local_var_params:
            query_params.append(('access_control_source_vpc_ids', local_var_params['access_control_source_vpc_ids']))
            collection_formats['access_control_source_vpc_ids'] = 'multi'
        if 'call_identity' in local_var_params:
            query_params.append(('call_identity', local_var_params['call_identity']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Location", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_stack_instances(self, request):
        r"""更新资源栈实例

        更新资源栈实例（UpdateStackInstances）
        
        此API用于更新并部署指定资源栈实例集合，并返回资源栈集操作ID（stack_set_operation_id）
        
        此API可以通过var_overrides参数，更新指定资源栈实例的参数值，进行参数覆盖。如果var_overrides参数未给予，则默认使用当前资源栈集中记录的参数进行部署，详见：var_overrides参数描述。用户只可以更新已经存在的资源栈实例，如果用户想要增加额外的资源栈实例，请使用CreateStackInstances API。
        
        通过DeployStackSet API更新资源栈集参数后，资源栈实例中已经被覆盖的参数不会被更新，仍然保留覆盖值。
        
        用户只能覆盖已经在资源栈集中记录的参数，如果用户想要增加可以覆盖的参数，需要先通过DeployStackSet API更新资源栈集记录的参数集合。
        
        * 当触发的部署失败时，资源栈实例不会自动回滚参数覆盖，但部署失败的资源栈会默认自动回滚，已经部署成功的资源栈不会触发回滚。
        
        * 用户可以根据资源栈集操作ID（stack_set_operation_id），通过ShowStackSetOperationMetadata API获取资源栈集操作状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStackInstances
        :type request: :class:`huaweicloudsdkaos.v1.UpdateStackInstancesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdateStackInstancesResponse`
        """
        http_info = self._update_stack_instances_http_info(request)
        return self._call_api(**http_info)

    def update_stack_instances_invoker(self, request):
        http_info = self._update_stack_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_stack_instances_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/stack-sets/{stack_set_name}/stack-instances",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStackInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_stack_set(self, request):
        r"""更新资源栈集

        更新资源栈集（UpdateStackSet）
        
        该API可以根据用户给予的信息对资源栈集的属性进行更新，可以更新资源栈集的“stack_set_description”、\&quot;initial_stack_description\&quot;、\&quot;permission_model\&quot;、“administration_agency_name”、\&quot;managed_agency_name\&quot;、“administration_agency_urn”六个属性中的一个或多个。
        
        该API只会更新用户给予的信息中所涉及的字段；如果某字段未给予，则不会对该资源栈集属性进行更新。
        
        注：
          * 所有属性的更新都是覆盖式更新。即，所给予的参数将被完全覆盖至资源栈已有的属性上。
          * 只有在permission_model&#x3D;SELF_MANAGED时，才可更新administration_agency_name、managed_agency_name和administration_agency_urn。
          * permission_model目前只支持更新SELF_MANAGED
          * 如果资源栈集的状态是OPERATION_IN_PROGRESS，不允许更新资源栈集。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStackSet
        :type request: :class:`huaweicloudsdkaos.v1.UpdateStackSetRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdateStackSetResponse`
        """
        http_info = self._update_stack_set_http_info(request)
        return self._call_api(**http_info)

    def update_stack_set_invoker(self, request):
        http_info = self._update_stack_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_stack_set_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/stack-sets/{stack_set_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStackSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_set_name' in local_var_params:
            path_params['stack_set_name'] = local_var_params['stack_set_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def parse_template_variables(self, request):
        r"""解析模板参数

        解析模板参数（ParseTemplateVariables）
        
        此API用于解析用户输入的模板中的参数（variable），将解析模板中的所有variable块并返回
        
        * 如果用户传入的模板中定义了variable参数，则返回200和所有variable
        * 如果用户传入的模板中没有定义variable参数，则返回200和空对象
        * 如果用户请求非法或传入的模板非法，则返回400
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseTemplateVariables
        :type request: :class:`huaweicloudsdkaos.v1.ParseTemplateVariablesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ParseTemplateVariablesResponse`
        """
        http_info = self._parse_template_variables_http_info(request)
        return self._call_api(**http_info)

    def parse_template_variables_invoker(self, request):
        http_info = self._parse_template_variables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_template_variables_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/template-analyses/variables",
            "request_type": request.__class__.__name__,
            "response_type": "ParseTemplateVariablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_template(self, request):
        r"""创建模板

        创建模板（CreateTemplate）
        
        此API用于创建一个带有版本的模板
        
          * 请求中必须包括template_uri或是template_body。前者为模板内容obs链接，后者为模板内容
          * 模板管理名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板
          * 模板创建时，会自动生成模板版本号为V1的模板版本
          * 模板必须存在一个或多个模板版本，即不存在没有模板版本的模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkaos.v1.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_template_version(self, request):
        r"""创建模板版本

        创建模板版本（CreateTemplateVersion）
        
        此API用于创建新的模板版本
        
          * 请求中必须包括template_uri或template_body。前者为模板内容obs链接，后者为模板内容
          * 新创建的模板版本版本ID会自动在当前最大模板版本ID的基础上加1
          * 创建模板版本需要的具体信息详见：CreateTemplateVersionRequestBody
          * template_id是模板的唯一Id。此Id由资源编排服务在生成模板的时候生成，为UUID。由于模板名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板。对于团队并行开发，用户可能希望确保，当前我操作的模板就是我认为的那个，而不是其他队友删除后创建的同名模板。因此，使用ID就可以做到强匹配。资源编排服务保证每次创建的模板所对应的ID都不相同，更新不会影响ID。如果给予的template_id和当前模板管理的ID不一致，则返回400
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplateVersion
        :type request: :class:`huaweicloudsdkaos.v1.CreateTemplateVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateTemplateVersionResponse`
        """
        http_info = self._create_template_version_http_info(request)
        return self._call_api(**http_info)

    def create_template_version_invoker(self, request):
        http_info = self._create_template_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_template_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/templates/{template_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_template(self, request):
        r"""删除模板

        删除模板（DeleteTemplate）
        
        此API用于删除某个模板以及模板下的全部模板版本
        **请谨慎操作，删除模板将会删除模板下的所有模板版本。**
        
          * template_id是模板的唯一Id。此Id由资源编排服务在生成模板的时候生成，为UUID。由于模板名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板。对于团队并行开发，用户可能希望确保，当前我操作的模板就是我认为的那个，而不是其他队友删除后创建的同名模板。因此，使用ID就可以做到强匹配。资源编排服务保证每次创建的模板所对应的ID都不相同，更新不会影响ID。如果给予的template_id和当前模板管理的ID不一致，则返回400
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkaos.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/templates/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_template_version(self, request):
        r"""删除模板版本

        删除模板版本（DeleteTemplateVersion）
        
        此API用于删除某个模板版本
        
          * template_id是模板的唯一Id。此Id由资源编排服务在生成模板的时候生成，为UUID。由于模板名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板。对于团队并行开发，用户可能希望确保，当前我操作的模板就是我认为的那个，而不是其他队友删除后创建的同名模板。因此，使用ID就可以做到强匹配。资源编排服务保证每次创建的模板所对应的ID都不相同，更新不会影响ID。如果给予的template_id和当前模板管理的ID不一致，则返回400
          * 如果模板下只存在唯一模板版本，此模板版本将无法被删除，如果需要删除此模板版本，请调用DeleteTemplate。模板服务不允许存在没有模板版本的模板
        
        **请谨慎操作**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplateVersion
        :type request: :class:`huaweicloudsdkaos.v1.DeleteTemplateVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteTemplateVersionResponse`
        """
        http_info = self._delete_template_version_http_info(request)
        return self._call_api(**http_info)

    def delete_template_version_invoker(self, request):
        http_info = self._delete_template_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_template_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/templates/{template_name}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_template_versions(self, request):
        r"""列举模板版本

        列举模板版本信息（ListTemplateVersions）
        
        此API用于列举模板下所有的模板版本信息
        
          * 默认按照生成时间降序排序，最新生成的模板排列在最前面
          * 注意：目前返回全量模板版本信息，即不支持分页
          * 如果没有任何模板版本，则返回空list
          * template_id是模板的唯一Id。此Id由资源编排服务在生成模板的时候生成，为UUID。由于模板名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板。对于团队并行开发，用户可能希望确保，当前我操作的模板就是我认为的那个，而不是其他队友删除后创建的同名模板。因此，使用ID就可以做到强匹配。资源编排服务保证每次创建的模板所对应的ID都不相同，更新不会影响ID。如果给予的template_id和当前模板管理的ID不一致，则返回400
          * 如果模板不存在则返回404
        
        ListTemplateVersions返回的信息只包含模板版本摘要信息（具体摘要信息见ListTemplateVersionsResponseBody），如果用户需要了解模板版本内容，请调用ShowTemplateVersionContent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateVersions
        :type request: :class:`huaweicloudsdkaos.v1.ListTemplateVersionsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListTemplateVersionsResponse`
        """
        http_info = self._list_template_versions_http_info(request)
        return self._call_api(**http_info)

    def list_template_versions_invoker(self, request):
        http_info = self._list_template_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/templates/{template_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_templates(self, request):
        r"""列举模板

        列举模板（ListTemplates）
        
        此API用于列举当前局点下用户所有的模板
        
          * 默认按照生成时间降序排序，最新生成的模板排列在最前面
          * 注意：目前返回全量模板信息，即不支持分页
          * 如果没有任何模板，则返回空list
          * 如果用户需要详细的模板版本信息，请调用ListTemplateVersions
        
        ListTemplates返回的信息只包含模板摘要信息（具体摘要信息见ListTemplatesResponseBody），如果用户需要详细的某个模板信息，请调用ShowTemplateMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkaos.v1.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_template_metadata(self, request):
        r"""获取模板元数据

        获取模板元数据（ShowTemplateMetadata）
        
        此API用于获取当前模板的元数据信息
        
        具体信息见ShowTemplateMetadataResponseBody，如果想查看模板下全部模板版本，请调用ListTemplateVersions。
        
          * template_id是模板的唯一Id。此Id由资源编排服务在生成模板的时候生成，为UUID。由于模板名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板。对于团队并行开发，用户可能希望确保，当前我操作的模板就是我认为的那个，而不是其他队友删除后创建的同名模板。因此，使用ID就可以做到强匹配。资源编排服务保证每次创建的模板所对应的ID都不相同，更新不会影响ID。如果给予的template_id和当前模板管理的ID不一致，则返回400
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowTemplateMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowTemplateMetadataResponse`
        """
        http_info = self._show_template_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_template_metadata_invoker(self, request):
        http_info = self._show_template_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/templates/{template_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_template_version_content(self, request):
        r"""获取模板版本内容

        获取模板版本内容（ShowTemplateVersionContent）
        
        此API用于获取用户的模板版本内容
        
          * template_id是模板的唯一Id。此Id由资源编排服务在生成模板的时候生成，为UUID。由于模板名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板。对于团队并行开发，用户可能希望确保，当前我操作的模板就是我认为的那个，而不是其他队友删除后创建的同名模板。因此，使用ID就可以做到强匹配。资源编排服务保证每次创建的模板所对应的ID都不相同，更新不会影响ID。如果给予的template_id和当前模板管理的ID不一致，则返回400
          * 此api会以临时重定向形式返回模板内容的下载链接，用户通过下载获取模板版本内容（OBS Pre Signed地址，有效期为5分钟）
          * 如果手动访问重定向的obs下载链接，请求时不可以携带任何的Request-Header，否则会导致签名失败
        
        ShowTemplateVersionContent返回的信息只包含模板版本内容，如果想知道模板版本的元数据，请调用ShowTemplateVersionMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateVersionContent
        :type request: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionContentRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionContentResponse`
        """
        http_info = self._show_template_version_content_http_info(request)
        return self._call_api(**http_info)

    def show_template_version_content_invoker(self, request):
        http_info = self._show_template_version_content_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_version_content_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/templates/{template_name}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateVersionContentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
        if 'access_control_source_vpc_ids' in local_var_params:
            query_params.append(('access_control_source_vpc_ids', local_var_params['access_control_source_vpc_ids']))
            collection_formats['access_control_source_vpc_ids'] = 'multi'
        if 'access_control_source_ips' in local_var_params:
            query_params.append(('access_control_source_ips', local_var_params['access_control_source_ips']))
            collection_formats['access_control_source_ips'] = 'multi'

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Location", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_template_version_metadata(self, request):
        r"""获取模板版本元数据

        获取模板版本元数据（ShowTemplateVersionMetadata）
        
        此API用于展示某一版本模板的元数据
        
          * template_id是模板的唯一Id。此Id由资源编排服务在生成模板的时候生成，为UUID。由于模板名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的模板，删除，再重新创建一个同名模板。对于团队并行开发，用户可能希望确保，当前我操作的模板就是我认为的那个，而不是其他队友删除后创建的同名模板。因此，使用ID就可以做到强匹配。资源编排服务保证每次创建的模板所对应的ID都不相同，更新不会影响ID。如果给予的template_id和当前模板管理的ID不一致，则返回400
        
        ShowTemplateVersionMetadata返回的信息只包含模板版本元数据信息（具体摘要信息见ShowTemplateVersionMetadataResponseBody），如果用户需要了解模板版本内容，请调用ShowTemplateVersionContent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateVersionMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionMetadataResponse`
        """
        http_info = self._show_template_version_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_template_version_metadata_invoker(self, request):
        http_info = self._show_template_version_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_version_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/templates/{template_name}/versions/{version_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateVersionMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_template_metadata(self, request):
        r"""更新模板元数据

        更新模板元数据（UpdateTemplateMetadata）
        
        此API用于更新模板元数据
        
        * 此api只支持更新模板描述
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplateMetadata
        :type request: :class:`huaweicloudsdkaos.v1.UpdateTemplateMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdateTemplateMetadataResponse`
        """
        http_info = self._update_template_metadata_http_info(request)
        return self._call_api(**http_info)

    def update_template_metadata_invoker(self, request):
        http_info = self._update_template_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_template_metadata_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/templates/{template_name}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)
