# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterRegionBandwidth:

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
        'description': 'str',
        'domain_id': 'str',
        'bandwidth_package_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'cloud_connection_id': 'str',
        'inter_regions': 'list[InterRegion]',
        'bandwidth': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'bandwidth_package_id': 'bandwidth_package_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cloud_connection_id': 'cloud_connection_id',
        'inter_regions': 'inter_regions',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, bandwidth_package_id=None, created_at=None, updated_at=None, cloud_connection_id=None, inter_regions=None, bandwidth=None):
        """InterRegionBandwidth

        The model defined in huaweicloud sdk

        :param id: 域间带宽实例的ID。
        :type id: str
        :param name: 域间带宽实例的名字。
        :type name: str
        :param description: 域间带宽实例的描述。
        :type description: str
        :param domain_id: 帐号ID。
        :type domain_id: str
        :param bandwidth_package_id: 带宽包实例的ID。
        :type bandwidth_package_id: str
        :param created_at: 域间带宽实例的创建时间。
        :type created_at: datetime
        :param updated_at: 域间带宽实例的更新时间。
        :type updated_at: datetime
        :param cloud_connection_id: 云连接实例的ID。
        :type cloud_connection_id: str
        :param inter_regions: 域间实例信息。
        :type inter_regions: list[:class:`huaweicloudsdkcc.v3.InterRegion`]
        :param bandwidth: 域间带宽的值。
        :type bandwidth: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._bandwidth_package_id = None
        self._created_at = None
        self._updated_at = None
        self._cloud_connection_id = None
        self._inter_regions = None
        self._bandwidth = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if bandwidth_package_id is not None:
            self.bandwidth_package_id = bandwidth_package_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if inter_regions is not None:
            self.inter_regions = inter_regions
        if bandwidth is not None:
            self.bandwidth = bandwidth

    @property
    def id(self):
        """Gets the id of this InterRegionBandwidth.

        域间带宽实例的ID。

        :return: The id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterRegionBandwidth.

        域间带宽实例的ID。

        :param id: The id of this InterRegionBandwidth.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this InterRegionBandwidth.

        域间带宽实例的名字。

        :return: The name of this InterRegionBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InterRegionBandwidth.

        域间带宽实例的名字。

        :param name: The name of this InterRegionBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this InterRegionBandwidth.

        域间带宽实例的描述。

        :return: The description of this InterRegionBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InterRegionBandwidth.

        域间带宽实例的描述。

        :param description: The description of this InterRegionBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this InterRegionBandwidth.

        帐号ID。

        :return: The domain_id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this InterRegionBandwidth.

        帐号ID。

        :param domain_id: The domain_id of this InterRegionBandwidth.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this InterRegionBandwidth.

        带宽包实例的ID。

        :return: The bandwidth_package_id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this InterRegionBandwidth.

        带宽包实例的ID。

        :param bandwidth_package_id: The bandwidth_package_id of this InterRegionBandwidth.
        :type bandwidth_package_id: str
        """
        self._bandwidth_package_id = bandwidth_package_id

    @property
    def created_at(self):
        """Gets the created_at of this InterRegionBandwidth.

        域间带宽实例的创建时间。

        :return: The created_at of this InterRegionBandwidth.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InterRegionBandwidth.

        域间带宽实例的创建时间。

        :param created_at: The created_at of this InterRegionBandwidth.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InterRegionBandwidth.

        域间带宽实例的更新时间。

        :return: The updated_at of this InterRegionBandwidth.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InterRegionBandwidth.

        域间带宽实例的更新时间。

        :param updated_at: The updated_at of this InterRegionBandwidth.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this InterRegionBandwidth.

        云连接实例的ID。

        :return: The cloud_connection_id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this InterRegionBandwidth.

        云连接实例的ID。

        :param cloud_connection_id: The cloud_connection_id of this InterRegionBandwidth.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def inter_regions(self):
        """Gets the inter_regions of this InterRegionBandwidth.

        域间实例信息。

        :return: The inter_regions of this InterRegionBandwidth.
        :rtype: list[:class:`huaweicloudsdkcc.v3.InterRegion`]
        """
        return self._inter_regions

    @inter_regions.setter
    def inter_regions(self, inter_regions):
        """Sets the inter_regions of this InterRegionBandwidth.

        域间实例信息。

        :param inter_regions: The inter_regions of this InterRegionBandwidth.
        :type inter_regions: list[:class:`huaweicloudsdkcc.v3.InterRegion`]
        """
        self._inter_regions = inter_regions

    @property
    def bandwidth(self):
        """Gets the bandwidth of this InterRegionBandwidth.

        域间带宽的值。

        :return: The bandwidth of this InterRegionBandwidth.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this InterRegionBandwidth.

        域间带宽的值。

        :param bandwidth: The bandwidth of this InterRegionBandwidth.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

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
        if not isinstance(other, InterRegionBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
