# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipeStorageSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'streaming_bandwidth': 'float',
        'streaming_dataspace_id': 'str',
        'index_storage_period': 'int',
        'index_storage_size': 'int',
        'index_shards': 'int',
        'data_transformation_cu': 'float',
        'lake_storage_period': 'int'
    }

    attribute_map = {
        'streaming_bandwidth': 'streaming_bandwidth',
        'streaming_dataspace_id': 'streaming_dataspace_id',
        'index_storage_period': 'index_storage_period',
        'index_storage_size': 'index_storage_size',
        'index_shards': 'index_shards',
        'data_transformation_cu': 'data_transformation_cu',
        'lake_storage_period': 'lake_storage_period'
    }

    def __init__(self, streaming_bandwidth=None, streaming_dataspace_id=None, index_storage_period=None, index_storage_size=None, index_shards=None, data_transformation_cu=None, lake_storage_period=None):
        r"""PipeStorageSetting

        The model defined in huaweicloud sdk

        :param streaming_bandwidth: Bandwidth in MB/s
        :type streaming_bandwidth: float
        :param streaming_dataspace_id: UUID
        :type streaming_dataspace_id: str
        :param index_storage_period: 索引存储周期
        :type index_storage_period: int
        :param index_storage_size: 索引存储容量，单位：GB
        :type index_storage_size: int
        :param index_shards: 索引分区数
        :type index_shards: int
        :param data_transformation_cu: 数据转换CU
        :type data_transformation_cu: float
        :param lake_storage_period: Index shards
        :type lake_storage_period: int
        """
        
        

        self._streaming_bandwidth = None
        self._streaming_dataspace_id = None
        self._index_storage_period = None
        self._index_storage_size = None
        self._index_shards = None
        self._data_transformation_cu = None
        self._lake_storage_period = None
        self.discriminator = None

        if streaming_bandwidth is not None:
            self.streaming_bandwidth = streaming_bandwidth
        self.streaming_dataspace_id = streaming_dataspace_id
        if index_storage_period is not None:
            self.index_storage_period = index_storage_period
        if index_storage_size is not None:
            self.index_storage_size = index_storage_size
        if index_shards is not None:
            self.index_shards = index_shards
        if data_transformation_cu is not None:
            self.data_transformation_cu = data_transformation_cu
        if lake_storage_period is not None:
            self.lake_storage_period = lake_storage_period

    @property
    def streaming_bandwidth(self):
        r"""Gets the streaming_bandwidth of this PipeStorageSetting.

        Bandwidth in MB/s

        :return: The streaming_bandwidth of this PipeStorageSetting.
        :rtype: float
        """
        return self._streaming_bandwidth

    @streaming_bandwidth.setter
    def streaming_bandwidth(self, streaming_bandwidth):
        r"""Sets the streaming_bandwidth of this PipeStorageSetting.

        Bandwidth in MB/s

        :param streaming_bandwidth: The streaming_bandwidth of this PipeStorageSetting.
        :type streaming_bandwidth: float
        """
        self._streaming_bandwidth = streaming_bandwidth

    @property
    def streaming_dataspace_id(self):
        r"""Gets the streaming_dataspace_id of this PipeStorageSetting.

        UUID

        :return: The streaming_dataspace_id of this PipeStorageSetting.
        :rtype: str
        """
        return self._streaming_dataspace_id

    @streaming_dataspace_id.setter
    def streaming_dataspace_id(self, streaming_dataspace_id):
        r"""Sets the streaming_dataspace_id of this PipeStorageSetting.

        UUID

        :param streaming_dataspace_id: The streaming_dataspace_id of this PipeStorageSetting.
        :type streaming_dataspace_id: str
        """
        self._streaming_dataspace_id = streaming_dataspace_id

    @property
    def index_storage_period(self):
        r"""Gets the index_storage_period of this PipeStorageSetting.

        索引存储周期

        :return: The index_storage_period of this PipeStorageSetting.
        :rtype: int
        """
        return self._index_storage_period

    @index_storage_period.setter
    def index_storage_period(self, index_storage_period):
        r"""Sets the index_storage_period of this PipeStorageSetting.

        索引存储周期

        :param index_storage_period: The index_storage_period of this PipeStorageSetting.
        :type index_storage_period: int
        """
        self._index_storage_period = index_storage_period

    @property
    def index_storage_size(self):
        r"""Gets the index_storage_size of this PipeStorageSetting.

        索引存储容量，单位：GB

        :return: The index_storage_size of this PipeStorageSetting.
        :rtype: int
        """
        return self._index_storage_size

    @index_storage_size.setter
    def index_storage_size(self, index_storage_size):
        r"""Sets the index_storage_size of this PipeStorageSetting.

        索引存储容量，单位：GB

        :param index_storage_size: The index_storage_size of this PipeStorageSetting.
        :type index_storage_size: int
        """
        self._index_storage_size = index_storage_size

    @property
    def index_shards(self):
        r"""Gets the index_shards of this PipeStorageSetting.

        索引分区数

        :return: The index_shards of this PipeStorageSetting.
        :rtype: int
        """
        return self._index_shards

    @index_shards.setter
    def index_shards(self, index_shards):
        r"""Sets the index_shards of this PipeStorageSetting.

        索引分区数

        :param index_shards: The index_shards of this PipeStorageSetting.
        :type index_shards: int
        """
        self._index_shards = index_shards

    @property
    def data_transformation_cu(self):
        r"""Gets the data_transformation_cu of this PipeStorageSetting.

        数据转换CU

        :return: The data_transformation_cu of this PipeStorageSetting.
        :rtype: float
        """
        return self._data_transformation_cu

    @data_transformation_cu.setter
    def data_transformation_cu(self, data_transformation_cu):
        r"""Sets the data_transformation_cu of this PipeStorageSetting.

        数据转换CU

        :param data_transformation_cu: The data_transformation_cu of this PipeStorageSetting.
        :type data_transformation_cu: float
        """
        self._data_transformation_cu = data_transformation_cu

    @property
    def lake_storage_period(self):
        r"""Gets the lake_storage_period of this PipeStorageSetting.

        Index shards

        :return: The lake_storage_period of this PipeStorageSetting.
        :rtype: int
        """
        return self._lake_storage_period

    @lake_storage_period.setter
    def lake_storage_period(self, lake_storage_period):
        r"""Sets the lake_storage_period of this PipeStorageSetting.

        Index shards

        :param lake_storage_period: The lake_storage_period of this PipeStorageSetting.
        :type lake_storage_period: int
        """
        self._lake_storage_period = lake_storage_period

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
        if not isinstance(other, PipeStorageSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
