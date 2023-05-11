# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationEndpoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'endpoint_urn': 'str',
        'user_data': 'str',
        'enabled': 'str',
        'token': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'endpoint_urn': 'endpoint_urn',
        'user_data': 'user_data',
        'enabled': 'enabled',
        'token': 'token'
    }

    def __init__(self, create_time=None, endpoint_urn=None, user_data=None, enabled=None, token=None):
        """ApplicationEndpoint

        The model defined in huaweicloud sdk

        :param create_time: 创建application的时间 时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param endpoint_urn: Application endpoint的唯一资源标识。
        :type endpoint_urn: str
        :param user_data: 用户自定义数据 最大长度支持UTF-8编码后2048字节。
        :type user_data: str
        :param enabled: endpoint启用开关 true或false字符串。
        :type enabled: str
        :param token: 设备token 最大长度512个字节。
        :type token: str
        """
        
        

        self._create_time = None
        self._endpoint_urn = None
        self._user_data = None
        self._enabled = None
        self._token = None
        self.discriminator = None

        self.create_time = create_time
        self.endpoint_urn = endpoint_urn
        self.user_data = user_data
        self.enabled = enabled
        self.token = token

    @property
    def create_time(self):
        """Gets the create_time of this ApplicationEndpoint.

        创建application的时间 时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this ApplicationEndpoint.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApplicationEndpoint.

        创建application的时间 时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this ApplicationEndpoint.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def endpoint_urn(self):
        """Gets the endpoint_urn of this ApplicationEndpoint.

        Application endpoint的唯一资源标识。

        :return: The endpoint_urn of this ApplicationEndpoint.
        :rtype: str
        """
        return self._endpoint_urn

    @endpoint_urn.setter
    def endpoint_urn(self, endpoint_urn):
        """Sets the endpoint_urn of this ApplicationEndpoint.

        Application endpoint的唯一资源标识。

        :param endpoint_urn: The endpoint_urn of this ApplicationEndpoint.
        :type endpoint_urn: str
        """
        self._endpoint_urn = endpoint_urn

    @property
    def user_data(self):
        """Gets the user_data of this ApplicationEndpoint.

        用户自定义数据 最大长度支持UTF-8编码后2048字节。

        :return: The user_data of this ApplicationEndpoint.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ApplicationEndpoint.

        用户自定义数据 最大长度支持UTF-8编码后2048字节。

        :param user_data: The user_data of this ApplicationEndpoint.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def enabled(self):
        """Gets the enabled of this ApplicationEndpoint.

        endpoint启用开关 true或false字符串。

        :return: The enabled of this ApplicationEndpoint.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ApplicationEndpoint.

        endpoint启用开关 true或false字符串。

        :param enabled: The enabled of this ApplicationEndpoint.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def token(self):
        """Gets the token of this ApplicationEndpoint.

        设备token 最大长度512个字节。

        :return: The token of this ApplicationEndpoint.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ApplicationEndpoint.

        设备token 最大长度512个字节。

        :param token: The token of this ApplicationEndpoint.
        :type token: str
        """
        self._token = token

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
        if not isinstance(other, ApplicationEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
