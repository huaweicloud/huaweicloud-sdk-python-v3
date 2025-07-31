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
        r"""ListUsersRequest

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param user_name: **参数解释**: 账号名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 
        :type user_name: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param login_permission: **参数解释**: 是否允许登录 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 
        :type login_permission: bool
        :param root_permission: **参数解释**: 是否有root权限 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 
        :type root_permission: bool
        :param user_group: **参数解释**: 是否是主机用户组 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 
        :type user_group: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param category: **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器  **默认取值**: 不涉及 
        :type category: str
        :param part_match: **参数解释**: 是否模糊匹配 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 
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
        r"""Gets the host_id of this ListUsersRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListUsersRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListUsersRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListUsersRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ListUsersRequest.

        **参数解释**: 账号名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :return: The user_name of this ListUsersRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListUsersRequest.

        **参数解释**: 账号名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :param user_name: The user_name of this ListUsersRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListUsersRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListUsersRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListUsersRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListUsersRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListUsersRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListUsersRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListUsersRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListUsersRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def login_permission(self):
        r"""Gets the login_permission of this ListUsersRequest.

        **参数解释**: 是否允许登录 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :return: The login_permission of this ListUsersRequest.
        :rtype: bool
        """
        return self._login_permission

    @login_permission.setter
    def login_permission(self, login_permission):
        r"""Sets the login_permission of this ListUsersRequest.

        **参数解释**: 是否允许登录 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :param login_permission: The login_permission of this ListUsersRequest.
        :type login_permission: bool
        """
        self._login_permission = login_permission

    @property
    def root_permission(self):
        r"""Gets the root_permission of this ListUsersRequest.

        **参数解释**: 是否有root权限 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :return: The root_permission of this ListUsersRequest.
        :rtype: bool
        """
        return self._root_permission

    @root_permission.setter
    def root_permission(self, root_permission):
        r"""Sets the root_permission of this ListUsersRequest.

        **参数解释**: 是否有root权限 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :param root_permission: The root_permission of this ListUsersRequest.
        :type root_permission: bool
        """
        self._root_permission = root_permission

    @property
    def user_group(self):
        r"""Gets the user_group of this ListUsersRequest.

        **参数解释**: 是否是主机用户组 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :return: The user_group of this ListUsersRequest.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        r"""Sets the user_group of this ListUsersRequest.

        **参数解释**: 是否是主机用户组 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :param user_group: The user_group of this ListUsersRequest.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListUsersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListUsersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListUsersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListUsersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListUsersRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUsersRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListUsersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUsersRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUsersRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def category(self):
        r"""Gets the category of this ListUsersRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器  **默认取值**: 不涉及 

        :return: The category of this ListUsersRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListUsersRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器  **默认取值**: 不涉及 

        :param category: The category of this ListUsersRequest.
        :type category: str
        """
        self._category = category

    @property
    def part_match(self):
        r"""Gets the part_match of this ListUsersRequest.

        **参数解释**: 是否模糊匹配 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :return: The part_match of this ListUsersRequest.
        :rtype: bool
        """
        return self._part_match

    @part_match.setter
    def part_match(self, part_match):
        r"""Sets the part_match of this ListUsersRequest.

        **参数解释**: 是否模糊匹配 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

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
