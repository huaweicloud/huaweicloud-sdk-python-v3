# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDedicatedHostTypesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'limit': 'str',
        'marker': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, availability_zone=None, limit=None, marker=None):
        r"""ListDedicatedHostTypesRequest

        The model defined in huaweicloud sdk

        :param availability_zone: AZ。
        :type availability_zone: str
        :param limit: 查询返回云服务器列表当前页面的数量。
        :type limit: str
        :param marker: 以单页最后一条专属主机的host_type作为分页标记
        :type marker: str
        """
        
        

        self._availability_zone = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.availability_zone = availability_zone
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListDedicatedHostTypesRequest.

        AZ。

        :return: The availability_zone of this ListDedicatedHostTypesRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListDedicatedHostTypesRequest.

        AZ。

        :param availability_zone: The availability_zone of this ListDedicatedHostTypesRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def limit(self):
        r"""Gets the limit of this ListDedicatedHostTypesRequest.

        查询返回云服务器列表当前页面的数量。

        :return: The limit of this ListDedicatedHostTypesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDedicatedHostTypesRequest.

        查询返回云服务器列表当前页面的数量。

        :param limit: The limit of this ListDedicatedHostTypesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListDedicatedHostTypesRequest.

        以单页最后一条专属主机的host_type作为分页标记

        :return: The marker of this ListDedicatedHostTypesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListDedicatedHostTypesRequest.

        以单页最后一条专属主机的host_type作为分页标记

        :param marker: The marker of this ListDedicatedHostTypesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListDedicatedHostTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
