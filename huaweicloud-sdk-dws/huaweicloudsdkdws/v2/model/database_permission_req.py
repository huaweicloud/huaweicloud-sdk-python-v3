# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabasePermissionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'is_grant': 'bool',
        'grant_list': 'list[Grant]',
        'revoke_list': 'list[Revoke]',
        'role_list': 'list[str]',
        'object_list': 'object',
        'all_object': 'bool',
        'cascade': 'bool',
        'database': 'str',
        'schema': 'str',
        'table': 'str'
    }

    attribute_map = {
        'type': 'type',
        'is_grant': 'is_grant',
        'grant_list': 'grant_list',
        'revoke_list': 'revoke_list',
        'role_list': 'role_list',
        'object_list': 'object_list',
        'all_object': 'all_object',
        'cascade': 'cascade',
        'database': 'database',
        'schema': 'schema',
        'table': 'table'
    }

    def __init__(self, type=None, is_grant=None, grant_list=None, revoke_list=None, role_list=None, object_list=None, all_object=None, cascade=None, database=None, schema=None, table=None):
        """DatabasePermissionReq

        The model defined in huaweicloud sdk

        :param type: 对象类型 [DATABASE | SCHEMA | TABLE | VIEW | COLUMN | FUNCTION| SEQUENCE | NODEGROUP | ROLE]
        :type type: str
        :param is_grant: 是否授权操作
        :type is_grant: bool
        :param grant_list: 授权列表 is_grant为true时必填
        :type grant_list: list[:class:`huaweicloudsdkdws.v2.Grant`]
        :param revoke_list: 撤销权限列表 is_grant为false时必填
        :type revoke_list: list[:class:`huaweicloudsdkdws.v2.Revoke`]
        :param role_list: 被授权角色列表
        :type role_list: list[str]
        :param object_list: 权限所属对象列表
        :type object_list: object
        :param all_object: schema下所有数据库对象权限，默认false
        :type all_object: bool
        :param cascade: 撤销权限是否级联撤销 默认 true
        :type cascade: bool
        :param database: 数据库名称
        :type database: str
        :param schema: 模式名称
        :type schema: str
        :param table: 表名
        :type table: str
        """
        
        

        self._type = None
        self._is_grant = None
        self._grant_list = None
        self._revoke_list = None
        self._role_list = None
        self._object_list = None
        self._all_object = None
        self._cascade = None
        self._database = None
        self._schema = None
        self._table = None
        self.discriminator = None

        self.type = type
        self.is_grant = is_grant
        if grant_list is not None:
            self.grant_list = grant_list
        if revoke_list is not None:
            self.revoke_list = revoke_list
        self.role_list = role_list
        self.object_list = object_list
        if all_object is not None:
            self.all_object = all_object
        if cascade is not None:
            self.cascade = cascade
        self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table

    @property
    def type(self):
        """Gets the type of this DatabasePermissionReq.

        对象类型 [DATABASE | SCHEMA | TABLE | VIEW | COLUMN | FUNCTION| SEQUENCE | NODEGROUP | ROLE]

        :return: The type of this DatabasePermissionReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatabasePermissionReq.

        对象类型 [DATABASE | SCHEMA | TABLE | VIEW | COLUMN | FUNCTION| SEQUENCE | NODEGROUP | ROLE]

        :param type: The type of this DatabasePermissionReq.
        :type type: str
        """
        self._type = type

    @property
    def is_grant(self):
        """Gets the is_grant of this DatabasePermissionReq.

        是否授权操作

        :return: The is_grant of this DatabasePermissionReq.
        :rtype: bool
        """
        return self._is_grant

    @is_grant.setter
    def is_grant(self, is_grant):
        """Sets the is_grant of this DatabasePermissionReq.

        是否授权操作

        :param is_grant: The is_grant of this DatabasePermissionReq.
        :type is_grant: bool
        """
        self._is_grant = is_grant

    @property
    def grant_list(self):
        """Gets the grant_list of this DatabasePermissionReq.

        授权列表 is_grant为true时必填

        :return: The grant_list of this DatabasePermissionReq.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Grant`]
        """
        return self._grant_list

    @grant_list.setter
    def grant_list(self, grant_list):
        """Sets the grant_list of this DatabasePermissionReq.

        授权列表 is_grant为true时必填

        :param grant_list: The grant_list of this DatabasePermissionReq.
        :type grant_list: list[:class:`huaweicloudsdkdws.v2.Grant`]
        """
        self._grant_list = grant_list

    @property
    def revoke_list(self):
        """Gets the revoke_list of this DatabasePermissionReq.

        撤销权限列表 is_grant为false时必填

        :return: The revoke_list of this DatabasePermissionReq.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Revoke`]
        """
        return self._revoke_list

    @revoke_list.setter
    def revoke_list(self, revoke_list):
        """Sets the revoke_list of this DatabasePermissionReq.

        撤销权限列表 is_grant为false时必填

        :param revoke_list: The revoke_list of this DatabasePermissionReq.
        :type revoke_list: list[:class:`huaweicloudsdkdws.v2.Revoke`]
        """
        self._revoke_list = revoke_list

    @property
    def role_list(self):
        """Gets the role_list of this DatabasePermissionReq.

        被授权角色列表

        :return: The role_list of this DatabasePermissionReq.
        :rtype: list[str]
        """
        return self._role_list

    @role_list.setter
    def role_list(self, role_list):
        """Sets the role_list of this DatabasePermissionReq.

        被授权角色列表

        :param role_list: The role_list of this DatabasePermissionReq.
        :type role_list: list[str]
        """
        self._role_list = role_list

    @property
    def object_list(self):
        """Gets the object_list of this DatabasePermissionReq.

        权限所属对象列表

        :return: The object_list of this DatabasePermissionReq.
        :rtype: object
        """
        return self._object_list

    @object_list.setter
    def object_list(self, object_list):
        """Sets the object_list of this DatabasePermissionReq.

        权限所属对象列表

        :param object_list: The object_list of this DatabasePermissionReq.
        :type object_list: object
        """
        self._object_list = object_list

    @property
    def all_object(self):
        """Gets the all_object of this DatabasePermissionReq.

        schema下所有数据库对象权限，默认false

        :return: The all_object of this DatabasePermissionReq.
        :rtype: bool
        """
        return self._all_object

    @all_object.setter
    def all_object(self, all_object):
        """Sets the all_object of this DatabasePermissionReq.

        schema下所有数据库对象权限，默认false

        :param all_object: The all_object of this DatabasePermissionReq.
        :type all_object: bool
        """
        self._all_object = all_object

    @property
    def cascade(self):
        """Gets the cascade of this DatabasePermissionReq.

        撤销权限是否级联撤销 默认 true

        :return: The cascade of this DatabasePermissionReq.
        :rtype: bool
        """
        return self._cascade

    @cascade.setter
    def cascade(self, cascade):
        """Sets the cascade of this DatabasePermissionReq.

        撤销权限是否级联撤销 默认 true

        :param cascade: The cascade of this DatabasePermissionReq.
        :type cascade: bool
        """
        self._cascade = cascade

    @property
    def database(self):
        """Gets the database of this DatabasePermissionReq.

        数据库名称

        :return: The database of this DatabasePermissionReq.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this DatabasePermissionReq.

        数据库名称

        :param database: The database of this DatabasePermissionReq.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        """Gets the schema of this DatabasePermissionReq.

        模式名称

        :return: The schema of this DatabasePermissionReq.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this DatabasePermissionReq.

        模式名称

        :param schema: The schema of this DatabasePermissionReq.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        """Gets the table of this DatabasePermissionReq.

        表名

        :return: The table of this DatabasePermissionReq.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this DatabasePermissionReq.

        表名

        :param table: The table of this DatabasePermissionReq.
        :type table: str
        """
        self._table = table

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
        if not isinstance(other, DatabasePermissionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
