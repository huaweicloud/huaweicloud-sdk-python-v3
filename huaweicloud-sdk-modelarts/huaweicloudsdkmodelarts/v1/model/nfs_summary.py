# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NFSSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nfs_path': 'str'
    }

    attribute_map = {
        'nfs_path': 'nfs_path'
    }

    def __init__(self, nfs_path=None):
        r"""NFSSummary

        The model defined in huaweicloud sdk

        :param nfs_path: **参数解释**：sfsTurbo弹性文件系统url。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type nfs_path: str
        """
        
        

        self._nfs_path = None
        self.discriminator = None

        self.nfs_path = nfs_path

    @property
    def nfs_path(self):
        r"""Gets the nfs_path of this NFSSummary.

        **参数解释**：sfsTurbo弹性文件系统url。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The nfs_path of this NFSSummary.
        :rtype: str
        """
        return self._nfs_path

    @nfs_path.setter
    def nfs_path(self, nfs_path):
        r"""Sets the nfs_path of this NFSSummary.

        **参数解释**：sfsTurbo弹性文件系统url。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param nfs_path: The nfs_path of this NFSSummary.
        :type nfs_path: str
        """
        self._nfs_path = nfs_path

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
        if not isinstance(other, NFSSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
