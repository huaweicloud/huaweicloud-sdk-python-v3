# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemLinesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'locale': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'locale': 'locale',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, locale=None, limit=None, offset=None):
        r"""ListSystemLinesRequest

        The model defined in huaweicloud sdk

        :param locale: **参数解释：** 指定显示语言。 **约束限制：** 不涉及。 **取值范围：** - zh-cn：中文 - en-us：英语             - es-us：西班牙语 - pt-br：葡萄牙语 **默认取值：** zh-cn
        :type locale: str
        :param limit: **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~1000。 **默认取值：** 1000
        :type limit: int
        :param offset: **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0
        :type offset: int
        """
        
        

        self._locale = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if locale is not None:
            self.locale = locale
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def locale(self):
        r"""Gets the locale of this ListSystemLinesRequest.

        **参数解释：** 指定显示语言。 **约束限制：** 不涉及。 **取值范围：** - zh-cn：中文 - en-us：英语             - es-us：西班牙语 - pt-br：葡萄牙语 **默认取值：** zh-cn

        :return: The locale of this ListSystemLinesRequest.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this ListSystemLinesRequest.

        **参数解释：** 指定显示语言。 **约束限制：** 不涉及。 **取值范围：** - zh-cn：中文 - en-us：英语             - es-us：西班牙语 - pt-br：葡萄牙语 **默认取值：** zh-cn

        :param locale: The locale of this ListSystemLinesRequest.
        :type locale: str
        """
        self._locale = locale

    @property
    def limit(self):
        r"""Gets the limit of this ListSystemLinesRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~1000。 **默认取值：** 1000

        :return: The limit of this ListSystemLinesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSystemLinesRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~1000。 **默认取值：** 1000

        :param limit: The limit of this ListSystemLinesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSystemLinesRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :return: The offset of this ListSystemLinesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSystemLinesRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :param offset: The offset of this ListSystemLinesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListSystemLinesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
