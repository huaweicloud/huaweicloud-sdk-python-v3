# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpnUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('password')

    openapi_types = {
        'name': 'str',
        'password': 'str',
        'description': 'str',
        'user_group_name': 'str',
        'static_ip': 'str'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'description': 'description',
        'user_group_name': 'user_group_name',
        'static_ip': 'static_ip'
    }

    def __init__(self, name=None, password=None, description=None, user_group_name=None, static_ip=None):
        r"""CreateVpnUser

        The model defined in huaweicloud sdk

        :param name: 用户名
        :type name: str
        :param password: 用户密码
        :type password: str
        :param description: 用户描述，0-64字符，中文、英文、数字包含下划线
        :type description: str
        :param user_group_name: 所属用户组名称
        :type user_group_name: str
        :param static_ip: 静态客户端IP地址，默认值disable，表示随机分配客户端IP
        :type static_ip: str
        """
        
        

        self._name = None
        self._password = None
        self._description = None
        self._user_group_name = None
        self._static_ip = None
        self.discriminator = None

        self.name = name
        self.password = password
        if description is not None:
            self.description = description
        if user_group_name is not None:
            self.user_group_name = user_group_name
        if static_ip is not None:
            self.static_ip = static_ip

    @property
    def name(self):
        r"""Gets the name of this CreateVpnUser.

        用户名

        :return: The name of this CreateVpnUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateVpnUser.

        用户名

        :param name: The name of this CreateVpnUser.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        r"""Gets the password of this CreateVpnUser.

        用户密码

        :return: The password of this CreateVpnUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateVpnUser.

        用户密码

        :param password: The password of this CreateVpnUser.
        :type password: str
        """
        self._password = password

    @property
    def description(self):
        r"""Gets the description of this CreateVpnUser.

        用户描述，0-64字符，中文、英文、数字包含下划线

        :return: The description of this CreateVpnUser.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateVpnUser.

        用户描述，0-64字符，中文、英文、数字包含下划线

        :param description: The description of this CreateVpnUser.
        :type description: str
        """
        self._description = description

    @property
    def user_group_name(self):
        r"""Gets the user_group_name of this CreateVpnUser.

        所属用户组名称

        :return: The user_group_name of this CreateVpnUser.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        r"""Sets the user_group_name of this CreateVpnUser.

        所属用户组名称

        :param user_group_name: The user_group_name of this CreateVpnUser.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def static_ip(self):
        r"""Gets the static_ip of this CreateVpnUser.

        静态客户端IP地址，默认值disable，表示随机分配客户端IP

        :return: The static_ip of this CreateVpnUser.
        :rtype: str
        """
        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        r"""Sets the static_ip of this CreateVpnUser.

        静态客户端IP地址，默认值disable，表示随机分配客户端IP

        :param static_ip: The static_ip of this CreateVpnUser.
        :type static_ip: str
        """
        self._static_ip = static_ip

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
        if not isinstance(other, CreateVpnUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
