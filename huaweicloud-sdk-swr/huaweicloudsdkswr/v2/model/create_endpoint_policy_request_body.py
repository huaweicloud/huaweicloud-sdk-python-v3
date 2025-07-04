# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool'
    }

    attribute_map = {
        'enable': 'enable'
    }

    def __init__(self, enable=None):
        r"""CreateEndpointPolicyRequestBody

        The model defined in huaweicloud sdk

        :param enable: true为开启，false为关闭。只有Disable、EnableFailed开启失败或者关闭时才能开启，只有Enable、DisableFailed时才能关闭。
        :type enable: bool
        """
        
        

        self._enable = None
        self.discriminator = None

        self.enable = enable

    @property
    def enable(self):
        r"""Gets the enable of this CreateEndpointPolicyRequestBody.

        true为开启，false为关闭。只有Disable、EnableFailed开启失败或者关闭时才能开启，只有Enable、DisableFailed时才能关闭。

        :return: The enable of this CreateEndpointPolicyRequestBody.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CreateEndpointPolicyRequestBody.

        true为开启，false为关闭。只有Disable、EnableFailed开启失败或者关闭时才能开启，只有Enable、DisableFailed时才能关闭。

        :param enable: The enable of this CreateEndpointPolicyRequestBody.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, CreateEndpointPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
