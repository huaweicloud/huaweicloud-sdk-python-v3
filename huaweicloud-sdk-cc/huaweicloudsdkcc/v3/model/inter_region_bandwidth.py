# coding: utf-8

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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'cloud_connection_id': 'str',
        'bandwidth_package_id': 'str',
        'inter_regions': 'list[InterRegion]',
        'bandwidth': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cloud_connection_id': 'cloud_connection_id',
        'bandwidth_package_id': 'bandwidth_package_id',
        'inter_regions': 'inter_regions',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, created_at=None, updated_at=None, cloud_connection_id=None, bandwidth_package_id=None, inter_regions=None, bandwidth=None):
        r"""InterRegionBandwidth

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param cloud_connection_id: 云连接实例ID。
        :type cloud_connection_id: str
        :param bandwidth_package_id: 带宽包实例ID。
        :type bandwidth_package_id: str
        :param inter_regions: 域间实例信息。
        :type inter_regions: list[:class:`huaweicloudsdkcc.v3.InterRegion`]
        :param bandwidth: 带宽值，单位Mbps。
        :type bandwidth: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._created_at = None
        self._updated_at = None
        self._cloud_connection_id = None
        self._bandwidth_package_id = None
        self._inter_regions = None
        self._bandwidth = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.domain_id = domain_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.cloud_connection_id = cloud_connection_id
        self.bandwidth_package_id = bandwidth_package_id
        if inter_regions is not None:
            self.inter_regions = inter_regions
        if bandwidth is not None:
            self.bandwidth = bandwidth

    @property
    def id(self):
        r"""Gets the id of this InterRegionBandwidth.

        实例ID。

        :return: The id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InterRegionBandwidth.

        实例ID。

        :param id: The id of this InterRegionBandwidth.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this InterRegionBandwidth.

        实例名称。

        :return: The name of this InterRegionBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InterRegionBandwidth.

        实例名称。

        :param name: The name of this InterRegionBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this InterRegionBandwidth.

        实例描述。不支持 <>。

        :return: The description of this InterRegionBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InterRegionBandwidth.

        实例描述。不支持 <>。

        :param description: The description of this InterRegionBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this InterRegionBandwidth.

        实例所属账号ID。

        :return: The domain_id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this InterRegionBandwidth.

        实例所属账号ID。

        :param domain_id: The domain_id of this InterRegionBandwidth.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def created_at(self):
        r"""Gets the created_at of this InterRegionBandwidth.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this InterRegionBandwidth.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this InterRegionBandwidth.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this InterRegionBandwidth.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this InterRegionBandwidth.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this InterRegionBandwidth.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this InterRegionBandwidth.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this InterRegionBandwidth.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this InterRegionBandwidth.

        云连接实例ID。

        :return: The cloud_connection_id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this InterRegionBandwidth.

        云连接实例ID。

        :param cloud_connection_id: The cloud_connection_id of this InterRegionBandwidth.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def bandwidth_package_id(self):
        r"""Gets the bandwidth_package_id of this InterRegionBandwidth.

        带宽包实例ID。

        :return: The bandwidth_package_id of this InterRegionBandwidth.
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        r"""Sets the bandwidth_package_id of this InterRegionBandwidth.

        带宽包实例ID。

        :param bandwidth_package_id: The bandwidth_package_id of this InterRegionBandwidth.
        :type bandwidth_package_id: str
        """
        self._bandwidth_package_id = bandwidth_package_id

    @property
    def inter_regions(self):
        r"""Gets the inter_regions of this InterRegionBandwidth.

        域间实例信息。

        :return: The inter_regions of this InterRegionBandwidth.
        :rtype: list[:class:`huaweicloudsdkcc.v3.InterRegion`]
        """
        return self._inter_regions

    @inter_regions.setter
    def inter_regions(self, inter_regions):
        r"""Sets the inter_regions of this InterRegionBandwidth.

        域间实例信息。

        :param inter_regions: The inter_regions of this InterRegionBandwidth.
        :type inter_regions: list[:class:`huaweicloudsdkcc.v3.InterRegion`]
        """
        self._inter_regions = inter_regions

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this InterRegionBandwidth.

        带宽值，单位Mbps。

        :return: The bandwidth of this InterRegionBandwidth.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this InterRegionBandwidth.

        带宽值，单位Mbps。

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
