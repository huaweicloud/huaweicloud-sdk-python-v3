# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFactorySupplementDataInstanceRequestBodyDependJobs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, job_name=None, workspace_id=None):
        """CreateFactorySupplementDataInstanceRequestBodyDependJobs

        The model defined in huaweicloud sdk

        :param job_name: 依赖的作业名称
        :type job_name: str
        :param workspace_id: 依赖的作业名称的空间ID
        :type workspace_id: str
        """
        
        

        self._job_name = None
        self._workspace_id = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def job_name(self):
        """Gets the job_name of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.

        依赖的作业名称

        :return: The job_name of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.

        依赖的作业名称

        :param job_name: The job_name of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.

        依赖的作业名称的空间ID

        :return: The workspace_id of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.

        依赖的作业名称的空间ID

        :param workspace_id: The workspace_id of this CreateFactorySupplementDataInstanceRequestBodyDependJobs.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, CreateFactorySupplementDataInstanceRequestBodyDependJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
