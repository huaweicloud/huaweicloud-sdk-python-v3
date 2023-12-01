# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionCollectStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func_urn': 'str',
        'state': 'str'
    }

    attribute_map = {
        'func_urn': 'func_urn',
        'state': 'state'
    }

    def __init__(self, func_urn=None, state=None):
        """UpdateFunctionCollectStateRequest

        The model defined in huaweicloud sdk

        :param func_urn: 函数URN
        :type func_urn: str
        :param state: 置顶状态
        :type state: str
        """
        
        

        self._func_urn = None
        self._state = None
        self.discriminator = None

        self.func_urn = func_urn
        self.state = state

    @property
    def func_urn(self):
        """Gets the func_urn of this UpdateFunctionCollectStateRequest.

        函数URN

        :return: The func_urn of this UpdateFunctionCollectStateRequest.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this UpdateFunctionCollectStateRequest.

        函数URN

        :param func_urn: The func_urn of this UpdateFunctionCollectStateRequest.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def state(self):
        """Gets the state of this UpdateFunctionCollectStateRequest.

        置顶状态

        :return: The state of this UpdateFunctionCollectStateRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateFunctionCollectStateRequest.

        置顶状态

        :param state: The state of this UpdateFunctionCollectStateRequest.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, UpdateFunctionCollectStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
