# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkPlaneDocument:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'associate_er_tables': 'list[AssociateErTableDocument]',
        'exclude_er_connections': 'list[list[AssociateErInstanceDocument]]'
    }

    attribute_map = {
        'name': 'name',
        'associate_er_tables': 'associate_er_tables',
        'exclude_er_connections': 'exclude_er_connections'
    }

    def __init__(self, name=None, associate_er_tables=None, exclude_er_connections=None):
        r"""CentralNetworkPlaneDocument

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param associate_er_tables: 关联的中心网络ER实例列表。
        :type associate_er_tables: list[:class:`huaweicloudsdkcc.v3.AssociateErTableDocument`]
        :param exclude_er_connections: 当自动连接所有ER实例时，排除中心网络的ER实例的连接。
        :type exclude_er_connections: list[list[AssociateErInstanceDocument]]
        """
        
        

        self._name = None
        self._associate_er_tables = None
        self._exclude_er_connections = None
        self.discriminator = None

        self.name = name
        if associate_er_tables is not None:
            self.associate_er_tables = associate_er_tables
        if exclude_er_connections is not None:
            self.exclude_er_connections = exclude_er_connections

    @property
    def name(self):
        r"""Gets the name of this CentralNetworkPlaneDocument.

        实例名称。

        :return: The name of this CentralNetworkPlaneDocument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CentralNetworkPlaneDocument.

        实例名称。

        :param name: The name of this CentralNetworkPlaneDocument.
        :type name: str
        """
        self._name = name

    @property
    def associate_er_tables(self):
        r"""Gets the associate_er_tables of this CentralNetworkPlaneDocument.

        关联的中心网络ER实例列表。

        :return: The associate_er_tables of this CentralNetworkPlaneDocument.
        :rtype: list[:class:`huaweicloudsdkcc.v3.AssociateErTableDocument`]
        """
        return self._associate_er_tables

    @associate_er_tables.setter
    def associate_er_tables(self, associate_er_tables):
        r"""Sets the associate_er_tables of this CentralNetworkPlaneDocument.

        关联的中心网络ER实例列表。

        :param associate_er_tables: The associate_er_tables of this CentralNetworkPlaneDocument.
        :type associate_er_tables: list[:class:`huaweicloudsdkcc.v3.AssociateErTableDocument`]
        """
        self._associate_er_tables = associate_er_tables

    @property
    def exclude_er_connections(self):
        r"""Gets the exclude_er_connections of this CentralNetworkPlaneDocument.

        当自动连接所有ER实例时，排除中心网络的ER实例的连接。

        :return: The exclude_er_connections of this CentralNetworkPlaneDocument.
        :rtype: list[list[AssociateErInstanceDocument]]
        """
        return self._exclude_er_connections

    @exclude_er_connections.setter
    def exclude_er_connections(self, exclude_er_connections):
        r"""Sets the exclude_er_connections of this CentralNetworkPlaneDocument.

        当自动连接所有ER实例时，排除中心网络的ER实例的连接。

        :param exclude_er_connections: The exclude_er_connections of this CentralNetworkPlaneDocument.
        :type exclude_er_connections: list[list[AssociateErInstanceDocument]]
        """
        self._exclude_er_connections = exclude_er_connections

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
        if not isinstance(other, CentralNetworkPlaneDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
