# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOauth2UserInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant': 'str',
        'name': 'str',
        'mobile': 'str',
        'user_name': 'str',
        'user_id': 'str',
        'email': 'str',
        'role': 'str'
    }

    attribute_map = {
        'tenant': 'tenant',
        'name': 'name',
        'mobile': 'mobile',
        'user_name': 'user_name',
        'user_id': 'user_id',
        'email': 'email',
        'role': 'role'
    }

    def __init__(self, tenant=None, name=None, mobile=None, user_name=None, user_id=None, email=None, role=None):
        r"""ShowOauth2UserInfoResponse

        The model defined in huaweicloud sdk

        :param tenant: 租户code，这里即企业code
        :type tenant: str
        :param name: 用户显示名
        :type name: str
        :param mobile: 手机号
        :type mobile: str
        :param user_name: 用户登录账号
        :type user_name: str
        :param user_id: 用户外部id
        :type user_id: str
        :param email: 邮箱
        :type email: str
        :param role: 角色，枚举：user或者admin
        :type role: str
        """
        
        super(ShowOauth2UserInfoResponse, self).__init__()

        self._tenant = None
        self._name = None
        self._mobile = None
        self._user_name = None
        self._user_id = None
        self._email = None
        self._role = None
        self.discriminator = None

        if tenant is not None:
            self.tenant = tenant
        if name is not None:
            self.name = name
        if mobile is not None:
            self.mobile = mobile
        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id
        if email is not None:
            self.email = email
        if role is not None:
            self.role = role

    @property
    def tenant(self):
        r"""Gets the tenant of this ShowOauth2UserInfoResponse.

        租户code，这里即企业code

        :return: The tenant of this ShowOauth2UserInfoResponse.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this ShowOauth2UserInfoResponse.

        租户code，这里即企业code

        :param tenant: The tenant of this ShowOauth2UserInfoResponse.
        :type tenant: str
        """
        self._tenant = tenant

    @property
    def name(self):
        r"""Gets the name of this ShowOauth2UserInfoResponse.

        用户显示名

        :return: The name of this ShowOauth2UserInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOauth2UserInfoResponse.

        用户显示名

        :param name: The name of this ShowOauth2UserInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def mobile(self):
        r"""Gets the mobile of this ShowOauth2UserInfoResponse.

        手机号

        :return: The mobile of this ShowOauth2UserInfoResponse.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        r"""Sets the mobile of this ShowOauth2UserInfoResponse.

        手机号

        :param mobile: The mobile of this ShowOauth2UserInfoResponse.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowOauth2UserInfoResponse.

        用户登录账号

        :return: The user_name of this ShowOauth2UserInfoResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowOauth2UserInfoResponse.

        用户登录账号

        :param user_name: The user_name of this ShowOauth2UserInfoResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowOauth2UserInfoResponse.

        用户外部id

        :return: The user_id of this ShowOauth2UserInfoResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowOauth2UserInfoResponse.

        用户外部id

        :param user_id: The user_id of this ShowOauth2UserInfoResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def email(self):
        r"""Gets the email of this ShowOauth2UserInfoResponse.

        邮箱

        :return: The email of this ShowOauth2UserInfoResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ShowOauth2UserInfoResponse.

        邮箱

        :param email: The email of this ShowOauth2UserInfoResponse.
        :type email: str
        """
        self._email = email

    @property
    def role(self):
        r"""Gets the role of this ShowOauth2UserInfoResponse.

        角色，枚举：user或者admin

        :return: The role of this ShowOauth2UserInfoResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ShowOauth2UserInfoResponse.

        角色，枚举：user或者admin

        :param role: The role of this ShowOauth2UserInfoResponse.
        :type role: str
        """
        self._role = role

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
        if not isinstance(other, ShowOauth2UserInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
