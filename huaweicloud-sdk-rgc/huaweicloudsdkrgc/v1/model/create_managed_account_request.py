# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateManagedAccountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('account_name')
    sensitive_list.append('account_email')
    sensitive_list.append('phone')
    sensitive_list.append('identity_store_user_name')
    sensitive_list.append('identity_store_email')

    openapi_types = {
        'account_name': 'str',
        'account_email': 'str',
        'phone': 'str',
        'identity_store_user_name': 'str',
        'identity_store_email': 'str',
        'parent_organizational_unit_id': 'str',
        'parent_organizational_unit_name': 'str',
        'blueprint': 'Blueprint'
    }

    attribute_map = {
        'account_name': 'account_name',
        'account_email': 'account_email',
        'phone': 'phone',
        'identity_store_user_name': 'identity_store_user_name',
        'identity_store_email': 'identity_store_email',
        'parent_organizational_unit_id': 'parent_organizational_unit_id',
        'parent_organizational_unit_name': 'parent_organizational_unit_name',
        'blueprint': 'blueprint'
    }

    def __init__(self, account_name=None, account_email=None, phone=None, identity_store_user_name=None, identity_store_email=None, parent_organizational_unit_id=None, parent_organizational_unit_name=None, blueprint=None):
        r"""CreateManagedAccountRequest

        The model defined in huaweicloud sdk

        :param account_name: 纳管账号名。
        :type account_name: str
        :param account_email: 纳管账号邮箱。
        :type account_email: str
        :param phone: 手机号码。
        :type phone: str
        :param identity_store_user_name: Identity Center用户名。
        :type identity_store_user_name: str
        :param identity_store_email: Identity Center邮箱。
        :type identity_store_email: str
        :param parent_organizational_unit_id: 父注册OU ID。
        :type parent_organizational_unit_id: str
        :param parent_organizational_unit_name: 父注册OU名称。
        :type parent_organizational_unit_name: str
        :param blueprint: 
        :type blueprint: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        
        

        self._account_name = None
        self._account_email = None
        self._phone = None
        self._identity_store_user_name = None
        self._identity_store_email = None
        self._parent_organizational_unit_id = None
        self._parent_organizational_unit_name = None
        self._blueprint = None
        self.discriminator = None

        self.account_name = account_name
        if account_email is not None:
            self.account_email = account_email
        if phone is not None:
            self.phone = phone
        if identity_store_user_name is not None:
            self.identity_store_user_name = identity_store_user_name
        if identity_store_email is not None:
            self.identity_store_email = identity_store_email
        self.parent_organizational_unit_id = parent_organizational_unit_id
        self.parent_organizational_unit_name = parent_organizational_unit_name
        if blueprint is not None:
            self.blueprint = blueprint

    @property
    def account_name(self):
        r"""Gets the account_name of this CreateManagedAccountRequest.

        纳管账号名。

        :return: The account_name of this CreateManagedAccountRequest.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this CreateManagedAccountRequest.

        纳管账号名。

        :param account_name: The account_name of this CreateManagedAccountRequest.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_email(self):
        r"""Gets the account_email of this CreateManagedAccountRequest.

        纳管账号邮箱。

        :return: The account_email of this CreateManagedAccountRequest.
        :rtype: str
        """
        return self._account_email

    @account_email.setter
    def account_email(self, account_email):
        r"""Sets the account_email of this CreateManagedAccountRequest.

        纳管账号邮箱。

        :param account_email: The account_email of this CreateManagedAccountRequest.
        :type account_email: str
        """
        self._account_email = account_email

    @property
    def phone(self):
        r"""Gets the phone of this CreateManagedAccountRequest.

        手机号码。

        :return: The phone of this CreateManagedAccountRequest.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this CreateManagedAccountRequest.

        手机号码。

        :param phone: The phone of this CreateManagedAccountRequest.
        :type phone: str
        """
        self._phone = phone

    @property
    def identity_store_user_name(self):
        r"""Gets the identity_store_user_name of this CreateManagedAccountRequest.

        Identity Center用户名。

        :return: The identity_store_user_name of this CreateManagedAccountRequest.
        :rtype: str
        """
        return self._identity_store_user_name

    @identity_store_user_name.setter
    def identity_store_user_name(self, identity_store_user_name):
        r"""Sets the identity_store_user_name of this CreateManagedAccountRequest.

        Identity Center用户名。

        :param identity_store_user_name: The identity_store_user_name of this CreateManagedAccountRequest.
        :type identity_store_user_name: str
        """
        self._identity_store_user_name = identity_store_user_name

    @property
    def identity_store_email(self):
        r"""Gets the identity_store_email of this CreateManagedAccountRequest.

        Identity Center邮箱。

        :return: The identity_store_email of this CreateManagedAccountRequest.
        :rtype: str
        """
        return self._identity_store_email

    @identity_store_email.setter
    def identity_store_email(self, identity_store_email):
        r"""Sets the identity_store_email of this CreateManagedAccountRequest.

        Identity Center邮箱。

        :param identity_store_email: The identity_store_email of this CreateManagedAccountRequest.
        :type identity_store_email: str
        """
        self._identity_store_email = identity_store_email

    @property
    def parent_organizational_unit_id(self):
        r"""Gets the parent_organizational_unit_id of this CreateManagedAccountRequest.

        父注册OU ID。

        :return: The parent_organizational_unit_id of this CreateManagedAccountRequest.
        :rtype: str
        """
        return self._parent_organizational_unit_id

    @parent_organizational_unit_id.setter
    def parent_organizational_unit_id(self, parent_organizational_unit_id):
        r"""Sets the parent_organizational_unit_id of this CreateManagedAccountRequest.

        父注册OU ID。

        :param parent_organizational_unit_id: The parent_organizational_unit_id of this CreateManagedAccountRequest.
        :type parent_organizational_unit_id: str
        """
        self._parent_organizational_unit_id = parent_organizational_unit_id

    @property
    def parent_organizational_unit_name(self):
        r"""Gets the parent_organizational_unit_name of this CreateManagedAccountRequest.

        父注册OU名称。

        :return: The parent_organizational_unit_name of this CreateManagedAccountRequest.
        :rtype: str
        """
        return self._parent_organizational_unit_name

    @parent_organizational_unit_name.setter
    def parent_organizational_unit_name(self, parent_organizational_unit_name):
        r"""Sets the parent_organizational_unit_name of this CreateManagedAccountRequest.

        父注册OU名称。

        :param parent_organizational_unit_name: The parent_organizational_unit_name of this CreateManagedAccountRequest.
        :type parent_organizational_unit_name: str
        """
        self._parent_organizational_unit_name = parent_organizational_unit_name

    @property
    def blueprint(self):
        r"""Gets the blueprint of this CreateManagedAccountRequest.

        :return: The blueprint of this CreateManagedAccountRequest.
        :rtype: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        return self._blueprint

    @blueprint.setter
    def blueprint(self, blueprint):
        r"""Sets the blueprint of this CreateManagedAccountRequest.

        :param blueprint: The blueprint of this CreateManagedAccountRequest.
        :type blueprint: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        self._blueprint = blueprint

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
        if not isinstance(other, CreateManagedAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
