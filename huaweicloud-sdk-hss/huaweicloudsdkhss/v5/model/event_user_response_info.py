# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventUserResponseInfo:

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
        'login_fail_count': 'int',
        'pwd_hash': 'str',
        'pwd_with_fuzzing': 'str',
        'pwd_used_days': 'int',
        'pwd_min_days': 'int',
        'pwd_max_days': 'int',
        'pwd_warn_left_days': 'int'
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
        'login_fail_count': 'login_fail_count',
        'pwd_hash': 'pwd_hash',
        'pwd_with_fuzzing': 'pwd_with_fuzzing',
        'pwd_used_days': 'pwd_used_days',
        'pwd_min_days': 'pwd_min_days',
        'pwd_max_days': 'pwd_max_days',
        'pwd_warn_left_days': 'pwd_warn_left_days'
    }

    def __init__(self, user_id=None, user_gid=None, user_name=None, user_group_name=None, user_home_dir=None, login_ip=None, service_type=None, service_port=None, login_mode=None, login_last_time=None, login_fail_count=None, pwd_hash=None, pwd_with_fuzzing=None, pwd_used_days=None, pwd_min_days=None, pwd_max_days=None, pwd_warn_left_days=None):
        """EventUserResponseInfo

        The model defined in huaweicloud sdk

        :param user_id: 用户uid
        :type user_id: int
        :param user_gid: 用户gid
        :type user_gid: int
        :param user_name: 用户名称
        :type user_name: str
        :param user_group_name: 用户组名称
        :type user_group_name: str
        :param user_home_dir: 用户home目录
        :type user_home_dir: str
        :param login_ip: 用户登录ip
        :type login_ip: str
        :param service_type: 登录的服务类型
        :type service_type: str
        :param service_port: 登录服务端口
        :type service_port: int
        :param login_mode: 登录方式
        :type login_mode: int
        :param login_last_time: 用户最后一次登录时间
        :type login_last_time: int
        :param login_fail_count: 用户登录失败次数
        :type login_fail_count: int
        :param pwd_hash: 口令hash
        :type pwd_hash: str
        :param pwd_with_fuzzing: 匿名化处理后的口令
        :type pwd_with_fuzzing: str
        :param pwd_used_days: 密码使用的天数
        :type pwd_used_days: int
        :param pwd_min_days: 口令的最短有效期限
        :type pwd_min_days: int
        :param pwd_max_days: 口令的最长有效期限
        :type pwd_max_days: int
        :param pwd_warn_left_days: 口令无效时提前告警天数
        :type pwd_warn_left_days: int
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
        self._pwd_hash = None
        self._pwd_with_fuzzing = None
        self._pwd_used_days = None
        self._pwd_min_days = None
        self._pwd_max_days = None
        self._pwd_warn_left_days = None
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
        if pwd_hash is not None:
            self.pwd_hash = pwd_hash
        if pwd_with_fuzzing is not None:
            self.pwd_with_fuzzing = pwd_with_fuzzing
        if pwd_used_days is not None:
            self.pwd_used_days = pwd_used_days
        if pwd_min_days is not None:
            self.pwd_min_days = pwd_min_days
        if pwd_max_days is not None:
            self.pwd_max_days = pwd_max_days
        if pwd_warn_left_days is not None:
            self.pwd_warn_left_days = pwd_warn_left_days

    @property
    def user_id(self):
        """Gets the user_id of this EventUserResponseInfo.

        用户uid

        :return: The user_id of this EventUserResponseInfo.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this EventUserResponseInfo.

        用户uid

        :param user_id: The user_id of this EventUserResponseInfo.
        :type user_id: int
        """
        self._user_id = user_id

    @property
    def user_gid(self):
        """Gets the user_gid of this EventUserResponseInfo.

        用户gid

        :return: The user_gid of this EventUserResponseInfo.
        :rtype: int
        """
        return self._user_gid

    @user_gid.setter
    def user_gid(self, user_gid):
        """Sets the user_gid of this EventUserResponseInfo.

        用户gid

        :param user_gid: The user_gid of this EventUserResponseInfo.
        :type user_gid: int
        """
        self._user_gid = user_gid

    @property
    def user_name(self):
        """Gets the user_name of this EventUserResponseInfo.

        用户名称

        :return: The user_name of this EventUserResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this EventUserResponseInfo.

        用户名称

        :param user_name: The user_name of this EventUserResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_group_name(self):
        """Gets the user_group_name of this EventUserResponseInfo.

        用户组名称

        :return: The user_group_name of this EventUserResponseInfo.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this EventUserResponseInfo.

        用户组名称

        :param user_group_name: The user_group_name of this EventUserResponseInfo.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def user_home_dir(self):
        """Gets the user_home_dir of this EventUserResponseInfo.

        用户home目录

        :return: The user_home_dir of this EventUserResponseInfo.
        :rtype: str
        """
        return self._user_home_dir

    @user_home_dir.setter
    def user_home_dir(self, user_home_dir):
        """Sets the user_home_dir of this EventUserResponseInfo.

        用户home目录

        :param user_home_dir: The user_home_dir of this EventUserResponseInfo.
        :type user_home_dir: str
        """
        self._user_home_dir = user_home_dir

    @property
    def login_ip(self):
        """Gets the login_ip of this EventUserResponseInfo.

        用户登录ip

        :return: The login_ip of this EventUserResponseInfo.
        :rtype: str
        """
        return self._login_ip

    @login_ip.setter
    def login_ip(self, login_ip):
        """Sets the login_ip of this EventUserResponseInfo.

        用户登录ip

        :param login_ip: The login_ip of this EventUserResponseInfo.
        :type login_ip: str
        """
        self._login_ip = login_ip

    @property
    def service_type(self):
        """Gets the service_type of this EventUserResponseInfo.

        登录的服务类型

        :return: The service_type of this EventUserResponseInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this EventUserResponseInfo.

        登录的服务类型

        :param service_type: The service_type of this EventUserResponseInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def service_port(self):
        """Gets the service_port of this EventUserResponseInfo.

        登录服务端口

        :return: The service_port of this EventUserResponseInfo.
        :rtype: int
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        """Sets the service_port of this EventUserResponseInfo.

        登录服务端口

        :param service_port: The service_port of this EventUserResponseInfo.
        :type service_port: int
        """
        self._service_port = service_port

    @property
    def login_mode(self):
        """Gets the login_mode of this EventUserResponseInfo.

        登录方式

        :return: The login_mode of this EventUserResponseInfo.
        :rtype: int
        """
        return self._login_mode

    @login_mode.setter
    def login_mode(self, login_mode):
        """Sets the login_mode of this EventUserResponseInfo.

        登录方式

        :param login_mode: The login_mode of this EventUserResponseInfo.
        :type login_mode: int
        """
        self._login_mode = login_mode

    @property
    def login_last_time(self):
        """Gets the login_last_time of this EventUserResponseInfo.

        用户最后一次登录时间

        :return: The login_last_time of this EventUserResponseInfo.
        :rtype: int
        """
        return self._login_last_time

    @login_last_time.setter
    def login_last_time(self, login_last_time):
        """Sets the login_last_time of this EventUserResponseInfo.

        用户最后一次登录时间

        :param login_last_time: The login_last_time of this EventUserResponseInfo.
        :type login_last_time: int
        """
        self._login_last_time = login_last_time

    @property
    def login_fail_count(self):
        """Gets the login_fail_count of this EventUserResponseInfo.

        用户登录失败次数

        :return: The login_fail_count of this EventUserResponseInfo.
        :rtype: int
        """
        return self._login_fail_count

    @login_fail_count.setter
    def login_fail_count(self, login_fail_count):
        """Sets the login_fail_count of this EventUserResponseInfo.

        用户登录失败次数

        :param login_fail_count: The login_fail_count of this EventUserResponseInfo.
        :type login_fail_count: int
        """
        self._login_fail_count = login_fail_count

    @property
    def pwd_hash(self):
        """Gets the pwd_hash of this EventUserResponseInfo.

        口令hash

        :return: The pwd_hash of this EventUserResponseInfo.
        :rtype: str
        """
        return self._pwd_hash

    @pwd_hash.setter
    def pwd_hash(self, pwd_hash):
        """Sets the pwd_hash of this EventUserResponseInfo.

        口令hash

        :param pwd_hash: The pwd_hash of this EventUserResponseInfo.
        :type pwd_hash: str
        """
        self._pwd_hash = pwd_hash

    @property
    def pwd_with_fuzzing(self):
        """Gets the pwd_with_fuzzing of this EventUserResponseInfo.

        匿名化处理后的口令

        :return: The pwd_with_fuzzing of this EventUserResponseInfo.
        :rtype: str
        """
        return self._pwd_with_fuzzing

    @pwd_with_fuzzing.setter
    def pwd_with_fuzzing(self, pwd_with_fuzzing):
        """Sets the pwd_with_fuzzing of this EventUserResponseInfo.

        匿名化处理后的口令

        :param pwd_with_fuzzing: The pwd_with_fuzzing of this EventUserResponseInfo.
        :type pwd_with_fuzzing: str
        """
        self._pwd_with_fuzzing = pwd_with_fuzzing

    @property
    def pwd_used_days(self):
        """Gets the pwd_used_days of this EventUserResponseInfo.

        密码使用的天数

        :return: The pwd_used_days of this EventUserResponseInfo.
        :rtype: int
        """
        return self._pwd_used_days

    @pwd_used_days.setter
    def pwd_used_days(self, pwd_used_days):
        """Sets the pwd_used_days of this EventUserResponseInfo.

        密码使用的天数

        :param pwd_used_days: The pwd_used_days of this EventUserResponseInfo.
        :type pwd_used_days: int
        """
        self._pwd_used_days = pwd_used_days

    @property
    def pwd_min_days(self):
        """Gets the pwd_min_days of this EventUserResponseInfo.

        口令的最短有效期限

        :return: The pwd_min_days of this EventUserResponseInfo.
        :rtype: int
        """
        return self._pwd_min_days

    @pwd_min_days.setter
    def pwd_min_days(self, pwd_min_days):
        """Sets the pwd_min_days of this EventUserResponseInfo.

        口令的最短有效期限

        :param pwd_min_days: The pwd_min_days of this EventUserResponseInfo.
        :type pwd_min_days: int
        """
        self._pwd_min_days = pwd_min_days

    @property
    def pwd_max_days(self):
        """Gets the pwd_max_days of this EventUserResponseInfo.

        口令的最长有效期限

        :return: The pwd_max_days of this EventUserResponseInfo.
        :rtype: int
        """
        return self._pwd_max_days

    @pwd_max_days.setter
    def pwd_max_days(self, pwd_max_days):
        """Sets the pwd_max_days of this EventUserResponseInfo.

        口令的最长有效期限

        :param pwd_max_days: The pwd_max_days of this EventUserResponseInfo.
        :type pwd_max_days: int
        """
        self._pwd_max_days = pwd_max_days

    @property
    def pwd_warn_left_days(self):
        """Gets the pwd_warn_left_days of this EventUserResponseInfo.

        口令无效时提前告警天数

        :return: The pwd_warn_left_days of this EventUserResponseInfo.
        :rtype: int
        """
        return self._pwd_warn_left_days

    @pwd_warn_left_days.setter
    def pwd_warn_left_days(self, pwd_warn_left_days):
        """Sets the pwd_warn_left_days of this EventUserResponseInfo.

        口令无效时提前告警天数

        :param pwd_warn_left_days: The pwd_warn_left_days of this EventUserResponseInfo.
        :type pwd_warn_left_days: int
        """
        self._pwd_warn_left_days = pwd_warn_left_days

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
        if not isinstance(other, EventUserResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
