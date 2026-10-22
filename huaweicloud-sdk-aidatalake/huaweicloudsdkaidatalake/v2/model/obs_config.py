# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsConfig:

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
        'agency_name': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'agency_name': 'agency_name'
    }

    def __init__(self, bucket_name=None, agency_name=None):
        r"""ObsConfig

        The model defined in huaweicloud sdk

        :param bucket_name: **参数解释**：OBS桶名称。该桶的类型必须是并行文件系统。 **约束限制**：不涉及。 **取值范围**：长度为3~63个字符，支持小写字母、数字、中划线和句点的组合。 **默认取值**：不涉及。
        :type bucket_name: str
        :param agency_name: **参数解释**：委托名称。云服务将使用该委托操作OBS桶。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type agency_name: str
        """
        
        

        self._bucket_name = None
        self._agency_name = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ObsConfig.

        **参数解释**：OBS桶名称。该桶的类型必须是并行文件系统。 **约束限制**：不涉及。 **取值范围**：长度为3~63个字符，支持小写字母、数字、中划线和句点的组合。 **默认取值**：不涉及。

        :return: The bucket_name of this ObsConfig.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ObsConfig.

        **参数解释**：OBS桶名称。该桶的类型必须是并行文件系统。 **约束限制**：不涉及。 **取值范围**：长度为3~63个字符，支持小写字母、数字、中划线和句点的组合。 **默认取值**：不涉及。

        :param bucket_name: The bucket_name of this ObsConfig.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ObsConfig.

        **参数解释**：委托名称。云服务将使用该委托操作OBS桶。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The agency_name of this ObsConfig.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ObsConfig.

        **参数解释**：委托名称。云服务将使用该委托操作OBS桶。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param agency_name: The agency_name of this ObsConfig.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, ObsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
