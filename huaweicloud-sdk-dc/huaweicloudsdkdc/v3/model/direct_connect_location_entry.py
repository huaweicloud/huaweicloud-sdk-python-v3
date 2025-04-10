# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectConnectLocationEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'region_id': 'str',
        'site_code': 'str',
        'address': 'AddressBody',
        'locales': 'LocalesBody',
        'provider_list': 'list[ProviderResponseBody]',
        'public_border_group': 'str',
        'latitude': 'str',
        'longitude': 'str',
        'description': 'str',
        'created_time': 'datetime',
        'updated_time': 'datetime',
        'available_port_speeds': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region_id': 'region_id',
        'site_code': 'site_code',
        'address': 'address',
        'locales': 'locales',
        'provider_list': 'provider_list',
        'public_border_group': 'public_border_group',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'description': 'description',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'available_port_speeds': 'available_port_speeds'
    }

    def __init__(self, id=None, name=None, region_id=None, site_code=None, address=None, locales=None, provider_list=None, public_border_group=None, latitude=None, longitude=None, description=None, created_time=None, updated_time=None, available_port_speeds=None):
        r"""DirectConnectLocationEntry

        The model defined in huaweicloud sdk

        :param id: 专线接入站点资源的ID
        :type id: str
        :param name: 专线接入点的名称
        :type name: str
        :param region_id: Location所属Region
        :type region_id: str
        :param site_code: 专线接入点对应的站点编码
        :type site_code: str
        :param address: 
        :type address: :class:`huaweicloudsdkdc.v3.AddressBody`
        :param locales: 
        :type locales: :class:`huaweicloudsdkdc.v3.LocalesBody`
        :param provider_list: 可支持的运营商列表。
        :type provider_list: list[:class:`huaweicloudsdkdc.v3.ProviderResponseBody`]
        :param public_border_group: 专线接入点所属public_border_group
        :type public_border_group: str
        :param latitude: 地理位置纬度
        :type latitude: str
        :param longitude: 地理位置经度
        :type longitude: str
        :param description: 描述信息。
        :type description: str
        :param created_time: 创建时间。
        :type created_time: datetime
        :param updated_time: 更新时间。
        :type updated_time: datetime
        :param available_port_speeds: 接入点内设备可选的端口类型
        :type available_port_speeds: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._region_id = None
        self._site_code = None
        self._address = None
        self._locales = None
        self._provider_list = None
        self._public_border_group = None
        self._latitude = None
        self._longitude = None
        self._description = None
        self._created_time = None
        self._updated_time = None
        self._available_port_speeds = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if site_code is not None:
            self.site_code = site_code
        if address is not None:
            self.address = address
        if locales is not None:
            self.locales = locales
        if provider_list is not None:
            self.provider_list = provider_list
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if description is not None:
            self.description = description
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if available_port_speeds is not None:
            self.available_port_speeds = available_port_speeds

    @property
    def id(self):
        r"""Gets the id of this DirectConnectLocationEntry.

        专线接入站点资源的ID

        :return: The id of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DirectConnectLocationEntry.

        专线接入站点资源的ID

        :param id: The id of this DirectConnectLocationEntry.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DirectConnectLocationEntry.

        专线接入点的名称

        :return: The name of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DirectConnectLocationEntry.

        专线接入点的名称

        :param name: The name of this DirectConnectLocationEntry.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this DirectConnectLocationEntry.

        Location所属Region

        :return: The region_id of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this DirectConnectLocationEntry.

        Location所属Region

        :param region_id: The region_id of this DirectConnectLocationEntry.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def site_code(self):
        r"""Gets the site_code of this DirectConnectLocationEntry.

        专线接入点对应的站点编码

        :return: The site_code of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this DirectConnectLocationEntry.

        专线接入点对应的站点编码

        :param site_code: The site_code of this DirectConnectLocationEntry.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def address(self):
        r"""Gets the address of this DirectConnectLocationEntry.

        :return: The address of this DirectConnectLocationEntry.
        :rtype: :class:`huaweicloudsdkdc.v3.AddressBody`
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this DirectConnectLocationEntry.

        :param address: The address of this DirectConnectLocationEntry.
        :type address: :class:`huaweicloudsdkdc.v3.AddressBody`
        """
        self._address = address

    @property
    def locales(self):
        r"""Gets the locales of this DirectConnectLocationEntry.

        :return: The locales of this DirectConnectLocationEntry.
        :rtype: :class:`huaweicloudsdkdc.v3.LocalesBody`
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        r"""Sets the locales of this DirectConnectLocationEntry.

        :param locales: The locales of this DirectConnectLocationEntry.
        :type locales: :class:`huaweicloudsdkdc.v3.LocalesBody`
        """
        self._locales = locales

    @property
    def provider_list(self):
        r"""Gets the provider_list of this DirectConnectLocationEntry.

        可支持的运营商列表。

        :return: The provider_list of this DirectConnectLocationEntry.
        :rtype: list[:class:`huaweicloudsdkdc.v3.ProviderResponseBody`]
        """
        return self._provider_list

    @provider_list.setter
    def provider_list(self, provider_list):
        r"""Sets the provider_list of this DirectConnectLocationEntry.

        可支持的运营商列表。

        :param provider_list: The provider_list of this DirectConnectLocationEntry.
        :type provider_list: list[:class:`huaweicloudsdkdc.v3.ProviderResponseBody`]
        """
        self._provider_list = provider_list

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this DirectConnectLocationEntry.

        专线接入点所属public_border_group

        :return: The public_border_group of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this DirectConnectLocationEntry.

        专线接入点所属public_border_group

        :param public_border_group: The public_border_group of this DirectConnectLocationEntry.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def latitude(self):
        r"""Gets the latitude of this DirectConnectLocationEntry.

        地理位置纬度

        :return: The latitude of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        r"""Sets the latitude of this DirectConnectLocationEntry.

        地理位置纬度

        :param latitude: The latitude of this DirectConnectLocationEntry.
        :type latitude: str
        """
        self._latitude = latitude

    @property
    def longitude(self):
        r"""Gets the longitude of this DirectConnectLocationEntry.

        地理位置经度

        :return: The longitude of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        r"""Sets the longitude of this DirectConnectLocationEntry.

        地理位置经度

        :param longitude: The longitude of this DirectConnectLocationEntry.
        :type longitude: str
        """
        self._longitude = longitude

    @property
    def description(self):
        r"""Gets the description of this DirectConnectLocationEntry.

        描述信息。

        :return: The description of this DirectConnectLocationEntry.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DirectConnectLocationEntry.

        描述信息。

        :param description: The description of this DirectConnectLocationEntry.
        :type description: str
        """
        self._description = description

    @property
    def created_time(self):
        r"""Gets the created_time of this DirectConnectLocationEntry.

        创建时间。

        :return: The created_time of this DirectConnectLocationEntry.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this DirectConnectLocationEntry.

        创建时间。

        :param created_time: The created_time of this DirectConnectLocationEntry.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this DirectConnectLocationEntry.

        更新时间。

        :return: The updated_time of this DirectConnectLocationEntry.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this DirectConnectLocationEntry.

        更新时间。

        :param updated_time: The updated_time of this DirectConnectLocationEntry.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def available_port_speeds(self):
        r"""Gets the available_port_speeds of this DirectConnectLocationEntry.

        接入点内设备可选的端口类型

        :return: The available_port_speeds of this DirectConnectLocationEntry.
        :rtype: list[str]
        """
        return self._available_port_speeds

    @available_port_speeds.setter
    def available_port_speeds(self, available_port_speeds):
        r"""Sets the available_port_speeds of this DirectConnectLocationEntry.

        接入点内设备可选的端口类型

        :param available_port_speeds: The available_port_speeds of this DirectConnectLocationEntry.
        :type available_port_speeds: list[str]
        """
        self._available_port_speeds = available_port_speeds

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
        if not isinstance(other, DirectConnectLocationEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
