# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Endpoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'region_id': 'str',
        'links': 'Links',
        'id': 'str',
        'interface': 'str',
        'region': 'str',
        'url': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'service_id': 'service_id',
        'region_id': 'region_id',
        'links': 'links',
        'id': 'id',
        'interface': 'interface',
        'region': 'region',
        'url': 'url',
        'enabled': 'enabled'
    }

    def __init__(self, service_id=None, region_id=None, links=None, id=None, interface=None, region=None, url=None, enabled=None):
        """Endpoint

        The model defined in huaweicloud sdk

        :param service_id: 终端节点所属服务的ID。
        :type service_id: str
        :param region_id: 终端节点所属区域的ID。
        :type region_id: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param id: 终端节点ID。
        :type id: str
        :param interface: 终端节点平面。
        :type interface: str
        :param region: 终端节点所属区域。
        :type region: str
        :param url: 终端节点的地址。
        :type url: str
        :param enabled: 终端节点是否可用。
        :type enabled: bool
        """
        
        

        self._service_id = None
        self._region_id = None
        self._links = None
        self._id = None
        self._interface = None
        self._region = None
        self._url = None
        self._enabled = None
        self.discriminator = None

        self.service_id = service_id
        self.region_id = region_id
        self.links = links
        self.id = id
        self.interface = interface
        self.region = region
        self.url = url
        self.enabled = enabled

    @property
    def service_id(self):
        """Gets the service_id of this Endpoint.

        终端节点所属服务的ID。

        :return: The service_id of this Endpoint.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Endpoint.

        终端节点所属服务的ID。

        :param service_id: The service_id of this Endpoint.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def region_id(self):
        """Gets the region_id of this Endpoint.

        终端节点所属区域的ID。

        :return: The region_id of this Endpoint.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this Endpoint.

        终端节点所属区域的ID。

        :param region_id: The region_id of this Endpoint.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def links(self):
        """Gets the links of this Endpoint.

        :return: The links of this Endpoint.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Endpoint.

        :param links: The links of this Endpoint.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this Endpoint.

        终端节点ID。

        :return: The id of this Endpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Endpoint.

        终端节点ID。

        :param id: The id of this Endpoint.
        :type id: str
        """
        self._id = id

    @property
    def interface(self):
        """Gets the interface of this Endpoint.

        终端节点平面。

        :return: The interface of this Endpoint.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this Endpoint.

        终端节点平面。

        :param interface: The interface of this Endpoint.
        :type interface: str
        """
        self._interface = interface

    @property
    def region(self):
        """Gets the region of this Endpoint.

        终端节点所属区域。

        :return: The region of this Endpoint.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Endpoint.

        终端节点所属区域。

        :param region: The region of this Endpoint.
        :type region: str
        """
        self._region = region

    @property
    def url(self):
        """Gets the url of this Endpoint.

        终端节点的地址。

        :return: The url of this Endpoint.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Endpoint.

        终端节点的地址。

        :param url: The url of this Endpoint.
        :type url: str
        """
        self._url = url

    @property
    def enabled(self):
        """Gets the enabled of this Endpoint.

        终端节点是否可用。

        :return: The enabled of this Endpoint.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Endpoint.

        终端节点是否可用。

        :param enabled: The enabled of this Endpoint.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, Endpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
