# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_transformation_cu': 'float',
        'index_replicas': 'int',
        'index_shards': 'int',
        'index_storage_period': 'int',
        'index_storage_size': 'int',
        'lake_storage_period': 'int',
        'streaming_bandwidth': 'float',
        'streaming_dataspace_id': 'str',
        'streaming_partition': 'int',
        'streaming_retention_size': 'int',
        'streaming_retention_time': 'int'
    }

    attribute_map = {
        'data_transformation_cu': 'data_transformation_cu',
        'index_replicas': 'index_replicas',
        'index_shards': 'index_shards',
        'index_storage_period': 'index_storage_period',
        'index_storage_size': 'index_storage_size',
        'lake_storage_period': 'lake_storage_period',
        'streaming_bandwidth': 'streaming_bandwidth',
        'streaming_dataspace_id': 'streaming_dataspace_id',
        'streaming_partition': 'streaming_partition',
        'streaming_retention_size': 'streaming_retention_size',
        'streaming_retention_time': 'streaming_retention_time'
    }

    def __init__(self, data_transformation_cu=None, index_replicas=None, index_shards=None, index_storage_period=None, index_storage_size=None, lake_storage_period=None, streaming_bandwidth=None, streaming_dataspace_id=None, streaming_partition=None, streaming_retention_size=None, streaming_retention_time=None):
        r"""StorageSetting

        The model defined in huaweicloud sdk

        :param data_transformation_cu: 数据转换 CU
        :type data_transformation_cu: float
        :param index_replicas: 索引副本数
        :type index_replicas: int
        :param index_shards: 索引分片数
        :type index_shards: int
        :param index_storage_period: 索引存储周期
        :type index_storage_period: int
        :param index_storage_size: 索引存储大小
        :type index_storage_size: int
        :param lake_storage_period: 湖存储周期
        :type lake_storage_period: int
        :param streaming_bandwidth: 流式带宽
        :type streaming_bandwidth: float
        :param streaming_dataspace_id: 流式数据空间ID
        :type streaming_dataspace_id: str
        :param streaming_partition: 流式分区数
        :type streaming_partition: int
        :param streaming_retention_size: 流式保留大小
        :type streaming_retention_size: int
        :param streaming_retention_time: 流式保留时间
        :type streaming_retention_time: int
        """
        
        

        self._data_transformation_cu = None
        self._index_replicas = None
        self._index_shards = None
        self._index_storage_period = None
        self._index_storage_size = None
        self._lake_storage_period = None
        self._streaming_bandwidth = None
        self._streaming_dataspace_id = None
        self._streaming_partition = None
        self._streaming_retention_size = None
        self._streaming_retention_time = None
        self.discriminator = None

        if data_transformation_cu is not None:
            self.data_transformation_cu = data_transformation_cu
        if index_replicas is not None:
            self.index_replicas = index_replicas
        if index_shards is not None:
            self.index_shards = index_shards
        if index_storage_period is not None:
            self.index_storage_period = index_storage_period
        if index_storage_size is not None:
            self.index_storage_size = index_storage_size
        if lake_storage_period is not None:
            self.lake_storage_period = lake_storage_period
        if streaming_bandwidth is not None:
            self.streaming_bandwidth = streaming_bandwidth
        if streaming_dataspace_id is not None:
            self.streaming_dataspace_id = streaming_dataspace_id
        if streaming_partition is not None:
            self.streaming_partition = streaming_partition
        if streaming_retention_size is not None:
            self.streaming_retention_size = streaming_retention_size
        if streaming_retention_time is not None:
            self.streaming_retention_time = streaming_retention_time

    @property
    def data_transformation_cu(self):
        r"""Gets the data_transformation_cu of this StorageSetting.

        数据转换 CU

        :return: The data_transformation_cu of this StorageSetting.
        :rtype: float
        """
        return self._data_transformation_cu

    @data_transformation_cu.setter
    def data_transformation_cu(self, data_transformation_cu):
        r"""Sets the data_transformation_cu of this StorageSetting.

        数据转换 CU

        :param data_transformation_cu: The data_transformation_cu of this StorageSetting.
        :type data_transformation_cu: float
        """
        self._data_transformation_cu = data_transformation_cu

    @property
    def index_replicas(self):
        r"""Gets the index_replicas of this StorageSetting.

        索引副本数

        :return: The index_replicas of this StorageSetting.
        :rtype: int
        """
        return self._index_replicas

    @index_replicas.setter
    def index_replicas(self, index_replicas):
        r"""Sets the index_replicas of this StorageSetting.

        索引副本数

        :param index_replicas: The index_replicas of this StorageSetting.
        :type index_replicas: int
        """
        self._index_replicas = index_replicas

    @property
    def index_shards(self):
        r"""Gets the index_shards of this StorageSetting.

        索引分片数

        :return: The index_shards of this StorageSetting.
        :rtype: int
        """
        return self._index_shards

    @index_shards.setter
    def index_shards(self, index_shards):
        r"""Sets the index_shards of this StorageSetting.

        索引分片数

        :param index_shards: The index_shards of this StorageSetting.
        :type index_shards: int
        """
        self._index_shards = index_shards

    @property
    def index_storage_period(self):
        r"""Gets the index_storage_period of this StorageSetting.

        索引存储周期

        :return: The index_storage_period of this StorageSetting.
        :rtype: int
        """
        return self._index_storage_period

    @index_storage_period.setter
    def index_storage_period(self, index_storage_period):
        r"""Sets the index_storage_period of this StorageSetting.

        索引存储周期

        :param index_storage_period: The index_storage_period of this StorageSetting.
        :type index_storage_period: int
        """
        self._index_storage_period = index_storage_period

    @property
    def index_storage_size(self):
        r"""Gets the index_storage_size of this StorageSetting.

        索引存储大小

        :return: The index_storage_size of this StorageSetting.
        :rtype: int
        """
        return self._index_storage_size

    @index_storage_size.setter
    def index_storage_size(self, index_storage_size):
        r"""Sets the index_storage_size of this StorageSetting.

        索引存储大小

        :param index_storage_size: The index_storage_size of this StorageSetting.
        :type index_storage_size: int
        """
        self._index_storage_size = index_storage_size

    @property
    def lake_storage_period(self):
        r"""Gets the lake_storage_period of this StorageSetting.

        湖存储周期

        :return: The lake_storage_period of this StorageSetting.
        :rtype: int
        """
        return self._lake_storage_period

    @lake_storage_period.setter
    def lake_storage_period(self, lake_storage_period):
        r"""Sets the lake_storage_period of this StorageSetting.

        湖存储周期

        :param lake_storage_period: The lake_storage_period of this StorageSetting.
        :type lake_storage_period: int
        """
        self._lake_storage_period = lake_storage_period

    @property
    def streaming_bandwidth(self):
        r"""Gets the streaming_bandwidth of this StorageSetting.

        流式带宽

        :return: The streaming_bandwidth of this StorageSetting.
        :rtype: float
        """
        return self._streaming_bandwidth

    @streaming_bandwidth.setter
    def streaming_bandwidth(self, streaming_bandwidth):
        r"""Sets the streaming_bandwidth of this StorageSetting.

        流式带宽

        :param streaming_bandwidth: The streaming_bandwidth of this StorageSetting.
        :type streaming_bandwidth: float
        """
        self._streaming_bandwidth = streaming_bandwidth

    @property
    def streaming_dataspace_id(self):
        r"""Gets the streaming_dataspace_id of this StorageSetting.

        流式数据空间ID

        :return: The streaming_dataspace_id of this StorageSetting.
        :rtype: str
        """
        return self._streaming_dataspace_id

    @streaming_dataspace_id.setter
    def streaming_dataspace_id(self, streaming_dataspace_id):
        r"""Sets the streaming_dataspace_id of this StorageSetting.

        流式数据空间ID

        :param streaming_dataspace_id: The streaming_dataspace_id of this StorageSetting.
        :type streaming_dataspace_id: str
        """
        self._streaming_dataspace_id = streaming_dataspace_id

    @property
    def streaming_partition(self):
        r"""Gets the streaming_partition of this StorageSetting.

        流式分区数

        :return: The streaming_partition of this StorageSetting.
        :rtype: int
        """
        return self._streaming_partition

    @streaming_partition.setter
    def streaming_partition(self, streaming_partition):
        r"""Sets the streaming_partition of this StorageSetting.

        流式分区数

        :param streaming_partition: The streaming_partition of this StorageSetting.
        :type streaming_partition: int
        """
        self._streaming_partition = streaming_partition

    @property
    def streaming_retention_size(self):
        r"""Gets the streaming_retention_size of this StorageSetting.

        流式保留大小

        :return: The streaming_retention_size of this StorageSetting.
        :rtype: int
        """
        return self._streaming_retention_size

    @streaming_retention_size.setter
    def streaming_retention_size(self, streaming_retention_size):
        r"""Sets the streaming_retention_size of this StorageSetting.

        流式保留大小

        :param streaming_retention_size: The streaming_retention_size of this StorageSetting.
        :type streaming_retention_size: int
        """
        self._streaming_retention_size = streaming_retention_size

    @property
    def streaming_retention_time(self):
        r"""Gets the streaming_retention_time of this StorageSetting.

        流式保留时间

        :return: The streaming_retention_time of this StorageSetting.
        :rtype: int
        """
        return self._streaming_retention_time

    @streaming_retention_time.setter
    def streaming_retention_time(self, streaming_retention_time):
        r"""Sets the streaming_retention_time of this StorageSetting.

        流式保留时间

        :param streaming_retention_time: The streaming_retention_time of this StorageSetting.
        :type streaming_retention_time: int
        """
        self._streaming_retention_time = streaming_retention_time

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
        if not isinstance(other, StorageSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
