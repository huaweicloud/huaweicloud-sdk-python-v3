# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'user_name': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'login_permission': 'bool',
        'root_permission': 'bool',
        'user_group': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'category': 'str',
        'part_match': 'bool'
    }

    attribute_map = {
        'host_id': 'host_id',
        'user_name': 'user_name',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'login_permission': 'login_permission',
        'root_permission': 'root_permission',
        'user_group': 'user_group',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'category': 'category',
        'part_match': 'part_match'
    }

    def __init__(self, host_id=None, user_name=None, host_name=None, private_ip=None, login_permission=None, root_permission=None, user_group=None, enterprise_project_id=None, limit=None, offset=None, category=None, part_match=None):
        """ListUsersRequest

        The model defined in huaweicloud sdk

        :param host_id: 主机ID
        :type host_id: str
        :param user_name: 账号名称
        :type user_name: str
        :param host_name: 主机名称
        :type host_name: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param login_permission: 是否允许登录
        :type login_permission: bool
        :param root_permission: 是否有root权限
        :type root_permission: bool
        :param user_group: 主机用户组
        :type user_group: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param category: 类别，默认为host，包含如下： - host：主机 - container：容器
        :type category: str
        :param part_match: 是否模糊匹配，默认false表示精确匹配
        :type part_match: bool
        """
        
        

        self._host_id = None
        self._user_name = None
        self._host_name = None
        self._private_ip = None
        self._login_permission = None
        self._root_permission = None
        self._user_group = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._category = None
        self._part_match = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if user_name is not None:
            self.user_name = user_name
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if login_permission is not None:
            self.login_permission = login_permission
        if root_permission is not None:
            self.root_permission = root_permission
        if user_group is not None:
            self.user_group = user_group
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if category is not None:
            self.category = category
        if part_match is not None:
            self.part_match = part_match

    @property
    def host_id(self):
        """Gets the host_id of this ListUsersRequest.

        主机ID

        :return: The host_id of this ListUsersRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListUsersRequest.

        主机ID

        :param host_id: The host_id of this ListUsersRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def user_name(self):
        """Gets the user_name of this ListUsersRequest.

        账号名称

        :return: The user_name of this ListUsersRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListUsersRequest.

        账号名称

        :param user_name: The user_name of this ListUsersRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def host_name(self):
        """Gets the host_name of this ListUsersRequest.

        主机名称

        :return: The host_name of this ListUsersRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListUsersRequest.

        主机名称

        :param host_name: The host_name of this ListUsersRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        """Gets the private_ip of this ListUsersRequest.

        服务器私有IP

        :return: The private_ip of this ListUsersRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListUsersRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListUsersRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def login_permission(self):
        """Gets the login_permission of this ListUsersRequest.

        是否允许登录

        :return: The login_permission of this ListUsersRequest.
        :rtype: bool
        """
        return self._login_permission

    @login_permission.setter
    def login_permission(self, login_permission):
        """Sets the login_permission of this ListUsersRequest.

        是否允许登录

        :param login_permission: The login_permission of this ListUsersRequest.
        :type login_permission: bool
        """
        self._login_permission = login_permission

    @property
    def root_permission(self):
        """Gets the root_permission of this ListUsersRequest.

        是否有root权限

        :return: The root_permission of this ListUsersRequest.
        :rtype: bool
        """
        return self._root_permission

    @root_permission.setter
    def root_permission(self, root_permission):
        """Sets the root_permission of this ListUsersRequest.

        是否有root权限

        :param root_permission: The root_permission of this ListUsersRequest.
        :type root_permission: bool
        """
        self._root_permission = root_permission

    @property
    def user_group(self):
        """Gets the user_group of this ListUsersRequest.

        主机用户组

        :return: The user_group of this ListUsersRequest.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this ListUsersRequest.

        主机用户组

        :param user_group: The user_group of this ListUsersRequest.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListUsersRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListUsersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListUsersRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListUsersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListUsersRequest.

        每页显示数量

        :return: The limit of this ListUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUsersRequest.

        每页显示数量

        :param limit: The limit of this ListUsersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListUsersRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUsersRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def category(self):
        """Gets the category of this ListUsersRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :return: The category of this ListUsersRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListUsersRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :param category: The category of this ListUsersRequest.
        :type category: str
        """
        self._category = category

    @property
    def part_match(self):
        """Gets the part_match of this ListUsersRequest.

        是否模糊匹配，默认false表示精确匹配

        :return: The part_match of this ListUsersRequest.
        :rtype: bool
        """
        return self._part_match

    @part_match.setter
    def part_match(self, part_match):
        """Sets the part_match of this ListUsersRequest.

        是否模糊匹配，默认false表示精确匹配

        :param part_match: The part_match of this ListUsersRequest.
        :type part_match: bool
        """
        self._part_match = part_match

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
        if not isinstance(other, ListUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
