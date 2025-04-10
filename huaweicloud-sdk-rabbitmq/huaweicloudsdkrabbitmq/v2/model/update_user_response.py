# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'secret_key': 'str',
        'vhosts': 'list[AMQPUserPerm]'
    }

    attribute_map = {
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'vhosts': 'vhosts'
    }

    def __init__(self, access_key=None, secret_key=None, vhosts=None):
        r"""UpdateUserResponse

        The model defined in huaweicloud sdk

        :param access_key: 用户名，只能英文字母开头，且由英文字母、数字、中划线、下划线组成，长度为7~64个字符。
        :type access_key: str
        :param secret_key: 密钥。 8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符&#x60;~!@#$%^&amp;*()-_&#x3D;+\\\\|[{}];:\\&#39;\\\&quot;,&lt;.&gt;/?。 不能与名称或倒序的名称相同。
        :type secret_key: str
        :param vhosts: 需要配置权限的Vhost，一个用户可以配置多个Vhost下的资源权限。
        :type vhosts: list[:class:`huaweicloudsdkrabbitmq.v2.AMQPUserPerm`]
        """
        
        super(UpdateUserResponse, self).__init__()

        self._access_key = None
        self._secret_key = None
        self._vhosts = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if vhosts is not None:
            self.vhosts = vhosts

    @property
    def access_key(self):
        r"""Gets the access_key of this UpdateUserResponse.

        用户名，只能英文字母开头，且由英文字母、数字、中划线、下划线组成，长度为7~64个字符。

        :return: The access_key of this UpdateUserResponse.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this UpdateUserResponse.

        用户名，只能英文字母开头，且由英文字母、数字、中划线、下划线组成，长度为7~64个字符。

        :param access_key: The access_key of this UpdateUserResponse.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        r"""Gets the secret_key of this UpdateUserResponse.

        密钥。 8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符`~!@#$%^&*()-_=+\\\\|[{}];:\\'\\\",<.>/?。 不能与名称或倒序的名称相同。

        :return: The secret_key of this UpdateUserResponse.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this UpdateUserResponse.

        密钥。 8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符`~!@#$%^&*()-_=+\\\\|[{}];:\\'\\\",<.>/?。 不能与名称或倒序的名称相同。

        :param secret_key: The secret_key of this UpdateUserResponse.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def vhosts(self):
        r"""Gets the vhosts of this UpdateUserResponse.

        需要配置权限的Vhost，一个用户可以配置多个Vhost下的资源权限。

        :return: The vhosts of this UpdateUserResponse.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.AMQPUserPerm`]
        """
        return self._vhosts

    @vhosts.setter
    def vhosts(self, vhosts):
        r"""Sets the vhosts of this UpdateUserResponse.

        需要配置权限的Vhost，一个用户可以配置多个Vhost下的资源权限。

        :param vhosts: The vhosts of this UpdateUserResponse.
        :type vhosts: list[:class:`huaweicloudsdkrabbitmq.v2.AMQPUserPerm`]
        """
        self._vhosts = vhosts

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
        if not isinstance(other, UpdateUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
