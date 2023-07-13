# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppState:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'state': 'state',
        'update_time': 'update_time'
    }

    def __init__(self, state=None, update_time=None):
        """AppState

        The model defined in huaweicloud sdk

        :param state: 状态 - ACTIVATION：开启 - DEACTIVATION：停用 - ARREARS：欠费 - DELETED：已删除 
        :type state: str
        :param update_time: app鉴权的更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type update_time: str
        """
        
        

        self._state = None
        self._update_time = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if update_time is not None:
            self.update_time = update_time

    @property
    def state(self):
        """Gets the state of this AppState.

        状态 - ACTIVATION：开启 - DEACTIVATION：停用 - ARREARS：欠费 - DELETED：已删除 

        :return: The state of this AppState.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AppState.

        状态 - ACTIVATION：开启 - DEACTIVATION：停用 - ARREARS：欠费 - DELETED：已删除 

        :param state: The state of this AppState.
        :type state: str
        """
        self._state = state

    @property
    def update_time(self):
        """Gets the update_time of this AppState.

        app鉴权的更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The update_time of this AppState.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AppState.

        app鉴权的更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param update_time: The update_time of this AppState.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, AppState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
