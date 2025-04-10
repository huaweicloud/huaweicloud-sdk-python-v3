# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'area': 'str',
        'province': 'str',
        'city': 'str',
        'operator': 'str',
        'id': 'str',
        'site_ids': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'area': 'area',
        'province': 'province',
        'city': 'city',
        'operator': 'operator',
        'id': 'id',
        'site_ids': 'site_ids'
    }

    def __init__(self, offset=None, limit=None, name=None, area=None, province=None, city=None, operator=None, id=None, site_ids=None):
        r"""ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param offset: 页码。 当前页面数，默认为1。 取值大于等于0，取值为0时返回第1页。
        :type offset: int
        :param limit: 查询返回边缘实例规格列表当前页面的数量 。 取值范围：0~1000。
        :type limit: int
        :param name: 查询条件，规格的名称。
        :type name: str
        :param area: 边缘规格所在大区。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。
        :type area: str
        :param province: 边缘规格所在省份。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。
        :type province: str
        :param city: 边缘规格所在城市。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。
        :type city: str
        :param operator: 边缘规格支持运营商。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。
        :type operator: str
        :param id: 查询条件，规格的ID。
        :type id: str
        :param site_ids: 查询条件，边缘规格站点列表，站点之间用“,”分隔。
        :type site_ids: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._area = None
        self._province = None
        self._city = None
        self._operator = None
        self._id = None
        self._site_ids = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if area is not None:
            self.area = area
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if operator is not None:
            self.operator = operator
        if id is not None:
            self.id = id
        if site_ids is not None:
            self.site_ids = site_ids

    @property
    def offset(self):
        r"""Gets the offset of this ListFlavorsRequest.

        页码。 当前页面数，默认为1。 取值大于等于0，取值为0时返回第1页。

        :return: The offset of this ListFlavorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFlavorsRequest.

        页码。 当前页面数，默认为1。 取值大于等于0，取值为0时返回第1页。

        :param offset: The offset of this ListFlavorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFlavorsRequest.

        查询返回边缘实例规格列表当前页面的数量 。 取值范围：0~1000。

        :return: The limit of this ListFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlavorsRequest.

        查询返回边缘实例规格列表当前页面的数量 。 取值范围：0~1000。

        :param limit: The limit of this ListFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListFlavorsRequest.

        查询条件，规格的名称。

        :return: The name of this ListFlavorsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFlavorsRequest.

        查询条件，规格的名称。

        :param name: The name of this ListFlavorsRequest.
        :type name: str
        """
        self._name = name

    @property
    def area(self):
        r"""Gets the area of this ListFlavorsRequest.

        边缘规格所在大区。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :return: The area of this ListFlavorsRequest.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        r"""Sets the area of this ListFlavorsRequest.

        边缘规格所在大区。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :param area: The area of this ListFlavorsRequest.
        :type area: str
        """
        self._area = area

    @property
    def province(self):
        r"""Gets the province of this ListFlavorsRequest.

        边缘规格所在省份。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :return: The province of this ListFlavorsRequest.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this ListFlavorsRequest.

        边缘规格所在省份。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :param province: The province of this ListFlavorsRequest.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        r"""Gets the city of this ListFlavorsRequest.

        边缘规格所在城市。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :return: The city of this ListFlavorsRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this ListFlavorsRequest.

        边缘规格所在城市。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :param city: The city of this ListFlavorsRequest.
        :type city: str
        """
        self._city = city

    @property
    def operator(self):
        r"""Gets the operator of this ListFlavorsRequest.

        边缘规格支持运营商。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :return: The operator of this ListFlavorsRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ListFlavorsRequest.

        边缘规格支持运营商。  大小写通用，皆支持。 支持多个查询，中间使用“,”分隔。

        :param operator: The operator of this ListFlavorsRequest.
        :type operator: str
        """
        self._operator = operator

    @property
    def id(self):
        r"""Gets the id of this ListFlavorsRequest.

        查询条件，规格的ID。

        :return: The id of this ListFlavorsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListFlavorsRequest.

        查询条件，规格的ID。

        :param id: The id of this ListFlavorsRequest.
        :type id: str
        """
        self._id = id

    @property
    def site_ids(self):
        r"""Gets the site_ids of this ListFlavorsRequest.

        查询条件，边缘规格站点列表，站点之间用“,”分隔。

        :return: The site_ids of this ListFlavorsRequest.
        :rtype: str
        """
        return self._site_ids

    @site_ids.setter
    def site_ids(self, site_ids):
        r"""Sets the site_ids of this ListFlavorsRequest.

        查询条件，边缘规格站点列表，站点之间用“,”分隔。

        :param site_ids: The site_ids of this ListFlavorsRequest.
        :type site_ids: str
        """
        self._site_ids = site_ids

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
