# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date_type': 'str',
        'date_start': 'str',
        'date_end': 'str'
    }

    attribute_map = {
        'date_type': 'date_type',
        'date_start': 'date_start',
        'date_end': 'date_end'
    }

    def __init__(self, date_type=None, date_start=None, date_end=None):
        r"""DateInfo

        The model defined in huaweicloud sdk

        :param date_type: **参数解释**： 日期类型，如每月1号执行则为1th。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type date_type: str
        :param date_start: **参数解释**： 开始时间，如：04:00:00。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type date_start: str
        :param date_end: **参数解释**： 结束时间，如：08:00:00。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type date_end: str
        """
        
        

        self._date_type = None
        self._date_start = None
        self._date_end = None
        self.discriminator = None

        if date_type is not None:
            self.date_type = date_type
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end

    @property
    def date_type(self):
        r"""Gets the date_type of this DateInfo.

        **参数解释**： 日期类型，如每月1号执行则为1th。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The date_type of this DateInfo.
        :rtype: str
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        r"""Sets the date_type of this DateInfo.

        **参数解释**： 日期类型，如每月1号执行则为1th。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param date_type: The date_type of this DateInfo.
        :type date_type: str
        """
        self._date_type = date_type

    @property
    def date_start(self):
        r"""Gets the date_start of this DateInfo.

        **参数解释**： 开始时间，如：04:00:00。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The date_start of this DateInfo.
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        r"""Sets the date_start of this DateInfo.

        **参数解释**： 开始时间，如：04:00:00。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param date_start: The date_start of this DateInfo.
        :type date_start: str
        """
        self._date_start = date_start

    @property
    def date_end(self):
        r"""Gets the date_end of this DateInfo.

        **参数解释**： 结束时间，如：08:00:00。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The date_end of this DateInfo.
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        r"""Sets the date_end of this DateInfo.

        **参数解释**： 结束时间，如：08:00:00。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param date_end: The date_end of this DateInfo.
        :type date_end: str
        """
        self._date_end = date_end

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
        if not isinstance(other, DateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
