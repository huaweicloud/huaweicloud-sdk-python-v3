# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTableSpaceIncrInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'table': 'str',
        'increment': 'int',
        'analyze_success': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'database': 'database',
        'table': 'table',
        'increment': 'increment',
        'analyze_success': 'analyze_success',
        'error_message': 'error_message'
    }

    def __init__(self, database=None, table=None, increment=None, analyze_success=None, error_message=None):
        r"""HealthReportTableSpaceIncrInfo

        The model defined in huaweicloud sdk

        :param database: 数据库名。
        :type database: str
        :param table: 表名。
        :type table: str
        :param increment: 增长量。
        :type increment: int
        :param analyze_success: 统计分析是否成功。
        :type analyze_success: bool
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        

        self._database = None
        self._table = None
        self._increment = None
        self._analyze_success = None
        self._error_message = None
        self.discriminator = None

        self.database = database
        self.table = table
        self.increment = increment
        self.analyze_success = analyze_success
        self.error_message = error_message

    @property
    def database(self):
        r"""Gets the database of this HealthReportTableSpaceIncrInfo.

        数据库名。

        :return: The database of this HealthReportTableSpaceIncrInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this HealthReportTableSpaceIncrInfo.

        数据库名。

        :param database: The database of this HealthReportTableSpaceIncrInfo.
        :type database: str
        """
        self._database = database

    @property
    def table(self):
        r"""Gets the table of this HealthReportTableSpaceIncrInfo.

        表名。

        :return: The table of this HealthReportTableSpaceIncrInfo.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this HealthReportTableSpaceIncrInfo.

        表名。

        :param table: The table of this HealthReportTableSpaceIncrInfo.
        :type table: str
        """
        self._table = table

    @property
    def increment(self):
        r"""Gets the increment of this HealthReportTableSpaceIncrInfo.

        增长量。

        :return: The increment of this HealthReportTableSpaceIncrInfo.
        :rtype: int
        """
        return self._increment

    @increment.setter
    def increment(self, increment):
        r"""Sets the increment of this HealthReportTableSpaceIncrInfo.

        增长量。

        :param increment: The increment of this HealthReportTableSpaceIncrInfo.
        :type increment: int
        """
        self._increment = increment

    @property
    def analyze_success(self):
        r"""Gets the analyze_success of this HealthReportTableSpaceIncrInfo.

        统计分析是否成功。

        :return: The analyze_success of this HealthReportTableSpaceIncrInfo.
        :rtype: bool
        """
        return self._analyze_success

    @analyze_success.setter
    def analyze_success(self, analyze_success):
        r"""Sets the analyze_success of this HealthReportTableSpaceIncrInfo.

        统计分析是否成功。

        :param analyze_success: The analyze_success of this HealthReportTableSpaceIncrInfo.
        :type analyze_success: bool
        """
        self._analyze_success = analyze_success

    @property
    def error_message(self):
        r"""Gets the error_message of this HealthReportTableSpaceIncrInfo.

        错误信息。

        :return: The error_message of this HealthReportTableSpaceIncrInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this HealthReportTableSpaceIncrInfo.

        错误信息。

        :param error_message: The error_message of this HealthReportTableSpaceIncrInfo.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, HealthReportTableSpaceIncrInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
