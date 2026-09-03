# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlTplTrendItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_at': 'int',
        'query_time_in500ms': 'int',
        'query_time_in100ms': 'int',
        'query_time_in1s': 'int',
        'query_time_over1s': 'int',
        'query_executions': 'int'
    }

    attribute_map = {
        'execute_at': 'execute_at',
        'query_time_in500ms': 'query_time_in500ms',
        'query_time_in100ms': 'query_time_in100ms',
        'query_time_in1s': 'query_time_in1s',
        'query_time_over1s': 'query_time_over1s',
        'query_executions': 'query_executions'
    }

    def __init__(self, execute_at=None, query_time_in500ms=None, query_time_in100ms=None, query_time_in1s=None, query_time_over1s=None, query_executions=None):
        r"""SqlTplTrendItem

        The model defined in huaweicloud sdk

        :param execute_at: 执行时间 ms
        :type execute_at: int
        :param query_time_in500ms: 耗时在500ms的个数
        :type query_time_in500ms: int
        :param query_time_in100ms: 耗时在100ms的个数
        :type query_time_in100ms: int
        :param query_time_in1s: 耗时在1s的个数
        :type query_time_in1s: int
        :param query_time_over1s: 耗时超过1s的个数
        :type query_time_over1s: int
        :param query_executions: 总个数
        :type query_executions: int
        """
        
        

        self._execute_at = None
        self._query_time_in500ms = None
        self._query_time_in100ms = None
        self._query_time_in1s = None
        self._query_time_over1s = None
        self._query_executions = None
        self.discriminator = None

        if execute_at is not None:
            self.execute_at = execute_at
        if query_time_in500ms is not None:
            self.query_time_in500ms = query_time_in500ms
        if query_time_in100ms is not None:
            self.query_time_in100ms = query_time_in100ms
        if query_time_in1s is not None:
            self.query_time_in1s = query_time_in1s
        if query_time_over1s is not None:
            self.query_time_over1s = query_time_over1s
        if query_executions is not None:
            self.query_executions = query_executions

    @property
    def execute_at(self):
        r"""Gets the execute_at of this SqlTplTrendItem.

        执行时间 ms

        :return: The execute_at of this SqlTplTrendItem.
        :rtype: int
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        r"""Sets the execute_at of this SqlTplTrendItem.

        执行时间 ms

        :param execute_at: The execute_at of this SqlTplTrendItem.
        :type execute_at: int
        """
        self._execute_at = execute_at

    @property
    def query_time_in500ms(self):
        r"""Gets the query_time_in500ms of this SqlTplTrendItem.

        耗时在500ms的个数

        :return: The query_time_in500ms of this SqlTplTrendItem.
        :rtype: int
        """
        return self._query_time_in500ms

    @query_time_in500ms.setter
    def query_time_in500ms(self, query_time_in500ms):
        r"""Sets the query_time_in500ms of this SqlTplTrendItem.

        耗时在500ms的个数

        :param query_time_in500ms: The query_time_in500ms of this SqlTplTrendItem.
        :type query_time_in500ms: int
        """
        self._query_time_in500ms = query_time_in500ms

    @property
    def query_time_in100ms(self):
        r"""Gets the query_time_in100ms of this SqlTplTrendItem.

        耗时在100ms的个数

        :return: The query_time_in100ms of this SqlTplTrendItem.
        :rtype: int
        """
        return self._query_time_in100ms

    @query_time_in100ms.setter
    def query_time_in100ms(self, query_time_in100ms):
        r"""Sets the query_time_in100ms of this SqlTplTrendItem.

        耗时在100ms的个数

        :param query_time_in100ms: The query_time_in100ms of this SqlTplTrendItem.
        :type query_time_in100ms: int
        """
        self._query_time_in100ms = query_time_in100ms

    @property
    def query_time_in1s(self):
        r"""Gets the query_time_in1s of this SqlTplTrendItem.

        耗时在1s的个数

        :return: The query_time_in1s of this SqlTplTrendItem.
        :rtype: int
        """
        return self._query_time_in1s

    @query_time_in1s.setter
    def query_time_in1s(self, query_time_in1s):
        r"""Sets the query_time_in1s of this SqlTplTrendItem.

        耗时在1s的个数

        :param query_time_in1s: The query_time_in1s of this SqlTplTrendItem.
        :type query_time_in1s: int
        """
        self._query_time_in1s = query_time_in1s

    @property
    def query_time_over1s(self):
        r"""Gets the query_time_over1s of this SqlTplTrendItem.

        耗时超过1s的个数

        :return: The query_time_over1s of this SqlTplTrendItem.
        :rtype: int
        """
        return self._query_time_over1s

    @query_time_over1s.setter
    def query_time_over1s(self, query_time_over1s):
        r"""Sets the query_time_over1s of this SqlTplTrendItem.

        耗时超过1s的个数

        :param query_time_over1s: The query_time_over1s of this SqlTplTrendItem.
        :type query_time_over1s: int
        """
        self._query_time_over1s = query_time_over1s

    @property
    def query_executions(self):
        r"""Gets the query_executions of this SqlTplTrendItem.

        总个数

        :return: The query_executions of this SqlTplTrendItem.
        :rtype: int
        """
        return self._query_executions

    @query_executions.setter
    def query_executions(self, query_executions):
        r"""Sets the query_executions of this SqlTplTrendItem.

        总个数

        :param query_executions: The query_executions of this SqlTplTrendItem.
        :type query_executions: int
        """
        self._query_executions = query_executions

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
        if not isinstance(other, SqlTplTrendItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
