# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobVolumeResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nfs': 'NfsResp'
    }

    attribute_map = {
        'nfs': 'nfs'
    }

    def __init__(self, nfs=None):
        r"""JobVolumeResp

        The model defined in huaweicloud sdk

        :param nfs: 
        :type nfs: :class:`huaweicloudsdkmodelarts.v1.NfsResp`
        """
        
        

        self._nfs = None
        self.discriminator = None

        if nfs is not None:
            self.nfs = nfs

    @property
    def nfs(self):
        r"""Gets the nfs of this JobVolumeResp.

        :return: The nfs of this JobVolumeResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NfsResp`
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        r"""Sets the nfs of this JobVolumeResp.

        :param nfs: The nfs of this JobVolumeResp.
        :type nfs: :class:`huaweicloudsdkmodelarts.v1.NfsResp`
        """
        self._nfs = nfs

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
        if not isinstance(other, JobVolumeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
