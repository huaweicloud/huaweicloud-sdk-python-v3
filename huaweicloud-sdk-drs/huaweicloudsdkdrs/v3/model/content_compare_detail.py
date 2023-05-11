# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentCompareDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db_name': 'str',
        'target_db_name': 'str',
        'source_table_name': 'str',
        'target_table_name': 'str',
        'source_row_num': 'int',
        'target_row_num': 'int',
        'diff_row_num': 'int',
        'line_compare_result': 'str',
        'content_compare_result': 'str',
        'message': 'str'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'target_db_name': 'target_db_name',
        'source_table_name': 'source_table_name',
        'target_table_name': 'target_table_name',
        'source_row_num': 'source_row_num',
        'target_row_num': 'target_row_num',
        'diff_row_num': 'diff_row_num',
        'line_compare_result': 'line_compare_result',
        'content_compare_result': 'content_compare_result',
        'message': 'message'
    }

    def __init__(self, source_db_name=None, target_db_name=None, source_table_name=None, target_table_name=None, source_row_num=None, target_row_num=None, diff_row_num=None, line_compare_result=None, content_compare_result=None, message=None):
        """ContentCompareDetail

        The model defined in huaweicloud sdk

        :param source_db_name: 源库名称。
        :type source_db_name: str
        :param target_db_name: 目标库名称。
        :type target_db_name: str
        :param source_table_name: 源库的表名称。
        :type source_table_name: str
        :param target_table_name: 目标库的表名称。
        :type target_table_name: str
        :param source_row_num: 源库的表的行数。
        :type source_row_num: int
        :param target_row_num: 目标库的表的行数。
        :type target_row_num: int
        :param diff_row_num: 源库的表和目标库的表的差异值。
        :type diff_row_num: int
        :param line_compare_result: 行对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比
        :type line_compare_result: str
        :param content_compare_result: 内容对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比
        :type content_compare_result: str
        :param message: 附加信息。
        :type message: str
        """
        
        

        self._source_db_name = None
        self._target_db_name = None
        self._source_table_name = None
        self._target_table_name = None
        self._source_row_num = None
        self._target_row_num = None
        self._diff_row_num = None
        self._line_compare_result = None
        self._content_compare_result = None
        self._message = None
        self.discriminator = None

        self.source_db_name = source_db_name
        self.target_db_name = target_db_name
        self.source_table_name = source_table_name
        self.target_table_name = target_table_name
        self.source_row_num = source_row_num
        self.target_row_num = target_row_num
        self.diff_row_num = diff_row_num
        if line_compare_result is not None:
            self.line_compare_result = line_compare_result
        self.content_compare_result = content_compare_result
        if message is not None:
            self.message = message

    @property
    def source_db_name(self):
        """Gets the source_db_name of this ContentCompareDetail.

        源库名称。

        :return: The source_db_name of this ContentCompareDetail.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this ContentCompareDetail.

        源库名称。

        :param source_db_name: The source_db_name of this ContentCompareDetail.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def target_db_name(self):
        """Gets the target_db_name of this ContentCompareDetail.

        目标库名称。

        :return: The target_db_name of this ContentCompareDetail.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        """Sets the target_db_name of this ContentCompareDetail.

        目标库名称。

        :param target_db_name: The target_db_name of this ContentCompareDetail.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def source_table_name(self):
        """Gets the source_table_name of this ContentCompareDetail.

        源库的表名称。

        :return: The source_table_name of this ContentCompareDetail.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        """Sets the source_table_name of this ContentCompareDetail.

        源库的表名称。

        :param source_table_name: The source_table_name of this ContentCompareDetail.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def target_table_name(self):
        """Gets the target_table_name of this ContentCompareDetail.

        目标库的表名称。

        :return: The target_table_name of this ContentCompareDetail.
        :rtype: str
        """
        return self._target_table_name

    @target_table_name.setter
    def target_table_name(self, target_table_name):
        """Sets the target_table_name of this ContentCompareDetail.

        目标库的表名称。

        :param target_table_name: The target_table_name of this ContentCompareDetail.
        :type target_table_name: str
        """
        self._target_table_name = target_table_name

    @property
    def source_row_num(self):
        """Gets the source_row_num of this ContentCompareDetail.

        源库的表的行数。

        :return: The source_row_num of this ContentCompareDetail.
        :rtype: int
        """
        return self._source_row_num

    @source_row_num.setter
    def source_row_num(self, source_row_num):
        """Sets the source_row_num of this ContentCompareDetail.

        源库的表的行数。

        :param source_row_num: The source_row_num of this ContentCompareDetail.
        :type source_row_num: int
        """
        self._source_row_num = source_row_num

    @property
    def target_row_num(self):
        """Gets the target_row_num of this ContentCompareDetail.

        目标库的表的行数。

        :return: The target_row_num of this ContentCompareDetail.
        :rtype: int
        """
        return self._target_row_num

    @target_row_num.setter
    def target_row_num(self, target_row_num):
        """Sets the target_row_num of this ContentCompareDetail.

        目标库的表的行数。

        :param target_row_num: The target_row_num of this ContentCompareDetail.
        :type target_row_num: int
        """
        self._target_row_num = target_row_num

    @property
    def diff_row_num(self):
        """Gets the diff_row_num of this ContentCompareDetail.

        源库的表和目标库的表的差异值。

        :return: The diff_row_num of this ContentCompareDetail.
        :rtype: int
        """
        return self._diff_row_num

    @diff_row_num.setter
    def diff_row_num(self, diff_row_num):
        """Sets the diff_row_num of this ContentCompareDetail.

        源库的表和目标库的表的差异值。

        :param diff_row_num: The diff_row_num of this ContentCompareDetail.
        :type diff_row_num: int
        """
        self._diff_row_num = diff_row_num

    @property
    def line_compare_result(self):
        """Gets the line_compare_result of this ContentCompareDetail.

        行对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比

        :return: The line_compare_result of this ContentCompareDetail.
        :rtype: str
        """
        return self._line_compare_result

    @line_compare_result.setter
    def line_compare_result(self, line_compare_result):
        """Sets the line_compare_result of this ContentCompareDetail.

        行对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比

        :param line_compare_result: The line_compare_result of this ContentCompareDetail.
        :type line_compare_result: str
        """
        self._line_compare_result = line_compare_result

    @property
    def content_compare_result(self):
        """Gets the content_compare_result of this ContentCompareDetail.

        内容对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比

        :return: The content_compare_result of this ContentCompareDetail.
        :rtype: str
        """
        return self._content_compare_result

    @content_compare_result.setter
    def content_compare_result(self, content_compare_result):
        """Sets the content_compare_result of this ContentCompareDetail.

        内容对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比

        :param content_compare_result: The content_compare_result of this ContentCompareDetail.
        :type content_compare_result: str
        """
        self._content_compare_result = content_compare_result

    @property
    def message(self):
        """Gets the message of this ContentCompareDetail.

        附加信息。

        :return: The message of this ContentCompareDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ContentCompareDetail.

        附加信息。

        :param message: The message of this ContentCompareDetail.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ContentCompareDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
