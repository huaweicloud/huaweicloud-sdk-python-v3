# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSparkJob:

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
        'staging_config': 'StagingConfig',
        'image': 'V2ImageBriefInfoAdmin'
    }

    attribute_map = {
        'type': 'type',
        'spark_config': 'spark_config',
        'scheduling_config': 'scheduling_config',
        'staging_config': 'staging_config',
        'image': 'image'
    }

    def __init__(self, type=None, spark_config=None, scheduling_config=None, staging_config=None, image=None):
        r"""CreateSparkJob

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：SparkJob。 **默认取值**：不涉及。 
        :type type: str
        :param spark_config: **参数解释**：Spark参数配置，Map的key为Spark配置参数名，value为对应的参数值。 **约束限制**：最大数量为100。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type spark_config: dict(str, str)
        :param scheduling_config: 
        :type scheduling_config: :class:`huaweicloudsdkaidatalake.v2.SparkSchedulingConfig`
        :param staging_config: 
        :type staging_config: :class:`huaweicloudsdkaidatalake.v2.StagingConfig`
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        
        

        self._type = None
        self._spark_config = None
        self._scheduling_config = None
        self._staging_config = None
        self._image = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if spark_config is not None:
            self.spark_config = spark_config
        if scheduling_config is not None:
            self.scheduling_config = scheduling_config
        self.staging_config = staging_config
        if image is not None:
            self.image = image

    @property
    def type(self):
        r"""Gets the type of this CreateSparkJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：SparkJob。 **默认取值**：不涉及。 

        :return: The type of this CreateSparkJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateSparkJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：SparkJob。 **默认取值**：不涉及。 

        :param type: The type of this CreateSparkJob.
        :type type: str
        """
        self._type = type

    @property
    def spark_config(self):
        r"""Gets the spark_config of this CreateSparkJob.

        **参数解释**：Spark参数配置，Map的key为Spark配置参数名，value为对应的参数值。 **约束限制**：最大数量为100。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The spark_config of this CreateSparkJob.
        :rtype: dict(str, str)
        """
        return self._spark_config

    @spark_config.setter
    def spark_config(self, spark_config):
        r"""Sets the spark_config of this CreateSparkJob.

        **参数解释**：Spark参数配置，Map的key为Spark配置参数名，value为对应的参数值。 **约束限制**：最大数量为100。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param spark_config: The spark_config of this CreateSparkJob.
        :type spark_config: dict(str, str)
        """
        self._spark_config = spark_config

    @property
    def scheduling_config(self):
        r"""Gets the scheduling_config of this CreateSparkJob.

        :return: The scheduling_config of this CreateSparkJob.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SparkSchedulingConfig`
        """
        return self._scheduling_config

    @scheduling_config.setter
    def scheduling_config(self, scheduling_config):
        r"""Sets the scheduling_config of this CreateSparkJob.

        :param scheduling_config: The scheduling_config of this CreateSparkJob.
        :type scheduling_config: :class:`huaweicloudsdkaidatalake.v2.SparkSchedulingConfig`
        """
        self._scheduling_config = scheduling_config

    @property
    def staging_config(self):
        r"""Gets the staging_config of this CreateSparkJob.

        :return: The staging_config of this CreateSparkJob.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.StagingConfig`
        """
        return self._staging_config

    @staging_config.setter
    def staging_config(self, staging_config):
        r"""Sets the staging_config of this CreateSparkJob.

        :param staging_config: The staging_config of this CreateSparkJob.
        :type staging_config: :class:`huaweicloudsdkaidatalake.v2.StagingConfig`
        """
        self._staging_config = staging_config

    @property
    def image(self):
        r"""Gets the image of this CreateSparkJob.

        :return: The image of this CreateSparkJob.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CreateSparkJob.

        :param image: The image of this CreateSparkJob.
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        self._image = image

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
        if not isinstance(other, CreateSparkJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
