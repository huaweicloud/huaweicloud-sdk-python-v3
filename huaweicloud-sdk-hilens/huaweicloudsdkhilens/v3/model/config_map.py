# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'list[Config]',
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'tags': 'list[Tag]',
        'type': 'str',
        'updated_at': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'configs': 'configs',
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'tags': 'tags',
        'type': 'type',
        'updated_at': 'updated_at',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, configs=None, created_at=None, description=None, id=None, name=None, project_id=None, tags=None, type=None, updated_at=None, workspace_id=None):
        """ConfigMap

        The model defined in huaweicloud sdk

        :param configs: 配置列表
        :type configs: list[:class:`huaweicloudsdkhilens.v3.Config`]
        :param created_at: 创建时间
        :type created_at: str
        :param description: 描述
        :type description: str
        :param id: 配置项ID
        :type id: str
        :param name: 名称
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        :param type: 类型
        :type type: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        """
        
        

        self._configs = None
        self._created_at = None
        self._description = None
        self._id = None
        self._name = None
        self._project_id = None
        self._tags = None
        self._type = None
        self._updated_at = None
        self._workspace_id = None
        self.discriminator = None

        self.configs = configs
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        self.name = name
        if project_id is not None:
            self.project_id = project_id
        self.tags = tags
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def configs(self):
        """Gets the configs of this ConfigMap.

        配置列表

        :return: The configs of this ConfigMap.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Config`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ConfigMap.

        配置列表

        :param configs: The configs of this ConfigMap.
        :type configs: list[:class:`huaweicloudsdkhilens.v3.Config`]
        """
        self._configs = configs

    @property
    def created_at(self):
        """Gets the created_at of this ConfigMap.

        创建时间

        :return: The created_at of this ConfigMap.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConfigMap.

        创建时间

        :param created_at: The created_at of this ConfigMap.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ConfigMap.

        描述

        :return: The description of this ConfigMap.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigMap.

        描述

        :param description: The description of this ConfigMap.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this ConfigMap.

        配置项ID

        :return: The id of this ConfigMap.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigMap.

        配置项ID

        :param id: The id of this ConfigMap.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ConfigMap.

        名称

        :return: The name of this ConfigMap.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigMap.

        名称

        :param name: The name of this ConfigMap.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ConfigMap.

        项目ID

        :return: The project_id of this ConfigMap.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ConfigMap.

        项目ID

        :param project_id: The project_id of this ConfigMap.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tags(self):
        """Gets the tags of this ConfigMap.

        标签列表

        :return: The tags of this ConfigMap.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ConfigMap.

        标签列表

        :param tags: The tags of this ConfigMap.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        self._tags = tags

    @property
    def type(self):
        """Gets the type of this ConfigMap.

        类型

        :return: The type of this ConfigMap.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigMap.

        类型

        :param type: The type of this ConfigMap.
        :type type: str
        """
        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this ConfigMap.

        更新时间

        :return: The updated_at of this ConfigMap.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ConfigMap.

        更新时间

        :param updated_at: The updated_at of this ConfigMap.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ConfigMap.

        工作空间ID

        :return: The workspace_id of this ConfigMap.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ConfigMap.

        工作空间ID

        :param workspace_id: The workspace_id of this ConfigMap.
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
        if not isinstance(other, ConfigMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
