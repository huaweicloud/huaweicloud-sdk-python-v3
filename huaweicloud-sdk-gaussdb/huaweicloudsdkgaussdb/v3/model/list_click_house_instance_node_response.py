# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClickHouseInstanceNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_list': 'list[ClickHouseNodeInfoResponseBodyNodeList]'
    }

    attribute_map = {
        'node_list': 'node_list'
    }

    def __init__(self, node_list=None):
        r"""ListClickHouseInstanceNodeResponse

        The model defined in huaweicloud sdk

        :param node_list: ClickHouse实例节点列表。
        :type node_list: list[:class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoResponseBodyNodeList`]
        """
        
        super(ListClickHouseInstanceNodeResponse, self).__init__()

        self._node_list = None
        self.discriminator = None

        if node_list is not None:
            self.node_list = node_list

    @property
    def node_list(self):
        r"""Gets the node_list of this ListClickHouseInstanceNodeResponse.

        ClickHouse实例节点列表。

        :return: The node_list of this ListClickHouseInstanceNodeResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoResponseBodyNodeList`]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this ListClickHouseInstanceNodeResponse.

        ClickHouse实例节点列表。

        :param node_list: The node_list of this ListClickHouseInstanceNodeResponse.
        :type node_list: list[:class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoResponseBodyNodeList`]
        """
        self._node_list = node_list

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
        if not isinstance(other, ListClickHouseInstanceNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
