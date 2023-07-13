# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListRoutersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'routers': 'list[NeutronRouter]',
        'routers_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'routers': 'routers',
        'routers_links': 'routers_links'
    }

    def __init__(self, routers=None, routers_links=None):
        """NeutronListRoutersResponse

        The model defined in huaweicloud sdk

        :param routers: router对象列表
        :type routers: list[:class:`huaweicloudsdkvpc.v2.NeutronRouter`]
        :param routers_links: 分页信息
        :type routers_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(NeutronListRoutersResponse, self).__init__()

        self._routers = None
        self._routers_links = None
        self.discriminator = None

        if routers is not None:
            self.routers = routers
        if routers_links is not None:
            self.routers_links = routers_links

    @property
    def routers(self):
        """Gets the routers of this NeutronListRoutersResponse.

        router对象列表

        :return: The routers of this NeutronListRoutersResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronRouter`]
        """
        return self._routers

    @routers.setter
    def routers(self, routers):
        """Sets the routers of this NeutronListRoutersResponse.

        router对象列表

        :param routers: The routers of this NeutronListRoutersResponse.
        :type routers: list[:class:`huaweicloudsdkvpc.v2.NeutronRouter`]
        """
        self._routers = routers

    @property
    def routers_links(self):
        """Gets the routers_links of this NeutronListRoutersResponse.

        分页信息

        :return: The routers_links of this NeutronListRoutersResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._routers_links

    @routers_links.setter
    def routers_links(self, routers_links):
        """Sets the routers_links of this NeutronListRoutersResponse.

        分页信息

        :param routers_links: The routers_links of this NeutronListRoutersResponse.
        :type routers_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        self._routers_links = routers_links

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
        if not isinstance(other, NeutronListRoutersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
