# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'job_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'job_name': 'job_name'
    }

    def __init__(self, workspace=None, job_name=None):
        """ShowJobStatusRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param job_name: 作业名称.
        :type job_name: str
        """
        
        

        self._workspace = None
        self._job_name = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.job_name = job_name

    @property
    def workspace(self):
        """Gets the workspace of this ShowJobStatusRequest.

        工作空间id

        :return: The workspace of this ShowJobStatusRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowJobStatusRequest.

        工作空间id

        :param workspace: The workspace of this ShowJobStatusRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def job_name(self):
        """Gets the job_name of this ShowJobStatusRequest.

        作业名称.

        :return: The job_name of this ShowJobStatusRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowJobStatusRequest.

        作业名称.

        :param job_name: The job_name of this ShowJobStatusRequest.
        :type job_name: str
        """
        self._job_name = job_name

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
        if not isinstance(other, ShowJobStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
