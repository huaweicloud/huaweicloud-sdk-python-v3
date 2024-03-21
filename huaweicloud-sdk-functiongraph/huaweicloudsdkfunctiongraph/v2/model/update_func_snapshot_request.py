# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFuncSnapshotRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'action': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'action': 'action'
    }

    def __init__(self, function_urn=None, action=None):
        """UpdateFuncSnapshotRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param action: 禁用/启用
        :type action: str
        """
        
        

        self._function_urn = None
        self._action = None
        self.discriminator = None

        self.function_urn = function_urn
        self.action = action

    @property
    def function_urn(self):
        """Gets the function_urn of this UpdateFuncSnapshotRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this UpdateFuncSnapshotRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this UpdateFuncSnapshotRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this UpdateFuncSnapshotRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def action(self):
        """Gets the action of this UpdateFuncSnapshotRequest.

        禁用/启用

        :return: The action of this UpdateFuncSnapshotRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateFuncSnapshotRequest.

        禁用/启用

        :param action: The action of this UpdateFuncSnapshotRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, UpdateFuncSnapshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
