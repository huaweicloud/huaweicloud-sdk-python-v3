# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Workspaces:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'int',
        'description': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'id': 'str',
        'name': 'str',
        'owner': 'str',
        'status': 'str',
        'update_at': 'int',
        'user_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'id': 'id',
        'name': 'name',
        'owner': 'owner',
        'status': 'status',
        'update_at': 'update_at',
        'user_id': 'userId',
        'project_id': 'projectId'
    }

    def __init__(self, created_at=None, description=None, enterprise_project_id=None, enterprise_project_name=None, id=None, name=None, owner=None, status=None, update_at=None, user_id=None, project_id=None):
        r"""Workspaces

        The model defined in huaweicloud sdk

        :param created_at: 创建时间。
        :type created_at: int
        :param description: 描述。
        :type description: str
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param id: 工作空间id。
        :type id: str
        :param name: 工作空间名称。
        :type name: str
        :param owner: 创建者。
        :type owner: str
        :param status: 状态。
        :type status: str
        :param update_at: 更新时间。
        :type update_at: int
        :param user_id: 用户id。
        :type user_id: str
        :param project_id: 调用账户的项目Id
        :type project_id: str
        """
        
        

        self._created_at = None
        self._description = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._id = None
        self._name = None
        self._owner = None
        self._status = None
        self._update_at = None
        self._user_id = None
        self._project_id = None
        self.discriminator = None

        self.created_at = created_at
        self.description = description
        self.enterprise_project_id = enterprise_project_id
        self.enterprise_project_name = enterprise_project_name
        self.id = id
        self.name = name
        self.owner = owner
        self.status = status
        self.update_at = update_at
        self.user_id = user_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this Workspaces.

        创建时间。

        :return: The created_at of this Workspaces.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Workspaces.

        创建时间。

        :param created_at: The created_at of this Workspaces.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def description(self):
        r"""Gets the description of this Workspaces.

        描述。

        :return: The description of this Workspaces.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Workspaces.

        描述。

        :param description: The description of this Workspaces.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Workspaces.

        企业项目id。

        :return: The enterprise_project_id of this Workspaces.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Workspaces.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this Workspaces.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this Workspaces.

        企业项目名称。

        :return: The enterprise_project_name of this Workspaces.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this Workspaces.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this Workspaces.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def id(self):
        r"""Gets the id of this Workspaces.

        工作空间id。

        :return: The id of this Workspaces.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Workspaces.

        工作空间id。

        :param id: The id of this Workspaces.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Workspaces.

        工作空间名称。

        :return: The name of this Workspaces.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Workspaces.

        工作空间名称。

        :param name: The name of this Workspaces.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this Workspaces.

        创建者。

        :return: The owner of this Workspaces.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this Workspaces.

        创建者。

        :param owner: The owner of this Workspaces.
        :type owner: str
        """
        self._owner = owner

    @property
    def status(self):
        r"""Gets the status of this Workspaces.

        状态。

        :return: The status of this Workspaces.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Workspaces.

        状态。

        :param status: The status of this Workspaces.
        :type status: str
        """
        self._status = status

    @property
    def update_at(self):
        r"""Gets the update_at of this Workspaces.

        更新时间。

        :return: The update_at of this Workspaces.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this Workspaces.

        更新时间。

        :param update_at: The update_at of this Workspaces.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def user_id(self):
        r"""Gets the user_id of this Workspaces.

        用户id。

        :return: The user_id of this Workspaces.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this Workspaces.

        用户id。

        :param user_id: The user_id of this Workspaces.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def project_id(self):
        r"""Gets the project_id of this Workspaces.

        调用账户的项目Id

        :return: The project_id of this Workspaces.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Workspaces.

        调用账户的项目Id

        :param project_id: The project_id of this Workspaces.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, Workspaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
