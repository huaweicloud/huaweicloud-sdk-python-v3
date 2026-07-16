# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolStatusResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creating': 'PoolResourceFlavorCount',
        'available': 'PoolResourceFlavorCount',
        'abnormal': 'PoolResourceFlavorCount',
        'deleting': 'PoolResourceFlavorCount'
    }

    attribute_map = {
        'creating': 'creating',
        'available': 'available',
        'abnormal': 'abnormal',
        'deleting': 'deleting'
    }

    def __init__(self, creating=None, available=None, abnormal=None, deleting=None):
        r"""NodePoolStatusResources

        The model defined in huaweicloud sdk

        :param creating: 
        :type creating: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        :param available: 
        :type available: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        :param abnormal: 
        :type abnormal: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        :param deleting: 
        :type deleting: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        
        

        self._creating = None
        self._available = None
        self._abnormal = None
        self._deleting = None
        self.discriminator = None

        if creating is not None:
            self.creating = creating
        if available is not None:
            self.available = available
        if abnormal is not None:
            self.abnormal = abnormal
        if deleting is not None:
            self.deleting = deleting

    @property
    def creating(self):
        r"""Gets the creating of this NodePoolStatusResources.

        :return: The creating of this NodePoolStatusResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        return self._creating

    @creating.setter
    def creating(self, creating):
        r"""Sets the creating of this NodePoolStatusResources.

        :param creating: The creating of this NodePoolStatusResources.
        :type creating: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        self._creating = creating

    @property
    def available(self):
        r"""Gets the available of this NodePoolStatusResources.

        :return: The available of this NodePoolStatusResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        return self._available

    @available.setter
    def available(self, available):
        r"""Sets the available of this NodePoolStatusResources.

        :param available: The available of this NodePoolStatusResources.
        :type available: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        self._available = available

    @property
    def abnormal(self):
        r"""Gets the abnormal of this NodePoolStatusResources.

        :return: The abnormal of this NodePoolStatusResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        return self._abnormal

    @abnormal.setter
    def abnormal(self, abnormal):
        r"""Sets the abnormal of this NodePoolStatusResources.

        :param abnormal: The abnormal of this NodePoolStatusResources.
        :type abnormal: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        self._abnormal = abnormal

    @property
    def deleting(self):
        r"""Gets the deleting of this NodePoolStatusResources.

        :return: The deleting of this NodePoolStatusResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        return self._deleting

    @deleting.setter
    def deleting(self, deleting):
        r"""Sets the deleting of this NodePoolStatusResources.

        :param deleting: The deleting of this NodePoolStatusResources.
        :type deleting: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorCount`
        """
        self._deleting = deleting

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
        if not isinstance(other, NodePoolStatusResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
