# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeContentCompareDetailResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db': 'str',
        'target_db': 'str',
        'source_table_name': 'str',
        'target_table_name': 'str',
        'source_row_num': 'int',
        'target_row_num': 'int',
        'difference_row_num': 'int',
        'line_compare_result': 'bool',
        'content_compare_result': 'bool',
        'message': 'str',
        'compare_line_config_filter': 'str'
    }

    attribute_map = {
        'source_db': 'source_db',
        'target_db': 'target_db',
        'source_table_name': 'source_table_name',
        'target_table_name': 'target_table_name',
        'source_row_num': 'source_row_num',
        'target_row_num': 'target_row_num',
        'difference_row_num': 'difference_row_num',
        'line_compare_result': 'line_compare_result',
        'content_compare_result': 'content_compare_result',
        'message': 'message',
        'compare_line_config_filter': 'compare_line_config_filter'
    }

    def __init__(self, source_db=None, target_db=None, source_table_name=None, target_table_name=None, source_row_num=None, target_row_num=None, difference_row_num=None, line_compare_result=None, content_compare_result=None, message=None, compare_line_config_filter=None):
        """NodeContentCompareDetailResult

        The model defined in huaweicloud sdk

        :param source_db: 源库名称。
        :type source_db: str
        :param target_db: 目标库名称。
        :type target_db: str
        :param source_table_name: 源库的表名称。
        :type source_table_name: str
        :param target_table_name: 目标库名称。
        :type target_table_name: str
        :param source_row_num: 源库表行数。
        :type source_row_num: int
        :param target_row_num: 目标库表行数。
        :type target_row_num: int
        :param difference_row_num: 源库的表和目标库的表的差异值。
        :type difference_row_num: int
        :param line_compare_result: 行对比结果。 - true：一致 - false：不一致
        :type line_compare_result: bool
        :param content_compare_result: 内容对比结果。 - true：一致 - false：不一致
        :type content_compare_result: bool
        :param message: 附加信息。
        :type message: str
        :param compare_line_config_filter: 行过滤配置条件
        :type compare_line_config_filter: str
        """
        
        

        self._source_db = None
        self._target_db = None
        self._source_table_name = None
        self._target_table_name = None
        self._source_row_num = None
        self._target_row_num = None
        self._difference_row_num = None
        self._line_compare_result = None
        self._content_compare_result = None
        self._message = None
        self._compare_line_config_filter = None
        self.discriminator = None

        if source_db is not None:
            self.source_db = source_db
        if target_db is not None:
            self.target_db = target_db
        if source_table_name is not None:
            self.source_table_name = source_table_name
        if target_table_name is not None:
            self.target_table_name = target_table_name
        if source_row_num is not None:
            self.source_row_num = source_row_num
        if target_row_num is not None:
            self.target_row_num = target_row_num
        if difference_row_num is not None:
            self.difference_row_num = difference_row_num
        if line_compare_result is not None:
            self.line_compare_result = line_compare_result
        if content_compare_result is not None:
            self.content_compare_result = content_compare_result
        if message is not None:
            self.message = message
        if compare_line_config_filter is not None:
            self.compare_line_config_filter = compare_line_config_filter

    @property
    def source_db(self):
        """Gets the source_db of this NodeContentCompareDetailResult.

        源库名称。

        :return: The source_db of this NodeContentCompareDetailResult.
        :rtype: str
        """
        return self._source_db

    @source_db.setter
    def source_db(self, source_db):
        """Sets the source_db of this NodeContentCompareDetailResult.

        源库名称。

        :param source_db: The source_db of this NodeContentCompareDetailResult.
        :type source_db: str
        """
        self._source_db = source_db

    @property
    def target_db(self):
        """Gets the target_db of this NodeContentCompareDetailResult.

        目标库名称。

        :return: The target_db of this NodeContentCompareDetailResult.
        :rtype: str
        """
        return self._target_db

    @target_db.setter
    def target_db(self, target_db):
        """Sets the target_db of this NodeContentCompareDetailResult.

        目标库名称。

        :param target_db: The target_db of this NodeContentCompareDetailResult.
        :type target_db: str
        """
        self._target_db = target_db

    @property
    def source_table_name(self):
        """Gets the source_table_name of this NodeContentCompareDetailResult.

        源库的表名称。

        :return: The source_table_name of this NodeContentCompareDetailResult.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        """Sets the source_table_name of this NodeContentCompareDetailResult.

        源库的表名称。

        :param source_table_name: The source_table_name of this NodeContentCompareDetailResult.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def target_table_name(self):
        """Gets the target_table_name of this NodeContentCompareDetailResult.

        目标库名称。

        :return: The target_table_name of this NodeContentCompareDetailResult.
        :rtype: str
        """
        return self._target_table_name

    @target_table_name.setter
    def target_table_name(self, target_table_name):
        """Sets the target_table_name of this NodeContentCompareDetailResult.

        目标库名称。

        :param target_table_name: The target_table_name of this NodeContentCompareDetailResult.
        :type target_table_name: str
        """
        self._target_table_name = target_table_name

    @property
    def source_row_num(self):
        """Gets the source_row_num of this NodeContentCompareDetailResult.

        源库表行数。

        :return: The source_row_num of this NodeContentCompareDetailResult.
        :rtype: int
        """
        return self._source_row_num

    @source_row_num.setter
    def source_row_num(self, source_row_num):
        """Sets the source_row_num of this NodeContentCompareDetailResult.

        源库表行数。

        :param source_row_num: The source_row_num of this NodeContentCompareDetailResult.
        :type source_row_num: int
        """
        self._source_row_num = source_row_num

    @property
    def target_row_num(self):
        """Gets the target_row_num of this NodeContentCompareDetailResult.

        目标库表行数。

        :return: The target_row_num of this NodeContentCompareDetailResult.
        :rtype: int
        """
        return self._target_row_num

    @target_row_num.setter
    def target_row_num(self, target_row_num):
        """Sets the target_row_num of this NodeContentCompareDetailResult.

        目标库表行数。

        :param target_row_num: The target_row_num of this NodeContentCompareDetailResult.
        :type target_row_num: int
        """
        self._target_row_num = target_row_num

    @property
    def difference_row_num(self):
        """Gets the difference_row_num of this NodeContentCompareDetailResult.

        源库的表和目标库的表的差异值。

        :return: The difference_row_num of this NodeContentCompareDetailResult.
        :rtype: int
        """
        return self._difference_row_num

    @difference_row_num.setter
    def difference_row_num(self, difference_row_num):
        """Sets the difference_row_num of this NodeContentCompareDetailResult.

        源库的表和目标库的表的差异值。

        :param difference_row_num: The difference_row_num of this NodeContentCompareDetailResult.
        :type difference_row_num: int
        """
        self._difference_row_num = difference_row_num

    @property
    def line_compare_result(self):
        """Gets the line_compare_result of this NodeContentCompareDetailResult.

        行对比结果。 - true：一致 - false：不一致

        :return: The line_compare_result of this NodeContentCompareDetailResult.
        :rtype: bool
        """
        return self._line_compare_result

    @line_compare_result.setter
    def line_compare_result(self, line_compare_result):
        """Sets the line_compare_result of this NodeContentCompareDetailResult.

        行对比结果。 - true：一致 - false：不一致

        :param line_compare_result: The line_compare_result of this NodeContentCompareDetailResult.
        :type line_compare_result: bool
        """
        self._line_compare_result = line_compare_result

    @property
    def content_compare_result(self):
        """Gets the content_compare_result of this NodeContentCompareDetailResult.

        内容对比结果。 - true：一致 - false：不一致

        :return: The content_compare_result of this NodeContentCompareDetailResult.
        :rtype: bool
        """
        return self._content_compare_result

    @content_compare_result.setter
    def content_compare_result(self, content_compare_result):
        """Sets the content_compare_result of this NodeContentCompareDetailResult.

        内容对比结果。 - true：一致 - false：不一致

        :param content_compare_result: The content_compare_result of this NodeContentCompareDetailResult.
        :type content_compare_result: bool
        """
        self._content_compare_result = content_compare_result

    @property
    def message(self):
        """Gets the message of this NodeContentCompareDetailResult.

        附加信息。

        :return: The message of this NodeContentCompareDetailResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NodeContentCompareDetailResult.

        附加信息。

        :param message: The message of this NodeContentCompareDetailResult.
        :type message: str
        """
        self._message = message

    @property
    def compare_line_config_filter(self):
        """Gets the compare_line_config_filter of this NodeContentCompareDetailResult.

        行过滤配置条件

        :return: The compare_line_config_filter of this NodeContentCompareDetailResult.
        :rtype: str
        """
        return self._compare_line_config_filter

    @compare_line_config_filter.setter
    def compare_line_config_filter(self, compare_line_config_filter):
        """Sets the compare_line_config_filter of this NodeContentCompareDetailResult.

        行过滤配置条件

        :param compare_line_config_filter: The compare_line_config_filter of this NodeContentCompareDetailResult.
        :type compare_line_config_filter: str
        """
        self._compare_line_config_filter = compare_line_config_filter

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
        if not isinstance(other, NodeContentCompareDetailResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
