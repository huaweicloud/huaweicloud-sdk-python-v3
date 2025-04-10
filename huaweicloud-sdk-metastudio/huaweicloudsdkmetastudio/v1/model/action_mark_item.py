# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionMarkItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_start_time': 'str',
        'action_end_time': 'str',
        'action_type': 'str'
    }

    attribute_map = {
        'action_start_time': 'action_start_time',
        'action_end_time': 'action_end_time',
        'action_type': 'action_type'
    }

    def __init__(self, action_start_time=None, action_end_time=None, action_type=None):
        r"""ActionMarkItem

        The model defined in huaweicloud sdk

        :param action_start_time: 选取推理数据预处理视频起始时间。格式：“HH:MM:SS.mmm”。
        :type action_start_time: str
        :param action_end_time: 选取推理数据预处理视频结束时间。格式：“HH:MM:SS.mmm”。
        :type action_end_time: str
        :param action_type: 动作类型。 * SILENCE: 静默 * ACTION：动作
        :type action_type: str
        """
        
        

        self._action_start_time = None
        self._action_end_time = None
        self._action_type = None
        self.discriminator = None

        if action_start_time is not None:
            self.action_start_time = action_start_time
        if action_end_time is not None:
            self.action_end_time = action_end_time
        if action_type is not None:
            self.action_type = action_type

    @property
    def action_start_time(self):
        r"""Gets the action_start_time of this ActionMarkItem.

        选取推理数据预处理视频起始时间。格式：“HH:MM:SS.mmm”。

        :return: The action_start_time of this ActionMarkItem.
        :rtype: str
        """
        return self._action_start_time

    @action_start_time.setter
    def action_start_time(self, action_start_time):
        r"""Sets the action_start_time of this ActionMarkItem.

        选取推理数据预处理视频起始时间。格式：“HH:MM:SS.mmm”。

        :param action_start_time: The action_start_time of this ActionMarkItem.
        :type action_start_time: str
        """
        self._action_start_time = action_start_time

    @property
    def action_end_time(self):
        r"""Gets the action_end_time of this ActionMarkItem.

        选取推理数据预处理视频结束时间。格式：“HH:MM:SS.mmm”。

        :return: The action_end_time of this ActionMarkItem.
        :rtype: str
        """
        return self._action_end_time

    @action_end_time.setter
    def action_end_time(self, action_end_time):
        r"""Sets the action_end_time of this ActionMarkItem.

        选取推理数据预处理视频结束时间。格式：“HH:MM:SS.mmm”。

        :param action_end_time: The action_end_time of this ActionMarkItem.
        :type action_end_time: str
        """
        self._action_end_time = action_end_time

    @property
    def action_type(self):
        r"""Gets the action_type of this ActionMarkItem.

        动作类型。 * SILENCE: 静默 * ACTION：动作

        :return: The action_type of this ActionMarkItem.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this ActionMarkItem.

        动作类型。 * SILENCE: 静默 * ACTION：动作

        :param action_type: The action_type of this ActionMarkItem.
        :type action_type: str
        """
        self._action_type = action_type

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
        if not isinstance(other, ActionMarkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
