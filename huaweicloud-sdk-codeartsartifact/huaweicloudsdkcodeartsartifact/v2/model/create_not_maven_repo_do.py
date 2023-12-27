# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotMavenRepoDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'type': 'str',
        'repository_name': 'str',
        'description': 'str',
        'includes_pattern': 'str',
        'project_id': 'str',
        'share_right': 'str'
    }

    attribute_map = {
        'format': 'format',
        'type': 'type',
        'repository_name': 'repository_name',
        'description': 'description',
        'includes_pattern': 'includes_pattern',
        'project_id': 'project_id',
        'share_right': 'share_right'
    }

    def __init__(self, format=None, type=None, repository_name=None, description=None, includes_pattern=None, project_id=None, share_right=None):
        """CreateNotMavenRepoDO

        The model defined in huaweicloud sdk

        :param format: 仓库格式
        :type format: str
        :param type: 仓库类型
        :type type: str
        :param repository_name: 仓库名称
        :type repository_name: str
        :param description: 仓库描述
        :type description: str
        :param includes_pattern: 路径白名单
        :type includes_pattern: str
        :param project_id: 项目id
        :type project_id: str
        :param share_right: 共享策略
        :type share_right: str
        """
        
        

        self._format = None
        self._type = None
        self._repository_name = None
        self._description = None
        self._includes_pattern = None
        self._project_id = None
        self._share_right = None
        self.discriminator = None

        self.format = format
        self.type = type
        self.repository_name = repository_name
        if description is not None:
            self.description = description
        self.includes_pattern = includes_pattern
        if project_id is not None:
            self.project_id = project_id
        if share_right is not None:
            self.share_right = share_right

    @property
    def format(self):
        """Gets the format of this CreateNotMavenRepoDO.

        仓库格式

        :return: The format of this CreateNotMavenRepoDO.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CreateNotMavenRepoDO.

        仓库格式

        :param format: The format of this CreateNotMavenRepoDO.
        :type format: str
        """
        self._format = format

    @property
    def type(self):
        """Gets the type of this CreateNotMavenRepoDO.

        仓库类型

        :return: The type of this CreateNotMavenRepoDO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateNotMavenRepoDO.

        仓库类型

        :param type: The type of this CreateNotMavenRepoDO.
        :type type: str
        """
        self._type = type

    @property
    def repository_name(self):
        """Gets the repository_name of this CreateNotMavenRepoDO.

        仓库名称

        :return: The repository_name of this CreateNotMavenRepoDO.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this CreateNotMavenRepoDO.

        仓库名称

        :param repository_name: The repository_name of this CreateNotMavenRepoDO.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def description(self):
        """Gets the description of this CreateNotMavenRepoDO.

        仓库描述

        :return: The description of this CreateNotMavenRepoDO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNotMavenRepoDO.

        仓库描述

        :param description: The description of this CreateNotMavenRepoDO.
        :type description: str
        """
        self._description = description

    @property
    def includes_pattern(self):
        """Gets the includes_pattern of this CreateNotMavenRepoDO.

        路径白名单

        :return: The includes_pattern of this CreateNotMavenRepoDO.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        """Sets the includes_pattern of this CreateNotMavenRepoDO.

        路径白名单

        :param includes_pattern: The includes_pattern of this CreateNotMavenRepoDO.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def project_id(self):
        """Gets the project_id of this CreateNotMavenRepoDO.

        项目id

        :return: The project_id of this CreateNotMavenRepoDO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateNotMavenRepoDO.

        项目id

        :param project_id: The project_id of this CreateNotMavenRepoDO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def share_right(self):
        """Gets the share_right of this CreateNotMavenRepoDO.

        共享策略

        :return: The share_right of this CreateNotMavenRepoDO.
        :rtype: str
        """
        return self._share_right

    @share_right.setter
    def share_right(self, share_right):
        """Sets the share_right of this CreateNotMavenRepoDO.

        共享策略

        :param share_right: The share_right of this CreateNotMavenRepoDO.
        :type share_right: str
        """
        self._share_right = share_right

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
        if not isinstance(other, CreateNotMavenRepoDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
