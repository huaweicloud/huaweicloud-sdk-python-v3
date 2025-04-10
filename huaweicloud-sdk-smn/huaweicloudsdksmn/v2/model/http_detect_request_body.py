# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpDetectRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'endpoint': 'str',
        'extension': 'HttpDetectRequestBodyExtension'
    }

    attribute_map = {
        'protocol': 'protocol',
        'endpoint': 'endpoint',
        'extension': 'extension'
    }

    def __init__(self, protocol=None, endpoint=None, extension=None):
        r"""HttpDetectRequestBody

        The model defined in huaweicloud sdk

        :param protocol: 协议类型，当前仅支持http/https，不可为空
        :type protocol: str
        :param endpoint: 待探测的终端地址，当前仅支持以http:// 或https://开头，不可为空
        :type endpoint: str
        :param extension: 
        :type extension: :class:`huaweicloudsdksmn.v2.HttpDetectRequestBodyExtension`
        """
        
        

        self._protocol = None
        self._endpoint = None
        self._extension = None
        self.discriminator = None

        self.protocol = protocol
        self.endpoint = endpoint
        if extension is not None:
            self.extension = extension

    @property
    def protocol(self):
        r"""Gets the protocol of this HttpDetectRequestBody.

        协议类型，当前仅支持http/https，不可为空

        :return: The protocol of this HttpDetectRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this HttpDetectRequestBody.

        协议类型，当前仅支持http/https，不可为空

        :param protocol: The protocol of this HttpDetectRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        r"""Gets the endpoint of this HttpDetectRequestBody.

        待探测的终端地址，当前仅支持以http:// 或https://开头，不可为空

        :return: The endpoint of this HttpDetectRequestBody.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this HttpDetectRequestBody.

        待探测的终端地址，当前仅支持以http:// 或https://开头，不可为空

        :param endpoint: The endpoint of this HttpDetectRequestBody.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def extension(self):
        r"""Gets the extension of this HttpDetectRequestBody.

        :return: The extension of this HttpDetectRequestBody.
        :rtype: :class:`huaweicloudsdksmn.v2.HttpDetectRequestBodyExtension`
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        r"""Sets the extension of this HttpDetectRequestBody.

        :param extension: The extension of this HttpDetectRequestBody.
        :type extension: :class:`huaweicloudsdksmn.v2.HttpDetectRequestBodyExtension`
        """
        self._extension = extension

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
        if not isinstance(other, HttpDetectRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
