# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseInstabcesParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'admin_user': 'str',
        'admin_password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'admin_user': 'adminUser',
        'admin_password': 'adminPassword'
    }

    def __init__(self, id=None, admin_user=None, admin_password=None):
        """DatabaseInstabcesParam

        The model defined in huaweicloud sdk

        :param id: 逻辑库关联的RDS的id
        :type id: str
        :param admin_user: 关联RDS实例的用户。
        :type admin_user: str
        :param admin_password: 关联RDS实例的密码。
        :type admin_password: str
        """
        
        

        self._id = None
        self._admin_user = None
        self._admin_password = None
        self.discriminator = None

        self.id = id
        self.admin_user = admin_user
        self.admin_password = admin_password

    @property
    def id(self):
        """Gets the id of this DatabaseInstabcesParam.

        逻辑库关联的RDS的id

        :return: The id of this DatabaseInstabcesParam.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseInstabcesParam.

        逻辑库关联的RDS的id

        :param id: The id of this DatabaseInstabcesParam.
        :type id: str
        """
        self._id = id

    @property
    def admin_user(self):
        """Gets the admin_user of this DatabaseInstabcesParam.

        关联RDS实例的用户。

        :return: The admin_user of this DatabaseInstabcesParam.
        :rtype: str
        """
        return self._admin_user

    @admin_user.setter
    def admin_user(self, admin_user):
        """Sets the admin_user of this DatabaseInstabcesParam.

        关联RDS实例的用户。

        :param admin_user: The admin_user of this DatabaseInstabcesParam.
        :type admin_user: str
        """
        self._admin_user = admin_user

    @property
    def admin_password(self):
        """Gets the admin_password of this DatabaseInstabcesParam.

        关联RDS实例的密码。

        :return: The admin_password of this DatabaseInstabcesParam.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """Sets the admin_password of this DatabaseInstabcesParam.

        关联RDS实例的密码。

        :param admin_password: The admin_password of this DatabaseInstabcesParam.
        :type admin_password: str
        """
        self._admin_password = admin_password

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
        if not isinstance(other, DatabaseInstabcesParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
