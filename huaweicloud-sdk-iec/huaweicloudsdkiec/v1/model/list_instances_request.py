# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequest:

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
        'status': 'str',
        'name': 'str',
        'area': 'str',
        'province': 'str',
        'city': 'str',
        'edgecloud_id': 'str',
        'site_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'name': 'name',
        'area': 'area',
        'province': 'province',
        'city': 'city',
        'edgecloud_id': 'edgecloud_id',
        'site_id': 'site_id'
    }

    def __init__(self, offset=None, limit=None, status=None, name=None, area=None, province=None, city=None, edgecloud_id=None, site_id=None):
        """ListInstancesRequest

        The model defined in huaweicloud sdk

        :param offset: 页码。 当前页面数，默认为0。 取值大于等于0，取值为0时返回第1页
        :type offset: int
        :param limit: 查询返回边缘实例列表当前页面的数量。 每页默认值是25，最多返回1000台边缘实例的信息，如果数据量过大建议设置成100。
        :type limit: int
        :param status: 边缘实例的状态。 取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE。  非上面范围的status字段将返回空列表。 &gt; 当边缘实例处于中间状态时，查询范围如下： - ACTIVE，查询范围：ACTIVE，REBOOT，HARD_REBOOT，REBUILD，MIGRATING - SHUTOFF，查询范围：SHUTOFF，RESIZE，REBUILD - ERROR，查询范围：ERROR，REBUILD - VERIFY_RESIZE，查询范围：VERIFY_RESIZE，REVERT_RESIZE
        :type status: str
        :param name: 查询条件，边缘实例名称。
        :type name: str
        :param area: 边缘实例所在大区。
        :type area: str
        :param province: 边缘实例所在省份。
        :type province: str
        :param city: 边缘实例所在城市。
        :type city: str
        :param edgecloud_id: 边缘业务ID。
        :type edgecloud_id: str
        :param site_id: 站点ID。
        :type site_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._status = None
        self._name = None
        self._area = None
        self._province = None
        self._city = None
        self._edgecloud_id = None
        self._site_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if area is not None:
            self.area = area
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if edgecloud_id is not None:
            self.edgecloud_id = edgecloud_id
        if site_id is not None:
            self.site_id = site_id

    @property
    def offset(self):
        """Gets the offset of this ListInstancesRequest.

        页码。 当前页面数，默认为0。 取值大于等于0，取值为0时返回第1页

        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesRequest.

        页码。 当前页面数，默认为0。 取值大于等于0，取值为0时返回第1页

        :param offset: The offset of this ListInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListInstancesRequest.

        查询返回边缘实例列表当前页面的数量。 每页默认值是25，最多返回1000台边缘实例的信息，如果数据量过大建议设置成100。

        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesRequest.

        查询返回边缘实例列表当前页面的数量。 每页默认值是25，最多返回1000台边缘实例的信息，如果数据量过大建议设置成100。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this ListInstancesRequest.

        边缘实例的状态。 取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE。  非上面范围的status字段将返回空列表。 > 当边缘实例处于中间状态时，查询范围如下： - ACTIVE，查询范围：ACTIVE，REBOOT，HARD_REBOOT，REBUILD，MIGRATING - SHUTOFF，查询范围：SHUTOFF，RESIZE，REBUILD - ERROR，查询范围：ERROR，REBUILD - VERIFY_RESIZE，查询范围：VERIFY_RESIZE，REVERT_RESIZE

        :return: The status of this ListInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesRequest.

        边缘实例的状态。 取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE。  非上面范围的status字段将返回空列表。 > 当边缘实例处于中间状态时，查询范围如下： - ACTIVE，查询范围：ACTIVE，REBOOT，HARD_REBOOT，REBUILD，MIGRATING - SHUTOFF，查询范围：SHUTOFF，RESIZE，REBUILD - ERROR，查询范围：ERROR，REBUILD - VERIFY_RESIZE，查询范围：VERIFY_RESIZE，REVERT_RESIZE

        :param status: The status of this ListInstancesRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ListInstancesRequest.

        查询条件，边缘实例名称。

        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesRequest.

        查询条件，边缘实例名称。

        :param name: The name of this ListInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def area(self):
        """Gets the area of this ListInstancesRequest.

        边缘实例所在大区。

        :return: The area of this ListInstancesRequest.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this ListInstancesRequest.

        边缘实例所在大区。

        :param area: The area of this ListInstancesRequest.
        :type area: str
        """
        self._area = area

    @property
    def province(self):
        """Gets the province of this ListInstancesRequest.

        边缘实例所在省份。

        :return: The province of this ListInstancesRequest.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this ListInstancesRequest.

        边缘实例所在省份。

        :param province: The province of this ListInstancesRequest.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this ListInstancesRequest.

        边缘实例所在城市。

        :return: The city of this ListInstancesRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ListInstancesRequest.

        边缘实例所在城市。

        :param city: The city of this ListInstancesRequest.
        :type city: str
        """
        self._city = city

    @property
    def edgecloud_id(self):
        """Gets the edgecloud_id of this ListInstancesRequest.

        边缘业务ID。

        :return: The edgecloud_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._edgecloud_id

    @edgecloud_id.setter
    def edgecloud_id(self, edgecloud_id):
        """Sets the edgecloud_id of this ListInstancesRequest.

        边缘业务ID。

        :param edgecloud_id: The edgecloud_id of this ListInstancesRequest.
        :type edgecloud_id: str
        """
        self._edgecloud_id = edgecloud_id

    @property
    def site_id(self):
        """Gets the site_id of this ListInstancesRequest.

        站点ID。

        :return: The site_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ListInstancesRequest.

        站点ID。

        :param site_id: The site_id of this ListInstancesRequest.
        :type site_id: str
        """
        self._site_id = site_id

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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
