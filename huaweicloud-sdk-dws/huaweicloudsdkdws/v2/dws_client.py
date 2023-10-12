# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DwsClient(Client):
    def __init__(self):
        super(DwsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdws.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DwsClient":
            raise TypeError("client type error, support client type is DwsClient")

        return ClientBuilder(clazz)

    def add_workload_queue(self, request):
        """添加工作负载队列

        添加工作负载队列
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddWorkloadQueue
        :type request: :class:`huaweicloudsdkdws.v2.AddWorkloadQueueRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.AddWorkloadQueueResponse`
        """
        return self._add_workload_queue_with_http_info(request)

    def _add_workload_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/workload/queues',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddWorkloadQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_eip(self, request):
        """集群绑定EIP

        集群绑定Eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateEip
        :type request: :class:`huaweicloudsdkdws.v2.AssociateEipRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.AssociateEipResponse`
        """
        return self._associate_eip_with_http_info(request)

    def _associate_eip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'eip_id' in local_var_params:
            path_params['eip_id'] = local_var_params['eip_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/eips/{eip_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_elb(self, request):
        """集群绑定ELB

        集群绑定Elb接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateElb
        :type request: :class:`huaweicloudsdkdws.v2.AssociateElbRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.AssociateElbResponse`
        """
        return self._associate_elb_with_http_info(request)

    def _associate_elb_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'elb_id' in local_var_params:
            path_params['elb_id'] = local_var_params['elb_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/elbs/{elb_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateElbResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_cluster_cn(self, request):
        """批量增加CN节点

        当用户集群创建后，实际需要的CN数量会随着业务需求而发生变化，因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。
        - 增删CN节点过程中不允许执行其他运维操作。
        - 增删CN节点过程中需要停止业务操作，建议在业务低峰期或业务中断情况下进行操作。
        - 增删CN节点时发生故障且回滚失败，需要用户登录后台进行处理，处理方案请参见《故障排除》中的“集群使用&gt;增删CN回滚失败”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateClusterCn
        :type request: :class:`huaweicloudsdkdws.v2.BatchCreateClusterCnRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchCreateClusterCnResponse`
        """
        return self._batch_create_cluster_cn_with_http_info(request)

    def _batch_create_cluster_cn_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/cns/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateClusterCnResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_resource_tag(self, request):
        """批量添加标签

        为指定集群批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateResourceTag
        :type request: :class:`huaweicloudsdkdws.v2.BatchCreateResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchCreateResourceTagResponse`
        """
        return self._batch_create_resource_tag_with_http_info(request)

    def _batch_create_resource_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/tags/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_cluster_cn(self, request):
        """批量删除CN节点

        当用户集群创建后，实际需要的CN数量会随着业务需求而发生变化，因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。
        - 增删CN节点过程中不允许执行其他运维操作。
        - 增删CN节点过程中需要停止业务操作，建议在业务低峰期或业务中断情况下进行操作。
        - 增删CN节点时发生故障且回滚失败，需要用户登录后台进行处理，处理方案请参见《故障排除》中的“集群使用&gt;增删CN回滚失败”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteClusterCn
        :type request: :class:`huaweicloudsdkdws.v2.BatchDeleteClusterCnRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchDeleteClusterCnResponse`
        """
        return self._batch_delete_cluster_cn_with_http_info(request)

    def _batch_delete_cluster_cn_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/cns/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteClusterCnResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_resource_tag(self, request):
        """批量删除标签

        为指定集群批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResourceTag
        :type request: :class:`huaweicloudsdkdws.v2.BatchDeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchDeleteResourceTagResponse`
        """
        return self._batch_delete_resource_tag_with_http_info(request)

    def _batch_delete_resource_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/tags/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_readonly_cluster(self, request):
        """解除只读

        当集群进入只读状态时，无法进行数据库相关操作，用户可以在管理控制台解除集群的只读状态。触发只读状态可能是由于磁盘使用率过高，因此需要对集群数据进行清理或扩容。
        - 解除只读支持1.7.2及以上版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelReadonlyCluster
        :type request: :class:`huaweicloudsdkdws.v2.CancelReadonlyClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CancelReadonlyClusterResponse`
        """
        return self._cancel_readonly_cluster_with_http_info(request)

    def _cancel_readonly_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/cancel-readonly',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelReadonlyClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_cluster(self, request):
        """创建集群前检查

        创建集群前预检查
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckCluster
        :type request: :class:`huaweicloudsdkdws.v2.CheckClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CheckClusterResponse`
        """
        return self._check_cluster_with_http_info(request)

    def _check_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cluster-precheck',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_disaster_name(self, request):
        """检查容灾名称

        检查容灾名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDisasterName
        :type request: :class:`huaweicloudsdkdws.v2.CheckDisasterNameRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CheckDisasterNameResponse`
        """
        return self._check_disaster_name_with_http_info(request)

    def _check_disaster_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dr_name' in local_var_params:
            query_params.append(('dr_name', local_var_params['dr_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'standby_region' in local_var_params:
            query_params.append(('standby_region', local_var_params['standby_region']))
        if 'standby_project_id' in local_var_params:
            query_params.append(('standby_project_id', local_var_params['standby_project_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/check-name',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckDisasterNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_snapshot(self, request):
        """复制快照

        该接口用于复制一个自动快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopySnapshot
        :type request: :class:`huaweicloudsdkdws.v2.CopySnapshotRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CopySnapshotResponse`
        """
        return self._copy_snapshot_with_http_info(request)

    def _copy_snapshot_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/snapshots/{snapshot_id}/linked-copy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopySnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alarm_sub(self, request):
        """创建告警订阅

        创建告警订阅
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlarmSub
        :type request: :class:`huaweicloudsdkdws.v2.CreateAlarmSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateAlarmSubResponse`
        """
        return self._create_alarm_sub_with_http_info(request)

    def _create_alarm_sub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-subs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlarmSubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cluster(self, request):
        """创建集群

        该接口用于创建集群。
        集群必须要运行在VPC之内，创建集群前，您需要先创建VPC，并获取VPC和子网的id。
        该接口为异步接口，创建集群需要10～15分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterResponse`
        """
        return self._create_cluster_with_http_info(request)

    def _create_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cluster_dns(self, request):
        """申请域名

        为指定集群申请域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterDns
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterDnsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterDnsResponse`
        """
        return self._create_cluster_dns_with_http_info(request)

    def _create_cluster_dns_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/dns',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateClusterDnsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cluster_v2(self, request):
        """V2创建集群

        该接口用于创建集群。
        集群必须要运行在VPC之内，创建集群前，您需要先创建VPC，并获取VPC和子网的id。
        该接口为异步接口，创建集群需要10～15分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterV2
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterV2Request`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterV2Response`
        """
        return self._create_cluster_v2_with_http_info(request)

    def _create_cluster_v2_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateClusterV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cluster_workload(self, request):
        """设置资源管理

        设置资源管理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterWorkload
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterWorkloadRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterWorkloadResponse`
        """
        return self._create_cluster_workload_with_http_info(request)

    def _create_cluster_workload_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/workload',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateClusterWorkloadResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_data_source(self, request):
        """创建数据源

        该接口用于创建一个数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataSource
        :type request: :class:`huaweicloudsdkdws.v2.CreateDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateDataSourceResponse`
        """
        return self._create_data_source_with_http_info(request)

    def _create_data_source_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDataSourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_disaster_recovery(self, request):
        """创建容灾

        创建容灾
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.CreateDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateDisasterRecoveryResponse`
        """
        return self._create_disaster_recovery_with_http_info(request)

    def _create_disaster_recovery_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recoveries',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDisasterRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_event_sub(self, request):
        """创建订阅事件

        添加订阅的事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEventSub
        :type request: :class:`huaweicloudsdkdws.v2.CreateEventSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateEventSubResponse`
        """
        return self._create_event_sub_with_http_info(request)

    def _create_event_sub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/event-subs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEventSubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_snapshot(self, request):
        """创建快照

        该接口用于为指定集群创建快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSnapshot
        :type request: :class:`huaweicloudsdkdws.v2.CreateSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateSnapshotResponse`
        """
        return self._create_snapshot_with_http_info(request)

    def _create_snapshot_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/snapshots',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_snapshot_policy(self, request):
        """添加快照策略

        该接口用于设置快照策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSnapshotPolicy
        :type request: :class:`huaweicloudsdkdws.v2.CreateSnapshotPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateSnapshotPolicyResponse`
        """
        return self._create_snapshot_policy_with_http_info(request)

    def _create_snapshot_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/snapshot-policies',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSnapshotPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workload_plan(self, request):
        """添加工作负载计划

        添加工作负载计划
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkloadPlan
        :type request: :class:`huaweicloudsdkdws.v2.CreateWorkloadPlanRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateWorkloadPlanResponse`
        """
        return self._create_workload_plan_with_http_info(request)

    def _create_workload_plan_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/workload/plans',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWorkloadPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alarm_sub(self, request):
        """删除告警订阅

        删除订阅的告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlarmSub
        :type request: :class:`huaweicloudsdkdws.v2.DeleteAlarmSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteAlarmSubResponse`
        """
        return self._delete_alarm_sub_with_http_info(request)

    def _delete_alarm_sub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_sub_id' in local_var_params:
            path_params['alarm_sub_id'] = local_var_params['alarm_sub_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-subs/{alarm_sub_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlarmSubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cluster(self, request):
        """删除集群

        此接口用于删除集群。集群删除后将释放此集群的所有资源，包括客户数据。为了安全起见，请在删除集群前为这个集群创建快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkdws.v2.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteClusterResponse`
        """
        return self._delete_cluster_with_http_info(request)

    def _delete_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cluster_dns(self, request):
        """删除集群域名

        删除指定集群域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClusterDns
        :type request: :class:`huaweicloudsdkdws.v2.DeleteClusterDnsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteClusterDnsResponse`
        """
        return self._delete_cluster_dns_with_http_info(request)

    def _delete_cluster_dns_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/dns',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteClusterDnsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_data_source(self, request):
        """删除数据源

        该接口用于删除一个数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataSource
        :type request: :class:`huaweicloudsdkdws.v2.DeleteDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteDataSourceResponse`
        """
        return self._delete_data_source_with_http_info(request)

    def _delete_data_source_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'ext_data_source_id' in local_var_params:
            path_params['ext_data_source_id'] = local_var_params['ext_data_source_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources/{ext_data_source_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDataSourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_disaster_recovery(self, request):
        """删除容灾

        删除容灾。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.DeleteDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteDisasterRecoveryResponse`
        """
        return self._delete_disaster_recovery_with_http_info(request)

    def _delete_disaster_recovery_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDisasterRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_event_sub(self, request):
        """删除订阅事件

        删除订阅的事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEventSub
        :type request: :class:`huaweicloudsdkdws.v2.DeleteEventSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteEventSubResponse`
        """
        return self._delete_event_sub_with_http_info(request)

    def _delete_event_sub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_sub_id' in local_var_params:
            path_params['event_sub_id'] = local_var_params['event_sub_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/event-subs/{event_sub_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEventSubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_snapshot(self, request):
        """删除快照

        该接口用于删除一个指定手动快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSnapshot
        :type request: :class:`huaweicloudsdkdws.v2.DeleteSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteSnapshotResponse`
        """
        return self._delete_snapshot_with_http_info(request)

    def _delete_snapshot_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/snapshots/{snapshot_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_snapshot_policy(self, request):
        """删除快照策略

        该接口用于删除一个快照策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSnapshotPolicy
        :type request: :class:`huaweicloudsdkdws.v2.DeleteSnapshotPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteSnapshotPolicyResponse`
        """
        return self._delete_snapshot_policy_with_http_info(request)

    def _delete_snapshot_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/snapshot-policies/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSnapshotPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_workload_queue(self, request):
        """删除工作负载队列

        该接口用于删除工作负载队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkloadQueue
        :type request: :class:`huaweicloudsdkdws.v2.DeleteWorkloadQueueRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteWorkloadQueueResponse`
        """
        return self._delete_workload_queue_with_http_info(request)

    def _delete_workload_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'logical_cluster_name' in local_var_params:
            query_params.append(('logical_cluster_name', local_var_params['logical_cluster_name']))
        if 'workload_queue_name' in local_var_params:
            query_params.append(('workload_queue_name', local_var_params['workload_queue_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/workload/queues',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteWorkloadQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_eip(self, request):
        """集群解绑EIP

        集群解绑Eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateEip
        :type request: :class:`huaweicloudsdkdws.v2.DisassociateEipRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DisassociateEipResponse`
        """
        return self._disassociate_eip_with_http_info(request)

    def _disassociate_eip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'eip_id' in local_var_params:
            path_params['eip_id'] = local_var_params['eip_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/eips/{eip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_elb(self, request):
        """集群解绑ELB

        集群解绑Elb接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateElb
        :type request: :class:`huaweicloudsdkdws.v2.DisassociateElbRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DisassociateElbResponse`
        """
        return self._disassociate_elb_with_http_info(request)

    def _disassociate_elb_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'elb_id' in local_var_params:
            path_params['elb_id'] = local_var_params['elb_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/elbs/{elb_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateElbResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_database_om_user_action(self, request):
        """执行运维用户操作

        进行数据库运维账户操作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteDatabaseOmUserAction
        :type request: :class:`huaweicloudsdkdws.v2.ExecuteDatabaseOmUserActionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ExecuteDatabaseOmUserActionResponse`
        """
        return self._execute_database_om_user_action_with_http_info(request)

    def _execute_database_om_user_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/om-user/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteDatabaseOmUserActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_redistribution_cluster(self, request):
        """下发重分布

        下发重分布
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteRedistributionCluster
        :type request: :class:`huaweicloudsdkdws.v2.ExecuteRedistributionClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ExecuteRedistributionClusterResponse`
        """
        return self._execute_redistribution_cluster_with_http_info(request)

    def _execute_redistribution_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/redistribution',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteRedistributionClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_instance_storage(self, request):
        """磁盘扩容

        随着客户业务的发展，磁盘空间往往最先出现资源瓶颈，在其他资源尚且充足的情况下，通过磁盘扩容可快速缓解存储资源瓶颈现象，操作过程中无需暂停业务，并且不会造成CPU、内存等资源浪费。
        - 磁盘扩容功能仅8.1.1.203及以上版本支持，并且创建集群规格需要为云数仓SSD云盘或实时数仓类型。
        - 按需+折扣套餐包消费模式下，存储扩容后超出折扣套餐包部分将按需收费。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandInstanceStorage
        :type request: :class:`huaweicloudsdkdws.v2.ExpandInstanceStorageRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ExpandInstanceStorageResponse`
        """
        return self._expand_instance_storage_with_http_info(request)

    def _expand_instance_storage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/expand-instance-storage',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandInstanceStorageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_configs(self, request):
        """查询告警配置

        查询告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmConfigs
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmConfigsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmConfigsResponse`
        """
        return self._list_alarm_configs_with_http_info(request)

    def _list_alarm_configs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_detail(self, request):
        """查询告警详情列表

        查询告警详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmDetail
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmDetailRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmDetailResponse`
        """
        return self._list_alarm_detail_with_http_info(request)

    def _list_alarm_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_statistic(self, request):
        """查询告警统计列表

        查询告警统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmStatistic
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmStatisticRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmStatisticResponse`
        """
        return self._list_alarm_statistic_with_http_info(request)

    def _list_alarm_statistic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_subs(self, request):
        """查询告警订阅列表

        查询订阅告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmSubs
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmSubsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmSubsResponse`
        """
        return self._list_alarm_subs_with_http_info(request)

    def _list_alarm_subs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-subs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmSubsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_log(self, request):
        """查询日志记录

        查询审计日志记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditLog
        :type request: :class:`huaweicloudsdkdws.v2.ListAuditLogRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAuditLogResponse`
        """
        return self._list_audit_log_with_http_info(request)

    def _list_audit_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/audit-log-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_availability_zones(self, request):
        """查询可用区列表

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkdws.v2.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAvailabilityZonesResponse`
        """
        return self._list_availability_zones_with_http_info(request)

    def _list_availability_zones_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/availability-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_available_disaster_clusters(self, request):
        """查询可用容灾集群列表

        查询可用容灾集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableDisasterClusters
        :type request: :class:`huaweicloudsdkdws.v2.ListAvailableDisasterClustersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAvailableDisasterClustersResponse`
        """
        return self._list_available_disaster_clusters_with_http_info(request)

    def _list_available_disaster_clusters_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'primary_cluster_id' in local_var_params:
            query_params.append(('primary_cluster_id', local_var_params['primary_cluster_id']))
        if 'primary_spec_id' in local_var_params:
            query_params.append(('primary_spec_id', local_var_params['primary_spec_id']))
        if 'primary_cluster_dn_num' in local_var_params:
            query_params.append(('primary_cluster_dn_num', local_var_params['primary_cluster_dn_num']))
        if 'standby_region' in local_var_params:
            query_params.append(('standby_region', local_var_params['standby_region']))
        if 'standby_project_id' in local_var_params:
            query_params.append(('standby_project_id', local_var_params['standby_project_id']))
        if 'standby_az_code' in local_var_params:
            query_params.append(('standby_az_code', local_var_params['standby_az_code']))
        if 'dr_type' in local_var_params:
            query_params.append(('dr_type', local_var_params['dr_type']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'datastore_version' in local_var_params:
            query_params.append(('datastore_version', local_var_params['datastore_version']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery-clusters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailableDisasterClustersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_cn(self, request):
        """查询集群CN节点

        查询集群的CN节点列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterCn
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterCnRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterCnResponse`
        """
        return self._list_cluster_cn_with_http_info(request)

    def _list_cluster_cn_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/cns',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterCnResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_configurations(self, request):
        """查询集群参数组

        查询集群所关联的参数组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterConfigurations
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsResponse`
        """
        return self._list_cluster_configurations_with_http_info(request)

    def _list_cluster_configurations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/configurations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_configurations_parameter(self, request):
        """查询集群参数配置

        查询集群所关联的参数组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterConfigurationsParameter
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsParameterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsParameterResponse`
        """
        return self._list_cluster_configurations_parameter_with_http_info(request)

    def _list_cluster_configurations_parameter_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/configurations/{configuration_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterConfigurationsParameterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_details(self, request):
        """查询集群详情

        该接口用于查询集群详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterDetails
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterDetailsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterDetailsResponse`
        """
        return self._list_cluster_details_with_http_info(request)

    def _list_cluster_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_scale_in_numbers(self, request):
        """查询合适的缩容数

        查询合适的缩容数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterScaleInNumbers
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterScaleInNumbersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterScaleInNumbersResponse`
        """
        return self._list_cluster_scale_in_numbers_with_http_info(request)

    def _list_cluster_scale_in_numbers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/shrink-numbers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterScaleInNumbersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_snapshots(self, request):
        """查询集群快照列表

        该接口用于查询集群快照列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterSnapshots
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterSnapshotsResponse`
        """
        return self._list_cluster_snapshots_with_http_info(request)

    def _list_cluster_snapshots_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/snapshots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterSnapshotsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_tags(self, request):
        """查询集群标签

        查询指定集群的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterTags
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterTagsResponse`
        """
        return self._list_cluster_tags_with_http_info(request)

    def _list_cluster_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_workload(self, request):
        """查询资源管理

        查询资管管理开关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterWorkload
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterWorkloadRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterWorkloadResponse`
        """
        return self._list_cluster_workload_with_http_info(request)

    def _list_cluster_workload_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/workload',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterWorkloadResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_clusters(self, request):
        """查询集群列表

        该接口用于查询并显示集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkdws.v2.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClustersResponse`
        """
        return self._list_clusters_with_http_info(request)

    def _list_clusters_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClustersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configurations_audit_records(self, request):
        """查询参数修改审计记录

        查询参数修改审计记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurationsAuditRecords
        :type request: :class:`huaweicloudsdkdws.v2.ListConfigurationsAuditRecordsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListConfigurationsAuditRecordsResponse`
        """
        return self._list_configurations_audit_records_with_http_info(request)

    def _list_configurations_audit_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'action_time' in local_var_params:
            query_params.append(('action_time', local_var_params['action_time']))
        if 'filter_by' in local_var_params:
            query_params.append(('filter_by', local_var_params['filter_by']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/configurations/audit-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigurationsAuditRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data_source(self, request):
        """查询数据源

        该接口用于查询数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataSource
        :type request: :class:`huaweicloudsdkdws.v2.ListDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDataSourceResponse`
        """
        return self._list_data_source_with_http_info(request)

    def _list_data_source_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataSourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_users(self, request):
        """查询所有数据库用户/角色

        查询所有数据库用户/角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseUsers
        :type request: :class:`huaweicloudsdkdws.v2.ListDatabaseUsersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDatabaseUsersResponse`
        """
        return self._list_database_users_with_http_info(request)

    def _list_database_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatabaseUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_disaster_recover(self, request):
        """查询容灾列表

        查询容灾列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDisasterRecover
        :type request: :class:`huaweicloudsdkdws.v2.ListDisasterRecoverRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDisasterRecoverResponse`
        """
        return self._list_disaster_recover_with_http_info(request)

    def _list_disaster_recover_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recoveries',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDisasterRecoverResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dss_pools(self, request):
        """查询专属分布式存储池列表

        获取专属分布式存储池列表，只包括用户开通的SSD专属资源池信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDssPools
        :type request: :class:`huaweicloudsdkdws.v2.ListDssPoolsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDssPoolsResponse`
        """
        return self._list_dss_pools_with_http_info(request)

    def _list_dss_pools_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dss-pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDssPoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_elbs(self, request):
        """获取集群可绑定的ELB列表

        查询集群可以关联的Elb列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListElbs
        :type request: :class:`huaweicloudsdkdws.v2.ListElbsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListElbsResponse`
        """
        return self._list_elbs_with_http_info(request)

    def _list_elbs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/elbs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListElbsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_event_specs(self, request):
        """查询事件配置

        查询事件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEventSpecs
        :type request: :class:`huaweicloudsdkdws.v2.ListEventSpecsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListEventSpecsResponse`
        """
        return self._list_event_specs_with_http_info(request)

    def _list_event_specs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_name' in local_var_params:
            query_params.append(('spec_name', local_var_params['spec_name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'source_type' in local_var_params:
            query_params.append(('source_type', local_var_params['source_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/event-specs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEventSpecsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_event_subs(self, request):
        """查询订阅事件

        查询订阅的事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEventSubs
        :type request: :class:`huaweicloudsdkdws.v2.ListEventSubsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListEventSubsResponse`
        """
        return self._list_event_subs_with_http_info(request)

    def _list_event_subs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/event-subs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEventSubsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_events(self, request):
        """查询事件列表

        查询事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkdws.v2.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListEventsResponse`
        """
        return self._list_events_with_http_info(request)

    def _list_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_disk(self, request):
        """openApi查询磁盘信息

        openApi查询磁盘信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostDisk
        :type request: :class:`huaweicloudsdkdws.v2.ListHostDiskRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListHostDiskResponse`
        """
        return self._list_host_disk_with_http_info(request)

    def _list_host_disk_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dms/disk',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostDiskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_net(self, request):
        """openapi获取网卡状态

        openapi获取网卡状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostNet
        :type request: :class:`huaweicloudsdkdws.v2.ListHostNetRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListHostNetResponse`
        """
        return self._list_host_net_with_http_info(request)

    def _list_host_net_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dms/net',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostNetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_overview(self, request):
        """openApi查询主机概览

        openApi查询主机概览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostOverview
        :type request: :class:`huaweicloudsdkdws.v2.ListHostOverviewRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListHostOverviewResponse`
        """
        return self._list_host_overview_with_http_info(request)

    def _list_host_overview_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dms/host-overview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostOverviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_job_details(self, request):
        """查询job进度

        查询job进度信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobDetails
        :type request: :class:`huaweicloudsdkdws.v2.ListJobDetailsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListJobDetailsResponse`
        """
        return self._list_job_details_with_http_info(request)

    def _list_job_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/job/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_monitor_indicator_data(self, request):
        """openApi查询历史监控数据

        openApi查询历史监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMonitorIndicatorData
        :type request: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorDataRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorDataResponse`
        """
        return self._list_monitor_indicator_data_with_http_info(request)

    def _list_monitor_indicator_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'function' in local_var_params:
            query_params.append(('function', local_var_params['function']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'indicator_name' in local_var_params:
            query_params.append(('indicator_name', local_var_params['indicator_name']))
        if 'dim0' in local_var_params:
            query_params.append(('dim0', local_var_params['dim0']))
        if 'dim1' in local_var_params:
            query_params.append(('dim1', local_var_params['dim1']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dms/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMonitorIndicatorDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_monitor_indicators(self, request):
        """openApi查询性能监控指标

        openApi查询性能监控指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMonitorIndicators
        :type request: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorsResponse`
        """
        return self._list_monitor_indicators_with_http_info(request)

    def _list_monitor_indicators_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dms/metric-data/indicators',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMonitorIndicatorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_node_types(self, request):
        """查询节点类型

        该接口用于查询所有GaussDB(DWS)服务支持的节点类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNodeTypes
        :type request: :class:`huaweicloudsdkdws.v2.ListNodeTypesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListNodeTypesResponse`
        """
        return self._list_node_types_with_http_info(request)

    def _list_node_types_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/node-types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNodeTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas(self, request):
        """查询配额

        查询单租户在GaussDB(DWS)服务下的配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkdws.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListQuotasResponse`
        """
        return self._list_quotas_with_http_info(request)

    def _list_quotas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_snapshot_details(self, request):
        """查询快照详情

        该接口用于使用快照ID查询快照详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshotDetails
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotDetailsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotDetailsResponse`
        """
        return self._list_snapshot_details_with_http_info(request)

    def _list_snapshot_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/snapshots/{snapshot_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSnapshotDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_snapshot_policy(self, request):
        """查询快照策略

        查询快照策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshotPolicy
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotPolicyResponse`
        """
        return self._list_snapshot_policy_with_http_info(request)

    def _list_snapshot_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/snapshot-policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSnapshotPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_snapshot_statistics(self, request):
        """快照统计信息

        快照统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshotStatistics
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotStatisticsResponse`
        """
        return self._list_snapshot_statistics_with_http_info(request)

    def _list_snapshot_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/snapshots/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSnapshotStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_snapshots(self, request):
        """查询快照列表

        该接口用于查询快照列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshots
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotsResponse`
        """
        return self._list_snapshots_with_http_info(request)

    def _list_snapshots_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/snapshots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSnapshotsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_statistics(self, request):
        """查询资源统计信息列表

        查询当前可用资源数量，其中包括“可用集群和总集群（个）”、“可用节点和总节点（个）”、“总容量（GB）”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStatistics
        :type request: :class:`huaweicloudsdkdws.v2.ListStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListStatisticsResponse`
        """
        return self._list_statistics_with_http_info(request)

    def _list_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags(self, request):
        """查询项目标签

        查询项目标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdws.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListTagsResponse`
        """
        return self._list_tags_with_http_info(request)

    def _list_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workload_queue(self, request):
        """查询工作负载队列

        查询工作负载队列
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkloadQueue
        :type request: :class:`huaweicloudsdkdws.v2.ListWorkloadQueueRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListWorkloadQueueResponse`
        """
        return self._list_workload_queue_with_http_info(request)

    def _list_workload_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/workload/queues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkloadQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def pause_disaster_recovery(self, request):
        """停止容灾

        停止容灾
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PauseDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.PauseDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.PauseDisasterRecoveryResponse`
        """
        return self._pause_disaster_recovery_with_http_info(request)

    def _pause_disaster_recovery_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/pause',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PauseDisasterRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_password(self, request):
        """重置密码

        此接口用于重置集群管理员密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkdws.v2.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ResetPasswordResponse`
        """
        return self._reset_password_with_http_info(request)

    def _reset_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/reset-password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_cluster(self, request):
        """扩容集群调整集群大小

        此接口用于扩容集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeCluster
        :type request: :class:`huaweicloudsdkdws.v2.ResizeClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ResizeClusterResponse`
        """
        return self._resize_cluster_with_http_info(request)

    def _resize_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_cluster(self, request):
        """重启集群

        此接口用于重启集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCluster
        :type request: :class:`huaweicloudsdkdws.v2.RestartClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestartClusterResponse`
        """
        return self._restart_cluster_with_http_info(request)

    def _restart_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_cluster(self, request):
        """恢复集群

        该接口用于使用快照恢复集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreCluster
        :type request: :class:`huaweicloudsdkdws.v2.RestoreClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestoreClusterResponse`
        """
        return self._restore_cluster_with_http_info(request)

    def _restore_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/snapshots/{snapshot_id}/actions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_disaster(self, request):
        """恢复容灾

        恢复容灾
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreDisaster
        :type request: :class:`huaweicloudsdkdws.v2.RestoreDisasterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestoreDisasterResponse`
        """
        return self._restore_disaster_with_http_info(request)

    def _restore_disaster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/recovery',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreDisasterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def save_cluster_description_info(self, request):
        """保存集群描述信息

        保存集群描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveClusterDescriptionInfo
        :type request: :class:`huaweicloudsdkdws.v2.SaveClusterDescriptionInfoRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SaveClusterDescriptionInfoResponse`
        """
        return self._save_cluster_description_info_with_http_info(request)

    def _save_cluster_description_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/description',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SaveClusterDescriptionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cluster_redistribution(self, request):
        """查询重分布详情

        查询重分布详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterRedistribution
        :type request: :class:`huaweicloudsdkdws.v2.ShowClusterRedistributionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowClusterRedistributionResponse`
        """
        return self._show_cluster_redistribution_with_http_info(request)

    def _show_cluster_redistribution_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/redistribution',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowClusterRedistributionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_database_authority(self, request):
        """查询数据库对象权限

        查询数据库对象权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatabaseAuthority
        :type request: :class:`huaweicloudsdkdws.v2.ShowDatabaseAuthorityRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDatabaseAuthorityResponse`
        """
        return self._show_database_authority_with_http_info(request)

    def _show_database_authority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'schema' in local_var_params:
            query_params.append(('schema', local_var_params['schema']))
        if 'table' in local_var_params:
            query_params.append(('table', local_var_params['table']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/authority',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDatabaseAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_database_om_user_status(self, request):
        """获得集群运维账户状态

        获得数据库运维账户状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatabaseOmUserStatus
        :type request: :class:`huaweicloudsdkdws.v2.ShowDatabaseOmUserStatusRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDatabaseOmUserStatusResponse`
        """
        return self._show_database_om_user_status_with_http_info(request)

    def _show_database_om_user_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/om-user/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDatabaseOmUserStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_database_user(self, request):
        """查询指定用户信息

        查询指定用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatabaseUser
        :type request: :class:`huaweicloudsdkdws.v2.ShowDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDatabaseUserResponse`
        """
        return self._show_database_user_with_http_info(request)

    def _show_database_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/users/{name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDatabaseUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_disaster_detail(self, request):
        """查询容灾详情

        查询容灾详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDisasterDetail
        :type request: :class:`huaweicloudsdkdws.v2.ShowDisasterDetailRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDisasterDetailResponse`
        """
        return self._show_disaster_detail_with_http_info(request)

    def _show_disaster_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDisasterDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_disaster_progress(self, request):
        """容灾-查询容灾进度详情

        容灾-查询容灾进度详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDisasterProgress
        :type request: :class:`huaweicloudsdkdws.v2.ShowDisasterProgressRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDisasterProgressResponse`
        """
        return self._show_disaster_progress_with_http_info(request)

    def _show_disaster_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/disaster-recovery/{disaster_recovery_id}/show-progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDisasterProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance(self, request):
        """查询单个实例

        查询单个实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkdws.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowInstanceResponse`
        """
        return self._show_instance_with_http_info(request)

    def _show_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def shrink_cluster(self, request):
        """集群缩容

        该接口用于缩容集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShrinkCluster
        :type request: :class:`huaweicloudsdkdws.v2.ShrinkClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShrinkClusterResponse`
        """
        return self._shrink_cluster_with_http_info(request)

    def _shrink_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/cluster-shrink',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShrinkClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_disaster_recovery(self, request):
        """启动容灾

        启动容灾
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.StartDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.StartDisasterRecoveryResponse`
        """
        return self._start_disaster_recovery_with_http_info(request)

    def _start_disaster_recovery_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartDisasterRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_failover_disaster(self, request):
        """容灾异常切换

        容灾-异常切换
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchFailoverDisaster
        :type request: :class:`huaweicloudsdkdws.v2.SwitchFailoverDisasterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SwitchFailoverDisasterResponse`
        """
        return self._switch_failover_disaster_with_http_info(request)

    def _switch_failover_disaster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/failover',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchFailoverDisasterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_over_cluster(self, request):
        """主备恢复

        当集群状态为“非均衡”时会出现某些节点主实例增多，从而负载压力较大。这种情况下集群状态是正常的，但整体性能要低于均衡状态。可进行集群主备恢复操作将集群状态切换为“可用“状态。
        - 集群主备恢复仅8.1.1.202及以上版本支持。
        - 集群主备恢复将会短暂中断业务，中断时间根据用户自身业务量所决定，建议用户在业务低峰期执行此操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchOverCluster
        :type request: :class:`huaweicloudsdkdws.v2.SwitchOverClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SwitchOverClusterResponse`
        """
        return self._switch_over_cluster_with_http_info(request)

    def _switch_over_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/switchover',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchOverClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switchover_disaster_recovery(self, request):
        """灾备切换

        容灾-灾备切换
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchoverDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.SwitchoverDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SwitchoverDisasterRecoveryResponse`
        """
        return self._switchover_disaster_recovery_with_http_info(request)

    def _switchover_disaster_recovery_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/switchover',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchoverDisasterRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def sync_iam_users(self, request):
        """同步IAM用户到数据库

        同步IAM用户到数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SyncIamUsers
        :type request: :class:`huaweicloudsdkdws.v2.SyncIamUsersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SyncIamUsersResponse`
        """
        return self._sync_iam_users_with_http_info(request)

    def _sync_iam_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/sync-iam-user',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SyncIamUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_sub(self, request):
        """更新告警订阅

        更新订阅的告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmSub
        :type request: :class:`huaweicloudsdkdws.v2.UpdateAlarmSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateAlarmSubResponse`
        """
        return self._update_alarm_sub_with_http_info(request)

    def _update_alarm_sub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_sub_id' in local_var_params:
            path_params['alarm_sub_id'] = local_var_params['alarm_sub_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-subs/{alarm_sub_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmSubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cluster_dns(self, request):
        """修改集群域名

        为指定集群修改域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterDns
        :type request: :class:`huaweicloudsdkdws.v2.UpdateClusterDnsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateClusterDnsResponse`
        """
        return self._update_cluster_dns_with_http_info(request)

    def _update_cluster_dns_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/dns',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateClusterDnsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_configuration(self, request):
        """修改集群参数配置

        修改集群使用的参数配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfiguration
        :type request: :class:`huaweicloudsdkdws.v2.UpdateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateConfigurationResponse`
        """
        return self._update_configuration_with_http_info(request)

    def _update_configuration_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/configurations/{configuration_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_data_source(self, request):
        """更新数据源

        该接口用于更新一个数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataSource
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDataSourceResponse`
        """
        return self._update_data_source_with_http_info(request)

    def _update_data_source_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'ext_data_source_id' in local_var_params:
            path_params['ext_data_source_id'] = local_var_params['ext_data_source_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources/{ext_data_source_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataSourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_database_authority(self, request):
        """修改数据库对象权限

        修改数据库对象权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseAuthority
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDatabaseAuthorityRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDatabaseAuthorityResponse`
        """
        return self._update_database_authority_with_http_info(request)

    def _update_database_authority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/authority',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDatabaseAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_database_user_info(self, request):
        """修改指定用户信息

        修改指定用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseUserInfo
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDatabaseUserInfoRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDatabaseUserInfoResponse`
        """
        return self._update_database_user_info_with_http_info(request)

    def _update_database_user_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/clusters/{cluster_id}/db-manager/users/{name}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDatabaseUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_disaster_info(self, request):
        """更新容灾配置

        更新容灾配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDisasterInfo
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDisasterInfoRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDisasterInfoResponse`
        """
        return self._update_disaster_info_with_http_info(request)

    def _update_disaster_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/disaster-recovery/{disaster_recovery_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDisasterInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_event_sub(self, request):
        """更新订阅事件

        更新订阅事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEventSub
        :type request: :class:`huaweicloudsdkdws.v2.UpdateEventSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateEventSubResponse`
        """
        return self._update_event_sub_with_http_info(request)

    def _update_event_sub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_sub_id' in local_var_params:
            path_params['event_sub_id'] = local_var_params['event_sub_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/event-subs/{event_sub_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEventSubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_maintenance_window(self, request):
        """修改运维时间窗

        您可以根据业务需求，设置可维护时间段。建议将可维护时间段设置在业务低峰期，避免业务在维护过程中异常中断。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMaintenanceWindow
        :type request: :class:`huaweicloudsdkdws.v2.UpdateMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateMaintenanceWindowResponse`
        """
        return self._update_maintenance_window_with_http_info(request)

    def _update_maintenance_window_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/maintenance-window',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMaintenanceWindowResponse',
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
