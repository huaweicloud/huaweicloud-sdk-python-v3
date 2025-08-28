# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecodeAuthorizationMessageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encoded_message': 'str'
    }

    attribute_map = {
        'encoded_message': 'encoded_message'
    }

    def __init__(self, encoded_message=None):
        r"""DecodeAuthorizationMessageReq

        The model defined in huaweicloud sdk

        :param encoded_message: 加密的鉴权失败原因，字符串长度范围[1,10240]。
        :type encoded_message: str
        """
        
        

        self._encoded_message = None
        self.discriminator = None

        self.encoded_message = encoded_message

    @property
    def encoded_message(self):
        r"""Gets the encoded_message of this DecodeAuthorizationMessageReq.

        加密的鉴权失败原因，字符串长度范围[1,10240]。

        :return: The encoded_message of this DecodeAuthorizationMessageReq.
        :rtype: str
        """
        return self._encoded_message

    @encoded_message.setter
    def encoded_message(self, encoded_message):
        r"""Sets the encoded_message of this DecodeAuthorizationMessageReq.

        加密的鉴权失败原因，字符串长度范围[1,10240]。

        :param encoded_message: The encoded_message of this DecodeAuthorizationMessageReq.
        :type encoded_message: str
        """
        self._encoded_message = encoded_message

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
        if not isinstance(other, DecodeAuthorizationMessageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
