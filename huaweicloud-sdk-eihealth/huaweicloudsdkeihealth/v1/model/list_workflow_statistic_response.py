# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_count': 'int',
        'workflow_count': 'int',
        'job_count': 'int',
        'succeed_job_count': 'int'
    }

    attribute_map = {
        'app_count': 'app_count',
        'workflow_count': 'workflow_count',
        'job_count': 'job_count',
        'succeed_job_count': 'succeed_job_count'
    }

    def __init__(self, app_count=None, workflow_count=None, job_count=None, succeed_job_count=None):
        """ListWorkflowStatisticResponse

        The model defined in huaweicloud sdk

        :param app_count: 应用总数
        :type app_count: int
        :param workflow_count: 流程总数
        :type workflow_count: int
        :param job_count: 作业总数
        :type job_count: int
        :param succeed_job_count: 运行成功作业总数
        :type succeed_job_count: int
        """
        
        super(ListWorkflowStatisticResponse, self).__init__()

        self._app_count = None
        self._workflow_count = None
        self._job_count = None
        self._succeed_job_count = None
        self.discriminator = None

        if app_count is not None:
            self.app_count = app_count
        if workflow_count is not None:
            self.workflow_count = workflow_count
        if job_count is not None:
            self.job_count = job_count
        if succeed_job_count is not None:
            self.succeed_job_count = succeed_job_count

    @property
    def app_count(self):
        """Gets the app_count of this ListWorkflowStatisticResponse.

        应用总数

        :return: The app_count of this ListWorkflowStatisticResponse.
        :rtype: int
        """
        return self._app_count

    @app_count.setter
    def app_count(self, app_count):
        """Sets the app_count of this ListWorkflowStatisticResponse.

        应用总数

        :param app_count: The app_count of this ListWorkflowStatisticResponse.
        :type app_count: int
        """
        self._app_count = app_count

    @property
    def workflow_count(self):
        """Gets the workflow_count of this ListWorkflowStatisticResponse.

        流程总数

        :return: The workflow_count of this ListWorkflowStatisticResponse.
        :rtype: int
        """
        return self._workflow_count

    @workflow_count.setter
    def workflow_count(self, workflow_count):
        """Sets the workflow_count of this ListWorkflowStatisticResponse.

        流程总数

        :param workflow_count: The workflow_count of this ListWorkflowStatisticResponse.
        :type workflow_count: int
        """
        self._workflow_count = workflow_count

    @property
    def job_count(self):
        """Gets the job_count of this ListWorkflowStatisticResponse.

        作业总数

        :return: The job_count of this ListWorkflowStatisticResponse.
        :rtype: int
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        """Sets the job_count of this ListWorkflowStatisticResponse.

        作业总数

        :param job_count: The job_count of this ListWorkflowStatisticResponse.
        :type job_count: int
        """
        self._job_count = job_count

    @property
    def succeed_job_count(self):
        """Gets the succeed_job_count of this ListWorkflowStatisticResponse.

        运行成功作业总数

        :return: The succeed_job_count of this ListWorkflowStatisticResponse.
        :rtype: int
        """
        return self._succeed_job_count

    @succeed_job_count.setter
    def succeed_job_count(self, succeed_job_count):
        """Sets the succeed_job_count of this ListWorkflowStatisticResponse.

        运行成功作业总数

        :param succeed_job_count: The succeed_job_count of this ListWorkflowStatisticResponse.
        :type succeed_job_count: int
        """
        self._succeed_job_count = succeed_job_count

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
        if not isinstance(other, ListWorkflowStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
