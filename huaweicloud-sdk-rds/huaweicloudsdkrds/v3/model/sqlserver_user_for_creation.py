# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlserverUserForCreation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'password': 'str',
        'instance_readonly': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'instance_readonly': 'instance_readonly'
    }

    def __init__(self, name=None, password=None, instance_readonly=None):
        r"""SqlserverUserForCreation

        The model defined in huaweicloud sdk

        :param name: 数据库用户名称。  数据库帐号名称在1到128个字符之间，不能和系统用户名称相同。  系统用户包括：rdsadmin, rdsuser, rdsbackup, rdsmirror。
        :type name: str
        :param password: 数据库帐号密码。  取值范围：非空，密码长度在8到128个字符之间，至少包含大写字母、小写字母、数字、特殊字符三种字符的组合。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param instance_readonly: 是否创建实例级只读账号。
        :type instance_readonly: bool
        """
        
        

        self._name = None
        self._password = None
        self._instance_readonly = None
        self.discriminator = None

        self.name = name
        self.password = password
        if instance_readonly is not None:
            self.instance_readonly = instance_readonly

    @property
    def name(self):
        r"""Gets the name of this SqlserverUserForCreation.

        数据库用户名称。  数据库帐号名称在1到128个字符之间，不能和系统用户名称相同。  系统用户包括：rdsadmin, rdsuser, rdsbackup, rdsmirror。

        :return: The name of this SqlserverUserForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SqlserverUserForCreation.

        数据库用户名称。  数据库帐号名称在1到128个字符之间，不能和系统用户名称相同。  系统用户包括：rdsadmin, rdsuser, rdsbackup, rdsmirror。

        :param name: The name of this SqlserverUserForCreation.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        r"""Gets the password of this SqlserverUserForCreation.

        数据库帐号密码。  取值范围：非空，密码长度在8到128个字符之间，至少包含大写字母、小写字母、数字、特殊字符三种字符的组合。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this SqlserverUserForCreation.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this SqlserverUserForCreation.

        数据库帐号密码。  取值范围：非空，密码长度在8到128个字符之间，至少包含大写字母、小写字母、数字、特殊字符三种字符的组合。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this SqlserverUserForCreation.
        :type password: str
        """
        self._password = password

    @property
    def instance_readonly(self):
        r"""Gets the instance_readonly of this SqlserverUserForCreation.

        是否创建实例级只读账号。

        :return: The instance_readonly of this SqlserverUserForCreation.
        :rtype: bool
        """
        return self._instance_readonly

    @instance_readonly.setter
    def instance_readonly(self, instance_readonly):
        r"""Sets the instance_readonly of this SqlserverUserForCreation.

        是否创建实例级只读账号。

        :param instance_readonly: The instance_readonly of this SqlserverUserForCreation.
        :type instance_readonly: bool
        """
        self._instance_readonly = instance_readonly

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
        if not isinstance(other, SqlserverUserForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
