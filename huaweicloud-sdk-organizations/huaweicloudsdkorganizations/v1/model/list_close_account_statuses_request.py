# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloseAccountStatusesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'states': 'list[str]'
    }

    attribute_map = {
        'states': 'states'
    }

    def __init__(self, states=None):
        """ListCloseAccountStatusesRequest

        The model defined in huaweicloud sdk

        :param states: 要包含在响应中的一个或多个状态的列表。如果此参数不存在，则所有请求都包含在响应中。
        :type states: list[str]
        """
        
        

        self._states = None
        self.discriminator = None

        if states is not None:
            self.states = states

    @property
    def states(self):
        """Gets the states of this ListCloseAccountStatusesRequest.

        要包含在响应中的一个或多个状态的列表。如果此参数不存在，则所有请求都包含在响应中。

        :return: The states of this ListCloseAccountStatusesRequest.
        :rtype: list[str]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this ListCloseAccountStatusesRequest.

        要包含在响应中的一个或多个状态的列表。如果此参数不存在，则所有请求都包含在响应中。

        :param states: The states of this ListCloseAccountStatusesRequest.
        :type states: list[str]
        """
        self._states = states

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
        if not isinstance(other, ListCloseAccountStatusesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
