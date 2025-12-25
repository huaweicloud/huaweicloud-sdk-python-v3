# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkCapability:

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
        'capability': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'capability': 'capability'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, id=None, domain_id=None, capability=None):
        r"""CentralNetworkCapability

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param capability: 能力类型定义： - central-network.is-support: 支持中心网络 - central-network.is-support-enterprise-project: 支持中心网络的企业项目 - central-network.is-support-tag: 支持中心网络的标签能力 - central-network.is-support-custom-er-table: 支持中心网络的自定义路由表能力 - connection-bandwidth.size-range: 跨地域连接带宽大小的范围 - connection-bandwidth.charge-mode: 跨地域连接带宽计费类型 - connection-bandwidth.free-line: 跨地域连接免费线路 - er-instance.support-regions: 支持ER实例的Region列表 - er-instance.support-ipv6-regions: 支持IPV6的ER实例Region列表 - er-instance.support-dscp-regions:支持带宽包线路等级配置的region列表 - er-instance.support-sts5-regions:支持sts5调用ER服务的region列表 - er-instance.support-sites: 支持ER实例的站点列表 - custom-connections.is-support: 是否支持自定义连接 - custom-connections.support-regions: 支持创建自定义连接的region - gdgw-instance.support-dscp-regions:支持GDGW全域互联带宽线路等级配置的region列表 - gdgw-instance.support-freeze-regions:支持GDGW全域互联带宽冻结的region列表 - gdgw-attachment.is-support: 支持GDGW附件 - gdgw-attachment.support-regions: 支持GDGW附件的Region列表 - gdgw-attachment.support-sites: 支持GDGW附件的站点列表 - er-route-table-attachment.is-support: 支持路由表附件 - er-route-table-attachment.support-regions: 支持路由表附件的Region列表 - er-route-table-attachment.support-sites: 支持路由表附件的站点列表 - cloud-alliance.support-regions: 支持云联盟场景的Region列表
        :type capability: str
        """
        
        

        self._id = None
        self._domain_id = None
        self._capability = None
        self.discriminator = 'capability'

        self.id = id
        self.domain_id = domain_id
        self.capability = capability

    @property
    def id(self):
        r"""Gets the id of this CentralNetworkCapability.

        实例ID。

        :return: The id of this CentralNetworkCapability.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CentralNetworkCapability.

        实例ID。

        :param id: The id of this CentralNetworkCapability.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CentralNetworkCapability.

        实例所属账号ID。

        :return: The domain_id of this CentralNetworkCapability.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CentralNetworkCapability.

        实例所属账号ID。

        :param domain_id: The domain_id of this CentralNetworkCapability.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def capability(self):
        r"""Gets the capability of this CentralNetworkCapability.

        能力类型定义： - central-network.is-support: 支持中心网络 - central-network.is-support-enterprise-project: 支持中心网络的企业项目 - central-network.is-support-tag: 支持中心网络的标签能力 - central-network.is-support-custom-er-table: 支持中心网络的自定义路由表能力 - connection-bandwidth.size-range: 跨地域连接带宽大小的范围 - connection-bandwidth.charge-mode: 跨地域连接带宽计费类型 - connection-bandwidth.free-line: 跨地域连接免费线路 - er-instance.support-regions: 支持ER实例的Region列表 - er-instance.support-ipv6-regions: 支持IPV6的ER实例Region列表 - er-instance.support-dscp-regions:支持带宽包线路等级配置的region列表 - er-instance.support-sts5-regions:支持sts5调用ER服务的region列表 - er-instance.support-sites: 支持ER实例的站点列表 - custom-connections.is-support: 是否支持自定义连接 - custom-connections.support-regions: 支持创建自定义连接的region - gdgw-instance.support-dscp-regions:支持GDGW全域互联带宽线路等级配置的region列表 - gdgw-instance.support-freeze-regions:支持GDGW全域互联带宽冻结的region列表 - gdgw-attachment.is-support: 支持GDGW附件 - gdgw-attachment.support-regions: 支持GDGW附件的Region列表 - gdgw-attachment.support-sites: 支持GDGW附件的站点列表 - er-route-table-attachment.is-support: 支持路由表附件 - er-route-table-attachment.support-regions: 支持路由表附件的Region列表 - er-route-table-attachment.support-sites: 支持路由表附件的站点列表 - cloud-alliance.support-regions: 支持云联盟场景的Region列表

        :return: The capability of this CentralNetworkCapability.
        :rtype: str
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        r"""Sets the capability of this CentralNetworkCapability.

        能力类型定义： - central-network.is-support: 支持中心网络 - central-network.is-support-enterprise-project: 支持中心网络的企业项目 - central-network.is-support-tag: 支持中心网络的标签能力 - central-network.is-support-custom-er-table: 支持中心网络的自定义路由表能力 - connection-bandwidth.size-range: 跨地域连接带宽大小的范围 - connection-bandwidth.charge-mode: 跨地域连接带宽计费类型 - connection-bandwidth.free-line: 跨地域连接免费线路 - er-instance.support-regions: 支持ER实例的Region列表 - er-instance.support-ipv6-regions: 支持IPV6的ER实例Region列表 - er-instance.support-dscp-regions:支持带宽包线路等级配置的region列表 - er-instance.support-sts5-regions:支持sts5调用ER服务的region列表 - er-instance.support-sites: 支持ER实例的站点列表 - custom-connections.is-support: 是否支持自定义连接 - custom-connections.support-regions: 支持创建自定义连接的region - gdgw-instance.support-dscp-regions:支持GDGW全域互联带宽线路等级配置的region列表 - gdgw-instance.support-freeze-regions:支持GDGW全域互联带宽冻结的region列表 - gdgw-attachment.is-support: 支持GDGW附件 - gdgw-attachment.support-regions: 支持GDGW附件的Region列表 - gdgw-attachment.support-sites: 支持GDGW附件的站点列表 - er-route-table-attachment.is-support: 支持路由表附件 - er-route-table-attachment.support-regions: 支持路由表附件的Region列表 - er-route-table-attachment.support-sites: 支持路由表附件的站点列表 - cloud-alliance.support-regions: 支持云联盟场景的Region列表

        :param capability: The capability of this CentralNetworkCapability.
        :type capability: str
        """
        self._capability = capability

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)
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
        if not isinstance(other, CentralNetworkCapability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
