# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecommendSqlLimitRuleRespSqlLimitInfos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'raw_sql': 'RecommendSqlLimitRuleRespRawSql',
        'average_time': 'float',
        'count': 'float',
        'max_time': 'int',
        'exe_time': 'int'
    }

    attribute_map = {
        'raw_sql': 'raw_sql',
        'average_time': 'average_time',
        'count': 'count',
        'max_time': 'maxTime',
        'exe_time': 'exe_time'
    }

    def __init__(self, raw_sql=None, average_time=None, count=None, max_time=None, exe_time=None):
        r"""RecommendSqlLimitRuleRespSqlLimitInfos

        The model defined in huaweicloud sdk

        :param raw_sql: 
        :type raw_sql: :class:`huaweicloudsdkdas.v3.RecommendSqlLimitRuleRespRawSql`
        :param average_time: 平均时间
        :type average_time: float
        :param count: 数量
        :type count: float
        :param max_time: mysql 提供， taurus不提供
        :type max_time: int
        :param exe_time: 执行时间
        :type exe_time: int
        """
        
        

        self._raw_sql = None
        self._average_time = None
        self._count = None
        self._max_time = None
        self._exe_time = None
        self.discriminator = None

        if raw_sql is not None:
            self.raw_sql = raw_sql
        if average_time is not None:
            self.average_time = average_time
        if count is not None:
            self.count = count
        if max_time is not None:
            self.max_time = max_time
        if exe_time is not None:
            self.exe_time = exe_time

    @property
    def raw_sql(self):
        r"""Gets the raw_sql of this RecommendSqlLimitRuleRespSqlLimitInfos.

        :return: The raw_sql of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :rtype: :class:`huaweicloudsdkdas.v3.RecommendSqlLimitRuleRespRawSql`
        """
        return self._raw_sql

    @raw_sql.setter
    def raw_sql(self, raw_sql):
        r"""Sets the raw_sql of this RecommendSqlLimitRuleRespSqlLimitInfos.

        :param raw_sql: The raw_sql of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :type raw_sql: :class:`huaweicloudsdkdas.v3.RecommendSqlLimitRuleRespRawSql`
        """
        self._raw_sql = raw_sql

    @property
    def average_time(self):
        r"""Gets the average_time of this RecommendSqlLimitRuleRespSqlLimitInfos.

        平均时间

        :return: The average_time of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :rtype: float
        """
        return self._average_time

    @average_time.setter
    def average_time(self, average_time):
        r"""Sets the average_time of this RecommendSqlLimitRuleRespSqlLimitInfos.

        平均时间

        :param average_time: The average_time of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :type average_time: float
        """
        self._average_time = average_time

    @property
    def count(self):
        r"""Gets the count of this RecommendSqlLimitRuleRespSqlLimitInfos.

        数量

        :return: The count of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this RecommendSqlLimitRuleRespSqlLimitInfos.

        数量

        :param count: The count of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :type count: float
        """
        self._count = count

    @property
    def max_time(self):
        r"""Gets the max_time of this RecommendSqlLimitRuleRespSqlLimitInfos.

        mysql 提供， taurus不提供

        :return: The max_time of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :rtype: int
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        r"""Sets the max_time of this RecommendSqlLimitRuleRespSqlLimitInfos.

        mysql 提供， taurus不提供

        :param max_time: The max_time of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :type max_time: int
        """
        self._max_time = max_time

    @property
    def exe_time(self):
        r"""Gets the exe_time of this RecommendSqlLimitRuleRespSqlLimitInfos.

        执行时间

        :return: The exe_time of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :rtype: int
        """
        return self._exe_time

    @exe_time.setter
    def exe_time(self, exe_time):
        r"""Sets the exe_time of this RecommendSqlLimitRuleRespSqlLimitInfos.

        执行时间

        :param exe_time: The exe_time of this RecommendSqlLimitRuleRespSqlLimitInfos.
        :type exe_time: int
        """
        self._exe_time = exe_time

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
        if not isinstance(other, RecommendSqlLimitRuleRespSqlLimitInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
