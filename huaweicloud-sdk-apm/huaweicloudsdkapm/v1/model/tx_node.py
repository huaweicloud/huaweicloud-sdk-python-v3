# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TxNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tx_node_id': 'str',
        'tx_node_name': 'str',
        'tx_node_type': 'str'
    }

    attribute_map = {
        'tx_node_id': 'tx_node_id',
        'tx_node_name': 'tx_node_name',
        'tx_node_type': 'tx_node_type'
    }

    def __init__(self, tx_node_id=None, tx_node_name=None, tx_node_type=None):
        r"""TxNode

        The model defined in huaweicloud sdk

        :param tx_node_id: 节点id。
        :type tx_node_id: str
        :param tx_node_name: 节点名称。
        :type tx_node_name: str
        :param tx_node_type: 节点类型。
        :type tx_node_type: str
        """
        
        

        self._tx_node_id = None
        self._tx_node_name = None
        self._tx_node_type = None
        self.discriminator = None

        if tx_node_id is not None:
            self.tx_node_id = tx_node_id
        if tx_node_name is not None:
            self.tx_node_name = tx_node_name
        if tx_node_type is not None:
            self.tx_node_type = tx_node_type

    @property
    def tx_node_id(self):
        r"""Gets the tx_node_id of this TxNode.

        节点id。

        :return: The tx_node_id of this TxNode.
        :rtype: str
        """
        return self._tx_node_id

    @tx_node_id.setter
    def tx_node_id(self, tx_node_id):
        r"""Sets the tx_node_id of this TxNode.

        节点id。

        :param tx_node_id: The tx_node_id of this TxNode.
        :type tx_node_id: str
        """
        self._tx_node_id = tx_node_id

    @property
    def tx_node_name(self):
        r"""Gets the tx_node_name of this TxNode.

        节点名称。

        :return: The tx_node_name of this TxNode.
        :rtype: str
        """
        return self._tx_node_name

    @tx_node_name.setter
    def tx_node_name(self, tx_node_name):
        r"""Sets the tx_node_name of this TxNode.

        节点名称。

        :param tx_node_name: The tx_node_name of this TxNode.
        :type tx_node_name: str
        """
        self._tx_node_name = tx_node_name

    @property
    def tx_node_type(self):
        r"""Gets the tx_node_type of this TxNode.

        节点类型。

        :return: The tx_node_type of this TxNode.
        :rtype: str
        """
        return self._tx_node_type

    @tx_node_type.setter
    def tx_node_type(self, tx_node_type):
        r"""Sets the tx_node_type of this TxNode.

        节点类型。

        :param tx_node_type: The tx_node_type of this TxNode.
        :type tx_node_type: str
        """
        self._tx_node_type = tx_node_type

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
        if not isinstance(other, TxNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
