# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDbPositionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reset_position_time': 'str'
    }

    attribute_map = {
        'reset_position_time': 'reset_position_time'
    }

    def __init__(self, reset_position_time=None):
        """QueryDbPositionReq

        The model defined in huaweicloud sdk

        :param reset_position_time: 重置位点时间, 使用UTC时间 示例：2023-09-19 15:00:00，UTC时间是2023-09-19T07:00:00Z
        :type reset_position_time: str
        """
        
        

        self._reset_position_time = None
        self.discriminator = None

        self.reset_position_time = reset_position_time

    @property
    def reset_position_time(self):
        """Gets the reset_position_time of this QueryDbPositionReq.

        重置位点时间, 使用UTC时间 示例：2023-09-19 15:00:00，UTC时间是2023-09-19T07:00:00Z

        :return: The reset_position_time of this QueryDbPositionReq.
        :rtype: str
        """
        return self._reset_position_time

    @reset_position_time.setter
    def reset_position_time(self, reset_position_time):
        """Sets the reset_position_time of this QueryDbPositionReq.

        重置位点时间, 使用UTC时间 示例：2023-09-19 15:00:00，UTC时间是2023-09-19T07:00:00Z

        :param reset_position_time: The reset_position_time of this QueryDbPositionReq.
        :type reset_position_time: str
        """
        self._reset_position_time = reset_position_time

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
        if not isinstance(other, QueryDbPositionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
