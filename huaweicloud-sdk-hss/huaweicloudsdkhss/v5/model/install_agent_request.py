# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstallAgentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('root_password')
    sensitive_list.append('login_password')

    openapi_types = {
        'enterprise_project_id': 'str',
        'root_permission': 'str',
        'root_password': 'str',
        'login_user': 'str',
        'login_password': 'str',
        'login_port': 'int',
        'host_id_list': 'str',
        'file': 'list[MultipartFile]',
        'login_type': 'str',
        'host_group_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'root_permission': 'root_permission',
        'root_password': 'root_password',
        'login_user': 'login_user',
        'login_password': 'login_password',
        'login_port': 'login_port',
        'host_id_list': 'host_id_list',
        'file': 'file',
        'login_type': 'login_type',
        'host_group_id': 'host_group_id'
    }

    def __init__(self, enterprise_project_id=None, root_permission=None, root_password=None, login_user=None, login_password=None, login_port=None, host_id_list=None, file=None, login_type=None, host_group_id=None):
        r"""InstallAgentRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param root_permission: **参数解释**: 是否允许root直连 **约束限制**: 不涉及 **取值范围**: - true：允许 - false：不允许  **默认取值**: 不涉及
        :type root_permission: str
        :param root_password: **参数解释**: root密码 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及
        :type root_password: str
        :param login_user: **参数解释**: 登录用户 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及
        :type login_user: str
        :param login_password: **参数解释**: 登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及
        :type login_password: str
        :param login_port: **参数解释**: 登录端口 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及
        :type login_port: int
        :param host_id_list: **参数解释**: 服务器id列表,有多个hostId的时使用逗号拼接 **约束限制**: 不涉及 **取值范围**: 字符长度0-3200 **默认取值**: 不涉及
        :type host_id_list: str
        :param file: 密码或者密钥模板文件
        :type file: list[:class:`huaweicloudsdkhss.v5.MultipartFile`]
        :param login_type: **参数解释**: 登录类型 **约束限制**: 不涉及 **取值范围**: - single_password - single_sshKey - dew - ssh_key - password  **默认取值**: 不涉及
        :type login_type: str
        :param host_group_id: **参数解释**: 服务器组id **约束限制**: 不涉及 **取值范围**: 字符长度0-128 **默认取值**: 不涉及
        :type host_group_id: str
        """
        
        

        self._enterprise_project_id = None
        self._root_permission = None
        self._root_password = None
        self._login_user = None
        self._login_password = None
        self._login_port = None
        self._host_id_list = None
        self._file = None
        self._login_type = None
        self._host_group_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if root_permission is not None:
            self.root_permission = root_permission
        if root_password is not None:
            self.root_password = root_password
        if login_user is not None:
            self.login_user = login_user
        if login_password is not None:
            self.login_password = login_password
        if login_port is not None:
            self.login_port = login_port
        self.host_id_list = host_id_list
        if file is not None:
            self.file = file
        self.login_type = login_type
        if host_group_id is not None:
            self.host_group_id = host_group_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InstallAgentRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this InstallAgentRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InstallAgentRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this InstallAgentRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def root_permission(self):
        r"""Gets the root_permission of this InstallAgentRequest.

        **参数解释**: 是否允许root直连 **约束限制**: 不涉及 **取值范围**: - true：允许 - false：不允许  **默认取值**: 不涉及

        :return: The root_permission of this InstallAgentRequest.
        :rtype: str
        """
        return self._root_permission

    @root_permission.setter
    def root_permission(self, root_permission):
        r"""Sets the root_permission of this InstallAgentRequest.

        **参数解释**: 是否允许root直连 **约束限制**: 不涉及 **取值范围**: - true：允许 - false：不允许  **默认取值**: 不涉及

        :param root_permission: The root_permission of this InstallAgentRequest.
        :type root_permission: str
        """
        self._root_permission = root_permission

    @property
    def root_password(self):
        r"""Gets the root_password of this InstallAgentRequest.

        **参数解释**: root密码 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :return: The root_password of this InstallAgentRequest.
        :rtype: str
        """
        return self._root_password

    @root_password.setter
    def root_password(self, root_password):
        r"""Sets the root_password of this InstallAgentRequest.

        **参数解释**: root密码 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :param root_password: The root_password of this InstallAgentRequest.
        :type root_password: str
        """
        self._root_password = root_password

    @property
    def login_user(self):
        r"""Gets the login_user of this InstallAgentRequest.

        **参数解释**: 登录用户 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :return: The login_user of this InstallAgentRequest.
        :rtype: str
        """
        return self._login_user

    @login_user.setter
    def login_user(self, login_user):
        r"""Sets the login_user of this InstallAgentRequest.

        **参数解释**: 登录用户 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :param login_user: The login_user of this InstallAgentRequest.
        :type login_user: str
        """
        self._login_user = login_user

    @property
    def login_password(self):
        r"""Gets the login_password of this InstallAgentRequest.

        **参数解释**: 登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :return: The login_password of this InstallAgentRequest.
        :rtype: str
        """
        return self._login_password

    @login_password.setter
    def login_password(self, login_password):
        r"""Sets the login_password of this InstallAgentRequest.

        **参数解释**: 登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :param login_password: The login_password of this InstallAgentRequest.
        :type login_password: str
        """
        self._login_password = login_password

    @property
    def login_port(self):
        r"""Gets the login_port of this InstallAgentRequest.

        **参数解释**: 登录端口 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :return: The login_port of this InstallAgentRequest.
        :rtype: int
        """
        return self._login_port

    @login_port.setter
    def login_port(self, login_port):
        r"""Sets the login_port of this InstallAgentRequest.

        **参数解释**: 登录端口 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及

        :param login_port: The login_port of this InstallAgentRequest.
        :type login_port: int
        """
        self._login_port = login_port

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this InstallAgentRequest.

        **参数解释**: 服务器id列表,有多个hostId的时使用逗号拼接 **约束限制**: 不涉及 **取值范围**: 字符长度0-3200 **默认取值**: 不涉及

        :return: The host_id_list of this InstallAgentRequest.
        :rtype: str
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this InstallAgentRequest.

        **参数解释**: 服务器id列表,有多个hostId的时使用逗号拼接 **约束限制**: 不涉及 **取值范围**: 字符长度0-3200 **默认取值**: 不涉及

        :param host_id_list: The host_id_list of this InstallAgentRequest.
        :type host_id_list: str
        """
        self._host_id_list = host_id_list

    @property
    def file(self):
        r"""Gets the file of this InstallAgentRequest.

        密码或者密钥模板文件

        :return: The file of this InstallAgentRequest.
        :rtype: list[:class:`huaweicloudsdkhss.v5.MultipartFile`]
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this InstallAgentRequest.

        密码或者密钥模板文件

        :param file: The file of this InstallAgentRequest.
        :type file: list[:class:`huaweicloudsdkhss.v5.MultipartFile`]
        """
        self._file = file

    @property
    def login_type(self):
        r"""Gets the login_type of this InstallAgentRequest.

        **参数解释**: 登录类型 **约束限制**: 不涉及 **取值范围**: - single_password - single_sshKey - dew - ssh_key - password  **默认取值**: 不涉及

        :return: The login_type of this InstallAgentRequest.
        :rtype: str
        """
        return self._login_type

    @login_type.setter
    def login_type(self, login_type):
        r"""Sets the login_type of this InstallAgentRequest.

        **参数解释**: 登录类型 **约束限制**: 不涉及 **取值范围**: - single_password - single_sshKey - dew - ssh_key - password  **默认取值**: 不涉及

        :param login_type: The login_type of this InstallAgentRequest.
        :type login_type: str
        """
        self._login_type = login_type

    @property
    def host_group_id(self):
        r"""Gets the host_group_id of this InstallAgentRequest.

        **参数解释**: 服务器组id **约束限制**: 不涉及 **取值范围**: 字符长度0-128 **默认取值**: 不涉及

        :return: The host_group_id of this InstallAgentRequest.
        :rtype: str
        """
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        r"""Sets the host_group_id of this InstallAgentRequest.

        **参数解释**: 服务器组id **约束限制**: 不涉及 **取值范围**: 字符长度0-128 **默认取值**: 不涉及

        :param host_group_id: The host_group_id of this InstallAgentRequest.
        :type host_group_id: str
        """
        self._host_group_id = host_group_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstallAgentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
