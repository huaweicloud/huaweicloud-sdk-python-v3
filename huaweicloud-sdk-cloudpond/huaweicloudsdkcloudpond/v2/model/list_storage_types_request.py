# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStorageTypesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_code': 'str',
        'name': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'zone_code': 'zone_code',
        'name': 'name',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, zone_code=None, name=None, limit=None, marker=None):
        r"""ListStorageTypesRequest

        The model defined in huaweicloud sdk

        :param zone_code: 地区编码
        :type zone_code: str
        :param name: 存储类型名称
        :type name: str
        :param limit: 每页的数量
        :type limit: int
        :param marker: 分页标识
        :type marker: str
        """
        
        

        self._zone_code = None
        self._name = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if zone_code is not None:
            self.zone_code = zone_code
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def zone_code(self):
        r"""Gets the zone_code of this ListStorageTypesRequest.

        地区编码

        :return: The zone_code of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        r"""Sets the zone_code of this ListStorageTypesRequest.

        地区编码

        :param zone_code: The zone_code of this ListStorageTypesRequest.
        :type zone_code: str
        """
        self._zone_code = zone_code

    @property
    def name(self):
        r"""Gets the name of this ListStorageTypesRequest.

        存储类型名称

        :return: The name of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListStorageTypesRequest.

        存储类型名称

        :param name: The name of this ListStorageTypesRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListStorageTypesRequest.

        每页的数量

        :return: The limit of this ListStorageTypesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListStorageTypesRequest.

        每页的数量

        :param limit: The limit of this ListStorageTypesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListStorageTypesRequest.

        分页标识

        :return: The marker of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListStorageTypesRequest.

        分页标识

        :param marker: The marker of this ListStorageTypesRequest.
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
        if not isinstance(other, ListStorageTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
