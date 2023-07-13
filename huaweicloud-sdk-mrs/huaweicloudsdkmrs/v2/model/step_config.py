# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_execution': 'JobExecution'
    }

    attribute_map = {
        'job_execution': 'job_execution'
    }

    def __init__(self, job_execution=None):
        """StepConfig

        The model defined in huaweicloud sdk

        :param job_execution: 
        :type job_execution: :class:`huaweicloudsdkmrs.v2.JobExecution`
        """
        
        

        self._job_execution = None
        self.discriminator = None

        self.job_execution = job_execution

    @property
    def job_execution(self):
        """Gets the job_execution of this StepConfig.

        :return: The job_execution of this StepConfig.
        :rtype: :class:`huaweicloudsdkmrs.v2.JobExecution`
        """
        return self._job_execution

    @job_execution.setter
    def job_execution(self, job_execution):
        """Sets the job_execution of this StepConfig.

        :param job_execution: The job_execution of this StepConfig.
        :type job_execution: :class:`huaweicloudsdkmrs.v2.JobExecution`
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
        if not isinstance(other, StepConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
