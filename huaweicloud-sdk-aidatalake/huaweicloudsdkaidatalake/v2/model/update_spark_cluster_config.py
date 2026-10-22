# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSparkClusterConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aging_time': 'int',
        'auto_stop_config': 'AutoStopConfig',
        'driver_resource_spec': 'UpdateSparkDriverResourceSpec',
        'executor_resource_spec': 'UpdateSparkExecutorResourceSpec',
        'min_clusters': 'int',
        'max_clusters': 'int',
        'max_cluster_concurrent_queries': 'int'
    }

    attribute_map = {
        'aging_time': 'aging_time',
        'auto_stop_config': 'auto_stop_config',
        'driver_resource_spec': 'driver_resource_spec',
        'executor_resource_spec': 'executor_resource_spec',
        'min_clusters': 'min_clusters',
        'max_clusters': 'max_clusters',
        'max_cluster_concurrent_queries': 'max_cluster_concurrent_queries'
    }

    def __init__(self, aging_time=None, auto_stop_config=None, driver_resource_spec=None, executor_resource_spec=None, min_clusters=None, max_clusters=None, max_cluster_concurrent_queries=None):
        r"""UpdateSparkClusterConfig

        The model defined in huaweicloud sdk

        :param aging_time: **参数解释**：集群老化时间（小时）。 **约束限制**：不涉及。 **取值范围**：1~12。 **默认取值**：不涉及。 
        :type aging_time: int
        :param auto_stop_config: 
        :type auto_stop_config: :class:`huaweicloudsdkaidatalake.v2.AutoStopConfig`
        :param driver_resource_spec: 
        :type driver_resource_spec: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkDriverResourceSpec`
        :param executor_resource_spec: 
        :type executor_resource_spec: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkExecutorResourceSpec`
        :param min_clusters: **参数解释**：最小集群数量。 **约束限制**：不涉及。 **取值范围**：0~20。 **默认取值**：不涉及。 
        :type min_clusters: int
        :param max_clusters: **参数解释**：最大集群数量。 **约束限制**：不涉及。 **取值范围**：2~20。 **默认取值**：不涉及。 
        :type max_clusters: int
        :param max_cluster_concurrent_queries: **参数解释**：集群最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~30。 **默认取值**：不涉及。 
        :type max_cluster_concurrent_queries: int
        """
        
        

        self._aging_time = None
        self._auto_stop_config = None
        self._driver_resource_spec = None
        self._executor_resource_spec = None
        self._min_clusters = None
        self._max_clusters = None
        self._max_cluster_concurrent_queries = None
        self.discriminator = None

        if aging_time is not None:
            self.aging_time = aging_time
        if auto_stop_config is not None:
            self.auto_stop_config = auto_stop_config
        if driver_resource_spec is not None:
            self.driver_resource_spec = driver_resource_spec
        if executor_resource_spec is not None:
            self.executor_resource_spec = executor_resource_spec
        if min_clusters is not None:
            self.min_clusters = min_clusters
        if max_clusters is not None:
            self.max_clusters = max_clusters
        if max_cluster_concurrent_queries is not None:
            self.max_cluster_concurrent_queries = max_cluster_concurrent_queries

    @property
    def aging_time(self):
        r"""Gets the aging_time of this UpdateSparkClusterConfig.

        **参数解释**：集群老化时间（小时）。 **约束限制**：不涉及。 **取值范围**：1~12。 **默认取值**：不涉及。 

        :return: The aging_time of this UpdateSparkClusterConfig.
        :rtype: int
        """
        return self._aging_time

    @aging_time.setter
    def aging_time(self, aging_time):
        r"""Sets the aging_time of this UpdateSparkClusterConfig.

        **参数解释**：集群老化时间（小时）。 **约束限制**：不涉及。 **取值范围**：1~12。 **默认取值**：不涉及。 

        :param aging_time: The aging_time of this UpdateSparkClusterConfig.
        :type aging_time: int
        """
        self._aging_time = aging_time

    @property
    def auto_stop_config(self):
        r"""Gets the auto_stop_config of this UpdateSparkClusterConfig.

        :return: The auto_stop_config of this UpdateSparkClusterConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.AutoStopConfig`
        """
        return self._auto_stop_config

    @auto_stop_config.setter
    def auto_stop_config(self, auto_stop_config):
        r"""Sets the auto_stop_config of this UpdateSparkClusterConfig.

        :param auto_stop_config: The auto_stop_config of this UpdateSparkClusterConfig.
        :type auto_stop_config: :class:`huaweicloudsdkaidatalake.v2.AutoStopConfig`
        """
        self._auto_stop_config = auto_stop_config

    @property
    def driver_resource_spec(self):
        r"""Gets the driver_resource_spec of this UpdateSparkClusterConfig.

        :return: The driver_resource_spec of this UpdateSparkClusterConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkDriverResourceSpec`
        """
        return self._driver_resource_spec

    @driver_resource_spec.setter
    def driver_resource_spec(self, driver_resource_spec):
        r"""Sets the driver_resource_spec of this UpdateSparkClusterConfig.

        :param driver_resource_spec: The driver_resource_spec of this UpdateSparkClusterConfig.
        :type driver_resource_spec: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkDriverResourceSpec`
        """
        self._driver_resource_spec = driver_resource_spec

    @property
    def executor_resource_spec(self):
        r"""Gets the executor_resource_spec of this UpdateSparkClusterConfig.

        :return: The executor_resource_spec of this UpdateSparkClusterConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkExecutorResourceSpec`
        """
        return self._executor_resource_spec

    @executor_resource_spec.setter
    def executor_resource_spec(self, executor_resource_spec):
        r"""Sets the executor_resource_spec of this UpdateSparkClusterConfig.

        :param executor_resource_spec: The executor_resource_spec of this UpdateSparkClusterConfig.
        :type executor_resource_spec: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkExecutorResourceSpec`
        """
        self._executor_resource_spec = executor_resource_spec

    @property
    def min_clusters(self):
        r"""Gets the min_clusters of this UpdateSparkClusterConfig.

        **参数解释**：最小集群数量。 **约束限制**：不涉及。 **取值范围**：0~20。 **默认取值**：不涉及。 

        :return: The min_clusters of this UpdateSparkClusterConfig.
        :rtype: int
        """
        return self._min_clusters

    @min_clusters.setter
    def min_clusters(self, min_clusters):
        r"""Sets the min_clusters of this UpdateSparkClusterConfig.

        **参数解释**：最小集群数量。 **约束限制**：不涉及。 **取值范围**：0~20。 **默认取值**：不涉及。 

        :param min_clusters: The min_clusters of this UpdateSparkClusterConfig.
        :type min_clusters: int
        """
        self._min_clusters = min_clusters

    @property
    def max_clusters(self):
        r"""Gets the max_clusters of this UpdateSparkClusterConfig.

        **参数解释**：最大集群数量。 **约束限制**：不涉及。 **取值范围**：2~20。 **默认取值**：不涉及。 

        :return: The max_clusters of this UpdateSparkClusterConfig.
        :rtype: int
        """
        return self._max_clusters

    @max_clusters.setter
    def max_clusters(self, max_clusters):
        r"""Sets the max_clusters of this UpdateSparkClusterConfig.

        **参数解释**：最大集群数量。 **约束限制**：不涉及。 **取值范围**：2~20。 **默认取值**：不涉及。 

        :param max_clusters: The max_clusters of this UpdateSparkClusterConfig.
        :type max_clusters: int
        """
        self._max_clusters = max_clusters

    @property
    def max_cluster_concurrent_queries(self):
        r"""Gets the max_cluster_concurrent_queries of this UpdateSparkClusterConfig.

        **参数解释**：集群最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~30。 **默认取值**：不涉及。 

        :return: The max_cluster_concurrent_queries of this UpdateSparkClusterConfig.
        :rtype: int
        """
        return self._max_cluster_concurrent_queries

    @max_cluster_concurrent_queries.setter
    def max_cluster_concurrent_queries(self, max_cluster_concurrent_queries):
        r"""Sets the max_cluster_concurrent_queries of this UpdateSparkClusterConfig.

        **参数解释**：集群最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~30。 **默认取值**：不涉及。 

        :param max_cluster_concurrent_queries: The max_cluster_concurrent_queries of this UpdateSparkClusterConfig.
        :type max_cluster_concurrent_queries: int
        """
        self._max_cluster_concurrent_queries = max_cluster_concurrent_queries

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
        if not isinstance(other, UpdateSparkClusterConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
