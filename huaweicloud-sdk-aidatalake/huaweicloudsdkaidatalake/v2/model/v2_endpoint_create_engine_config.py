# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2EndpointCreateEngineConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'spark_config': 'dict(str, str)',
        'scheduling_config': 'SparkSchedulingConfig',
        'staging_config': 'AuraV2StagingConfig',
        'image': 'V2ImageBriefInfoAdmin',
        'cluster_config': 'RayClusterConfigV3',
        'max_endpoint_concurrent_queries': 'int',
        'history_server_config': 'HistoryServerConfig',
        'redis_config': 'RedisConfig',
        'storages_config': 'CreateStoragesConfig',
        'flink_config': 'dict(str, str)',
        'expand_cpu_resource': 'bool',
        'worker_group_config': 'list[WorkerGroupConfig]',
        'serve_config': 'ServeConfig',
        'data_infos': 'list[DataInfo]'
    }

    attribute_map = {
        'type': 'type',
        'spark_config': 'spark_config',
        'scheduling_config': 'scheduling_config',
        'staging_config': 'staging_config',
        'image': 'image',
        'cluster_config': 'cluster_config',
        'max_endpoint_concurrent_queries': 'max_endpoint_concurrent_queries',
        'history_server_config': 'history_server_config',
        'redis_config': 'redis_config',
        'storages_config': 'storages_config',
        'flink_config': 'flink_config',
        'expand_cpu_resource': 'expand_cpu_resource',
        'worker_group_config': 'worker_group_config',
        'serve_config': 'serve_config',
        'data_infos': 'data_infos'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, type=None, spark_config=None, scheduling_config=None, staging_config=None, image=None, cluster_config=None, max_endpoint_concurrent_queries=None, history_server_config=None, redis_config=None, storages_config=None, flink_config=None, expand_cpu_resource=None, worker_group_config=None, serve_config=None, data_infos=None):
        r"""V2EndpointCreateEngineConfig

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayService。 **默认取值**：不涉及。 
        :type type: str
        :param spark_config: **参数解释**：SparkSql参数配置。 **约束限制**：最大数量为100。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type spark_config: dict(str, str)
        :param scheduling_config: 
        :type scheduling_config: :class:`huaweicloudsdkaidatalake.v2.SparkSchedulingConfig`
        :param staging_config: 
        :type staging_config: :class:`huaweicloudsdkaidatalake.v2.AuraV2StagingConfig`
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        :param cluster_config: 
        :type cluster_config: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        :param max_endpoint_concurrent_queries: **参数解释**：端点最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：300。 
        :type max_endpoint_concurrent_queries: int
        :param history_server_config: 
        :type history_server_config: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        :param redis_config: 
        :type redis_config: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        :param storages_config: 
        :type storages_config: :class:`huaweicloudsdkaidatalake.v2.CreateStoragesConfig`
        :param flink_config: **参数解释**：Flink参数配置，Map的key为Flink配置参数名，value为对应的参数值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flink_config: dict(str, str)
        :param expand_cpu_resource: **参数解释**：开启后，通算工作组作业能够使用智算工作组空闲CPU及内存资源，该操作可能会导致智算任务因资源不足而排队。 **约束限制**：不涉及。 **取值范围**：   - true：开启通算工作组作业使用智算工作组空闲CPU及内存资源。   - false：关闭通算工作组作业使用智算工作组空闲CPU及内存资源。 **默认取值**：false。
        :type expand_cpu_resource: bool
        :param worker_group_config: **参数解释**：工作组补充配置，和外部capacity对应。 **约束限制**：最多10个。
        :type worker_group_config: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupConfig`]
        :param serve_config: 
        :type serve_config: :class:`huaweicloudsdkaidatalake.v2.ServeConfig`
        :param data_infos: **参数解释**：模型信息列表（可选）。模型可以打包在镜像中（通过 working_dir 配置项指定），也可以通过此字段上传模型地址。创建时如果模型已预置在镜像中，可省略此字段；更新时如果模型没有变化，也可以不填。 **约束限制**：不涉及。
        :type data_infos: list[:class:`huaweicloudsdkaidatalake.v2.DataInfo`]
        """
        
        

        self._type = None
        self._spark_config = None
        self._scheduling_config = None
        self._staging_config = None
        self._image = None
        self._cluster_config = None
        self._max_endpoint_concurrent_queries = None
        self._history_server_config = None
        self._redis_config = None
        self._storages_config = None
        self._flink_config = None
        self._expand_cpu_resource = None
        self._worker_group_config = None
        self._serve_config = None
        self._data_infos = None
        self.discriminator = 'type'

        if type is not None:
            self.type = type
        if spark_config is not None:
            self.spark_config = spark_config
        if scheduling_config is not None:
            self.scheduling_config = scheduling_config
        self.staging_config = staging_config
        self.image = image
        self.cluster_config = cluster_config
        if max_endpoint_concurrent_queries is not None:
            self.max_endpoint_concurrent_queries = max_endpoint_concurrent_queries
        if history_server_config is not None:
            self.history_server_config = history_server_config
        if redis_config is not None:
            self.redis_config = redis_config
        self.storages_config = storages_config
        if flink_config is not None:
            self.flink_config = flink_config
        if expand_cpu_resource is not None:
            self.expand_cpu_resource = expand_cpu_resource
        self.worker_group_config = worker_group_config
        self.serve_config = serve_config
        if data_infos is not None:
            self.data_infos = data_infos

    @property
    def type(self):
        r"""Gets the type of this V2EndpointCreateEngineConfig.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayService。 **默认取值**：不涉及。 

        :return: The type of this V2EndpointCreateEngineConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this V2EndpointCreateEngineConfig.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayService。 **默认取值**：不涉及。 

        :param type: The type of this V2EndpointCreateEngineConfig.
        :type type: str
        """
        self._type = type

    @property
    def spark_config(self):
        r"""Gets the spark_config of this V2EndpointCreateEngineConfig.

        **参数解释**：SparkSql参数配置。 **约束限制**：最大数量为100。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The spark_config of this V2EndpointCreateEngineConfig.
        :rtype: dict(str, str)
        """
        return self._spark_config

    @spark_config.setter
    def spark_config(self, spark_config):
        r"""Sets the spark_config of this V2EndpointCreateEngineConfig.

        **参数解释**：SparkSql参数配置。 **约束限制**：最大数量为100。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param spark_config: The spark_config of this V2EndpointCreateEngineConfig.
        :type spark_config: dict(str, str)
        """
        self._spark_config = spark_config

    @property
    def scheduling_config(self):
        r"""Gets the scheduling_config of this V2EndpointCreateEngineConfig.

        :return: The scheduling_config of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SparkSchedulingConfig`
        """
        return self._scheduling_config

    @scheduling_config.setter
    def scheduling_config(self, scheduling_config):
        r"""Sets the scheduling_config of this V2EndpointCreateEngineConfig.

        :param scheduling_config: The scheduling_config of this V2EndpointCreateEngineConfig.
        :type scheduling_config: :class:`huaweicloudsdkaidatalake.v2.SparkSchedulingConfig`
        """
        self._scheduling_config = scheduling_config

    @property
    def staging_config(self):
        r"""Gets the staging_config of this V2EndpointCreateEngineConfig.

        :return: The staging_config of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.AuraV2StagingConfig`
        """
        return self._staging_config

    @staging_config.setter
    def staging_config(self, staging_config):
        r"""Sets the staging_config of this V2EndpointCreateEngineConfig.

        :param staging_config: The staging_config of this V2EndpointCreateEngineConfig.
        :type staging_config: :class:`huaweicloudsdkaidatalake.v2.AuraV2StagingConfig`
        """
        self._staging_config = staging_config

    @property
    def image(self):
        r"""Gets the image of this V2EndpointCreateEngineConfig.

        :return: The image of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this V2EndpointCreateEngineConfig.

        :param image: The image of this V2EndpointCreateEngineConfig.
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        self._image = image

    @property
    def cluster_config(self):
        r"""Gets the cluster_config of this V2EndpointCreateEngineConfig.

        :return: The cluster_config of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        """
        return self._cluster_config

    @cluster_config.setter
    def cluster_config(self, cluster_config):
        r"""Sets the cluster_config of this V2EndpointCreateEngineConfig.

        :param cluster_config: The cluster_config of this V2EndpointCreateEngineConfig.
        :type cluster_config: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        """
        self._cluster_config = cluster_config

    @property
    def max_endpoint_concurrent_queries(self):
        r"""Gets the max_endpoint_concurrent_queries of this V2EndpointCreateEngineConfig.

        **参数解释**：端点最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：300。 

        :return: The max_endpoint_concurrent_queries of this V2EndpointCreateEngineConfig.
        :rtype: int
        """
        return self._max_endpoint_concurrent_queries

    @max_endpoint_concurrent_queries.setter
    def max_endpoint_concurrent_queries(self, max_endpoint_concurrent_queries):
        r"""Sets the max_endpoint_concurrent_queries of this V2EndpointCreateEngineConfig.

        **参数解释**：端点最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：300。 

        :param max_endpoint_concurrent_queries: The max_endpoint_concurrent_queries of this V2EndpointCreateEngineConfig.
        :type max_endpoint_concurrent_queries: int
        """
        self._max_endpoint_concurrent_queries = max_endpoint_concurrent_queries

    @property
    def history_server_config(self):
        r"""Gets the history_server_config of this V2EndpointCreateEngineConfig.

        :return: The history_server_config of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        return self._history_server_config

    @history_server_config.setter
    def history_server_config(self, history_server_config):
        r"""Sets the history_server_config of this V2EndpointCreateEngineConfig.

        :param history_server_config: The history_server_config of this V2EndpointCreateEngineConfig.
        :type history_server_config: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        self._history_server_config = history_server_config

    @property
    def redis_config(self):
        r"""Gets the redis_config of this V2EndpointCreateEngineConfig.

        :return: The redis_config of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        """
        return self._redis_config

    @redis_config.setter
    def redis_config(self, redis_config):
        r"""Sets the redis_config of this V2EndpointCreateEngineConfig.

        :param redis_config: The redis_config of this V2EndpointCreateEngineConfig.
        :type redis_config: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        """
        self._redis_config = redis_config

    @property
    def storages_config(self):
        r"""Gets the storages_config of this V2EndpointCreateEngineConfig.

        :return: The storages_config of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateStoragesConfig`
        """
        return self._storages_config

    @storages_config.setter
    def storages_config(self, storages_config):
        r"""Sets the storages_config of this V2EndpointCreateEngineConfig.

        :param storages_config: The storages_config of this V2EndpointCreateEngineConfig.
        :type storages_config: :class:`huaweicloudsdkaidatalake.v2.CreateStoragesConfig`
        """
        self._storages_config = storages_config

    @property
    def flink_config(self):
        r"""Gets the flink_config of this V2EndpointCreateEngineConfig.

        **参数解释**：Flink参数配置，Map的key为Flink配置参数名，value为对应的参数值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flink_config of this V2EndpointCreateEngineConfig.
        :rtype: dict(str, str)
        """
        return self._flink_config

    @flink_config.setter
    def flink_config(self, flink_config):
        r"""Sets the flink_config of this V2EndpointCreateEngineConfig.

        **参数解释**：Flink参数配置，Map的key为Flink配置参数名，value为对应的参数值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flink_config: The flink_config of this V2EndpointCreateEngineConfig.
        :type flink_config: dict(str, str)
        """
        self._flink_config = flink_config

    @property
    def expand_cpu_resource(self):
        r"""Gets the expand_cpu_resource of this V2EndpointCreateEngineConfig.

        **参数解释**：开启后，通算工作组作业能够使用智算工作组空闲CPU及内存资源，该操作可能会导致智算任务因资源不足而排队。 **约束限制**：不涉及。 **取值范围**：   - true：开启通算工作组作业使用智算工作组空闲CPU及内存资源。   - false：关闭通算工作组作业使用智算工作组空闲CPU及内存资源。 **默认取值**：false。

        :return: The expand_cpu_resource of this V2EndpointCreateEngineConfig.
        :rtype: bool
        """
        return self._expand_cpu_resource

    @expand_cpu_resource.setter
    def expand_cpu_resource(self, expand_cpu_resource):
        r"""Sets the expand_cpu_resource of this V2EndpointCreateEngineConfig.

        **参数解释**：开启后，通算工作组作业能够使用智算工作组空闲CPU及内存资源，该操作可能会导致智算任务因资源不足而排队。 **约束限制**：不涉及。 **取值范围**：   - true：开启通算工作组作业使用智算工作组空闲CPU及内存资源。   - false：关闭通算工作组作业使用智算工作组空闲CPU及内存资源。 **默认取值**：false。

        :param expand_cpu_resource: The expand_cpu_resource of this V2EndpointCreateEngineConfig.
        :type expand_cpu_resource: bool
        """
        self._expand_cpu_resource = expand_cpu_resource

    @property
    def worker_group_config(self):
        r"""Gets the worker_group_config of this V2EndpointCreateEngineConfig.

        **参数解释**：工作组补充配置，和外部capacity对应。 **约束限制**：最多10个。

        :return: The worker_group_config of this V2EndpointCreateEngineConfig.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupConfig`]
        """
        return self._worker_group_config

    @worker_group_config.setter
    def worker_group_config(self, worker_group_config):
        r"""Sets the worker_group_config of this V2EndpointCreateEngineConfig.

        **参数解释**：工作组补充配置，和外部capacity对应。 **约束限制**：最多10个。

        :param worker_group_config: The worker_group_config of this V2EndpointCreateEngineConfig.
        :type worker_group_config: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupConfig`]
        """
        self._worker_group_config = worker_group_config

    @property
    def serve_config(self):
        r"""Gets the serve_config of this V2EndpointCreateEngineConfig.

        :return: The serve_config of this V2EndpointCreateEngineConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ServeConfig`
        """
        return self._serve_config

    @serve_config.setter
    def serve_config(self, serve_config):
        r"""Sets the serve_config of this V2EndpointCreateEngineConfig.

        :param serve_config: The serve_config of this V2EndpointCreateEngineConfig.
        :type serve_config: :class:`huaweicloudsdkaidatalake.v2.ServeConfig`
        """
        self._serve_config = serve_config

    @property
    def data_infos(self):
        r"""Gets the data_infos of this V2EndpointCreateEngineConfig.

        **参数解释**：模型信息列表（可选）。模型可以打包在镜像中（通过 working_dir 配置项指定），也可以通过此字段上传模型地址。创建时如果模型已预置在镜像中，可省略此字段；更新时如果模型没有变化，也可以不填。 **约束限制**：不涉及。

        :return: The data_infos of this V2EndpointCreateEngineConfig.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.DataInfo`]
        """
        return self._data_infos

    @data_infos.setter
    def data_infos(self, data_infos):
        r"""Sets the data_infos of this V2EndpointCreateEngineConfig.

        **参数解释**：模型信息列表（可选）。模型可以打包在镜像中（通过 working_dir 配置项指定），也可以通过此字段上传模型地址。创建时如果模型已预置在镜像中，可省略此字段；更新时如果模型没有变化，也可以不填。 **约束限制**：不涉及。

        :param data_infos: The data_infos of this V2EndpointCreateEngineConfig.
        :type data_infos: list[:class:`huaweicloudsdkaidatalake.v2.DataInfo`]
        """
        self._data_infos = data_infos

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)
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
        if not isinstance(other, V2EndpointCreateEngineConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
