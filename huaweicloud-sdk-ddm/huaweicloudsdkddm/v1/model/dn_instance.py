# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DNInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dn_instance_id': 'str',
        'admin_user': 'str',
        'admin_password': 'str'
    }

    attribute_map = {
        'dn_instance_id': 'dn_instance_id',
        'admin_user': 'admin_user',
        'admin_password': 'admin_password'
    }

    def __init__(self, dn_instance_id=None, admin_user=None, admin_password=None):
        r"""DNInstance

        The model defined in huaweicloud sdk

        :param dn_instance_id: 实例id。
        :type dn_instance_id: str
        :param admin_user: 实例账号。
        :type admin_user: str
        :param admin_password: 实例密码。
        :type admin_password: str
        """
        
        

        self._dn_instance_id = None
        self._admin_user = None
        self._admin_password = None
        self.discriminator = None

        if dn_instance_id is not None:
            self.dn_instance_id = dn_instance_id
        if admin_user is not None:
            self.admin_user = admin_user
        if admin_password is not None:
            self.admin_password = admin_password

    @property
    def dn_instance_id(self):
        r"""Gets the dn_instance_id of this DNInstance.

        实例id。

        :return: The dn_instance_id of this DNInstance.
        :rtype: str
        """
        return self._dn_instance_id

    @dn_instance_id.setter
    def dn_instance_id(self, dn_instance_id):
        r"""Sets the dn_instance_id of this DNInstance.

        实例id。

        :param dn_instance_id: The dn_instance_id of this DNInstance.
        :type dn_instance_id: str
        """
        self._dn_instance_id = dn_instance_id

    @property
    def admin_user(self):
        r"""Gets the admin_user of this DNInstance.

        实例账号。

        :return: The admin_user of this DNInstance.
        :rtype: str
        """
        return self._admin_user

    @admin_user.setter
    def admin_user(self, admin_user):
        r"""Sets the admin_user of this DNInstance.

        实例账号。

        :param admin_user: The admin_user of this DNInstance.
        :type admin_user: str
        """
        self._admin_user = admin_user

    @property
    def admin_password(self):
        r"""Gets the admin_password of this DNInstance.

        实例密码。

        :return: The admin_password of this DNInstance.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        r"""Sets the admin_password of this DNInstance.

        实例密码。

        :param admin_password: The admin_password of this DNInstance.
        :type admin_password: str
        """
        self._admin_password = admin_password

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
        if not isinstance(other, DNInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
