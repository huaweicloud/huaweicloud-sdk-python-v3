# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TwoFactorLoginHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'os_type': 'str',
        'auth_switch': 'bool',
        'auth_type': 'str',
        'topic_display_name': 'str',
        'topic_urn': 'str',
        'outside_host': 'bool'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'os_type': 'os_type',
        'auth_switch': 'auth_switch',
        'auth_type': 'auth_type',
        'topic_display_name': 'topic_display_name',
        'topic_urn': 'topic_urn',
        'outside_host': 'outside_host'
    }

    def __init__(self, host_id=None, host_name=None, os_type=None, auth_switch=None, auth_type=None, topic_display_name=None, topic_urn=None, outside_host=None):
        r"""TwoFactorLoginHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param auth_switch: 是否开启双因子认证
        :type auth_switch: bool
        :param auth_type: 认证类型 - sms ： 短信邮件验证 - code ： 验证码验证
        :type auth_type: str
        :param topic_display_name: 主题别名
        :type topic_display_name: str
        :param topic_urn: 主题唯一资源标识
        :type topic_urn: str
        :param outside_host: 是否为外部（非华为云）机器
        :type outside_host: bool
        """
        
        

        self._host_id = None
        self._host_name = None
        self._os_type = None
        self._auth_switch = None
        self._auth_type = None
        self._topic_display_name = None
        self._topic_urn = None
        self._outside_host = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if os_type is not None:
            self.os_type = os_type
        if auth_switch is not None:
            self.auth_switch = auth_switch
        if auth_type is not None:
            self.auth_type = auth_type
        if topic_display_name is not None:
            self.topic_display_name = topic_display_name
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if outside_host is not None:
            self.outside_host = outside_host

    @property
    def host_id(self):
        r"""Gets the host_id of this TwoFactorLoginHostResponseInfo.

        主机id

        :return: The host_id of this TwoFactorLoginHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this TwoFactorLoginHostResponseInfo.

        主机id

        :param host_id: The host_id of this TwoFactorLoginHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this TwoFactorLoginHostResponseInfo.

        主机名称

        :return: The host_name of this TwoFactorLoginHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this TwoFactorLoginHostResponseInfo.

        主机名称

        :param host_name: The host_name of this TwoFactorLoginHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def os_type(self):
        r"""Gets the os_type of this TwoFactorLoginHostResponseInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this TwoFactorLoginHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this TwoFactorLoginHostResponseInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this TwoFactorLoginHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def auth_switch(self):
        r"""Gets the auth_switch of this TwoFactorLoginHostResponseInfo.

        是否开启双因子认证

        :return: The auth_switch of this TwoFactorLoginHostResponseInfo.
        :rtype: bool
        """
        return self._auth_switch

    @auth_switch.setter
    def auth_switch(self, auth_switch):
        r"""Sets the auth_switch of this TwoFactorLoginHostResponseInfo.

        是否开启双因子认证

        :param auth_switch: The auth_switch of this TwoFactorLoginHostResponseInfo.
        :type auth_switch: bool
        """
        self._auth_switch = auth_switch

    @property
    def auth_type(self):
        r"""Gets the auth_type of this TwoFactorLoginHostResponseInfo.

        认证类型 - sms ： 短信邮件验证 - code ： 验证码验证

        :return: The auth_type of this TwoFactorLoginHostResponseInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this TwoFactorLoginHostResponseInfo.

        认证类型 - sms ： 短信邮件验证 - code ： 验证码验证

        :param auth_type: The auth_type of this TwoFactorLoginHostResponseInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def topic_display_name(self):
        r"""Gets the topic_display_name of this TwoFactorLoginHostResponseInfo.

        主题别名

        :return: The topic_display_name of this TwoFactorLoginHostResponseInfo.
        :rtype: str
        """
        return self._topic_display_name

    @topic_display_name.setter
    def topic_display_name(self, topic_display_name):
        r"""Sets the topic_display_name of this TwoFactorLoginHostResponseInfo.

        主题别名

        :param topic_display_name: The topic_display_name of this TwoFactorLoginHostResponseInfo.
        :type topic_display_name: str
        """
        self._topic_display_name = topic_display_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this TwoFactorLoginHostResponseInfo.

        主题唯一资源标识

        :return: The topic_urn of this TwoFactorLoginHostResponseInfo.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this TwoFactorLoginHostResponseInfo.

        主题唯一资源标识

        :param topic_urn: The topic_urn of this TwoFactorLoginHostResponseInfo.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def outside_host(self):
        r"""Gets the outside_host of this TwoFactorLoginHostResponseInfo.

        是否为外部（非华为云）机器

        :return: The outside_host of this TwoFactorLoginHostResponseInfo.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        r"""Sets the outside_host of this TwoFactorLoginHostResponseInfo.

        是否为外部（非华为云）机器

        :param outside_host: The outside_host of this TwoFactorLoginHostResponseInfo.
        :type outside_host: bool
        """
        self._outside_host = outside_host

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
        if not isinstance(other, TwoFactorLoginHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
