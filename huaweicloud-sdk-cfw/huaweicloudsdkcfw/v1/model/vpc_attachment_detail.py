# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcAttachmentDetail:

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
        'vpc_id': 'str',
        'virsubnet_id': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'tags': 'list[Tag]',
        'description': 'str',
        'project_id': 'str',
        'vpc_project_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags',
        'description': 'description',
        'project_id': 'project_id',
        'vpc_project_id': 'vpc_project_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, vpc_id=None, virsubnet_id=None, state=None, created_at=None, updated_at=None, tags=None, description=None, project_id=None, vpc_project_id=None, enterprise_project_id=None):
        """VpcAttachmentDetail

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param name: 名称
        :type name: str
        :param vpc_id: vpc id
        :type vpc_id: str
        :param virsubnet_id: 子网id
        :type virsubnet_id: str
        :param state: 状态
        :type state: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkcfw.v1.Tag`]
        :param description: 描述
        :type description: str
        :param project_id: 项目id
        :type project_id: str
        :param vpc_project_id: vpc项目id
        :type vpc_project_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._vpc_id = None
        self._virsubnet_id = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self._description = None
        self._project_id = None
        self._vpc_project_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if vpc_project_id is not None:
            self.vpc_project_id = vpc_project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this VpcAttachmentDetail.

        id

        :return: The id of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpcAttachmentDetail.

        id

        :param id: The id of this VpcAttachmentDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VpcAttachmentDetail.

        名称

        :return: The name of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpcAttachmentDetail.

        名称

        :param name: The name of this VpcAttachmentDetail.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this VpcAttachmentDetail.

        vpc id

        :return: The vpc_id of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this VpcAttachmentDetail.

        vpc id

        :param vpc_id: The vpc_id of this VpcAttachmentDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this VpcAttachmentDetail.

        子网id

        :return: The virsubnet_id of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this VpcAttachmentDetail.

        子网id

        :param virsubnet_id: The virsubnet_id of this VpcAttachmentDetail.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def state(self):
        """Gets the state of this VpcAttachmentDetail.

        状态

        :return: The state of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VpcAttachmentDetail.

        状态

        :param state: The state of this VpcAttachmentDetail.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this VpcAttachmentDetail.

        创建时间

        :return: The created_at of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VpcAttachmentDetail.

        创建时间

        :param created_at: The created_at of this VpcAttachmentDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VpcAttachmentDetail.

        更新时间

        :return: The updated_at of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VpcAttachmentDetail.

        更新时间

        :param updated_at: The updated_at of this VpcAttachmentDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        """Gets the tags of this VpcAttachmentDetail.

        标签

        :return: The tags of this VpcAttachmentDetail.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VpcAttachmentDetail.

        标签

        :param tags: The tags of this VpcAttachmentDetail.
        :type tags: list[:class:`huaweicloudsdkcfw.v1.Tag`]
        """
        self._tags = tags

    @property
    def description(self):
        """Gets the description of this VpcAttachmentDetail.

        描述

        :return: The description of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VpcAttachmentDetail.

        描述

        :param description: The description of this VpcAttachmentDetail.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this VpcAttachmentDetail.

        项目id

        :return: The project_id of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this VpcAttachmentDetail.

        项目id

        :param project_id: The project_id of this VpcAttachmentDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vpc_project_id(self):
        """Gets the vpc_project_id of this VpcAttachmentDetail.

        vpc项目id

        :return: The vpc_project_id of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._vpc_project_id

    @vpc_project_id.setter
    def vpc_project_id(self, vpc_project_id):
        """Sets the vpc_project_id of this VpcAttachmentDetail.

        vpc项目id

        :param vpc_project_id: The vpc_project_id of this VpcAttachmentDetail.
        :type vpc_project_id: str
        """
        self._vpc_project_id = vpc_project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this VpcAttachmentDetail.

        企业项目id

        :return: The enterprise_project_id of this VpcAttachmentDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this VpcAttachmentDetail.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this VpcAttachmentDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, VpcAttachmentDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
