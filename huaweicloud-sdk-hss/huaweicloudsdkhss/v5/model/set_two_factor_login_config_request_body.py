# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetTwoFactorLoginConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'auth_type': 'str',
        'topic_display_name': 'str',
        'topic_urn': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'auth_type': 'auth_type',
        'topic_display_name': 'topic_display_name',
        'topic_urn': 'topic_urn',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, enabled=None, auth_type=None, topic_display_name=None, topic_urn=None, host_id_list=None):
        r"""SetTwoFactorLoginConfigRequestBody

        The model defined in huaweicloud sdk

        :param enabled: 是否开启双因子认证
        :type enabled: bool
        :param auth_type: 认证类型 - sms ：短信邮件验证 - code ：验证码验证
        :type auth_type: str
        :param topic_display_name: 主题别名
        :type topic_display_name: str
        :param topic_urn: 主题的唯一资源标识
        :type topic_urn: str
        :param host_id_list: 服务器列表
        :type host_id_list: list[str]
        """
        
        

        self._enabled = None
        self._auth_type = None
        self._topic_display_name = None
        self._topic_urn = None
        self._host_id_list = None
        self.discriminator = None

        self.enabled = enabled
        self.auth_type = auth_type
        self.topic_display_name = topic_display_name
        self.topic_urn = topic_urn
        self.host_id_list = host_id_list

    @property
    def enabled(self):
        r"""Gets the enabled of this SetTwoFactorLoginConfigRequestBody.

        是否开启双因子认证

        :return: The enabled of this SetTwoFactorLoginConfigRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this SetTwoFactorLoginConfigRequestBody.

        是否开启双因子认证

        :param enabled: The enabled of this SetTwoFactorLoginConfigRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def auth_type(self):
        r"""Gets the auth_type of this SetTwoFactorLoginConfigRequestBody.

        认证类型 - sms ：短信邮件验证 - code ：验证码验证

        :return: The auth_type of this SetTwoFactorLoginConfigRequestBody.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this SetTwoFactorLoginConfigRequestBody.

        认证类型 - sms ：短信邮件验证 - code ：验证码验证

        :param auth_type: The auth_type of this SetTwoFactorLoginConfigRequestBody.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def topic_display_name(self):
        r"""Gets the topic_display_name of this SetTwoFactorLoginConfigRequestBody.

        主题别名

        :return: The topic_display_name of this SetTwoFactorLoginConfigRequestBody.
        :rtype: str
        """
        return self._topic_display_name

    @topic_display_name.setter
    def topic_display_name(self, topic_display_name):
        r"""Sets the topic_display_name of this SetTwoFactorLoginConfigRequestBody.

        主题别名

        :param topic_display_name: The topic_display_name of this SetTwoFactorLoginConfigRequestBody.
        :type topic_display_name: str
        """
        self._topic_display_name = topic_display_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this SetTwoFactorLoginConfigRequestBody.

        主题的唯一资源标识

        :return: The topic_urn of this SetTwoFactorLoginConfigRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this SetTwoFactorLoginConfigRequestBody.

        主题的唯一资源标识

        :param topic_urn: The topic_urn of this SetTwoFactorLoginConfigRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this SetTwoFactorLoginConfigRequestBody.

        服务器列表

        :return: The host_id_list of this SetTwoFactorLoginConfigRequestBody.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this SetTwoFactorLoginConfigRequestBody.

        服务器列表

        :param host_id_list: The host_id_list of this SetTwoFactorLoginConfigRequestBody.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, SetTwoFactorLoginConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
