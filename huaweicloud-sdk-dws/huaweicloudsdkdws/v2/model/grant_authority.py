# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantAuthority:

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
        'database': 'str',
        'schema': 'str',
        'obj_name': 'str',
        'all_object': 'bool',
        'future': 'bool',
        'future_object_owners': 'str',
        'column_name': 'list[str]',
        'privileges': 'list[Grant]'
    }

    attribute_map = {
        'type': 'type',
        'database': 'database',
        'schema': 'schema',
        'obj_name': 'obj_name',
        'all_object': 'all_object',
        'future': 'future',
        'future_object_owners': 'future_object_owners',
        'column_name': 'column_name',
        'privileges': 'privileges'
    }

    def __init__(self, type=None, database=None, schema=None, obj_name=None, all_object=None, future=None, future_object_owners=None, column_name=None, privileges=None):
        r"""GrantAuthority

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 权限类型。 **取值范围**： 不涉及。
        :type type: str
        :param database: **参数解释**： 数据库名称。 **取值范围**： 不涉及。
        :type database: str
        :param schema: **参数解释**： 模式名称。 **取值范围**： 不涉及。
        :type schema: str
        :param obj_name: **参数解释**： 对象名称。 **取值范围**： 不涉及。
        :type obj_name: str
        :param all_object: **参数解释**： 是否所有对象生效。 **取值范围**： 不涉及。
        :type all_object: bool
        :param future: **参数解释**： 是否对未来对象生效。 **取值范围**： 不涉及。
        :type future: bool
        :param future_object_owners: **参数解释**： 未来对象-所属用户。 **取值范围**： 不涉及。
        :type future_object_owners: str
        :param column_name: **参数解释**： 列名。 **取值范围**： 不涉及。
        :type column_name: list[str]
        :param privileges: **参数解释**： 权限。 **取值范围**： 不涉及。
        :type privileges: list[:class:`huaweicloudsdkdws.v2.Grant`]
        """
        
        

        self._type = None
        self._database = None
        self._schema = None
        self._obj_name = None
        self._all_object = None
        self._future = None
        self._future_object_owners = None
        self._column_name = None
        self._privileges = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if obj_name is not None:
            self.obj_name = obj_name
        if all_object is not None:
            self.all_object = all_object
        if future is not None:
            self.future = future
        if future_object_owners is not None:
            self.future_object_owners = future_object_owners
        if column_name is not None:
            self.column_name = column_name
        if privileges is not None:
            self.privileges = privileges

    @property
    def type(self):
        r"""Gets the type of this GrantAuthority.

        **参数解释**： 权限类型。 **取值范围**： 不涉及。

        :return: The type of this GrantAuthority.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GrantAuthority.

        **参数解释**： 权限类型。 **取值范围**： 不涉及。

        :param type: The type of this GrantAuthority.
        :type type: str
        """
        self._type = type

    @property
    def database(self):
        r"""Gets the database of this GrantAuthority.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :return: The database of this GrantAuthority.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this GrantAuthority.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :param database: The database of this GrantAuthority.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        r"""Gets the schema of this GrantAuthority.

        **参数解释**： 模式名称。 **取值范围**： 不涉及。

        :return: The schema of this GrantAuthority.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this GrantAuthority.

        **参数解释**： 模式名称。 **取值范围**： 不涉及。

        :param schema: The schema of this GrantAuthority.
        :type schema: str
        """
        self._schema = schema

    @property
    def obj_name(self):
        r"""Gets the obj_name of this GrantAuthority.

        **参数解释**： 对象名称。 **取值范围**： 不涉及。

        :return: The obj_name of this GrantAuthority.
        :rtype: str
        """
        return self._obj_name

    @obj_name.setter
    def obj_name(self, obj_name):
        r"""Sets the obj_name of this GrantAuthority.

        **参数解释**： 对象名称。 **取值范围**： 不涉及。

        :param obj_name: The obj_name of this GrantAuthority.
        :type obj_name: str
        """
        self._obj_name = obj_name

    @property
    def all_object(self):
        r"""Gets the all_object of this GrantAuthority.

        **参数解释**： 是否所有对象生效。 **取值范围**： 不涉及。

        :return: The all_object of this GrantAuthority.
        :rtype: bool
        """
        return self._all_object

    @all_object.setter
    def all_object(self, all_object):
        r"""Sets the all_object of this GrantAuthority.

        **参数解释**： 是否所有对象生效。 **取值范围**： 不涉及。

        :param all_object: The all_object of this GrantAuthority.
        :type all_object: bool
        """
        self._all_object = all_object

    @property
    def future(self):
        r"""Gets the future of this GrantAuthority.

        **参数解释**： 是否对未来对象生效。 **取值范围**： 不涉及。

        :return: The future of this GrantAuthority.
        :rtype: bool
        """
        return self._future

    @future.setter
    def future(self, future):
        r"""Sets the future of this GrantAuthority.

        **参数解释**： 是否对未来对象生效。 **取值范围**： 不涉及。

        :param future: The future of this GrantAuthority.
        :type future: bool
        """
        self._future = future

    @property
    def future_object_owners(self):
        r"""Gets the future_object_owners of this GrantAuthority.

        **参数解释**： 未来对象-所属用户。 **取值范围**： 不涉及。

        :return: The future_object_owners of this GrantAuthority.
        :rtype: str
        """
        return self._future_object_owners

    @future_object_owners.setter
    def future_object_owners(self, future_object_owners):
        r"""Sets the future_object_owners of this GrantAuthority.

        **参数解释**： 未来对象-所属用户。 **取值范围**： 不涉及。

        :param future_object_owners: The future_object_owners of this GrantAuthority.
        :type future_object_owners: str
        """
        self._future_object_owners = future_object_owners

    @property
    def column_name(self):
        r"""Gets the column_name of this GrantAuthority.

        **参数解释**： 列名。 **取值范围**： 不涉及。

        :return: The column_name of this GrantAuthority.
        :rtype: list[str]
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this GrantAuthority.

        **参数解释**： 列名。 **取值范围**： 不涉及。

        :param column_name: The column_name of this GrantAuthority.
        :type column_name: list[str]
        """
        self._column_name = column_name

    @property
    def privileges(self):
        r"""Gets the privileges of this GrantAuthority.

        **参数解释**： 权限。 **取值范围**： 不涉及。

        :return: The privileges of this GrantAuthority.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Grant`]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        r"""Sets the privileges of this GrantAuthority.

        **参数解释**： 权限。 **取值范围**： 不涉及。

        :param privileges: The privileges of this GrantAuthority.
        :type privileges: list[:class:`huaweicloudsdkdws.v2.Grant`]
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
        if not isinstance(other, GrantAuthority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
