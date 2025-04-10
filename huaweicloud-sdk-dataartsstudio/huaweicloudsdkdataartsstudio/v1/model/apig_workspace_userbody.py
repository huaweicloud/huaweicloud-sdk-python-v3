# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigWorkspaceUserbody:

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
        'user_id': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'display_user_name': 'str',
        'domain_owner': 'bool',
        'description': 'str',
        'workspace_id': 'str',
        'roles': 'list[ApigRoleVo]',
        'create_time': 'float',
        'create_user': 'str',
        'update_time': 'float',
        'update_user': 'str',
        'type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'display_user_name': 'display_user_name',
        'domain_owner': 'domain_owner',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'roles': 'roles',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'type': 'type'
    }

    def __init__(self, id=None, user_id=None, user_name=None, domain_id=None, domain_name=None, display_user_name=None, domain_owner=None, description=None, workspace_id=None, roles=None, create_time=None, create_user=None, update_time=None, update_user=None, type=None):
        r"""ApigWorkspaceUserbody

        The model defined in huaweicloud sdk

        :param id: 记录id
        :type id: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param domain_id: 租户id
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param display_user_name: 租户名
        :type display_user_name: str
        :param domain_owner: 是否是空间所有者
        :type domain_owner: bool
        :param description: 描述
        :type description: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param roles: 角色列表
        :type roles: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigRoleVo`]
        :param create_time: 创建时间
        :type create_time: float
        :param create_user: 创建人员
        :type create_user: str
        :param update_time: 更新时间
        :type update_time: float
        :param update_user: 更新人员
        :type update_user: str
        :param type: 用户类型，0用户，1用户组
        :type type: int
        """
        
        

        self._id = None
        self._user_id = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._display_user_name = None
        self._domain_owner = None
        self._description = None
        self._workspace_id = None
        self._roles = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if display_user_name is not None:
            self.display_user_name = display_user_name
        if domain_owner is not None:
            self.domain_owner = domain_owner
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if roles is not None:
            self.roles = roles
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this ApigWorkspaceUserbody.

        记录id

        :return: The id of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApigWorkspaceUserbody.

        记录id

        :param id: The id of this ApigWorkspaceUserbody.
        :type id: str
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this ApigWorkspaceUserbody.

        用户id

        :return: The user_id of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ApigWorkspaceUserbody.

        用户id

        :param user_id: The user_id of this ApigWorkspaceUserbody.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ApigWorkspaceUserbody.

        用户名

        :return: The user_name of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ApigWorkspaceUserbody.

        用户名

        :param user_name: The user_name of this ApigWorkspaceUserbody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ApigWorkspaceUserbody.

        租户id

        :return: The domain_id of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ApigWorkspaceUserbody.

        租户id

        :param domain_id: The domain_id of this ApigWorkspaceUserbody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ApigWorkspaceUserbody.

        租户名

        :return: The domain_name of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ApigWorkspaceUserbody.

        租户名

        :param domain_name: The domain_name of this ApigWorkspaceUserbody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def display_user_name(self):
        r"""Gets the display_user_name of this ApigWorkspaceUserbody.

        租户名

        :return: The display_user_name of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._display_user_name

    @display_user_name.setter
    def display_user_name(self, display_user_name):
        r"""Sets the display_user_name of this ApigWorkspaceUserbody.

        租户名

        :param display_user_name: The display_user_name of this ApigWorkspaceUserbody.
        :type display_user_name: str
        """
        self._display_user_name = display_user_name

    @property
    def domain_owner(self):
        r"""Gets the domain_owner of this ApigWorkspaceUserbody.

        是否是空间所有者

        :return: The domain_owner of this ApigWorkspaceUserbody.
        :rtype: bool
        """
        return self._domain_owner

    @domain_owner.setter
    def domain_owner(self, domain_owner):
        r"""Sets the domain_owner of this ApigWorkspaceUserbody.

        是否是空间所有者

        :param domain_owner: The domain_owner of this ApigWorkspaceUserbody.
        :type domain_owner: bool
        """
        self._domain_owner = domain_owner

    @property
    def description(self):
        r"""Gets the description of this ApigWorkspaceUserbody.

        描述

        :return: The description of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApigWorkspaceUserbody.

        描述

        :param description: The description of this ApigWorkspaceUserbody.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ApigWorkspaceUserbody.

        工作空间id

        :return: The workspace_id of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ApigWorkspaceUserbody.

        工作空间id

        :param workspace_id: The workspace_id of this ApigWorkspaceUserbody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def roles(self):
        r"""Gets the roles of this ApigWorkspaceUserbody.

        角色列表

        :return: The roles of this ApigWorkspaceUserbody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigRoleVo`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ApigWorkspaceUserbody.

        角色列表

        :param roles: The roles of this ApigWorkspaceUserbody.
        :type roles: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigRoleVo`]
        """
        self._roles = roles

    @property
    def create_time(self):
        r"""Gets the create_time of this ApigWorkspaceUserbody.

        创建时间

        :return: The create_time of this ApigWorkspaceUserbody.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ApigWorkspaceUserbody.

        创建时间

        :param create_time: The create_time of this ApigWorkspaceUserbody.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ApigWorkspaceUserbody.

        创建人员

        :return: The create_user of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ApigWorkspaceUserbody.

        创建人员

        :param create_user: The create_user of this ApigWorkspaceUserbody.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this ApigWorkspaceUserbody.

        更新时间

        :return: The update_time of this ApigWorkspaceUserbody.
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ApigWorkspaceUserbody.

        更新时间

        :param update_time: The update_time of this ApigWorkspaceUserbody.
        :type update_time: float
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this ApigWorkspaceUserbody.

        更新人员

        :return: The update_user of this ApigWorkspaceUserbody.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this ApigWorkspaceUserbody.

        更新人员

        :param update_user: The update_user of this ApigWorkspaceUserbody.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def type(self):
        r"""Gets the type of this ApigWorkspaceUserbody.

        用户类型，0用户，1用户组

        :return: The type of this ApigWorkspaceUserbody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ApigWorkspaceUserbody.

        用户类型，0用户，1用户组

        :param type: The type of this ApigWorkspaceUserbody.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ApigWorkspaceUserbody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
