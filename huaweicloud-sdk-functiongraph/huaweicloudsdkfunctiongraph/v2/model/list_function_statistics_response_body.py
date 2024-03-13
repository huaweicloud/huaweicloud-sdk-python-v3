# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionStatisticsResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'list[SlaReportsValue]',
        'duration': 'list[SlaReportsValue]',
        'fail_count': 'list[SlaReportsValue]',
        'max_duration': 'list[SlaReportsValue]',
        'min_duration': 'list[SlaReportsValue]',
        'reject_count': 'list[SlaReportsValue]',
        'function_error_count': 'list[SlaReportsValue]',
        'system_error_count': 'list[SlaReportsValue]',
        'reserved_instance_num': 'list[SlaReportsValue]',
        'concurrency_num': 'list[SlaReportsValue]'
    }

    attribute_map = {
        'count': 'count',
        'duration': 'duration',
        'fail_count': 'fail_count',
        'max_duration': 'max_duration',
        'min_duration': 'min_duration',
        'reject_count': 'reject_count',
        'function_error_count': 'function_error_count',
        'system_error_count': 'system_error_count',
        'reserved_instance_num': 'reserved_instance_num',
        'concurrency_num': 'concurrency_num'
    }

    def __init__(self, count=None, duration=None, fail_count=None, max_duration=None, min_duration=None, reject_count=None, function_error_count=None, system_error_count=None, reserved_instance_num=None, concurrency_num=None):
        """ListFunctionStatisticsResponseBody

        The model defined in huaweicloud sdk

        :param count: 调用次数
        :type count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param duration: 平均时延，单位毫秒
        :type duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param fail_count: 错误次数
        :type fail_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param max_duration: 最大时延，单位毫秒
        :type max_duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param min_duration: 最小时延，单位毫秒
        :type min_duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param reject_count: 被拒绝次数
        :type reject_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param function_error_count: 函数错误次数
        :type function_error_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param system_error_count: 系统错误次数
        :type system_error_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param reserved_instance_num: 预留实例指标
        :type reserved_instance_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param concurrency_num: 弹性实例指标
        :type concurrency_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        
        

        self._count = None
        self._duration = None
        self._fail_count = None
        self._max_duration = None
        self._min_duration = None
        self._reject_count = None
        self._function_error_count = None
        self._system_error_count = None
        self._reserved_instance_num = None
        self._concurrency_num = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if duration is not None:
            self.duration = duration
        if fail_count is not None:
            self.fail_count = fail_count
        if max_duration is not None:
            self.max_duration = max_duration
        if min_duration is not None:
            self.min_duration = min_duration
        if reject_count is not None:
            self.reject_count = reject_count
        if function_error_count is not None:
            self.function_error_count = function_error_count
        if system_error_count is not None:
            self.system_error_count = system_error_count
        if reserved_instance_num is not None:
            self.reserved_instance_num = reserved_instance_num
        if concurrency_num is not None:
            self.concurrency_num = concurrency_num

    @property
    def count(self):
        """Gets the count of this ListFunctionStatisticsResponseBody.

        调用次数

        :return: The count of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFunctionStatisticsResponseBody.

        调用次数

        :param count: The count of this ListFunctionStatisticsResponseBody.
        :type count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._count = count

    @property
    def duration(self):
        """Gets the duration of this ListFunctionStatisticsResponseBody.

        平均时延，单位毫秒

        :return: The duration of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ListFunctionStatisticsResponseBody.

        平均时延，单位毫秒

        :param duration: The duration of this ListFunctionStatisticsResponseBody.
        :type duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._duration = duration

    @property
    def fail_count(self):
        """Gets the fail_count of this ListFunctionStatisticsResponseBody.

        错误次数

        :return: The fail_count of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        """Sets the fail_count of this ListFunctionStatisticsResponseBody.

        错误次数

        :param fail_count: The fail_count of this ListFunctionStatisticsResponseBody.
        :type fail_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._fail_count = fail_count

    @property
    def max_duration(self):
        """Gets the max_duration of this ListFunctionStatisticsResponseBody.

        最大时延，单位毫秒

        :return: The max_duration of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._max_duration

    @max_duration.setter
    def max_duration(self, max_duration):
        """Sets the max_duration of this ListFunctionStatisticsResponseBody.

        最大时延，单位毫秒

        :param max_duration: The max_duration of this ListFunctionStatisticsResponseBody.
        :type max_duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._max_duration = max_duration

    @property
    def min_duration(self):
        """Gets the min_duration of this ListFunctionStatisticsResponseBody.

        最小时延，单位毫秒

        :return: The min_duration of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._min_duration

    @min_duration.setter
    def min_duration(self, min_duration):
        """Sets the min_duration of this ListFunctionStatisticsResponseBody.

        最小时延，单位毫秒

        :param min_duration: The min_duration of this ListFunctionStatisticsResponseBody.
        :type min_duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._min_duration = min_duration

    @property
    def reject_count(self):
        """Gets the reject_count of this ListFunctionStatisticsResponseBody.

        被拒绝次数

        :return: The reject_count of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._reject_count

    @reject_count.setter
    def reject_count(self, reject_count):
        """Sets the reject_count of this ListFunctionStatisticsResponseBody.

        被拒绝次数

        :param reject_count: The reject_count of this ListFunctionStatisticsResponseBody.
        :type reject_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._reject_count = reject_count

    @property
    def function_error_count(self):
        """Gets the function_error_count of this ListFunctionStatisticsResponseBody.

        函数错误次数

        :return: The function_error_count of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._function_error_count

    @function_error_count.setter
    def function_error_count(self, function_error_count):
        """Sets the function_error_count of this ListFunctionStatisticsResponseBody.

        函数错误次数

        :param function_error_count: The function_error_count of this ListFunctionStatisticsResponseBody.
        :type function_error_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._function_error_count = function_error_count

    @property
    def system_error_count(self):
        """Gets the system_error_count of this ListFunctionStatisticsResponseBody.

        系统错误次数

        :return: The system_error_count of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._system_error_count

    @system_error_count.setter
    def system_error_count(self, system_error_count):
        """Sets the system_error_count of this ListFunctionStatisticsResponseBody.

        系统错误次数

        :param system_error_count: The system_error_count of this ListFunctionStatisticsResponseBody.
        :type system_error_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._system_error_count = system_error_count

    @property
    def reserved_instance_num(self):
        """Gets the reserved_instance_num of this ListFunctionStatisticsResponseBody.

        预留实例指标

        :return: The reserved_instance_num of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._reserved_instance_num

    @reserved_instance_num.setter
    def reserved_instance_num(self, reserved_instance_num):
        """Sets the reserved_instance_num of this ListFunctionStatisticsResponseBody.

        预留实例指标

        :param reserved_instance_num: The reserved_instance_num of this ListFunctionStatisticsResponseBody.
        :type reserved_instance_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._reserved_instance_num = reserved_instance_num

    @property
    def concurrency_num(self):
        """Gets the concurrency_num of this ListFunctionStatisticsResponseBody.

        弹性实例指标

        :return: The concurrency_num of this ListFunctionStatisticsResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._concurrency_num

    @concurrency_num.setter
    def concurrency_num(self, concurrency_num):
        """Sets the concurrency_num of this ListFunctionStatisticsResponseBody.

        弹性实例指标

        :param concurrency_num: The concurrency_num of this ListFunctionStatisticsResponseBody.
        :type concurrency_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._concurrency_num = concurrency_num

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
        if not isinstance(other, ListFunctionStatisticsResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
