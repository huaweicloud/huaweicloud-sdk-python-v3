# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityConfigUserChangeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'change_type': 'str',
        'login_permission': 'bool',
        'root_permission': 'bool',
        'user_group_name': 'str',
        'user_home_dir': 'str',
        'shell': 'str',
        'user_name': 'str',
        'scan_time': 'int'
    }

    attribute_map = {
        'change_type': 'change_type',
        'login_permission': 'login_permission',
        'root_permission': 'root_permission',
        'user_group_name': 'user_group_name',
        'user_home_dir': 'user_home_dir',
        'shell': 'shell',
        'user_name': 'user_name',
        'scan_time': 'scan_time'
    }

    def __init__(self, change_type=None, login_permission=None, root_permission=None, user_group_name=None, user_home_dir=None, shell=None, user_name=None, scan_time=None):
        r"""SecurityConfigUserChangeInfo

        The model defined in huaweicloud sdk

        :param change_type: **参数解释**： 主机账户历史变动类型 **取值范围**： - add：添加 - delete：删除 - modify：修改 
        :type change_type: str
        :param login_permission: **参数解释**： 是否有登陆权限 **取值范围**： - true：有登录权限 - false：无登录权限 
        :type login_permission: bool
        :param root_permission: **参数解释**： 是否有root权限 **取值范围**： - true：有root权限 - false：无root权限 
        :type root_permission: bool
        :param user_group_name: **参数解释**： 用户组 **取值范围**： 不涉及 
        :type user_group_name: str
        :param user_home_dir: **参数解释**： 用户目录 **取值范围**： 不涉及 
        :type user_home_dir: str
        :param shell: **参数解释**： 用户启动shell **取值范围**： 不涉及 
        :type shell: str
        :param user_name: **参数解释**： 用户名 **取值范围**： 不涉及 
        :type user_name: str
        :param scan_time: **参数解释**： 最新扫描时间，采用时间戳，默认毫秒 **取值范围**： 不涉及 
        :type scan_time: int
        """
        
        

        self._change_type = None
        self._login_permission = None
        self._root_permission = None
        self._user_group_name = None
        self._user_home_dir = None
        self._shell = None
        self._user_name = None
        self._scan_time = None
        self.discriminator = None

        if change_type is not None:
            self.change_type = change_type
        if login_permission is not None:
            self.login_permission = login_permission
        if root_permission is not None:
            self.root_permission = root_permission
        if user_group_name is not None:
            self.user_group_name = user_group_name
        if user_home_dir is not None:
            self.user_home_dir = user_home_dir
        if shell is not None:
            self.shell = shell
        if user_name is not None:
            self.user_name = user_name
        if scan_time is not None:
            self.scan_time = scan_time

    @property
    def change_type(self):
        r"""Gets the change_type of this SecurityConfigUserChangeInfo.

        **参数解释**： 主机账户历史变动类型 **取值范围**： - add：添加 - delete：删除 - modify：修改 

        :return: The change_type of this SecurityConfigUserChangeInfo.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this SecurityConfigUserChangeInfo.

        **参数解释**： 主机账户历史变动类型 **取值范围**： - add：添加 - delete：删除 - modify：修改 

        :param change_type: The change_type of this SecurityConfigUserChangeInfo.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def login_permission(self):
        r"""Gets the login_permission of this SecurityConfigUserChangeInfo.

        **参数解释**： 是否有登陆权限 **取值范围**： - true：有登录权限 - false：无登录权限 

        :return: The login_permission of this SecurityConfigUserChangeInfo.
        :rtype: bool
        """
        return self._login_permission

    @login_permission.setter
    def login_permission(self, login_permission):
        r"""Sets the login_permission of this SecurityConfigUserChangeInfo.

        **参数解释**： 是否有登陆权限 **取值范围**： - true：有登录权限 - false：无登录权限 

        :param login_permission: The login_permission of this SecurityConfigUserChangeInfo.
        :type login_permission: bool
        """
        self._login_permission = login_permission

    @property
    def root_permission(self):
        r"""Gets the root_permission of this SecurityConfigUserChangeInfo.

        **参数解释**： 是否有root权限 **取值范围**： - true：有root权限 - false：无root权限 

        :return: The root_permission of this SecurityConfigUserChangeInfo.
        :rtype: bool
        """
        return self._root_permission

    @root_permission.setter
    def root_permission(self, root_permission):
        r"""Sets the root_permission of this SecurityConfigUserChangeInfo.

        **参数解释**： 是否有root权限 **取值范围**： - true：有root权限 - false：无root权限 

        :param root_permission: The root_permission of this SecurityConfigUserChangeInfo.
        :type root_permission: bool
        """
        self._root_permission = root_permission

    @property
    def user_group_name(self):
        r"""Gets the user_group_name of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户组 **取值范围**： 不涉及 

        :return: The user_group_name of this SecurityConfigUserChangeInfo.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        r"""Sets the user_group_name of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户组 **取值范围**： 不涉及 

        :param user_group_name: The user_group_name of this SecurityConfigUserChangeInfo.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def user_home_dir(self):
        r"""Gets the user_home_dir of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户目录 **取值范围**： 不涉及 

        :return: The user_home_dir of this SecurityConfigUserChangeInfo.
        :rtype: str
        """
        return self._user_home_dir

    @user_home_dir.setter
    def user_home_dir(self, user_home_dir):
        r"""Sets the user_home_dir of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户目录 **取值范围**： 不涉及 

        :param user_home_dir: The user_home_dir of this SecurityConfigUserChangeInfo.
        :type user_home_dir: str
        """
        self._user_home_dir = user_home_dir

    @property
    def shell(self):
        r"""Gets the shell of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户启动shell **取值范围**： 不涉及 

        :return: The shell of this SecurityConfigUserChangeInfo.
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        r"""Sets the shell of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户启动shell **取值范围**： 不涉及 

        :param shell: The shell of this SecurityConfigUserChangeInfo.
        :type shell: str
        """
        self._shell = shell

    @property
    def user_name(self):
        r"""Gets the user_name of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户名 **取值范围**： 不涉及 

        :return: The user_name of this SecurityConfigUserChangeInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SecurityConfigUserChangeInfo.

        **参数解释**： 用户名 **取值范围**： 不涉及 

        :param user_name: The user_name of this SecurityConfigUserChangeInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def scan_time(self):
        r"""Gets the scan_time of this SecurityConfigUserChangeInfo.

        **参数解释**： 最新扫描时间，采用时间戳，默认毫秒 **取值范围**： 不涉及 

        :return: The scan_time of this SecurityConfigUserChangeInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this SecurityConfigUserChangeInfo.

        **参数解释**： 最新扫描时间，采用时间戳，默认毫秒 **取值范围**： 不涉及 

        :param scan_time: The scan_time of this SecurityConfigUserChangeInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

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
        if not isinstance(other, SecurityConfigUserChangeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
