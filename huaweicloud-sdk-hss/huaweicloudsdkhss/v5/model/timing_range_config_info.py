# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimingRangeConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_range': 'str',
        'description': 'str'
    }

    attribute_map = {
        'time_range': 'time_range',
        'description': 'description'
    }

    def __init__(self, time_range=None, description=None):
        r"""TimingRangeConfigInfo

        The model defined in huaweicloud sdk

        :param time_range: 时间范围
        :type time_range: str
        :param description: 描述
        :type description: str
        """
        
        

        self._time_range = None
        self._description = None
        self.discriminator = None

        if time_range is not None:
            self.time_range = time_range
        if description is not None:
            self.description = description

    @property
    def time_range(self):
        r"""Gets the time_range of this TimingRangeConfigInfo.

        时间范围

        :return: The time_range of this TimingRangeConfigInfo.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this TimingRangeConfigInfo.

        时间范围

        :param time_range: The time_range of this TimingRangeConfigInfo.
        :type time_range: str
        """
        self._time_range = time_range

    @property
    def description(self):
        r"""Gets the description of this TimingRangeConfigInfo.

        描述

        :return: The description of this TimingRangeConfigInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TimingRangeConfigInfo.

        描述

        :param description: The description of this TimingRangeConfigInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, TimingRangeConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
