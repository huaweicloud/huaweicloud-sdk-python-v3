# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroserviceImportReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_info': 'MicroserviceGroup',
        'service_type': 'str',
        'protocol': 'str',
        'apis': 'list[MicroserviceApiCreate]',
        'backend_timeout': 'int',
        'auth_type': 'str',
        'cors': 'bool',
        'cse_info': 'MicroServiceInfoCSECreate',
        'cce_info': 'MicroServiceInfoCCECreate'
    }

    attribute_map = {
        'group_info': 'group_info',
        'service_type': 'service_type',
        'protocol': 'protocol',
        'apis': 'apis',
        'backend_timeout': 'backend_timeout',
        'auth_type': 'auth_type',
        'cors': 'cors',
        'cse_info': 'cse_info',
        'cce_info': 'cce_info'
    }

    def __init__(self, group_info=None, service_type=None, protocol=None, apis=None, backend_timeout=None, auth_type=None, cors=None, cse_info=None, cce_info=None):
        """MicroserviceImportReq

        The model defined in huaweicloud sdk

        :param group_info: 
        :type group_info: :class:`huaweicloudsdkapig.v2.MicroserviceGroup`
        :param service_type: 微服务中心类型。 - CSE：CSE微服务注册中心 - CCE: CCE云容器引擎
        :type service_type: str
        :param protocol: API网关访问微服务的请求协议 - HTTP - HTTPS
        :type protocol: str
        :param apis: 导入的api列表
        :type apis: list[:class:`huaweicloudsdkapig.v2.MicroserviceApiCreate`]
        :param backend_timeout: 服务集成请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000，默认5000  单位：毫秒。
        :type backend_timeout: int
        :param auth_type: API的认证方式，默认无认证[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证
        :type auth_type: str
        :param cors: 是否支持跨域，默认不支持 - true：支持 - false：不支持
        :type cors: bool
        :param cse_info: 
        :type cse_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCSECreate`
        :param cce_info: 
        :type cce_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCECreate`
        """
        
        

        self._group_info = None
        self._service_type = None
        self._protocol = None
        self._apis = None
        self._backend_timeout = None
        self._auth_type = None
        self._cors = None
        self._cse_info = None
        self._cce_info = None
        self.discriminator = None

        self.group_info = group_info
        self.service_type = service_type
        if protocol is not None:
            self.protocol = protocol
        self.apis = apis
        if backend_timeout is not None:
            self.backend_timeout = backend_timeout
        if auth_type is not None:
            self.auth_type = auth_type
        if cors is not None:
            self.cors = cors
        if cse_info is not None:
            self.cse_info = cse_info
        if cce_info is not None:
            self.cce_info = cce_info

    @property
    def group_info(self):
        """Gets the group_info of this MicroserviceImportReq.


        :return: The group_info of this MicroserviceImportReq.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroserviceGroup`
        """
        return self._group_info

    @group_info.setter
    def group_info(self, group_info):
        """Sets the group_info of this MicroserviceImportReq.


        :param group_info: The group_info of this MicroserviceImportReq.
        :type group_info: :class:`huaweicloudsdkapig.v2.MicroserviceGroup`
        """
        self._group_info = group_info

    @property
    def service_type(self):
        """Gets the service_type of this MicroserviceImportReq.

        微服务中心类型。 - CSE：CSE微服务注册中心 - CCE: CCE云容器引擎

        :return: The service_type of this MicroserviceImportReq.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this MicroserviceImportReq.

        微服务中心类型。 - CSE：CSE微服务注册中心 - CCE: CCE云容器引擎

        :param service_type: The service_type of this MicroserviceImportReq.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def protocol(self):
        """Gets the protocol of this MicroserviceImportReq.

        API网关访问微服务的请求协议 - HTTP - HTTPS

        :return: The protocol of this MicroserviceImportReq.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this MicroserviceImportReq.

        API网关访问微服务的请求协议 - HTTP - HTTPS

        :param protocol: The protocol of this MicroserviceImportReq.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def apis(self):
        """Gets the apis of this MicroserviceImportReq.

        导入的api列表

        :return: The apis of this MicroserviceImportReq.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MicroserviceApiCreate`]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this MicroserviceImportReq.

        导入的api列表

        :param apis: The apis of this MicroserviceImportReq.
        :type apis: list[:class:`huaweicloudsdkapig.v2.MicroserviceApiCreate`]
        """
        self._apis = apis

    @property
    def backend_timeout(self):
        """Gets the backend_timeout of this MicroserviceImportReq.

        服务集成请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000，默认5000  单位：毫秒。

        :return: The backend_timeout of this MicroserviceImportReq.
        :rtype: int
        """
        return self._backend_timeout

    @backend_timeout.setter
    def backend_timeout(self, backend_timeout):
        """Sets the backend_timeout of this MicroserviceImportReq.

        服务集成请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000，默认5000  单位：毫秒。

        :param backend_timeout: The backend_timeout of this MicroserviceImportReq.
        :type backend_timeout: int
        """
        self._backend_timeout = backend_timeout

    @property
    def auth_type(self):
        """Gets the auth_type of this MicroserviceImportReq.

        API的认证方式，默认无认证[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证

        :return: The auth_type of this MicroserviceImportReq.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this MicroserviceImportReq.

        API的认证方式，默认无认证[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证

        :param auth_type: The auth_type of this MicroserviceImportReq.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def cors(self):
        """Gets the cors of this MicroserviceImportReq.

        是否支持跨域，默认不支持 - true：支持 - false：不支持

        :return: The cors of this MicroserviceImportReq.
        :rtype: bool
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """Sets the cors of this MicroserviceImportReq.

        是否支持跨域，默认不支持 - true：支持 - false：不支持

        :param cors: The cors of this MicroserviceImportReq.
        :type cors: bool
        """
        self._cors = cors

    @property
    def cse_info(self):
        """Gets the cse_info of this MicroserviceImportReq.


        :return: The cse_info of this MicroserviceImportReq.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCSECreate`
        """
        return self._cse_info

    @cse_info.setter
    def cse_info(self, cse_info):
        """Sets the cse_info of this MicroserviceImportReq.


        :param cse_info: The cse_info of this MicroserviceImportReq.
        :type cse_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCSECreate`
        """
        self._cse_info = cse_info

    @property
    def cce_info(self):
        """Gets the cce_info of this MicroserviceImportReq.


        :return: The cce_info of this MicroserviceImportReq.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCECreate`
        """
        return self._cce_info

    @cce_info.setter
    def cce_info(self, cce_info):
        """Sets the cce_info of this MicroserviceImportReq.


        :param cce_info: The cce_info of this MicroserviceImportReq.
        :type cce_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfoCCECreate`
        """
        self._cce_info = cce_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MicroserviceImportReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
