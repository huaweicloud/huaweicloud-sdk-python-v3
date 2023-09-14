# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeSiteResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_site': 'EdgeSiteDetail'
    }

    attribute_map = {
        'edge_site': 'edge_site'
    }

    def __init__(self, edge_site=None):
        """CreateEdgeSiteResponse

        The model defined in huaweicloud sdk

        :param edge_site: 
        :type edge_site: :class:`huaweicloudsdkcloudpond.v1.EdgeSiteDetail`
        """
        
        super(CreateEdgeSiteResponse, self).__init__()

        self._edge_site = None
        self.discriminator = None

        if edge_site is not None:
            self.edge_site = edge_site

    @property
    def edge_site(self):
        """Gets the edge_site of this CreateEdgeSiteResponse.

        :return: The edge_site of this CreateEdgeSiteResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.EdgeSiteDetail`
        """
        return self._edge_site

    @edge_site.setter
    def edge_site(self, edge_site):
        """Sets the edge_site of this CreateEdgeSiteResponse.

        :param edge_site: The edge_site of this CreateEdgeSiteResponse.
        :type edge_site: :class:`huaweicloudsdkcloudpond.v1.EdgeSiteDetail`
        """
        self._edge_site = edge_site

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
        if not isinstance(other, CreateEdgeSiteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
