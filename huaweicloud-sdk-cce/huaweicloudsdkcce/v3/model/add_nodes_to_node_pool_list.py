# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddNodesToNodePoolList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'node_list': 'list[AddNodesToNodePool]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'node_list': 'nodeList'
    }

    def __init__(self, api_version=None, kind=None, node_list=None):
        r"""AddNodesToNodePoolList

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值“v3”。
        :type api_version: str
        :param kind: API类型，固定值“List”。
        :type kind: str
        :param node_list: 纳管节点列表，当前最多支持同时纳管200个节点。
        :type node_list: list[:class:`huaweicloudsdkcce.v3.AddNodesToNodePool`]
        """
        
        

        self._api_version = None
        self._kind = None
        self._node_list = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.node_list = node_list

    @property
    def api_version(self):
        r"""Gets the api_version of this AddNodesToNodePoolList.

        API版本，固定值“v3”。

        :return: The api_version of this AddNodesToNodePoolList.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AddNodesToNodePoolList.

        API版本，固定值“v3”。

        :param api_version: The api_version of this AddNodesToNodePoolList.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this AddNodesToNodePoolList.

        API类型，固定值“List”。

        :return: The kind of this AddNodesToNodePoolList.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this AddNodesToNodePoolList.

        API类型，固定值“List”。

        :param kind: The kind of this AddNodesToNodePoolList.
        :type kind: str
        """
        self._kind = kind

    @property
    def node_list(self):
        r"""Gets the node_list of this AddNodesToNodePoolList.

        纳管节点列表，当前最多支持同时纳管200个节点。

        :return: The node_list of this AddNodesToNodePoolList.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AddNodesToNodePool`]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this AddNodesToNodePoolList.

        纳管节点列表，当前最多支持同时纳管200个节点。

        :param node_list: The node_list of this AddNodesToNodePoolList.
        :type node_list: list[:class:`huaweicloudsdkcce.v3.AddNodesToNodePool`]
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
        if not isinstance(other, AddNodesToNodePoolList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
