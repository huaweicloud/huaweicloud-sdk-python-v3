# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PFSSummaryResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pfs_path': 'str'
    }

    attribute_map = {
        'pfs_path': 'pfs_path'
    }

    def __init__(self, pfs_path=None):
        r"""PFSSummaryResp

        The model defined in huaweicloud sdk

        :param pfs_path: **参数解释**：obs并行文件系统路径url。 **取值范围**：不涉及。
        :type pfs_path: str
        """
        
        

        self._pfs_path = None
        self.discriminator = None

        self.pfs_path = pfs_path

    @property
    def pfs_path(self):
        r"""Gets the pfs_path of this PFSSummaryResp.

        **参数解释**：obs并行文件系统路径url。 **取值范围**：不涉及。

        :return: The pfs_path of this PFSSummaryResp.
        :rtype: str
        """
        return self._pfs_path

    @pfs_path.setter
    def pfs_path(self, pfs_path):
        r"""Sets the pfs_path of this PFSSummaryResp.

        **参数解释**：obs并行文件系统路径url。 **取值范围**：不涉及。

        :param pfs_path: The pfs_path of this PFSSummaryResp.
        :type pfs_path: str
        """
        self._pfs_path = pfs_path

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
        if not isinstance(other, PFSSummaryResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
