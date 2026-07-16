# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishOpsDatasetVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'version_name': 'version_name',
        'description': 'description'
    }

    def __init__(self, version_name=None, description=None):
        r"""PublishOpsDatasetVersionRequestBody

        The model defined in huaweicloud sdk

        :param version_name: **参数解释：** 用户定义的版本标签或编号。 **约束限制：** 建议长度不超过 100 字符。 **取值范围：** 字符串，如 \&quot;v1.0\&quot;、\&quot;20240413_test\&quot;。 **默认取值：** 不涉及。 
        :type version_name: str
        :param description: **参数解释：** 该版本的变更摘要或备注信息。 **约束限制：** 可选参数；长度0到200字符。 **取值范围：** 中英文及常见符号。 **默认取值：** 不涉及。 
        :type description: str
        """
        
        

        self._version_name = None
        self._description = None
        self.discriminator = None

        self.version_name = version_name
        if description is not None:
            self.description = description

    @property
    def version_name(self):
        r"""Gets the version_name of this PublishOpsDatasetVersionRequestBody.

        **参数解释：** 用户定义的版本标签或编号。 **约束限制：** 建议长度不超过 100 字符。 **取值范围：** 字符串，如 \"v1.0\"、\"20240413_test\"。 **默认取值：** 不涉及。 

        :return: The version_name of this PublishOpsDatasetVersionRequestBody.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this PublishOpsDatasetVersionRequestBody.

        **参数解释：** 用户定义的版本标签或编号。 **约束限制：** 建议长度不超过 100 字符。 **取值范围：** 字符串，如 \"v1.0\"、\"20240413_test\"。 **默认取值：** 不涉及。 

        :param version_name: The version_name of this PublishOpsDatasetVersionRequestBody.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def description(self):
        r"""Gets the description of this PublishOpsDatasetVersionRequestBody.

        **参数解释：** 该版本的变更摘要或备注信息。 **约束限制：** 可选参数；长度0到200字符。 **取值范围：** 中英文及常见符号。 **默认取值：** 不涉及。 

        :return: The description of this PublishOpsDatasetVersionRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublishOpsDatasetVersionRequestBody.

        **参数解释：** 该版本的变更摘要或备注信息。 **约束限制：** 可选参数；长度0到200字符。 **取值范围：** 中英文及常见符号。 **默认取值：** 不涉及。 

        :param description: The description of this PublishOpsDatasetVersionRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, PublishOpsDatasetVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
