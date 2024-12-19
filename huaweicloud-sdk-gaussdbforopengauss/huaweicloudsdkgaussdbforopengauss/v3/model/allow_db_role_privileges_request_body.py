# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllowDbRolePrivilegesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'user': 'object'
    }

    attribute_map = {
        'db_name': 'db_name',
        'user': 'user'
    }

    def __init__(self, db_name=None, user=None):
        """AllowDbRolePrivilegesRequestBody

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。 不能使用模板库，且是已存在的数据库名称。 模板库包括postgres， template0 ，template1，templatea，template_pdb，templatem。
        :type db_name: str
        :param user: 角色权限信息。
        :type user: object
        """
        
        

        self._db_name = None
        self._user = None
        self.discriminator = None

        self.db_name = db_name
        self.user = user

    @property
    def db_name(self):
        """Gets the db_name of this AllowDbRolePrivilegesRequestBody.

        数据库名称。 不能使用模板库，且是已存在的数据库名称。 模板库包括postgres， template0 ，template1，templatea，template_pdb，templatem。

        :return: The db_name of this AllowDbRolePrivilegesRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this AllowDbRolePrivilegesRequestBody.

        数据库名称。 不能使用模板库，且是已存在的数据库名称。 模板库包括postgres， template0 ，template1，templatea，template_pdb，templatem。

        :param db_name: The db_name of this AllowDbRolePrivilegesRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def user(self):
        """Gets the user of this AllowDbRolePrivilegesRequestBody.

        角色权限信息。

        :return: The user of this AllowDbRolePrivilegesRequestBody.
        :rtype: object
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AllowDbRolePrivilegesRequestBody.

        角色权限信息。

        :param user: The user of this AllowDbRolePrivilegesRequestBody.
        :type user: object
        """
        self._user = user

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
        if not isinstance(other, AllowDbRolePrivilegesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
