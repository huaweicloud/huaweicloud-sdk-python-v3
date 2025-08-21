# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantedUsersDto:

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
        'name_cn': 'str',
        'username': 'str',
        'nick_name': 'str',
        'tenant_name': 'str',
        'email': 'str',
        'iam_id': 'str',
        'service_license_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'name_cn': 'name_cn',
        'username': 'username',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'email': 'email',
        'iam_id': 'iam_id',
        'service_license_status': 'service_license_status'
    }

    def __init__(self, id=None, name=None, name_cn=None, username=None, nick_name=None, tenant_name=None, email=None, iam_id=None, service_license_status=None):
        r"""GrantedUsersDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 用户id。
        :type id: int
        :param name: **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param name_cn: **参数解释：** 用户中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name_cn: str
        :param username: **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type username: str
        :param nick_name: **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type tenant_name: str
        :param email: **参数解释：** 用户邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type email: str
        :param iam_id: **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type iam_id: str
        :param service_license_status: **参数解释：** license的状态。
        :type service_license_status: int
        """
        
        

        self._id = None
        self._name = None
        self._name_cn = None
        self._username = None
        self._nick_name = None
        self._tenant_name = None
        self._email = None
        self._iam_id = None
        self._service_license_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if name_cn is not None:
            self.name_cn = name_cn
        if username is not None:
            self.username = username
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if email is not None:
            self.email = email
        if iam_id is not None:
            self.iam_id = iam_id
        if service_license_status is not None:
            self.service_license_status = service_license_status

    @property
    def id(self):
        r"""Gets the id of this GrantedUsersDto.

        **参数解释：** 用户id。

        :return: The id of this GrantedUsersDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GrantedUsersDto.

        **参数解释：** 用户id。

        :param id: The id of this GrantedUsersDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GrantedUsersDto.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this GrantedUsersDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GrantedUsersDto.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this GrantedUsersDto.
        :type name: str
        """
        self._name = name

    @property
    def name_cn(self):
        r"""Gets the name_cn of this GrantedUsersDto.

        **参数解释：** 用户中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name_cn of this GrantedUsersDto.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this GrantedUsersDto.

        **参数解释：** 用户中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name_cn: The name_cn of this GrantedUsersDto.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def username(self):
        r"""Gets the username of this GrantedUsersDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The username of this GrantedUsersDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this GrantedUsersDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param username: The username of this GrantedUsersDto.
        :type username: str
        """
        self._username = username

    @property
    def nick_name(self):
        r"""Gets the nick_name of this GrantedUsersDto.

        **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The nick_name of this GrantedUsersDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this GrantedUsersDto.

        **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param nick_name: The nick_name of this GrantedUsersDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this GrantedUsersDto.

        **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The tenant_name of this GrantedUsersDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this GrantedUsersDto.

        **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param tenant_name: The tenant_name of this GrantedUsersDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def email(self):
        r"""Gets the email of this GrantedUsersDto.

        **参数解释：** 用户邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The email of this GrantedUsersDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this GrantedUsersDto.

        **参数解释：** 用户邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param email: The email of this GrantedUsersDto.
        :type email: str
        """
        self._email = email

    @property
    def iam_id(self):
        r"""Gets the iam_id of this GrantedUsersDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The iam_id of this GrantedUsersDto.
        :rtype: str
        """
        return self._iam_id

    @iam_id.setter
    def iam_id(self, iam_id):
        r"""Sets the iam_id of this GrantedUsersDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param iam_id: The iam_id of this GrantedUsersDto.
        :type iam_id: str
        """
        self._iam_id = iam_id

    @property
    def service_license_status(self):
        r"""Gets the service_license_status of this GrantedUsersDto.

        **参数解释：** license的状态。

        :return: The service_license_status of this GrantedUsersDto.
        :rtype: int
        """
        return self._service_license_status

    @service_license_status.setter
    def service_license_status(self, service_license_status):
        r"""Sets the service_license_status of this GrantedUsersDto.

        **参数解释：** license的状态。

        :param service_license_status: The service_license_status of this GrantedUsersDto.
        :type service_license_status: int
        """
        self._service_license_status = service_license_status

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
        if not isinstance(other, GrantedUsersDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
