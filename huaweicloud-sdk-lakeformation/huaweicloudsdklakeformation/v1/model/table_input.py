# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'table_type': 'str',
        'owner': 'str',
        'owner_type': 'str',
        'create_time': 'datetime',
        'last_access_time': 'datetime',
        'last_analyzed_time': 'datetime',
        'partition_keys': 'list[Column]',
        'retention': 'int',
        'storage_descriptor': 'StorageDescriptor',
        'parameters': 'dict(str, str)',
        'comments': 'str',
        'view_expanded_text': 'str',
        'view_original_text': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'table_type': 'table_type',
        'owner': 'owner',
        'owner_type': 'owner_type',
        'create_time': 'create_time',
        'last_access_time': 'last_access_time',
        'last_analyzed_time': 'last_analyzed_time',
        'partition_keys': 'partition_keys',
        'retention': 'retention',
        'storage_descriptor': 'storage_descriptor',
        'parameters': 'parameters',
        'comments': 'comments',
        'view_expanded_text': 'view_expanded_text',
        'view_original_text': 'view_original_text'
    }

    def __init__(self, table_name=None, table_type=None, owner=None, owner_type=None, create_time=None, last_access_time=None, last_analyzed_time=None, partition_keys=None, retention=None, storage_descriptor=None, parameters=None, comments=None, view_expanded_text=None, view_original_text=None):
        """TableInput

        The model defined in huaweicloud sdk

        :param table_name: 表名字
        :type table_name: str
        :param table_type: 表类型
        :type table_type: str
        :param owner: 表所有者
        :type owner: str
        :param owner_type: 所有者类型
        :type owner_type: str
        :param create_time: 表创建时间
        :type create_time: datetime
        :param last_access_time: 最近一次访问时间
        :type last_access_time: datetime
        :param last_analyzed_time: 最近一次分析统计时间
        :type last_analyzed_time: datetime
        :param partition_keys: 分区列的信息
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        :param retention: 表保留时间
        :type retention: int
        :param storage_descriptor: 
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        :param parameters: 表参数信息，每个键是一个键字符串，不少于 1 个字节或超过 255 个字节 每个值是一个 UTF-8 字符串，不超过 4000 个字节
        :type parameters: dict(str, str)
        :param comments: 表描述信息
        :type comments: str
        :param view_expanded_text: 如果表是视图，则为视图的扩展文本；否则为 null
        :type view_expanded_text: str
        :param view_original_text: 如果表是视图，则为视图的原始文本；否则为 null
        :type view_original_text: str
        """
        
        

        self._table_name = None
        self._table_type = None
        self._owner = None
        self._owner_type = None
        self._create_time = None
        self._last_access_time = None
        self._last_analyzed_time = None
        self._partition_keys = None
        self._retention = None
        self._storage_descriptor = None
        self._parameters = None
        self._comments = None
        self._view_expanded_text = None
        self._view_original_text = None
        self.discriminator = None

        self.table_name = table_name
        self.table_type = table_type
        self.owner = owner
        self.owner_type = owner_type
        if create_time is not None:
            self.create_time = create_time
        if last_access_time is not None:
            self.last_access_time = last_access_time
        if last_analyzed_time is not None:
            self.last_analyzed_time = last_analyzed_time
        if partition_keys is not None:
            self.partition_keys = partition_keys
        if retention is not None:
            self.retention = retention
        self.storage_descriptor = storage_descriptor
        if parameters is not None:
            self.parameters = parameters
        if comments is not None:
            self.comments = comments
        if view_expanded_text is not None:
            self.view_expanded_text = view_expanded_text
        if view_original_text is not None:
            self.view_original_text = view_original_text

    @property
    def table_name(self):
        """Gets the table_name of this TableInput.

        表名字

        :return: The table_name of this TableInput.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this TableInput.

        表名字

        :param table_name: The table_name of this TableInput.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_type(self):
        """Gets the table_type of this TableInput.

        表类型

        :return: The table_type of this TableInput.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this TableInput.

        表类型

        :param table_type: The table_type of this TableInput.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def owner(self):
        """Gets the owner of this TableInput.

        表所有者

        :return: The owner of this TableInput.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TableInput.

        表所有者

        :param owner: The owner of this TableInput.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        """Gets the owner_type of this TableInput.

        所有者类型

        :return: The owner_type of this TableInput.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this TableInput.

        所有者类型

        :param owner_type: The owner_type of this TableInput.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def create_time(self):
        """Gets the create_time of this TableInput.

        表创建时间

        :return: The create_time of this TableInput.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TableInput.

        表创建时间

        :param create_time: The create_time of this TableInput.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def last_access_time(self):
        """Gets the last_access_time of this TableInput.

        最近一次访问时间

        :return: The last_access_time of this TableInput.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """Sets the last_access_time of this TableInput.

        最近一次访问时间

        :param last_access_time: The last_access_time of this TableInput.
        :type last_access_time: datetime
        """
        self._last_access_time = last_access_time

    @property
    def last_analyzed_time(self):
        """Gets the last_analyzed_time of this TableInput.

        最近一次分析统计时间

        :return: The last_analyzed_time of this TableInput.
        :rtype: datetime
        """
        return self._last_analyzed_time

    @last_analyzed_time.setter
    def last_analyzed_time(self, last_analyzed_time):
        """Sets the last_analyzed_time of this TableInput.

        最近一次分析统计时间

        :param last_analyzed_time: The last_analyzed_time of this TableInput.
        :type last_analyzed_time: datetime
        """
        self._last_analyzed_time = last_analyzed_time

    @property
    def partition_keys(self):
        """Gets the partition_keys of this TableInput.

        分区列的信息

        :return: The partition_keys of this TableInput.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        return self._partition_keys

    @partition_keys.setter
    def partition_keys(self, partition_keys):
        """Sets the partition_keys of this TableInput.

        分区列的信息

        :param partition_keys: The partition_keys of this TableInput.
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        self._partition_keys = partition_keys

    @property
    def retention(self):
        """Gets the retention of this TableInput.

        表保留时间

        :return: The retention of this TableInput.
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this TableInput.

        表保留时间

        :param retention: The retention of this TableInput.
        :type retention: int
        """
        self._retention = retention

    @property
    def storage_descriptor(self):
        """Gets the storage_descriptor of this TableInput.

        :return: The storage_descriptor of this TableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        return self._storage_descriptor

    @storage_descriptor.setter
    def storage_descriptor(self, storage_descriptor):
        """Sets the storage_descriptor of this TableInput.

        :param storage_descriptor: The storage_descriptor of this TableInput.
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        self._storage_descriptor = storage_descriptor

    @property
    def parameters(self):
        """Gets the parameters of this TableInput.

        表参数信息，每个键是一个键字符串，不少于 1 个字节或超过 255 个字节 每个值是一个 UTF-8 字符串，不超过 4000 个字节

        :return: The parameters of this TableInput.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this TableInput.

        表参数信息，每个键是一个键字符串，不少于 1 个字节或超过 255 个字节 每个值是一个 UTF-8 字符串，不超过 4000 个字节

        :param parameters: The parameters of this TableInput.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def comments(self):
        """Gets the comments of this TableInput.

        表描述信息

        :return: The comments of this TableInput.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TableInput.

        表描述信息

        :param comments: The comments of this TableInput.
        :type comments: str
        """
        self._comments = comments

    @property
    def view_expanded_text(self):
        """Gets the view_expanded_text of this TableInput.

        如果表是视图，则为视图的扩展文本；否则为 null

        :return: The view_expanded_text of this TableInput.
        :rtype: str
        """
        return self._view_expanded_text

    @view_expanded_text.setter
    def view_expanded_text(self, view_expanded_text):
        """Sets the view_expanded_text of this TableInput.

        如果表是视图，则为视图的扩展文本；否则为 null

        :param view_expanded_text: The view_expanded_text of this TableInput.
        :type view_expanded_text: str
        """
        self._view_expanded_text = view_expanded_text

    @property
    def view_original_text(self):
        """Gets the view_original_text of this TableInput.

        如果表是视图，则为视图的原始文本；否则为 null

        :return: The view_original_text of this TableInput.
        :rtype: str
        """
        return self._view_original_text

    @view_original_text.setter
    def view_original_text(self, view_original_text):
        """Sets the view_original_text of this TableInput.

        如果表是视图，则为视图的原始文本；否则为 null

        :param view_original_text: The view_original_text of this TableInput.
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
        if not isinstance(other, TableInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
