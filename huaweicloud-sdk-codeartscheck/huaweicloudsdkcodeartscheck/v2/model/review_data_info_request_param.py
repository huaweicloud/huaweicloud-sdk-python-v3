# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewDataInfoRequestParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_type': 'str',
        'is_check': 'int',
        'name': 'str',
        'value': 'int'
    }

    attribute_map = {
        'compare_type': 'compareType',
        'is_check': 'isCheck',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, compare_type=None, is_check=None, name=None, value=None):
        r"""ReviewDataInfoRequestParam

        The model defined in huaweicloud sdk

        :param compare_type: **参数解释：** 运算逻辑。 **约束限制：** 不涉及。 **取值范围：** 取值为\&quot;≤\&quot;。 **默认取值：** 不涉及。
        :type compare_type: str
        :param is_check: **参数解释：** 门禁开关。 **约束限制：** 不涉及。 **取值范围：** - 0：关闭门禁。 - 1：打开门禁。 **默认取值：** 不涉及。
        :type is_check: int
        :param name: **参数解释：** 门禁项。 **约束限制：** 不涉及。 **取值范围：** - 致命问题数。 - 严重问题数。 - 一般问题数。 - 提示问题数。 **默认取值：** 不涉及。
        :type name: str
        :param value: **参数解释：** 门禁阈值。 **约束限制：** 不涉及。 **取值范围：** ≥0 **默认取值：** 不涉及。
        :type value: int
        """
        
        

        self._compare_type = None
        self._is_check = None
        self._name = None
        self._value = None
        self.discriminator = None

        self.compare_type = compare_type
        self.is_check = is_check
        self.name = name
        self.value = value

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ReviewDataInfoRequestParam.

        **参数解释：** 运算逻辑。 **约束限制：** 不涉及。 **取值范围：** 取值为\"≤\"。 **默认取值：** 不涉及。

        :return: The compare_type of this ReviewDataInfoRequestParam.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ReviewDataInfoRequestParam.

        **参数解释：** 运算逻辑。 **约束限制：** 不涉及。 **取值范围：** 取值为\"≤\"。 **默认取值：** 不涉及。

        :param compare_type: The compare_type of this ReviewDataInfoRequestParam.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def is_check(self):
        r"""Gets the is_check of this ReviewDataInfoRequestParam.

        **参数解释：** 门禁开关。 **约束限制：** 不涉及。 **取值范围：** - 0：关闭门禁。 - 1：打开门禁。 **默认取值：** 不涉及。

        :return: The is_check of this ReviewDataInfoRequestParam.
        :rtype: int
        """
        return self._is_check

    @is_check.setter
    def is_check(self, is_check):
        r"""Sets the is_check of this ReviewDataInfoRequestParam.

        **参数解释：** 门禁开关。 **约束限制：** 不涉及。 **取值范围：** - 0：关闭门禁。 - 1：打开门禁。 **默认取值：** 不涉及。

        :param is_check: The is_check of this ReviewDataInfoRequestParam.
        :type is_check: int
        """
        self._is_check = is_check

    @property
    def name(self):
        r"""Gets the name of this ReviewDataInfoRequestParam.

        **参数解释：** 门禁项。 **约束限制：** 不涉及。 **取值范围：** - 致命问题数。 - 严重问题数。 - 一般问题数。 - 提示问题数。 **默认取值：** 不涉及。

        :return: The name of this ReviewDataInfoRequestParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ReviewDataInfoRequestParam.

        **参数解释：** 门禁项。 **约束限制：** 不涉及。 **取值范围：** - 致命问题数。 - 严重问题数。 - 一般问题数。 - 提示问题数。 **默认取值：** 不涉及。

        :param name: The name of this ReviewDataInfoRequestParam.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this ReviewDataInfoRequestParam.

        **参数解释：** 门禁阈值。 **约束限制：** 不涉及。 **取值范围：** ≥0 **默认取值：** 不涉及。

        :return: The value of this ReviewDataInfoRequestParam.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ReviewDataInfoRequestParam.

        **参数解释：** 门禁阈值。 **约束限制：** 不涉及。 **取值范围：** ≥0 **默认取值：** 不涉及。

        :param value: The value of this ReviewDataInfoRequestParam.
        :type value: int
        """
        self._value = value

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
        if not isinstance(other, ReviewDataInfoRequestParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
