# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'workspace_id': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'secrets': 'list[Secret]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'secrets': 'secrets',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, workspace_id=None, project_id=None, created_at=None, updated_at=None, secrets=None, tags=None):
        """SecretDetail

        The model defined in huaweicloud sdk

        :param id: 密钥ID
        :type id: str
        :param name: 密钥名称
        :type name: str
        :param description: 密钥描述
        :type description: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 密钥创建时间
        :type created_at: str
        :param updated_at: 密钥更新时间
        :type updated_at: str
        :param secrets: 密钥列表
        :type secrets: list[:class:`huaweicloudsdkhilens.v3.Secret`]
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._workspace_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._secrets = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if secrets is not None:
            self.secrets = secrets
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this SecretDetail.

        密钥ID

        :return: The id of this SecretDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecretDetail.

        密钥ID

        :param id: The id of this SecretDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SecretDetail.

        密钥名称

        :return: The name of this SecretDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecretDetail.

        密钥名称

        :param name: The name of this SecretDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecretDetail.

        密钥描述

        :return: The description of this SecretDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecretDetail.

        密钥描述

        :param description: The description of this SecretDetail.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        """Gets the workspace_id of this SecretDetail.

        工作空间ID

        :return: The workspace_id of this SecretDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this SecretDetail.

        工作空间ID

        :param workspace_id: The workspace_id of this SecretDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def project_id(self):
        """Gets the project_id of this SecretDetail.

        项目ID

        :return: The project_id of this SecretDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SecretDetail.

        项目ID

        :param project_id: The project_id of this SecretDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this SecretDetail.

        密钥创建时间

        :return: The created_at of this SecretDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SecretDetail.

        密钥创建时间

        :param created_at: The created_at of this SecretDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SecretDetail.

        密钥更新时间

        :return: The updated_at of this SecretDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SecretDetail.

        密钥更新时间

        :param updated_at: The updated_at of this SecretDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def secrets(self):
        """Gets the secrets of this SecretDetail.

        密钥列表

        :return: The secrets of this SecretDetail.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Secret`]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this SecretDetail.

        密钥列表

        :param secrets: The secrets of this SecretDetail.
        :type secrets: list[:class:`huaweicloudsdkhilens.v3.Secret`]
        """
        self._secrets = secrets

    @property
    def tags(self):
        """Gets the tags of this SecretDetail.

        标签列表

        :return: The tags of this SecretDetail.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SecretDetail.

        标签列表

        :param tags: The tags of this SecretDetail.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, SecretDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
