# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobRespJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'status_name': 'str',
        'status_desc': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status_name': 'status_name',
        'status_desc': 'status_desc'
    }

    def __init__(self, job_id=None, status_name=None, status_desc=None):
        """CreateJobRespJob

        The model defined in huaweicloud sdk

        :param job_id: 作业Id。
        :type job_id: int
        :param status_name: 作业状态名称。
        :type status_name: str
        :param status_desc: 当前状态描述，包含异常状态原因及建议。
        :type status_desc: str
        """
        
        

        self._job_id = None
        self._status_name = None
        self._status_desc = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status_name is not None:
            self.status_name = status_name
        if status_desc is not None:
            self.status_desc = status_desc

    @property
    def job_id(self):
        """Gets the job_id of this CreateJobRespJob.

        作业Id。

        :return: The job_id of this CreateJobRespJob.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateJobRespJob.

        作业Id。

        :param job_id: The job_id of this CreateJobRespJob.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def status_name(self):
        """Gets the status_name of this CreateJobRespJob.

        作业状态名称。

        :return: The status_name of this CreateJobRespJob.
        :rtype: str
        """
        return self._status_name

    @status_name.setter
    def status_name(self, status_name):
        """Sets the status_name of this CreateJobRespJob.

        作业状态名称。

        :param status_name: The status_name of this CreateJobRespJob.
        :type status_name: str
        """
        self._status_name = status_name

    @property
    def status_desc(self):
        """Gets the status_desc of this CreateJobRespJob.

        当前状态描述，包含异常状态原因及建议。

        :return: The status_desc of this CreateJobRespJob.
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this CreateJobRespJob.

        当前状态描述，包含异常状态原因及建议。

        :param status_desc: The status_desc of this CreateJobRespJob.
        :type status_desc: str
        """
        self._status_desc = status_desc

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
        if not isinstance(other, CreateJobRespJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
