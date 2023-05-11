# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComponentInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[Nodes]',
        'total_count': 'int'
    }

    attribute_map = {
        'nodes': 'nodes',
        'total_count': 'total_count'
    }

    def __init__(self, nodes=None, total_count=None):
        """ListComponentInfosResponse

        The model defined in huaweicloud sdk

        :param nodes: 组件信息。
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Nodes`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListComponentInfosResponse, self).__init__()

        self._nodes = None
        self._total_count = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if total_count is not None:
            self.total_count = total_count

    @property
    def nodes(self):
        """Gets the nodes of this ListComponentInfosResponse.

        组件信息。

        :return: The nodes of this ListComponentInfosResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Nodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ListComponentInfosResponse.

        组件信息。

        :param nodes: The nodes of this ListComponentInfosResponse.
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Nodes`]
        """
        self._nodes = nodes

    @property
    def total_count(self):
        """Gets the total_count of this ListComponentInfosResponse.

        总记录数。

        :return: The total_count of this ListComponentInfosResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListComponentInfosResponse.

        总记录数。

        :param total_count: The total_count of this ListComponentInfosResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListComponentInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
