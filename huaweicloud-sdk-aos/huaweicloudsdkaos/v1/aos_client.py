# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class AosClient(Client):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(AosClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaos.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "AosClient":
            raise TypeError("client type error, support client type is AosClient")

        return ClientBuilder(clazz)

    def apply_execution_plan(self, request):
        """执行执行计划

        执行执行计划（ApplyExecutionPlan）
        
        此API用于执行一个执行计划
        
        * 当执行请求接受后，执行计划状态将变为&#x60;APPLY_IN_PROGRESS&#x60;，后台会进行异步处理。
        * 当执行结束后，执行计划状态将变为&#x60;APPLIED&#x60;。
        * 用户可以调用GetStackMetadata查询资源栈的状态（status）来跟踪资源栈部署情况以及确认本次执行结果是否成功。
        
        如果不希望通过执行计划进行部署操作，也可以选择调用DeployStack进行直接部署
        
        关于执行计划的过期失效：
          1. 若指定资源栈下有多个执行计划，则在执行某个执行计划后（无论结果是否成功），剩余所有的执行计划将过期失效；
          2. 若调用ApplyExecutionPlan时，指定的执行计划已经过期失效，则返回403
        
        若资源栈状态处于非终态（即以&#x60;IN_PROGRESS&#x60;结尾，详细见下方）状态时，则不允许执行执行计划，并返回403。非终态状态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanResponse`
        """
        return self.apply_execution_plan_with_http_info(request)

    def apply_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'apply_execution_plan_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_execution_plan(self, request):
        """创建执行计划

        创建执行计划（CreateExecutionPlan）
        
        此API用于在指定的资源栈下生成一个执行计划，执行计划描述了当前资源栈中记录的资源状态和模板描述的目的资源状态之间的区别（如，资源A将以以下配置文件生成，资源B将以下参数从XXX修改成YYY）
        
        调用此API触发创建执行计划之后，可以通过GetExecutionPlanMetadata来跟踪执行计划的状态
        当执行计划状态为&#x60;AVAILABLE&#x60;时，可以通过GetExecutionPlan获取本次执行计划的结果
        
        执行计划不会做过多深层的检查和校验，如用户是否有权限生成、修改资源等
                
        **注意：**
          * 若指定资源栈不存在，则返回404
          * 若请求中不含有template_body和template_uri，则返回400
          * 若资源栈进行了某次部署操作，则在该次部署操作前生成的执行计划将全部失效
          * 执行计划只代表生成时刻的结果，若执行计划生成后，用户手动修改资源状态，则执行计划不会自动更新
          * 若资源栈状态处于&#x60;DEPLOYMENT_IN_PROGRESS&#x60;、&#x60;ROLLBACK_IN_PROGRESS&#x60;、&#x60;DELETION_IN_PROGRESS&#x60;等状态时，则不允许创建执行计划，并返回403
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.CreateExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateExecutionPlanResponse`
        """
        return self.create_execution_plan_with_http_info(request)

    def create_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'create_execution_plan_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_execution_plan(self, request):
        """删除执行计划

        删除执行计划（DeleteExecutionPlan）
        
        删除指定的执行计划
        
        若执行计划状态处于&#x60;CREATION_IN_PROGRESS&#x60;、&#x60;APPLY_IN_PROGRESS&#x60;状态时，则不允许删除并返回403
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.DeleteExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteExecutionPlanResponse`
        """
        return self.delete_execution_plan_with_http_info(request)

    def delete_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def estimate_execution_plan_price(self, request):
        """预估执行计划价格

        预估执行计划价格（EstimateExecutionPlanPrice）
        
        此API可以基于一份已有的执行计划中增量的资源进行询价，当前支持询价的计费模式有包周期计费、按需计费、免费，暂不支持其他形式的计费模式，例如竞价计费模式等。
        
        注：
          * 由于某些资源的属性值含有默认值，且该属性和询价参数相关。若用户的模板中描述的资源没有声明这些属性，则询价结果可能存在偏差。
          * 询价结果仅为预估结果，具体请以实际为准。
          * 若用户在模板中使用了depends_on参数，如A资源询价必要字段依赖于B资源的创建，则A资源不支持询价。
          * 暂不支持传入data sources的flavor.id的场景的询价。
          * 暂不支持镜像询价。
        
        支持询价的资源列表和询价必要参数如下
        
        | 资源类型          | 模板类型                               | 计费模式（按需/包周期/免费） | 询价必要参数                                                                                                                                                                                                                                                                            |
        |---------------|------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | cce           | huaweicloud_cce_cluster            | 包周期、按需          | -                                                                                                                                                                                                                                                                                 |
        | css           | huaweicloud_css_cluster            | 按需              | -                                                                                                                                                                                                                                                                                 |
        | evs           | huaweicloud_evs_volume             | 包周期、按需          | **包周期：**&lt;br/&gt;size：磁盘规格&lt;br/&gt;&lt;br/&gt;**按需：**&lt;br/&gt;size：磁盘规格                                                                                                                                                                                                                             |
        | ecs           | huaweicloud_compute_instance       | 包周期、按需          | **包周期：**&lt;br/&gt;flavor_id：规格ID。flavor_id和flavor_name至少给出一个&lt;br/&gt;flavor_name：规格名称。flavor_id和flavor_name至少给出一个&lt;br/&gt;system_disk_size：系统磁盘大小&lt;br/&gt;&lt;br/&gt;**按需：**&lt;br/&gt;flavor_id：规格ID。flavor_id和flavor_name至少给出一个&lt;br/&gt;flavor_name：规格名称。flavor_id和flavor_name至少给出一个&lt;br/&gt;system_disk_size：系统磁盘大小 |
        | bandwidth     | huaweicloud_vpc_bandwidth          | 按需              | charge_mode: 仅支持bandwidth                                                                                                                                                                                                                                                         |
        | eip           | huaweicloud_vpc_eip                | 包周期、按需          | **包周期：**&lt;br/&gt;bandwidth.size：带宽大小&lt;br/&gt;&lt;br/&gt;**按需：**&lt;br/&gt;bandwidth.size：带宽大小                                                                                                                                                                                                         |
        | gaussdb_redis | huaweicloud_gaussdb_redis_instance | 包周期、按需          | -                                                                                                                                                                                                                                                                                 |
        | nat           | huaweicloud_nat_gateway            | 按需              | -                                                                                                                                                                                                                                                                                 |
        | rds           | huaweicloud_rds_instance           | 包周期、按需          | -                                                                                                                                                                                                                                                                                 |
        | sfs_turbo     | huaweicloud_sfs_turbo              | 按需              | share_type：文件系统类型                                                                                                                                                                                                                                                                 |
        | dms_kafka     | huaweicloud_dms_kafka_instance     | 按需              | flavor_id：规格ID。flavor_id和product_id至少给出一个&lt;br/&gt;product_id：产品ID。flavor_id和product_id至少给出一个&lt;br/&gt;storage_space：存储容量                                                                                                                                                                   |
        | dcs           | huaweicloud_dcs_instance           | 包周期、按需          | -                                                                                                                                                                                                                                                                                 |
        | gaussdb_mysql | huaweicloud_gaussdb_mysql_instance | 包周期、按需          | **包周期：**&lt;br/&gt;proxy_node_number：代理节点数量&lt;br/&gt;volume_size：挂载卷的存储空间&lt;br/&gt;&lt;br/&gt;**按需：**&lt;br/&gt;proxy_node_number：代理节点数量&lt;br/&gt;volume_size：挂载卷的存储空间                                                                                                                                             |
        | vpc           | huaweicloud_vpc                    | 免费              | -                                                                                                                                                                                                                                                                                 |
        | drs           | huaweicloud_drs_job                | 按需              | -                                                                                                                                                                                                                                                                                 |
        | apig          | huaweicloud_apig_instance          | 按需              | -                                                                                                                                                                                                                                                                                 |
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateExecutionPlanPrice
        :type request: :class:`huaweicloudsdkaos.v1.EstimateExecutionPlanPriceRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.EstimateExecutionPlanPriceResponse`
        """
        return self.estimate_execution_plan_price_with_http_info(request)

    def estimate_execution_plan_price_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}/prices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EstimateExecutionPlanPriceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_execution_plan(self, request):
        """获取执行计划

        获取执行计划（GetExecutionPlan）
        
        此API用于获取指定执行计划的详细内容（即执行计划项目），用户可通过此API得知指定执行计划在执行后，资源栈中的资源会发生何种变化
        
        若执行计划状态为&#x60;CREATION_IN_PROGRESS&#x60;或&#x60;CREATION_FAILED&#x60;，则不返回执行计划项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.GetExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetExecutionPlanResponse`
        """
        return self.get_execution_plan_with_http_info(request)

    def get_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GetExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_execution_plan_metadata(self, request):
        """获取执行计划元数据

        获取执行计划元数据（GetExecutionPlanMetadata）
        
        该API可以获取指定执行计划的元数据，包括资源栈ID、资源栈名称、执行计划ID、执行计划名称、执行计划描述、执行计划的创建时间和执行时间、执行计划状态等信息。
        
        具体信息见GetExecutionPlanMetadataResponseBody。
        
        如果需要获取执行计划的具体内容，请调用GetExecutionPlan。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetExecutionPlanMetadata
        :type request: :class:`huaweicloudsdkaos.v1.GetExecutionPlanMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetExecutionPlanMetadataResponse`
        """
        return self.get_execution_plan_metadata_with_http_info(request)

    def get_execution_plan_metadata_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GetExecutionPlanMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_execution_plans(self, request):
        """列举执行计划

        列举执行计划（ListExecutionPlans）
        
        列举当前局点下用户指定资源栈下所有的执行计划
        
          * 默认按照生成时间排序，最早生成的在最前
          * 注意：目前暂时返回全量执行计划信息，即不支持分页
          * 如果指定的资源栈下没有任何执行计划，则返回空list
          * 如果指定的资源栈不存在，则返回404
        
        ListExecutionPlans返回的只有摘要信息（具体摘要信息见ListExecutionPlansResponseBody），如果用户需要详细的执行计划元数据请调用GetExecutionPlanMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExecutionPlans
        :type request: :class:`huaweicloudsdkaos.v1.ListExecutionPlansRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListExecutionPlansResponse`
        """
        return self.list_execution_plans_with_http_info(request)

    def list_execution_plans_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListExecutionPlansResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def continue_rollback_stack(self, request):
        """继续回滚资源栈

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
        return self.continue_rollback_stack_with_http_info(request)

    def continue_rollback_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'continue_rollback_stack_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/rollbacks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ContinueRollbackStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_stack(self, request):
        """创建资源栈

        CreateStack用于生成一个资源栈
        
        * 当请求中不含有模板（template）、参数（vars）等信息，将生成一个无任何资源的空资源栈，返回资源栈ID（stack_id）
        * 当请求中携带了模板（template）、参数（vars）等信息，则会同时创建并部署资源栈，返回资源栈ID（stack_id）和部署ID（deployment_id）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStack
        :type request: :class:`huaweicloudsdkaos.v1.CreateStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateStackResponse`
        """
        return self.create_stack_with_http_info(request)

    def create_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'create_stack_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_stack(self, request):
        """删除资源栈

        删除资源栈（DeleteStack）
        
        此API用于删除某个资源栈
        **请谨慎操作，删除资源栈将会删除与该资源栈相关的所有数据和资源，如：执行计划、资源栈事件、资源栈输出、资源等。**
        
        * 此API会触发删除资源栈，并以最终一致性删除所有数据，用户可以调用GetStackMetadata或ListStacks跟踪资源栈删除情况
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
        return self.delete_stack_with_http_info(request)

    def delete_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def deploy_stack(self, request):
        """部署资源栈

        部署资源栈（DeployStack）
        
        此API用于部署一个已有的资源栈
        
        * 用户可以使用此API更新模板、参数等并触发一个新的部署
        
        * 此API会直接触发部署，如果用户希望先确认部署会发生的时间，请使用执行计划，即使用CreateExecutionPlan以创建执行计划、使用GetExecutionPlan以获取执行计划
        
        * 此API为全量API，即用户每次部署都需要给予所想要使用的template、vars的全量
        
        * 当触发的部署失败时，如果资源栈开启了自动回滚，会触发自动回滚的流程，否则就会停留在部署失败时的状态
        
        * 资源栈状态是DELETION_FAILED时，用户可根据StackEvents信息修复当前模板中的错误后，重新触发部署。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeployStack
        :type request: :class:`huaweicloudsdkaos.v1.DeployStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeployStackResponse`
        """
        return self.deploy_stack_with_http_info(request)

    def deploy_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'deploy_stack_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/deployments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeployStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_stack_metadata(self, request):
        """获取资源栈元数据

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
        return self.get_stack_metadata_with_http_info(request)

    def get_stack_metadata_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GetStackMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_stack_template(self, request):
        """获取资源栈模板

        获取资源栈模板（GetStackTemplate）
        
        此API用于获取资源栈最近的一次部署使用的模板。
        
        如果获取成功，则以临时重定向形式返回模板下载链接（OBS Pre Signed地址，有效期为5分钟），大多数的客户端会进行自动重定向并下载模板；
        若未进行自动重定向，请参考HTTP的重定向规则获取模板下载链接，手动下载模板。
        
        若资源栈当前没有模板，则返回404，并提示模板不存在
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetStackTemplate
        :type request: :class:`huaweicloudsdkaos.v1.GetStackTemplateRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetStackTemplateResponse`
        """
        return self.get_stack_template_with_http_info(request)

    def get_stack_template_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GetStackTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stack_events(self, request):
        """列举资源栈事件

        列举资源栈事件（ListStackEvents）
        
        此API用于列举资源栈某一次或全部的部署事件
        
        * 若给予deployment_id，则会将deployment_id作为查询条件，返回对应某一次部署的资源栈事件；若不给予deployment_id，则返回全量的资源栈事件
        * 若给定的deployment_id对应的部署不存在，则返回404
        * 可以使用filter作为过滤器，过滤出指定事件类型（event_type）、资源类型（resource_type）、资源名称（resource_name）的资源栈事件
        * 可以使用field选择数据应返回的属性，属性事件类型（event_type）不可配置，一定会返回，可选择的属性有逝去时间（elapsed_seconds）、事件消息（event_message）、 资源ID键（resource_id_key）、资源ID值（resource_id_value）、资源键（resource_key）、资源类型（resource_type）、资源名称（resource_name）和时间戳（timestamp）
        * 事件返回将以时间降序排列
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackEvents
        :type request: :class:`huaweicloudsdkaos.v1.ListStackEventsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackEventsResponse`
        """
        return self.list_stack_events_with_http_info(request)

    def list_stack_events_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id', 'deployment_id', 'filter', 'field']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStackEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stack_outputs(self, request):
        """列举资源栈输出

        列举资源栈输出（ListStackOutputs）
        
        此API用于列举该资源栈的所有输出
        
        资源栈输出为用户在模板中定义的 output 语句块在部署结束后所产生的返回信息，用户可在部署结束后，调用此API获取其具体的输出信息
        
        当资源栈状态处于非终态（状态以&#x60;IN_PROGRESS&#x60;结尾）状态时，此API将返回空。非终态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        output为HCL官方定义的语法，其返回信息类似于常见编程语言中的返回值，详细定义请参考HCL官方的说明
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackOutputs
        :type request: :class:`huaweicloudsdkaos.v1.ListStackOutputsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackOutputsResponse`
        """
        return self.list_stack_outputs_with_http_info(request)

    def list_stack_outputs_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/outputs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStackOutputsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stack_resources(self, request):
        """列举资源栈资源

        列举资源栈资源（ListStackResources）
        
        此API用于列举资源栈中当前管理的所有资源的信息
        
        对于非终态的资源栈（状态以&#x60;IN_PROGRESS&#x60;结尾），不返回资源属性。非终态状态包括但不限于以下状态：
          * 正在部署（DEPLOYMENT_IN_PROGRESS）
          * 正在删除（DELETION_IN_PROGRESS）
          * 正在回滚（ROLLBACK_IN_PROGRESS）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackResources
        :type request: :class:`huaweicloudsdkaos.v1.ListStackResourcesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackResourcesResponse`
        """
        return self.list_stack_resources_with_http_info(request)

    def list_stack_resources_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStackResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stacks(self, request):
        """列举资源栈

        列举资源栈（ListStacks）
        
        此API用于列举当前局点下用户所有的资源栈
        
          * 默认按照生成时间排序，最早生成的在最前
          * 注意：目前暂时返回全量资源栈信息，即不支持分页
          * 如果没有任何资源栈，则返回空list
        
        ListStacks返回的只有摘要信息（具体摘要信息见ListStacksResponseBody），如果用户需要详细的资源栈元数据请调用GetStackMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStacks
        :type request: :class:`huaweicloudsdkaos.v1.ListStacksRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStacksResponse`
        """
        return self.list_stacks_with_http_info(request)

    def list_stacks_with_http_info(self, request):
        all_params = ['client_request_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStacksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_stack(self, request):
        """更新资源栈

        更新资源栈的属性，该API可以根据用户给予的信息对资源栈的属性进行更新，可以更新资源栈的“description”、“enable_deletion_protection”、\&quot;enable_auto_rollback\&quot;、\&quot;agencies\&quot;四个属性中的一个或多个
        
        该API只会更新用户给予的信息中所涉及的字段；若某字段未给予，则不会对该资源栈属性进行更新
        
        注：所有属性的更新都是覆盖式更新。即，所给予的参数将被完全覆盖至资源栈已有的属性上
        
        例如，若要新增agencies，请通过GetStackMetadata获取该资源栈原有的agencies信息，将新旧agencies信息进行整合后再调用UpdateStack
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStack
        :type request: :class:`huaweicloudsdkaos.v1.UpdateStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdateStackResponse`
        """
        return self.update_stack_with_http_info(request)

    def update_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'update_stack_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def parse_template_variables(self, request):
        """解析模板参数

        解析模板参数（ParseTemplateVariables）
        
        此API用于解析用户输入的模板中的参数（variable），将解析模板中的所有variable块并返回
        
        * 若用户传入的模板中定义了variable参数，则返回200和所有variable
        * 若用户传入的模板中没有定义variable参数，则返回200和空对象
        * 若用户请求非法或传入的模板非法，则返回400
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseTemplateVariables
        :type request: :class:`huaweicloudsdkaos.v1.ParseTemplateVariablesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ParseTemplateVariablesResponse`
        """
        return self.parse_template_variables_with_http_info(request)

    def parse_template_variables_with_http_info(self, request):
        all_params = ['client_request_id', 'parse_template_variables_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/template-analyses/variables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ParseTemplateVariablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template(self, request):
        """删除模板

        删除模板（DeleteTemplate）
        
        此API用于删除某个模板以及模板下的全部模板版本
        **请谨慎操作，删除模板将会删除模板下的所有模板版本。**
        
          * 若template_name和template_id同时存在，则模板服务会检查是否两个匹配
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkaos.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteTemplateResponse`
        """
        return self.delete_template_with_http_info(request)

    def delete_template_with_http_info(self, request):
        all_params = ['client_request_id', 'template_name', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/templates/{template_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template_version(self, request):
        """删除模板版本

        删除模板版本（DeleteTemplateVersion）
        
        此API用于删除某个模板版本
        
          * 若template_name和template_id同时存在，则模板服务会检查是否两个匹配，否则返回400
          * 若模板下只存在唯一模板版本，此模板版本将无法被删除，如果需要删除此模板版本，请调用DeleteTemplate。模板服务不允许存在没有模板版本的模板
        
        **请谨慎操作**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplateVersion
        :type request: :class:`huaweicloudsdkaos.v1.DeleteTemplateVersionRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteTemplateVersionResponse`
        """
        return self.delete_template_version_with_http_info(request)

    def delete_template_version_with_http_info(self, request):
        all_params = ['client_request_id', 'template_name', 'version_id', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/templates/{template_name}/versions/{version_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTemplateVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_templates(self, request):
        """列举模板

        列举模板（ListTemplates）
        
        此API用于列举当前局点下用户所有的模板
        
          * 默认按照生成时间排序，最早生成的模板排列在最前面
          * 注意：目前返回全量模板信息，即不支持分页
          * 如果没有任何模板，则返回空list
          * 若用户需要详细的模板版本信息，请调用ListTemplateVersions
        
        ListTemplates返回的信息只包含模板摘要信息（具体摘要信息见ListTemplatesResponseBody），若用户需要详细的某个模板信息，请调用ShowTemplateMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkaos.v1.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListTemplatesResponse`
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
        all_params = ['client_request_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_template_metadata(self, request):
        """获取模板元数据

        获取模板元数据（ShowTemplateMetadata）
        
        此API用于获取当前模板的元数据信息
        
        具体信息见ShowTemplateMetadataResponseBody，若想查看模板下全部模板版本，请调用ListTemplateVersions。
        
          * 若template_name和template_id同时存在，则模板服务会检查是否两个匹配
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowTemplateMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowTemplateMetadataResponse`
        """
        return self.show_template_metadata_with_http_info(request)

    def show_template_metadata_with_http_info(self, request):
        all_params = ['client_request_id', 'template_name', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/templates/{template_name}/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTemplateMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_template_version_content(self, request):
        """获取模板版本内容

        获取模板版本内容（ShowTemplateVersionContent）
        
        此API用于获取用户的模板版本内容
        
          * 若template_name和template_id同时存在，则模板服务会检查是否两个匹配，否则返回400
          * 此api会以临时重定向形式返回模板内容的下载链接，用户通过下载获取模板版本内容（OBS Pre Signed地址，有效期为5分钟）
        
        ShowTemplateVersionContent返回的信息只包含模板版本内容，若想知道模板版本的元数据，请调用ShowTemplateVersionMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateVersionContent
        :type request: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionContentRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionContentResponse`
        """
        return self.show_template_version_content_with_http_info(request)

    def show_template_version_content_with_http_info(self, request):
        all_params = ['client_request_id', 'template_name', 'version_id', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/templates/{template_name}/versions/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTemplateVersionContentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_template_version_metadata(self, request):
        """获取模板版本元数据

        获取模板版本元数据（ShowTemplateVersionMetadata）
        
        此API用于展示某一版本模板的元数据
        
        ShowTemplateVersionMetadata返回的信息只包含模板版本元数据信息（具体摘要信息见ShowTemplateVersionMetadataResponseBody），若用户需要了解模板版本内容，请调用ShowTemplateVersionContent。
        
          * 若template_name和template_id同时存在，则模板服务会检查是否两个匹配，否则返回400
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateVersionMetadata
        :type request: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ShowTemplateVersionMetadataResponse`
        """
        return self.show_template_version_metadata_with_http_info(request)

    def show_template_version_metadata_with_http_info(self, request):
        all_params = ['client_request_id', 'template_name', 'version_id', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/templates/{template_name}/versions/{version_id}/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTemplateVersionMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_template_metadata(self, request):
        """更新模板元数据

        更新模板元数据（UpdateTemplateMetadata）
        
        此API用于更新模板元数据
        
        * 此api只支持更新模板描述
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplateMetadata
        :type request: :class:`huaweicloudsdkaos.v1.UpdateTemplateMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.UpdateTemplateMetadataResponse`
        """
        return self.update_template_metadata_with_http_info(request)

    def update_template_metadata_with_http_info(self, request):
        all_params = ['client_request_id', 'template_name', 'update_template_metadata_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/templates/{template_name}/metadata',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTemplateMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
