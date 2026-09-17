# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'task_uri': 'str',
        'version_uri': 'str'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'task_uri': 'task_uri',
        'version_uri': 'version_uri'
    }

    def __init__(self, project_uuid=None, task_uri=None, version_uri=None):
        r"""ShowTaskRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param task_uri: 测试套件uri
        :type task_uri: str
        :param version_uri: 分支/迭代uri
        :type version_uri: str
        """
        
        

        self._project_uuid = None
        self._task_uri = None
        self._version_uri = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.task_uri = task_uri
        if version_uri is not None:
            self.version_uri = version_uri

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ShowTaskRequest.

        项目id

        :return: The project_uuid of this ShowTaskRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ShowTaskRequest.

        项目id

        :param project_uuid: The project_uuid of this ShowTaskRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def task_uri(self):
        r"""Gets the task_uri of this ShowTaskRequest.

        测试套件uri

        :return: The task_uri of this ShowTaskRequest.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this ShowTaskRequest.

        测试套件uri

        :param task_uri: The task_uri of this ShowTaskRequest.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def version_uri(self):
        r"""Gets the version_uri of this ShowTaskRequest.

        分支/迭代uri

        :return: The version_uri of this ShowTaskRequest.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this ShowTaskRequest.

        分支/迭代uri

        :param version_uri: The version_uri of this ShowTaskRequest.
        :type version_uri: str
        """
        self._version_uri = version_uri

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
