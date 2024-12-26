# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGdgwRouteTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[str]',
        'ext_fields': 'list[str]',
        'gdgw_id': 'str',
        'nexthop': 'list[str]',
        'destination': 'list[str]',
        'address_family': 'list[str]'
    }

    attribute_map = {
        'fields': 'fields',
        'ext_fields': 'ext_fields',
        'gdgw_id': 'gdgw_id',
        'nexthop': 'nexthop',
        'destination': 'destination',
        'address_family': 'address_family'
    }

    def __init__(self, fields=None, ext_fields=None, gdgw_id=None, nexthop=None, destination=None, address_family=None):
        """ListGdgwRouteTablesRequest

        The model defined in huaweicloud sdk

        :param fields: 显示字段列表
        :type fields: list[str]
        :param ext_fields: show response ext-fields
        :type ext_fields: list[str]
        :param gdgw_id: 全域接入网关ID
        :type gdgw_id: str
        :param nexthop: 下一条ID
        :type nexthop: list[str]
        :param destination: 目的地址
        :type destination: list[str]
        :param address_family: 地址簇
        :type address_family: list[str]
        """
        
        

        self._fields = None
        self._ext_fields = None
        self._gdgw_id = None
        self._nexthop = None
        self._destination = None
        self._address_family = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if ext_fields is not None:
            self.ext_fields = ext_fields
        self.gdgw_id = gdgw_id
        if nexthop is not None:
            self.nexthop = nexthop
        if destination is not None:
            self.destination = destination
        if address_family is not None:
            self.address_family = address_family

    @property
    def fields(self):
        """Gets the fields of this ListGdgwRouteTablesRequest.

        显示字段列表

        :return: The fields of this ListGdgwRouteTablesRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListGdgwRouteTablesRequest.

        显示字段列表

        :param fields: The fields of this ListGdgwRouteTablesRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def ext_fields(self):
        """Gets the ext_fields of this ListGdgwRouteTablesRequest.

        show response ext-fields

        :return: The ext_fields of this ListGdgwRouteTablesRequest.
        :rtype: list[str]
        """
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        """Sets the ext_fields of this ListGdgwRouteTablesRequest.

        show response ext-fields

        :param ext_fields: The ext_fields of this ListGdgwRouteTablesRequest.
        :type ext_fields: list[str]
        """
        self._ext_fields = ext_fields

    @property
    def gdgw_id(self):
        """Gets the gdgw_id of this ListGdgwRouteTablesRequest.

        全域接入网关ID

        :return: The gdgw_id of this ListGdgwRouteTablesRequest.
        :rtype: str
        """
        return self._gdgw_id

    @gdgw_id.setter
    def gdgw_id(self, gdgw_id):
        """Sets the gdgw_id of this ListGdgwRouteTablesRequest.

        全域接入网关ID

        :param gdgw_id: The gdgw_id of this ListGdgwRouteTablesRequest.
        :type gdgw_id: str
        """
        self._gdgw_id = gdgw_id

    @property
    def nexthop(self):
        """Gets the nexthop of this ListGdgwRouteTablesRequest.

        下一条ID

        :return: The nexthop of this ListGdgwRouteTablesRequest.
        :rtype: list[str]
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this ListGdgwRouteTablesRequest.

        下一条ID

        :param nexthop: The nexthop of this ListGdgwRouteTablesRequest.
        :type nexthop: list[str]
        """
        self._nexthop = nexthop

    @property
    def destination(self):
        """Gets the destination of this ListGdgwRouteTablesRequest.

        目的地址

        :return: The destination of this ListGdgwRouteTablesRequest.
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ListGdgwRouteTablesRequest.

        目的地址

        :param destination: The destination of this ListGdgwRouteTablesRequest.
        :type destination: list[str]
        """
        self._destination = destination

    @property
    def address_family(self):
        """Gets the address_family of this ListGdgwRouteTablesRequest.

        地址簇

        :return: The address_family of this ListGdgwRouteTablesRequest.
        :rtype: list[str]
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this ListGdgwRouteTablesRequest.

        地址簇

        :param address_family: The address_family of this ListGdgwRouteTablesRequest.
        :type address_family: list[str]
        """
        self._address_family = address_family

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
        if not isinstance(other, ListGdgwRouteTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
