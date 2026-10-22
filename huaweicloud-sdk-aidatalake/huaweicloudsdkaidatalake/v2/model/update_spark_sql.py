# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSparkSql:

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
        'image': 'V2ImageBriefInfoAdmin',
        'spark_config': 'dict(str, str)',
        'cluster_config': 'UpdateSparkClusterConfig',
        'max_endpoint_concurrent_queries': 'int'
    }

    attribute_map = {
        'type': 'type',
        'image': 'image',
        'spark_config': 'spark_config',
        'cluster_config': 'cluster_config',
        'max_endpoint_concurrent_queries': 'max_endpoint_concurrent_queries'
    }

    def __init__(self, type=None, image=None, spark_config=None, cluster_config=None, max_endpoint_concurrent_queries=None):
        r"""UpdateSparkSql

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：SparkSql。 **默认取值**：不涉及。 
        :type type: str
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        :param spark_config: **参数解释**：Spark 参数配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type spark_config: dict(str, str)
        :param cluster_config: 
        :type cluster_config: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkClusterConfig`
        :param max_endpoint_concurrent_queries: **参数解释**：端点最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：300。 
        :type max_endpoint_concurrent_queries: int
        """
        
        

        self._type = None
        self._image = None
        self._spark_config = None
        self._cluster_config = None
        self._max_endpoint_concurrent_queries = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if image is not None:
            self.image = image
        if spark_config is not None:
            self.spark_config = spark_config
        if cluster_config is not None:
            self.cluster_config = cluster_config
        if max_endpoint_concurrent_queries is not None:
            self.max_endpoint_concurrent_queries = max_endpoint_concurrent_queries

    @property
    def type(self):
        r"""Gets the type of this UpdateSparkSql.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：SparkSql。 **默认取值**：不涉及。 

        :return: The type of this UpdateSparkSql.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateSparkSql.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：SparkSql。 **默认取值**：不涉及。 

        :param type: The type of this UpdateSparkSql.
        :type type: str
        """
        self._type = type

    @property
    def image(self):
        r"""Gets the image of this UpdateSparkSql.

        :return: The image of this UpdateSparkSql.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this UpdateSparkSql.

        :param image: The image of this UpdateSparkSql.
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        self._image = image

    @property
    def spark_config(self):
        r"""Gets the spark_config of this UpdateSparkSql.

        **参数解释**：Spark 参数配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The spark_config of this UpdateSparkSql.
        :rtype: dict(str, str)
        """
        return self._spark_config

    @spark_config.setter
    def spark_config(self, spark_config):
        r"""Sets the spark_config of this UpdateSparkSql.

        **参数解释**：Spark 参数配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param spark_config: The spark_config of this UpdateSparkSql.
        :type spark_config: dict(str, str)
        """
        self._spark_config = spark_config

    @property
    def cluster_config(self):
        r"""Gets the cluster_config of this UpdateSparkSql.

        :return: The cluster_config of this UpdateSparkSql.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkClusterConfig`
        """
        return self._cluster_config

    @cluster_config.setter
    def cluster_config(self, cluster_config):
        r"""Sets the cluster_config of this UpdateSparkSql.

        :param cluster_config: The cluster_config of this UpdateSparkSql.
        :type cluster_config: :class:`huaweicloudsdkaidatalake.v2.UpdateSparkClusterConfig`
        """
        self._cluster_config = cluster_config

    @property
    def max_endpoint_concurrent_queries(self):
        r"""Gets the max_endpoint_concurrent_queries of this UpdateSparkSql.

        **参数解释**：端点最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：300。 

        :return: The max_endpoint_concurrent_queries of this UpdateSparkSql.
        :rtype: int
        """
        return self._max_endpoint_concurrent_queries

    @max_endpoint_concurrent_queries.setter
    def max_endpoint_concurrent_queries(self, max_endpoint_concurrent_queries):
        r"""Sets the max_endpoint_concurrent_queries of this UpdateSparkSql.

        **参数解释**：端点最大并发SQL数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：300。 

        :param max_endpoint_concurrent_queries: The max_endpoint_concurrent_queries of this UpdateSparkSql.
        :type max_endpoint_concurrent_queries: int
        """
        self._max_endpoint_concurrent_queries = max_endpoint_concurrent_queries

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
        if not isinstance(other, UpdateSparkSql):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
