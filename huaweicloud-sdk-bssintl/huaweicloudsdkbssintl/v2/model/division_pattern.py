# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DivisionPattern:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pattern_type': 'int',
        'division_type': 'int',
        'division_list': 'list[Division]'
    }

    attribute_map = {
        'pattern_type': 'pattern_type',
        'division_type': 'division_type',
        'division_list': 'division_list'
    }

    def __init__(self, pattern_type=None, division_type=None, division_list=None):
        r"""DivisionPattern

        The model defined in huaweicloud sdk

        :param pattern_type: 阶梯类型，1：一次分档模式、2：累计分档模式
        :type pattern_type: int
        :param division_type: 分档类型，1：STEP，按档拆分定价、2：TIER，按最终档定价
        :type division_type: int
        :param division_list: 阶梯分档列表
        :type division_list: list[:class:`huaweicloudsdkbssintl.v2.Division`]
        """
        
        

        self._pattern_type = None
        self._division_type = None
        self._division_list = None
        self.discriminator = None

        if pattern_type is not None:
            self.pattern_type = pattern_type
        if division_type is not None:
            self.division_type = division_type
        if division_list is not None:
            self.division_list = division_list

    @property
    def pattern_type(self):
        r"""Gets the pattern_type of this DivisionPattern.

        阶梯类型，1：一次分档模式、2：累计分档模式

        :return: The pattern_type of this DivisionPattern.
        :rtype: int
        """
        return self._pattern_type

    @pattern_type.setter
    def pattern_type(self, pattern_type):
        r"""Sets the pattern_type of this DivisionPattern.

        阶梯类型，1：一次分档模式、2：累计分档模式

        :param pattern_type: The pattern_type of this DivisionPattern.
        :type pattern_type: int
        """
        self._pattern_type = pattern_type

    @property
    def division_type(self):
        r"""Gets the division_type of this DivisionPattern.

        分档类型，1：STEP，按档拆分定价、2：TIER，按最终档定价

        :return: The division_type of this DivisionPattern.
        :rtype: int
        """
        return self._division_type

    @division_type.setter
    def division_type(self, division_type):
        r"""Sets the division_type of this DivisionPattern.

        分档类型，1：STEP，按档拆分定价、2：TIER，按最终档定价

        :param division_type: The division_type of this DivisionPattern.
        :type division_type: int
        """
        self._division_type = division_type

    @property
    def division_list(self):
        r"""Gets the division_list of this DivisionPattern.

        阶梯分档列表

        :return: The division_list of this DivisionPattern.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.Division`]
        """
        return self._division_list

    @division_list.setter
    def division_list(self, division_list):
        r"""Sets the division_list of this DivisionPattern.

        阶梯分档列表

        :param division_list: The division_list of this DivisionPattern.
        :type division_list: list[:class:`huaweicloudsdkbssintl.v2.Division`]
        """
        self._division_list = division_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DivisionPattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
