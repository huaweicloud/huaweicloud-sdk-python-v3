# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployedResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service': 'str',
        'resource_num': 'int',
        'resource_location': 'str',
        'region_resources': 'list[RegionResourceDetail]'
    }

    attribute_map = {
        'service': 'service',
        'resource_num': 'resource_num',
        'resource_location': 'resource_location',
        'region_resources': 'region_resources'
    }

    def __init__(self, service=None, resource_num=None, resource_location=None, region_resources=None):
        r"""DeployedResourceDetail

        The model defined in huaweicloud sdk

        :param service: 证书已部署资源服务名称。 - WAF：证书关联Web应用防火墙的资源。 - CDN：证书关联内容分发网络的资源。 - ELB：证书关联弹性负载均衡（经典型）的资源。
        :type service: str
        :param resource_num: 证书在当前服务已部署资源数量。
        :type resource_num: int
        :param resource_location: 全局服务或Region级服务。
        :type resource_location: str
        :param region_resources: 局点资源列表，详情请参见RegionResourceDetail字段数据结构说明。
        :type region_resources: list[:class:`huaweicloudsdkscm.v3.RegionResourceDetail`]
        """
        
        

        self._service = None
        self._resource_num = None
        self._resource_location = None
        self._region_resources = None
        self.discriminator = None

        self.service = service
        self.resource_num = resource_num
        self.resource_location = resource_location
        self.region_resources = region_resources

    @property
    def service(self):
        r"""Gets the service of this DeployedResourceDetail.

        证书已部署资源服务名称。 - WAF：证书关联Web应用防火墙的资源。 - CDN：证书关联内容分发网络的资源。 - ELB：证书关联弹性负载均衡（经典型）的资源。

        :return: The service of this DeployedResourceDetail.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this DeployedResourceDetail.

        证书已部署资源服务名称。 - WAF：证书关联Web应用防火墙的资源。 - CDN：证书关联内容分发网络的资源。 - ELB：证书关联弹性负载均衡（经典型）的资源。

        :param service: The service of this DeployedResourceDetail.
        :type service: str
        """
        self._service = service

    @property
    def resource_num(self):
        r"""Gets the resource_num of this DeployedResourceDetail.

        证书在当前服务已部署资源数量。

        :return: The resource_num of this DeployedResourceDetail.
        :rtype: int
        """
        return self._resource_num

    @resource_num.setter
    def resource_num(self, resource_num):
        r"""Sets the resource_num of this DeployedResourceDetail.

        证书在当前服务已部署资源数量。

        :param resource_num: The resource_num of this DeployedResourceDetail.
        :type resource_num: int
        """
        self._resource_num = resource_num

    @property
    def resource_location(self):
        r"""Gets the resource_location of this DeployedResourceDetail.

        全局服务或Region级服务。

        :return: The resource_location of this DeployedResourceDetail.
        :rtype: str
        """
        return self._resource_location

    @resource_location.setter
    def resource_location(self, resource_location):
        r"""Sets the resource_location of this DeployedResourceDetail.

        全局服务或Region级服务。

        :param resource_location: The resource_location of this DeployedResourceDetail.
        :type resource_location: str
        """
        self._resource_location = resource_location

    @property
    def region_resources(self):
        r"""Gets the region_resources of this DeployedResourceDetail.

        局点资源列表，详情请参见RegionResourceDetail字段数据结构说明。

        :return: The region_resources of this DeployedResourceDetail.
        :rtype: list[:class:`huaweicloudsdkscm.v3.RegionResourceDetail`]
        """
        return self._region_resources

    @region_resources.setter
    def region_resources(self, region_resources):
        r"""Sets the region_resources of this DeployedResourceDetail.

        局点资源列表，详情请参见RegionResourceDetail字段数据结构说明。

        :param region_resources: The region_resources of this DeployedResourceDetail.
        :type region_resources: list[:class:`huaweicloudsdkscm.v3.RegionResourceDetail`]
        """
        self._region_resources = region_resources

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
        if not isinstance(other, DeployedResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
