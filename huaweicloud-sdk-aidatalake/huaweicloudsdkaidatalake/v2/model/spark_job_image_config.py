# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkJobImageConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'image_version_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_version_id': 'image_version_id'
    }

    def __init__(self, image_id=None, image_version_id=None):
        r"""SparkJobImageConfig

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**：镜像ID，用于指定Spark作业运行所需的镜像。 **约束限制**：不涉及。 **取值范围**：长度为2~64个字符。 **默认取值**：不涉及。
        :type image_id: str
        :param image_version_id: **参数解释**：镜像版本，用于指定Spark作业运行所需的镜像版本。 **约束限制**：不涉及。 **取值范围**：长度为2~64个字符。 **默认取值**：不涉及。
        :type image_version_id: str
        """
        
        

        self._image_id = None
        self._image_version_id = None
        self.discriminator = None

        self.image_id = image_id
        self.image_version_id = image_version_id

    @property
    def image_id(self):
        r"""Gets the image_id of this SparkJobImageConfig.

        **参数解释**：镜像ID，用于指定Spark作业运行所需的镜像。 **约束限制**：不涉及。 **取值范围**：长度为2~64个字符。 **默认取值**：不涉及。

        :return: The image_id of this SparkJobImageConfig.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this SparkJobImageConfig.

        **参数解释**：镜像ID，用于指定Spark作业运行所需的镜像。 **约束限制**：不涉及。 **取值范围**：长度为2~64个字符。 **默认取值**：不涉及。

        :param image_id: The image_id of this SparkJobImageConfig.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_version_id(self):
        r"""Gets the image_version_id of this SparkJobImageConfig.

        **参数解释**：镜像版本，用于指定Spark作业运行所需的镜像版本。 **约束限制**：不涉及。 **取值范围**：长度为2~64个字符。 **默认取值**：不涉及。

        :return: The image_version_id of this SparkJobImageConfig.
        :rtype: str
        """
        return self._image_version_id

    @image_version_id.setter
    def image_version_id(self, image_version_id):
        r"""Sets the image_version_id of this SparkJobImageConfig.

        **参数解释**：镜像版本，用于指定Spark作业运行所需的镜像版本。 **约束限制**：不涉及。 **取值范围**：长度为2~64个字符。 **默认取值**：不涉及。

        :param image_version_id: The image_version_id of this SparkJobImageConfig.
        :type image_version_id: str
        """
        self._image_version_id = image_version_id

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
        if not isinstance(other, SparkJobImageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
