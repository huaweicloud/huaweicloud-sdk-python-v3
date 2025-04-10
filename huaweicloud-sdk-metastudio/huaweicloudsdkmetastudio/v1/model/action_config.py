# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_interval': 'float'
    }

    attribute_map = {
        'action_interval': 'action_interval'
    }

    def __init__(self, action_interval=None):
        r"""ActionConfig

        The model defined in huaweicloud sdk

        :param action_interval: 算法自动插入无语义动作的时间间隔。这个参数填0或者不填默认是间隔4秒，设置成255时不自动插入无语义动作。
        :type action_interval: float
        """
        
        

        self._action_interval = None
        self.discriminator = None

        if action_interval is not None:
            self.action_interval = action_interval

    @property
    def action_interval(self):
        r"""Gets the action_interval of this ActionConfig.

        算法自动插入无语义动作的时间间隔。这个参数填0或者不填默认是间隔4秒，设置成255时不自动插入无语义动作。

        :return: The action_interval of this ActionConfig.
        :rtype: float
        """
        return self._action_interval

    @action_interval.setter
    def action_interval(self, action_interval):
        r"""Sets the action_interval of this ActionConfig.

        算法自动插入无语义动作的时间间隔。这个参数填0或者不填默认是间隔4秒，设置成255时不自动插入无语义动作。

        :param action_interval: The action_interval of this ActionConfig.
        :type action_interval: float
        """
        self._action_interval = action_interval

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
        if not isinstance(other, ActionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
