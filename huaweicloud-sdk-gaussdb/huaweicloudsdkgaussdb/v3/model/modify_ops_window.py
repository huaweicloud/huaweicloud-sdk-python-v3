# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyOpsWindow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, start_time=None, end_time=None):
        r"""ModifyOpsWindow

        The model defined in huaweicloud sdk

        :param start_time: 维护起始时间，UTC时间。
        :type start_time: str
        :param end_time: 维护结束时间，UTC时间。  说明：GuassDB(for MySQL)数据库的结束时间和开始时间必须为整点时间，且相隔四个小时。 
        :type end_time: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ModifyOpsWindow.

        维护起始时间，UTC时间。

        :return: The start_time of this ModifyOpsWindow.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ModifyOpsWindow.

        维护起始时间，UTC时间。

        :param start_time: The start_time of this ModifyOpsWindow.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ModifyOpsWindow.

        维护结束时间，UTC时间。  说明：GuassDB(for MySQL)数据库的结束时间和开始时间必须为整点时间，且相隔四个小时。 

        :return: The end_time of this ModifyOpsWindow.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ModifyOpsWindow.

        维护结束时间，UTC时间。  说明：GuassDB(for MySQL)数据库的结束时间和开始时间必须为整点时间，且相隔四个小时。 

        :param end_time: The end_time of this ModifyOpsWindow.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ModifyOpsWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
