# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTimeDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_time': 'int',
        'data_io_time': 'int',
        'other_time': 'int'
    }

    attribute_map = {
        'cpu_time': 'cpu_time',
        'data_io_time': 'data_io_time',
        'other_time': 'other_time'
    }

    def __init__(self, cpu_time=None, data_io_time=None, other_time=None):
        r"""ResourceTimeDetails

        The model defined in huaweicloud sdk

        :param cpu_time: **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。
        :type cpu_time: int
        :param data_io_time: **参数解释**: IO上的时间花费（单位：微秒）。 **取值范围**: 不涉及。
        :type data_io_time: int
        :param other_time: **参数解释**: 其余耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type other_time: int
        """
        
        

        self._cpu_time = None
        self._data_io_time = None
        self._other_time = None
        self.discriminator = None

        self.cpu_time = cpu_time
        self.data_io_time = data_io_time
        self.other_time = other_time

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this ResourceTimeDetails.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The cpu_time of this ResourceTimeDetails.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this ResourceTimeDetails.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :param cpu_time: The cpu_time of this ResourceTimeDetails.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

    @property
    def data_io_time(self):
        r"""Gets the data_io_time of this ResourceTimeDetails.

        **参数解释**: IO上的时间花费（单位：微秒）。 **取值范围**: 不涉及。

        :return: The data_io_time of this ResourceTimeDetails.
        :rtype: int
        """
        return self._data_io_time

    @data_io_time.setter
    def data_io_time(self, data_io_time):
        r"""Sets the data_io_time of this ResourceTimeDetails.

        **参数解释**: IO上的时间花费（单位：微秒）。 **取值范围**: 不涉及。

        :param data_io_time: The data_io_time of this ResourceTimeDetails.
        :type data_io_time: int
        """
        self._data_io_time = data_io_time

    @property
    def other_time(self):
        r"""Gets the other_time of this ResourceTimeDetails.

        **参数解释**: 其余耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The other_time of this ResourceTimeDetails.
        :rtype: int
        """
        return self._other_time

    @other_time.setter
    def other_time(self, other_time):
        r"""Sets the other_time of this ResourceTimeDetails.

        **参数解释**: 其余耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param other_time: The other_time of this ResourceTimeDetails.
        :type other_time: int
        """
        self._other_time = other_time

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
        if not isinstance(other, ResourceTimeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
