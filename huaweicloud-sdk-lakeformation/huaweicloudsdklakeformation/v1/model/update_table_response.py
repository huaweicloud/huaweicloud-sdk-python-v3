# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTableResponse(SdkResponse):

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
        r"""UpdateTableResponse

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
        
        super(UpdateTableResponse, self).__init__()

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
        r"""Gets the catalog_name of this UpdateTableResponse.

        catalog名字

        :return: The catalog_name of this UpdateTableResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this UpdateTableResponse.

        catalog名字

        :param catalog_name: The catalog_name of this UpdateTableResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this UpdateTableResponse.

        数据库名字

        :return: The database_name of this UpdateTableResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this UpdateTableResponse.

        数据库名字

        :param database_name: The database_name of this UpdateTableResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this UpdateTableResponse.

        表名字

        :return: The table_name of this UpdateTableResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this UpdateTableResponse.

        表名字

        :param table_name: The table_name of this UpdateTableResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateTableResponse.

        表创建时间

        :return: The create_time of this UpdateTableResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateTableResponse.

        表创建时间

        :param create_time: The create_time of this UpdateTableResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def last_access_time(self):
        r"""Gets the last_access_time of this UpdateTableResponse.

        最后访问时间

        :return: The last_access_time of this UpdateTableResponse.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        r"""Sets the last_access_time of this UpdateTableResponse.

        最后访问时间

        :param last_access_time: The last_access_time of this UpdateTableResponse.
        :type last_access_time: datetime
        """
        self._last_access_time = last_access_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateTableResponse.

        表元数据最后一次修改时间

        :return: The update_time of this UpdateTableResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateTableResponse.

        表元数据最后一次修改时间

        :param update_time: The update_time of this UpdateTableResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def last_analyzed_time(self):
        r"""Gets the last_analyzed_time of this UpdateTableResponse.

        上一次做列级别的统计信息计算的时间

        :return: The last_analyzed_time of this UpdateTableResponse.
        :rtype: datetime
        """
        return self._last_analyzed_time

    @last_analyzed_time.setter
    def last_analyzed_time(self, last_analyzed_time):
        r"""Sets the last_analyzed_time of this UpdateTableResponse.

        上一次做列级别的统计信息计算的时间

        :param last_analyzed_time: The last_analyzed_time of this UpdateTableResponse.
        :type last_analyzed_time: datetime
        """
        self._last_analyzed_time = last_analyzed_time

    @property
    def owner(self):
        r"""Gets the owner of this UpdateTableResponse.

        用户信息

        :return: The owner of this UpdateTableResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this UpdateTableResponse.

        用户信息

        :param owner: The owner of this UpdateTableResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        r"""Gets the owner_type of this UpdateTableResponse.

        用户类型

        :return: The owner_type of this UpdateTableResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this UpdateTableResponse.

        用户类型

        :param owner_type: The owner_type of this UpdateTableResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def parameters(self):
        r"""Gets the parameters of this UpdateTableResponse.

        参数

        :return: The parameters of this UpdateTableResponse.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this UpdateTableResponse.

        参数

        :param parameters: The parameters of this UpdateTableResponse.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def partition_keys(self):
        r"""Gets the partition_keys of this UpdateTableResponse.

        表分区列的列表

        :return: The partition_keys of this UpdateTableResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        return self._partition_keys

    @partition_keys.setter
    def partition_keys(self, partition_keys):
        r"""Sets the partition_keys of this UpdateTableResponse.

        表分区列的列表

        :param partition_keys: The partition_keys of this UpdateTableResponse.
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        self._partition_keys = partition_keys

    @property
    def retention(self):
        r"""Gets the retention of this UpdateTableResponse.

        表保留时间

        :return: The retention of this UpdateTableResponse.
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        r"""Sets the retention of this UpdateTableResponse.

        表保留时间

        :param retention: The retention of this UpdateTableResponse.
        :type retention: int
        """
        self._retention = retention

    @property
    def storage_descriptor(self):
        r"""Gets the storage_descriptor of this UpdateTableResponse.

        :return: The storage_descriptor of this UpdateTableResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        return self._storage_descriptor

    @storage_descriptor.setter
    def storage_descriptor(self, storage_descriptor):
        r"""Sets the storage_descriptor of this UpdateTableResponse.

        :param storage_descriptor: The storage_descriptor of this UpdateTableResponse.
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        self._storage_descriptor = storage_descriptor

    @property
    def table_type(self):
        r"""Gets the table_type of this UpdateTableResponse.

        表类型

        :return: The table_type of this UpdateTableResponse.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this UpdateTableResponse.

        表类型

        :param table_type: The table_type of this UpdateTableResponse.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def comments(self):
        r"""Gets the comments of this UpdateTableResponse.

        表描述信息

        :return: The comments of this UpdateTableResponse.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this UpdateTableResponse.

        表描述信息

        :param comments: The comments of this UpdateTableResponse.
        :type comments: str
        """
        self._comments = comments

    @property
    def view_expanded_text(self):
        r"""Gets the view_expanded_text of this UpdateTableResponse.

        如果表是视图，则为视图的扩展文本；否则为 null

        :return: The view_expanded_text of this UpdateTableResponse.
        :rtype: str
        """
        return self._view_expanded_text

    @view_expanded_text.setter
    def view_expanded_text(self, view_expanded_text):
        r"""Sets the view_expanded_text of this UpdateTableResponse.

        如果表是视图，则为视图的扩展文本；否则为 null

        :param view_expanded_text: The view_expanded_text of this UpdateTableResponse.
        :type view_expanded_text: str
        """
        self._view_expanded_text = view_expanded_text

    @property
    def view_original_text(self):
        r"""Gets the view_original_text of this UpdateTableResponse.

        如果表是视图，则为视图的原始文本；否则为 null

        :return: The view_original_text of this UpdateTableResponse.
        :rtype: str
        """
        return self._view_original_text

    @view_original_text.setter
    def view_original_text(self, view_original_text):
        r"""Sets the view_original_text of this UpdateTableResponse.

        如果表是视图，则为视图的原始文本；否则为 null

        :param view_original_text: The view_original_text of this UpdateTableResponse.
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
        if not isinstance(other, UpdateTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
