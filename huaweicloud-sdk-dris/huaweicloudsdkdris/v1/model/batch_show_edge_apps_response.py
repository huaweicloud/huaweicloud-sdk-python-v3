# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowEdgeAppsResponse(SdkResponse):

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
        'edge_apps': 'list[QueryApplicationBriefResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'edge_apps': 'edge_apps'
    }

    def __init__(self, count=None, edge_apps=None):
        """BatchShowEdgeAppsResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：总记录数。
        :type count: int
        :param edge_apps: **参数说明**：列举每条记录。
        :type edge_apps: list[:class:`huaweicloudsdkdris.v1.QueryApplicationBriefResponseDTO`]
        """
        
        super(BatchShowEdgeAppsResponse, self).__init__()

        self._count = None
        self._edge_apps = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if edge_apps is not None:
            self.edge_apps = edge_apps

    @property
    def count(self):
        """Gets the count of this BatchShowEdgeAppsResponse.

        **参数说明**：总记录数。

        :return: The count of this BatchShowEdgeAppsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchShowEdgeAppsResponse.

        **参数说明**：总记录数。

        :param count: The count of this BatchShowEdgeAppsResponse.
        :type count: int
        """
        self._count = count

    @property
    def edge_apps(self):
        """Gets the edge_apps of this BatchShowEdgeAppsResponse.

        **参数说明**：列举每条记录。

        :return: The edge_apps of this BatchShowEdgeAppsResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.QueryApplicationBriefResponseDTO`]
        """
        return self._edge_apps

    @edge_apps.setter
    def edge_apps(self, edge_apps):
        """Sets the edge_apps of this BatchShowEdgeAppsResponse.

        **参数说明**：列举每条记录。

        :param edge_apps: The edge_apps of this BatchShowEdgeAppsResponse.
        :type edge_apps: list[:class:`huaweicloudsdkdris.v1.QueryApplicationBriefResponseDTO`]
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
        if not isinstance(other, BatchShowEdgeAppsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
