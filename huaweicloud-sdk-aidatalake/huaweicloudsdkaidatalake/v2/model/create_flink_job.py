# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkJob:

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
        'flink_config': 'dict(str, str)',
        'staging_config': 'StagingConfig',
        'image': 'V2ImageBriefInfoAdmin'
    }

    attribute_map = {
        'type': 'type',
        'flink_config': 'flink_config',
        'staging_config': 'staging_config',
        'image': 'image'
    }

    def __init__(self, type=None, flink_config=None, staging_config=None, image=None):
        r"""CreateFlinkJob

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：FlinkJob。 **默认取值**：不涉及。 
        :type type: str
        :param flink_config: **参数解释**：Flink参数配置，Map的key为Flink配置参数名，value为对应的参数值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flink_config: dict(str, str)
        :param staging_config: 
        :type staging_config: :class:`huaweicloudsdkaidatalake.v2.StagingConfig`
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        
        

        self._type = None
        self._flink_config = None
        self._staging_config = None
        self._image = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if flink_config is not None:
            self.flink_config = flink_config
        self.staging_config = staging_config
        if image is not None:
            self.image = image

    @property
    def type(self):
        r"""Gets the type of this CreateFlinkJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：FlinkJob。 **默认取值**：不涉及。 

        :return: The type of this CreateFlinkJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateFlinkJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：FlinkJob。 **默认取值**：不涉及。 

        :param type: The type of this CreateFlinkJob.
        :type type: str
        """
        self._type = type

    @property
    def flink_config(self):
        r"""Gets the flink_config of this CreateFlinkJob.

        **参数解释**：Flink参数配置，Map的key为Flink配置参数名，value为对应的参数值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flink_config of this CreateFlinkJob.
        :rtype: dict(str, str)
        """
        return self._flink_config

    @flink_config.setter
    def flink_config(self, flink_config):
        r"""Sets the flink_config of this CreateFlinkJob.

        **参数解释**：Flink参数配置，Map的key为Flink配置参数名，value为对应的参数值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flink_config: The flink_config of this CreateFlinkJob.
        :type flink_config: dict(str, str)
        """
        self._flink_config = flink_config

    @property
    def staging_config(self):
        r"""Gets the staging_config of this CreateFlinkJob.

        :return: The staging_config of this CreateFlinkJob.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.StagingConfig`
        """
        return self._staging_config

    @staging_config.setter
    def staging_config(self, staging_config):
        r"""Sets the staging_config of this CreateFlinkJob.

        :param staging_config: The staging_config of this CreateFlinkJob.
        :type staging_config: :class:`huaweicloudsdkaidatalake.v2.StagingConfig`
        """
        self._staging_config = staging_config

    @property
    def image(self):
        r"""Gets the image of this CreateFlinkJob.

        :return: The image of this CreateFlinkJob.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CreateFlinkJob.

        :param image: The image of this CreateFlinkJob.
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
        if not isinstance(other, CreateFlinkJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
