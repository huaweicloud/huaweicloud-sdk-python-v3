# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeLineageGuids:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node': 'str',
        'column_lineages': 'list[str]'
    }

    attribute_map = {
        'node': 'node',
        'column_lineages': 'column_lineages'
    }

    def __init__(self, node=None, column_lineages=None):
        r"""NodeLineageGuids

        The model defined in huaweicloud sdk

        :param node: 节点guid。
        :type node: str
        :param column_lineages: schema名称。
        :type column_lineages: list[str]
        """
        
        

        self._node = None
        self._column_lineages = None
        self.discriminator = None

        if node is not None:
            self.node = node
        if column_lineages is not None:
            self.column_lineages = column_lineages

    @property
    def node(self):
        r"""Gets the node of this NodeLineageGuids.

        节点guid。

        :return: The node of this NodeLineageGuids.
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        r"""Sets the node of this NodeLineageGuids.

        节点guid。

        :param node: The node of this NodeLineageGuids.
        :type node: str
        """
        self._node = node

    @property
    def column_lineages(self):
        r"""Gets the column_lineages of this NodeLineageGuids.

        schema名称。

        :return: The column_lineages of this NodeLineageGuids.
        :rtype: list[str]
        """
        return self._column_lineages

    @column_lineages.setter
    def column_lineages(self, column_lineages):
        r"""Sets the column_lineages of this NodeLineageGuids.

        schema名称。

        :param column_lineages: The column_lineages of this NodeLineageGuids.
        :type column_lineages: list[str]
        """
        self._column_lineages = column_lineages

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
        if not isinstance(other, NodeLineageGuids):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
