# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordRequestArgs:

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
        'end_time': 'str',
        'format': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'format': 'format',
        'unit': 'unit'
    }

    def __init__(self, start_time=None, end_time=None, format=None, unit=None):
        r"""RecordRequestArgs

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param format: 格式
        :type format: str
        :param unit: 单位
        :type unit: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._format = None
        self._unit = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if format is not None:
            self.format = format
        if unit is not None:
            self.unit = unit

    @property
    def start_time(self):
        r"""Gets the start_time of this RecordRequestArgs.

        开始时间

        :return: The start_time of this RecordRequestArgs.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RecordRequestArgs.

        开始时间

        :param start_time: The start_time of this RecordRequestArgs.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RecordRequestArgs.

        结束时间

        :return: The end_time of this RecordRequestArgs.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RecordRequestArgs.

        结束时间

        :param end_time: The end_time of this RecordRequestArgs.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def format(self):
        r"""Gets the format of this RecordRequestArgs.

        格式

        :return: The format of this RecordRequestArgs.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this RecordRequestArgs.

        格式

        :param format: The format of this RecordRequestArgs.
        :type format: str
        """
        self._format = format

    @property
    def unit(self):
        r"""Gets the unit of this RecordRequestArgs.

        单位

        :return: The unit of this RecordRequestArgs.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this RecordRequestArgs.

        单位

        :param unit: The unit of this RecordRequestArgs.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, RecordRequestArgs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
