# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDbObjNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'obj_name': 'str',
        'obj_id': 'str',
        'object_sub_type': 'str',
        'obj_type': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'obj_name': 'obj_name',
        'obj_id': 'obj_id',
        'object_sub_type': 'object_sub_type',
        'obj_type': 'obj_type'
    }

    def __init__(self, connection_id=None, db_name=None, schema_name=None, table_name=None, obj_name=None, obj_id=None, object_sub_type=None, obj_type=None):
        r"""DeleteDbObjNewRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param schema_name: Schema名称
        :type schema_name: str
        :param table_name: 表名
        :type table_name: str
        :param obj_name: 对象名称
        :type obj_name: str
        :param obj_id: 对象ID
        :type obj_id: str
        :param object_sub_type: 对象子类型
        :type object_sub_type: str
        :param obj_type: 对象类型
        :type obj_type: str
        """
        
        

        self._connection_id = None
        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._obj_name = None
        self._obj_id = None
        self._object_sub_type = None
        self._obj_type = None
        self.discriminator = None

        self.connection_id = connection_id
        self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if obj_name is not None:
            self.obj_name = obj_name
        if obj_id is not None:
            self.obj_id = obj_id
        if object_sub_type is not None:
            self.object_sub_type = object_sub_type
        self.obj_type = obj_type

    @property
    def connection_id(self):
        r"""Gets the connection_id of this DeleteDbObjNewRequest.

        连接ID

        :return: The connection_id of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this DeleteDbObjNewRequest.

        连接ID

        :param connection_id: The connection_id of this DeleteDbObjNewRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def db_name(self):
        r"""Gets the db_name of this DeleteDbObjNewRequest.

        数据库名称

        :return: The db_name of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DeleteDbObjNewRequest.

        数据库名称

        :param db_name: The db_name of this DeleteDbObjNewRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this DeleteDbObjNewRequest.

        Schema名称

        :return: The schema_name of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this DeleteDbObjNewRequest.

        Schema名称

        :param schema_name: The schema_name of this DeleteDbObjNewRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this DeleteDbObjNewRequest.

        表名

        :return: The table_name of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DeleteDbObjNewRequest.

        表名

        :param table_name: The table_name of this DeleteDbObjNewRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def obj_name(self):
        r"""Gets the obj_name of this DeleteDbObjNewRequest.

        对象名称

        :return: The obj_name of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._obj_name

    @obj_name.setter
    def obj_name(self, obj_name):
        r"""Sets the obj_name of this DeleteDbObjNewRequest.

        对象名称

        :param obj_name: The obj_name of this DeleteDbObjNewRequest.
        :type obj_name: str
        """
        self._obj_name = obj_name

    @property
    def obj_id(self):
        r"""Gets the obj_id of this DeleteDbObjNewRequest.

        对象ID

        :return: The obj_id of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._obj_id

    @obj_id.setter
    def obj_id(self, obj_id):
        r"""Sets the obj_id of this DeleteDbObjNewRequest.

        对象ID

        :param obj_id: The obj_id of this DeleteDbObjNewRequest.
        :type obj_id: str
        """
        self._obj_id = obj_id

    @property
    def object_sub_type(self):
        r"""Gets the object_sub_type of this DeleteDbObjNewRequest.

        对象子类型

        :return: The object_sub_type of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._object_sub_type

    @object_sub_type.setter
    def object_sub_type(self, object_sub_type):
        r"""Sets the object_sub_type of this DeleteDbObjNewRequest.

        对象子类型

        :param object_sub_type: The object_sub_type of this DeleteDbObjNewRequest.
        :type object_sub_type: str
        """
        self._object_sub_type = object_sub_type

    @property
    def obj_type(self):
        r"""Gets the obj_type of this DeleteDbObjNewRequest.

        对象类型

        :return: The obj_type of this DeleteDbObjNewRequest.
        :rtype: str
        """
        return self._obj_type

    @obj_type.setter
    def obj_type(self, obj_type):
        r"""Sets the obj_type of this DeleteDbObjNewRequest.

        对象类型

        :param obj_type: The obj_type of this DeleteDbObjNewRequest.
        :type obj_type: str
        """
        self._obj_type = obj_type

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
        if not isinstance(other, DeleteDbObjNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
