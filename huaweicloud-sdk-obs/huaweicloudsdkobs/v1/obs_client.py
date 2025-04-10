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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkobs'")


class ObsClient(Client):
    def __init__(self):
        super(ObsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkobs.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "ObsCredentials")
        else:
            if clazz.__name__ != "ObsClient":
                raise TypeError("client type error, support client type is ObsClient")
            client_builder = ClientBuilder(clazz, "ObsCredentials")

        

        return client_builder

    def delete_bucket_customdomain(self, request):
        r"""Deleting a Custom Domain Name of a Bucket

        This operation deletes a custom domain name of a bucket.
        
        To use this operation, you must have the **PutBucketcustomdomain** permission. The bucket owner can perform this operation by default and can grant this permission to others by using a bucket policy or a user policy.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBucketCustomdomain
        :type request: :class:`huaweicloudsdkobs.v1.DeleteBucketCustomdomainRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteBucketCustomdomainResponse`
        """
        http_info = self._delete_bucket_customdomain_http_info(request)
        return self._call_api(**http_info)

    def delete_bucket_customdomain_invoker(self, request):
        http_info = self._delete_bucket_customdomain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_bucket_customdomain_http_info(cls, request):
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

    def get_bucket_acl(self, request):
        r"""Obtaining a Bucket ACL

        This operation returns the ACL of a bucket. To use this operation, you must have the **READ_ACP** or **FULL_CONTROL** permission for the bucket.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetBucketAcl
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketAclRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketAclResponse`
        """
        http_info = self._get_bucket_acl_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_acl_invoker(self, request):
        http_info = self._get_bucket_acl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_bucket_acl_http_info(cls, request):
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

    def get_bucket_customdomain(self, request):
        r"""Getting a Custom Domain Name of a Bucket

        This operation gets a custom domain name of a bucket.
        
        To use this operation, you must have the **GetBucketcustomdomainConfiguration** permission. The bucket owner has this permission by default and can grant it to others.
        
        For details about permission control, see the [permission control](https://support.huaweicloud.com/intl/en-us/perms-cfg-obs/obs_40_0001.html) in the *Object Storage Service Permissions Configuration Guide*.
        
        User-defined domain names currently only allow requests over HTTP. To import a certificate to use HTTPS, you can [submit a service ticket](https://support.huaweicloud.com/intl/en-us/usermanual-ticket/topic_0065264094.html).
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetBucketCustomdomain
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketCustomdomainRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketCustomdomainResponse`
        """
        http_info = self._get_bucket_customdomain_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_customdomain_invoker(self, request):
        http_info = self._get_bucket_customdomain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_bucket_customdomain_http_info(cls, request):
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

    def get_bucket_notification(self, request):
        r"""Getting the Notification Configuration of a Bucket

        This operation returns the notification configuration of a bucket.
        
        To use this operation, you must have the **GetBucketNotification** permission. The bucket owner has this permission by default and can grant it to others by using a bucket policy or a user policy.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetBucketNotification
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketNotificationRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketNotificationResponse`
        """
        http_info = self._get_bucket_notification_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_notification_invoker(self, request):
        http_info = self._get_bucket_notification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_bucket_notification_http_info(cls, request):
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

    def set_bucket_acl(self, request):
        r"""Configuring a Bucket ACL

        This operation controls access to a bucket. By default, only the bucket creator has the read and write permissions on the bucket. You can also customize access policies for a bucket, for example, configuring a public read policy for the bucket to allow all users to read it.
        
        You can configure an ACL when creating a bucket, or modify or obtain the bucket ACL using API calls. A bucket ACL supports a maximum of 100 grants. The PUT method is idempotent. With this method, a new bucket ACL will overwrite the previous bucket ACL. To modify or delete an ACL, you just need to create a new one using the PUT method.
        
        For details about how to use bucket ACLs to control permissions, see the [OBS permission control](https://support.huaweicloud.com/intl/en-us/perms-cfg-obs/obs_40_0001.html) in the *Object Storage Service Permissions Configuration Guide*.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBucketAcl
        :type request: :class:`huaweicloudsdkobs.v1.SetBucketAclRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketAclResponse`
        """
        http_info = self._set_bucket_acl_http_info(request)
        return self._call_api(**http_info)

    def set_bucket_acl_invoker(self, request):
        http_info = self._set_bucket_acl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_bucket_acl_http_info(cls, request):
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

    def set_bucket_customedomain(self, request):
        r"""Configuring a Custom Domain Name for a Bucket

        This operation configures a custom domain name for a bucket. After the configuration is successful, you can access the bucket using its custom domain name.
        
        Ensure that DNS can resolve the custom domain name to OBS.
        
        User-defined domain names currently only allow requests over HTTP. To import a certificate to use HTTPS, you can [submit a service ticket](https://support.huaweicloud.com/intl/en-us/usermanual-ticket/topic_0065264094.html).
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBucketCustomedomain
        :type request: :class:`huaweicloudsdkobs.v1.SetBucketCustomedomainRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketCustomedomainResponse`
        """
        http_info = self._set_bucket_customedomain_http_info(request)
        return self._call_api(**http_info)

    def set_bucket_customedomain_invoker(self, request):
        http_info = self._set_bucket_customedomain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_bucket_customedomain_http_info(cls, request):
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

    def set_bucket_notification(self, request):
        r"""Configuring Notifications for a Bucket

        This operation configures event notifications for your OBS bucket so that you can receive notifications when certain events happen in your bucket.
        
        By default, a bucket has no event notifications configured. In this case, the bucket has an empty **NotificationConfiguration**. If a bucket has event notifications configured, you can add an empty **NotificationConfiguration** to disable notifications.
        
        &lt;NotificationConfiguration&gt;
        &lt;/NotificationConfiguration&gt; 
        
        OBS currently supports event notifications relying on Simple Message Notification (SMN) and FunctionGraph. Take SMN as an example. After receiving an event notification configuration request, OBS verifies whether the specified SMN topic exists and whether the topic is authorized to OBS. If the topic exists and is authorized to OBS, OBS sends a test notification to the topic subscriber..
        
        To use this operation, you must have the **PutBucketNotification** permission. The bucket owner has this permission by default and can grant it to others by using a bucket policy.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBucketNotification
        :type request: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketNotificationResponse`
        """
        http_info = self._set_bucket_notification_http_info(request)
        return self._call_api(**http_info)

    def set_bucket_notification_invoker(self, request):
        http_info = self._set_bucket_notification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_bucket_notification_http_info(cls, request):
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

    def create_bucket(self, request):
        r"""Creating a Bucket

        This operation creates a new bucket.
        
        Note:
        By default, a user can have a maximum of 100 buckets.
        The name of a deleted bucket can be reused for another bucket or a parallel file system at least 30 minutes later after the deletion.
        When creating a bucket in OBS, you can enable the multi-AZ storage for the bucket or disable it. With the multi-AZ storage disabled, data in a bucket is stored in a single AZ by default. With the multi-AZ storage enabled, data in a bucket is stored redundantly in multiple AZs, improving reliability. Old buckets use single-AZ storage by default.
        A bucket name must be unique in OBS. If you create namesake buckets in the same region, a success message is returned. In other cases, if namesake buckets are created, an error message will be returned, indicating that the bucket already exists. You can add parameters like **x-obs-acl** in request headers to configure access control policies for a bucket.
        
        **Storage Classes**
        You can create buckets with different storage classes. In a bucket creation request, add the **x-obs-storage-class** header to specify the default storage class for a bucket. The storage class of objects in a bucket defaults to that of the bucket. There are three storage classes: Standard (STANDARD), Infrequent Access (WARM), and Archive (COLD). If **x-obs-storage-class** is not included in a bucket creation request, the bucket is created in the Standard storage class.
        
        When uploading an object, if you do not specify a storage class for the object (see the upload with PUT), it inherits the storage class of the bucket by default.
        
        The OBS Standard features low latency and high throughput. It is good for storing frequently accessed files. Its application scenarios include big data analytics, mobile apps, hot videos, and social apps.
        The OBS Infrequent Access is for storing data that is infrequently (less than 12 times per year) accessed, but when needed, the access has to be fast. It can be used for file synchronization, file sharing, enterprise backups, and many other scenarios. It has the same durability, low latency, and high throughput as the Standard storage class, with a lower cost, but its availability is slightly lower than the Standard storage class.
        The OBS Archive is for storing data that is rarely (once per year) accessed. The application scenarios include data archive and long-term backup storage. It is secure and durable and delivers the lowest cost among the three storage classes. The OBS Archive storage class can be used to replace tape libraries. To keep cost low, it may take hours to restore data from the Archive storage class.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBucket
        :type request: :class:`huaweicloudsdkobs.v1.CreateBucketRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.CreateBucketResponse`
        """
        http_info = self._create_bucket_http_info(request)
        return self._call_api(**http_info)

    def create_bucket_invoker(self, request):
        http_info = self._create_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_bucket_http_info(cls, request):
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

    def delete_bucket(self, request):
        r"""Deleting a Bucket

        This operation deletes a bucket. Only the bucket owner or the user who has the bucket delete permission can delete the bucket. Before a bucket itself can be deleted, all objects in the bucket must be deleted. A bucket is not empty if it has any object or multipart upload in it. You can list objects and multipart uploads in the bucket to check whether the bucket is empty.
        Note:
        If the server returns a **5***XX* error or times out when a bucket is being deleted, the system needs to synchronize the bucket information. During this period, the bucket information may be inaccurate. Wait a while and then check whether the bucket is deleted. If the bucket can still be queried, send a delete request again.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBucket
        :type request: :class:`huaweicloudsdkobs.v1.DeleteBucketRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteBucketResponse`
        """
        http_info = self._delete_bucket_http_info(request)
        return self._call_api(**http_info)

    def delete_bucket_invoker(self, request):
        http_info = self._delete_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_bucket_http_info(cls, request):
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

    def get_bucket_metadata(self, request):
        r"""Getting Metadata of a Bucket

        This operation queries the metadata of a bucket. To use this operation, you must have the permission to read the bucket.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetBucketMetadata
        :type request: :class:`huaweicloudsdkobs.v1.GetBucketMetadataRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetBucketMetadataResponse`
        """
        http_info = self._get_bucket_metadata_http_info(request)
        return self._call_api(**http_info)

    def get_bucket_metadata_invoker(self, request):
        http_info = self._get_bucket_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_bucket_metadata_http_info(cls, request):
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

    def list_buckets(self, request):
        r"""Getting a List of Buckets

        This operation returns a list of all buckets you created.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBuckets
        :type request: :class:`huaweicloudsdkobs.v1.ListBucketsRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.ListBucketsResponse`
        """
        http_info = self._list_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_buckets_invoker(self, request):
        http_info = self._list_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_buckets_http_info(cls, request):
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

    def list_objects(self, request):
        r"""Listing Objects in a Bucket

        This operation returns objects in a bucket.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObjects
        :type request: :class:`huaweicloudsdkobs.v1.ListObjectsRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.ListObjectsResponse`
        """
        http_info = self._list_objects_http_info(request)
        return self._call_api(**http_info)

    def list_objects_invoker(self, request):
        http_info = self._list_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_objects_http_info(cls, request):
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

    def copy_object(self, request):
        r"""Copying an Object

        This operation creates a copy of an object in OBS.
        
        When copying an object, you can keep all metadata of the source object (default) or replace the metadata with the new metadata provided in the request. However, the ACL of the source object is not preserved and is set to private for the object copy. You can use the ACL setting API to update the ACL of the new object.
        
        The data copy request needs to carry the information about the source bucket and object in headers, but cannot carry the message body.
        
        This operation supports server-side encryption.
        
        The object you can copy is up to 5 GB. If the source object is larger than 5 GB, you can only copy some of the object using **Range**.
        
        **Versioning**
        By default, **x-obs-copy-source** specifies the latest version of the source object. If the latest version of the source object has a delete marker, the object is considered deleted. To copy a specific object version, add the **versionId** parameter in the **x-obs-copy-source** request header.
        
        If versioning is enabled for the bucket storing the target object, OBS generates a unique version ID for the target object (this version ID is different from that of the source object) and returns the version ID in the **x-obs-version-id** response header. If versioning is suspended for the target bucket, the version ID of the target object is **null**.
        
        Note:
        Assume that the target bucket already has **object_B** in it and has the versioning not enabled. If you make a copy of **object_A** and save it as **object_B** in the target bucket, the new **object_B** will overwrite the old one. You can download only the new **object_B**, as the old one has been deleted. To use this API, ensure that there is no object with the same name as the object copy to protect data from being deleted by mistake. This copy operation does not make any changes to **object_A**.
        
        **status_code** in the returned HTTP header does not represent whether an object copy is successful. Status code 200 indicates that the server has received the data copy request and starts to process it. A copy request succeeds only when the body in the response contains ETag, or the copy request failed.
        
        **Archive Objects**
        If source objects are in the Archive storage class, ensure that these objects have been restored before you copy them. If a source object is not restored or is being restored, its copy will fail and error **403 Forbidden** will be returned. The error description is as follows:
        
        ErrorCode: InvalidObjectState
        
        ErrorMessage: Operation is not valid for the source object&#39;s storage class
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyObject
        :type request: :class:`huaweicloudsdkobs.v1.CopyObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.CopyObjectResponse`
        """
        http_info = self._copy_object_http_info(request)
        return self._call_api(**http_info)

    def copy_object_invoker(self, request):
        http_info = self._copy_object_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_object_http_info(cls, request):
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

    def delete_object(self, request):
        r"""Deleting an Object

        This operation deletes an object. If you try to delete an object that does not exist, OBS still returns a success message.
        
        **Versioning**
        When versioning is enabled for a bucket, deleting an object with no version ID specified attaches a delete marker with a unique version ID to the object, but the object is not really deleted. When versioning is suspended for a bucket, deleting an object with no version ID specified deletes the object whose version ID is **null** and creates a delete marker with a version ID **null**.
        
        To delete a specific object version, add the **versionId** parameter in the request.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteObject
        :type request: :class:`huaweicloudsdkobs.v1.DeleteObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteObjectResponse`
        """
        http_info = self._delete_object_http_info(request)
        return self._call_api(**http_info)

    def delete_object_invoker(self, request):
        http_info = self._delete_object_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_object_http_info(cls, request):
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

    def delete_objects(self, request):
        r"""Batch Deleting Objects

        This operation deletes some objects in a bucket at a time. The operation cannot be undone.  OBS synchronously deletes objects in a batch. The deletion result of each object is returned.
        
        Batch object deletion supports two response methods: verbose and quiet. With verbose, OBS returns the results of both successful and failed deletions in the XML response; with quiet, OBS only returns the results of failed deletions in the XML response. OBS uses verbose by default. To use quiet, specify the quiet method in the request body.
        
        In a batch deletion request, the **Content-MD5** and **Content-Length** headers must be included, so that the message body can be identified if the server discovers a network transmission error.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteObjects
        :type request: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteObjectsResponse`
        """
        http_info = self._delete_objects_http_info(request)
        return self._call_api(**http_info)

    def delete_objects_invoker(self, request):
        http_info = self._delete_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_objects_http_info(cls, request):
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

    def get_object(self, request):
        r"""Downloading an Object

        This operation downloads an object from OBS. To use this operation, you must have the read permission for the object. If the object owner has granted anonymous users the read permission for the object, anonymous users can access this object without using the authentication header field.
        
        **Server-Side Encryption**
        If the object uploaded to a server is encrypted with the key provided by the client, the key must also be provided in the message for downloading the object.
        
        **Versioning**
        By default, this operation returns the latest object version. If the latest object version has a delete marker, OBS returns a message indicating that the object does not exist. To download a specific object version, add the **versionId** parameter in the request.
        
        **Archive Objects**
        You must restore an Archive object before you can download it. The response varies depending on the restore status of the object. If an object has been restored, after this object is downloaded, the **x-obs-restore** header is returned to indicate when the retention of the restored object expires. If you send a request to download Archive objects that are not restored or are being restored, a **403 Forbidden** error is returned.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetObject
        :type request: :class:`huaweicloudsdkobs.v1.GetObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetObjectResponse`
        """
        http_info = self._get_object_http_info(request)
        return self._call_api(**http_info)

    def get_object_invoker(self, request):
        http_info = self._get_object_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_object_http_info(cls, request):
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

    def get_object_metadata(self, request):
        r"""Getting Metadata of an Object

        This operation returns the metadata of an object. To use this operation, you must have the read permission on the object.
        This operation supports server-side encryption.
        
        **Versioning**
        By default, this operation returns the metadata of the latest object version. If this object has a delete marker, status code 404 is returned. To obtain the metadata of a specific object version, add the **versionId** parameter in the request.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetObjectMetadata
        :type request: :class:`huaweicloudsdkobs.v1.GetObjectMetadataRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.GetObjectMetadataResponse`
        """
        http_info = self._get_object_metadata_http_info(request)
        return self._call_api(**http_info)

    def get_object_metadata_invoker(self, request):
        http_info = self._get_object_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_object_metadata_http_info(cls, request):
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

    def put_object(self, request):
        r"""Uploading an Object - PUT

        After you create a bucket in OBS, you can use this operation to upload an object to your bucket. This operation adds an object to a bucket. To use this operation, you must have write permissions on the bucket.The name of each object in a bucket must be unique.With versioning not enabled, if an object to be uploaded has the same name as an existing object in the bucket, the newly uploaded object will overwrite the existing one. To protect data from being corrupted during transmission, you can add the **Content-MD5** parameter in the request header. After receiving the request, OBS will perform an MD5 consistency check. If the two MD5 values are inconsistent, the system returns an error message.You can also specify the **x-obs-acl** parameter to configure an access control policy for the object. If an anonymous user does not specify **x-obs-acl** when uploading an object, the object can be accessed by all OBS users by default.This operation supports server-side encryption.The object size in a single upload is up to 5 GB. To upload a file larger than 5 GB, use the multipart upload.OBS does not have real folders. For easy data management, OBS allows you to simulate a folder by adding a slash (/) to the object name, for example, **test/123.jpg**. OBS will present **test** to you as a folder and **123.jpg** as the name of a file stored inside of **test**, but the object key is still actually **test/123.jpg**. Objects named this way appear as folders on OBS Console.**Differences Between PUT and POST**  In the PUT method, parameters are passed using request headers. In the POST method, parameters are passed using form fields in the message body.To upload an object with PUT, you need to specify the object name in the URL. The object name is not required with the POST method that uses the bucket domain name as the URL. An example of an upload with PUT or POST is as follows:PUT /ObjectName HTTP/1.1POST / HTTP/1.1For POST upload, see the corresponding section.**Versioning**   If versioning is enabled on a bucket, OBS assigns a unique version ID for the object you upload to the bucket and returns this version ID in the **x-obs-version-id** header in the response. If versioning is suspended for the bucket, the object version ID is **null**. For details about the bucket versioning status, see the configuration of bucket versioning.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PutObject
        :type request: :class:`huaweicloudsdkobs.v1.PutObjectRequest`
        :rtype: :class:`huaweicloudsdkobs.v1.PutObjectResponse`
        """
        http_info = self._put_object_http_info(request)
        return self._call_api(**http_info)

    def put_object_invoker(self, request):
        http_info = self._put_object_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _put_object_http_info(cls, request):
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
