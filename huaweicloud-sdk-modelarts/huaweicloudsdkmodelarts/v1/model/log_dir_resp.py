# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogDirResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pfs': 'PFSSummaryResp'
    }

    attribute_map = {
        'pfs': 'pfs'
    }

    def __init__(self, pfs=None):
        r"""LogDirResp

        The model defined in huaweicloud sdk

        :param pfs: 
        :type pfs: :class:`huaweicloudsdkmodelarts.v1.PFSSummaryResp`
        """
        
        

        self._pfs = None
        self.discriminator = None

        self.pfs = pfs

    @property
    def pfs(self):
        r"""Gets the pfs of this LogDirResp.

        :return: The pfs of this LogDirResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PFSSummaryResp`
        """
        return self._pfs

    @pfs.setter
    def pfs(self, pfs):
        r"""Sets the pfs of this LogDirResp.

        :param pfs: The pfs of this LogDirResp.
        :type pfs: :class:`huaweicloudsdkmodelarts.v1.PFSSummaryResp`
        """
        self._pfs = pfs

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
        if not isinstance(other, LogDirResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
