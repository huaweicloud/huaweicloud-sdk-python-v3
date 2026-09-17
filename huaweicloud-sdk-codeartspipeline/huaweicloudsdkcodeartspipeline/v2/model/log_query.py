# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_offset': 'int',
        'end_offset': 'int',
        'limit': 'int',
        'sort': 'str',
        'offset': 'int',
        'level': 'str'
    }

    attribute_map = {
        'start_offset': 'start_offset',
        'end_offset': 'end_offset',
        'limit': 'limit',
        'sort': 'sort',
        'offset': 'offset',
        'level': 'level'
    }

    def __init__(self, start_offset=None, end_offset=None, limit=None, sort=None, offset=None, level=None):
        r"""LogQuery

        The model defined in huaweicloud sdk

        :param start_offset: **参数解释**： 日志起始偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type start_offset: int
        :param end_offset: **参数解释**： 日志结束偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type end_offset: int
        :param limit: **参数解释**： 最大日志行数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type limit: int
        :param sort: **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序 **默认取值**： 不涉及。 
        :type sort: str
        :param offset: **参数解释**： 日志偏移量。仅查询Jenkins日志时使用，其余场景请使用start_offset和end_offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type offset: int
        :param level: **参数解释**： 日志级别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type level: str
        """
        
        

        self._start_offset = None
        self._end_offset = None
        self._limit = None
        self._sort = None
        self._offset = None
        self._level = None
        self.discriminator = None

        if start_offset is not None:
            self.start_offset = start_offset
        if end_offset is not None:
            self.end_offset = end_offset
        self.limit = limit
        self.sort = sort
        if offset is not None:
            self.offset = offset
        if level is not None:
            self.level = level

    @property
    def start_offset(self):
        r"""Gets the start_offset of this LogQuery.

        **参数解释**： 日志起始偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The start_offset of this LogQuery.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        r"""Sets the start_offset of this LogQuery.

        **参数解释**： 日志起始偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param start_offset: The start_offset of this LogQuery.
        :type start_offset: int
        """
        self._start_offset = start_offset

    @property
    def end_offset(self):
        r"""Gets the end_offset of this LogQuery.

        **参数解释**： 日志结束偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The end_offset of this LogQuery.
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        r"""Sets the end_offset of this LogQuery.

        **参数解释**： 日志结束偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param end_offset: The end_offset of this LogQuery.
        :type end_offset: int
        """
        self._end_offset = end_offset

    @property
    def limit(self):
        r"""Gets the limit of this LogQuery.

        **参数解释**： 最大日志行数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The limit of this LogQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this LogQuery.

        **参数解释**： 最大日志行数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param limit: The limit of this LogQuery.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        r"""Gets the sort of this LogQuery.

        **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序 **默认取值**： 不涉及。 

        :return: The sort of this LogQuery.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this LogQuery.

        **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序 **默认取值**： 不涉及。 

        :param sort: The sort of this LogQuery.
        :type sort: str
        """
        self._sort = sort

    @property
    def offset(self):
        r"""Gets the offset of this LogQuery.

        **参数解释**： 日志偏移量。仅查询Jenkins日志时使用，其余场景请使用start_offset和end_offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The offset of this LogQuery.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this LogQuery.

        **参数解释**： 日志偏移量。仅查询Jenkins日志时使用，其余场景请使用start_offset和end_offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param offset: The offset of this LogQuery.
        :type offset: int
        """
        self._offset = offset

    @property
    def level(self):
        r"""Gets the level of this LogQuery.

        **参数解释**： 日志级别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The level of this LogQuery.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this LogQuery.

        **参数解释**： 日志级别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param level: The level of this LogQuery.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, LogQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
