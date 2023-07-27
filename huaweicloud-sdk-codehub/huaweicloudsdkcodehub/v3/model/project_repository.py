# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectRepository:

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
        'repository_uuid': 'str'
    }

    attribute_map = {
        'project_uuid': 'projectUuid',
        'repository_uuid': 'repositoryUuid'
    }

    def __init__(self, project_uuid=None, repository_uuid=None):
        """ProjectRepository

        The model defined in huaweicloud sdk

        :param project_uuid: 项目ID，获取方式请参见[获取项目ID](codehub_api_0014.xml)。
        :type project_uuid: str
        :param repository_uuid: 仓库UUID
        :type repository_uuid: str
        """
        
        

        self._project_uuid = None
        self._repository_uuid = None
        self.discriminator = None

        if project_uuid is not None:
            self.project_uuid = project_uuid
        if repository_uuid is not None:
            self.repository_uuid = repository_uuid

    @property
    def project_uuid(self):
        """Gets the project_uuid of this ProjectRepository.

        项目ID，获取方式请参见[获取项目ID](codehub_api_0014.xml)。

        :return: The project_uuid of this ProjectRepository.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this ProjectRepository.

        项目ID，获取方式请参见[获取项目ID](codehub_api_0014.xml)。

        :param project_uuid: The project_uuid of this ProjectRepository.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def repository_uuid(self):
        """Gets the repository_uuid of this ProjectRepository.

        仓库UUID

        :return: The repository_uuid of this ProjectRepository.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        """Sets the repository_uuid of this ProjectRepository.

        仓库UUID

        :param repository_uuid: The repository_uuid of this ProjectRepository.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

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
        if not isinstance(other, ProjectRepository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
