# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteNetworkCapabilityEntry:

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
        'specification': 'SiteNetworkSpecificationEnum',
        'is_support': 'bool',
        'is_support_enterprise_project': 'bool',
        'is_support_tag': 'bool',
        'is_support_intra_region': 'bool',
        'support_topologies': 'list[SiteNetworkTopologyEnum]',
        'support_regions': 'list[str]',
        'support_dscp_regions': 'list[str]',
        'support_freeze_regions': 'list[str]',
        'support_locations': 'list[str]',
        'size_range': 'ConnectionBandwidthSizeRange',
        'charge_mode': 'list[ConnectionBandwidthChargeModeEnum]'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'specification': 'specification',
        'is_support': 'is_support',
        'is_support_enterprise_project': 'is_support_enterprise_project',
        'is_support_tag': 'is_support_tag',
        'is_support_intra_region': 'is_support_intra_region',
        'support_topologies': 'support_topologies',
        'support_regions': 'support_regions',
        'support_dscp_regions': 'support_dscp_regions',
        'support_freeze_regions': 'support_freeze_regions',
        'support_locations': 'support_locations',
        'size_range': 'size_range',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, id=None, domain_id=None, specification=None, is_support=None, is_support_enterprise_project=None, is_support_tag=None, is_support_intra_region=None, support_topologies=None, support_regions=None, support_dscp_regions=None, support_freeze_regions=None, support_locations=None, size_range=None, charge_mode=None):
        r"""SiteNetworkCapabilityEntry

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param specification: 
        :type specification: :class:`huaweicloudsdkcc.v3.SiteNetworkSpecificationEnum`
        :param is_support: 是否支持分支网络。
        :type is_support: bool
        :param is_support_enterprise_project: 是否支持分支网络企业项目。
        :type is_support_enterprise_project: bool
        :param is_support_tag: 是否支持分支网络标签。
        :type is_support_tag: bool
        :param is_support_intra_region: 是否支持创建同region分支网络。
        :type is_support_intra_region: bool
        :param support_topologies: 分支网络的拓扑列表。
        :type support_topologies: list[:class:`huaweicloudsdkcc.v3.SiteNetworkTopologyEnum`]
        :param support_regions: list类型
        :type support_regions: list[str]
        :param support_dscp_regions: list类型
        :type support_dscp_regions: list[str]
        :param support_freeze_regions: list类型
        :type support_freeze_regions: list[str]
        :param support_locations: list类型
        :type support_locations: list[str]
        :param size_range: 
        :type size_range: :class:`huaweicloudsdkcc.v3.ConnectionBandwidthSizeRange`
        :param charge_mode: list类型
        :type charge_mode: list[:class:`huaweicloudsdkcc.v3.ConnectionBandwidthChargeModeEnum`]
        """
        
        

        self._id = None
        self._domain_id = None
        self._specification = None
        self._is_support = None
        self._is_support_enterprise_project = None
        self._is_support_tag = None
        self._is_support_intra_region = None
        self._support_topologies = None
        self._support_regions = None
        self._support_dscp_regions = None
        self._support_freeze_regions = None
        self._support_locations = None
        self._size_range = None
        self._charge_mode = None
        self.discriminator = None

        self.id = id
        self.domain_id = domain_id
        self.specification = specification
        if is_support is not None:
            self.is_support = is_support
        if is_support_enterprise_project is not None:
            self.is_support_enterprise_project = is_support_enterprise_project
        if is_support_tag is not None:
            self.is_support_tag = is_support_tag
        if is_support_intra_region is not None:
            self.is_support_intra_region = is_support_intra_region
        if support_topologies is not None:
            self.support_topologies = support_topologies
        if support_regions is not None:
            self.support_regions = support_regions
        if support_dscp_regions is not None:
            self.support_dscp_regions = support_dscp_regions
        if support_freeze_regions is not None:
            self.support_freeze_regions = support_freeze_regions
        if support_locations is not None:
            self.support_locations = support_locations
        if size_range is not None:
            self.size_range = size_range
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def id(self):
        r"""Gets the id of this SiteNetworkCapabilityEntry.

        实例ID。

        :return: The id of this SiteNetworkCapabilityEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SiteNetworkCapabilityEntry.

        实例ID。

        :param id: The id of this SiteNetworkCapabilityEntry.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SiteNetworkCapabilityEntry.

        实例所属账号ID。

        :return: The domain_id of this SiteNetworkCapabilityEntry.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SiteNetworkCapabilityEntry.

        实例所属账号ID。

        :param domain_id: The domain_id of this SiteNetworkCapabilityEntry.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def specification(self):
        r"""Gets the specification of this SiteNetworkCapabilityEntry.

        :return: The specification of this SiteNetworkCapabilityEntry.
        :rtype: :class:`huaweicloudsdkcc.v3.SiteNetworkSpecificationEnum`
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this SiteNetworkCapabilityEntry.

        :param specification: The specification of this SiteNetworkCapabilityEntry.
        :type specification: :class:`huaweicloudsdkcc.v3.SiteNetworkSpecificationEnum`
        """
        self._specification = specification

    @property
    def is_support(self):
        r"""Gets the is_support of this SiteNetworkCapabilityEntry.

        是否支持分支网络。

        :return: The is_support of this SiteNetworkCapabilityEntry.
        :rtype: bool
        """
        return self._is_support

    @is_support.setter
    def is_support(self, is_support):
        r"""Sets the is_support of this SiteNetworkCapabilityEntry.

        是否支持分支网络。

        :param is_support: The is_support of this SiteNetworkCapabilityEntry.
        :type is_support: bool
        """
        self._is_support = is_support

    @property
    def is_support_enterprise_project(self):
        r"""Gets the is_support_enterprise_project of this SiteNetworkCapabilityEntry.

        是否支持分支网络企业项目。

        :return: The is_support_enterprise_project of this SiteNetworkCapabilityEntry.
        :rtype: bool
        """
        return self._is_support_enterprise_project

    @is_support_enterprise_project.setter
    def is_support_enterprise_project(self, is_support_enterprise_project):
        r"""Sets the is_support_enterprise_project of this SiteNetworkCapabilityEntry.

        是否支持分支网络企业项目。

        :param is_support_enterprise_project: The is_support_enterprise_project of this SiteNetworkCapabilityEntry.
        :type is_support_enterprise_project: bool
        """
        self._is_support_enterprise_project = is_support_enterprise_project

    @property
    def is_support_tag(self):
        r"""Gets the is_support_tag of this SiteNetworkCapabilityEntry.

        是否支持分支网络标签。

        :return: The is_support_tag of this SiteNetworkCapabilityEntry.
        :rtype: bool
        """
        return self._is_support_tag

    @is_support_tag.setter
    def is_support_tag(self, is_support_tag):
        r"""Sets the is_support_tag of this SiteNetworkCapabilityEntry.

        是否支持分支网络标签。

        :param is_support_tag: The is_support_tag of this SiteNetworkCapabilityEntry.
        :type is_support_tag: bool
        """
        self._is_support_tag = is_support_tag

    @property
    def is_support_intra_region(self):
        r"""Gets the is_support_intra_region of this SiteNetworkCapabilityEntry.

        是否支持创建同region分支网络。

        :return: The is_support_intra_region of this SiteNetworkCapabilityEntry.
        :rtype: bool
        """
        return self._is_support_intra_region

    @is_support_intra_region.setter
    def is_support_intra_region(self, is_support_intra_region):
        r"""Sets the is_support_intra_region of this SiteNetworkCapabilityEntry.

        是否支持创建同region分支网络。

        :param is_support_intra_region: The is_support_intra_region of this SiteNetworkCapabilityEntry.
        :type is_support_intra_region: bool
        """
        self._is_support_intra_region = is_support_intra_region

    @property
    def support_topologies(self):
        r"""Gets the support_topologies of this SiteNetworkCapabilityEntry.

        分支网络的拓扑列表。

        :return: The support_topologies of this SiteNetworkCapabilityEntry.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SiteNetworkTopologyEnum`]
        """
        return self._support_topologies

    @support_topologies.setter
    def support_topologies(self, support_topologies):
        r"""Sets the support_topologies of this SiteNetworkCapabilityEntry.

        分支网络的拓扑列表。

        :param support_topologies: The support_topologies of this SiteNetworkCapabilityEntry.
        :type support_topologies: list[:class:`huaweicloudsdkcc.v3.SiteNetworkTopologyEnum`]
        """
        self._support_topologies = support_topologies

    @property
    def support_regions(self):
        r"""Gets the support_regions of this SiteNetworkCapabilityEntry.

        list类型

        :return: The support_regions of this SiteNetworkCapabilityEntry.
        :rtype: list[str]
        """
        return self._support_regions

    @support_regions.setter
    def support_regions(self, support_regions):
        r"""Sets the support_regions of this SiteNetworkCapabilityEntry.

        list类型

        :param support_regions: The support_regions of this SiteNetworkCapabilityEntry.
        :type support_regions: list[str]
        """
        self._support_regions = support_regions

    @property
    def support_dscp_regions(self):
        r"""Gets the support_dscp_regions of this SiteNetworkCapabilityEntry.

        list类型

        :return: The support_dscp_regions of this SiteNetworkCapabilityEntry.
        :rtype: list[str]
        """
        return self._support_dscp_regions

    @support_dscp_regions.setter
    def support_dscp_regions(self, support_dscp_regions):
        r"""Sets the support_dscp_regions of this SiteNetworkCapabilityEntry.

        list类型

        :param support_dscp_regions: The support_dscp_regions of this SiteNetworkCapabilityEntry.
        :type support_dscp_regions: list[str]
        """
        self._support_dscp_regions = support_dscp_regions

    @property
    def support_freeze_regions(self):
        r"""Gets the support_freeze_regions of this SiteNetworkCapabilityEntry.

        list类型

        :return: The support_freeze_regions of this SiteNetworkCapabilityEntry.
        :rtype: list[str]
        """
        return self._support_freeze_regions

    @support_freeze_regions.setter
    def support_freeze_regions(self, support_freeze_regions):
        r"""Sets the support_freeze_regions of this SiteNetworkCapabilityEntry.

        list类型

        :param support_freeze_regions: The support_freeze_regions of this SiteNetworkCapabilityEntry.
        :type support_freeze_regions: list[str]
        """
        self._support_freeze_regions = support_freeze_regions

    @property
    def support_locations(self):
        r"""Gets the support_locations of this SiteNetworkCapabilityEntry.

        list类型

        :return: The support_locations of this SiteNetworkCapabilityEntry.
        :rtype: list[str]
        """
        return self._support_locations

    @support_locations.setter
    def support_locations(self, support_locations):
        r"""Sets the support_locations of this SiteNetworkCapabilityEntry.

        list类型

        :param support_locations: The support_locations of this SiteNetworkCapabilityEntry.
        :type support_locations: list[str]
        """
        self._support_locations = support_locations

    @property
    def size_range(self):
        r"""Gets the size_range of this SiteNetworkCapabilityEntry.

        :return: The size_range of this SiteNetworkCapabilityEntry.
        :rtype: :class:`huaweicloudsdkcc.v3.ConnectionBandwidthSizeRange`
        """
        return self._size_range

    @size_range.setter
    def size_range(self, size_range):
        r"""Sets the size_range of this SiteNetworkCapabilityEntry.

        :param size_range: The size_range of this SiteNetworkCapabilityEntry.
        :type size_range: :class:`huaweicloudsdkcc.v3.ConnectionBandwidthSizeRange`
        """
        self._size_range = size_range

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this SiteNetworkCapabilityEntry.

        list类型

        :return: The charge_mode of this SiteNetworkCapabilityEntry.
        :rtype: list[:class:`huaweicloudsdkcc.v3.ConnectionBandwidthChargeModeEnum`]
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this SiteNetworkCapabilityEntry.

        list类型

        :param charge_mode: The charge_mode of this SiteNetworkCapabilityEntry.
        :type charge_mode: list[:class:`huaweicloudsdkcc.v3.ConnectionBandwidthChargeModeEnum`]
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, SiteNetworkCapabilityEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
