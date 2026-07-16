# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayObsConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'object_key': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'object_key': 'object_key'
    }

    def __init__(self, bucket_name=None, object_key=None):
        r"""CoreGatewayObsConfiguration

        The model defined in huaweicloud sdk

        :param bucket_name: **参数解释：** OBS 桶名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 3-63 个字符，匹配单个小写字母或数字，或者以字母数字开头和结尾、中间可含1到61个小写字母/数字/点/短横线的字符串，符合正则条件^[a-z0-9]\\([a-z0-9.-]{1,61}[a-z0-9])?$。 **默认取值：** 不涉及。 
        :type bucket_name: str
        :param object_key: **参数解释：** OBS 对象键名（文件路径）： - 示例：specs/petstore.yaml **约束限制：** 不涉及。 **取值范围：** 长度为 1-1024 个字符。 **默认取值：** 不涉及。 
        :type object_key: str
        """
        
        

        self._bucket_name = None
        self._object_key = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.object_key = object_key

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CoreGatewayObsConfiguration.

        **参数解释：** OBS 桶名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 3-63 个字符，匹配单个小写字母或数字，或者以字母数字开头和结尾、中间可含1到61个小写字母/数字/点/短横线的字符串，符合正则条件^[a-z0-9]\\([a-z0-9.-]{1,61}[a-z0-9])?$。 **默认取值：** 不涉及。 

        :return: The bucket_name of this CoreGatewayObsConfiguration.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CoreGatewayObsConfiguration.

        **参数解释：** OBS 桶名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 3-63 个字符，匹配单个小写字母或数字，或者以字母数字开头和结尾、中间可含1到61个小写字母/数字/点/短横线的字符串，符合正则条件^[a-z0-9]\\([a-z0-9.-]{1,61}[a-z0-9])?$。 **默认取值：** 不涉及。 

        :param bucket_name: The bucket_name of this CoreGatewayObsConfiguration.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this CoreGatewayObsConfiguration.

        **参数解释：** OBS 对象键名（文件路径）： - 示例：specs/petstore.yaml **约束限制：** 不涉及。 **取值范围：** 长度为 1-1024 个字符。 **默认取值：** 不涉及。 

        :return: The object_key of this CoreGatewayObsConfiguration.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this CoreGatewayObsConfiguration.

        **参数解释：** OBS 对象键名（文件路径）： - 示例：specs/petstore.yaml **约束限制：** 不涉及。 **取值范围：** 长度为 1-1024 个字符。 **默认取值：** 不涉及。 

        :param object_key: The object_key of this CoreGatewayObsConfiguration.
        :type object_key: str
        """
        self._object_key = object_key

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
        if not isinstance(other, CoreGatewayObsConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
