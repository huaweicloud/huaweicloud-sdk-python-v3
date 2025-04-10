# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotasRespQuotasResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'available': 'int',
        'edge_volume': 'int'
    }

    attribute_map = {
        'type': 'type',
        'available': 'available',
        'edge_volume': 'edge_volume'
    }

    def __init__(self, type=None, available=None, edge_volume=None):
        r"""ListQuotasRespQuotasResources

        The model defined in huaweicloud sdk

        :param type: 类型。  取值范围：  - \&quot;graph\&quot; - \&quot;backup\&quot; - \&quot;metadata\&quot;
        :type type: str
        :param available: 图的可用个数。
        :type available: int
        :param edge_volume: 边的可用个数。type为graph时此值有效。
        :type edge_volume: int
        """
        
        

        self._type = None
        self._available = None
        self._edge_volume = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if available is not None:
            self.available = available
        if edge_volume is not None:
            self.edge_volume = edge_volume

    @property
    def type(self):
        r"""Gets the type of this ListQuotasRespQuotasResources.

        类型。  取值范围：  - \"graph\" - \"backup\" - \"metadata\"

        :return: The type of this ListQuotasRespQuotasResources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListQuotasRespQuotasResources.

        类型。  取值范围：  - \"graph\" - \"backup\" - \"metadata\"

        :param type: The type of this ListQuotasRespQuotasResources.
        :type type: str
        """
        self._type = type

    @property
    def available(self):
        r"""Gets the available of this ListQuotasRespQuotasResources.

        图的可用个数。

        :return: The available of this ListQuotasRespQuotasResources.
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        r"""Sets the available of this ListQuotasRespQuotasResources.

        图的可用个数。

        :param available: The available of this ListQuotasRespQuotasResources.
        :type available: int
        """
        self._available = available

    @property
    def edge_volume(self):
        r"""Gets the edge_volume of this ListQuotasRespQuotasResources.

        边的可用个数。type为graph时此值有效。

        :return: The edge_volume of this ListQuotasRespQuotasResources.
        :rtype: int
        """
        return self._edge_volume

    @edge_volume.setter
    def edge_volume(self, edge_volume):
        r"""Sets the edge_volume of this ListQuotasRespQuotasResources.

        边的可用个数。type为graph时此值有效。

        :param edge_volume: The edge_volume of this ListQuotasRespQuotasResources.
        :type edge_volume: int
        """
        self._edge_volume = edge_volume

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
        if not isinstance(other, ListQuotasRespQuotasResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
