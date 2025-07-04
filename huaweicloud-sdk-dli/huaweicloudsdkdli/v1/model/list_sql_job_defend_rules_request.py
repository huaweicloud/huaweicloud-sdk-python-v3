# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlJobDefendRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'rule_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'rule_name': 'rule_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, queue_name=None, rule_name=None, offset=None, limit=None):
        r"""ListSqlJobDefendRulesRequest

        The model defined in huaweicloud sdk

        :param queue_name: 队列名称。
        :type queue_name: str
        :param rule_name: 规则名称。
        :type rule_name: str
        :param offset: 分页偏移量。
        :type offset: int
        :param limit: 分页个数。
        :type limit: int
        """
        
        

        self._queue_name = None
        self._rule_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if queue_name is not None:
            self.queue_name = queue_name
        if rule_name is not None:
            self.rule_name = rule_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ListSqlJobDefendRulesRequest.

        队列名称。

        :return: The queue_name of this ListSqlJobDefendRulesRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ListSqlJobDefendRulesRequest.

        队列名称。

        :param queue_name: The queue_name of this ListSqlJobDefendRulesRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ListSqlJobDefendRulesRequest.

        规则名称。

        :return: The rule_name of this ListSqlJobDefendRulesRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ListSqlJobDefendRulesRequest.

        规则名称。

        :param rule_name: The rule_name of this ListSqlJobDefendRulesRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def offset(self):
        r"""Gets the offset of this ListSqlJobDefendRulesRequest.

        分页偏移量。

        :return: The offset of this ListSqlJobDefendRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSqlJobDefendRulesRequest.

        分页偏移量。

        :param offset: The offset of this ListSqlJobDefendRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSqlJobDefendRulesRequest.

        分页个数。

        :return: The limit of this ListSqlJobDefendRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSqlJobDefendRulesRequest.

        分页个数。

        :param limit: The limit of this ListSqlJobDefendRulesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSqlJobDefendRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
