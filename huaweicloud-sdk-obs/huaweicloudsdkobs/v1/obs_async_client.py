# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkobs'")


class ObsAsyncClient(Client):
    def __init__(self):
        super(ObsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkobs.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "ObsCredentials")
        else:
            if clazz.__name__ != "ObsAsyncClient":
                raise TypeError("client type error, support client type is ObsAsyncClient")
            client_builder = ClientBuilder(clazz, "ObsCredentials")

        

        return client_builder

    def copy_object_async(self, request):
        """复制对象

        复制对象（Copy Object）特性用来为OBS上已经存在的对象创建一个副本。
        
        当进行复制对象操作时，目标对象默认复制源对象的元数据；用户也可以将目标对象的元数据替换为本次请求中所带的元数据。新建的目标对象不会复制源对象的ACL信息，默认的新建对象的ACL是private，用户可以使用设置ACL的操作接口来重新设定新对象的ACL。
        
        复制对象操作的请求需要通过头域携带拷贝的原桶和对象信息，不能携带消息实体。
        
        该操作支持服务端加密功能。
        
        目标对象大小范围是[0, 5GB]，如果源对象大小超过5GB，只能使用Range拷贝部分对象。
        
        #### 多版本 ####
        默认情况下，x-obs-copy-source标识复制源对象的最新版本。如果源对象的最新版本是删除标记，则认为该对象已删除。要复制指定版本的对象，可以在x-obs-copy-source请求消息头中携带versionId参数。
        
        如果目标对象的桶的多版本状态是开启的，系统为目标对象生成唯一的版本号（此版本号与源对象的版本号不同），并且会在响应报头x-obs-version-id返回该版本号。如果目标对象的桶的多版本状态是暂停的，则目标对象的版本号为null。
        
        须知：
        在桶没有开启多版本的情况下，将源对象object_A复制为目标对象object_B，如果在复制操作之前对象object_B已经存在，复制操作执行之后老对象object_B则会被新复制对象object_B覆盖，复制成功后，只能下载到新的对象object_B，老对象object_B将会被删除。因此在使用copy接口时请确保目标对象不存在或者已无价值，避免因copy导致数据误删除。复制过程中源对象object_A无任何变化。
        
        复制对象的结果不能仅根据HTTP返回头域中的status_code来判断请求是否成功，头域中status_code返回200时表示服务端已经收到请求，且开始处理复制对象请求。复制是否成功会在响应消息的body中，只有body体中有ETag标签才表示成功，否则表示复制失败。
        
        #### 归档存储对象 ####
        如果源对象是归档存储对象，需要判断源对象的取回状态，只有当源对象处于已取回状态时，才能复制成功。源对象未取回或者正在取回时，会复制失败，返回错误403 Forbidden。异常描述为：
        
        ErrorCode: InvalidObjectState
        
        ErrorMessage: Operation is not valid for the source object&#39;s storage class
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyObject
        :type request: :class:`huaweicloudsdkobs.v1.CopyObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.CopyObjectResponse`
        """
        http_info = self._copy_object_http_info(request)
        return self._call_api(**http_info)

    def copy_object_async_invoker(self, request):
        http_info = self._copy_object_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_object_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/{object_key}",
            "request_type": request.__class__.__name__,
            "response_type": "CopyObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'object_key' in local_var_params:
            path_params['object_key'] = local_var_params['object_key']

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'x_obs_acl' in local_var_params:
            header_params['x-obs-acl'] = local_var_params['x_obs_acl']
        if 'x_obs_grant_read' in local_var_params:
            header_params['x-obs-grant-read'] = local_var_params['x_obs_grant_read']
        if 'x_obs_grant_read_acp' in local_var_params:
            header_params['x-obs-grant-read-acp'] = local_var_params['x_obs_grant_read_acp']
        if 'x_obs_grant_write_acp' in local_var_params:
            header_params['x-obs-grant-write-acp'] = local_var_params['x_obs_grant_write_acp']
        if 'x_obs_grant_full_control' in local_var_params:
            header_params['x-obs-grant-full-control'] = local_var_params['x_obs_grant_full_control']
        if 'x_obs_copy_source' in local_var_params:
            header_params['x-obs-copy-source'] = local_var_params['x_obs_copy_source']
        if 'x_obs_metadata_directive' in local_var_params:
            header_params['x-obs-metadata-directive'] = local_var_params['x_obs_metadata_directive']
        if 'x_obs_copy_source_if_match' in local_var_params:
            header_params['x-obs-copy-source-if-match'] = local_var_params['x_obs_copy_source_if_match']
        if 'x_obs_copy_source_if_none_match' in local_var_params:
            header_params['x-obs-copy-source-if-none-match'] = local_var_params['x_obs_copy_source_if_none_match']
        if 'x_obs_copy_source_if_unmodified_since' in local_var_params:
            header_params['x-obs-copy-source-if-unmodified-since'] = local_var_params['x_obs_copy_source_if_unmodified_since']
        if 'x_obs_copy_source_if_modified_since' in local_var_params:
            header_params['x-obs-copy-source-if-modified-since'] = local_var_params['x_obs_copy_source_if_modified_since']
        if 'x_obs_storage_class' in local_var_params:
            header_params['x-obs-storage-class'] = local_var_params['x_obs_storage_class']
        if 'x_obs_persistent_headers' in local_var_params:
            header_params['x-obs-persistent-headers'] = local_var_params['x_obs_persistent_headers']
        if 'x_obs_website_redirect_location' in local_var_params:
            header_params['x-obs-website-redirect-location'] = local_var_params['x_obs_website_redirect_location']
        if 'x_obs_server_side_encryption' in local_var_params:
            header_params['x-obs-server-side-encryption'] = local_var_params['x_obs_server_side_encryption']
        if 'x_obs_server_side_encryption_kms_key_id' in local_var_params:
            header_params['x-obs-server-side-encryption-kms-key-id'] = local_var_params['x_obs_server_side_encryption_kms_key_id']
        if 'x_obs_server_side_encryption_customer_algorithm' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-algorithm'] = local_var_params['x_obs_server_side_encryption_customer_algorithm']
        if 'x_obs_server_side_encryption_customer_key' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key'] = local_var_params['x_obs_server_side_encryption_customer_key']
        if 'x_obs_server_side_encryption_customer_key_md5' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key-MD5'] = local_var_params['x_obs_server_side_encryption_customer_key_md5']
        if 'x_obs_copy_source_server_side_encryption_customer_algorithm' in local_var_params:
            header_params['x-obs-copy-source-server-side-encryption-customer-algorithm'] = local_var_params['x_obs_copy_source_server_side_encryption_customer_algorithm']
        if 'x_obs_copy_source_server_side_encryption_customer_key' in local_var_params:
            header_params['x-obs-copy-source-server-side-encryption-customer-key'] = local_var_params['x_obs_copy_source_server_side_encryption_customer_key']
        if 'x_obs_copy_source_server_side_encryption_customer_key_md5' in local_var_params:
            header_params['x-obs-copy-source-server-side-encryption-customer-key-MD5'] = local_var_params['x_obs_copy_source_server_side_encryption_customer_key_md5']
        if 'success_action_redirect' in local_var_params:
            header_params['success_action_redirect'] = local_var_params['success_action_redirect']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "x-obs-server-side-encryption", "Connection", "x-obs-server-side-encryption-customer-key-MD5", "Date", "ETag", "x-obs-server-side-encryption-customer-algorithm", "x-obs-copy-source-version-id", "x-obs-storage-class", "x-obs-server-side-encryption-kms-key-id", "Content-Length", "x-obs-version-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_bucket_async(self, request):
        """创建桶

        创建桶是指按照用户指定的桶名创建一个新桶的操作。
        
        说明：
        默认情况下，一个用户可以拥有的桶的数量不能超过100个。
        用户删除桶后，需要等待30分钟才能创建同名桶和并行文件系统。
        OBS支持在创建桶时指定桶的AZ类型，您可以开启或关闭多AZ。关闭多AZ时，桶内数据默认存储在单个AZ内；开启多AZ时，桶内数据冗余存储在多个AZ内，可靠性更高。旧桶AZ类型默认为单AZ。
        新创建桶的桶名在OBS中必须是唯一的。如果是同一个用户重复创建同一区域的同名桶时返回成功。除此以外的其他场景重复创建同名桶返回桶已存在。用户可以在请求消息头中加入x-obs-acl等参数，设置要创建桶的权限控制策略。
        
        #### 存储类型 ####
        允许用户创建不同默认存储类型的桶。发送创桶请求时携带头域“x-obs-storage-class”来指定桶的默认存储类型。桶内对象的存储类型与桶默认存储类型保持一致。存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）。如果没有携带此头域 ，则创建的桶为标准存储类型。
        
        当往桶内上传对象时，如果没有指定对象的存储类别（参考PUT上传），则该对象的存储类型取桶的默认存储类型。
        
        OBS标准存储拥有低访问时延和较高的吞吐量，因而适用于有大量热点文件需要频繁访问数据的业务场景，例如：大数据、移动应用、热点视频、社交图片等场景。
        OBS低频访问存储适用于不频繁访问（少于每月一次访问）但在需要时也要求快速访问数据的业务场景，例如：文件同步/共享、企业备份等场景。与标准存储相比，低频访问存储有相同的数据持久性、吞吐量以及访问时延，且成本较低，但是可用性略低于标准存储。
        OBS归档存储适用于很少访问（平均一年访问一次）数据的业务场景，例如：数据归档、长期备份等场景。归档存储安全、持久且成本极低，可以用来替代磁带库。为了保持成本低廉，数据取回时间可能长达数分钟到数小时不等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBucket
        :type request: :class:`huaweicloudsdkobs.v1.CreateBucketRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.CreateBucketResponse`
        """
        http_info = self._create_bucket_http_info(request)
        return self._call_api(**http_info)

    def create_bucket_async_invoker(self, request):
        http_info = self._create_bucket_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_bucket_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBucketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'x_obs_acl' in local_var_params:
            header_params['x-obs-acl'] = local_var_params['x_obs_acl']
        if 'x_obs_storage_class' in local_var_params:
            header_params['x-obs-storage-class'] = local_var_params['x_obs_storage_class']
        if 'x_obs_grant_read' in local_var_params:
            header_params['x-obs-grant-read'] = local_var_params['x_obs_grant_read']
        if 'x_obs_grant_write' in local_var_params:
            header_params['x-obs-grant-write'] = local_var_params['x_obs_grant_write']
        if 'x_obs_grant_read_acp' in local_var_params:
            header_params['x-obs-grant-read-acp'] = local_var_params['x_obs_grant_read_acp']
        if 'x_obs_grant_write_acp' in local_var_params:
            header_params['x-obs-grant-write-acp'] = local_var_params['x_obs_grant_write_acp']
        if 'x_obs_grant_full_control' in local_var_params:
            header_params['x-obs-grant-full-control'] = local_var_params['x_obs_grant_full_control']
        if 'x_obs_grant_read_delivered' in local_var_params:
            header_params['x-obs-grant-read-delivered'] = local_var_params['x_obs_grant_read_delivered']
        if 'x_obs_grant_full_control_delivered' in local_var_params:
            header_params['x-obs-grant-full-control-delivered'] = local_var_params['x_obs_grant_full_control_delivered']
        if 'x_obs_az_redundancy' in local_var_params:
            header_params['x-obs-az-redundancy'] = local_var_params['x_obs_az_redundancy']
        if 'x_obs_fs_file_interface' in local_var_params:
            header_params['x-obs-fs-file-interface'] = local_var_params['x_obs_fs_file_interface']
        if 'x_obs_epid' in local_var_params:
            header_params['x-obs-epid'] = local_var_params['x_obs_epid']
        if 'x_obs_cluster_type' in local_var_params:
            header_params['x-obs-cluster-type'] = local_var_params['x_obs_cluster_type']
        if 'x_obs_location_clustergroup_id' in local_var_params:
            header_params['x-obs-location-clustergroup-id'] = local_var_params['x_obs_location_clustergroup_id']
        if 'x_obs_ies_location' in local_var_params:
            header_params['x-obs-ies-location'] = local_var_params['x_obs_ies_location']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/xml'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_bucket_async(self, request):
        """删除桶

        删除桶操作用于删除用户指定的桶。只有桶的所有者或者拥有桶的删桶policy权限的用户可以执行删除桶的操作，要删除的桶必须是空桶。如果桶中有对象或者有多段任务则认为桶不为空，可以使用列举桶内对象和列举出多段上传任务接口来确认桶是否为空。
        注：
        如果删除桶时，服务端返回5XX错误或超时，系统需要时间进行桶信息一致性处理，在此期间桶的信息会不准确，过一段时间再查看桶是否删除成功，查询到桶，需要再次发送删除桶消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBucket
        :type request: :class:`huaweicloudsdkobs.v1.DeleteBucketRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteBucketResponse`
        """
        http_info = self._delete_bucket_http_info(request)
        return self._call_api(**http_info)

    def delete_bucket_async_invoker(self, request):
        http_info = self._delete_bucket_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_bucket_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBucketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_bucket_customdomain_async(self, request):
        """删除桶的自定义域名

        OBS使用DELETE操作来删除指定桶的标签。
        
        要正确执行此操作，需要确保执行者有PutBucketcustomdomain权限。缺省情况下只有桶的所有者可以执行此操作，也可以通过设置桶策略或用户策略授权给其他用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBucketCustomdomain
        :type request: :class:`huaweicloudsdkobs.v1.DeleteBucketCustomdomainRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteBucketCustomdomainResponse`
        """
        http_info = self._delete_bucket_customdomain_http_info(request)
        return self._call_api(**http_info)

    def delete_bucket_customdomain_async_invoker(self, request):
        http_info = self._delete_bucket_customdomain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_bucket_customdomain_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBucketCustomdomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'customdomain' in local_var_params:
            query_params.append(('customdomain', local_var_params['customdomain']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_object_async(self, request):
        """删除对象

        删除对象的操作。如果要删除的对象不存在，则仍然返回成功信息。
        
        #### 多版本 ####
        当桶的多版本状态是开启时，不指定版本删除对象将产生一个带唯一版本号的删除标记，并不删除对象；当桶的多版本状态是Suspended时，不指定版本删除将删除版本号为null的对象，并将产生一个版本号为null的删除标记。
        
        如果要删除指定版本的对象，请求可携带versionId消息参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteObject
        :type request: :class:`huaweicloudsdkobs.v1.DeleteObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteObjectResponse`
        """
        http_info = self._delete_object_http_info(request)
        return self._call_api(**http_info)

    def delete_object_async_invoker(self, request):
        http_info = self._delete_object_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_object_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/{object_key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'object_key' in local_var_params:
            path_params['object_key'] = local_var_params['object_key']

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'version_id' in local_var_params:
            query_params.append(('versionId', local_var_params['version_id']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", "x-obs-delete-marker", "x-obs-version-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_objects_async(self, request):
        """批量删除对象

        批量删除对象特性用于将一个桶内的部分对象一次性删除，删除后不可恢复。批量删除对象要求返回结果里包含每个对象的删除结果。OBS的批量删除对象使用同步删除对象的方式，每个对象的删除结果返回给请求用户。
        
        批量删除对象支持两种响应方式：verbose和quiet。Verbose是指在返回响应时，不管对象是否删除成功都将删除结果包含在XML响应里；quiet是指在返回响应时，只返回删除失败的对象结果，没有返回的认为删除成功。OBS默认使用verbose模式，如果用户在请求消息体中指定quiet模式的话， 使用quiet模式。
        
        批量删除的请求消息头中必须包含Content-MD5以及Content-Length，用以保证请求的消息体在服务端检测到网络传输如果有错，则可以检测出来。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteObjects
        :type request: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteObjectsResponse`
        """
        http_info = self._delete_objects_http_info(request)
        return self._call_api(**http_info)

    def delete_objects_async_invoker(self, request):
        http_info = self._delete_objects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_objects_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'delete' in local_var_params:
            query_params.append(('delete', local_var_params['delete']))

        header_params = {}
        if 'content_md5' in local_var_params:
            header_params['Content-MD5'] = local_var_params['content_md5']
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/xml'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_bucket_acl_async(self, request):
        """获取桶ACL

        用户执行获取桶ACL的操作，返回信息包含指定桶的权限控制列表信息。用户必须拥有对指定桶READ_ACP的权限或FULL_CONTROL权限，才能执行获取桶ACL的操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetBucketAcl
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketAclRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketAclResponse`
        """
        http_info = self._get_bucket_acl_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_acl_async_invoker(self, request):
        http_info = self._get_bucket_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_bucket_acl_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "GetBucketAclResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'acl' in local_var_params:
            query_params.append(('acl', local_var_params['acl']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_bucket_customdomain_async(self, request):
        """获取桶的自定义域名

        OBS使用GET操作来获取桶的自定义域名。
        
        要正确执行此操作，需要确保执行者有GetBucketcustomdomainConfiguration权限。桶拥有者默认具有此权限，并且可以将此权限授予其他人。
        
        有关权限控制的更多信息请参考《对象存储服务权限配置指南》的[OBS权限控制概述](https://support.huaweicloud.com/perms-cfg-obs/obs_40_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetBucketCustomdomain
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketCustomdomainRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketCustomdomainResponse`
        """
        http_info = self._get_bucket_customdomain_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_customdomain_async_invoker(self, request):
        http_info = self._get_bucket_customdomain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_bucket_customdomain_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "GetBucketCustomdomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'customdomain' in local_var_params:
            query_params.append(('customdomain', local_var_params['customdomain']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_bucket_metadata_async(self, request):
        """获取桶元数据

        对桶拥有读权限的用户可以执行查询桶元数据是否存在的操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetBucketMetadata
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketMetadataRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketMetadataResponse`
        """
        http_info = self._get_bucket_metadata_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_metadata_async_invoker(self, request):
        http_info = self._get_bucket_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_bucket_metadata_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "GetBucketMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'origin' in local_var_params:
            header_params['Origin'] = local_var_params['origin']
        if 'access_control_request_headers' in local_var_params:
            header_params['Access-Control-Request-Headers'] = local_var_params['access_control_request_headers']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "x-obs-fs-file-interface", "x-obs-version", "Access-Control-Allow-Origin", "Access-Control-Allow-Methods", "x-obs-bucket-location", "Connection", "x-obs-epid", "Date", "Access-Control-Allow-Headers", "Access-Control-Expose-Headers", "ETag", "x-obs-storage-class", "x-obs-az-redundancy", "Content-Length", "Access-Control-Max-Age", "x-obs-ies-location", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_bucket_notification_async(self, request):
        """获取桶的消息通知配置

        获取指定桶的消息通知配置信息。
        
        为了能成功执行此配置操作，需要确保执行者拥有GetBucketNotification权限。默认情况下只有桶的所有者拥有该权限，但可以通过设置桶策略或用户策略授权给其他用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetBucketNotification
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketNotificationRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketNotificationResponse`
        """
        http_info = self._get_bucket_notification_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_notification_async_invoker(self, request):
        http_info = self._get_bucket_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_bucket_notification_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "GetBucketNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'notification' in local_var_params:
            query_params.append(('notification', local_var_params['notification']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_object_async(self, request):
        """获取对象内容

        GET操作从对象存储下载对象。使用GET接口前，请确认必须拥有对象的READ权限。如果对象Owner向匿名用户授予READ访问权限，则可以在不使用鉴权头域的情况下访问该对象。
        
        #### 服务端加密 ####
        如果客户端的对象上传时，使用了客户提供的加密密钥进行服务端加密，当下载对象时，同样也必须在消息中提供密钥。
        
        #### 多版本 ####
        默认情况下，获取的是最新版本的对象。如果最新版本的对象是删除标记，则返回对象不存在。如果要获取指定版本的对象，请求可携带versionId消息参数。
        
        #### 归档存储对象 ####
        如果要下载的对象是归档存储类对象，由于对象存储在存档设备中，您必须先使用对象取回，然后才能下载该归档存储对象。对象处于不同的取回状态时，给出不同响应：如果对象已取回，下载对象成功时需要返回x-obs-restore头域指示取回失效时间。对未取回或正在取回的归档存储对象发送下载请求时，会返回错误403 Forbidden。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetObject
        :type request: :class:`huaweicloudsdkobs.v1.GetObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetObjectResponse`
        """
        http_info = self._get_object_http_info(request)
        return self._call_api(**http_info)

    def get_object_async_invoker(self, request):
        http_info = self._get_object_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_object_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{object_key}",
            "request_type": request.__class__.__name__,
            "response_type": "GetObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'object_key' in local_var_params:
            path_params['object_key'] = local_var_params['object_key']

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'response_content_type' in local_var_params:
            query_params.append(('response-content-type', local_var_params['response_content_type']))
        if 'response_content_language' in local_var_params:
            query_params.append(('response-content-language', local_var_params['response_content_language']))
        if 'response_expires' in local_var_params:
            query_params.append(('response-expires', local_var_params['response_expires']))
        if 'response_cache_control' in local_var_params:
            query_params.append(('response-cache-control', local_var_params['response_cache_control']))
        if 'response_content_disposition' in local_var_params:
            query_params.append(('response-content-disposition', local_var_params['response_content_disposition']))
        if 'response_content_encoding' in local_var_params:
            query_params.append(('response-content-encoding', local_var_params['response_content_encoding']))
        if 'version_id' in local_var_params:
            query_params.append(('versionId', local_var_params['version_id']))
        if 'x_image_process' in local_var_params:
            query_params.append(('x-image-process', local_var_params['x_image_process']))
        if 'attname' in local_var_params:
            query_params.append(('attname', local_var_params['attname']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'range' in local_var_params:
            header_params['Range'] = local_var_params['range']
        if 'if_modified_since' in local_var_params:
            header_params['If-Modified-Since'] = local_var_params['if_modified_since']
        if 'if_unmodified_since' in local_var_params:
            header_params['If-Unmodified-Since'] = local_var_params['if_unmodified_since']
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']
        if 'if_none_match' in local_var_params:
            header_params['If-None-Match'] = local_var_params['if_none_match']
        if 'x_obs_server_side_encryption_customer_algorithm' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-algorithm'] = local_var_params['x_obs_server_side_encryption_customer_algorithm']
        if 'x_obs_server_side_encryption_customer_key' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key'] = local_var_params['x_obs_server_side_encryption_customer_key']
        if 'x_obs_server_side_encryption_customer_key_md5' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key-MD5'] = local_var_params['x_obs_server_side_encryption_customer_key_md5']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "x-obs-server-side-encryption", "x-obs-object-type", "x-obs-next-append-position", "Connection", "x-obs-server-side-encryption-customer-key-MD5", "x-obs-expiration", "Date", "ETag", "x-obs-server-side-encryption-customer-algorithm", "x-obs-server-side-encryption-kms-key-id", "Content-Length", "x-obs-website-redirect-location", "x-obs-delete-marker", "x-obs-version-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_object_metadata_async(self, request):
        """获取对象元数据

        拥有对象读权限的用户可以执行HEAD操作命令获取对象元数据，返回信息包含对象的元数据信息。
        该操作支持服务端加密功能。
        
        #### 多版本 ####
        默认情况下，获取的是最新版本的对象元数据。如果最新版本的对象是删除标记，则返回404。如果要获取指定版本的对象元数据，请求可携带versionId消息参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetObjectMetadata
        :type request: :class:`huaweicloudsdkobs.v1.GetObjectMetadataRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetObjectMetadataResponse`
        """
        http_info = self._get_object_metadata_http_info(request)
        return self._call_api(**http_info)

    def get_object_metadata_async_invoker(self, request):
        http_info = self._get_object_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_object_metadata_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/{object_key}",
            "request_type": request.__class__.__name__,
            "response_type": "GetObjectMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'object_key' in local_var_params:
            path_params['object_key'] = local_var_params['object_key']

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'version_id' in local_var_params:
            query_params.append(('versionId', local_var_params['version_id']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'origin' in local_var_params:
            header_params['Origin'] = local_var_params['origin']
        if 'access_control_request_headers' in local_var_params:
            header_params['Access-Control-Request-Headers'] = local_var_params['access_control_request_headers']
        if 'x_obs_server_side_encryption_customer_algorithm' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-algorithm'] = local_var_params['x_obs_server_side_encryption_customer_algorithm']
        if 'x_obs_server_side_encryption_customer_key' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key'] = local_var_params['x_obs_server_side_encryption_customer_key']
        if 'x_obs_server_side_encryption_customer_key_md5' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key-MD5'] = local_var_params['x_obs_server_side_encryption_customer_key_md5']
        if 'success_action_redirect' in local_var_params:
            header_params['success-action-redirect'] = local_var_params['success_action_redirect']
        if 'x_obs_expires' in local_var_params:
            header_params['x-obs-expires'] = local_var_params['x_obs_expires']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "x-obs-hash-crc64ecma", "Access-Control-Allow-Origin", "x-obs-server-side-encryption", "x-obs-restore", "x-obs-object-type", "x-obs-next-append-position", "Access-Control-Allow-Methods", "Connection", "x-obs-server-side-encryption-customer-key-MD5", "x-obs-expiration", "Date", "Access-Control-Allow-Headers", "x-obs-uploadId", "Access-Control-Expose-Headers", "ETag", "x-obs-server-side-encryption-customer-algorithm", "x-obs-storage-class", "x-obs-server-side-encryption-kms-key-id", "Content-Length", "Access-Control-Max-Age", "x-obs-website-redirect-location", "x-obs-version-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_buckets_async(self, request):
        """获取桶列表

        OBS用户可以通过请求查询自己创建的桶列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuckets
        :type request: :class:`huaweicloudsdkobs.v1.ListBucketsRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.ListBucketsResponse`
        """
        http_info = self._list_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_buckets_async_invoker(self, request):
        http_info = self._list_buckets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_buckets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListBucketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'x_obs_bucket_type' in local_var_params:
            header_params['x-obs-bucket-type'] = local_var_params['x_obs_bucket_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "x-obs-bucket-type", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_objects_async(self, request):
        """列举桶内对象

        对桶拥有读权限的用户可以执行获取桶内对象列表的操作。
        
        如果用户在请求的URI里只指定了桶名，即GET /BucketName，则返回信息中会包含桶内部分或所有对象的描述信息（一次最多返回1000个对象信息）；如果用户还指定了prefix、marker、max-keys、delimiter参数中的一个或多个，则返回的对象列表将按照如表1所示规定的语义返回指定的对象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListObjects
        :type request: :class:`huaweicloudsdkobs.v1.ListObjectsRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.ListObjectsResponse`
        """
        http_info = self._list_objects_http_info(request)
        return self._call_api(**http_info)

    def list_objects_async_invoker(self, request):
        http_info = self._list_objects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_objects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'max_keys' in local_var_params:
            query_params.append(('max-keys', local_var_params['max_keys']))
        if 'delimiter' in local_var_params:
            query_params.append(('delimiter', local_var_params['delimiter']))
        if 'key_marker' in local_var_params:
            query_params.append(('key-marker', local_var_params['key_marker']))
        if 'version_id_marker' in local_var_params:
            query_params.append(('version-id-marker', local_var_params['version_id_marker']))
        if 'encoding_type' in local_var_params:
            query_params.append(('encoding-type', local_var_params['encoding_type']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "x-obs-bucket-type", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def put_object_async(self, request):
        """PUT上传对象

        用户在OBS系统中创建了桶之后，可以采用PUT操作的方式将对象上传到桶中。上传对象操作是指在指定的桶内增加一个对象，执行该操作需要用户拥有桶的写权限。
        说明： 同一个桶中存储的对象名是唯一的。
        在桶未开启多版本的情况下，如果在指定的桶内已经有相同的对象键值的对象，用户上传的新对象会覆盖原来的对象；为了确保数据在传输过程中没有遭到破坏，用户可以在请求消息头中加入Content-MD5参数。在这种情况下，OBS收到上传的对象后，会对对象进行MD5校验，如果不一致则返回出错信息。
        用户还可以在上传对象时指定x-obs-acl参数，设置对象的权限控制策略。如果匿名用户在上传对象时未指定x-obs-acl参数，则该对象默认可以被所有OBS用户访问。
        该操作支持服务端加密功能。
        单次上传对象大小范围是[0, 5GB]，如果需要上传超过5GB的大文件，需要通过多段操作来分段上传。
        OBS没有文件夹的概念。为了使用户更方便进行管理数据，OBS提供了一种方式模拟文件夹：通过在对象的名称中增加“/”，例如“test/123.jpg”。此时，“test”就被模拟成了一个文件夹，“123.jpg”则模拟成“test”文件夹下的文件名了，而实际上，对象名称（Key）仍然是“test/123.jpg”。此类命名方式的对象，在控制台上会以文件夹的形式展示。
        #### 与POST上传的区别 #### PUT上传中参数通过请求头域传递；POST上传则作为消息体中的表单域传递。
        PUT上传需在URL中指定对象名；POST上传提交的URL为桶域名，无需指定对象名。两者的请求行分别为：
        PUT /ObjectName HTTP/1.1
        POST / HTTP/1.1
        关于POST上传的更多详细信息，请参考POST上传。
        #### 多版本 #### 如果桶的多版本状态是开启的，系统会自动为对象生成一个唯一的版本号，并且会在响应报头x-obs-version-id返回该版本号。如果桶的多版本状态是暂停的，则对象的版本号为null。关于桶的多版本状态，参见设置桶的多版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PutObject
        :type request: :class:`huaweicloudsdkobs.v1.PutObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.PutObjectResponse`
        """
        http_info = self._put_object_http_info(request)
        return self._call_api(**http_info)

    def put_object_async_invoker(self, request):
        http_info = self._put_object_http_info(request)
        return AsyncInvoker(self, http_info)

    def _put_object_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/{object_key}",
            "request_type": request.__class__.__name__,
            "response_type": "PutObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'object_key' in local_var_params:
            path_params['object_key'] = local_var_params['object_key']

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'content_md5' in local_var_params:
            header_params['Content-MD5'] = local_var_params['content_md5']
        if 'x_obs_acl' in local_var_params:
            header_params['x-obs-acl'] = local_var_params['x_obs_acl']
        if 'x_obs_grant_read' in local_var_params:
            header_params['x-obs-grant-read'] = local_var_params['x_obs_grant_read']
        if 'x_obs_grant_read_acp' in local_var_params:
            header_params['x-obs-grant-read-acp'] = local_var_params['x_obs_grant_read_acp']
        if 'x_obs_grant_write_acp' in local_var_params:
            header_params['x-obs-grant-write-acp'] = local_var_params['x_obs_grant_write_acp']
        if 'x_obs_grant_full_control' in local_var_params:
            header_params['x-obs-grant-full-control'] = local_var_params['x_obs_grant_full_control']
        if 'x_obs_storage_class' in local_var_params:
            header_params['x-obs-storage-class'] = local_var_params['x_obs_storage_class']
        if 'x_obs_meta_xxx' in local_var_params:
            header_params['x-obs-meta-xxx'] = local_var_params['x_obs_meta_xxx']
        if 'x_obs_persistent_headers' in local_var_params:
            header_params['x-obs-persistent-headers'] = local_var_params['x_obs_persistent_headers']
        if 'x_obs_website_redirect_location' in local_var_params:
            header_params['x-obs-website-redirect-location'] = local_var_params['x_obs_website_redirect_location']
        if 'x_obs_server_side_encryption' in local_var_params:
            header_params['x-obs-server-side-encryption'] = local_var_params['x_obs_server_side_encryption']
        if 'x_obs_server_side_encryption_kms_key_id' in local_var_params:
            header_params['x-obs-server-side-encryption-kms-key-id'] = local_var_params['x_obs_server_side_encryption_kms_key_id']
        if 'x_obs_server_side_encryption_customer_algorithm' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-algorithm'] = local_var_params['x_obs_server_side_encryption_customer_algorithm']
        if 'x_obs_server_side_encryption_customer_key' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key'] = local_var_params['x_obs_server_side_encryption_customer_key']
        if 'x_obs_server_side_encryption_customer_key_md5' in local_var_params:
            header_params['x-obs-server-side-encryption-customer-key-MD5'] = local_var_params['x_obs_server_side_encryption_customer_key_md5']
        if 'success_action_redirect' in local_var_params:
            header_params['success-action-redirect'] = local_var_params['success_action_redirect']
        if 'x_obs_expires' in local_var_params:
            header_params['x-obs-expires'] = local_var_params['x_obs_expires']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "x-obs-server-side-encryption", "x-obs-server-side-encryption-customer-algorithm", "x-obs-storage-class", "Connection", "x-obs-server-side-encryption-customer-key-MD5", "x-obs-server-side-encryption-kms-key-id", "Content-Length", "Date", "x-obs-version-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/octet-stream'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_bucket_acl_async(self, request):
        """设置桶ACL

        OBS支持对桶操作进行权限控制。默认情况下，只有桶的创建者才有该桶的读写权限。用户也可以设置其他的访问策略，比如对一个桶可以设置公共访问策略，允许所有人对其都有读权限。
        
        OBS用户在创建桶时可以设置权限控制策略，也可以通过ACL操作API接口对已存在的桶更改或者获取ACL(access control list) 。一个桶的ACL最多支持100条Grant授权。PUT接口为幂等的覆盖写语意，新设置的桶ACL将覆盖原有的桶ACL，如果需要修改或者删除某条ACL重新PUT一个新的桶ACL即可。
        
        使用桶ACL进行权限控制请参考[《对象存储服务权限配置指南》的OBS权限控制概述章节](https://support.huaweicloud.com/perms-cfg-obs/obs_40_0001.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetBucketAcl
        :type request: :class:`huaweicloudsdkobs.v1.SetBucketAclRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketAclResponse`
        """
        http_info = self._set_bucket_acl_http_info(request)
        return self._call_api(**http_info)

    def set_bucket_acl_async_invoker(self, request):
        http_info = self._set_bucket_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_bucket_acl_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "SetBucketAclResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'acl' in local_var_params:
            query_params.append(('acl', local_var_params['acl']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']
        if 'x_obs_acl' in local_var_params:
            header_params['x-obs-acl'] = local_var_params['x_obs_acl']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/xml'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_bucket_customedomain_async(self, request):
        """设置桶的自定义域名

        OBS使用PUT操作为桶设置自定义域名，设置成功之后，用户访问桶的自定义域名就能访问到桶。
        
        必须保证此自定义域名通过DNS能够正确解析到OBS服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetBucketCustomedomain
        :type request: :class:`huaweicloudsdkobs.v1.SetBucketCustomedomainRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketCustomedomainResponse`
        """
        http_info = self._set_bucket_customedomain_http_info(request)
        return self._call_api(**http_info)

    def set_bucket_customedomain_async_invoker(self, request):
        http_info = self._set_bucket_customedomain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_bucket_customedomain_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "SetBucketCustomedomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'customdomain' in local_var_params:
            query_params.append(('customdomain', local_var_params['customdomain']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/xml'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_bucket_notification_async(self, request):
        """设置桶的消息通知配置

        OBS消息通知功能能够帮助您对桶的重要的操作及时通知到您，确保您安全、及时知道发生在桶上的关键事件。
        
        默认情况下，您的桶没有配置事件通知。这个时候桶的通知配置将是一个空NotificationConfiguration。对已配置有事件通知的桶，可以通过添加空NotificationConfiguration元素禁用消息通知功能。
        
        &lt;NotificationConfiguration&gt;
        &lt;/NotificationConfiguration&gt; 
        
        目前对象存储服务（OBS）支持包括简单通知服务（SMN）、函数工作流服务（FunctionGraph）在内的两种桶通知服务配置。以SMN为例，当OBS接收到配置消息通知的请求后，会验证指定的消息通知服务（SMN）主题是否存在及主题策略是否授权给了对象存储服务，验证通过后会向该主题订阅者发送一个测试消息通知。
        
        为了能成功执行此配置操作，需要确保执行者拥有PutBucketNotification权限。默认情况下只有桶的所有者拥有该权限，但可以通过设置桶策略授权给其他用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetBucketNotification
        :type request: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketNotificationResponse`
        """
        http_info = self._set_bucket_notification_http_info(request)
        return self._call_api(**http_info)

    def set_bucket_notification_async_invoker(self, request):
        http_info = self._set_bucket_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_bucket_notification_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "SetBucketNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket_name' in local_var_params:
            cname = local_var_params['bucket_name']
        if 'notification' in local_var_params:
            query_params.append(('notification', local_var_params['notification']))

        header_params = {}
        if 'date' in local_var_params:
            header_params['Date'] = local_var_params['date']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-obs-id-2", "x-obs-request-id", "ETag", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/xml'])

        auth_settings = []

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
            kwargs["async_request"] = True
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	        async_request=True)
