# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubscriptionResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'sku': 'str',
        'upper_limit': 'float',
        'unit': 'str',
        'step': 'float',
        'used_amount': 'float',
        'unused_amount': 'float',
        'version': 'int',
        'create_time': 'int',
        'update_time': 'int',
        'index_storage_upper_limit': 'int',
        'index_shards_upper_limit': 'int',
        'index_shards_unused': 'int',
        'partitions_unused': 'int',
        'partition_upper_limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'sku': 'sku',
        'upper_limit': 'upper_limit',
        'unit': 'unit',
        'step': 'step',
        'used_amount': 'used_amount',
        'unused_amount': 'unused_amount',
        'version': 'version',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'index_storage_upper_limit': 'index_storage_upper_limit',
        'index_shards_upper_limit': 'index_shards_upper_limit',
        'index_shards_unused': 'index_shards_unused',
        'partitions_unused': 'partitions_unused',
        'partition_upper_limit': 'partition_upper_limit'
    }

    def __init__(self, project_id=None, sku=None, upper_limit=None, unit=None, step=None, used_amount=None, unused_amount=None, version=None, create_time=None, update_time=None, index_storage_upper_limit=None, index_shards_upper_limit=None, index_shards_unused=None, partitions_unused=None, partition_upper_limit=None):
        r"""ShowSubscriptionResourcesResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param sku: **参数解释**: sku类型 - FLOW_DATA_BANDWIDTH 数据带宽 - CSS_CAPACITY 索引集群容量 - PAIMON_CAPACITY 数据库容量 - OBS_CAPACITY 对象存储容量 - JOB_CAPACITY 作业容量 - AD_HOC_COUNT 即席查询数量  **约束限制** 不涉及 **取值范围**: - FLOW_DATA_BANDWIDTH - CSS_CAPACITY - PAIMON_CAPACITY - OBS_CAPACITY - JOB_CAPACITY - AD_HOC_COUNT  **默认值** 不涉及      
        :type sku: str
        :param upper_limit: 资源上限值
        :type upper_limit: float
        :param unit: 配额单位（如 GB、条、分片等）
        :type unit: str
        :param step: 配额步长
        :type step: float
        :param used_amount: 已使用的资源数量
        :type used_amount: float
        :param unused_amount: 剩余可用的资源数量
        :type unused_amount: float
        :param version: 版本号
        :type version: int
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param index_storage_upper_limit: 索引存储上限
        :type index_storage_upper_limit: int
        :param index_shards_upper_limit: 索引分片上限
        :type index_shards_upper_limit: int
        :param index_shards_unused: 剩余可用索引分片数量
        :type index_shards_unused: int
        :param partitions_unused: 剩余可用分区数量
        :type partitions_unused: int
        :param partition_upper_limit: 分区上限
        :type partition_upper_limit: int
        """
        
        super().__init__()

        self._project_id = None
        self._sku = None
        self._upper_limit = None
        self._unit = None
        self._step = None
        self._used_amount = None
        self._unused_amount = None
        self._version = None
        self._create_time = None
        self._update_time = None
        self._index_storage_upper_limit = None
        self._index_shards_upper_limit = None
        self._index_shards_unused = None
        self._partitions_unused = None
        self._partition_upper_limit = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if sku is not None:
            self.sku = sku
        if upper_limit is not None:
            self.upper_limit = upper_limit
        if unit is not None:
            self.unit = unit
        if step is not None:
            self.step = step
        if used_amount is not None:
            self.used_amount = used_amount
        if unused_amount is not None:
            self.unused_amount = unused_amount
        if version is not None:
            self.version = version
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if index_storage_upper_limit is not None:
            self.index_storage_upper_limit = index_storage_upper_limit
        if index_shards_upper_limit is not None:
            self.index_shards_upper_limit = index_shards_upper_limit
        if index_shards_unused is not None:
            self.index_shards_unused = index_shards_unused
        if partitions_unused is not None:
            self.partitions_unused = partitions_unused
        if partition_upper_limit is not None:
            self.partition_upper_limit = partition_upper_limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowSubscriptionResourcesResponse.

        项目ID

        :return: The project_id of this ShowSubscriptionResourcesResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowSubscriptionResourcesResponse.

        项目ID

        :param project_id: The project_id of this ShowSubscriptionResourcesResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def sku(self):
        r"""Gets the sku of this ShowSubscriptionResourcesResponse.

        **参数解释**: sku类型 - FLOW_DATA_BANDWIDTH 数据带宽 - CSS_CAPACITY 索引集群容量 - PAIMON_CAPACITY 数据库容量 - OBS_CAPACITY 对象存储容量 - JOB_CAPACITY 作业容量 - AD_HOC_COUNT 即席查询数量  **约束限制** 不涉及 **取值范围**: - FLOW_DATA_BANDWIDTH - CSS_CAPACITY - PAIMON_CAPACITY - OBS_CAPACITY - JOB_CAPACITY - AD_HOC_COUNT  **默认值** 不涉及      

        :return: The sku of this ShowSubscriptionResourcesResponse.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        r"""Sets the sku of this ShowSubscriptionResourcesResponse.

        **参数解释**: sku类型 - FLOW_DATA_BANDWIDTH 数据带宽 - CSS_CAPACITY 索引集群容量 - PAIMON_CAPACITY 数据库容量 - OBS_CAPACITY 对象存储容量 - JOB_CAPACITY 作业容量 - AD_HOC_COUNT 即席查询数量  **约束限制** 不涉及 **取值范围**: - FLOW_DATA_BANDWIDTH - CSS_CAPACITY - PAIMON_CAPACITY - OBS_CAPACITY - JOB_CAPACITY - AD_HOC_COUNT  **默认值** 不涉及      

        :param sku: The sku of this ShowSubscriptionResourcesResponse.
        :type sku: str
        """
        self._sku = sku

    @property
    def upper_limit(self):
        r"""Gets the upper_limit of this ShowSubscriptionResourcesResponse.

        资源上限值

        :return: The upper_limit of this ShowSubscriptionResourcesResponse.
        :rtype: float
        """
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, upper_limit):
        r"""Sets the upper_limit of this ShowSubscriptionResourcesResponse.

        资源上限值

        :param upper_limit: The upper_limit of this ShowSubscriptionResourcesResponse.
        :type upper_limit: float
        """
        self._upper_limit = upper_limit

    @property
    def unit(self):
        r"""Gets the unit of this ShowSubscriptionResourcesResponse.

        配额单位（如 GB、条、分片等）

        :return: The unit of this ShowSubscriptionResourcesResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ShowSubscriptionResourcesResponse.

        配额单位（如 GB、条、分片等）

        :param unit: The unit of this ShowSubscriptionResourcesResponse.
        :type unit: str
        """
        self._unit = unit

    @property
    def step(self):
        r"""Gets the step of this ShowSubscriptionResourcesResponse.

        配额步长

        :return: The step of this ShowSubscriptionResourcesResponse.
        :rtype: float
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ShowSubscriptionResourcesResponse.

        配额步长

        :param step: The step of this ShowSubscriptionResourcesResponse.
        :type step: float
        """
        self._step = step

    @property
    def used_amount(self):
        r"""Gets the used_amount of this ShowSubscriptionResourcesResponse.

        已使用的资源数量

        :return: The used_amount of this ShowSubscriptionResourcesResponse.
        :rtype: float
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        r"""Sets the used_amount of this ShowSubscriptionResourcesResponse.

        已使用的资源数量

        :param used_amount: The used_amount of this ShowSubscriptionResourcesResponse.
        :type used_amount: float
        """
        self._used_amount = used_amount

    @property
    def unused_amount(self):
        r"""Gets the unused_amount of this ShowSubscriptionResourcesResponse.

        剩余可用的资源数量

        :return: The unused_amount of this ShowSubscriptionResourcesResponse.
        :rtype: float
        """
        return self._unused_amount

    @unused_amount.setter
    def unused_amount(self, unused_amount):
        r"""Sets the unused_amount of this ShowSubscriptionResourcesResponse.

        剩余可用的资源数量

        :param unused_amount: The unused_amount of this ShowSubscriptionResourcesResponse.
        :type unused_amount: float
        """
        self._unused_amount = unused_amount

    @property
    def version(self):
        r"""Gets the version of this ShowSubscriptionResourcesResponse.

        版本号

        :return: The version of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowSubscriptionResourcesResponse.

        版本号

        :param version: The version of this ShowSubscriptionResourcesResponse.
        :type version: int
        """
        self._version = version

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSubscriptionResourcesResponse.

        毫秒时间戳

        :return: The create_time of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSubscriptionResourcesResponse.

        毫秒时间戳

        :param create_time: The create_time of this ShowSubscriptionResourcesResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowSubscriptionResourcesResponse.

        毫秒时间戳

        :return: The update_time of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowSubscriptionResourcesResponse.

        毫秒时间戳

        :param update_time: The update_time of this ShowSubscriptionResourcesResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def index_storage_upper_limit(self):
        r"""Gets the index_storage_upper_limit of this ShowSubscriptionResourcesResponse.

        索引存储上限

        :return: The index_storage_upper_limit of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._index_storage_upper_limit

    @index_storage_upper_limit.setter
    def index_storage_upper_limit(self, index_storage_upper_limit):
        r"""Sets the index_storage_upper_limit of this ShowSubscriptionResourcesResponse.

        索引存储上限

        :param index_storage_upper_limit: The index_storage_upper_limit of this ShowSubscriptionResourcesResponse.
        :type index_storage_upper_limit: int
        """
        self._index_storage_upper_limit = index_storage_upper_limit

    @property
    def index_shards_upper_limit(self):
        r"""Gets the index_shards_upper_limit of this ShowSubscriptionResourcesResponse.

        索引分片上限

        :return: The index_shards_upper_limit of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._index_shards_upper_limit

    @index_shards_upper_limit.setter
    def index_shards_upper_limit(self, index_shards_upper_limit):
        r"""Sets the index_shards_upper_limit of this ShowSubscriptionResourcesResponse.

        索引分片上限

        :param index_shards_upper_limit: The index_shards_upper_limit of this ShowSubscriptionResourcesResponse.
        :type index_shards_upper_limit: int
        """
        self._index_shards_upper_limit = index_shards_upper_limit

    @property
    def index_shards_unused(self):
        r"""Gets the index_shards_unused of this ShowSubscriptionResourcesResponse.

        剩余可用索引分片数量

        :return: The index_shards_unused of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._index_shards_unused

    @index_shards_unused.setter
    def index_shards_unused(self, index_shards_unused):
        r"""Sets the index_shards_unused of this ShowSubscriptionResourcesResponse.

        剩余可用索引分片数量

        :param index_shards_unused: The index_shards_unused of this ShowSubscriptionResourcesResponse.
        :type index_shards_unused: int
        """
        self._index_shards_unused = index_shards_unused

    @property
    def partitions_unused(self):
        r"""Gets the partitions_unused of this ShowSubscriptionResourcesResponse.

        剩余可用分区数量

        :return: The partitions_unused of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._partitions_unused

    @partitions_unused.setter
    def partitions_unused(self, partitions_unused):
        r"""Sets the partitions_unused of this ShowSubscriptionResourcesResponse.

        剩余可用分区数量

        :param partitions_unused: The partitions_unused of this ShowSubscriptionResourcesResponse.
        :type partitions_unused: int
        """
        self._partitions_unused = partitions_unused

    @property
    def partition_upper_limit(self):
        r"""Gets the partition_upper_limit of this ShowSubscriptionResourcesResponse.

        分区上限

        :return: The partition_upper_limit of this ShowSubscriptionResourcesResponse.
        :rtype: int
        """
        return self._partition_upper_limit

    @partition_upper_limit.setter
    def partition_upper_limit(self, partition_upper_limit):
        r"""Sets the partition_upper_limit of this ShowSubscriptionResourcesResponse.

        分区上限

        :param partition_upper_limit: The partition_upper_limit of this ShowSubscriptionResourcesResponse.
        :type partition_upper_limit: int
        """
        self._partition_upper_limit = partition_upper_limit

    def to_dict(self):
        import warnings
        warnings.warn("ShowSubscriptionResourcesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSubscriptionResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
