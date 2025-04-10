# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSitesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'id': 'str',
        'area': 'str',
        'province': 'str',
        'city': 'str',
        'flavor': 'str',
        'volume_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'id': 'id',
        'area': 'area',
        'province': 'province',
        'city': 'city',
        'flavor': 'flavor',
        'volume_type': 'volume_type'
    }

    def __init__(self, limit=None, offset=None, id=None, area=None, province=None, city=None, flavor=None, volume_type=None):
        r"""ListSitesRequest

        The model defined in huaweicloud sdk

        :param limit: 查询返回边缘站点列表当前页面的数量。 取值范围：0~1000。
        :type limit: int
        :param offset: 查询的偏移量。默认为0。
        :type offset: int
        :param id: 查询条件，站点ID。
        :type id: str
        :param area: 边缘实例所在大区。   大小写通用，皆支持。 支持多个查询，中间使用&#39;,&#39;分隔。
        :type area: str
        :param province: 边缘实例所在省份。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。
        :type province: str
        :param city: 边缘实例所在城市。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。
        :type city: str
        :param flavor: 边缘实例规格。
        :type flavor: str
        :param volume_type: 过滤支持磁盘类型的站点，多个类型之间用“,”分割。
        :type volume_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._id = None
        self._area = None
        self._province = None
        self._city = None
        self._flavor = None
        self._volume_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if id is not None:
            self.id = id
        if area is not None:
            self.area = area
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if flavor is not None:
            self.flavor = flavor
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def limit(self):
        r"""Gets the limit of this ListSitesRequest.

        查询返回边缘站点列表当前页面的数量。 取值范围：0~1000。

        :return: The limit of this ListSitesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSitesRequest.

        查询返回边缘站点列表当前页面的数量。 取值范围：0~1000。

        :param limit: The limit of this ListSitesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSitesRequest.

        查询的偏移量。默认为0。

        :return: The offset of this ListSitesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSitesRequest.

        查询的偏移量。默认为0。

        :param offset: The offset of this ListSitesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def id(self):
        r"""Gets the id of this ListSitesRequest.

        查询条件，站点ID。

        :return: The id of this ListSitesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSitesRequest.

        查询条件，站点ID。

        :param id: The id of this ListSitesRequest.
        :type id: str
        """
        self._id = id

    @property
    def area(self):
        r"""Gets the area of this ListSitesRequest.

        边缘实例所在大区。   大小写通用，皆支持。 支持多个查询，中间使用','分隔。

        :return: The area of this ListSitesRequest.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        r"""Sets the area of this ListSitesRequest.

        边缘实例所在大区。   大小写通用，皆支持。 支持多个查询，中间使用','分隔。

        :param area: The area of this ListSitesRequest.
        :type area: str
        """
        self._area = area

    @property
    def province(self):
        r"""Gets the province of this ListSitesRequest.

        边缘实例所在省份。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :return: The province of this ListSitesRequest.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this ListSitesRequest.

        边缘实例所在省份。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :param province: The province of this ListSitesRequest.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        r"""Gets the city of this ListSitesRequest.

        边缘实例所在城市。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :return: The city of this ListSitesRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this ListSitesRequest.

        边缘实例所在城市。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :param city: The city of this ListSitesRequest.
        :type city: str
        """
        self._city = city

    @property
    def flavor(self):
        r"""Gets the flavor of this ListSitesRequest.

        边缘实例规格。

        :return: The flavor of this ListSitesRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ListSitesRequest.

        边缘实例规格。

        :param flavor: The flavor of this ListSitesRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def volume_type(self):
        r"""Gets the volume_type of this ListSitesRequest.

        过滤支持磁盘类型的站点，多个类型之间用“,”分割。

        :return: The volume_type of this ListSitesRequest.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this ListSitesRequest.

        过滤支持磁盘类型的站点，多个类型之间用“,”分割。

        :param volume_type: The volume_type of this ListSitesRequest.
        :type volume_type: str
        """
        self._volume_type = volume_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSitesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
