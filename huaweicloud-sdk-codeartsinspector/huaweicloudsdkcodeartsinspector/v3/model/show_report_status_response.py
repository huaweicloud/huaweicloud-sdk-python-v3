# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'report_status': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'report_status': 'report_status'
    }

    def __init__(self, task_id=None, report_status=None):
        r"""ShowReportStatusResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param report_status: PDF报告生成状态:   * ungenerated - 未生成   * generating - 生成中   * generated - 已生成   * failed - 生成失败 
        :type report_status: str
        """
        
        super(ShowReportStatusResponse, self).__init__()

        self._task_id = None
        self._report_status = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if report_status is not None:
            self.report_status = report_status

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowReportStatusResponse.

        任务ID

        :return: The task_id of this ShowReportStatusResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowReportStatusResponse.

        任务ID

        :param task_id: The task_id of this ShowReportStatusResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def report_status(self):
        r"""Gets the report_status of this ShowReportStatusResponse.

        PDF报告生成状态:   * ungenerated - 未生成   * generating - 生成中   * generated - 已生成   * failed - 生成失败 

        :return: The report_status of this ShowReportStatusResponse.
        :rtype: str
        """
        return self._report_status

    @report_status.setter
    def report_status(self, report_status):
        r"""Sets the report_status of this ShowReportStatusResponse.

        PDF报告生成状态:   * ungenerated - 未生成   * generating - 生成中   * generated - 已生成   * failed - 生成失败 

        :param report_status: The report_status of this ShowReportStatusResponse.
        :type report_status: str
        """
        self._report_status = report_status

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
        if not isinstance(other, ShowReportStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
