# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCompareTaskResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'compare_task_id': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'compare_task_id': 'compare_task_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, compare_task_id=None, error_code=None, error_msg=None):
        """CreateCompareTaskResult

        The model defined in huaweicloud sdk

        :param compare_task_id: 对比任务创建成功后，返回对比任务的id，用于查询该对比任务的结果。
        :type compare_task_id: str
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        

        self._compare_task_id = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if compare_task_id is not None:
            self.compare_task_id = compare_task_id
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def compare_task_id(self):
        """Gets the compare_task_id of this CreateCompareTaskResult.

        对比任务创建成功后，返回对比任务的id，用于查询该对比任务的结果。

        :return: The compare_task_id of this CreateCompareTaskResult.
        :rtype: str
        """
        return self._compare_task_id

    @compare_task_id.setter
    def compare_task_id(self, compare_task_id):
        """Sets the compare_task_id of this CreateCompareTaskResult.

        对比任务创建成功后，返回对比任务的id，用于查询该对比任务的结果。

        :param compare_task_id: The compare_task_id of this CreateCompareTaskResult.
        :type compare_task_id: str
        """
        self._compare_task_id = compare_task_id

    @property
    def error_code(self):
        """Gets the error_code of this CreateCompareTaskResult.

        错误码。

        :return: The error_code of this CreateCompareTaskResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CreateCompareTaskResult.

        错误码。

        :param error_code: The error_code of this CreateCompareTaskResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CreateCompareTaskResult.

        错误信息。

        :return: The error_msg of this CreateCompareTaskResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CreateCompareTaskResult.

        错误信息。

        :param error_msg: The error_msg of this CreateCompareTaskResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, CreateCompareTaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
