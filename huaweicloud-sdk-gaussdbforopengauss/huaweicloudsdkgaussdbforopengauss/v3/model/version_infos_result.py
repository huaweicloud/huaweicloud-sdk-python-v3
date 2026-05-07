# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionInfosResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'kernel_version': 'str',
        'recommend': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'kernel_version': 'kernel_version',
        'recommend': 'recommend'
    }

    def __init__(self, version=None, kernel_version=None, recommend=None):
        r"""VersionInfosResult

        The model defined in huaweicloud sdk

        :param version: **参数解释**: 引擎版本号。 **取值范围**: 不涉及 
        :type version: str
        :param kernel_version: **参数解释**: 内核引擎版本号。 **取值范围**: 不涉及 
        :type kernel_version: str
        :param recommend: **参数解释**: 是否为推荐版本。 **取值范围**: - true：推荐版本 - flase: 非推荐版本 
        :type recommend: bool
        """
        
        

        self._version = None
        self._kernel_version = None
        self._recommend = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if recommend is not None:
            self.recommend = recommend

    @property
    def version(self):
        r"""Gets the version of this VersionInfosResult.

        **参数解释**: 引擎版本号。 **取值范围**: 不涉及 

        :return: The version of this VersionInfosResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VersionInfosResult.

        **参数解释**: 引擎版本号。 **取值范围**: 不涉及 

        :param version: The version of this VersionInfosResult.
        :type version: str
        """
        self._version = version

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this VersionInfosResult.

        **参数解释**: 内核引擎版本号。 **取值范围**: 不涉及 

        :return: The kernel_version of this VersionInfosResult.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this VersionInfosResult.

        **参数解释**: 内核引擎版本号。 **取值范围**: 不涉及 

        :param kernel_version: The kernel_version of this VersionInfosResult.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def recommend(self):
        r"""Gets the recommend of this VersionInfosResult.

        **参数解释**: 是否为推荐版本。 **取值范围**: - true：推荐版本 - flase: 非推荐版本 

        :return: The recommend of this VersionInfosResult.
        :rtype: bool
        """
        return self._recommend

    @recommend.setter
    def recommend(self, recommend):
        r"""Sets the recommend of this VersionInfosResult.

        **参数解释**: 是否为推荐版本。 **取值范围**: - true：推荐版本 - flase: 非推荐版本 

        :param recommend: The recommend of this VersionInfosResult.
        :type recommend: bool
        """
        self._recommend = recommend

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
        if not isinstance(other, VersionInfosResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
