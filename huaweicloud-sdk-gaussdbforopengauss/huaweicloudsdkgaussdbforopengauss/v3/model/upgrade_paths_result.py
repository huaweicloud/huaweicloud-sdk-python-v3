# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradePathsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_version': 'str',
        'end_version': 'str'
    }

    attribute_map = {
        'start_version': 'start_version',
        'end_version': 'end_version'
    }

    def __init__(self, start_version=None, end_version=None):
        r"""UpgradePathsResult

        The model defined in huaweicloud sdk

        :param start_version: **参数解释**: 源引擎版本号。 **取值范围**: 不涉及 
        :type start_version: str
        :param end_version: **参数解释**: 目标引擎版本号。 **取值范围**: 不涉及 
        :type end_version: str
        """
        
        

        self._start_version = None
        self._end_version = None
        self.discriminator = None

        if start_version is not None:
            self.start_version = start_version
        if end_version is not None:
            self.end_version = end_version

    @property
    def start_version(self):
        r"""Gets the start_version of this UpgradePathsResult.

        **参数解释**: 源引擎版本号。 **取值范围**: 不涉及 

        :return: The start_version of this UpgradePathsResult.
        :rtype: str
        """
        return self._start_version

    @start_version.setter
    def start_version(self, start_version):
        r"""Sets the start_version of this UpgradePathsResult.

        **参数解释**: 源引擎版本号。 **取值范围**: 不涉及 

        :param start_version: The start_version of this UpgradePathsResult.
        :type start_version: str
        """
        self._start_version = start_version

    @property
    def end_version(self):
        r"""Gets the end_version of this UpgradePathsResult.

        **参数解释**: 目标引擎版本号。 **取值范围**: 不涉及 

        :return: The end_version of this UpgradePathsResult.
        :rtype: str
        """
        return self._end_version

    @end_version.setter
    def end_version(self, end_version):
        r"""Sets the end_version of this UpgradePathsResult.

        **参数解释**: 目标引擎版本号。 **取值范围**: 不涉及 

        :param end_version: The end_version of this UpgradePathsResult.
        :type end_version: str
        """
        self._end_version = end_version

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
        if not isinstance(other, UpgradePathsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
