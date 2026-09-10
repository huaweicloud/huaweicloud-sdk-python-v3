# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelServiceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_spec': 'ModelServiceConfigCustomSpec',
        'user_env': 'dict(str, str)',
        'instance_count': 'int',
        'request_size_limit': 'int',
        'request_limit_per_second': 'int',
        'request_timeout': 'int'
    }

    attribute_map = {
        'custom_spec': 'custom_spec',
        'user_env': 'user_env',
        'instance_count': 'instance_count',
        'request_size_limit': 'request_size_limit',
        'request_limit_per_second': 'request_limit_per_second',
        'request_timeout': 'request_timeout'
    }

    def __init__(self, custom_spec=None, user_env=None, instance_count=None, request_size_limit=None, request_limit_per_second=None, request_timeout=None):
        r"""ModelServiceConfig

        The model defined in huaweicloud sdk

        :param custom_spec: 
        :type custom_spec: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfigCustomSpec`
        :param user_env: 部署环境变量，Map格式
        :type user_env: dict(str, str)
        :param instance_count: 部署实例个数，取值范围[1-10]，默认值1
        :type instance_count: int
        :param request_size_limit: 请求大小限制，取值范围[1-64000]，默认值6400
        :type request_size_limit: int
        :param request_limit_per_second: 请求QPS限制，取值范围[1-10000]，默认值100
        :type request_limit_per_second: int
        :param request_timeout: 请求超时时间，取值范围[1-120000]，默认值120000，单位毫秒
        :type request_timeout: int
        """
        
        

        self._custom_spec = None
        self._user_env = None
        self._instance_count = None
        self._request_size_limit = None
        self._request_limit_per_second = None
        self._request_timeout = None
        self.discriminator = None

        if custom_spec is not None:
            self.custom_spec = custom_spec
        if user_env is not None:
            self.user_env = user_env
        self.instance_count = instance_count
        if request_size_limit is not None:
            self.request_size_limit = request_size_limit
        if request_limit_per_second is not None:
            self.request_limit_per_second = request_limit_per_second
        if request_timeout is not None:
            self.request_timeout = request_timeout

    @property
    def custom_spec(self):
        r"""Gets the custom_spec of this ModelServiceConfig.

        :return: The custom_spec of this ModelServiceConfig.
        :rtype: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfigCustomSpec`
        """
        return self._custom_spec

    @custom_spec.setter
    def custom_spec(self, custom_spec):
        r"""Sets the custom_spec of this ModelServiceConfig.

        :param custom_spec: The custom_spec of this ModelServiceConfig.
        :type custom_spec: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfigCustomSpec`
        """
        self._custom_spec = custom_spec

    @property
    def user_env(self):
        r"""Gets the user_env of this ModelServiceConfig.

        部署环境变量，Map格式

        :return: The user_env of this ModelServiceConfig.
        :rtype: dict(str, str)
        """
        return self._user_env

    @user_env.setter
    def user_env(self, user_env):
        r"""Sets the user_env of this ModelServiceConfig.

        部署环境变量，Map格式

        :param user_env: The user_env of this ModelServiceConfig.
        :type user_env: dict(str, str)
        """
        self._user_env = user_env

    @property
    def instance_count(self):
        r"""Gets the instance_count of this ModelServiceConfig.

        部署实例个数，取值范围[1-10]，默认值1

        :return: The instance_count of this ModelServiceConfig.
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        r"""Sets the instance_count of this ModelServiceConfig.

        部署实例个数，取值范围[1-10]，默认值1

        :param instance_count: The instance_count of this ModelServiceConfig.
        :type instance_count: int
        """
        self._instance_count = instance_count

    @property
    def request_size_limit(self):
        r"""Gets the request_size_limit of this ModelServiceConfig.

        请求大小限制，取值范围[1-64000]，默认值6400

        :return: The request_size_limit of this ModelServiceConfig.
        :rtype: int
        """
        return self._request_size_limit

    @request_size_limit.setter
    def request_size_limit(self, request_size_limit):
        r"""Sets the request_size_limit of this ModelServiceConfig.

        请求大小限制，取值范围[1-64000]，默认值6400

        :param request_size_limit: The request_size_limit of this ModelServiceConfig.
        :type request_size_limit: int
        """
        self._request_size_limit = request_size_limit

    @property
    def request_limit_per_second(self):
        r"""Gets the request_limit_per_second of this ModelServiceConfig.

        请求QPS限制，取值范围[1-10000]，默认值100

        :return: The request_limit_per_second of this ModelServiceConfig.
        :rtype: int
        """
        return self._request_limit_per_second

    @request_limit_per_second.setter
    def request_limit_per_second(self, request_limit_per_second):
        r"""Sets the request_limit_per_second of this ModelServiceConfig.

        请求QPS限制，取值范围[1-10000]，默认值100

        :param request_limit_per_second: The request_limit_per_second of this ModelServiceConfig.
        :type request_limit_per_second: int
        """
        self._request_limit_per_second = request_limit_per_second

    @property
    def request_timeout(self):
        r"""Gets the request_timeout of this ModelServiceConfig.

        请求超时时间，取值范围[1-120000]，默认值120000，单位毫秒

        :return: The request_timeout of this ModelServiceConfig.
        :rtype: int
        """
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout):
        r"""Sets the request_timeout of this ModelServiceConfig.

        请求超时时间，取值范围[1-120000]，默认值120000，单位毫秒

        :param request_timeout: The request_timeout of this ModelServiceConfig.
        :type request_timeout: int
        """
        self._request_timeout = request_timeout

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelServiceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
