# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableUserPermissionsRespPrivilege:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'object': 'str',
        'privileges': 'list[str]'
    }

    attribute_map = {
        'object': 'object',
        'privileges': 'privileges'
    }

    def __init__(self, object=None, privileges=None):
        """TableUserPermissionsRespPrivilege

        The model defined in huaweicloud sdk

        :param object: 该用户有权限的对象： “databases.数据库名.tables.表名”，用户在当前表上的权限。 “databases.数据库名.tables.表名.columns.列名”，用户在列上的权限。
        :type object: str
        :param privileges: 用户在指定对象上的权限。
        :type privileges: list[str]
        """
        
        

        self._object = None
        self._privileges = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if privileges is not None:
            self.privileges = privileges

    @property
    def object(self):
        """Gets the object of this TableUserPermissionsRespPrivilege.

        该用户有权限的对象： “databases.数据库名.tables.表名”，用户在当前表上的权限。 “databases.数据库名.tables.表名.columns.列名”，用户在列上的权限。

        :return: The object of this TableUserPermissionsRespPrivilege.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this TableUserPermissionsRespPrivilege.

        该用户有权限的对象： “databases.数据库名.tables.表名”，用户在当前表上的权限。 “databases.数据库名.tables.表名.columns.列名”，用户在列上的权限。

        :param object: The object of this TableUserPermissionsRespPrivilege.
        :type object: str
        """
        self._object = object

    @property
    def privileges(self):
        """Gets the privileges of this TableUserPermissionsRespPrivilege.

        用户在指定对象上的权限。

        :return: The privileges of this TableUserPermissionsRespPrivilege.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this TableUserPermissionsRespPrivilege.

        用户在指定对象上的权限。

        :param privileges: The privileges of this TableUserPermissionsRespPrivilege.
        :type privileges: list[str]
        """
        self._privileges = privileges

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
        if not isinstance(other, TableUserPermissionsRespPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
