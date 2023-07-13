# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'create_time': 'datetime',
        'last_access_time': 'datetime',
        'update_time': 'datetime',
        'last_analyzed_time': 'datetime',
        'owner': 'str',
        'owner_type': 'str',
        'parameters': 'dict(str, str)',
        'partition_keys': 'list[Column]',
        'retention': 'int',
        'storage_descriptor': 'StorageDescriptor',
        'table_type': 'str',
        'comments': 'str',
        'view_expanded_text': 'str',
        'view_original_text': 'str'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'create_time': 'create_time',
        'last_access_time': 'last_access_time',
        'update_time': 'update_time',
        'last_analyzed_time': 'last_analyzed_time',
        'owner': 'owner',
        'owner_type': 'owner_type',
        'parameters': 'parameters',
        'partition_keys': 'partition_keys',
        'retention': 'retention',
        'storage_descriptor': 'storage_descriptor',
        'table_type': 'table_type',
        'comments': 'comments',
        'view_expanded_text': 'view_expanded_text',
        'view_original_text': 'view_original_text'
    }

    def __init__(self, catalog_name=None, database_name=None, table_name=None, create_time=None, last_access_time=None, update_time=None, last_analyzed_time=None, owner=None, owner_type=None, parameters=None, partition_keys=None, retention=None, storage_descriptor=None, table_type=None, comments=None, view_expanded_text=None, view_original_text=None):
        """CreateTableResponse

        The model defined in huaweicloud sdk

        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名字
        :type table_name: str
        :param create_time: 表创建时间
        :type create_time: datetime
        :param last_access_time: 最后访问时间
        :type last_access_time: datetime
        :param update_time: 表元数据最后一次修改时间
        :type update_time: datetime
        :param last_analyzed_time: 上一次做列级别的统计信息计算的时间
        :type last_analyzed_time: datetime
        :param owner: 用户信息
        :type owner: str
        :param owner_type: 用户类型
        :type owner_type: str
        :param parameters: 参数
        :type parameters: dict(str, str)
        :param partition_keys: 表分区列的列表
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        :param retention: 表保留时间
        :type retention: int
        :param storage_descriptor: 
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        :param table_type: 表类型
        :type table_type: str
        :param comments: 表描述信息
        :type comments: str
        :param view_expanded_text: 如果表是视图，则为视图的扩展文本；否则为 null
        :type view_expanded_text: str
        :param view_original_text: 如果表是视图，则为视图的原始文本；否则为 null
        :type view_original_text: str
        """
        
        super(CreateTableResponse, self).__init__()

        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._create_time = None
        self._last_access_time = None
        self._update_time = None
        self._last_analyzed_time = None
        self._owner = None
        self._owner_type = None
        self._parameters = None
        self._partition_keys = None
        self._retention = None
        self._storage_descriptor = None
        self._table_type = None
        self._comments = None
        self._view_expanded_text = None
        self._view_original_text = None
        self.discriminator = None

        if catalog_name is not None:
            self.catalog_name = catalog_name
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if create_time is not None:
            self.create_time = create_time
        if last_access_time is not None:
            self.last_access_time = last_access_time
        if update_time is not None:
            self.update_time = update_time
        if last_analyzed_time is not None:
            self.last_analyzed_time = last_analyzed_time
        if owner is not None:
            self.owner = owner
        if owner_type is not None:
            self.owner_type = owner_type
        if parameters is not None:
            self.parameters = parameters
        if partition_keys is not None:
            self.partition_keys = partition_keys
        if retention is not None:
            self.retention = retention
        if storage_descriptor is not None:
            self.storage_descriptor = storage_descriptor
        if table_type is not None:
            self.table_type = table_type
        if comments is not None:
            self.comments = comments
        if view_expanded_text is not None:
            self.view_expanded_text = view_expanded_text
        if view_original_text is not None:
            self.view_original_text = view_original_text

    @property
    def catalog_name(self):
        """Gets the catalog_name of this CreateTableResponse.

        catalog名字

        :return: The catalog_name of this CreateTableResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this CreateTableResponse.

        catalog名字

        :param catalog_name: The catalog_name of this CreateTableResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this CreateTableResponse.

        数据库名字

        :return: The database_name of this CreateTableResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this CreateTableResponse.

        数据库名字

        :param database_name: The database_name of this CreateTableResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this CreateTableResponse.

        表名字

        :return: The table_name of this CreateTableResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this CreateTableResponse.

        表名字

        :param table_name: The table_name of this CreateTableResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def create_time(self):
        """Gets the create_time of this CreateTableResponse.

        表创建时间

        :return: The create_time of this CreateTableResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateTableResponse.

        表创建时间

        :param create_time: The create_time of this CreateTableResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def last_access_time(self):
        """Gets the last_access_time of this CreateTableResponse.

        最后访问时间

        :return: The last_access_time of this CreateTableResponse.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """Sets the last_access_time of this CreateTableResponse.

        最后访问时间

        :param last_access_time: The last_access_time of this CreateTableResponse.
        :type last_access_time: datetime
        """
        self._last_access_time = last_access_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateTableResponse.

        表元数据最后一次修改时间

        :return: The update_time of this CreateTableResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateTableResponse.

        表元数据最后一次修改时间

        :param update_time: The update_time of this CreateTableResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def last_analyzed_time(self):
        """Gets the last_analyzed_time of this CreateTableResponse.

        上一次做列级别的统计信息计算的时间

        :return: The last_analyzed_time of this CreateTableResponse.
        :rtype: datetime
        """
        return self._last_analyzed_time

    @last_analyzed_time.setter
    def last_analyzed_time(self, last_analyzed_time):
        """Sets the last_analyzed_time of this CreateTableResponse.

        上一次做列级别的统计信息计算的时间

        :param last_analyzed_time: The last_analyzed_time of this CreateTableResponse.
        :type last_analyzed_time: datetime
        """
        self._last_analyzed_time = last_analyzed_time

    @property
    def owner(self):
        """Gets the owner of this CreateTableResponse.

        用户信息

        :return: The owner of this CreateTableResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateTableResponse.

        用户信息

        :param owner: The owner of this CreateTableResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        """Gets the owner_type of this CreateTableResponse.

        用户类型

        :return: The owner_type of this CreateTableResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this CreateTableResponse.

        用户类型

        :param owner_type: The owner_type of this CreateTableResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def parameters(self):
        """Gets the parameters of this CreateTableResponse.

        参数

        :return: The parameters of this CreateTableResponse.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CreateTableResponse.

        参数

        :param parameters: The parameters of this CreateTableResponse.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def partition_keys(self):
        """Gets the partition_keys of this CreateTableResponse.

        表分区列的列表

        :return: The partition_keys of this CreateTableResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        return self._partition_keys

    @partition_keys.setter
    def partition_keys(self, partition_keys):
        """Sets the partition_keys of this CreateTableResponse.

        表分区列的列表

        :param partition_keys: The partition_keys of this CreateTableResponse.
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        self._partition_keys = partition_keys

    @property
    def retention(self):
        """Gets the retention of this CreateTableResponse.

        表保留时间

        :return: The retention of this CreateTableResponse.
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this CreateTableResponse.

        表保留时间

        :param retention: The retention of this CreateTableResponse.
        :type retention: int
        """
        self._retention = retention

    @property
    def storage_descriptor(self):
        """Gets the storage_descriptor of this CreateTableResponse.

        :return: The storage_descriptor of this CreateTableResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        return self._storage_descriptor

    @storage_descriptor.setter
    def storage_descriptor(self, storage_descriptor):
        """Sets the storage_descriptor of this CreateTableResponse.

        :param storage_descriptor: The storage_descriptor of this CreateTableResponse.
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        self._storage_descriptor = storage_descriptor

    @property
    def table_type(self):
        """Gets the table_type of this CreateTableResponse.

        表类型

        :return: The table_type of this CreateTableResponse.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this CreateTableResponse.

        表类型

        :param table_type: The table_type of this CreateTableResponse.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def comments(self):
        """Gets the comments of this CreateTableResponse.

        表描述信息

        :return: The comments of this CreateTableResponse.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CreateTableResponse.

        表描述信息

        :param comments: The comments of this CreateTableResponse.
        :type comments: str
        """
        self._comments = comments

    @property
    def view_expanded_text(self):
        """Gets the view_expanded_text of this CreateTableResponse.

        如果表是视图，则为视图的扩展文本；否则为 null

        :return: The view_expanded_text of this CreateTableResponse.
        :rtype: str
        """
        return self._view_expanded_text

    @view_expanded_text.setter
    def view_expanded_text(self, view_expanded_text):
        """Sets the view_expanded_text of this CreateTableResponse.

        如果表是视图，则为视图的扩展文本；否则为 null

        :param view_expanded_text: The view_expanded_text of this CreateTableResponse.
        :type view_expanded_text: str
        """
        self._view_expanded_text = view_expanded_text

    @property
    def view_original_text(self):
        """Gets the view_original_text of this CreateTableResponse.

        如果表是视图，则为视图的原始文本；否则为 null

        :return: The view_original_text of this CreateTableResponse.
        :rtype: str
        """
        return self._view_original_text

    @view_original_text.setter
    def view_original_text(self, view_original_text):
        """Sets the view_original_text of this CreateTableResponse.

        如果表是视图，则为视图的原始文本；否则为 null

        :param view_original_text: The view_original_text of this CreateTableResponse.
        :type view_original_text: str
        """
        self._view_original_text = view_original_text

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
        if not isinstance(other, CreateTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
