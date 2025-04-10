# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_status': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'rollback_enabled': 'bool'
    }

    attribute_map = {
        'execution_status': 'execution_status',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'rollback_enabled': 'rollback_enabled'
    }

    def __init__(self, execution_status=None, job_id=None, job_type=None, rollback_enabled=None):
        r"""JobInfo

        The model defined in huaweicloud sdk

        :param execution_status: 
        :type execution_status: str
        :param job_id: 
        :type job_id: str
        :param job_type: 
        :type job_type: str
        :param rollback_enabled: 
        :type rollback_enabled: bool
        """
        
        

        self._execution_status = None
        self._job_id = None
        self._job_type = None
        self._rollback_enabled = None
        self.discriminator = None

        if execution_status is not None:
            self.execution_status = execution_status
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if rollback_enabled is not None:
            self.rollback_enabled = rollback_enabled

    @property
    def execution_status(self):
        r"""Gets the execution_status of this JobInfo.

        :return: The execution_status of this JobInfo.
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        r"""Sets the execution_status of this JobInfo.

        :param execution_status: The execution_status of this JobInfo.
        :type execution_status: str
        """
        self._execution_status = execution_status

    @property
    def job_id(self):
        r"""Gets the job_id of this JobInfo.

        :return: The job_id of this JobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this JobInfo.

        :param job_id: The job_id of this JobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this JobInfo.

        :return: The job_type of this JobInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobInfo.

        :param job_type: The job_type of this JobInfo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def rollback_enabled(self):
        r"""Gets the rollback_enabled of this JobInfo.

        :return: The rollback_enabled of this JobInfo.
        :rtype: bool
        """
        return self._rollback_enabled

    @rollback_enabled.setter
    def rollback_enabled(self, rollback_enabled):
        r"""Sets the rollback_enabled of this JobInfo.

        :param rollback_enabled: The rollback_enabled of this JobInfo.
        :type rollback_enabled: bool
        """
        self._rollback_enabled = rollback_enabled

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
        if not isinstance(other, JobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
