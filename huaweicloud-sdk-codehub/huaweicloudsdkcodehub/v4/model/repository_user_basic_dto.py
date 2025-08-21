# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryUserBasicDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'username': 'str',
        'state': 'str',
        'service_license_status': 'int',
        'name_cn': 'str',
        'nick_name': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'username': 'username',
        'state': 'state',
        'service_license_status': 'service_license_status',
        'name_cn': 'name_cn',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, id=None, name=None, username=None, state=None, service_license_status=None, name_cn=None, nick_name=None, tenant_name=None):
        r"""RepositoryUserBasicDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  用户id **约束限制：** 不涉及。
        :type id: int
        :param name: **参数解释：**  用户名称 **约束限制：** 不涉及。
        :type name: str
        :param username: **参数解释：**  用户名 **约束限制：** 不涉及。
        :type username: str
        :param state: **参数解释：**  用户状态 **约束限制：** 不涉及。
        :type state: str
        :param service_license_status: **参数解释：**  服务级权限状态 0：停用 1：启用 **约束限制：** 不涉及。
        :type service_license_status: int
        :param name_cn: **参数解释：**  用户中文名称 **约束限制：** 不涉及。
        :type name_cn: str
        :param nick_name: **参数解释：**  用户昵称 **约束限制：** 不涉及。
        :type nick_name: str
        :param tenant_name: **参数解释：**  租户名称 **约束限制：** 不涉及。
        :type tenant_name: str
        """
        
        

        self._id = None
        self._name = None
        self._username = None
        self._state = None
        self._service_license_status = None
        self._name_cn = None
        self._nick_name = None
        self._tenant_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if state is not None:
            self.state = state
        if service_license_status is not None:
            self.service_license_status = service_license_status
        if name_cn is not None:
            self.name_cn = name_cn
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def id(self):
        r"""Gets the id of this RepositoryUserBasicDto.

        **参数解释：**  用户id **约束限制：** 不涉及。

        :return: The id of this RepositoryUserBasicDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepositoryUserBasicDto.

        **参数解释：**  用户id **约束限制：** 不涉及。

        :param id: The id of this RepositoryUserBasicDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RepositoryUserBasicDto.

        **参数解释：**  用户名称 **约束限制：** 不涉及。

        :return: The name of this RepositoryUserBasicDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryUserBasicDto.

        **参数解释：**  用户名称 **约束限制：** 不涉及。

        :param name: The name of this RepositoryUserBasicDto.
        :type name: str
        """
        self._name = name

    @property
    def username(self):
        r"""Gets the username of this RepositoryUserBasicDto.

        **参数解释：**  用户名 **约束限制：** 不涉及。

        :return: The username of this RepositoryUserBasicDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RepositoryUserBasicDto.

        **参数解释：**  用户名 **约束限制：** 不涉及。

        :param username: The username of this RepositoryUserBasicDto.
        :type username: str
        """
        self._username = username

    @property
    def state(self):
        r"""Gets the state of this RepositoryUserBasicDto.

        **参数解释：**  用户状态 **约束限制：** 不涉及。

        :return: The state of this RepositoryUserBasicDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this RepositoryUserBasicDto.

        **参数解释：**  用户状态 **约束限制：** 不涉及。

        :param state: The state of this RepositoryUserBasicDto.
        :type state: str
        """
        self._state = state

    @property
    def service_license_status(self):
        r"""Gets the service_license_status of this RepositoryUserBasicDto.

        **参数解释：**  服务级权限状态 0：停用 1：启用 **约束限制：** 不涉及。

        :return: The service_license_status of this RepositoryUserBasicDto.
        :rtype: int
        """
        return self._service_license_status

    @service_license_status.setter
    def service_license_status(self, service_license_status):
        r"""Sets the service_license_status of this RepositoryUserBasicDto.

        **参数解释：**  服务级权限状态 0：停用 1：启用 **约束限制：** 不涉及。

        :param service_license_status: The service_license_status of this RepositoryUserBasicDto.
        :type service_license_status: int
        """
        self._service_license_status = service_license_status

    @property
    def name_cn(self):
        r"""Gets the name_cn of this RepositoryUserBasicDto.

        **参数解释：**  用户中文名称 **约束限制：** 不涉及。

        :return: The name_cn of this RepositoryUserBasicDto.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this RepositoryUserBasicDto.

        **参数解释：**  用户中文名称 **约束限制：** 不涉及。

        :param name_cn: The name_cn of this RepositoryUserBasicDto.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def nick_name(self):
        r"""Gets the nick_name of this RepositoryUserBasicDto.

        **参数解释：**  用户昵称 **约束限制：** 不涉及。

        :return: The nick_name of this RepositoryUserBasicDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this RepositoryUserBasicDto.

        **参数解释：**  用户昵称 **约束限制：** 不涉及。

        :param nick_name: The nick_name of this RepositoryUserBasicDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this RepositoryUserBasicDto.

        **参数解释：**  租户名称 **约束限制：** 不涉及。

        :return: The tenant_name of this RepositoryUserBasicDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this RepositoryUserBasicDto.

        **参数解释：**  租户名称 **约束限制：** 不涉及。

        :param tenant_name: The tenant_name of this RepositoryUserBasicDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

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
        if not isinstance(other, RepositoryUserBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
