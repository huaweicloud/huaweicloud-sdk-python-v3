# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnlockRepositoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'repository_id': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'repository_id': 'repository_id'
    }

    def __init__(self, project_id=None, repository_id=None):
        """UnlockRepositoryRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param repository_id: 仓库的主键id
        :type repository_id: int
        """
        
        

        self._project_id = None
        self._repository_id = None
        self.discriminator = None

        self.project_id = project_id
        self.repository_id = repository_id

    @property
    def project_id(self):
        """Gets the project_id of this UnlockRepositoryRequest.

        项目id

        :return: The project_id of this UnlockRepositoryRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UnlockRepositoryRequest.

        项目id

        :param project_id: The project_id of this UnlockRepositoryRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repository_id(self):
        """Gets the repository_id of this UnlockRepositoryRequest.

        仓库的主键id

        :return: The repository_id of this UnlockRepositoryRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this UnlockRepositoryRequest.

        仓库的主键id

        :param repository_id: The repository_id of this UnlockRepositoryRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

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
        if not isinstance(other, UnlockRepositoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
