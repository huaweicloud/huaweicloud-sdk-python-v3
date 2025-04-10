# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplaySlowSqlTemplateResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_template': 'str',
        'sql_template_md5': 'str',
        'target_name': 'str',
        'schema_name': 'str',
        'query_type': 'str',
        'min_latency': 'int',
        'max_latency': 'int',
        'avg_latency': 'int',
        'total_latency': 'int',
        'target_type': 'str',
        'count': 'int'
    }

    attribute_map = {
        'sql_template': 'sql_template',
        'sql_template_md5': 'sql_template_md5',
        'target_name': 'target_name',
        'schema_name': 'schema_name',
        'query_type': 'query_type',
        'min_latency': 'min_latency',
        'max_latency': 'max_latency',
        'avg_latency': 'avg_latency',
        'total_latency': 'total_latency',
        'target_type': 'target_type',
        'count': 'count'
    }

    def __init__(self, sql_template=None, sql_template_md5=None, target_name=None, schema_name=None, query_type=None, min_latency=None, max_latency=None, avg_latency=None, total_latency=None, target_type=None, count=None):
        r"""ReplaySlowSqlTemplateResp

        The model defined in huaweicloud sdk

        :param sql_template: SQL语句模板
        :type sql_template: str
        :param sql_template_md5: SQL语句模板MD5
        :type sql_template_md5: str
        :param target_name: 目标库别名
        :type target_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param query_type: SQL类型
        :type query_type: str
        :param min_latency: SQL执行最小耗时
        :type min_latency: int
        :param max_latency: SQL执行最大耗时
        :type max_latency: int
        :param avg_latency: SQL执行平均耗时
        :type avg_latency: int
        :param total_latency: SQL执行总的耗时
        :type total_latency: int
        :param target_type: 目标库类型
        :type target_type: str
        :param count: SQL数量
        :type count: int
        """
        
        

        self._sql_template = None
        self._sql_template_md5 = None
        self._target_name = None
        self._schema_name = None
        self._query_type = None
        self._min_latency = None
        self._max_latency = None
        self._avg_latency = None
        self._total_latency = None
        self._target_type = None
        self._count = None
        self.discriminator = None

        self.sql_template = sql_template
        if sql_template_md5 is not None:
            self.sql_template_md5 = sql_template_md5
        if target_name is not None:
            self.target_name = target_name
        if schema_name is not None:
            self.schema_name = schema_name
        if query_type is not None:
            self.query_type = query_type
        if min_latency is not None:
            self.min_latency = min_latency
        if max_latency is not None:
            self.max_latency = max_latency
        self.avg_latency = avg_latency
        if total_latency is not None:
            self.total_latency = total_latency
        if target_type is not None:
            self.target_type = target_type
        self.count = count

    @property
    def sql_template(self):
        r"""Gets the sql_template of this ReplaySlowSqlTemplateResp.

        SQL语句模板

        :return: The sql_template of this ReplaySlowSqlTemplateResp.
        :rtype: str
        """
        return self._sql_template

    @sql_template.setter
    def sql_template(self, sql_template):
        r"""Sets the sql_template of this ReplaySlowSqlTemplateResp.

        SQL语句模板

        :param sql_template: The sql_template of this ReplaySlowSqlTemplateResp.
        :type sql_template: str
        """
        self._sql_template = sql_template

    @property
    def sql_template_md5(self):
        r"""Gets the sql_template_md5 of this ReplaySlowSqlTemplateResp.

        SQL语句模板MD5

        :return: The sql_template_md5 of this ReplaySlowSqlTemplateResp.
        :rtype: str
        """
        return self._sql_template_md5

    @sql_template_md5.setter
    def sql_template_md5(self, sql_template_md5):
        r"""Sets the sql_template_md5 of this ReplaySlowSqlTemplateResp.

        SQL语句模板MD5

        :param sql_template_md5: The sql_template_md5 of this ReplaySlowSqlTemplateResp.
        :type sql_template_md5: str
        """
        self._sql_template_md5 = sql_template_md5

    @property
    def target_name(self):
        r"""Gets the target_name of this ReplaySlowSqlTemplateResp.

        目标库别名

        :return: The target_name of this ReplaySlowSqlTemplateResp.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        r"""Sets the target_name of this ReplaySlowSqlTemplateResp.

        目标库别名

        :param target_name: The target_name of this ReplaySlowSqlTemplateResp.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ReplaySlowSqlTemplateResp.

        schema名称

        :return: The schema_name of this ReplaySlowSqlTemplateResp.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ReplaySlowSqlTemplateResp.

        schema名称

        :param schema_name: The schema_name of this ReplaySlowSqlTemplateResp.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def query_type(self):
        r"""Gets the query_type of this ReplaySlowSqlTemplateResp.

        SQL类型

        :return: The query_type of this ReplaySlowSqlTemplateResp.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ReplaySlowSqlTemplateResp.

        SQL类型

        :param query_type: The query_type of this ReplaySlowSqlTemplateResp.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def min_latency(self):
        r"""Gets the min_latency of this ReplaySlowSqlTemplateResp.

        SQL执行最小耗时

        :return: The min_latency of this ReplaySlowSqlTemplateResp.
        :rtype: int
        """
        return self._min_latency

    @min_latency.setter
    def min_latency(self, min_latency):
        r"""Sets the min_latency of this ReplaySlowSqlTemplateResp.

        SQL执行最小耗时

        :param min_latency: The min_latency of this ReplaySlowSqlTemplateResp.
        :type min_latency: int
        """
        self._min_latency = min_latency

    @property
    def max_latency(self):
        r"""Gets the max_latency of this ReplaySlowSqlTemplateResp.

        SQL执行最大耗时

        :return: The max_latency of this ReplaySlowSqlTemplateResp.
        :rtype: int
        """
        return self._max_latency

    @max_latency.setter
    def max_latency(self, max_latency):
        r"""Sets the max_latency of this ReplaySlowSqlTemplateResp.

        SQL执行最大耗时

        :param max_latency: The max_latency of this ReplaySlowSqlTemplateResp.
        :type max_latency: int
        """
        self._max_latency = max_latency

    @property
    def avg_latency(self):
        r"""Gets the avg_latency of this ReplaySlowSqlTemplateResp.

        SQL执行平均耗时

        :return: The avg_latency of this ReplaySlowSqlTemplateResp.
        :rtype: int
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        r"""Sets the avg_latency of this ReplaySlowSqlTemplateResp.

        SQL执行平均耗时

        :param avg_latency: The avg_latency of this ReplaySlowSqlTemplateResp.
        :type avg_latency: int
        """
        self._avg_latency = avg_latency

    @property
    def total_latency(self):
        r"""Gets the total_latency of this ReplaySlowSqlTemplateResp.

        SQL执行总的耗时

        :return: The total_latency of this ReplaySlowSqlTemplateResp.
        :rtype: int
        """
        return self._total_latency

    @total_latency.setter
    def total_latency(self, total_latency):
        r"""Sets the total_latency of this ReplaySlowSqlTemplateResp.

        SQL执行总的耗时

        :param total_latency: The total_latency of this ReplaySlowSqlTemplateResp.
        :type total_latency: int
        """
        self._total_latency = total_latency

    @property
    def target_type(self):
        r"""Gets the target_type of this ReplaySlowSqlTemplateResp.

        目标库类型

        :return: The target_type of this ReplaySlowSqlTemplateResp.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this ReplaySlowSqlTemplateResp.

        目标库类型

        :param target_type: The target_type of this ReplaySlowSqlTemplateResp.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def count(self):
        r"""Gets the count of this ReplaySlowSqlTemplateResp.

        SQL数量

        :return: The count of this ReplaySlowSqlTemplateResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ReplaySlowSqlTemplateResp.

        SQL数量

        :param count: The count of this ReplaySlowSqlTemplateResp.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ReplaySlowSqlTemplateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
