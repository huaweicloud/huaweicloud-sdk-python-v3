# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmDetailDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'int',
        'end': 'int',
        'int_target': 'int',
        'string_target': 'str'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'int_target': 'int_target',
        'string_target': 'string_target'
    }

    def __init__(self, start=None, end=None, int_target=None, string_target=None):
        r"""AlgorithmDetailDTO

        The model defined in huaweicloud sdk

        :param start: 开始位数，该值需要大于0且小于end值。
        :type start: int
        :param end: 结束位数，该值需要大于或等于start值。
        :type end: int
        :param int_target: 数值类型。
        :type int_target: int
        :param string_target: 字符串类型。可输入参数为\&quot;*\&quot;或者\&quot;#\&quot;。
        :type string_target: str
        """
        
        

        self._start = None
        self._end = None
        self._int_target = None
        self._string_target = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if int_target is not None:
            self.int_target = int_target
        if string_target is not None:
            self.string_target = string_target

    @property
    def start(self):
        r"""Gets the start of this AlgorithmDetailDTO.

        开始位数，该值需要大于0且小于end值。

        :return: The start of this AlgorithmDetailDTO.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this AlgorithmDetailDTO.

        开始位数，该值需要大于0且小于end值。

        :param start: The start of this AlgorithmDetailDTO.
        :type start: int
        """
        self._start = start

    @property
    def end(self):
        r"""Gets the end of this AlgorithmDetailDTO.

        结束位数，该值需要大于或等于start值。

        :return: The end of this AlgorithmDetailDTO.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this AlgorithmDetailDTO.

        结束位数，该值需要大于或等于start值。

        :param end: The end of this AlgorithmDetailDTO.
        :type end: int
        """
        self._end = end

    @property
    def int_target(self):
        r"""Gets the int_target of this AlgorithmDetailDTO.

        数值类型。

        :return: The int_target of this AlgorithmDetailDTO.
        :rtype: int
        """
        return self._int_target

    @int_target.setter
    def int_target(self, int_target):
        r"""Sets the int_target of this AlgorithmDetailDTO.

        数值类型。

        :param int_target: The int_target of this AlgorithmDetailDTO.
        :type int_target: int
        """
        self._int_target = int_target

    @property
    def string_target(self):
        r"""Gets the string_target of this AlgorithmDetailDTO.

        字符串类型。可输入参数为\"*\"或者\"#\"。

        :return: The string_target of this AlgorithmDetailDTO.
        :rtype: str
        """
        return self._string_target

    @string_target.setter
    def string_target(self, string_target):
        r"""Sets the string_target of this AlgorithmDetailDTO.

        字符串类型。可输入参数为\"*\"或者\"#\"。

        :param string_target: The string_target of this AlgorithmDetailDTO.
        :type string_target: str
        """
        self._string_target = string_target

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
        if not isinstance(other, AlgorithmDetailDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
