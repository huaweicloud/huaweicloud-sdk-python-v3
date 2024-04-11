# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbObjectFilteringResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'is_success': 'bool',
        'message': 'str',
        'source': 'str',
        'target_result': 'str',
        'source_result': 'str',
        'target_message': 'str',
        'source_message': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'is_success': 'is_success',
        'message': 'message',
        'source': 'source',
        'target_result': 'target_result',
        'source_result': 'source_result',
        'target_message': 'target_message',
        'source_message': 'source_message'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None, is_success=None, message=None, source=None, target_result=None, source_result=None, target_message=None, source_message=None):
        """DbObjectFilteringResult

        The model defined in huaweicloud sdk

        :param db_name: 数据库库名。
        :type db_name: str
        :param schema_name: 数据库Schema名称。
        :type schema_name: str
        :param table_name: 数据库表名称。
        :type table_name: str
        :param is_success: 数据过滤校验结果。
        :type is_success: bool
        :param message: 当数据过滤校验结果是false，返回校验失败的原因。
        :type message: str
        :param source: 对比的来源 - job 表示数据同步时的过滤 - compare 表示数据对比的过滤
        :type source: str
        :param target_result: 校验目标库比对条件过滤的结果
        :type target_result: str
        :param source_result: 校验源库比对条件过滤的结果
        :type source_result: str
        :param target_message: 校验目标库比对条件过滤的失败原因
        :type target_message: str
        :param source_message: 校验源库比对条件过滤的失败原因
        :type source_message: str
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._is_success = None
        self._message = None
        self._source = None
        self._target_result = None
        self._source_result = None
        self._target_message = None
        self._source_message = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if source is not None:
            self.source = source
        if target_result is not None:
            self.target_result = target_result
        if source_result is not None:
            self.source_result = source_result
        if target_message is not None:
            self.target_message = target_message
        if source_message is not None:
            self.source_message = source_message

    @property
    def db_name(self):
        """Gets the db_name of this DbObjectFilteringResult.

        数据库库名。

        :return: The db_name of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DbObjectFilteringResult.

        数据库库名。

        :param db_name: The db_name of this DbObjectFilteringResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        """Gets the schema_name of this DbObjectFilteringResult.

        数据库Schema名称。

        :return: The schema_name of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this DbObjectFilteringResult.

        数据库Schema名称。

        :param schema_name: The schema_name of this DbObjectFilteringResult.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this DbObjectFilteringResult.

        数据库表名称。

        :return: The table_name of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DbObjectFilteringResult.

        数据库表名称。

        :param table_name: The table_name of this DbObjectFilteringResult.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def is_success(self):
        """Gets the is_success of this DbObjectFilteringResult.

        数据过滤校验结果。

        :return: The is_success of this DbObjectFilteringResult.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this DbObjectFilteringResult.

        数据过滤校验结果。

        :param is_success: The is_success of this DbObjectFilteringResult.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this DbObjectFilteringResult.

        当数据过滤校验结果是false，返回校验失败的原因。

        :return: The message of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DbObjectFilteringResult.

        当数据过滤校验结果是false，返回校验失败的原因。

        :param message: The message of this DbObjectFilteringResult.
        :type message: str
        """
        self._message = message

    @property
    def source(self):
        """Gets the source of this DbObjectFilteringResult.

        对比的来源 - job 表示数据同步时的过滤 - compare 表示数据对比的过滤

        :return: The source of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DbObjectFilteringResult.

        对比的来源 - job 表示数据同步时的过滤 - compare 表示数据对比的过滤

        :param source: The source of this DbObjectFilteringResult.
        :type source: str
        """
        self._source = source

    @property
    def target_result(self):
        """Gets the target_result of this DbObjectFilteringResult.

        校验目标库比对条件过滤的结果

        :return: The target_result of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._target_result

    @target_result.setter
    def target_result(self, target_result):
        """Sets the target_result of this DbObjectFilteringResult.

        校验目标库比对条件过滤的结果

        :param target_result: The target_result of this DbObjectFilteringResult.
        :type target_result: str
        """
        self._target_result = target_result

    @property
    def source_result(self):
        """Gets the source_result of this DbObjectFilteringResult.

        校验源库比对条件过滤的结果

        :return: The source_result of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._source_result

    @source_result.setter
    def source_result(self, source_result):
        """Sets the source_result of this DbObjectFilteringResult.

        校验源库比对条件过滤的结果

        :param source_result: The source_result of this DbObjectFilteringResult.
        :type source_result: str
        """
        self._source_result = source_result

    @property
    def target_message(self):
        """Gets the target_message of this DbObjectFilteringResult.

        校验目标库比对条件过滤的失败原因

        :return: The target_message of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._target_message

    @target_message.setter
    def target_message(self, target_message):
        """Sets the target_message of this DbObjectFilteringResult.

        校验目标库比对条件过滤的失败原因

        :param target_message: The target_message of this DbObjectFilteringResult.
        :type target_message: str
        """
        self._target_message = target_message

    @property
    def source_message(self):
        """Gets the source_message of this DbObjectFilteringResult.

        校验源库比对条件过滤的失败原因

        :return: The source_message of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._source_message

    @source_message.setter
    def source_message(self, source_message):
        """Sets the source_message of this DbObjectFilteringResult.

        校验源库比对条件过滤的失败原因

        :param source_message: The source_message of this DbObjectFilteringResult.
        :type source_message: str
        """
        self._source_message = source_message

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
        if not isinstance(other, DbObjectFilteringResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
