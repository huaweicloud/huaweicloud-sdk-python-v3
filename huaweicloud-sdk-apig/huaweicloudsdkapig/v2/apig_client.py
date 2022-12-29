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


class ApigClient(Client):
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
        super(ApigClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkapig.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ApigClient":
            raise TypeError("client type error, support client type is ApigClient")

        return ClientBuilder(clazz)

    def add_eip_v2(self, request):
        """实例更新或绑定EIP

        实例更新或绑定EIP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddEipV2
        :type request: :class:`huaweicloudsdkapig.v2.AddEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddEipV2Response`
        """
        return self.add_eip_v2_with_http_info(request)

    def add_eip_v2_with_http_info(self, request):
        all_params = ['instance_id', 'add_eip_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/eip',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_engress_eip_v2(self, request):
        """开启实例公网出口

        实例开启公网出口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.AddEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddEngressEipV2Response`
        """
        return self.add_engress_eip_v2_with_http_info(request)

    def add_engress_eip_v2_with_http_info(self, request):
        all_params = ['instance_id', 'add_engress_eip_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/nat-eip',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddEngressEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_certificate_v2(self, request):
        """绑定域名证书

        如果创建API时，“定义API请求”使用HTTPS请求协议，那么在独立域名中需要添加SSL证书。
        本章节主要介绍为特定域名绑定证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateCertificateV2Response`
        """
        return self.associate_certificate_v2_with_http_info(request)

    def associate_certificate_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'associate_certificate_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_domain_v2(self, request):
        """绑定域名

        用户自定义的域名，需要增加A记录才能生效，具体方法请参见《云解析服务用户指南》的“添加A类型记录集”章节。
        每个API分组下最多可绑定5个域名。绑定域名后，用户可通过自定义域名调用API。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateDomainV2Response`
        """
        return self.associate_domain_v2_with_http_info(request)

    def associate_domain_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'associate_domain_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateDomainV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_signature_key_v2(self, request):
        """绑定签名密钥

        签名密钥创建后，需要绑定到API才能生效。
        
        将签名密钥绑定到API后，则API网关请求后端服务时就会使用这个签名密钥进行加密签名，后端服务可以校验这个签名来验证请求来源。
        
        将指定的签名密钥绑定到一个或多个已发布的API上。同一个API发布到不同的环境可以绑定不同的签名密钥；一个API在发布到特定环境后只能绑定一个签名密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateSignatureKeyV2Response`
        """
        return self.associate_signature_key_v2_with_http_info(request)

    def associate_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'associate_signature_key_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_api_to_plugin(self, request):
        """插件绑定API

        绑定插件到API上。
        - 只能选择发布状态的API
        - 绑定以后及时生效
        - 修改插件后及时生效
        - 相同类型的插件只能绑定一个，原来已经绑定的通类型插件，会直接覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachApiToPlugin
        :type request: :class:`huaweicloudsdkapig.v2.AttachApiToPluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AttachApiToPluginResponse`
        """
        return self.attach_api_to_plugin_with_http_info(request)

    def attach_api_to_plugin_with_http_info(self, request):
        all_params = ['instance_id', 'plugin_id', 'attach_api_to_plugin_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/attach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachApiToPluginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_plugin_to_api(self, request):
        """API绑定插件

        绑定插件到API上。
        - 只能选择发布状态的API
        - 绑定以后及时生效
        - 修改插件后及时生效
        - 相同类型的插件只能绑定一个，原来已经绑定的通类型插件，会直接覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachPluginToApi
        :type request: :class:`huaweicloudsdkapig.v2.AttachPluginToApiRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AttachPluginToApiResponse`
        """
        return self.attach_plugin_to_api_with_http_info(request)

    def attach_plugin_to_api_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'attach_plugin_to_api_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/plugins/attach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachPluginToApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_or_delete_instance_tags(self, request):
        """批量添加或删除单个实例的标签

        批量添加或删除单个实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateOrDeleteInstanceTags
        :type request: :class:`huaweicloudsdkapig.v2.BatchCreateOrDeleteInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchCreateOrDeleteInstanceTagsResponse`
        """
        return self.batch_create_or_delete_instance_tags_with_http_info(request)

    def batch_create_or_delete_instance_tags_with_http_info(self, request):
        all_params = ['instance_id', 'batch_create_or_delete_instance_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/instance-tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateOrDeleteInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_custom_authorizer_v2(self, request):
        """创建自定义认证

        创建自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateCustomAuthorizerV2Response`
        """
        return self.create_custom_authorizer_v2_with_http_info(request)

    def create_custom_authorizer_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_custom_authorizer_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCustomAuthorizerV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_environment_v2(self, request):
        """创建环境

        在实际的生产中，API提供者可能有多个环境，如开发环境、测试环境、生产环境等，用户可以自由将API发布到某个环境，供调用者调用。
        
        对于不同的环境，API的版本、请求地址甚至于包括请求消息等均有可能不同。如：某个API，v1.0的版本为稳定版本，发布到了生产环境供生产使用，同时，该API正处于迭代中，v1.1的版本是开发人员交付测试人员进行测试的版本，发布在测试环境上，而v1.2的版本目前开发团队正处于开发过程中，可以发布到开发环境进行自测等。
        
        为此，API网关提供多环境管理功能，使租户能够最大化的模拟实际场景，低成本的接入API网关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateEnvironmentV2Response`
        """
        return self.create_environment_v2_with_http_info(request)

    def create_environment_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_environment_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEnvironmentV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_environment_variable_v2(self, request):
        """新建变量

        将API发布到不同的环境后，对于不同的环境，可能会有不同的环境变量，比如，API的服务部署地址，请求的版本号等。
        
        
        用户可以定义不同的环境变量，用户在定义API时，在API的定义中使用这些变量，当调用API时，API网关会将这些变量替换成真实的变量值，以达到不同环境的区分效果。
        
        
        环境变量定义在API分组上，该分组下的所有API都可以使用这些变量。
        
        &gt; 1. 环境变量的变量名称必须保持唯一，即一个分组在同一个环境上不能有两个同名的变量。
        &gt; 2. 环境变量区分大小写，即变量ABC与变量abc是两个不同的变量。
        &gt; 3. 设置了环境变量后，使用到该变量的API的调试功能将不可使用。
        &gt; 4. 定义了环境变量后，使用到环境变量的地方应该以对称的#标识环境变量，当API发布到相应的环境后，会对环境变量的值进行替换，如：定义的API的URL为：https://#address#:8080，环境变量address在RELEASE环境上的值为：192.168.1.5，则API发布到RELEASE环境后的真实的URL为：https://192.168.1.5:8080。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateEnvironmentVariableV2Response`
        """
        return self.create_environment_variable_v2_with_http_info(request)

    def create_environment_variable_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_environment_variable_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEnvironmentVariableV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_feature_v2(self, request):
        """实例配置特性

        为实例配置需要的特性。
        
        支持配置的特性列表及特性配置示例如下：
        
        | 特性名称 | 特性描述 | 特性配置示例 | 特性参数名称 | 参数描述 | 参数默认值 | 参数范围 | 
        --------| :------- | :-------| :-------| :-------| :-------| :-------
        | lts | 是否支持shubao访问日志上报功能。|{\&quot;name\&quot;:\&quot;lts\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;group_id\\\\\&quot;: \\\&quot;\\,\\\\\&quot;topic_id\\\\\&quot;:\\\\\&quot;\\\\\&quot;,\\\\\&quot;log_group\\\\\&quot;:\\\\\&quot;\\\\\&quot;,\\\\\&quot;log_stream\\\\\&quot;:\\\\\&quot;\\\\\&quot;}\&quot;} | (1) group_id &lt;br/&gt;(2) topic_id &lt;br/&gt;(3) log_group &lt;br/&gt;(4) log_stream | (1) 日志组ID &lt;br/&gt;(2) 日志流ID &lt;br/&gt;(3) 日志组名称 &lt;br/&gt;(4) 日志流名称 | - | - |
        | ratelimit | 是否支持自定义流控值。|{\&quot;name\&quot;:\&quot;ratelimit\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;api_limits\\\\\&quot;: 500}\&quot;} | api_limits | API全局默认流控值。注意：如果配置过小会导致业务持续被流控，请根据业务谨慎修改。 | 200 次/秒 | 1-1000000 次/秒 |
        | request_body_size | 是否支持设置请求体大小上限。|{\&quot;name\&quot;:\&quot;request_body_size\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;104857600\&quot;} | request_body_size | 请求中允许携带的Body大小上限。 | 12 M | 1-9536 M |
        | backend_timeout | 是否支持配置后端API最大超时时间。|{\&quot;name\&quot;:\&quot;backend_timeout\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\&quot;max_timeout\\\&quot;: 500}\&quot;} | max_timeout | API网关到后端服务的超时时间上限。 | 60000 ms | 1-600000 ms |
        | app_token | 是否开启app_token认证方式。|{\&quot;name\&quot;:\&quot;app_token\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;, \\\\\&quot;app_token_expire_time\\\\\&quot;: 3600, \\\\\&quot;app_token_uri\\\\\&quot;: \\\\\&quot;/v1/apigw/oauth2/token\\\\\&quot;, \\\\\&quot;refresh_token_expire_time\\\\\&quot;: 7200}\&quot;} | (1) enable &lt;br/&gt;(2) app_token_expire_time &lt;br/&gt;(3) refresh_token_expire_time &lt;br/&gt;(4) app_token_uri &lt;br/&gt;(5) app_token_key | (1) 是否开启 &lt;br/&gt;(2) access token的有效时间 &lt;br/&gt;(3) refresh token的有效时间 &lt;br/&gt;(4) 获取token的uri &lt;br/&gt;(5) token的加密key | (1) off &lt;br/&gt;(2) 3600 s &lt;br/&gt;(3) 7200 s &lt;br/&gt;(4) /v1/apigw/oauth2/token | (1) on/off &lt;br/&gt;(2) 1-72000 s &lt;br/&gt;(3) 1-72000 s |
        | app_api_key | 是否开启app_api_key认证方式。|{\&quot;name\&quot;:\&quot;app_api_key\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} | - | - | off | on/off | 
        | app_basic | 是否开启app_basic认证方式。|{\&quot;name\&quot;:\&quot;app_basic\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} | - | - | off | on/off | 
        | app_secret | 是否支持app_secret认证方式。|{\&quot;name\&quot;:\&quot;app_secret\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} | - | - | off | on/off | 
        | app_jwt | 是否支持app_jwt认证方式。|{\&quot;name\&quot;:\&quot;app_jwt\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;, \\\\\&quot;auth_header\\\\\&quot;: \\\\\&quot;Authorization\\\\\&quot;}\&quot;}| (1) enable &lt;br/&gt;(2) auth_header | (1) 是否开启app_jwt认证方式。 &lt;br/&gt;(2) app_jwt认证头 | (1) off &lt;br/&gt;(2) Authorization | (1) on/off | 
        | public_key | 是否支持public_key类型的后端签名。|{\&quot;name\&quot;:\&quot;public_key\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;, \\\\\&quot;public_key_uri_prefix\\\\\&quot;: \\\\\&quot;/apigw/authadv/v2/public-key/\\\\\&quot;}\&quot;}| (1) enable &lt;br/&gt;(2) public_key_uri_prefix | (1)  是否开启app_jwt认证方式。 &lt;br/&gt;(2) 获取public key的uri前缀 | (1) off&lt;br/&gt;(2) /apigw/authadv/v2/public-key/ | (1) on/off | 
        | backend_token_allow | 是否支持普通租户透传token到后端。|{\&quot;name\&quot;:\&quot;backend_token_allow\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;backend_token_allow_users\\\\\&quot;: [\\\\\&quot;user_name\\\\\&quot;]}\&quot;} | backend_token_allow_users | 透传token到后端普通租户白名单，匹配普通租户domain name正则表达式 | - | - |
        | backend_client_certificate | 是否开启后端双向认证。|{\&quot;name\&quot;:\&quot;backend_client_certificate\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;,\\\\\&quot;ca\\\\\&quot;: \\\\\&quot;\\\\\&quot;,\\\\\&quot;content\\\\\&quot;: \\\\\&quot;\\\\\&quot;,\\\\\&quot;key\\\\\&quot;: \\\\\&quot;\\\\\&quot;}\&quot;} | (1) enable &lt;br/&gt;(2) ca &lt;br/&gt;(3)  content &lt;br/&gt;(4) key | (1) 是否开启 &lt;br/&gt;(2) 双向认证信任证书 &lt;br/&gt;(3) 双向认证证书 &lt;br/&gt;(4) 双向认证信任私钥 | (1) off | (1) on/off | 
        | ssl_ciphers | 是否支持https加密套件。|{\&quot;name\&quot;:\&quot;ssl_ciphers\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;config\&quot;: \&quot;{\\\\\&quot;ssl_ciphers\\\\\&quot;: [\\\\\&quot;ECDHE-ECDSA-AES256-GCM-SHA384\\\\\&quot;]}\&quot;} | ssl_ciphers | 支持的加解密套件。ssl_ciphers数组中只允许出现默认值中的字符串，且数组不能为空。 | - | ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256 |
        | real_ip_from_xff | 是否开启使用xff头作为访问控制、流控策略的源ip生效依据。|{\&quot;name\&quot;:\&quot;real_ip_from_xff\&quot;,\&quot;enable\&quot;: true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;,\\\\\&quot;xff_index\\\\\&quot;: 1}\&quot;} | (1) enable &lt;br/&gt;(2) xff_index | (1) 是否开启 &lt;br/&gt;(2)  源ip所在xff头的索引位置（支持负数，-1为最后一位，以此类推） | (1) off &lt;br/&gt;(2) -1 | (1) on/off &lt;br/&gt;(2) int32有效值 | 
        | app_route | 是否支持ip访问。|{\&quot;name\&quot;:\&quot;app_route\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} | - | - | off | on/off | 
        | vpc_name_modifiable | 是否支持修改负载通道名称。 |{\&quot;name\&quot;:\&quot;vpc_name_modifiable\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} | - | - | on | on/off | 
        | default_group_host_trustlist | DEFAULT分组是否支持配置非本实例IP访问。|{\&quot;name\&quot;:\&quot;default_group_host_trustlist\&quot;,\&quot;enable\&quot;: true,\&quot;config\&quot;:  \&quot;{\\\\\&quot;enable\\\\\&quot;:\\\\\&quot;on\\\\\&quot;,\\\\\&quot;hosts\\\\\&quot;:[\\\\\&quot;123.2.2.2\\\\\&quot;,\\\\\&quot;202.2.2.2\\\\\&quot;]}\&quot;} | (1) enable &lt;br/&gt;(2) hosts | (1) 是否开启 &lt;br/&gt;(2) 非本实例IP列表 | - | (1) on/off | 
        | throttle_strategy | 是否启用流控模式。 |{\&quot;name\&quot;:\&quot;throttle_strategy\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;,\\\\\&quot;strategy\\\\\&quot;: \\\\\&quot;local\\\\\&quot;}\&quot;} | (1) enable &lt;br/&gt;(2) strategy | (1) 是否开启&lt;br/&gt;(2) 流控模式 | (1) off | (1) on/off &lt;br/&gt;(2) cluster/local | 
        | custom_log | 是否支持用户自定义API请求中的HEADER、QUERY、COOKIE参数值打印到日志。 |{\&quot;name\&quot;:\&quot;custom_log\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;custom_logs\\\\\&quot;:[{\\\\\&quot;location\\\\\&quot;:\\\\\&quot;header\\\\\&quot;,\\\\\&quot;name\\\\\&quot;:\\\\\&quot;a1234\\\\\&quot;}]}\&quot;} | (1) custom_logs &lt;br/&gt;(2) location &lt;br/&gt;(3) name | (1) 自定义日志 &lt;br/&gt;(2) 位置&lt;br/&gt;(3) 名称 | - | (1) 数量不超过10个 &lt;br/&gt;(2) header/query/cookie | 
        | real_ip_header_getter | 是否开启通过用户自定义的Header获取用户源IP地址。 |{\&quot;name\&quot;:\&quot;real_ip_header_getter\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;{\\\\\&quot;enable\\\\\&quot;: \\\\\&quot;on\\\\\&quot;,\\\\\&quot;header_getter\\\\\&quot;: \\\\\&quot;header:testIP\\\\\&quot;}\&quot;} | (1) enable &lt;br/&gt;(2) header_getter | (1) 是否开启 &lt;br/&gt;(2) 获取用户源IP地址的自定义Header | (1) off | (1) on/off | 
        | policy_cookie_param | 是否开启策略后端条件支持cookie类型。 |{\&quot;name\&quot;:\&quot;policy_cookie_param\&quot;,\&quot;enable\&quot;:true,\&quot;config\&quot;: \&quot;on\&quot;} | - | - | off | on/off |
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFeatureV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateFeatureV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateFeatureV2Response`
        """
        return self.create_feature_v2_with_http_info(request)

    def create_feature_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_feature_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/features',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFeatureV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gateway_response_v2(self, request):
        """创建分组自定义响应

        新增分组下自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateGatewayResponseV2Response`
        """
        return self.create_gateway_response_v2_with_http_info(request)

    def create_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'create_gateway_response_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_v2(self, request):
        """创建专享版实例

        创建专享版实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateInstanceV2Response`
        """
        return self.create_instance_v2_with_http_info(request)

    def create_instance_v2_with_http_info(self, request):
        all_params = ['create_instance_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_plugin(self, request):
        """创建插件

        创建插件信息。
        - 插件不允许重名
        - 插件创建后未绑定API前是无意义的，绑定API后，对绑定的API即时生效
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlugin
        :type request: :class:`huaweicloudsdkapig.v2.CreatePluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreatePluginResponse`
        """
        return self.create_plugin_with_http_info(request)

    def create_plugin_with_http_info(self, request):
        all_params = ['instance_id', 'create_plugin_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePluginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_request_throttling_policy_v2(self, request):
        """创建流控策略

        当API上线后，系统会默认给每个API提供一个流控策略，API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。 流控策略即限制API在一定长度的时间内，能够允许被访问的最大次数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateRequestThrottlingPolicyV2Response`
        """
        return self.create_request_throttling_policy_v2_with_http_info(request)

    def create_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_request_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_signature_key_v2(self, request):
        """创建签名密钥

        为了保护API的安全性，建议租户为API的访问提供一套保护机制，即租户开放的API，需要对请求来源进行认证，不符合认证的请求直接拒绝访问。
        
        其中，签名密钥就是API安全保护机制的一种。
        
        租户创建一个签名密钥，并将签名密钥与API进行绑定，则API网关在请求这个API时，就会使用绑定的签名密钥对请求参数进行数据加密，生成签名。当租户的后端服务收到请求时，可以校验这个签名，如果签名校验不通过，则该请求不是API网关发出的请求，租户可以拒绝这个请求，从而保证API的安全性，避免API被未知来源的请求攻击。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateSignatureKeyV2Response`
        """
        return self.create_signature_key_v2_with_http_info(request)

    def create_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_signature_key_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_special_throttling_configuration_v2(self, request):
        """创建特殊设置

        流控策略可以限制一段时间内可以访问API的最大次数，也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。
        
        如果想要对某个特定的APP进行特殊设置，例如设置所有APP每分钟的访问次数为500次，但想设置APP1每分钟的访问次数为800次，可以通过在流控策略中设置特殊APP来实现该功能。
        
        为流控策略添加一个特殊设置的对象，可以是APP，也可以是租户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateSpecialThrottlingConfigurationV2Response`
        """
        return self.create_special_throttling_configuration_v2_with_http_info(request)

    def create_special_throttling_configuration_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'create_special_throttling_configuration_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSpecialThrottlingConfigurationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_custom_authorizer_v2(self, request):
        """删除自定义认证

        删除自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteCustomAuthorizerV2Response`
        """
        return self.delete_custom_authorizer_v2_with_http_info(request)

    def delete_custom_authorizer_v2_with_http_info(self, request):
        all_params = ['instance_id', 'authorizer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCustomAuthorizerV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_environment_v2(self, request):
        """删除环境

        删除指定的环境。
        
        该操作将导致此API在指定的环境无法被访问，可能会影响相当一部分应用和用户。请确保已经告知用户，或者确认需要强制下线。
        
        环境上存在已发布的API时，该环境不能被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentV2Response`
        """
        return self.delete_environment_v2_with_http_info(request)

    def delete_environment_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs/{env_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnvironmentV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_environment_variable_v2(self, request):
        """删除变量

        删除指定的环境变量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentVariableV2Response`
        """
        return self.delete_environment_variable_v2_with_http_info(request)

    def delete_environment_variable_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_variable_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_variable_id' in local_var_params:
            path_params['env_variable_id'] = local_var_params['env_variable_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables/{env_variable_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnvironmentVariableV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gateway_response_type_v2(self, request):
        """删除分组指定错误类型的自定义响应配置

        删除分组指定错误类型的自定义响应配置，还原为使用默认值的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseTypeV2Response`
        """
        return self.delete_gateway_response_type_v2_with_http_info(request)

    def delete_gateway_response_type_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'response_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGatewayResponseTypeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gateway_response_v2(self, request):
        """删除分组自定义响应

        删除分组自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseV2Response`
        """
        return self.delete_gateway_response_v2_with_http_info(request)

    def delete_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instances_v2(self, request):
        """删除专享版实例

        删除专享版实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteInstancesV2Response`
        """
        return self.delete_instances_v2_with_http_info(request)

    def delete_instances_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_plugin(self, request):
        """删除插件

        删除插件。
        - 必须先解除API和插件的绑定关系，否则删除报错
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlugin
        :type request: :class:`huaweicloudsdkapig.v2.DeletePluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeletePluginResponse`
        """
        return self.delete_plugin_with_http_info(request)

    def delete_plugin_with_http_info(self, request):
        all_params = ['instance_id', 'plugin_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePluginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_request_throttling_policy_v2(self, request):
        """删除流控策略

        删除指定的流控策略，以及该流控策略与API的所有绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteRequestThrottlingPolicyV2Response`
        """
        return self.delete_request_throttling_policy_v2_with_http_info(request)

    def delete_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_signature_key_v2(self, request):
        """删除签名密钥

        删除指定的签名密钥，删除签名密钥时，其配置的绑定关系会一并删除，相应的签名密钥会失效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteSignatureKeyV2Response`
        """
        return self.delete_signature_key_v2_with_http_info(request)

    def delete_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_id' in local_var_params:
            path_params['sign_id'] = local_var_params['sign_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs/{sign_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_special_throttling_configuration_v2(self, request):
        """删除特殊设置

        删除某个流控策略的某个特殊配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteSpecialThrottlingConfigurationV2Response`
        """
        return self.delete_special_throttling_configuration_v2_with_http_info(request)

    def delete_special_throttling_configuration_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'strategy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']
        if 'strategy_id' in local_var_params:
            path_params['strategy_id'] = local_var_params['strategy_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSpecialThrottlingConfigurationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_api_from_plugin(self, request):
        """解除绑定插件的API

        解除绑定在插件上的API。
        - 解绑及时生效
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachApiFromPlugin
        :type request: :class:`huaweicloudsdkapig.v2.DetachApiFromPluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DetachApiFromPluginResponse`
        """
        return self.detach_api_from_plugin_with_http_info(request)

    def detach_api_from_plugin_with_http_info(self, request):
        all_params = ['instance_id', 'plugin_id', 'detach_api_from_plugin_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/detach',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachApiFromPluginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_plugin_from_api(self, request):
        """解除绑定API的插件

        解除绑定在API上的插件。
        - 解绑及时生效
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachPluginFromApi
        :type request: :class:`huaweicloudsdkapig.v2.DetachPluginFromApiRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DetachPluginFromApiResponse`
        """
        return self.detach_plugin_from_api_with_http_info(request)

    def detach_plugin_from_api_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'detach_plugin_from_api_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/plugins/detach',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachPluginFromApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_certificate_v2(self, request):
        """删除域名证书

        如果域名证书不再需要或者已过期，则可以删除证书内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateCertificateV2Response`
        """
        return self.disassociate_certificate_v2_with_http_info(request)

    def disassociate_certificate_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_domain_v2(self, request):
        """解绑域名

        如果API分组不再需要绑定某个自定义域名，则可以为此API分组解绑此域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateDomainV2Response`
        """
        return self.disassociate_domain_v2_with_http_info(request)

    def disassociate_domain_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateDomainV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_signature_key_v2(self, request):
        """解除绑定

        解除API与签名密钥的绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateSignatureKeyV2Response`
        """
        return self.disassociate_signature_key_v2_with_http_info(request)

    def disassociate_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_bindings_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_bindings_id' in local_var_params:
            path_params['sign_bindings_id'] = local_var_params['sign_bindings_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/{sign_bindings_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_microservice(self, request):
        """导入微服务

        导入微服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportMicroservice
        :type request: :class:`huaweicloudsdkapig.v2.ImportMicroserviceRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ImportMicroserviceResponse`
        """
        return self.import_microservice_with_http_info(request)

    def import_microservice_with_http_info(self, request):
        all_params = ['instance_id', 'import_microservice_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/microservice/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportMicroserviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_attachable_plugins(self, request):
        """查询可绑定当前API的插件

        查询可绑定当前API的插件信息。
        - 支持分页返回
        - 支持插件名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiAttachablePlugins
        :type request: :class:`huaweicloudsdkapig.v2.ListApiAttachablePluginsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiAttachablePluginsResponse`
        """
        return self.list_api_attachable_plugins_with_http_info(request)

    def list_api_attachable_plugins_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'env_id', 'plugin_name', 'plugin_type', 'plugin_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'plugin_type' in local_var_params:
            query_params.append(('plugin_type', local_var_params['plugin_type']))
        if 'plugin_id' in local_var_params:
            query_params.append(('plugin_id', local_var_params['plugin_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/attachable-plugins',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiAttachablePluginsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_attached_plugins(self, request):
        """查询API下绑定的插件

        查询指定API下绑定的插件信息。
        - 用于查询指定API下已经绑定的插件列表信息
        - 支持分页返回
        - 支持插件名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiAttachedPlugins
        :type request: :class:`huaweicloudsdkapig.v2.ListApiAttachedPluginsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiAttachedPluginsResponse`
        """
        return self.list_api_attached_plugins_with_http_info(request)

    def list_api_attached_plugins_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'env_id', 'plugin_name', 'plugin_id', 'env_name', 'plugin_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'plugin_id' in local_var_params:
            query_params.append(('plugin_id', local_var_params['plugin_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))
        if 'plugin_type' in local_var_params:
            query_params.append(('plugin_type', local_var_params['plugin_type']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/attached-plugins',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiAttachedPluginsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_groups_quantities_v2(self, request):
        """查询API分组概况

        查询租户名下的API分组概况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiGroupsQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiGroupsQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiGroupsQuantitiesV2Response`
        """
        return self.list_api_groups_quantities_v2_with_http_info(request)

    def list_api_groups_quantities_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiGroupsQuantitiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_quantities_v2(self, request):
        """查询API概况

        查询租户名下的API概况：已发布到RELEASE环境的API个数，未发布到RELEASE环境的API个数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiQuantitiesV2Response`
        """
        return self.list_api_quantities_v2_with_http_info(request)

    def list_api_quantities_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiQuantitiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_signature_key_v2(self, request):
        """查看签名密钥绑定的API列表

        查询某个签名密钥上已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToSignatureKeyV2Response`
        """
        return self.list_apis_binded_to_signature_key_v2_with_http_info(request)

    def list_apis_binded_to_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id', 'offset', 'limit', 'env_id', 'api_id', 'api_name', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisBindedToSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_not_bound_with_signature_key_v2(self, request):
        """查看签名密钥未绑定的API列表

        查询所有未绑定到该签名密钥上的API列表。需要API已经发布，未发布的API不予展示。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisNotBoundWithSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisNotBoundWithSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisNotBoundWithSignatureKeyV2Response`
        """
        return self.list_apis_not_bound_with_signature_key_v2_with_http_info(request)

    def list_apis_not_bound_with_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id', 'offset', 'limit', 'env_id', 'api_id', 'api_name', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisNotBoundWithSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_quantities_v2(self, request):
        """查询APP概况

        查询租户名下的APP概况：已进行API访问授权的APP个数，未进行API访问授权的APP个数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppQuantitiesV2Response`
        """
        return self.list_app_quantities_v2_with_http_info(request)

    def list_app_quantities_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppQuantitiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_available_zones_v2(self, request):
        """查看可用区信息

        查看可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableZonesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAvailableZonesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAvailableZonesV2Response`
        """
        return self.list_available_zones_v2_with_http_info(request)

    def list_available_zones_v2_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/available-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailableZonesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_custom_authorizers_v2(self, request):
        """查询自定义认证列表

        查询自定义认证列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkapig.v2.ListCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListCustomAuthorizersV2Response`
        """
        return self.list_custom_authorizers_v2_with_http_info(request)

    def list_custom_authorizers_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCustomAuthorizersV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_environment_variables_v2(self, request):
        """查询变量列表

        查询分组下的所有环境变量的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvironmentVariablesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListEnvironmentVariablesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEnvironmentVariablesV2Response`
        """
        return self.list_environment_variables_v2_with_http_info(request)

    def list_environment_variables_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'offset', 'limit', 'env_id', 'variable_name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'variable_name' in local_var_params:
            query_params.append(('variable_name', local_var_params['variable_name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnvironmentVariablesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_environments_v2(self, request):
        """查询环境列表

        查询符合条件的环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvironmentsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListEnvironmentsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEnvironmentsV2Response`
        """
        return self.list_environments_v2_with_http_info(request)

    def list_environments_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnvironmentsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_features_v2(self, request):
        """查看实例特性列表

        查看实例特性列表。注意：实例不支持以下特性的需要联系技术支持升级实例版本。
        
        当前支持的特性列表如下：
        
        特性名称 | 特性描述 | 特性是否可配置|
        --------| :------- | :-------|
        lts | 是否支持shubao访问日志上报功能。| 是 |
        gateway_responses | 是否支持网关自定义响应。| 否 |
        ratelimit | 是否支持自定义流控值。| 是 |
        request_body_size | 是否支持设置请求体大小上限。| 是 |
        backend_timeout | 是否支持配置后端API最大超时时间。| 是 |
        app_token | 是否开启app_token认证方式。| 是 |
        app_api_key | 是否开启app_api_key认证方式。| 是 |
        app_basic | 是否开启app_basic认证方式。| 是 |
        app_secret | 是否支持app_secret认证方式。| 是 |
        app_jwt | 是否支持app_jwt认证方式。| 是 |
        public_key | 是否支持public_key类型的后端签名。| 是 |
        backend_token_allow | 是否支持普通租户透传token到后端。| 是 |
        sign_basic | 签名密钥是否支持basic类型。| 否 |
        multi_auth | API是否支持双重认证方式。| 否 |
        backend_client_certificate | 是否开启后端双向认证。| 是 |
        ssl_ciphers | 是否支持https加密套件。  | 是 |
        route | 是否支持自定义路由。| 否 |
        cors | 是否支持API使用插件功能。| 否 |
        real_ip_from_xff | 是否开启使用xff头作为访问控制、流控策略的源ip生效依据。  | 是 |
        app_route | 是否支持ip访问。| 是 |
        vpc_name_modifiable | 是否支持修改负载通道名称。 | 是 |
        default_group_host_trustlist | DEFAULT分组是否支持配置非本实例IP访问。 | 是 |
        throttle_strategy | 是否支持配置流控算法策略。 | 是 |
        custom_log | 是否支持用户自定义API请求中的HEADER、QUERY、COOKIE参数值打印到日志。 | 是 |
        real_ip_header_getter | 是否开启通过用户自定义的Header获取用户源IP地址。 | 是 |
        policy_cookie_param | 是否开启策略后端条件支持cookie类型。 | 是 |
        app_quota | 是否支持客户端配额策略。 | 否 |
        app_acl | 是否支持流控策略。 | 否 |
        set_resp_headers | 是否支持响应header插件。 | 否 |
        vpc_backup | 是否支持VPC通道的主备配置。 | 否 |
        sign_aes | 签名密钥是否支持AES加密方式。 | 否 |
        kafka_log | 是否支持增删改查kafka日志插件。 | 否 |
        backend_retry_count | 是否支持API配置重试次数。 | 否 |
        policy_sys_param | 策略后端条件来源是否支持系统参数。 | 否 |
        breaker | 是否支持断路器。 | 否 |
        content_type_configurable | 获取API列表的接口返回信息中是否存在API的请求参数类型信息（Content-Type）。 | 否 |
        rate_limit_plugin | 是否支持流控插件。 | 否 |
        breakerv2 | 是否支持断路器，能够实现过载情况下服务能力降级。 | 否 |
        sm_cipher_type | 加密本地敏感数据时，是否支持应用商密加密算法。 | 否 |
        rate_limit_algorithm | 是否支持切换流控算法。 | 否 |
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFeaturesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListFeaturesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListFeaturesV2Response`
        """
        return self.list_features_v2_with_http_info(request)

    def list_features_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/features',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFeaturesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gateway_responses_v2(self, request):
        """查询分组自定义响应列表

        查询分组自定义响应列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGatewayResponsesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListGatewayResponsesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListGatewayResponsesV2Response`
        """
        return self.list_gateway_responses_v2_with_http_info(request)

    def list_gateway_responses_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGatewayResponsesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_configs_v2(self, request):
        """查询租户实例配置列表

        查询租户实例配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceConfigsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListInstanceConfigsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstanceConfigsV2Response`
        """
        return self.list_instance_configs_v2_with_http_info(request)

    def list_instance_configs_v2_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instance/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceConfigsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_tags(self, request):
        """查询单个实例标签

        查询单个实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkapig.v2.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstanceTagsResponse`
        """
        return self.list_instance_tags_with_http_info(request)

    def list_instance_tags_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/instance-tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_v2(self, request):
        """查询专享版实例列表

        查询专享版实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstancesV2Response`
        """
        return self.list_instances_v2_with_http_info(request)

    def list_instances_v2_with_http_info(self, request):
        all_params = ['offset', 'limit', 'instance_id', 'instance_name', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v2/{project_id}/apigw/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_lately_api_statistics_v2(self, request):
        """API统计信息查询-最近一段时间

        根据API的id和最近的一段时间查询API被调用的次数，统计周期为1分钟。查询范围一小时以内，一分钟一个样本，其样本值为一分钟内的累计值。
        &gt; 为了安全起见，在服务器上使用curl命令调用接口查询信息后，需要清理历史操作记录，包括但不限于“~/.bash_history”、“/var/log/messages”（如有）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLatelyApiStatisticsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListLatelyApiStatisticsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListLatelyApiStatisticsV2Response`
        """
        return self.list_lately_api_statistics_v2_with_http_info(request)

    def list_lately_api_statistics_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'duration']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'duration' in local_var_params:
            query_params.append(('duration', local_var_params['duration']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/statistics/api/latest',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLatelyApiStatisticsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_lately_group_statistics_v2(self, request):
        """分组统计信息查询-最近一小时内

        根据API分组的编号查询该分组下所有API被调用的总次数，统计周期为1分钟。查询范围一小时以内，一分钟一个样本，其样本值为一分钟内的累计值。
        &gt; 为了安全起见，在服务器上使用curl命令调用接口查询信息后，需要清理历史操作记录，包括但不限于“~/.bash_history”、“/var/log/messages”（如有）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLatelyGroupStatisticsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListLatelyGroupStatisticsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListLatelyGroupStatisticsV2Response`
        """
        return self.list_lately_group_statistics_v2_with_http_info(request)

    def list_lately_group_statistics_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/statistics/group/latest',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLatelyGroupStatisticsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_metric_data(self, request):
        """查询监控数据

        查询指定时间范围指定指标的指定粒度的监控数据，可以通过参数指定需要查询的数据维度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetricData
        :type request: :class:`huaweicloudsdkapig.v2.ListMetricDataRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListMetricDataResponse`
        """
        return self.list_metric_data_with_http_info(request)

    def list_metric_data_with_http_info(self, request):
        all_params = ['instance_id', 'dim', 'metric_name', '_from', 'to', 'period', 'filter']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dim' in local_var_params:
            query_params.append(('dim', local_var_params['dim']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_plugin_attachable_apis(self, request):
        """查询可绑定当前插件的API

        查询可绑定当前插件的API信息。
        - 支持分页返回
        - 支持API名称模糊查询
        - 支持已绑定其他插件的API查询返回
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPluginAttachableApis
        :type request: :class:`huaweicloudsdkapig.v2.ListPluginAttachableApisRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListPluginAttachableApisResponse`
        """
        return self.list_plugin_attachable_apis_with_http_info(request)

    def list_plugin_attachable_apis_with_http_info(self, request):
        all_params = ['instance_id', 'plugin_id', 'offset', 'limit', 'env_id', 'api_name', 'api_id', 'group_id', 'req_method', 'req_uri']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'req_method' in local_var_params:
            query_params.append(('req_method', local_var_params['req_method']))
        if 'req_uri' in local_var_params:
            query_params.append(('req_uri', local_var_params['req_uri']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/attachable-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPluginAttachableApisResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_plugin_attached_apis(self, request):
        """查询插件下绑定的API

        查询指定插件下绑定的API信息。
        - 用于查询指定插件下已经绑定的API列表信息
        - 支持分页返回
        - 支持API名称模糊查询
        - 绑定关系列表中返回的API在对应的环境中可能已经下线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPluginAttachedApis
        :type request: :class:`huaweicloudsdkapig.v2.ListPluginAttachedApisRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListPluginAttachedApisResponse`
        """
        return self.list_plugin_attached_apis_with_http_info(request)

    def list_plugin_attached_apis_with_http_info(self, request):
        all_params = ['instance_id', 'plugin_id', 'offset', 'limit', 'env_id', 'api_name', 'api_id', 'group_id', 'req_method', 'req_uri']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'req_method' in local_var_params:
            query_params.append(('req_method', local_var_params['req_method']))
        if 'req_uri' in local_var_params:
            query_params.append(('req_uri', local_var_params['req_uri']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/attached-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPluginAttachedApisResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_plugins(self, request):
        """查询插件列表

        查询一组符合条件的API网关插件详情。
        - 支持分页
        - 支持根据插件类型查询
        - 支持根据插件可见范围查询
        - 支持根据插件编码查询
        - 支持根据名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlugins
        :type request: :class:`huaweicloudsdkapig.v2.ListPluginsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListPluginsResponse`
        """
        return self.list_plugins_with_http_info(request)

    def list_plugins_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'plugin_type', 'plugin_scope', 'plugin_id', 'plugin_name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'plugin_type' in local_var_params:
            query_params.append(('plugin_type', local_var_params['plugin_type']))
        if 'plugin_scope' in local_var_params:
            query_params.append(('plugin_scope', local_var_params['plugin_scope']))
        if 'plugin_id' in local_var_params:
            query_params.append(('plugin_id', local_var_params['plugin_id']))
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPluginsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_cofigs_v2(self, request):
        """查询某个实例的租户配置列表

        查询某个实例的租户配置列表，用户可以通过此接口查看各类型资源配置及使用情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectCofigsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListProjectCofigsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListProjectCofigsV2Response`
        """
        return self.list_project_cofigs_v2_with_http_info(request)

    def list_project_cofigs_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/project/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectCofigsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_instance_tags(self, request):
        """查询项目下所有实例标签

        查询项目下所有实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectInstanceTags
        :type request: :class:`huaweicloudsdkapig.v2.ListProjectInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListProjectInstanceTagsResponse`
        """
        return self.list_project_instance_tags_with_http_info(request)

    def list_project_instance_tags_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instance-tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_request_throttling_policy_v2(self, request):
        """查询流控策略列表

        查询所有流控策略的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPolicyV2Response`
        """
        return self.list_request_throttling_policy_v2_with_http_info(request)

    def list_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_signature_keys_binded_to_api_v2(self, request):
        """查看API绑定的签名密钥列表

        查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSignatureKeysBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSignatureKeysBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSignatureKeysBindedToApiV2Response`
        """
        return self.list_signature_keys_binded_to_api_v2_with_http_info(request)

    def list_signature_keys_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'sign_id', 'sign_name', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'sign_name' in local_var_params:
            query_params.append(('sign_name', local_var_params['sign_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/binded-signs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSignatureKeysBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_signature_keys_v2(self, request):
        """查询签名密钥列表

        查询所有签名密钥的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSignatureKeysV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSignatureKeysV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSignatureKeysV2Response`
        """
        return self.list_signature_keys_v2_with_http_info(request)

    def list_signature_keys_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSignatureKeysV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_special_throttling_configurations_v2(self, request):
        """查看特殊设置列表

        查看给流控策略设置的特殊配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSpecialThrottlingConfigurationsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSpecialThrottlingConfigurationsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSpecialThrottlingConfigurationsV2Response`
        """
        return self.list_special_throttling_configurations_v2_with_http_info(request)

    def list_special_throttling_configurations_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'offset', 'limit', 'object_type', 'app_name', 'user']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSpecialThrottlingConfigurationsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_v2(self, request):
        """查询标签列表

        查询标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListTagsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListTagsV2Response`
        """
        return self.list_tags_v2_with_http_info(request)

    def list_tags_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_eip_v2(self, request):
        """实例解绑EIP

        实例解绑EIP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveEipV2
        :type request: :class:`huaweicloudsdkapig.v2.RemoveEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.RemoveEipV2Response`
        """
        return self.remove_eip_v2_with_http_info(request)

    def remove_eip_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/eip',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_engress_eip_v2(self, request):
        """关闭实例公网出口

        关闭实例公网出口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.RemoveEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.RemoveEngressEipV2Response`
        """
        return self.remove_engress_eip_v2_with_http_info(request)

    def remove_engress_eip_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/nat-eip',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveEngressEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_custom_authorizers_v2(self, request):
        """查看自定义认证详情

        查看自定义认证详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCustomAuthorizersV2Response`
        """
        return self.show_details_of_custom_authorizers_v2_with_http_info(request)

    def show_details_of_custom_authorizers_v2_with_http_info(self, request):
        all_params = ['instance_id', 'authorizer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfCustomAuthorizersV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_domain_name_certificate_v2(self, request):
        """查看域名证书

        查看域名下绑定的证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfDomainNameCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfDomainNameCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfDomainNameCertificateV2Response`
        """
        return self.show_details_of_domain_name_certificate_v2_with_http_info(request)

    def show_details_of_domain_name_certificate_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfDomainNameCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_environment_variable_v2(self, request):
        """查看变量详情

        查看指定的环境变量的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfEnvironmentVariableV2Response`
        """
        return self.show_details_of_environment_variable_v2_with_http_info(request)

    def show_details_of_environment_variable_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_variable_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_variable_id' in local_var_params:
            path_params['env_variable_id'] = local_var_params['env_variable_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/env-variables/{env_variable_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfEnvironmentVariableV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_gateway_response_type_v2(self, request):
        """查看分组下指定错误类型的自定义响应

        查看分组下指定错误类型的自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseTypeV2Response`
        """
        return self.show_details_of_gateway_response_type_v2_with_http_info(request)

    def show_details_of_gateway_response_type_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'response_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfGatewayResponseTypeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_gateway_response_v2(self, request):
        """查询分组自定义响应详情

        查询分组自定义响应详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseV2Response`
        """
        return self.show_details_of_gateway_response_v2_with_http_info(request)

    def show_details_of_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_instance_progress_v2(self, request):
        """查看专享版实例创建进度

        查看专享版实例创建进度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfInstanceProgressV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceProgressV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceProgressV2Response`
        """
        return self.show_details_of_instance_progress_v2_with_http_info(request)

    def show_details_of_instance_progress_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfInstanceProgressV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_instance_v2(self, request):
        """查看专享版实例详情

        查看专享版实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceV2Response`
        """
        return self.show_details_of_instance_v2_with_http_info(request)

    def show_details_of_instance_v2_with_http_info(self, request):
        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_request_throttling_policy_v2(self, request):
        """查看流控策略详情

        查看指定流控策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfRequestThrottlingPolicyV2Response`
        """
        return self.show_details_of_request_throttling_policy_v2_with_http_info(request)

    def show_details_of_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_plugin(self, request):
        """查询插件详情

        查询插件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlugin
        :type request: :class:`huaweicloudsdkapig.v2.ShowPluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowPluginResponse`
        """
        return self.show_plugin_with_http_info(request)

    def show_plugin_with_http_info(self, request):
        all_params = ['instance_id', 'plugin_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPluginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_custom_authorizer_v2(self, request):
        """修改自定义认证

        修改自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateCustomAuthorizerV2Response`
        """
        return self.update_custom_authorizer_v2_with_http_info(request)

    def update_custom_authorizer_v2_with_http_info(self, request):
        all_params = ['instance_id', 'authorizer_id', 'update_custom_authorizer_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCustomAuthorizerV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_v2(self, request):
        """修改域名

        修改绑定的域名所对应的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateDomainV2Response`
        """
        return self.update_domain_v2_with_http_info(request)

    def update_domain_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'update_domain_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_engress_eip_v2(self, request):
        """更新实例出公网带宽

        更新实例出公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateEngressEipV2Response`
        """
        return self.update_engress_eip_v2_with_http_info(request)

    def update_engress_eip_v2_with_http_info(self, request):
        all_params = ['instance_id', 'update_engress_eip_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/nat-eip',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEngressEipV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_environment_v2(self, request):
        """修改环境

        修改指定环境的信息。其中可修改的属性为：name、remark，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentV2Response`
        """
        return self.update_environment_v2_with_http_info(request)

    def update_environment_v2_with_http_info(self, request):
        all_params = ['instance_id', 'env_id', 'update_environment_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/envs/{env_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEnvironmentV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gateway_response_type_v2(self, request):
        """修改分组下指定错误类型的自定义响应

        修改分组下指定错误类型的自定义响应。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseTypeV2Response`
        """
        return self.update_gateway_response_type_v2_with_http_info(request)

    def update_gateway_response_type_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'response_type', 'update_gateway_response_type_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGatewayResponseTypeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gateway_response_v2(self, request):
        """修改分组自定义响应

        修改分组自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseV2Response`
        """
        return self.update_gateway_response_v2_with_http_info(request)

    def update_gateway_response_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'response_id', 'update_gateway_response_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGatewayResponseV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_v2(self, request):
        """更新专享版实例

        更新专享版实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateInstanceV2Response`
        """
        return self.update_instance_v2_with_http_info(request)

    def update_instance_v2_with_http_info(self, request):
        all_params = ['instance_id', 'update_instance_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_plugin(self, request):
        """修改插件

        修改插件信息。
        - 插件不允许重名
        - 插件不支持修改类型和可见范围
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlugin
        :type request: :class:`huaweicloudsdkapig.v2.UpdatePluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdatePluginResponse`
        """
        return self.update_plugin_with_http_info(request)

    def update_plugin_with_http_info(self, request):
        all_params = ['instance_id', 'plugin_id', 'update_plugin_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePluginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_request_throttling_policy_v2(self, request):
        """修改流控策略

        修改指定流控策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateRequestThrottlingPolicyV2Response`
        """
        return self.update_request_throttling_policy_v2_with_http_info(request)

    def update_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'update_request_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_signature_key_v2(self, request):
        """修改签名密钥

        修改指定签名密钥的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateSignatureKeyV2Response`
        """
        return self.update_signature_key_v2_with_http_info(request)

    def update_signature_key_v2_with_http_info(self, request):
        all_params = ['instance_id', 'sign_id', 'update_signature_key_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_id' in local_var_params:
            path_params['sign_id'] = local_var_params['sign_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/signs/{sign_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSignatureKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_special_throttling_configuration_v2(self, request):
        """修改特殊设置

        修改某个流控策略下的某个特殊设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateSpecialThrottlingConfigurationV2Response`
        """
        return self.update_special_throttling_configuration_v2_with_http_info(request)

    def update_special_throttling_configuration_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'strategy_id', 'update_special_throttling_configuration_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']
        if 'strategy_id' in local_var_params:
            path_params['strategy_id'] = local_var_params['strategy_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSpecialThrottlingConfigurationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_acl_v2(self, request):
        """批量删除ACL策略

        批量删除指定的多个ACL策略。
        
        删除ACL策略时，如果存在ACL策略与API绑定关系，则无法删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAclV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDeleteAclV2Response`
        """
        return self.batch_delete_acl_v2_with_http_info(request)

    def batch_delete_acl_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_delete_acl_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAclV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_acl_strategy_v2(self, request):
        """创建ACL策略

        增加一个ACL策略，策略类型通过字段acl_type来确定（permit或者deny），限制的对象的类型可以为IP或者DOMAIN，这里的DOMAIN对应的acl_value的值为租户名称，而非“www.exampleDomain.com\&quot;之类的网络域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAclStrategyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAclStrategyV2Response`
        """
        return self.create_acl_strategy_v2_with_http_info(request)

    def create_acl_strategy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_acl_strategy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAclStrategyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_acl_v2(self, request):
        """删除ACL策略

        删除指定的ACL策略， 如果存在api与该ACL策略的绑定关系，则无法删除
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAclV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAclV2Response`
        """
        return self.delete_acl_v2_with_http_info(request)

    def delete_acl_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAclV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_acl_strategies_v2(self, request):
        """查看ACL策略列表

        查询所有的ACL策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAclStrategiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAclStrategiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAclStrategiesV2Response`
        """
        return self.list_acl_strategies_v2_with_http_info(request)

    def list_acl_strategies_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'acl_type', 'entity_type', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'acl_type' in local_var_params:
            query_params.append(('acl_type', local_var_params['acl_type']))
        if 'entity_type' in local_var_params:
            query_params.append(('entity_type', local_var_params['entity_type']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAclStrategiesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_acl_policy_v2(self, request):
        """查看ACL策略详情

        查询指定ACL策略的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAclPolicyV2Response`
        """
        return self.show_details_of_acl_policy_v2_with_http_info(request)

    def show_details_of_acl_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfAclPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_acl_strategy_v2(self, request):
        """修改ACL策略

        修改指定的ACL策略，其中可修改的属性为：acl_name、acl_type、acl_value，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclStrategyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAclStrategyV2Response`
        """
        return self.update_acl_strategy_v2_with_http_info(request)

    def update_acl_strategy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id', 'update_acl_strategy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAclStrategyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_request_throttling_policy_v2(self, request):
        """绑定流控策略

        将流控策略应用于API，则所有对该API的访问将会受到该流控策略的限制。
        
        当一定时间内的访问次数超过流控策略设置的API最大访问次数限制后，后续的访问将会被拒绝，从而能够较好的保护后端API免受异常流量的冲击，保障服务的稳定运行。
        
        为指定的API绑定流控策略，绑定时，需要指定在哪个环境上生效。同一个API发布到不同的环境可以绑定不同的流控策略；一个API在发布到特定环境后只能绑定一个默认的流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateRequestThrottlingPolicyV2Response`
        """
        return self.associate_request_throttling_policy_v2_with_http_info(request)

    def associate_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'associate_request_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_disassociate_throttling_policy_v2(self, request):
        """批量解绑流控策略

        批量解除API与流控策略的绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisassociateThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisassociateThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisassociateThrottlingPolicyV2Response`
        """
        return self.batch_disassociate_throttling_policy_v2_with_http_info(request)

    def batch_disassociate_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_disassociate_throttling_policy_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDisassociateThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_publish_or_offline_api_v2(self, request):
        """批量发布或下线API

        将多个API发布到一个指定的环境，或将多个API从指定的环境下线。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchPublishOrOfflineApiV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchPublishOrOfflineApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchPublishOrOfflineApiV2Response`
        """
        return self.batch_publish_or_offline_api_v2_with_http_info(request)

    def batch_publish_or_offline_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_publish_or_offline_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchPublishOrOfflineApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_api_version_v2(self, request):
        """切换API版本

        API每次发布时，会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。
        
        多个版本之间可以进行随意切换。但一个API在一个环境上，只能有一个版本生效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeApiVersionV2
        :type request: :class:`huaweicloudsdkapig.v2.ChangeApiVersionV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ChangeApiVersionV2Response`
        """
        return self.change_api_version_v2_with_http_info(request)

    def change_api_version_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'change_api_version_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/publish/{api_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeApiVersionV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_api_group_v2(self, request):
        """创建API分组

        API分组是API的管理单元，一个API分组等同于一个服务入口，创建API分组时，返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiGroupV2Response`
        """
        return self.create_api_group_v2_with_http_info(request)

    def create_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_api_group_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_api_v2(self, request):
        """注册API

        添加一个API，API即一个服务接口，具体的服务能力。
        
        API分为两部分，第一部分为面向API使用者的API接口，定义了使用者如何调用这个API。第二部分面向API提供者，由API提供者定义这个API的真实的后端情况，定义了API网关如何去访问真实的后端服务。API的真实后端服务目前支持三种类型：传统的HTTP/HTTPS形式的web后端、函数工作流、MOCK。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApiV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiV2Response`
        """
        return self.create_api_v2_with_http_info(request)

    def create_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_or_delete_publish_record_for_api_v2(self, request):
        """发布或下线API

        对API进行发布或下线。
        
        发布操作是将一个指定的API发布到一个指定的环境，API只有发布后，才能够被调用，且只能在该环境上才能被调用。未发布的API无法被调用。
        
        下线操作是将API从某个已发布的环境上下线，下线后，API将无法再被调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrDeletePublishRecordForApiV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateOrDeletePublishRecordForApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateOrDeletePublishRecordForApiV2Response`
        """
        return self.create_or_delete_publish_record_for_api_v2_with_http_info(request)

    def create_or_delete_publish_record_for_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_or_delete_publish_record_for_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrDeletePublishRecordForApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def debug_api_v2(self, request):
        """调试API

        调试一个API在指定运行环境下的定义，接口调用者需要具有操作该API的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DebugApiV2
        :type request: :class:`huaweicloudsdkapig.v2.DebugApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DebugApiV2Response`
        """
        return self.debug_api_v2_with_http_info(request)

    def debug_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'debug_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/debug/{api_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DebugApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_by_version_id_v2(self, request):
        """根据版本编号下线API

        对某个生效中的API版本进行下线操作，下线后，API在该版本生效的环境中将不再能够被调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApiByVersionIdV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiByVersionIdV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiByVersionIdV2Response`
        """
        return self.delete_api_by_version_id_v2_with_http_info(request)

    def delete_api_by_version_id_v2_with_http_info(self, request):
        all_params = ['instance_id', 'version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/versions/{version_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApiByVersionIdV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_group_v2(self, request):
        """删除API分组

        删除指定的API分组。
        删除API分组前，要先下线并删除分组下的所有API。
        删除时，会一并删除直接或间接关联到该分组下的所有资源，包括独立域名、SSL证书信息等等。并会将外部域名与子域名的绑定关系进行解除（取决于域名cname方式）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiGroupV2Response`
        """
        return self.delete_api_group_v2_with_http_info(request)

    def delete_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_v2(self, request):
        """删除API

        删除指定的API。
        
        删除API时，会删除该API所有相关的资源信息或绑定关系，如API的发布记录，绑定的后端服务，对APP的授权信息等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApiV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiV2Response`
        """
        return self.delete_api_v2_with_http_info(request)

    def delete_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_request_throttling_policy_v2(self, request):
        """解除API与流控策略的绑定关系

        解除API与流控策略的绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateRequestThrottlingPolicyV2Response`
        """
        return self.disassociate_request_throttling_policy_v2_with_http_info(request)

    def disassociate_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_binding_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_binding_id' in local_var_params:
            path_params['throttle_binding_id'] = local_var_params['throttle_binding_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/{throttle_binding_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_groups_v2(self, request):
        """查询分组列表

        查询API分组列表。
        
        如果是租户操作，则查询该租户下所有的分组；如果是管理员权限帐号操作，则查询的是所有租户的分组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiGroupsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiGroupsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiGroupsV2Response`
        """
        return self.list_api_groups_v2_with_http_info(request)

    def list_api_groups_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiGroupsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_runtime_definition_v2(self, request):
        """查询API运行时定义

        查看指定的API在指定的环境上的运行时定义，默认查询RELEASE环境上的运行时定义。
        
        API的定义分为临时定义和运行时定义，分别代表如下含义：
        - 临时定义：API在编辑中的定义，表示用户最后一次编辑后的API的状态
        - 运行时定义：API在发布到某个环境时，对发布时的API的临时定义进行快照，固化出来的API的状态。
        
        访问某个环境上的API，其实访问的就是其运行时的定义
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiRuntimeDefinitionV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiRuntimeDefinitionV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiRuntimeDefinitionV2Response`
        """
        return self.list_api_runtime_definition_v2_with_http_info(request)

    def list_api_runtime_definition_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/runtime/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiRuntimeDefinitionV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_version_detail_v2(self, request):
        """查看版本详情

        查询某个指定的版本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersionDetailV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiVersionDetailV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiVersionDetailV2Response`
        """
        return self.list_api_version_detail_v2_with_http_info(request)

    def list_api_version_detail_v2_with_http_info(self, request):
        all_params = ['instance_id', 'version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/versions/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiVersionDetailV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions_v2(self, request):
        """查询API历史版本列表

        查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiVersionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiVersionsV2Response`
        """
        return self.list_api_versions_v2_with_http_info(request)

    def list_api_versions_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'env_id', 'env_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/publish/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiVersionsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_request_throttling_policy_v2(self, request):
        """查看流控策略绑定的API列表

        查询某个流控策略上已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToRequestThrottlingPolicyV2Response`
        """
        return self.list_apis_binded_to_request_throttling_policy_v2_with_http_info(request)

    def list_apis_binded_to_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'offset', 'limit', 'env_id', 'group_id', 'api_id', 'api_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisBindedToRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_unbinded_to_request_throttling_policy_v2(self, request):
        """查看流控策略未绑定的API列表

        查询所有未绑定到该流控策略上的自有API列表。需要API已经发布，未发布的API不予展示。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisUnbindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToRequestThrottlingPolicyV2Response`
        """
        return self.list_apis_unbinded_to_request_throttling_policy_v2_with_http_info(request)

    def list_apis_unbinded_to_request_throttling_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'throttle_id', 'offset', 'limit', 'env_id', 'group_id', 'api_id', 'api_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisUnbindedToRequestThrottlingPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_v2(self, request):
        """查询API列表

        查看API列表，返回API详细信息、发布信息等，但不能查看到后端服务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisV2Response`
        """
        return self.list_apis_v2_with_http_info(request)

    def list_apis_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'group_id', 'req_protocol', 'req_method', 'req_uri', 'auth_type', 'env_id', 'type', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'req_protocol' in local_var_params:
            query_params.append(('req_protocol', local_var_params['req_protocol']))
        if 'req_method' in local_var_params:
            query_params.append(('req_method', local_var_params['req_method']))
        if 'req_uri' in local_var_params:
            query_params.append(('req_uri', local_var_params['req_uri']))
        if 'auth_type' in local_var_params:
            query_params.append(('auth_type', local_var_params['auth_type']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_request_throttling_policies_binded_to_api_v2(self, request):
        """查看API绑定的流控策略列表

        查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRequestThrottlingPoliciesBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPoliciesBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPoliciesBindedToApiV2Response`
        """
        return self.list_request_throttling_policies_binded_to_api_v2_with_http_info(request)

    def list_request_throttling_policies_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'throttle_id', 'throttle_name', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'throttle_name' in local_var_params:
            query_params.append(('throttle_name', local_var_params['throttle_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/binded-throttles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRequestThrottlingPoliciesBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_api_group_v2(self, request):
        """查询分组详情

        查询指定分组的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiGroupV2Response`
        """
        return self.show_details_of_api_group_v2_with_http_info(request)

    def show_details_of_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_api_v2(self, request):
        """查询API详情

        查看指定的API的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiV2Response`
        """
        return self.show_details_of_api_v2_with_http_info(request)

    def show_details_of_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_api_group_v2(self, request):
        """修改API分组

        修改API分组属性。其中name和remark可修改，其他属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateApiGroupV2Response`
        """
        return self.update_api_group_v2_with_http_info(request)

    def update_api_group_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'update_api_group_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateApiGroupV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_api_v2(self, request):
        """修改API

        修改指定API的信息，包括后端服务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApiV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateApiV2Response`
        """
        return self.update_api_v2_with_http_info(request)

    def update_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'update_api_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_api_acl_binding_v2(self, request):
        """批量解除API与ACL策略的绑定

        批量解除API与ACL策略的绑定
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDeleteApiAclBindingV2Response`
        """
        return self.batch_delete_api_acl_binding_v2_with_http_info(request)

    def batch_delete_api_acl_binding_v2_with_http_info(self, request):
        all_params = ['instance_id', 'action', 'batch_delete_api_acl_binding_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteApiAclBindingV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_api_acl_binding_v2(self, request):
        """将API与ACL策略进行绑定

        将API与ACL策略进行绑定。
        
        同一个API发布到不同的环境可以绑定不同的ACL策略；一个API在发布到特定环境后只能绑定一个同一种类型的ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiAclBindingV2Response`
        """
        return self.create_api_acl_binding_v2_with_http_info(request)

    def create_api_acl_binding_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_api_acl_binding_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateApiAclBindingV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api_acl_binding_v2(self, request):
        """解除API与ACL策略的绑定

        解除某条API与ACL策略的绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiAclBindingV2Response`
        """
        return self.delete_api_acl_binding_v2_with_http_info(request)

    def delete_api_acl_binding_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_bindings_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_bindings_id' in local_var_params:
            path_params['acl_bindings_id'] = local_var_params['acl_bindings_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/{acl_bindings_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApiAclBindingV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_acl_policy_binded_to_api_v2(self, request):
        """查看API绑定的ACL策略列表

        查看API绑定的ACL策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAclPolicyBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAclPolicyBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAclPolicyBindedToApiV2Response`
        """
        return self.list_acl_policy_binded_to_api_v2_with_http_info(request)

    def list_acl_policy_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'api_id', 'offset', 'limit', 'env_id', 'env_name', 'acl_id', 'acl_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'acl_name' in local_var_params:
            query_params.append(('acl_name', local_var_params['acl_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/binded-acls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAclPolicyBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_acl_policy_v2(self, request):
        """查看ACL策略绑定的API列表

        查看ACL策略绑定的API列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToAclPolicyV2Response`
        """
        return self.list_apis_binded_to_acl_policy_v2_with_http_info(request)

    def list_apis_binded_to_acl_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id', 'offset', 'limit', 'api_id', 'api_name', 'env_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisBindedToAclPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_unbinded_to_acl_policy_v2(self, request):
        """查看ACL策略未绑定的API列表

        查看ACL策略未绑定的API列表，需要API已发布
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisUnbindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAclPolicyV2Response`
        """
        return self.list_apis_unbinded_to_acl_policy_v2_with_http_info(request)

    def list_apis_unbinded_to_acl_policy_v2_with_http_info(self, request):
        all_params = ['instance_id', 'acl_id', 'offset', 'limit', 'api_id', 'api_name', 'env_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisUnbindedToAclPolicyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def canceling_authorization_v2(self, request):
        """解除授权

        解除API对APP的授权关系。解除授权后，APP将不再能够调用该API。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelingAuthorizationV2
        :type request: :class:`huaweicloudsdkapig.v2.CancelingAuthorizationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CancelingAuthorizationV2Response`
        """
        return self.canceling_authorization_v2_with_http_info(request)

    def canceling_authorization_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_auth_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_auth_id' in local_var_params:
            path_params['app_auth_id'] = local_var_params['app_auth_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/{app_auth_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelingAuthorizationV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_app_v2(self, request):
        """校验APP

        校验app是否存在，非APP所有者可以调用该接口校验APP是否真实存在。这个接口只展示app的基本信息id 、name、 remark，其他信息不显示。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckAppV2
        :type request: :class:`huaweicloudsdkapig.v2.CheckAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CheckAppV2Response`
        """
        return self.check_app_v2_with_http_info(request)

    def check_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/validation/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_an_app_v2(self, request):
        """创建APP

        APP即应用，是一个可以访问API的身份标识。将API授权给APP后，APP即可调用API。
        创建一个APP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAnAppV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAnAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAnAppV2Response`
        """
        return self.create_an_app_v2_with_http_info(request)

    def create_an_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_an_app_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAnAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_code_auto_v2(self, request):
        """自动生成APP Code

        创建App Code时，可以不指定具体值，由后台自动生成随机字符串填充。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAppCodeAutoV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAppCodeAutoV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAppCodeAutoV2Response`
        """
        return self.create_app_code_auto_v2_with_http_info(request)

    def create_app_code_auto_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAppCodeAutoV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_code_v2(self, request):
        """创建APP Code

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAppCodeV2Response`
        """
        return self.create_app_code_v2_with_http_info(request)

    def create_app_code_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'create_app_code_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAppCodeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_authorizing_apps_v2(self, request):
        """APP授权

        APP创建成功后，还不能访问API，如果想要访问某个环境上的API，需要将该API在该环境上授权给APP。授权成功后，APP即可访问该环境上的这个API。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuthorizingAppsV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAuthorizingAppsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAuthorizingAppsV2Response`
        """
        return self.create_authorizing_apps_v2_with_http_info(request)

    def create_authorizing_apps_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_authorizing_apps_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAuthorizingAppsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app_code_v2(self, request):
        """删除APP Code

        删除App Code，App Code删除后，将无法再通过简易认证访问对应的API。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppCodeV2Response`
        """
        return self.delete_app_code_v2_with_http_info(request)

    def delete_app_code_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'app_code_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_code_id' in local_var_params:
            path_params['app_code_id'] = local_var_params['app_code_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAppCodeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app_v2(self, request):
        """删除APP

        删除指定的APP。
        APP删除后，将无法再调用任何API[；其中，云商店自动创建的APP无法被删除](tag:hws)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAppV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppV2Response`
        """
        return self.delete_app_v2_with_http_info(request)

    def delete_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_binded_to_app_v2(self, request):
        """查看APP已绑定的API列表

        查询APP已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisBindedToAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToAppV2Response`
        """
        return self.list_apis_binded_to_app_v2_with_http_info(request)

    def list_apis_binded_to_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'offset', 'limit', 'api_id', 'api_name', 'group_id', 'group_name', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/binded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisBindedToAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_unbinded_to_app_v2(self, request):
        """查看APP未绑定的API列表

        查询指定环境上某个APP未绑定的API列表[，包括自有API和从云商店购买的API](tag:hws)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisUnbindedToAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAppV2Response`
        """
        return self.list_apis_unbinded_to_app_v2_with_http_info(request)

    def list_apis_unbinded_to_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'env_id', 'offset', 'limit', 'group_id', 'api_id', 'api_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/unbinded-apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisUnbindedToAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_codes_v2(self, request):
        """查询APP Code列表

        查询App Code列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppCodesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppCodesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppCodesV2Response`
        """
        return self.list_app_codes_v2_with_http_info(request)

    def list_app_codes_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppCodesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps_binded_to_api_v2(self, request):
        """查看API已绑定的APP列表

        查询API绑定的APP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppsBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppsBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppsBindedToApiV2Response`
        """
        return self.list_apps_binded_to_api_v2_with_http_info(request)

    def list_apps_binded_to_api_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'api_id', 'app_name', 'app_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/app-auths/binded-apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppsBindedToApiV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps_v2(self, request):
        """查询APP列表

        查询APP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppsV2Response`
        """
        return self.list_apps_v2_with_http_info(request)

    def list_apps_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'status', 'app_key', 'creator', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'app_key' in local_var_params:
            query_params.append(('app_key', local_var_params['app_key']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resetting_app_secret_v2(self, request):
        """重置密钥

        重置指定APP的密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResettingAppSecretV2
        :type request: :class:`huaweicloudsdkapig.v2.ResettingAppSecretV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ResettingAppSecretV2Response`
        """
        return self.resetting_app_secret_v2_with_http_info(request)

    def resetting_app_secret_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'resetting_app_secret_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/secret/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResettingAppSecretV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_app_code_v2(self, request):
        """查看APP Code详情

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppCodeV2Response`
        """
        return self.show_details_of_app_code_v2_with_http_info(request)

    def show_details_of_app_code_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'app_code_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_code_id' in local_var_params:
            path_params['app_code_id'] = local_var_params['app_code_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfAppCodeV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_app_v2(self, request):
        """查看APP详情

        查看指定APP的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppV2Response`
        """
        return self.show_details_of_app_v2_with_http_info(request)

    def show_details_of_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app_v2(self, request):
        """修改APP

        修改指定APP的信息。其中可修改的属性为：name、remark，当支持用户自定义key和secret的开关开启时，app_key和app_secret也支持修改，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAppV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAppV2Response`
        """
        return self.update_app_v2_with_http_info(request)

    def update_app_v2_with_http_info(self, request):
        all_params = ['instance_id', 'app_id', 'update_app_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAppV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_api_definitions_v2(self, request):
        """导出API

        导出分组下API的定义信息。导出文件内容符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsV2Response`
        """
        return self.export_api_definitions_v2_with_http_info(request)

    def export_api_definitions_v2_with_http_info(self, request):
        all_params = ['instance_id', 'export_api_definitions_v2_request_body', 'oas_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'oas_version' in local_var_params:
            query_params.append(('oas_version', local_var_params['oas_version']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/openapi/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportApiDefinitionsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_api_definitions_v2(self, request):
        """导入API

        导入API。导入文件内容需要符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsV2Response`
        """
        return self.import_api_definitions_v2_with_http_info(request)

    def import_api_definitions_v2_with_http_info(self, request):
        all_params = ['instance_id', 'file_name', 'is_create_group', 'group_id', 'extend_mode', 'simple_mode', 'mock_mode', 'api_mode']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'is_create_group' in local_var_params:
            form_params['is_create_group'] = local_var_params['is_create_group']
        if 'group_id' in local_var_params:
            form_params['group_id'] = local_var_params['group_id']
        if 'extend_mode' in local_var_params:
            form_params['extend_mode'] = local_var_params['extend_mode']
        if 'simple_mode' in local_var_params:
            form_params['simple_mode'] = local_var_params['simple_mode']
        if 'mock_mode' in local_var_params:
            form_params['mock_mode'] = local_var_params['mock_mode']
        if 'api_mode' in local_var_params:
            form_params['api_mode'] = local_var_params['api_mode']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/openapi/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportApiDefinitionsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_associate_certs_v2(self, request):
        """域名绑定SSL证书

        域名绑定SSL证书。目前暂时仅支持单个绑定，请求体当中的certificate_ids里面有且只能有一个证书ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAssociateCertsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchAssociateCertsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchAssociateCertsV2Response`
        """
        return self.batch_associate_certs_v2_with_http_info(request)

    def batch_associate_certs_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'batch_associate_certs_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificates/attach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAssociateCertsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_associate_domains_v2(self, request):
        """SSL证书绑定域名

        SSL证书绑定域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAssociateDomainsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchAssociateDomainsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchAssociateDomainsV2Response`
        """
        return self.batch_associate_domains_v2_with_http_info(request)

    def batch_associate_domains_v2_with_http_info(self, request):
        all_params = ['certificate_id', 'batch_associate_domains_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/certificates/{certificate_id}/domains/attach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAssociateDomainsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_disassociate_certs_v2(self, request):
        """域名解绑SSL证书

        域名解绑SSL证书。目前暂时仅支持单个解绑，请求体当中的certificate_ids里面有且只能有一个证书ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisassociateCertsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisassociateCertsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisassociateCertsV2Response`
        """
        return self.batch_disassociate_certs_v2_with_http_info(request)

    def batch_disassociate_certs_v2_with_http_info(self, request):
        all_params = ['instance_id', 'group_id', 'domain_id', 'batch_disassociate_certs_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificates/detach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDisassociateCertsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_disassociate_domains_v2(self, request):
        """SSL证书解绑域名

        SSL证书解绑域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisassociateDomainsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisassociateDomainsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisassociateDomainsV2Response`
        """
        return self.batch_disassociate_domains_v2_with_http_info(request)

    def batch_disassociate_domains_v2_with_http_info(self, request):
        all_params = ['certificate_id', 'batch_disassociate_domains_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/certificates/{certificate_id}/domains/detach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDisassociateDomainsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_certificate_v2(self, request):
        """创建SSL证书

        创建SSL证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateCertificateV2Response`
        """
        return self.create_certificate_v2_with_http_info(request)

    def create_certificate_v2_with_http_info(self, request):
        all_params = ['create_certificate_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/apigw/certificates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_certificate_v2(self, request):
        """删除SSL证书

        删除ssl证书接口，删除时只有没有关联域名的证书才能被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteCertificateV2Response`
        """
        return self.delete_certificate_v2_with_http_info(request)

    def delete_certificate_v2_with_http_info(self, request):
        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/certificates/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_attached_domains_v2(self, request):
        """获取SSL证书已绑定域名列表

        获取SSL证书已绑定域名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttachedDomainsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAttachedDomainsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAttachedDomainsV2Response`
        """
        return self.list_attached_domains_v2_with_http_info(request)

    def list_attached_domains_v2_with_http_info(self, request):
        all_params = ['certificate_id', 'offset', 'limit', 'url_domain']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'url_domain' in local_var_params:
            query_params.append(('url_domain', local_var_params['url_domain']))

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
            resource_path='/v2/{project_id}/apigw/certificates/{certificate_id}/attached-domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAttachedDomainsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificates_v2(self, request):
        """获取SSL证书列表

        获取SSL证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificatesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListCertificatesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListCertificatesV2Response`
        """
        return self.list_certificates_v2_with_http_info(request)

    def list_certificates_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'name', 'common_name', 'signature_algorithm', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'common_name' in local_var_params:
            query_params.append(('common_name', local_var_params['common_name']))
        if 'signature_algorithm' in local_var_params:
            query_params.append(('signature_algorithm', local_var_params['signature_algorithm']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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
            resource_path='/v2/{project_id}/apigw/certificates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertificatesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_certificate_v2(self, request):
        """查看证书详情

        查看证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCertificateV2Response`
        """
        return self.show_details_of_certificate_v2_with_http_info(request)

    def show_details_of_certificate_v2_with_http_info(self, request):
        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/certificates/{certificate_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_certificate_v2(self, request):
        """修改SSL证书

        修改SSL证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateCertificateV2Response`
        """
        return self.update_certificate_v2_with_http_info(request)

    def update_certificate_v2_with_http_info(self, request):
        all_params = ['certificate_id', 'update_certificate_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v2/{project_id}/apigw/certificates/{certificate_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCertificateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def adding_backend_instances_v2(self, request):
        """添加或更新后端实例

        为指定的VPC通道添加后端实例
        
        若指定地址的后端实例已存在，则更新对应后端实例信息。若请求体中包含多个重复地址的后端实例定义，则使用第一个定义。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddingBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.AddingBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddingBackendInstancesV2Response`
        """
        return self.adding_backend_instances_v2_with_http_info(request)

    def adding_backend_instances_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'adding_backend_instances_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddingBackendInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_disable_members(self, request):
        """批量修改后端服务器状态不可用

        批量修改后端服务器状态不可用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisableMembers
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisableMembersRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisableMembersResponse`
        """
        return self.batch_disable_members_with_http_info(request)

    def batch_disable_members_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'batch_disable_members_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/batch-disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDisableMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_enable_members(self, request):
        """批量修改后端服务器状态可用

        批量修改后端服务器状态可用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchEnableMembers
        :type request: :class:`huaweicloudsdkapig.v2.BatchEnableMembersRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchEnableMembersResponse`
        """
        return self.batch_enable_members_with_http_info(request)

    def batch_enable_members_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'batch_enable_members_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/batch-enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchEnableMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_member_group(self, request):
        """添加或更新VPC通道后端服务器组

        在APIG中创建VPC通道后端服务器组，VPC通道后端实例可以选择是否关联后端实例服务器组，以便管理后端服务器节点。
        
        若指定名称的后端服务器组已存在，则更新对应后端服务器组信息。若请求体中包含多个重复名称的后端服务器定义，则使用第一个定义。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.CreateMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateMemberGroupResponse`
        """
        return self.create_member_group_with_http_info(request)

    def create_member_group_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'create_member_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMemberGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_channel_v2(self, request):
        """创建VPC通道

        在API网关中创建连接私有VPC资源的通道，并在创建API时将后端节点配置为使用这些VPC通道，以便API网关直接访问私有VPC资源。
        &gt; 每个用户最多创建30个VPC通道。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateVpcChannelV2Response`
        """
        return self.create_vpc_channel_v2_with_http_info(request)

    def create_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'create_vpc_channel_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcChannelV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_backend_instance_v2(self, request):
        """删除后端实例

        删除指定VPC通道中的后端实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBackendInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteBackendInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteBackendInstanceV2Response`
        """
        return self.delete_backend_instance_v2_with_http_info(request)

    def delete_backend_instance_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBackendInstanceV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_member_group(self, request):
        """删除VPC通道后端服务器组

        删除指定的VPC通道后端服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.DeleteMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteMemberGroupResponse`
        """
        return self.delete_member_group_with_http_info(request)

    def delete_member_group_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'member_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_group_id' in local_var_params:
            path_params['member_group_id'] = local_var_params['member_group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMemberGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_channel_v2(self, request):
        """删除VPC通道

        删除指定的VPC通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteVpcChannelV2Response`
        """
        return self.delete_vpc_channel_v2_with_http_info(request)

    def delete_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcChannelV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backend_instances_v2(self, request):
        """查看后端实例列表

        查看指定VPC通道的后端实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListBackendInstancesV2Response`
        """
        return self.list_backend_instances_v2_with_http_info(request)

    def list_backend_instances_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'offset', 'limit', 'name', 'member_group_name', 'member_group_id', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'member_group_name' in local_var_params:
            query_params.append(('member_group_name', local_var_params['member_group_name']))
        if 'member_group_id' in local_var_params:
            query_params.append(('member_group_id', local_var_params['member_group_id']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBackendInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_member_groups(self, request):
        """查询VPC通道后端云服务组列表

        查询VPC通道后端云服务组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMemberGroups
        :type request: :class:`huaweicloudsdkapig.v2.ListMemberGroupsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListMemberGroupsResponse`
        """
        return self.list_member_groups_with_http_info(request)

    def list_member_groups_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'offset', 'limit', 'dict_code', 'member_group_name', 'precise_search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'dict_code' in local_var_params:
            query_params.append(('dict_code', local_var_params['dict_code']))
        if 'member_group_name' in local_var_params:
            query_params.append(('member_group_name', local_var_params['member_group_name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMemberGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpc_channels_v2(self, request):
        """查询VPC通道列表

        查看VPC通道列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpcChannelsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListVpcChannelsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListVpcChannelsV2Response`
        """
        return self.list_vpc_channels_v2_with_http_info(request)

    def list_vpc_channels_v2_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'id', 'name', 'dict_code', 'precise_search', 'member_host', 'member_port', 'member_group_name', 'member_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'dict_code' in local_var_params:
            query_params.append(('dict_code', local_var_params['dict_code']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))
        if 'member_host' in local_var_params:
            query_params.append(('member_host', local_var_params['member_host']))
        if 'member_port' in local_var_params:
            query_params.append(('member_port', local_var_params['member_port']))
        if 'member_group_name' in local_var_params:
            query_params.append(('member_group_name', local_var_params['member_group_name']))
        if 'member_group_id' in local_var_params:
            query_params.append(('member_group_id', local_var_params['member_group_id']))

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcChannelsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_member_group(self, request):
        """查看VPC通道后端服务器组详情

        查看指定的VPC通道后端服务器组详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfMemberGroupResponse`
        """
        return self.show_details_of_member_group_with_http_info(request)

    def show_details_of_member_group_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'member_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_group_id' in local_var_params:
            path_params['member_group_id'] = local_var_params['member_group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfMemberGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_details_of_vpc_channel_v2(self, request):
        """查看VPC通道详情

        查看指定的VPC通道详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDetailsOfVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfVpcChannelV2Response`
        """
        return self.show_details_of_vpc_channel_v2_with_http_info(request)

    def show_details_of_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDetailsOfVpcChannelV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_backend_instances_v2(self, request):
        """更新后端实例

        更新指定的VPC通道的后端实例。更新时，使用传入的请求参数对对应云服务组的后端实例进行全量覆盖修改。若未指定修改的云服务器组，则进行全量覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateBackendInstancesV2Response`
        """
        return self.update_backend_instances_v2_with_http_info(request)

    def update_backend_instances_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'update_backend_instances_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBackendInstancesV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_health_check(self, request):
        """修改VPC通道健康检查

        修改VPC通道健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHealthCheck
        :type request: :class:`huaweicloudsdkapig.v2.UpdateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateHealthCheckResponse`
        """
        return self.update_health_check_with_http_info(request)

    def update_health_check_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'update_health_check_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/health-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateHealthCheckResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_member_group(self, request):
        """更新VPC通道后端服务器组

        更新指定VPC通道后端服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.UpdateMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateMemberGroupResponse`
        """
        return self.update_member_group_with_http_info(request)

    def update_member_group_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'member_group_id', 'update_member_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_group_id' in local_var_params:
            path_params['member_group_id'] = local_var_params['member_group_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMemberGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vpc_channel_v2(self, request):
        """更新VPC通道

        更新指定VPC通道的参数
        
        使用传入的后端实例列表对VPC通道进行全量覆盖，若后端实例列表为空，则会全量删除已有的后端实例；
        
        使用传入的后端服务器组列表对VPC通道进行全量覆盖，若后端服务器组列表为空，则会全量删除已有的服务器组；
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateVpcChannelV2Response`
        """
        return self.update_vpc_channel_v2_with_http_info(request)

    def update_vpc_channel_v2_with_http_info(self, request):
        all_params = ['instance_id', 'vpc_channel_id', 'update_vpc_channel_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            resource_path='/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVpcChannelV2Response',
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
