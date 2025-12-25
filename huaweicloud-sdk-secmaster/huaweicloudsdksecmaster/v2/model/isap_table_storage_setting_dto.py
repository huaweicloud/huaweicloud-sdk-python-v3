# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapTableStorageSettingDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_index': 'str',
        'application_topic': 'str',
        'application_data_class_id': 'str',
        'streaming_bandwidth': 'float',
        'streaming_partition': 'int',
        'streaming_dataspace_id': 'str',
        'index_storage_period': 'int',
        'index_storage_size': 'int',
        'index_shards': 'int',
        'lake_storage_period': 'int',
        'lake_partition_setting': 'str'
    }

    attribute_map = {
        'application_index': 'application_index',
        'application_topic': 'application_topic',
        'application_data_class_id': 'application_data_class_id',
        'streaming_bandwidth': 'streaming_bandwidth',
        'streaming_partition': 'streaming_partition',
        'streaming_dataspace_id': 'streaming_dataspace_id',
        'index_storage_period': 'index_storage_period',
        'index_storage_size': 'index_storage_size',
        'index_shards': 'index_shards',
        'lake_storage_period': 'lake_storage_period',
        'lake_partition_setting': 'lake_partition_setting'
    }

    def __init__(self, application_index=None, application_topic=None, application_data_class_id=None, streaming_bandwidth=None, streaming_partition=None, streaming_dataspace_id=None, index_storage_period=None, index_storage_size=None, index_shards=None, lake_storage_period=None, lake_partition_setting=None):
        r"""IsapTableStorageSettingDto

        The model defined in huaweicloud sdk

        :param application_index: 应用索引
        :type application_index: str
        :param application_topic: 应用主题
        :type application_topic: str
        :param application_data_class_id: 应用数据类ID
        :type application_data_class_id: str
        :param streaming_bandwidth: 流式带宽 MB/s
        :type streaming_bandwidth: float
        :param streaming_partition: 流式分区
        :type streaming_partition: int
        :param streaming_dataspace_id: 流式数据空间ID
        :type streaming_dataspace_id: str
        :param index_storage_period: 索引存储周期
        :type index_storage_period: int
        :param index_storage_size: 索引存储大小
        :type index_storage_size: int
        :param index_shards: 索引分片数
        :type index_shards: int
        :param lake_storage_period: 数据湖存储周期
        :type lake_storage_period: int
        :param lake_partition_setting: **参数解释**: 数据湖定时分区设置 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及    
        :type lake_partition_setting: str
        """
        
        

        self._application_index = None
        self._application_topic = None
        self._application_data_class_id = None
        self._streaming_bandwidth = None
        self._streaming_partition = None
        self._streaming_dataspace_id = None
        self._index_storage_period = None
        self._index_storage_size = None
        self._index_shards = None
        self._lake_storage_period = None
        self._lake_partition_setting = None
        self.discriminator = None

        if application_index is not None:
            self.application_index = application_index
        if application_topic is not None:
            self.application_topic = application_topic
        if application_data_class_id is not None:
            self.application_data_class_id = application_data_class_id
        if streaming_bandwidth is not None:
            self.streaming_bandwidth = streaming_bandwidth
        if streaming_partition is not None:
            self.streaming_partition = streaming_partition
        if streaming_dataspace_id is not None:
            self.streaming_dataspace_id = streaming_dataspace_id
        if index_storage_period is not None:
            self.index_storage_period = index_storage_period
        if index_storage_size is not None:
            self.index_storage_size = index_storage_size
        if index_shards is not None:
            self.index_shards = index_shards
        if lake_storage_period is not None:
            self.lake_storage_period = lake_storage_period
        if lake_partition_setting is not None:
            self.lake_partition_setting = lake_partition_setting

    @property
    def application_index(self):
        r"""Gets the application_index of this IsapTableStorageSettingDto.

        应用索引

        :return: The application_index of this IsapTableStorageSettingDto.
        :rtype: str
        """
        return self._application_index

    @application_index.setter
    def application_index(self, application_index):
        r"""Sets the application_index of this IsapTableStorageSettingDto.

        应用索引

        :param application_index: The application_index of this IsapTableStorageSettingDto.
        :type application_index: str
        """
        self._application_index = application_index

    @property
    def application_topic(self):
        r"""Gets the application_topic of this IsapTableStorageSettingDto.

        应用主题

        :return: The application_topic of this IsapTableStorageSettingDto.
        :rtype: str
        """
        return self._application_topic

    @application_topic.setter
    def application_topic(self, application_topic):
        r"""Sets the application_topic of this IsapTableStorageSettingDto.

        应用主题

        :param application_topic: The application_topic of this IsapTableStorageSettingDto.
        :type application_topic: str
        """
        self._application_topic = application_topic

    @property
    def application_data_class_id(self):
        r"""Gets the application_data_class_id of this IsapTableStorageSettingDto.

        应用数据类ID

        :return: The application_data_class_id of this IsapTableStorageSettingDto.
        :rtype: str
        """
        return self._application_data_class_id

    @application_data_class_id.setter
    def application_data_class_id(self, application_data_class_id):
        r"""Sets the application_data_class_id of this IsapTableStorageSettingDto.

        应用数据类ID

        :param application_data_class_id: The application_data_class_id of this IsapTableStorageSettingDto.
        :type application_data_class_id: str
        """
        self._application_data_class_id = application_data_class_id

    @property
    def streaming_bandwidth(self):
        r"""Gets the streaming_bandwidth of this IsapTableStorageSettingDto.

        流式带宽 MB/s

        :return: The streaming_bandwidth of this IsapTableStorageSettingDto.
        :rtype: float
        """
        return self._streaming_bandwidth

    @streaming_bandwidth.setter
    def streaming_bandwidth(self, streaming_bandwidth):
        r"""Sets the streaming_bandwidth of this IsapTableStorageSettingDto.

        流式带宽 MB/s

        :param streaming_bandwidth: The streaming_bandwidth of this IsapTableStorageSettingDto.
        :type streaming_bandwidth: float
        """
        self._streaming_bandwidth = streaming_bandwidth

    @property
    def streaming_partition(self):
        r"""Gets the streaming_partition of this IsapTableStorageSettingDto.

        流式分区

        :return: The streaming_partition of this IsapTableStorageSettingDto.
        :rtype: int
        """
        return self._streaming_partition

    @streaming_partition.setter
    def streaming_partition(self, streaming_partition):
        r"""Sets the streaming_partition of this IsapTableStorageSettingDto.

        流式分区

        :param streaming_partition: The streaming_partition of this IsapTableStorageSettingDto.
        :type streaming_partition: int
        """
        self._streaming_partition = streaming_partition

    @property
    def streaming_dataspace_id(self):
        r"""Gets the streaming_dataspace_id of this IsapTableStorageSettingDto.

        流式数据空间ID

        :return: The streaming_dataspace_id of this IsapTableStorageSettingDto.
        :rtype: str
        """
        return self._streaming_dataspace_id

    @streaming_dataspace_id.setter
    def streaming_dataspace_id(self, streaming_dataspace_id):
        r"""Sets the streaming_dataspace_id of this IsapTableStorageSettingDto.

        流式数据空间ID

        :param streaming_dataspace_id: The streaming_dataspace_id of this IsapTableStorageSettingDto.
        :type streaming_dataspace_id: str
        """
        self._streaming_dataspace_id = streaming_dataspace_id

    @property
    def index_storage_period(self):
        r"""Gets the index_storage_period of this IsapTableStorageSettingDto.

        索引存储周期

        :return: The index_storage_period of this IsapTableStorageSettingDto.
        :rtype: int
        """
        return self._index_storage_period

    @index_storage_period.setter
    def index_storage_period(self, index_storage_period):
        r"""Sets the index_storage_period of this IsapTableStorageSettingDto.

        索引存储周期

        :param index_storage_period: The index_storage_period of this IsapTableStorageSettingDto.
        :type index_storage_period: int
        """
        self._index_storage_period = index_storage_period

    @property
    def index_storage_size(self):
        r"""Gets the index_storage_size of this IsapTableStorageSettingDto.

        索引存储大小

        :return: The index_storage_size of this IsapTableStorageSettingDto.
        :rtype: int
        """
        return self._index_storage_size

    @index_storage_size.setter
    def index_storage_size(self, index_storage_size):
        r"""Sets the index_storage_size of this IsapTableStorageSettingDto.

        索引存储大小

        :param index_storage_size: The index_storage_size of this IsapTableStorageSettingDto.
        :type index_storage_size: int
        """
        self._index_storage_size = index_storage_size

    @property
    def index_shards(self):
        r"""Gets the index_shards of this IsapTableStorageSettingDto.

        索引分片数

        :return: The index_shards of this IsapTableStorageSettingDto.
        :rtype: int
        """
        return self._index_shards

    @index_shards.setter
    def index_shards(self, index_shards):
        r"""Sets the index_shards of this IsapTableStorageSettingDto.

        索引分片数

        :param index_shards: The index_shards of this IsapTableStorageSettingDto.
        :type index_shards: int
        """
        self._index_shards = index_shards

    @property
    def lake_storage_period(self):
        r"""Gets the lake_storage_period of this IsapTableStorageSettingDto.

        数据湖存储周期

        :return: The lake_storage_period of this IsapTableStorageSettingDto.
        :rtype: int
        """
        return self._lake_storage_period

    @lake_storage_period.setter
    def lake_storage_period(self, lake_storage_period):
        r"""Sets the lake_storage_period of this IsapTableStorageSettingDto.

        数据湖存储周期

        :param lake_storage_period: The lake_storage_period of this IsapTableStorageSettingDto.
        :type lake_storage_period: int
        """
        self._lake_storage_period = lake_storage_period

    @property
    def lake_partition_setting(self):
        r"""Gets the lake_partition_setting of this IsapTableStorageSettingDto.

        **参数解释**: 数据湖定时分区设置 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及    

        :return: The lake_partition_setting of this IsapTableStorageSettingDto.
        :rtype: str
        """
        return self._lake_partition_setting

    @lake_partition_setting.setter
    def lake_partition_setting(self, lake_partition_setting):
        r"""Sets the lake_partition_setting of this IsapTableStorageSettingDto.

        **参数解释**: 数据湖定时分区设置 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及    

        :param lake_partition_setting: The lake_partition_setting of this IsapTableStorageSettingDto.
        :type lake_partition_setting: str
        """
        self._lake_partition_setting = lake_partition_setting

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
        if not isinstance(other, IsapTableStorageSettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
