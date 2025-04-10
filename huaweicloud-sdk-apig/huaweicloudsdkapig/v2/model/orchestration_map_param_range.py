# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrchestrationMapParamRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'range_start': 'str',
        'range_end': 'str'
    }

    attribute_map = {
        'range_start': 'range_start',
        'range_end': 'range_end'
    }

    def __init__(self, range_start=None, range_end=None):
        r"""OrchestrationMapParamRange

        The model defined in huaweicloud sdk

        :param range_start: 区间起始值。  为可以转换成integer的string，转换后的range_start的范围为0-9223372036854775807， range_start不大于range_end。
        :type range_start: str
        :param range_end: 区间终止值。  为可以转换成integer的string，转换后的range_end的范围为0-9223372036854775807， range_start不大于range_end。
        :type range_end: str
        """
        
        

        self._range_start = None
        self._range_end = None
        self.discriminator = None

        if range_start is not None:
            self.range_start = range_start
        if range_end is not None:
            self.range_end = range_end

    @property
    def range_start(self):
        r"""Gets the range_start of this OrchestrationMapParamRange.

        区间起始值。  为可以转换成integer的string，转换后的range_start的范围为0-9223372036854775807， range_start不大于range_end。

        :return: The range_start of this OrchestrationMapParamRange.
        :rtype: str
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        r"""Sets the range_start of this OrchestrationMapParamRange.

        区间起始值。  为可以转换成integer的string，转换后的range_start的范围为0-9223372036854775807， range_start不大于range_end。

        :param range_start: The range_start of this OrchestrationMapParamRange.
        :type range_start: str
        """
        self._range_start = range_start

    @property
    def range_end(self):
        r"""Gets the range_end of this OrchestrationMapParamRange.

        区间终止值。  为可以转换成integer的string，转换后的range_end的范围为0-9223372036854775807， range_start不大于range_end。

        :return: The range_end of this OrchestrationMapParamRange.
        :rtype: str
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        r"""Sets the range_end of this OrchestrationMapParamRange.

        区间终止值。  为可以转换成integer的string，转换后的range_end的范围为0-9223372036854775807， range_start不大于range_end。

        :param range_end: The range_end of this OrchestrationMapParamRange.
        :type range_end: str
        """
        self._range_end = range_end

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
        if not isinstance(other, OrchestrationMapParamRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
