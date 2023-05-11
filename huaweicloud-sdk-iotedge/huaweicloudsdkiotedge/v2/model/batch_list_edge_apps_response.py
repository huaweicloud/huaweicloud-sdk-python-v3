# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListEdgeAppsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'page_info': 'PageInfoDTO',
        'edge_apps': 'list[QueryApplicationBriefResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'page_info': 'page_info',
        'edge_apps': 'edge_apps'
    }

    def __init__(self, count=None, page_info=None, edge_apps=None):
        """BatchListEdgeAppsResponse

        The model defined in huaweicloud sdk

        :param count: 总记录数
        :type count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiotedge.v2.PageInfoDTO`
        :param edge_apps: 每页记录数
        :type edge_apps: list[:class:`huaweicloudsdkiotedge.v2.QueryApplicationBriefResponseDTO`]
        """
        
        super(BatchListEdgeAppsResponse, self).__init__()

        self._count = None
        self._page_info = None
        self._edge_apps = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info
        if edge_apps is not None:
            self.edge_apps = edge_apps

    @property
    def count(self):
        """Gets the count of this BatchListEdgeAppsResponse.

        总记录数

        :return: The count of this BatchListEdgeAppsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchListEdgeAppsResponse.

        总记录数

        :param count: The count of this BatchListEdgeAppsResponse.
        :type count: int
        """
        self._count = count

    @property
    def page_info(self):
        """Gets the page_info of this BatchListEdgeAppsResponse.

        :return: The page_info of this BatchListEdgeAppsResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.PageInfoDTO`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this BatchListEdgeAppsResponse.

        :param page_info: The page_info of this BatchListEdgeAppsResponse.
        :type page_info: :class:`huaweicloudsdkiotedge.v2.PageInfoDTO`
        """
        self._page_info = page_info

    @property
    def edge_apps(self):
        """Gets the edge_apps of this BatchListEdgeAppsResponse.

        每页记录数

        :return: The edge_apps of this BatchListEdgeAppsResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.QueryApplicationBriefResponseDTO`]
        """
        return self._edge_apps

    @edge_apps.setter
    def edge_apps(self, edge_apps):
        """Sets the edge_apps of this BatchListEdgeAppsResponse.

        每页记录数

        :param edge_apps: The edge_apps of this BatchListEdgeAppsResponse.
        :type edge_apps: list[:class:`huaweicloudsdkiotedge.v2.QueryApplicationBriefResponseDTO`]
        """
        self._edge_apps = edge_apps

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
        if not isinstance(other, BatchListEdgeAppsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
