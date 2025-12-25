# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeExpansionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_label': 'str',
        'data_center': 'str',
        'description': 'str',
        'maintainer': 'str',
        'network_plane': 'str'
    }

    attribute_map = {
        'custom_label': 'custom_label',
        'data_center': 'data_center',
        'description': 'description',
        'maintainer': 'maintainer',
        'network_plane': 'network_plane'
    }

    def __init__(self, custom_label=None, data_center=None, description=None, maintainer=None, network_plane=None):
        r"""NodeExpansionInfo

        The model defined in huaweicloud sdk

        :param custom_label: 自定义标签
        :type custom_label: str
        :param data_center: 数据中心
        :type data_center: str
        :param description: 描述
        :type description: str
        :param maintainer: 维护人
        :type maintainer: str
        :param network_plane: 网络平面
        :type network_plane: str
        """
        
        

        self._custom_label = None
        self._data_center = None
        self._description = None
        self._maintainer = None
        self._network_plane = None
        self.discriminator = None

        if custom_label is not None:
            self.custom_label = custom_label
        if data_center is not None:
            self.data_center = data_center
        if description is not None:
            self.description = description
        if maintainer is not None:
            self.maintainer = maintainer
        if network_plane is not None:
            self.network_plane = network_plane

    @property
    def custom_label(self):
        r"""Gets the custom_label of this NodeExpansionInfo.

        自定义标签

        :return: The custom_label of this NodeExpansionInfo.
        :rtype: str
        """
        return self._custom_label

    @custom_label.setter
    def custom_label(self, custom_label):
        r"""Sets the custom_label of this NodeExpansionInfo.

        自定义标签

        :param custom_label: The custom_label of this NodeExpansionInfo.
        :type custom_label: str
        """
        self._custom_label = custom_label

    @property
    def data_center(self):
        r"""Gets the data_center of this NodeExpansionInfo.

        数据中心

        :return: The data_center of this NodeExpansionInfo.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        r"""Sets the data_center of this NodeExpansionInfo.

        数据中心

        :param data_center: The data_center of this NodeExpansionInfo.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def description(self):
        r"""Gets the description of this NodeExpansionInfo.

        描述

        :return: The description of this NodeExpansionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NodeExpansionInfo.

        描述

        :param description: The description of this NodeExpansionInfo.
        :type description: str
        """
        self._description = description

    @property
    def maintainer(self):
        r"""Gets the maintainer of this NodeExpansionInfo.

        维护人

        :return: The maintainer of this NodeExpansionInfo.
        :rtype: str
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        r"""Sets the maintainer of this NodeExpansionInfo.

        维护人

        :param maintainer: The maintainer of this NodeExpansionInfo.
        :type maintainer: str
        """
        self._maintainer = maintainer

    @property
    def network_plane(self):
        r"""Gets the network_plane of this NodeExpansionInfo.

        网络平面

        :return: The network_plane of this NodeExpansionInfo.
        :rtype: str
        """
        return self._network_plane

    @network_plane.setter
    def network_plane(self, network_plane):
        r"""Sets the network_plane of this NodeExpansionInfo.

        网络平面

        :param network_plane: The network_plane of this NodeExpansionInfo.
        :type network_plane: str
        """
        self._network_plane = network_plane

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
        if not isinstance(other, NodeExpansionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
