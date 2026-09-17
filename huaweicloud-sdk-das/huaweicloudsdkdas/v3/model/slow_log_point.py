# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogPoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'node_name': 'str',
        'trend_data': 'list[SlowLogTrendPoint]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'trend_data': 'trend_data'
    }

    def __init__(self, node_id=None, node_name=None, trend_data=None):
        r"""SlowLogPoint

        The model defined in huaweicloud sdk

        :param node_id: 节点ID，实例节点的唯一标识
        :type node_id: str
        :param node_name: 节点名称
        :type node_name: str
        :param trend_data: 趋势数量列表
        :type trend_data: list[:class:`huaweicloudsdkdas.v3.SlowLogTrendPoint`]
        """
        
        

        self._node_id = None
        self._node_name = None
        self._trend_data = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if trend_data is not None:
            self.trend_data = trend_data

    @property
    def node_id(self):
        r"""Gets the node_id of this SlowLogPoint.

        节点ID，实例节点的唯一标识

        :return: The node_id of this SlowLogPoint.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SlowLogPoint.

        节点ID，实例节点的唯一标识

        :param node_id: The node_id of this SlowLogPoint.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this SlowLogPoint.

        节点名称

        :return: The node_name of this SlowLogPoint.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this SlowLogPoint.

        节点名称

        :param node_name: The node_name of this SlowLogPoint.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def trend_data(self):
        r"""Gets the trend_data of this SlowLogPoint.

        趋势数量列表

        :return: The trend_data of this SlowLogPoint.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogTrendPoint`]
        """
        return self._trend_data

    @trend_data.setter
    def trend_data(self, trend_data):
        r"""Sets the trend_data of this SlowLogPoint.

        趋势数量列表

        :param trend_data: The trend_data of this SlowLogPoint.
        :type trend_data: list[:class:`huaweicloudsdkdas.v3.SlowLogTrendPoint`]
        """
        self._trend_data = trend_data

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
        if not isinstance(other, SlowLogPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
