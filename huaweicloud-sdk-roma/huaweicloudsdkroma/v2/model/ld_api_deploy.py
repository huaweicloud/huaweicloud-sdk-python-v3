# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdApiDeploy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploy_front_api': 'bool',
        'auth_type': 'str',
        'authorizer_id': 'str',
        'group_id': 'str',
        'env_id': 'str',
        'protocol': 'str',
        'backend_timeout': 'int',
        'path': 'str',
        'method': 'str',
        'cors': 'bool',
        'roma_app_id': 'str',
        'retry_count': 'str'
    }

    attribute_map = {
        'deploy_front_api': 'deploy_front_api',
        'auth_type': 'auth_type',
        'authorizer_id': 'authorizer_id',
        'group_id': 'group_id',
        'env_id': 'env_id',
        'protocol': 'protocol',
        'backend_timeout': 'backend_timeout',
        'path': 'path',
        'method': 'method',
        'cors': 'cors',
        'roma_app_id': 'roma_app_id',
        'retry_count': 'retry_count'
    }

    def __init__(self, deploy_front_api=None, auth_type=None, authorizer_id=None, group_id=None, env_id=None, protocol=None, backend_timeout=None, path=None, method=None, cors=None, roma_app_id=None, retry_count=None):
        """LdApiDeploy

        The model defined in huaweicloud sdk

        :param deploy_front_api: 是否自动发布API - true：部署完成后自动创建并发布前端API。此时auth_type，group_id，env_id，protocol必填。 - false：部署完成后不创建前端API 
        :type deploy_front_api: bool
        :param auth_type: 认证方式[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证 
        :type auth_type: str
        :param authorizer_id: 自定义认证编号。  认证方式auth_type &#x3D; AUTHORIZER时必填
        :type authorizer_id: str
        :param group_id: 部署的前端API分组编号
        :type group_id: str
        :param env_id: 部署的环境编号
        :type env_id: str
        :param protocol: 请求协议
        :type protocol: str
        :param backend_timeout: 超时时间
        :type backend_timeout: int
        :param path: 请求路径
        :type path: str
        :param method: 请求方式
        :type method: str
        :param cors: 是否支持跨域 - true：支持 - false：不支持 
        :type cors: bool
        :param roma_app_id: 部署到前端的api归属的应用编号，与后端归属的应用编号保持一致
        :type roma_app_id: str
        :param retry_count: ROMA Connect APIC请求后端服务的重试次数，默认为-1，范围[-1,10]
        :type retry_count: str
        """
        
        

        self._deploy_front_api = None
        self._auth_type = None
        self._authorizer_id = None
        self._group_id = None
        self._env_id = None
        self._protocol = None
        self._backend_timeout = None
        self._path = None
        self._method = None
        self._cors = None
        self._roma_app_id = None
        self._retry_count = None
        self.discriminator = None

        if deploy_front_api is not None:
            self.deploy_front_api = deploy_front_api
        if auth_type is not None:
            self.auth_type = auth_type
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if group_id is not None:
            self.group_id = group_id
        if env_id is not None:
            self.env_id = env_id
        if protocol is not None:
            self.protocol = protocol
        if backend_timeout is not None:
            self.backend_timeout = backend_timeout
        if path is not None:
            self.path = path
        if method is not None:
            self.method = method
        if cors is not None:
            self.cors = cors
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if retry_count is not None:
            self.retry_count = retry_count

    @property
    def deploy_front_api(self):
        """Gets the deploy_front_api of this LdApiDeploy.

        是否自动发布API - true：部署完成后自动创建并发布前端API。此时auth_type，group_id，env_id，protocol必填。 - false：部署完成后不创建前端API 

        :return: The deploy_front_api of this LdApiDeploy.
        :rtype: bool
        """
        return self._deploy_front_api

    @deploy_front_api.setter
    def deploy_front_api(self, deploy_front_api):
        """Sets the deploy_front_api of this LdApiDeploy.

        是否自动发布API - true：部署完成后自动创建并发布前端API。此时auth_type，group_id，env_id，protocol必填。 - false：部署完成后不创建前端API 

        :param deploy_front_api: The deploy_front_api of this LdApiDeploy.
        :type deploy_front_api: bool
        """
        self._deploy_front_api = deploy_front_api

    @property
    def auth_type(self):
        """Gets the auth_type of this LdApiDeploy.

        认证方式[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证 

        :return: The auth_type of this LdApiDeploy.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this LdApiDeploy.

        认证方式[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证 

        :param auth_type: The auth_type of this LdApiDeploy.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this LdApiDeploy.

        自定义认证编号。  认证方式auth_type = AUTHORIZER时必填

        :return: The authorizer_id of this LdApiDeploy.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this LdApiDeploy.

        自定义认证编号。  认证方式auth_type = AUTHORIZER时必填

        :param authorizer_id: The authorizer_id of this LdApiDeploy.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

    @property
    def group_id(self):
        """Gets the group_id of this LdApiDeploy.

        部署的前端API分组编号

        :return: The group_id of this LdApiDeploy.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this LdApiDeploy.

        部署的前端API分组编号

        :param group_id: The group_id of this LdApiDeploy.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def env_id(self):
        """Gets the env_id of this LdApiDeploy.

        部署的环境编号

        :return: The env_id of this LdApiDeploy.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this LdApiDeploy.

        部署的环境编号

        :param env_id: The env_id of this LdApiDeploy.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def protocol(self):
        """Gets the protocol of this LdApiDeploy.

        请求协议

        :return: The protocol of this LdApiDeploy.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this LdApiDeploy.

        请求协议

        :param protocol: The protocol of this LdApiDeploy.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def backend_timeout(self):
        """Gets the backend_timeout of this LdApiDeploy.

        超时时间

        :return: The backend_timeout of this LdApiDeploy.
        :rtype: int
        """
        return self._backend_timeout

    @backend_timeout.setter
    def backend_timeout(self, backend_timeout):
        """Sets the backend_timeout of this LdApiDeploy.

        超时时间

        :param backend_timeout: The backend_timeout of this LdApiDeploy.
        :type backend_timeout: int
        """
        self._backend_timeout = backend_timeout

    @property
    def path(self):
        """Gets the path of this LdApiDeploy.

        请求路径

        :return: The path of this LdApiDeploy.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LdApiDeploy.

        请求路径

        :param path: The path of this LdApiDeploy.
        :type path: str
        """
        self._path = path

    @property
    def method(self):
        """Gets the method of this LdApiDeploy.

        请求方式

        :return: The method of this LdApiDeploy.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this LdApiDeploy.

        请求方式

        :param method: The method of this LdApiDeploy.
        :type method: str
        """
        self._method = method

    @property
    def cors(self):
        """Gets the cors of this LdApiDeploy.

        是否支持跨域 - true：支持 - false：不支持 

        :return: The cors of this LdApiDeploy.
        :rtype: bool
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """Sets the cors of this LdApiDeploy.

        是否支持跨域 - true：支持 - false：不支持 

        :param cors: The cors of this LdApiDeploy.
        :type cors: bool
        """
        self._cors = cors

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this LdApiDeploy.

        部署到前端的api归属的应用编号，与后端归属的应用编号保持一致

        :return: The roma_app_id of this LdApiDeploy.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this LdApiDeploy.

        部署到前端的api归属的应用编号，与后端归属的应用编号保持一致

        :param roma_app_id: The roma_app_id of this LdApiDeploy.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def retry_count(self):
        """Gets the retry_count of this LdApiDeploy.

        ROMA Connect APIC请求后端服务的重试次数，默认为-1，范围[-1,10]

        :return: The retry_count of this LdApiDeploy.
        :rtype: str
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this LdApiDeploy.

        ROMA Connect APIC请求后端服务的重试次数，默认为-1，范围[-1,10]

        :param retry_count: The retry_count of this LdApiDeploy.
        :type retry_count: str
        """
        self._retry_count = retry_count

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
        if not isinstance(other, LdApiDeploy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
