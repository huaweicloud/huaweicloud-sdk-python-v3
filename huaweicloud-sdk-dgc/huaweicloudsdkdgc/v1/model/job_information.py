# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInformation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_space': 'str',
        'job_name': 'str',
        'job_id': 'int'
    }

    attribute_map = {
        'work_space': 'workSpace',
        'job_name': 'jobName',
        'job_id': 'jobId'
    }

    def __init__(self, work_space=None, job_name=None, job_id=None):
        r"""JobInformation

        The model defined in huaweicloud sdk

        :param work_space: 下游作业的工作空间名称
        :type work_space: str
        :param job_name: 下游作业名称
        :type job_name: str
        :param job_id: 下游作业ID
        :type job_id: int
        """
        
        

        self._work_space = None
        self._job_name = None
        self._job_id = None
        self.discriminator = None

        if work_space is not None:
            self.work_space = work_space
        if job_name is not None:
            self.job_name = job_name
        if job_id is not None:
            self.job_id = job_id

    @property
    def work_space(self):
        r"""Gets the work_space of this JobInformation.

        下游作业的工作空间名称

        :return: The work_space of this JobInformation.
        :rtype: str
        """
        return self._work_space

    @work_space.setter
    def work_space(self, work_space):
        r"""Sets the work_space of this JobInformation.

        下游作业的工作空间名称

        :param work_space: The work_space of this JobInformation.
        :type work_space: str
        """
        self._work_space = work_space

    @property
    def job_name(self):
        r"""Gets the job_name of this JobInformation.

        下游作业名称

        :return: The job_name of this JobInformation.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this JobInformation.

        下游作业名称

        :param job_name: The job_name of this JobInformation.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_id(self):
        r"""Gets the job_id of this JobInformation.

        下游作业ID

        :return: The job_id of this JobInformation.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this JobInformation.

        下游作业ID

        :param job_id: The job_id of this JobInformation.
        :type job_id: int
        """
        self._job_id = job_id

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
        if not isinstance(other, JobInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
