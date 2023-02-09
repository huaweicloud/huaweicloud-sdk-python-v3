# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConstraintsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'catalog_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'type': 'str',
        'parent_db': 'str',
        'parent_tbl': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'type': 'type',
        'parent_db': 'parent_db',
        'parent_tbl': 'parent_tbl'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name=None, type=None, parent_db=None, parent_tbl=None):
        """ListConstraintsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param type: 列限制条件类型
        :type type: str
        :param parent_db: 获取表外键时使用，指定外键被引用表所在的数据库名
        :type parent_db: str
        :param parent_tbl: 获取表外键时使用，指定外键被引用表的表名
        :type parent_tbl: str
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._type = None
        self._parent_db = None
        self._parent_tbl = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        self.type = type
        if parent_db is not None:
            self.parent_db = parent_db
        if parent_tbl is not None:
            self.parent_tbl = parent_tbl

    @property
    def instance_id(self):
        """Gets the instance_id of this ListConstraintsRequest.

        实例ID

        :return: The instance_id of this ListConstraintsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListConstraintsRequest.

        实例ID

        :param instance_id: The instance_id of this ListConstraintsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        """Gets the catalog_name of this ListConstraintsRequest.

        catalog名字

        :return: The catalog_name of this ListConstraintsRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this ListConstraintsRequest.

        catalog名字

        :param catalog_name: The catalog_name of this ListConstraintsRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this ListConstraintsRequest.

        数据库名字

        :return: The database_name of this ListConstraintsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListConstraintsRequest.

        数据库名字

        :param database_name: The database_name of this ListConstraintsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this ListConstraintsRequest.

        表名称

        :return: The table_name of this ListConstraintsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ListConstraintsRequest.

        表名称

        :param table_name: The table_name of this ListConstraintsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def type(self):
        """Gets the type of this ListConstraintsRequest.

        列限制条件类型

        :return: The type of this ListConstraintsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListConstraintsRequest.

        列限制条件类型

        :param type: The type of this ListConstraintsRequest.
        :type type: str
        """
        self._type = type

    @property
    def parent_db(self):
        """Gets the parent_db of this ListConstraintsRequest.

        获取表外键时使用，指定外键被引用表所在的数据库名

        :return: The parent_db of this ListConstraintsRequest.
        :rtype: str
        """
        return self._parent_db

    @parent_db.setter
    def parent_db(self, parent_db):
        """Sets the parent_db of this ListConstraintsRequest.

        获取表外键时使用，指定外键被引用表所在的数据库名

        :param parent_db: The parent_db of this ListConstraintsRequest.
        :type parent_db: str
        """
        self._parent_db = parent_db

    @property
    def parent_tbl(self):
        """Gets the parent_tbl of this ListConstraintsRequest.

        获取表外键时使用，指定外键被引用表的表名

        :return: The parent_tbl of this ListConstraintsRequest.
        :rtype: str
        """
        return self._parent_tbl

    @parent_tbl.setter
    def parent_tbl(self, parent_tbl):
        """Sets the parent_tbl of this ListConstraintsRequest.

        获取表外键时使用，指定外键被引用表的表名

        :param parent_tbl: The parent_tbl of this ListConstraintsRequest.
        :type parent_tbl: str
        """
        self._parent_tbl = parent_tbl

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
        if not isinstance(other, ListConstraintsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
