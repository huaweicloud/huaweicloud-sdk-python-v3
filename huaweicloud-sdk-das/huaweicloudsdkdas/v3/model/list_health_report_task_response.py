# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHealthReportTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'health_report_task_list': 'list[HealthReportTask]'
    }

    attribute_map = {
        'total': 'total',
        'health_report_task_list': 'health_report_task_list'
    }

    def __init__(self, total=None, health_report_task_list=None):
        r"""ListHealthReportTaskResponse

        The model defined in huaweicloud sdk

        :param total: 诊断报告总数
        :type total: int
        :param health_report_task_list: 诊断报告列表
        :type health_report_task_list: list[:class:`huaweicloudsdkdas.v3.HealthReportTask`]
        """
        
        super(ListHealthReportTaskResponse, self).__init__()

        self._total = None
        self._health_report_task_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if health_report_task_list is not None:
            self.health_report_task_list = health_report_task_list

    @property
    def total(self):
        r"""Gets the total of this ListHealthReportTaskResponse.

        诊断报告总数

        :return: The total of this ListHealthReportTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListHealthReportTaskResponse.

        诊断报告总数

        :param total: The total of this ListHealthReportTaskResponse.
        :type total: int
        """
        self._total = total

    @property
    def health_report_task_list(self):
        r"""Gets the health_report_task_list of this ListHealthReportTaskResponse.

        诊断报告列表

        :return: The health_report_task_list of this ListHealthReportTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTask`]
        """
        return self._health_report_task_list

    @health_report_task_list.setter
    def health_report_task_list(self, health_report_task_list):
        r"""Sets the health_report_task_list of this ListHealthReportTaskResponse.

        诊断报告列表

        :param health_report_task_list: The health_report_task_list of this ListHealthReportTaskResponse.
        :type health_report_task_list: list[:class:`huaweicloudsdkdas.v3.HealthReportTask`]
        """
        self._health_report_task_list = health_report_task_list

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
        if not isinstance(other, ListHealthReportTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
