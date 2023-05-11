# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobExesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_execution': 'JobExeResult'
    }

    attribute_map = {
        'job_execution': 'job_execution'
    }

    def __init__(self, job_execution=None):
        """ShowJobExesResponse

        The model defined in huaweicloud sdk

        :param job_execution: 
        :type job_execution: :class:`huaweicloudsdkmrs.v1.JobExeResult`
        """
        
        super(ShowJobExesResponse, self).__init__()

        self._job_execution = None
        self.discriminator = None

        if job_execution is not None:
            self.job_execution = job_execution

    @property
    def job_execution(self):
        """Gets the job_execution of this ShowJobExesResponse.

        :return: The job_execution of this ShowJobExesResponse.
        :rtype: :class:`huaweicloudsdkmrs.v1.JobExeResult`
        """
        return self._job_execution

    @job_execution.setter
    def job_execution(self, job_execution):
        """Sets the job_execution of this ShowJobExesResponse.

        :param job_execution: The job_execution of this ShowJobExesResponse.
        :type job_execution: :class:`huaweicloudsdkmrs.v1.JobExeResult`
        """
        self._job_execution = job_execution

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
        if not isinstance(other, ShowJobExesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
