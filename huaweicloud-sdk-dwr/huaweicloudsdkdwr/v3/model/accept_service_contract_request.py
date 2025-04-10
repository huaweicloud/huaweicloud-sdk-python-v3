# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AcceptServiceContractRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):
        r"""AcceptServiceContractRequest

        The model defined in huaweicloud sdk

        :param type: 服务协议名称 使用公共Action的免责声明协议: use_public_action_privacy_statement 注册公共Action的免责声明协议: register_public_action_privacy_statement
        :type type: str
        """
        
        

        self._type = None
        self.discriminator = None

        self.type = type

    @property
    def type(self):
        r"""Gets the type of this AcceptServiceContractRequest.

        服务协议名称 使用公共Action的免责声明协议: use_public_action_privacy_statement 注册公共Action的免责声明协议: register_public_action_privacy_statement

        :return: The type of this AcceptServiceContractRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AcceptServiceContractRequest.

        服务协议名称 使用公共Action的免责声明协议: use_public_action_privacy_statement 注册公共Action的免责声明协议: register_public_action_privacy_statement

        :param type: The type of this AcceptServiceContractRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, AcceptServiceContractRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
