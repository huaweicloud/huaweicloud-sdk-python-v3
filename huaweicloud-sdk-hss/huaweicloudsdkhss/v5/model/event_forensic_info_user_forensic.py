# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoUserForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'int',
        'user_gid': 'int',
        'user_name': 'str',
        'user_group_name': 'str',
        'user_home_dir': 'str',
        'login_ip': 'str',
        'service_type': 'str',
        'service_port': 'int',
        'login_mode': 'int',
        'login_last_time': 'int',
        'login_fail_count': 'int'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_gid': 'user_gid',
        'user_name': 'user_name',
        'user_group_name': 'user_group_name',
        'user_home_dir': 'user_home_dir',
        'login_ip': 'login_ip',
        'service_type': 'service_type',
        'service_port': 'service_port',
        'login_mode': 'login_mode',
        'login_last_time': 'login_last_time',
        'login_fail_count': 'login_fail_count'
    }

    def __init__(self, user_id=None, user_gid=None, user_name=None, user_group_name=None, user_home_dir=None, login_ip=None, service_type=None, service_port=None, login_mode=None, login_last_time=None, login_fail_count=None):
        r"""EventForensicInfoUserForensic

        The model defined in huaweicloud sdk

        :param user_id: **参数解释**： 用户uid **取值范围**： 不涉及
        :type user_id: int
        :param user_gid: **参数解释**： 用户gid **取值范围**： 不涉及
        :type user_gid: int
        :param user_name: **参数解释**： 用户名称 **取值范围**： 不涉及
        :type user_name: str
        :param user_group_name: **参数解释**： 用户组名称 **取值范围**： 不涉及
        :type user_group_name: str
        :param user_home_dir: **参数解释**： 用户home目录 **取值范围**： 不涉及
        :type user_home_dir: str
        :param login_ip: **参数解释**： 用户登录ip **取值范围**： 不涉及
        :type login_ip: str
        :param service_type: **参数解释**： 登录的服务类型 **取值范围**： 不涉及
        :type service_type: str
        :param service_port: **参数解释**： 登录服务端口 **取值范围**： 不涉及
        :type service_port: int
        :param login_mode: **参数解释**： 登录方式 **取值范围**： 不涉及
        :type login_mode: int
        :param login_last_time: **参数解释**： 用户最后一次登录时间 **取值范围**： 不涉及
        :type login_last_time: int
        :param login_fail_count: **参数解释**： 用户登录失败次数 **取值范围**： 不涉及
        :type login_fail_count: int
        """
        
        

        self._user_id = None
        self._user_gid = None
        self._user_name = None
        self._user_group_name = None
        self._user_home_dir = None
        self._login_ip = None
        self._service_type = None
        self._service_port = None
        self._login_mode = None
        self._login_last_time = None
        self._login_fail_count = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_gid is not None:
            self.user_gid = user_gid
        if user_name is not None:
            self.user_name = user_name
        if user_group_name is not None:
            self.user_group_name = user_group_name
        if user_home_dir is not None:
            self.user_home_dir = user_home_dir
        if login_ip is not None:
            self.login_ip = login_ip
        if service_type is not None:
            self.service_type = service_type
        if service_port is not None:
            self.service_port = service_port
        if login_mode is not None:
            self.login_mode = login_mode
        if login_last_time is not None:
            self.login_last_time = login_last_time
        if login_fail_count is not None:
            self.login_fail_count = login_fail_count

    @property
    def user_id(self):
        r"""Gets the user_id of this EventForensicInfoUserForensic.

        **参数解释**： 用户uid **取值范围**： 不涉及

        :return: The user_id of this EventForensicInfoUserForensic.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this EventForensicInfoUserForensic.

        **参数解释**： 用户uid **取值范围**： 不涉及

        :param user_id: The user_id of this EventForensicInfoUserForensic.
        :type user_id: int
        """
        self._user_id = user_id

    @property
    def user_gid(self):
        r"""Gets the user_gid of this EventForensicInfoUserForensic.

        **参数解释**： 用户gid **取值范围**： 不涉及

        :return: The user_gid of this EventForensicInfoUserForensic.
        :rtype: int
        """
        return self._user_gid

    @user_gid.setter
    def user_gid(self, user_gid):
        r"""Sets the user_gid of this EventForensicInfoUserForensic.

        **参数解释**： 用户gid **取值范围**： 不涉及

        :param user_gid: The user_gid of this EventForensicInfoUserForensic.
        :type user_gid: int
        """
        self._user_gid = user_gid

    @property
    def user_name(self):
        r"""Gets the user_name of this EventForensicInfoUserForensic.

        **参数解释**： 用户名称 **取值范围**： 不涉及

        :return: The user_name of this EventForensicInfoUserForensic.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this EventForensicInfoUserForensic.

        **参数解释**： 用户名称 **取值范围**： 不涉及

        :param user_name: The user_name of this EventForensicInfoUserForensic.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_group_name(self):
        r"""Gets the user_group_name of this EventForensicInfoUserForensic.

        **参数解释**： 用户组名称 **取值范围**： 不涉及

        :return: The user_group_name of this EventForensicInfoUserForensic.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        r"""Sets the user_group_name of this EventForensicInfoUserForensic.

        **参数解释**： 用户组名称 **取值范围**： 不涉及

        :param user_group_name: The user_group_name of this EventForensicInfoUserForensic.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def user_home_dir(self):
        r"""Gets the user_home_dir of this EventForensicInfoUserForensic.

        **参数解释**： 用户home目录 **取值范围**： 不涉及

        :return: The user_home_dir of this EventForensicInfoUserForensic.
        :rtype: str
        """
        return self._user_home_dir

    @user_home_dir.setter
    def user_home_dir(self, user_home_dir):
        r"""Sets the user_home_dir of this EventForensicInfoUserForensic.

        **参数解释**： 用户home目录 **取值范围**： 不涉及

        :param user_home_dir: The user_home_dir of this EventForensicInfoUserForensic.
        :type user_home_dir: str
        """
        self._user_home_dir = user_home_dir

    @property
    def login_ip(self):
        r"""Gets the login_ip of this EventForensicInfoUserForensic.

        **参数解释**： 用户登录ip **取值范围**： 不涉及

        :return: The login_ip of this EventForensicInfoUserForensic.
        :rtype: str
        """
        return self._login_ip

    @login_ip.setter
    def login_ip(self, login_ip):
        r"""Sets the login_ip of this EventForensicInfoUserForensic.

        **参数解释**： 用户登录ip **取值范围**： 不涉及

        :param login_ip: The login_ip of this EventForensicInfoUserForensic.
        :type login_ip: str
        """
        self._login_ip = login_ip

    @property
    def service_type(self):
        r"""Gets the service_type of this EventForensicInfoUserForensic.

        **参数解释**： 登录的服务类型 **取值范围**： 不涉及

        :return: The service_type of this EventForensicInfoUserForensic.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this EventForensicInfoUserForensic.

        **参数解释**： 登录的服务类型 **取值范围**： 不涉及

        :param service_type: The service_type of this EventForensicInfoUserForensic.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def service_port(self):
        r"""Gets the service_port of this EventForensicInfoUserForensic.

        **参数解释**： 登录服务端口 **取值范围**： 不涉及

        :return: The service_port of this EventForensicInfoUserForensic.
        :rtype: int
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        r"""Sets the service_port of this EventForensicInfoUserForensic.

        **参数解释**： 登录服务端口 **取值范围**： 不涉及

        :param service_port: The service_port of this EventForensicInfoUserForensic.
        :type service_port: int
        """
        self._service_port = service_port

    @property
    def login_mode(self):
        r"""Gets the login_mode of this EventForensicInfoUserForensic.

        **参数解释**： 登录方式 **取值范围**： 不涉及

        :return: The login_mode of this EventForensicInfoUserForensic.
        :rtype: int
        """
        return self._login_mode

    @login_mode.setter
    def login_mode(self, login_mode):
        r"""Sets the login_mode of this EventForensicInfoUserForensic.

        **参数解释**： 登录方式 **取值范围**： 不涉及

        :param login_mode: The login_mode of this EventForensicInfoUserForensic.
        :type login_mode: int
        """
        self._login_mode = login_mode

    @property
    def login_last_time(self):
        r"""Gets the login_last_time of this EventForensicInfoUserForensic.

        **参数解释**： 用户最后一次登录时间 **取值范围**： 不涉及

        :return: The login_last_time of this EventForensicInfoUserForensic.
        :rtype: int
        """
        return self._login_last_time

    @login_last_time.setter
    def login_last_time(self, login_last_time):
        r"""Sets the login_last_time of this EventForensicInfoUserForensic.

        **参数解释**： 用户最后一次登录时间 **取值范围**： 不涉及

        :param login_last_time: The login_last_time of this EventForensicInfoUserForensic.
        :type login_last_time: int
        """
        self._login_last_time = login_last_time

    @property
    def login_fail_count(self):
        r"""Gets the login_fail_count of this EventForensicInfoUserForensic.

        **参数解释**： 用户登录失败次数 **取值范围**： 不涉及

        :return: The login_fail_count of this EventForensicInfoUserForensic.
        :rtype: int
        """
        return self._login_fail_count

    @login_fail_count.setter
    def login_fail_count(self, login_fail_count):
        r"""Sets the login_fail_count of this EventForensicInfoUserForensic.

        **参数解释**： 用户登录失败次数 **取值范围**： 不涉及

        :param login_fail_count: The login_fail_count of this EventForensicInfoUserForensic.
        :type login_fail_count: int
        """
        self._login_fail_count = login_fail_count

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
        if not isinstance(other, EventForensicInfoUserForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
