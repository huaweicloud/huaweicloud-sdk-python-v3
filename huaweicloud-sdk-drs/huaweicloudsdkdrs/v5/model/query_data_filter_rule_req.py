# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDataFilterRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter_type': 'str',
        'is_all_rules': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'filter_type': 'filter_type',
        'is_all_rules': 'is_all_rules',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, filter_type=None, is_all_rules=None, limit=None, offset=None):
        r"""QueryDataFilterRuleReq

        The model defined in huaweicloud sdk

        :param filter_type: 数据过滤类型，取值分别是common、config。common表示简单条件过滤， config表示关联表过滤
        :type filter_type: str
        :param is_all_rules: 标记是否查询全部过滤规则（含已同步和未下发的），即 true（查询所有）、false（仅查询已同步）
        :type is_all_rules: bool
        :param limit: 查询返回记录的数量限制。
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录。
        :type offset: int
        """
        
        

        self._filter_type = None
        self._is_all_rules = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.filter_type = filter_type
        if is_all_rules is not None:
            self.is_all_rules = is_all_rules
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def filter_type(self):
        r"""Gets the filter_type of this QueryDataFilterRuleReq.

        数据过滤类型，取值分别是common、config。common表示简单条件过滤， config表示关联表过滤

        :return: The filter_type of this QueryDataFilterRuleReq.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        r"""Sets the filter_type of this QueryDataFilterRuleReq.

        数据过滤类型，取值分别是common、config。common表示简单条件过滤， config表示关联表过滤

        :param filter_type: The filter_type of this QueryDataFilterRuleReq.
        :type filter_type: str
        """
        self._filter_type = filter_type

    @property
    def is_all_rules(self):
        r"""Gets the is_all_rules of this QueryDataFilterRuleReq.

        标记是否查询全部过滤规则（含已同步和未下发的），即 true（查询所有）、false（仅查询已同步）

        :return: The is_all_rules of this QueryDataFilterRuleReq.
        :rtype: bool
        """
        return self._is_all_rules

    @is_all_rules.setter
    def is_all_rules(self, is_all_rules):
        r"""Sets the is_all_rules of this QueryDataFilterRuleReq.

        标记是否查询全部过滤规则（含已同步和未下发的），即 true（查询所有）、false（仅查询已同步）

        :param is_all_rules: The is_all_rules of this QueryDataFilterRuleReq.
        :type is_all_rules: bool
        """
        self._is_all_rules = is_all_rules

    @property
    def limit(self):
        r"""Gets the limit of this QueryDataFilterRuleReq.

        查询返回记录的数量限制。

        :return: The limit of this QueryDataFilterRuleReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QueryDataFilterRuleReq.

        查询返回记录的数量限制。

        :param limit: The limit of this QueryDataFilterRuleReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this QueryDataFilterRuleReq.

        偏移量，表示查询该偏移量后面的记录。

        :return: The offset of this QueryDataFilterRuleReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QueryDataFilterRuleReq.

        偏移量，表示查询该偏移量后面的记录。

        :param offset: The offset of this QueryDataFilterRuleReq.
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
        if not isinstance(other, QueryDataFilterRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
