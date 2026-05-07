# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpgradePathsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'source_version': 'str',
        'target_version': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'source_version': 'source_version',
        'target_version': 'target_version'
    }

    def __init__(self, x_language=None, source_version=None, target_version=None):
        r"""ListUpgradePathsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param source_version: **参数解释**: 源引擎版本号。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 
        :type source_version: str
        :param target_version: **参数解释**: 目标引擎版本号。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 
        :type target_version: str
        """
        
        

        self._x_language = None
        self._source_version = None
        self._target_version = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.source_version = source_version
        if target_version is not None:
            self.target_version = target_version

    @property
    def x_language(self):
        r"""Gets the x_language of this ListUpgradePathsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListUpgradePathsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListUpgradePathsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListUpgradePathsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def source_version(self):
        r"""Gets the source_version of this ListUpgradePathsRequest.

        **参数解释**: 源引擎版本号。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 

        :return: The source_version of this ListUpgradePathsRequest.
        :rtype: str
        """
        return self._source_version

    @source_version.setter
    def source_version(self, source_version):
        r"""Sets the source_version of this ListUpgradePathsRequest.

        **参数解释**: 源引擎版本号。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 

        :param source_version: The source_version of this ListUpgradePathsRequest.
        :type source_version: str
        """
        self._source_version = source_version

    @property
    def target_version(self):
        r"""Gets the target_version of this ListUpgradePathsRequest.

        **参数解释**: 目标引擎版本号。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 

        :return: The target_version of this ListUpgradePathsRequest.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ListUpgradePathsRequest.

        **参数解释**: 目标引擎版本号。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 

        :param target_version: The target_version of this ListUpgradePathsRequest.
        :type target_version: str
        """
        self._target_version = target_version

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
        if not isinstance(other, ListUpgradePathsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
