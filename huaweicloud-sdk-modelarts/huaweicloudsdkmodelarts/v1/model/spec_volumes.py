# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nfs': 'Nfs',
        'pfs': 'Pfs',
        'obs': 'Obs'
    }

    attribute_map = {
        'nfs': 'nfs',
        'pfs': 'pfs',
        'obs': 'obs'
    }

    def __init__(self, nfs=None, pfs=None, obs=None):
        r"""SpecVolumes

        The model defined in huaweicloud sdk

        :param nfs: 
        :type nfs: :class:`huaweicloudsdkmodelarts.v1.Nfs`
        :param pfs: 
        :type pfs: :class:`huaweicloudsdkmodelarts.v1.Pfs`
        :param obs: 
        :type obs: :class:`huaweicloudsdkmodelarts.v1.Obs`
        """
        
        

        self._nfs = None
        self._pfs = None
        self._obs = None
        self.discriminator = None

        if nfs is not None:
            self.nfs = nfs
        if pfs is not None:
            self.pfs = pfs
        if obs is not None:
            self.obs = obs

    @property
    def nfs(self):
        r"""Gets the nfs of this SpecVolumes.

        :return: The nfs of this SpecVolumes.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Nfs`
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        r"""Sets the nfs of this SpecVolumes.

        :param nfs: The nfs of this SpecVolumes.
        :type nfs: :class:`huaweicloudsdkmodelarts.v1.Nfs`
        """
        self._nfs = nfs

    @property
    def pfs(self):
        r"""Gets the pfs of this SpecVolumes.

        :return: The pfs of this SpecVolumes.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Pfs`
        """
        return self._pfs

    @pfs.setter
    def pfs(self, pfs):
        r"""Sets the pfs of this SpecVolumes.

        :param pfs: The pfs of this SpecVolumes.
        :type pfs: :class:`huaweicloudsdkmodelarts.v1.Pfs`
        """
        self._pfs = pfs

    @property
    def obs(self):
        r"""Gets the obs of this SpecVolumes.

        :return: The obs of this SpecVolumes.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Obs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this SpecVolumes.

        :param obs: The obs of this SpecVolumes.
        :type obs: :class:`huaweicloudsdkmodelarts.v1.Obs`
        """
        self._obs = obs

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
        if not isinstance(other, SpecVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
