# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportSqlTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'template': 'str',
        'databases': 'list[str]',
        'times': 'int',
        'avg_query_time': 'float',
        'max_query_time': 'float',
        'avg_rows_examined': 'float',
        'max_rows_examined': 'float',
        'sum_rows_examined': 'float',
        'avg_rows_sent': 'float',
        'max_rows_sent': 'float'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template': 'template',
        'databases': 'databases',
        'times': 'times',
        'avg_query_time': 'avg_query_time',
        'max_query_time': 'max_query_time',
        'avg_rows_examined': 'avg_rows_examined',
        'max_rows_examined': 'max_rows_examined',
        'sum_rows_examined': 'sum_rows_examined',
        'avg_rows_sent': 'avg_rows_sent',
        'max_rows_sent': 'max_rows_sent'
    }

    def __init__(self, template_id=None, template=None, databases=None, times=None, avg_query_time=None, max_query_time=None, avg_rows_examined=None, max_rows_examined=None, sum_rows_examined=None, avg_rows_sent=None, max_rows_sent=None):
        r"""HealthReportSqlTemplate

        The model defined in huaweicloud sdk

        :param template_id: 模版ID。
        :type template_id: str
        :param template: 模版内容。
        :type template: str
        :param databases: 数据库列表。
        :type databases: list[str]
        :param times: 执行次数。
        :type times: int
        :param avg_query_time: 平均执行时间。
        :type avg_query_time: float
        :param max_query_time: 最大执行时间。
        :type max_query_time: float
        :param avg_rows_examined: 平均扫描行数。
        :type avg_rows_examined: float
        :param max_rows_examined: 最大扫描行数。
        :type max_rows_examined: float
        :param sum_rows_examined: 总扫描行数。
        :type sum_rows_examined: float
        :param avg_rows_sent: 平均返回行数。
        :type avg_rows_sent: float
        :param max_rows_sent: 最大返回行数。
        :type max_rows_sent: float
        """
        
        

        self._template_id = None
        self._template = None
        self._databases = None
        self._times = None
        self._avg_query_time = None
        self._max_query_time = None
        self._avg_rows_examined = None
        self._max_rows_examined = None
        self._sum_rows_examined = None
        self._avg_rows_sent = None
        self._max_rows_sent = None
        self.discriminator = None

        self.template_id = template_id
        self.template = template
        self.databases = databases
        self.times = times
        self.avg_query_time = avg_query_time
        self.max_query_time = max_query_time
        self.avg_rows_examined = avg_rows_examined
        self.max_rows_examined = max_rows_examined
        self.sum_rows_examined = sum_rows_examined
        self.avg_rows_sent = avg_rows_sent
        self.max_rows_sent = max_rows_sent

    @property
    def template_id(self):
        r"""Gets the template_id of this HealthReportSqlTemplate.

        模版ID。

        :return: The template_id of this HealthReportSqlTemplate.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this HealthReportSqlTemplate.

        模版ID。

        :param template_id: The template_id of this HealthReportSqlTemplate.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template(self):
        r"""Gets the template of this HealthReportSqlTemplate.

        模版内容。

        :return: The template of this HealthReportSqlTemplate.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this HealthReportSqlTemplate.

        模版内容。

        :param template: The template of this HealthReportSqlTemplate.
        :type template: str
        """
        self._template = template

    @property
    def databases(self):
        r"""Gets the databases of this HealthReportSqlTemplate.

        数据库列表。

        :return: The databases of this HealthReportSqlTemplate.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this HealthReportSqlTemplate.

        数据库列表。

        :param databases: The databases of this HealthReportSqlTemplate.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def times(self):
        r"""Gets the times of this HealthReportSqlTemplate.

        执行次数。

        :return: The times of this HealthReportSqlTemplate.
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        r"""Sets the times of this HealthReportSqlTemplate.

        执行次数。

        :param times: The times of this HealthReportSqlTemplate.
        :type times: int
        """
        self._times = times

    @property
    def avg_query_time(self):
        r"""Gets the avg_query_time of this HealthReportSqlTemplate.

        平均执行时间。

        :return: The avg_query_time of this HealthReportSqlTemplate.
        :rtype: float
        """
        return self._avg_query_time

    @avg_query_time.setter
    def avg_query_time(self, avg_query_time):
        r"""Sets the avg_query_time of this HealthReportSqlTemplate.

        平均执行时间。

        :param avg_query_time: The avg_query_time of this HealthReportSqlTemplate.
        :type avg_query_time: float
        """
        self._avg_query_time = avg_query_time

    @property
    def max_query_time(self):
        r"""Gets the max_query_time of this HealthReportSqlTemplate.

        最大执行时间。

        :return: The max_query_time of this HealthReportSqlTemplate.
        :rtype: float
        """
        return self._max_query_time

    @max_query_time.setter
    def max_query_time(self, max_query_time):
        r"""Sets the max_query_time of this HealthReportSqlTemplate.

        最大执行时间。

        :param max_query_time: The max_query_time of this HealthReportSqlTemplate.
        :type max_query_time: float
        """
        self._max_query_time = max_query_time

    @property
    def avg_rows_examined(self):
        r"""Gets the avg_rows_examined of this HealthReportSqlTemplate.

        平均扫描行数。

        :return: The avg_rows_examined of this HealthReportSqlTemplate.
        :rtype: float
        """
        return self._avg_rows_examined

    @avg_rows_examined.setter
    def avg_rows_examined(self, avg_rows_examined):
        r"""Sets the avg_rows_examined of this HealthReportSqlTemplate.

        平均扫描行数。

        :param avg_rows_examined: The avg_rows_examined of this HealthReportSqlTemplate.
        :type avg_rows_examined: float
        """
        self._avg_rows_examined = avg_rows_examined

    @property
    def max_rows_examined(self):
        r"""Gets the max_rows_examined of this HealthReportSqlTemplate.

        最大扫描行数。

        :return: The max_rows_examined of this HealthReportSqlTemplate.
        :rtype: float
        """
        return self._max_rows_examined

    @max_rows_examined.setter
    def max_rows_examined(self, max_rows_examined):
        r"""Sets the max_rows_examined of this HealthReportSqlTemplate.

        最大扫描行数。

        :param max_rows_examined: The max_rows_examined of this HealthReportSqlTemplate.
        :type max_rows_examined: float
        """
        self._max_rows_examined = max_rows_examined

    @property
    def sum_rows_examined(self):
        r"""Gets the sum_rows_examined of this HealthReportSqlTemplate.

        总扫描行数。

        :return: The sum_rows_examined of this HealthReportSqlTemplate.
        :rtype: float
        """
        return self._sum_rows_examined

    @sum_rows_examined.setter
    def sum_rows_examined(self, sum_rows_examined):
        r"""Sets the sum_rows_examined of this HealthReportSqlTemplate.

        总扫描行数。

        :param sum_rows_examined: The sum_rows_examined of this HealthReportSqlTemplate.
        :type sum_rows_examined: float
        """
        self._sum_rows_examined = sum_rows_examined

    @property
    def avg_rows_sent(self):
        r"""Gets the avg_rows_sent of this HealthReportSqlTemplate.

        平均返回行数。

        :return: The avg_rows_sent of this HealthReportSqlTemplate.
        :rtype: float
        """
        return self._avg_rows_sent

    @avg_rows_sent.setter
    def avg_rows_sent(self, avg_rows_sent):
        r"""Sets the avg_rows_sent of this HealthReportSqlTemplate.

        平均返回行数。

        :param avg_rows_sent: The avg_rows_sent of this HealthReportSqlTemplate.
        :type avg_rows_sent: float
        """
        self._avg_rows_sent = avg_rows_sent

    @property
    def max_rows_sent(self):
        r"""Gets the max_rows_sent of this HealthReportSqlTemplate.

        最大返回行数。

        :return: The max_rows_sent of this HealthReportSqlTemplate.
        :rtype: float
        """
        return self._max_rows_sent

    @max_rows_sent.setter
    def max_rows_sent(self, max_rows_sent):
        r"""Sets the max_rows_sent of this HealthReportSqlTemplate.

        最大返回行数。

        :param max_rows_sent: The max_rows_sent of this HealthReportSqlTemplate.
        :type max_rows_sent: float
        """
        self._max_rows_sent = max_rows_sent

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
        if not isinstance(other, HealthReportSqlTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
