# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CVEAllowlistItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cve_id': 'str'
    }

    attribute_map = {
        'cve_id': 'cve_id'
    }

    def __init__(self, cve_id=None):
        r"""CVEAllowlistItem

        The model defined in huaweicloud sdk

        :param cve_id: CVE的ID, 比如：CVE-2019-10164
        :type cve_id: str
        """
        
        

        self._cve_id = None
        self.discriminator = None

        if cve_id is not None:
            self.cve_id = cve_id

    @property
    def cve_id(self):
        r"""Gets the cve_id of this CVEAllowlistItem.

        CVE的ID, 比如：CVE-2019-10164

        :return: The cve_id of this CVEAllowlistItem.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this CVEAllowlistItem.

        CVE的ID, 比如：CVE-2019-10164

        :param cve_id: The cve_id of this CVEAllowlistItem.
        :type cve_id: str
        """
        self._cve_id = cve_id

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
        if not isinstance(other, CVEAllowlistItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
