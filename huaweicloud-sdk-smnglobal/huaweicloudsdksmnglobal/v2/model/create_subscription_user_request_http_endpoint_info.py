# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionUserRequestHttpEndpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'header': 'dict(str, str)'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'header': 'header'
    }

    def __init__(self, endpoint=None, header=None):
        r"""CreateSubscriptionUserRequestHttpEndpointInfo

        The model defined in huaweicloud sdk

        :param endpoint: 终端地址。必须以“http://”开头。
        :type endpoint: str
        :param header: http协议订阅用户的自定义请求头。http协议订阅用户可以自定义请求头。
        :type header: dict(str, str)
        """
        
        

        self._endpoint = None
        self._header = None
        self.discriminator = None

        self.endpoint = endpoint
        if header is not None:
            self.header = header

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CreateSubscriptionUserRequestHttpEndpointInfo.

        终端地址。必须以“http://”开头。

        :return: The endpoint of this CreateSubscriptionUserRequestHttpEndpointInfo.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CreateSubscriptionUserRequestHttpEndpointInfo.

        终端地址。必须以“http://”开头。

        :param endpoint: The endpoint of this CreateSubscriptionUserRequestHttpEndpointInfo.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def header(self):
        r"""Gets the header of this CreateSubscriptionUserRequestHttpEndpointInfo.

        http协议订阅用户的自定义请求头。http协议订阅用户可以自定义请求头。

        :return: The header of this CreateSubscriptionUserRequestHttpEndpointInfo.
        :rtype: dict(str, str)
        """
        return self._header

    @header.setter
    def header(self, header):
        r"""Sets the header of this CreateSubscriptionUserRequestHttpEndpointInfo.

        http协议订阅用户的自定义请求头。http协议订阅用户可以自定义请求头。

        :param header: The header of this CreateSubscriptionUserRequestHttpEndpointInfo.
        :type header: dict(str, str)
        """
        self._header = header

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
        if not isinstance(other, CreateSubscriptionUserRequestHttpEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
