# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudConnectionCapabilityInfo:

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
        'domain_id': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'is_support': 'bool',
        'bandwidth': 'CloudConnectionDomainBandwidthValue',
        'support_regions': 'list[str]',
        'support_sites': 'list[str]',
        'resource_type': 'CloudConnectionCapabilityKeyEnum'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'is_support': 'is_support',
        'bandwidth': 'bandwidth',
        'support_regions': 'support_regions',
        'support_sites': 'support_sites',
        'resource_type': 'resource_type'
    }

    def __init__(self, id=None, domain_id=None, description=None, created_at=None, updated_at=None, is_support=None, bandwidth=None, support_regions=None, support_sites=None, resource_type=None):
        r"""CloudConnectionCapabilityInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param is_support: 是否支持云连接能力。
        :type is_support: bool
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkcc.v3.CloudConnectionDomainBandwidthValue`
        :param support_regions: 租户支持的区域列表。
        :type support_regions: list[str]
        :param support_sites: 租户支持的Site列表。
        :type support_sites: list[str]
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkcc.v3.CloudConnectionCapabilityKeyEnum`
        """
        
        

        self._id = None
        self._domain_id = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._is_support = None
        self._bandwidth = None
        self._support_regions = None
        self._support_sites = None
        self._resource_type = None
        self.discriminator = None

        self.id = id
        self.domain_id = domain_id
        if description is not None:
            self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_support = is_support
        self.bandwidth = bandwidth
        self.support_regions = support_regions
        self.support_sites = support_sites
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def id(self):
        r"""Gets the id of this CloudConnectionCapabilityInfo.

        实例ID。

        :return: The id of this CloudConnectionCapabilityInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloudConnectionCapabilityInfo.

        实例ID。

        :param id: The id of this CloudConnectionCapabilityInfo.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CloudConnectionCapabilityInfo.

        实例所属账号ID。

        :return: The domain_id of this CloudConnectionCapabilityInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CloudConnectionCapabilityInfo.

        实例所属账号ID。

        :param domain_id: The domain_id of this CloudConnectionCapabilityInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def description(self):
        r"""Gets the description of this CloudConnectionCapabilityInfo.

        实例描述。不支持 <>。

        :return: The description of this CloudConnectionCapabilityInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CloudConnectionCapabilityInfo.

        实例描述。不支持 <>。

        :param description: The description of this CloudConnectionCapabilityInfo.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this CloudConnectionCapabilityInfo.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this CloudConnectionCapabilityInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CloudConnectionCapabilityInfo.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this CloudConnectionCapabilityInfo.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CloudConnectionCapabilityInfo.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this CloudConnectionCapabilityInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CloudConnectionCapabilityInfo.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this CloudConnectionCapabilityInfo.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def is_support(self):
        r"""Gets the is_support of this CloudConnectionCapabilityInfo.

        是否支持云连接能力。

        :return: The is_support of this CloudConnectionCapabilityInfo.
        :rtype: bool
        """
        return self._is_support

    @is_support.setter
    def is_support(self, is_support):
        r"""Sets the is_support of this CloudConnectionCapabilityInfo.

        是否支持云连接能力。

        :param is_support: The is_support of this CloudConnectionCapabilityInfo.
        :type is_support: bool
        """
        self._is_support = is_support

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this CloudConnectionCapabilityInfo.

        :return: The bandwidth of this CloudConnectionCapabilityInfo.
        :rtype: :class:`huaweicloudsdkcc.v3.CloudConnectionDomainBandwidthValue`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this CloudConnectionCapabilityInfo.

        :param bandwidth: The bandwidth of this CloudConnectionCapabilityInfo.
        :type bandwidth: :class:`huaweicloudsdkcc.v3.CloudConnectionDomainBandwidthValue`
        """
        self._bandwidth = bandwidth

    @property
    def support_regions(self):
        r"""Gets the support_regions of this CloudConnectionCapabilityInfo.

        租户支持的区域列表。

        :return: The support_regions of this CloudConnectionCapabilityInfo.
        :rtype: list[str]
        """
        return self._support_regions

    @support_regions.setter
    def support_regions(self, support_regions):
        r"""Sets the support_regions of this CloudConnectionCapabilityInfo.

        租户支持的区域列表。

        :param support_regions: The support_regions of this CloudConnectionCapabilityInfo.
        :type support_regions: list[str]
        """
        self._support_regions = support_regions

    @property
    def support_sites(self):
        r"""Gets the support_sites of this CloudConnectionCapabilityInfo.

        租户支持的Site列表。

        :return: The support_sites of this CloudConnectionCapabilityInfo.
        :rtype: list[str]
        """
        return self._support_sites

    @support_sites.setter
    def support_sites(self, support_sites):
        r"""Sets the support_sites of this CloudConnectionCapabilityInfo.

        租户支持的Site列表。

        :param support_sites: The support_sites of this CloudConnectionCapabilityInfo.
        :type support_sites: list[str]
        """
        self._support_sites = support_sites

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CloudConnectionCapabilityInfo.

        :return: The resource_type of this CloudConnectionCapabilityInfo.
        :rtype: :class:`huaweicloudsdkcc.v3.CloudConnectionCapabilityKeyEnum`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CloudConnectionCapabilityInfo.

        :param resource_type: The resource_type of this CloudConnectionCapabilityInfo.
        :type resource_type: :class:`huaweicloudsdkcc.v3.CloudConnectionCapabilityKeyEnum`
        """
        self._resource_type = resource_type

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
        if not isinstance(other, CloudConnectionCapabilityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
