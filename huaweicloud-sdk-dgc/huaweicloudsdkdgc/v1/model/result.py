# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Result:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'object',
        'schema': 'object',
        'rows': 'object',
        'row_count': 'int',
        'input_row_count': 'int',
        'result_count': 'int',
        'duration': 'float',
        'raw_result': 'object'
    }

    attribute_map = {
        'message': 'message',
        'schema': 'schema',
        'rows': 'rows',
        'row_count': 'rowCount',
        'input_row_count': 'inputRowCount',
        'result_count': 'resultCount',
        'duration': 'duration',
        'raw_result': 'rawResult'
    }

    def __init__(self, message=None, schema=None, rows=None, row_count=None, input_row_count=None, result_count=None, duration=None, raw_result=None):
        """Result

        The model defined in huaweicloud sdk

        :param message: 结果返回信息
        :type message: object
        :param schema: 元数据信息
        :type schema: object
        :param rows: 每条结果的信息
        :type rows: object
        :param row_count: 结果行数
        :type row_count: int
        :param input_row_count: 输入结果的行数。（dli等脚本执行会执行此结果）
        :type input_row_count: int
        :param result_count: 结果行数。（dli等脚本执行会执行此结果）
        :type result_count: int
        :param duration: 脚本运行时间
        :type duration: float
        :param raw_result: 脚本结果信息
        :type raw_result: object
        """
        
        

        self._message = None
        self._schema = None
        self._rows = None
        self._row_count = None
        self._input_row_count = None
        self._result_count = None
        self._duration = None
        self._raw_result = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if schema is not None:
            self.schema = schema
        if rows is not None:
            self.rows = rows
        if row_count is not None:
            self.row_count = row_count
        if input_row_count is not None:
            self.input_row_count = input_row_count
        if result_count is not None:
            self.result_count = result_count
        if duration is not None:
            self.duration = duration
        if raw_result is not None:
            self.raw_result = raw_result

    @property
    def message(self):
        """Gets the message of this Result.

        结果返回信息

        :return: The message of this Result.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Result.

        结果返回信息

        :param message: The message of this Result.
        :type message: object
        """
        self._message = message

    @property
    def schema(self):
        """Gets the schema of this Result.

        元数据信息

        :return: The schema of this Result.
        :rtype: object
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Result.

        元数据信息

        :param schema: The schema of this Result.
        :type schema: object
        """
        self._schema = schema

    @property
    def rows(self):
        """Gets the rows of this Result.

        每条结果的信息

        :return: The rows of this Result.
        :rtype: object
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this Result.

        每条结果的信息

        :param rows: The rows of this Result.
        :type rows: object
        """
        self._rows = rows

    @property
    def row_count(self):
        """Gets the row_count of this Result.

        结果行数

        :return: The row_count of this Result.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this Result.

        结果行数

        :param row_count: The row_count of this Result.
        :type row_count: int
        """
        self._row_count = row_count

    @property
    def input_row_count(self):
        """Gets the input_row_count of this Result.

        输入结果的行数。（dli等脚本执行会执行此结果）

        :return: The input_row_count of this Result.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        """Sets the input_row_count of this Result.

        输入结果的行数。（dli等脚本执行会执行此结果）

        :param input_row_count: The input_row_count of this Result.
        :type input_row_count: int
        """
        self._input_row_count = input_row_count

    @property
    def result_count(self):
        """Gets the result_count of this Result.

        结果行数。（dli等脚本执行会执行此结果）

        :return: The result_count of this Result.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this Result.

        结果行数。（dli等脚本执行会执行此结果）

        :param result_count: The result_count of this Result.
        :type result_count: int
        """
        self._result_count = result_count

    @property
    def duration(self):
        """Gets the duration of this Result.

        脚本运行时间

        :return: The duration of this Result.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Result.

        脚本运行时间

        :param duration: The duration of this Result.
        :type duration: float
        """
        self._duration = duration

    @property
    def raw_result(self):
        """Gets the raw_result of this Result.

        脚本结果信息

        :return: The raw_result of this Result.
        :rtype: object
        """
        return self._raw_result

    @raw_result.setter
    def raw_result(self, raw_result):
        """Sets the raw_result of this Result.

        脚本结果信息

        :param raw_result: The raw_result of this Result.
        :type raw_result: object
        """
        self._raw_result = raw_result

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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
