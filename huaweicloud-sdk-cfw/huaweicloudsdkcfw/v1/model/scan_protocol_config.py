# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanProtocolConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'int',
        'protocol_type': 'int'
    }

    attribute_map = {
        'action': 'action',
        'protocol_type': 'protocol_type'
    }

    def __init__(self, action=None, protocol_type=None):
        r"""ScanProtocolConfig

        The model defined in huaweicloud sdk

        :param action: 反病毒动作，0：观察 1：拦截 2：禁用
        :type action: int
        :param protocol_type: 协议类型
        :type protocol_type: int
        """
        
        

        self._action = None
        self._protocol_type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if protocol_type is not None:
            self.protocol_type = protocol_type

    @property
    def action(self):
        r"""Gets the action of this ScanProtocolConfig.

        反病毒动作，0：观察 1：拦截 2：禁用

        :return: The action of this ScanProtocolConfig.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ScanProtocolConfig.

        反病毒动作，0：观察 1：拦截 2：禁用

        :param action: The action of this ScanProtocolConfig.
        :type action: int
        """
        self._action = action

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this ScanProtocolConfig.

        协议类型

        :return: The protocol_type of this ScanProtocolConfig.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this ScanProtocolConfig.

        协议类型

        :param protocol_type: The protocol_type of this ScanProtocolConfig.
        :type protocol_type: int
        """
        self._protocol_type = protocol_type

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
        if not isinstance(other, ScanProtocolConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
