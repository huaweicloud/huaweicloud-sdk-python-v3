# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalWorkflowStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_count': 'int'
    }

    attribute_map = {
        'job_count': 'job_count'
    }

    def __init__(self, job_count=None):
        r"""ListGlobalWorkflowStatisticResponse

        The model defined in huaweicloud sdk

        :param job_count: 所有作业总数
        :type job_count: int
        """
        
        super(ListGlobalWorkflowStatisticResponse, self).__init__()

        self._job_count = None
        self.discriminator = None

        if job_count is not None:
            self.job_count = job_count

    @property
    def job_count(self):
        r"""Gets the job_count of this ListGlobalWorkflowStatisticResponse.

        所有作业总数

        :return: The job_count of this ListGlobalWorkflowStatisticResponse.
        :rtype: int
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        r"""Sets the job_count of this ListGlobalWorkflowStatisticResponse.

        所有作业总数

        :param job_count: The job_count of this ListGlobalWorkflowStatisticResponse.
        :type job_count: int
        """
        self._job_count = job_count

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
        if not isinstance(other, ListGlobalWorkflowStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
