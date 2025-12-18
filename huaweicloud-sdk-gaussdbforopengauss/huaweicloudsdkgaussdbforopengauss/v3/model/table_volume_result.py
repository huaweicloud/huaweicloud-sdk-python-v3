# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableVolumeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_size': 'str',
        'id': 'str',
        'table_name': 'str',
        'table_owner': 'str',
        'schema_name': 'str',
        'database_name': 'str',
        'is_part_type': 'bool',
        'is_hash_cluster_key': 'bool',
        'tuples': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'average_size': 'str',
        'max_ratio': 'str',
        'min_ratio': 'str',
        'skew_size': 'str',
        'skew_ratio': 'str',
        'skew_stddev': 'str'
    }

    attribute_map = {
        'table_size': 'table_size',
        'id': 'id',
        'table_name': 'table_name',
        'table_owner': 'table_owner',
        'schema_name': 'schema_name',
        'database_name': 'database_name',
        'is_part_type': 'is_part_type',
        'is_hash_cluster_key': 'is_hash_cluster_key',
        'tuples': 'tuples',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'average_size': 'average_size',
        'max_ratio': 'max_ratio',
        'min_ratio': 'min_ratio',
        'skew_size': 'skew_size',
        'skew_ratio': 'skew_ratio',
        'skew_stddev': 'skew_stddev'
    }

    def __init__(self, table_size=None, id=None, table_name=None, table_owner=None, schema_name=None, database_name=None, is_part_type=None, is_hash_cluster_key=None, tuples=None, create_time=None, update_time=None, average_size=None, max_ratio=None, min_ratio=None, skew_size=None, skew_ratio=None, skew_stddev=None):
        r"""TableVolumeResult

        The model defined in huaweicloud sdk

        :param table_size: **参数解释**: 表的大小。 **取值范围**: 不涉及。 
        :type table_size: str
        :param id: **参数解释**: 表ID。 **取值范围**: 不涉及。 
        :type id: str
        :param table_name: **参数解释**: 表名称。 **取值范围**: 不涉及。 
        :type table_name: str
        :param table_owner: **参数解释**: 表所属用户名称。 **取值范围**: 不涉及。 
        :type table_owner: str
        :param schema_name: **参数解释**: schema名称。 **取值范围**: 不涉及。 
        :type schema_name: str
        :param database_name: **参数解释**: 数据库名称。 **取值范围**: 不涉及。 
        :type database_name: str
        :param is_part_type: **参数解释**: 表或者索引是否具有分区表的性质。 **取值范围**: 不涉及。 
        :type is_part_type: bool
        :param is_hash_cluster_key: **参数解释**: 是否包含hash分区列信息。 **取值范围**: 不涉及。 
        :type is_hash_cluster_key: bool
        :param tuples: **参数解释**: 表中行的数目。 **取值范围**: 不涉及。 
        :type tuples: str
        :param create_time: **参数解释**: 创建时间。 **取值范围**: 不涉及。 
        :type create_time: str
        :param update_time: **参数解释**: 修改时间。 **取值范围**: 不涉及。 
        :type update_time: str
        :param average_size: **参数解释**: 表大小平均值(totalsize/DN个数，该值为平均分布的理想情况下，表在各DN占用空间大小)。 **取值范围**: 不涉及。 
        :type average_size: str
        :param max_ratio: **参数解释**: 单DN表大小最大值占比（表在各DN占用空间的最大值/totalsize）。 **取值范围**: 不涉及。 
        :type max_ratio: str
        :param min_ratio: **参数解释**: 单DN表大小最小值占比（表在各DN占用空间的最小值/totalsize）。 **取值范围**: 不涉及。 
        :type min_ratio: str
        :param skew_size: **参数解释**: 表分布倾斜值（单DN表大小最大值 - 单DN表大小最小值）。 **取值范围**: 不涉及。 
        :type skew_size: str
        :param skew_ratio: **参数解释**: 表分布倾斜率（skewsize/totalsize）。 **取值范围**: 不涉及。 
        :type skew_ratio: str
        :param skew_stddev: **参数解释**: 表分布标准方差（在表大小一定的情况下，该值越大表明表的整体分布情况越倾斜）。。 **取值范围**: 不涉及。 
        :type skew_stddev: str
        """
        
        

        self._table_size = None
        self._id = None
        self._table_name = None
        self._table_owner = None
        self._schema_name = None
        self._database_name = None
        self._is_part_type = None
        self._is_hash_cluster_key = None
        self._tuples = None
        self._create_time = None
        self._update_time = None
        self._average_size = None
        self._max_ratio = None
        self._min_ratio = None
        self._skew_size = None
        self._skew_ratio = None
        self._skew_stddev = None
        self.discriminator = None

        if table_size is not None:
            self.table_size = table_size
        if id is not None:
            self.id = id
        if table_name is not None:
            self.table_name = table_name
        if table_owner is not None:
            self.table_owner = table_owner
        if schema_name is not None:
            self.schema_name = schema_name
        if database_name is not None:
            self.database_name = database_name
        if is_part_type is not None:
            self.is_part_type = is_part_type
        if is_hash_cluster_key is not None:
            self.is_hash_cluster_key = is_hash_cluster_key
        if tuples is not None:
            self.tuples = tuples
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if average_size is not None:
            self.average_size = average_size
        if max_ratio is not None:
            self.max_ratio = max_ratio
        if min_ratio is not None:
            self.min_ratio = min_ratio
        if skew_size is not None:
            self.skew_size = skew_size
        if skew_ratio is not None:
            self.skew_ratio = skew_ratio
        if skew_stddev is not None:
            self.skew_stddev = skew_stddev

    @property
    def table_size(self):
        r"""Gets the table_size of this TableVolumeResult.

        **参数解释**: 表的大小。 **取值范围**: 不涉及。 

        :return: The table_size of this TableVolumeResult.
        :rtype: str
        """
        return self._table_size

    @table_size.setter
    def table_size(self, table_size):
        r"""Sets the table_size of this TableVolumeResult.

        **参数解释**: 表的大小。 **取值范围**: 不涉及。 

        :param table_size: The table_size of this TableVolumeResult.
        :type table_size: str
        """
        self._table_size = table_size

    @property
    def id(self):
        r"""Gets the id of this TableVolumeResult.

        **参数解释**: 表ID。 **取值范围**: 不涉及。 

        :return: The id of this TableVolumeResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TableVolumeResult.

        **参数解释**: 表ID。 **取值范围**: 不涉及。 

        :param id: The id of this TableVolumeResult.
        :type id: str
        """
        self._id = id

    @property
    def table_name(self):
        r"""Gets the table_name of this TableVolumeResult.

        **参数解释**: 表名称。 **取值范围**: 不涉及。 

        :return: The table_name of this TableVolumeResult.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this TableVolumeResult.

        **参数解释**: 表名称。 **取值范围**: 不涉及。 

        :param table_name: The table_name of this TableVolumeResult.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_owner(self):
        r"""Gets the table_owner of this TableVolumeResult.

        **参数解释**: 表所属用户名称。 **取值范围**: 不涉及。 

        :return: The table_owner of this TableVolumeResult.
        :rtype: str
        """
        return self._table_owner

    @table_owner.setter
    def table_owner(self, table_owner):
        r"""Sets the table_owner of this TableVolumeResult.

        **参数解释**: 表所属用户名称。 **取值范围**: 不涉及。 

        :param table_owner: The table_owner of this TableVolumeResult.
        :type table_owner: str
        """
        self._table_owner = table_owner

    @property
    def schema_name(self):
        r"""Gets the schema_name of this TableVolumeResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。 

        :return: The schema_name of this TableVolumeResult.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this TableVolumeResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。 

        :param schema_name: The schema_name of this TableVolumeResult.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def database_name(self):
        r"""Gets the database_name of this TableVolumeResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。 

        :return: The database_name of this TableVolumeResult.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this TableVolumeResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。 

        :param database_name: The database_name of this TableVolumeResult.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def is_part_type(self):
        r"""Gets the is_part_type of this TableVolumeResult.

        **参数解释**: 表或者索引是否具有分区表的性质。 **取值范围**: 不涉及。 

        :return: The is_part_type of this TableVolumeResult.
        :rtype: bool
        """
        return self._is_part_type

    @is_part_type.setter
    def is_part_type(self, is_part_type):
        r"""Sets the is_part_type of this TableVolumeResult.

        **参数解释**: 表或者索引是否具有分区表的性质。 **取值范围**: 不涉及。 

        :param is_part_type: The is_part_type of this TableVolumeResult.
        :type is_part_type: bool
        """
        self._is_part_type = is_part_type

    @property
    def is_hash_cluster_key(self):
        r"""Gets the is_hash_cluster_key of this TableVolumeResult.

        **参数解释**: 是否包含hash分区列信息。 **取值范围**: 不涉及。 

        :return: The is_hash_cluster_key of this TableVolumeResult.
        :rtype: bool
        """
        return self._is_hash_cluster_key

    @is_hash_cluster_key.setter
    def is_hash_cluster_key(self, is_hash_cluster_key):
        r"""Sets the is_hash_cluster_key of this TableVolumeResult.

        **参数解释**: 是否包含hash分区列信息。 **取值范围**: 不涉及。 

        :param is_hash_cluster_key: The is_hash_cluster_key of this TableVolumeResult.
        :type is_hash_cluster_key: bool
        """
        self._is_hash_cluster_key = is_hash_cluster_key

    @property
    def tuples(self):
        r"""Gets the tuples of this TableVolumeResult.

        **参数解释**: 表中行的数目。 **取值范围**: 不涉及。 

        :return: The tuples of this TableVolumeResult.
        :rtype: str
        """
        return self._tuples

    @tuples.setter
    def tuples(self, tuples):
        r"""Sets the tuples of this TableVolumeResult.

        **参数解释**: 表中行的数目。 **取值范围**: 不涉及。 

        :param tuples: The tuples of this TableVolumeResult.
        :type tuples: str
        """
        self._tuples = tuples

    @property
    def create_time(self):
        r"""Gets the create_time of this TableVolumeResult.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。 

        :return: The create_time of this TableVolumeResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TableVolumeResult.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。 

        :param create_time: The create_time of this TableVolumeResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TableVolumeResult.

        **参数解释**: 修改时间。 **取值范围**: 不涉及。 

        :return: The update_time of this TableVolumeResult.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TableVolumeResult.

        **参数解释**: 修改时间。 **取值范围**: 不涉及。 

        :param update_time: The update_time of this TableVolumeResult.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def average_size(self):
        r"""Gets the average_size of this TableVolumeResult.

        **参数解释**: 表大小平均值(totalsize/DN个数，该值为平均分布的理想情况下，表在各DN占用空间大小)。 **取值范围**: 不涉及。 

        :return: The average_size of this TableVolumeResult.
        :rtype: str
        """
        return self._average_size

    @average_size.setter
    def average_size(self, average_size):
        r"""Sets the average_size of this TableVolumeResult.

        **参数解释**: 表大小平均值(totalsize/DN个数，该值为平均分布的理想情况下，表在各DN占用空间大小)。 **取值范围**: 不涉及。 

        :param average_size: The average_size of this TableVolumeResult.
        :type average_size: str
        """
        self._average_size = average_size

    @property
    def max_ratio(self):
        r"""Gets the max_ratio of this TableVolumeResult.

        **参数解释**: 单DN表大小最大值占比（表在各DN占用空间的最大值/totalsize）。 **取值范围**: 不涉及。 

        :return: The max_ratio of this TableVolumeResult.
        :rtype: str
        """
        return self._max_ratio

    @max_ratio.setter
    def max_ratio(self, max_ratio):
        r"""Sets the max_ratio of this TableVolumeResult.

        **参数解释**: 单DN表大小最大值占比（表在各DN占用空间的最大值/totalsize）。 **取值范围**: 不涉及。 

        :param max_ratio: The max_ratio of this TableVolumeResult.
        :type max_ratio: str
        """
        self._max_ratio = max_ratio

    @property
    def min_ratio(self):
        r"""Gets the min_ratio of this TableVolumeResult.

        **参数解释**: 单DN表大小最小值占比（表在各DN占用空间的最小值/totalsize）。 **取值范围**: 不涉及。 

        :return: The min_ratio of this TableVolumeResult.
        :rtype: str
        """
        return self._min_ratio

    @min_ratio.setter
    def min_ratio(self, min_ratio):
        r"""Sets the min_ratio of this TableVolumeResult.

        **参数解释**: 单DN表大小最小值占比（表在各DN占用空间的最小值/totalsize）。 **取值范围**: 不涉及。 

        :param min_ratio: The min_ratio of this TableVolumeResult.
        :type min_ratio: str
        """
        self._min_ratio = min_ratio

    @property
    def skew_size(self):
        r"""Gets the skew_size of this TableVolumeResult.

        **参数解释**: 表分布倾斜值（单DN表大小最大值 - 单DN表大小最小值）。 **取值范围**: 不涉及。 

        :return: The skew_size of this TableVolumeResult.
        :rtype: str
        """
        return self._skew_size

    @skew_size.setter
    def skew_size(self, skew_size):
        r"""Sets the skew_size of this TableVolumeResult.

        **参数解释**: 表分布倾斜值（单DN表大小最大值 - 单DN表大小最小值）。 **取值范围**: 不涉及。 

        :param skew_size: The skew_size of this TableVolumeResult.
        :type skew_size: str
        """
        self._skew_size = skew_size

    @property
    def skew_ratio(self):
        r"""Gets the skew_ratio of this TableVolumeResult.

        **参数解释**: 表分布倾斜率（skewsize/totalsize）。 **取值范围**: 不涉及。 

        :return: The skew_ratio of this TableVolumeResult.
        :rtype: str
        """
        return self._skew_ratio

    @skew_ratio.setter
    def skew_ratio(self, skew_ratio):
        r"""Sets the skew_ratio of this TableVolumeResult.

        **参数解释**: 表分布倾斜率（skewsize/totalsize）。 **取值范围**: 不涉及。 

        :param skew_ratio: The skew_ratio of this TableVolumeResult.
        :type skew_ratio: str
        """
        self._skew_ratio = skew_ratio

    @property
    def skew_stddev(self):
        r"""Gets the skew_stddev of this TableVolumeResult.

        **参数解释**: 表分布标准方差（在表大小一定的情况下，该值越大表明表的整体分布情况越倾斜）。。 **取值范围**: 不涉及。 

        :return: The skew_stddev of this TableVolumeResult.
        :rtype: str
        """
        return self._skew_stddev

    @skew_stddev.setter
    def skew_stddev(self, skew_stddev):
        r"""Sets the skew_stddev of this TableVolumeResult.

        **参数解释**: 表分布标准方差（在表大小一定的情况下，该值越大表明表的整体分布情况越倾斜）。。 **取值范围**: 不涉及。 

        :param skew_stddev: The skew_stddev of this TableVolumeResult.
        :type skew_stddev: str
        """
        self._skew_stddev = skew_stddev

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
        if not isinstance(other, TableVolumeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
