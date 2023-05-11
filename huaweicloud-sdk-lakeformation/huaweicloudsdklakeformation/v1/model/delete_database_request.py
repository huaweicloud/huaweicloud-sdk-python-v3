# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDatabaseRequest:

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
        'delete_data': 'bool',
        'cascade': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'delete_data': 'delete_data',
        'cascade': 'cascade'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, delete_data=None, cascade=None):
        """DeleteDatabaseRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例Id
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名
        :type database_name: str
        :param delete_data: 是否删除数据库路径下的数据
        :type delete_data: bool
        :param cascade: 是否级联删除数据库下的表、分区以及函数
        :type cascade: bool
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._delete_data = None
        self._cascade = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        if delete_data is not None:
            self.delete_data = delete_data
        if cascade is not None:
            self.cascade = cascade

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteDatabaseRequest.

        实例Id

        :return: The instance_id of this DeleteDatabaseRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteDatabaseRequest.

        实例Id

        :param instance_id: The instance_id of this DeleteDatabaseRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        """Gets the catalog_name of this DeleteDatabaseRequest.

        catalog名字

        :return: The catalog_name of this DeleteDatabaseRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this DeleteDatabaseRequest.

        catalog名字

        :param catalog_name: The catalog_name of this DeleteDatabaseRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this DeleteDatabaseRequest.

        数据库名

        :return: The database_name of this DeleteDatabaseRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DeleteDatabaseRequest.

        数据库名

        :param database_name: The database_name of this DeleteDatabaseRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def delete_data(self):
        """Gets the delete_data of this DeleteDatabaseRequest.

        是否删除数据库路径下的数据

        :return: The delete_data of this DeleteDatabaseRequest.
        :rtype: bool
        """
        return self._delete_data

    @delete_data.setter
    def delete_data(self, delete_data):
        """Sets the delete_data of this DeleteDatabaseRequest.

        是否删除数据库路径下的数据

        :param delete_data: The delete_data of this DeleteDatabaseRequest.
        :type delete_data: bool
        """
        self._delete_data = delete_data

    @property
    def cascade(self):
        """Gets the cascade of this DeleteDatabaseRequest.

        是否级联删除数据库下的表、分区以及函数

        :return: The cascade of this DeleteDatabaseRequest.
        :rtype: bool
        """
        return self._cascade

    @cascade.setter
    def cascade(self, cascade):
        """Sets the cascade of this DeleteDatabaseRequest.

        是否级联删除数据库下的表、分区以及函数

        :param cascade: The cascade of this DeleteDatabaseRequest.
        :type cascade: bool
        """
        self._cascade = cascade

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
        if not isinstance(other, DeleteDatabaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
