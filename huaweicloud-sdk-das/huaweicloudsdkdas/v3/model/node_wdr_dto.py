# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeWdrDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_wdr': 'str',
        'node_name': 'str'
    }

    attribute_map = {
        'node_wdr': 'node_wdr',
        'node_name': 'node_name'
    }

    def __init__(self, node_wdr=None, node_name=None):
        r"""NodeWdrDto

        The model defined in huaweicloud sdk

        :param node_wdr: 节点WDR报表下载地址
        :type node_wdr: str
        :param node_name: 节点WDR报表名称
        :type node_name: str
        """
        
        

        self._node_wdr = None
        self._node_name = None
        self.discriminator = None

        if node_wdr is not None:
            self.node_wdr = node_wdr
        if node_name is not None:
            self.node_name = node_name

    @property
    def node_wdr(self):
        r"""Gets the node_wdr of this NodeWdrDto.

        节点WDR报表下载地址

        :return: The node_wdr of this NodeWdrDto.
        :rtype: str
        """
        return self._node_wdr

    @node_wdr.setter
    def node_wdr(self, node_wdr):
        r"""Sets the node_wdr of this NodeWdrDto.

        节点WDR报表下载地址

        :param node_wdr: The node_wdr of this NodeWdrDto.
        :type node_wdr: str
        """
        self._node_wdr = node_wdr

    @property
    def node_name(self):
        r"""Gets the node_name of this NodeWdrDto.

        节点WDR报表名称

        :return: The node_name of this NodeWdrDto.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this NodeWdrDto.

        节点WDR报表名称

        :param node_name: The node_name of this NodeWdrDto.
        :type node_name: str
        """
        self._node_name = node_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeWdrDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
