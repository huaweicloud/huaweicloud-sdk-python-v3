# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConstraintRequest:

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
        'constraint_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'constraint_name': 'constraint_name'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name=None, constraint_name=None):
        r"""DeleteConstraintRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param constraint_name: 列限制信息名字; 外键填写外键限制名
        :type constraint_name: str
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._constraint_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        self.constraint_name = constraint_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteConstraintRequest.

        实例ID

        :return: The instance_id of this DeleteConstraintRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteConstraintRequest.

        实例ID

        :param instance_id: The instance_id of this DeleteConstraintRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this DeleteConstraintRequest.

        catalog名字

        :return: The catalog_name of this DeleteConstraintRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this DeleteConstraintRequest.

        catalog名字

        :param catalog_name: The catalog_name of this DeleteConstraintRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this DeleteConstraintRequest.

        数据库名字

        :return: The database_name of this DeleteConstraintRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DeleteConstraintRequest.

        数据库名字

        :param database_name: The database_name of this DeleteConstraintRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this DeleteConstraintRequest.

        表名称

        :return: The table_name of this DeleteConstraintRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DeleteConstraintRequest.

        表名称

        :param table_name: The table_name of this DeleteConstraintRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def constraint_name(self):
        r"""Gets the constraint_name of this DeleteConstraintRequest.

        列限制信息名字; 外键填写外键限制名

        :return: The constraint_name of this DeleteConstraintRequest.
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        r"""Sets the constraint_name of this DeleteConstraintRequest.

        列限制信息名字; 外键填写外键限制名

        :param constraint_name: The constraint_name of this DeleteConstraintRequest.
        :type constraint_name: str
        """
        self._constraint_name = constraint_name

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
        if not isinstance(other, DeleteConstraintRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
