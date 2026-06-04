# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTableRequest:

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
        'delete_data': 'bool',
        'is_async': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'delete_data': 'delete_data',
        'is_async': 'is_async'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name=None, delete_data=None, is_async=None):
        r"""DeleteTableRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param catalog_name: catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type catalog_name: str
        :param database_name: 数据库名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。
        :type database_name: str
        :param table_name: 表名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~256个字符。
        :type table_name: str
        :param delete_data: 是否删除表中的数据，该参数只针对内表生效，外表不会删除数据。默认为false。
        :type delete_data: bool
        :param is_async: 是否异步删除，默认为false。
        :type is_async: bool
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._delete_data = None
        self._is_async = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        if delete_data is not None:
            self.delete_data = delete_data
        if is_async is not None:
            self.is_async = is_async

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteTableRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this DeleteTableRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteTableRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this DeleteTableRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this DeleteTableRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The catalog_name of this DeleteTableRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this DeleteTableRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param catalog_name: The catalog_name of this DeleteTableRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this DeleteTableRequest.

        数据库名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。

        :return: The database_name of this DeleteTableRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DeleteTableRequest.

        数据库名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。

        :param database_name: The database_name of this DeleteTableRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this DeleteTableRequest.

        表名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~256个字符。

        :return: The table_name of this DeleteTableRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DeleteTableRequest.

        表名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~256个字符。

        :param table_name: The table_name of this DeleteTableRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def delete_data(self):
        r"""Gets the delete_data of this DeleteTableRequest.

        是否删除表中的数据，该参数只针对内表生效，外表不会删除数据。默认为false。

        :return: The delete_data of this DeleteTableRequest.
        :rtype: bool
        """
        return self._delete_data

    @delete_data.setter
    def delete_data(self, delete_data):
        r"""Sets the delete_data of this DeleteTableRequest.

        是否删除表中的数据，该参数只针对内表生效，外表不会删除数据。默认为false。

        :param delete_data: The delete_data of this DeleteTableRequest.
        :type delete_data: bool
        """
        self._delete_data = delete_data

    @property
    def is_async(self):
        r"""Gets the is_async of this DeleteTableRequest.

        是否异步删除，默认为false。

        :return: The is_async of this DeleteTableRequest.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this DeleteTableRequest.

        是否异步删除，默认为false。

        :param is_async: The is_async of this DeleteTableRequest.
        :type is_async: bool
        """
        self._is_async = is_async

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
        if not isinstance(other, DeleteTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
