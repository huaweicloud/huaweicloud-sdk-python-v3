# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDedicatedHostAllTypesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'availability_zone': 'str',
        'limit': 'str',
        'marker': 'str',
        'host_type': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'availability_zone': 'availability_zone',
        'limit': 'limit',
        'marker': 'marker',
        'host_type': 'host_type'
    }

    def __init__(self, flavor=None, availability_zone=None, limit=None, marker=None, host_type=None):
        r"""ListDedicatedHostAllTypesRequest

        The model defined in huaweicloud sdk

        :param flavor: 
        :type flavor: str
        :param availability_zone: 
        :type availability_zone: str
        :param limit: 
        :type limit: str
        :param marker: 
        :type marker: str
        :param host_type: 
        :type host_type: str
        """
        
        

        self._flavor = None
        self._availability_zone = None
        self._limit = None
        self._marker = None
        self._host_type = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if host_type is not None:
            self.host_type = host_type

    @property
    def flavor(self):
        r"""Gets the flavor of this ListDedicatedHostAllTypesRequest.

        :return: The flavor of this ListDedicatedHostAllTypesRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ListDedicatedHostAllTypesRequest.

        :param flavor: The flavor of this ListDedicatedHostAllTypesRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListDedicatedHostAllTypesRequest.

        :return: The availability_zone of this ListDedicatedHostAllTypesRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListDedicatedHostAllTypesRequest.

        :param availability_zone: The availability_zone of this ListDedicatedHostAllTypesRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def limit(self):
        r"""Gets the limit of this ListDedicatedHostAllTypesRequest.

        :return: The limit of this ListDedicatedHostAllTypesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDedicatedHostAllTypesRequest.

        :param limit: The limit of this ListDedicatedHostAllTypesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListDedicatedHostAllTypesRequest.

        :return: The marker of this ListDedicatedHostAllTypesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListDedicatedHostAllTypesRequest.

        :param marker: The marker of this ListDedicatedHostAllTypesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def host_type(self):
        r"""Gets the host_type of this ListDedicatedHostAllTypesRequest.

        :return: The host_type of this ListDedicatedHostAllTypesRequest.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this ListDedicatedHostAllTypesRequest.

        :param host_type: The host_type of this ListDedicatedHostAllTypesRequest.
        :type host_type: str
        """
        self._host_type = host_type

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
        if not isinstance(other, ListDedicatedHostAllTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
