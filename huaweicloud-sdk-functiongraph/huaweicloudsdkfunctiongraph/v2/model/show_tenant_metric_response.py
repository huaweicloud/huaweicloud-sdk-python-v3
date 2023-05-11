# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantMetricResponse(SdkResponse):

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
        'running_count': 'list[SlaReportsValue]'
    }

    attribute_map = {
        'count': 'count',
        'duration': 'duration',
        'fail_count': 'fail_count',
        'running_count': 'running_count'
    }

    def __init__(self, count=None, duration=None, fail_count=None, running_count=None):
        """ShowTenantMetricResponse

        The model defined in huaweicloud sdk

        :param count: 执行次数
        :type count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param duration: 平均时延，单位毫秒
        :type duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param fail_count: 错误次数
        :type fail_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param running_count: 运行中数量
        :type running_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        
        super(ShowTenantMetricResponse, self).__init__()

        self._count = None
        self._duration = None
        self._fail_count = None
        self._running_count = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if duration is not None:
            self.duration = duration
        if fail_count is not None:
            self.fail_count = fail_count
        if running_count is not None:
            self.running_count = running_count

    @property
    def count(self):
        """Gets the count of this ShowTenantMetricResponse.

        执行次数

        :return: The count of this ShowTenantMetricResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowTenantMetricResponse.

        执行次数

        :param count: The count of this ShowTenantMetricResponse.
        :type count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._count = count

    @property
    def duration(self):
        """Gets the duration of this ShowTenantMetricResponse.

        平均时延，单位毫秒

        :return: The duration of this ShowTenantMetricResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ShowTenantMetricResponse.

        平均时延，单位毫秒

        :param duration: The duration of this ShowTenantMetricResponse.
        :type duration: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._duration = duration

    @property
    def fail_count(self):
        """Gets the fail_count of this ShowTenantMetricResponse.

        错误次数

        :return: The fail_count of this ShowTenantMetricResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        """Sets the fail_count of this ShowTenantMetricResponse.

        错误次数

        :param fail_count: The fail_count of this ShowTenantMetricResponse.
        :type fail_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._fail_count = fail_count

    @property
    def running_count(self):
        """Gets the running_count of this ShowTenantMetricResponse.

        运行中数量

        :return: The running_count of this ShowTenantMetricResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        """Sets the running_count of this ShowTenantMetricResponse.

        运行中数量

        :param running_count: The running_count of this ShowTenantMetricResponse.
        :type running_count: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._running_count = running_count

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
        if not isinstance(other, ShowTenantMetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
