# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProgressInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'completed': 'str',
        'remaining_time': 'str'
    }

    attribute_map = {
        'completed': 'completed',
        'remaining_time': 'remaining_time'
    }

    def __init__(self, completed=None, remaining_time=None):
        """ProgressInfo

        The model defined in huaweicloud sdk

        :param completed: 完成进度
        :type completed: str
        :param remaining_time: 预计剩余时间
        :type remaining_time: str
        """
        
        

        self._completed = None
        self._remaining_time = None
        self.discriminator = None

        if completed is not None:
            self.completed = completed
        if remaining_time is not None:
            self.remaining_time = remaining_time

    @property
    def completed(self):
        """Gets the completed of this ProgressInfo.

        完成进度

        :return: The completed of this ProgressInfo.
        :rtype: str
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this ProgressInfo.

        完成进度

        :param completed: The completed of this ProgressInfo.
        :type completed: str
        """
        self._completed = completed

    @property
    def remaining_time(self):
        """Gets the remaining_time of this ProgressInfo.

        预计剩余时间

        :return: The remaining_time of this ProgressInfo.
        :rtype: str
        """
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, remaining_time):
        """Sets the remaining_time of this ProgressInfo.

        预计剩余时间

        :param remaining_time: The remaining_time of this ProgressInfo.
        :type remaining_time: str
        """
        self._remaining_time = remaining_time

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
        if not isinstance(other, ProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
