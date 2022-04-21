# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareTaskListResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'compare_task_list': 'list[CompareTaskList]',
        'compare_task_list_count': 'int',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'compare_task_list': 'CompareTaskList',
        'compare_task_list_count': 'compare_task_list_count',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, compare_task_list=None, compare_task_list_count=None, error_msg=None, error_code=None):
        """CompareTaskListResult

        The model defined in huaweicloud sdk

        :param compare_task_list: 对比任务列表。
        :type compare_task_list: list[:class:`huaweicloudsdkdrs.v3.CompareTaskList`]
        :param compare_task_list_count: 对比任务列表总数。
        :type compare_task_list_count: int
        :param error_msg: 错误信息
        :type error_msg: str
        :param error_code: 错误码。
        :type error_code: str
        """
        
        

        self._compare_task_list = None
        self._compare_task_list_count = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if compare_task_list is not None:
            self.compare_task_list = compare_task_list
        if compare_task_list_count is not None:
            self.compare_task_list_count = compare_task_list_count
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def compare_task_list(self):
        """Gets the compare_task_list of this CompareTaskListResult.

        对比任务列表。

        :return: The compare_task_list of this CompareTaskListResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CompareTaskList`]
        """
        return self._compare_task_list

    @compare_task_list.setter
    def compare_task_list(self, compare_task_list):
        """Sets the compare_task_list of this CompareTaskListResult.

        对比任务列表。

        :param compare_task_list: The compare_task_list of this CompareTaskListResult.
        :type compare_task_list: list[:class:`huaweicloudsdkdrs.v3.CompareTaskList`]
        """
        self._compare_task_list = compare_task_list

    @property
    def compare_task_list_count(self):
        """Gets the compare_task_list_count of this CompareTaskListResult.

        对比任务列表总数。

        :return: The compare_task_list_count of this CompareTaskListResult.
        :rtype: int
        """
        return self._compare_task_list_count

    @compare_task_list_count.setter
    def compare_task_list_count(self, compare_task_list_count):
        """Sets the compare_task_list_count of this CompareTaskListResult.

        对比任务列表总数。

        :param compare_task_list_count: The compare_task_list_count of this CompareTaskListResult.
        :type compare_task_list_count: int
        """
        self._compare_task_list_count = compare_task_list_count

    @property
    def error_msg(self):
        """Gets the error_msg of this CompareTaskListResult.

        错误信息

        :return: The error_msg of this CompareTaskListResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CompareTaskListResult.

        错误信息

        :param error_msg: The error_msg of this CompareTaskListResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this CompareTaskListResult.

        错误码。

        :return: The error_code of this CompareTaskListResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CompareTaskListResult.

        错误码。

        :param error_code: The error_code of this CompareTaskListResult.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, CompareTaskListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
