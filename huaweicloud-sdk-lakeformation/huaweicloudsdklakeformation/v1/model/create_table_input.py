# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTableInput:

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
        'table_format': 'str',
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
        'view_original_text': 'str',
        'ignore_obs_checked': 'bool',
        'data_statistic_enable': 'bool',
        'create_open_table_format_input': 'CreateOpenTableFormatInput'
    }

    attribute_map = {
        'table_name': 'table_name',
        'table_format': 'table_format',
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
        'view_original_text': 'view_original_text',
        'ignore_obs_checked': 'ignore_obs_checked',
        'data_statistic_enable': 'data_statistic_enable',
        'create_open_table_format_input': 'create_open_table_format_input'
    }

    def __init__(self, table_name=None, table_format=None, table_type=None, owner=None, owner_type=None, create_time=None, last_access_time=None, last_analyzed_time=None, partition_keys=None, retention=None, storage_descriptor=None, parameters=None, comments=None, view_expanded_text=None, view_original_text=None, ignore_obs_checked=None, data_statistic_enable=None, create_open_table_format_input=None):
        r"""CreateTableInput

        The model defined in huaweicloud sdk

        :param table_name: 表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。
        :type table_name: str
        :param table_format: 表格式，支持HIVE、ICEBERG、LANCE
        :type table_format: str
        :param table_type: 表类型，MANAGED_TABLE-内表、EXTERNAL_TABLE-外表、VIRTUAL_VIEW-视图、MATERIALIZED_VIEW-物化视图、DICTIONARY_TABLE-字典表、LAKE_TABLE-内表
        :type table_type: str
        :param owner: 表所有者。只能包含字母、数字和下划线，且长度为0~49个字符。可以为null。
        :type owner: str
        :param owner_type: 所有者类型，USER-用户、GROUP-组、ROLE-角色
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
        :param comments: 表描述信息。由用户创建表时输入，最大长度为4000个字符。
        :type comments: str
        :param view_expanded_text: 如果表是视图，则为视图的扩展文本；否则为 null
        :type view_expanded_text: str
        :param view_original_text: 如果表是视图，则为视图的原始文本；否则为 null
        :type view_original_text: str
        :param ignore_obs_checked: 是否忽略内表建表时对Obs路径的限制
        :type ignore_obs_checked: bool
        :param data_statistic_enable: 数据概况统计开关。默认状态为开，修改table开关状态后，还需检查所属database的开关状态。例如：table与所属database开关同时打开，则数据概况统计开启。否则关闭
        :type data_statistic_enable: bool
        :param create_open_table_format_input: 
        :type create_open_table_format_input: :class:`huaweicloudsdklakeformation.v1.CreateOpenTableFormatInput`
        """
        
        

        self._table_name = None
        self._table_format = None
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
        self._ignore_obs_checked = None
        self._data_statistic_enable = None
        self._create_open_table_format_input = None
        self.discriminator = None

        self.table_name = table_name
        if table_format is not None:
            self.table_format = table_format
        self.table_type = table_type
        if owner is not None:
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
        if ignore_obs_checked is not None:
            self.ignore_obs_checked = ignore_obs_checked
        if data_statistic_enable is not None:
            self.data_statistic_enable = data_statistic_enable
        if create_open_table_format_input is not None:
            self.create_open_table_format_input = create_open_table_format_input

    @property
    def table_name(self):
        r"""Gets the table_name of this CreateTableInput.

        表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。

        :return: The table_name of this CreateTableInput.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this CreateTableInput.

        表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。

        :param table_name: The table_name of this CreateTableInput.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_format(self):
        r"""Gets the table_format of this CreateTableInput.

        表格式，支持HIVE、ICEBERG、LANCE

        :return: The table_format of this CreateTableInput.
        :rtype: str
        """
        return self._table_format

    @table_format.setter
    def table_format(self, table_format):
        r"""Sets the table_format of this CreateTableInput.

        表格式，支持HIVE、ICEBERG、LANCE

        :param table_format: The table_format of this CreateTableInput.
        :type table_format: str
        """
        self._table_format = table_format

    @property
    def table_type(self):
        r"""Gets the table_type of this CreateTableInput.

        表类型，MANAGED_TABLE-内表、EXTERNAL_TABLE-外表、VIRTUAL_VIEW-视图、MATERIALIZED_VIEW-物化视图、DICTIONARY_TABLE-字典表、LAKE_TABLE-内表

        :return: The table_type of this CreateTableInput.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this CreateTableInput.

        表类型，MANAGED_TABLE-内表、EXTERNAL_TABLE-外表、VIRTUAL_VIEW-视图、MATERIALIZED_VIEW-物化视图、DICTIONARY_TABLE-字典表、LAKE_TABLE-内表

        :param table_type: The table_type of this CreateTableInput.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def owner(self):
        r"""Gets the owner of this CreateTableInput.

        表所有者。只能包含字母、数字和下划线，且长度为0~49个字符。可以为null。

        :return: The owner of this CreateTableInput.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CreateTableInput.

        表所有者。只能包含字母、数字和下划线，且长度为0~49个字符。可以为null。

        :param owner: The owner of this CreateTableInput.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        r"""Gets the owner_type of this CreateTableInput.

        所有者类型，USER-用户、GROUP-组、ROLE-角色

        :return: The owner_type of this CreateTableInput.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this CreateTableInput.

        所有者类型，USER-用户、GROUP-组、ROLE-角色

        :param owner_type: The owner_type of this CreateTableInput.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateTableInput.

        表创建时间

        :return: The create_time of this CreateTableInput.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateTableInput.

        表创建时间

        :param create_time: The create_time of this CreateTableInput.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def last_access_time(self):
        r"""Gets the last_access_time of this CreateTableInput.

        最近一次访问时间

        :return: The last_access_time of this CreateTableInput.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        r"""Sets the last_access_time of this CreateTableInput.

        最近一次访问时间

        :param last_access_time: The last_access_time of this CreateTableInput.
        :type last_access_time: datetime
        """
        self._last_access_time = last_access_time

    @property
    def last_analyzed_time(self):
        r"""Gets the last_analyzed_time of this CreateTableInput.

        最近一次分析统计时间

        :return: The last_analyzed_time of this CreateTableInput.
        :rtype: datetime
        """
        return self._last_analyzed_time

    @last_analyzed_time.setter
    def last_analyzed_time(self, last_analyzed_time):
        r"""Sets the last_analyzed_time of this CreateTableInput.

        最近一次分析统计时间

        :param last_analyzed_time: The last_analyzed_time of this CreateTableInput.
        :type last_analyzed_time: datetime
        """
        self._last_analyzed_time = last_analyzed_time

    @property
    def partition_keys(self):
        r"""Gets the partition_keys of this CreateTableInput.

        分区列的信息

        :return: The partition_keys of this CreateTableInput.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        return self._partition_keys

    @partition_keys.setter
    def partition_keys(self, partition_keys):
        r"""Sets the partition_keys of this CreateTableInput.

        分区列的信息

        :param partition_keys: The partition_keys of this CreateTableInput.
        :type partition_keys: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        self._partition_keys = partition_keys

    @property
    def retention(self):
        r"""Gets the retention of this CreateTableInput.

        表保留时间

        :return: The retention of this CreateTableInput.
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        r"""Sets the retention of this CreateTableInput.

        表保留时间

        :param retention: The retention of this CreateTableInput.
        :type retention: int
        """
        self._retention = retention

    @property
    def storage_descriptor(self):
        r"""Gets the storage_descriptor of this CreateTableInput.

        :return: The storage_descriptor of this CreateTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        return self._storage_descriptor

    @storage_descriptor.setter
    def storage_descriptor(self, storage_descriptor):
        r"""Sets the storage_descriptor of this CreateTableInput.

        :param storage_descriptor: The storage_descriptor of this CreateTableInput.
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        self._storage_descriptor = storage_descriptor

    @property
    def parameters(self):
        r"""Gets the parameters of this CreateTableInput.

        表参数信息，每个键是一个键字符串，不少于 1 个字节或超过 255 个字节 每个值是一个 UTF-8 字符串，不超过 4000 个字节

        :return: The parameters of this CreateTableInput.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CreateTableInput.

        表参数信息，每个键是一个键字符串，不少于 1 个字节或超过 255 个字节 每个值是一个 UTF-8 字符串，不超过 4000 个字节

        :param parameters: The parameters of this CreateTableInput.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def comments(self):
        r"""Gets the comments of this CreateTableInput.

        表描述信息。由用户创建表时输入，最大长度为4000个字符。

        :return: The comments of this CreateTableInput.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this CreateTableInput.

        表描述信息。由用户创建表时输入，最大长度为4000个字符。

        :param comments: The comments of this CreateTableInput.
        :type comments: str
        """
        self._comments = comments

    @property
    def view_expanded_text(self):
        r"""Gets the view_expanded_text of this CreateTableInput.

        如果表是视图，则为视图的扩展文本；否则为 null

        :return: The view_expanded_text of this CreateTableInput.
        :rtype: str
        """
        return self._view_expanded_text

    @view_expanded_text.setter
    def view_expanded_text(self, view_expanded_text):
        r"""Sets the view_expanded_text of this CreateTableInput.

        如果表是视图，则为视图的扩展文本；否则为 null

        :param view_expanded_text: The view_expanded_text of this CreateTableInput.
        :type view_expanded_text: str
        """
        self._view_expanded_text = view_expanded_text

    @property
    def view_original_text(self):
        r"""Gets the view_original_text of this CreateTableInput.

        如果表是视图，则为视图的原始文本；否则为 null

        :return: The view_original_text of this CreateTableInput.
        :rtype: str
        """
        return self._view_original_text

    @view_original_text.setter
    def view_original_text(self, view_original_text):
        r"""Sets the view_original_text of this CreateTableInput.

        如果表是视图，则为视图的原始文本；否则为 null

        :param view_original_text: The view_original_text of this CreateTableInput.
        :type view_original_text: str
        """
        self._view_original_text = view_original_text

    @property
    def ignore_obs_checked(self):
        r"""Gets the ignore_obs_checked of this CreateTableInput.

        是否忽略内表建表时对Obs路径的限制

        :return: The ignore_obs_checked of this CreateTableInput.
        :rtype: bool
        """
        return self._ignore_obs_checked

    @ignore_obs_checked.setter
    def ignore_obs_checked(self, ignore_obs_checked):
        r"""Sets the ignore_obs_checked of this CreateTableInput.

        是否忽略内表建表时对Obs路径的限制

        :param ignore_obs_checked: The ignore_obs_checked of this CreateTableInput.
        :type ignore_obs_checked: bool
        """
        self._ignore_obs_checked = ignore_obs_checked

    @property
    def data_statistic_enable(self):
        r"""Gets the data_statistic_enable of this CreateTableInput.

        数据概况统计开关。默认状态为开，修改table开关状态后，还需检查所属database的开关状态。例如：table与所属database开关同时打开，则数据概况统计开启。否则关闭

        :return: The data_statistic_enable of this CreateTableInput.
        :rtype: bool
        """
        return self._data_statistic_enable

    @data_statistic_enable.setter
    def data_statistic_enable(self, data_statistic_enable):
        r"""Sets the data_statistic_enable of this CreateTableInput.

        数据概况统计开关。默认状态为开，修改table开关状态后，还需检查所属database的开关状态。例如：table与所属database开关同时打开，则数据概况统计开启。否则关闭

        :param data_statistic_enable: The data_statistic_enable of this CreateTableInput.
        :type data_statistic_enable: bool
        """
        self._data_statistic_enable = data_statistic_enable

    @property
    def create_open_table_format_input(self):
        r"""Gets the create_open_table_format_input of this CreateTableInput.

        :return: The create_open_table_format_input of this CreateTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateOpenTableFormatInput`
        """
        return self._create_open_table_format_input

    @create_open_table_format_input.setter
    def create_open_table_format_input(self, create_open_table_format_input):
        r"""Sets the create_open_table_format_input of this CreateTableInput.

        :param create_open_table_format_input: The create_open_table_format_input of this CreateTableInput.
        :type create_open_table_format_input: :class:`huaweicloudsdklakeformation.v1.CreateOpenTableFormatInput`
        """
        self._create_open_table_format_input = create_open_table_format_input

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
        if not isinstance(other, CreateTableInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
