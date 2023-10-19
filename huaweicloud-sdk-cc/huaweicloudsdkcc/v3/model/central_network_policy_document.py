# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkPolicyDocument:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_plane': 'str',
        'planes': 'list[CentralNetworkPlaneDocument]',
        'er_instances': 'list[AssociateErInstanceDocument]'
    }

    attribute_map = {
        'default_plane': 'default_plane',
        'planes': 'planes',
        'er_instances': 'er_instances'
    }

    def __init__(self, default_plane=None, planes=None, er_instances=None):
        """CentralNetworkPolicyDocument

        The model defined in huaweicloud sdk

        :param default_plane: 中心网络默认平面的名字。
        :type default_plane: str
        :param planes: 中心网络平面列表。
        :type planes: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPlaneDocument`]
        :param er_instances: 中心网络ER实例列表。
        :type er_instances: list[:class:`huaweicloudsdkcc.v3.AssociateErInstanceDocument`]
        """
        
        

        self._default_plane = None
        self._planes = None
        self._er_instances = None
        self.discriminator = None

        self.default_plane = default_plane
        self.planes = planes
        if er_instances is not None:
            self.er_instances = er_instances

    @property
    def default_plane(self):
        """Gets the default_plane of this CentralNetworkPolicyDocument.

        中心网络默认平面的名字。

        :return: The default_plane of this CentralNetworkPolicyDocument.
        :rtype: str
        """
        return self._default_plane

    @default_plane.setter
    def default_plane(self, default_plane):
        """Sets the default_plane of this CentralNetworkPolicyDocument.

        中心网络默认平面的名字。

        :param default_plane: The default_plane of this CentralNetworkPolicyDocument.
        :type default_plane: str
        """
        self._default_plane = default_plane

    @property
    def planes(self):
        """Gets the planes of this CentralNetworkPolicyDocument.

        中心网络平面列表。

        :return: The planes of this CentralNetworkPolicyDocument.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPlaneDocument`]
        """
        return self._planes

    @planes.setter
    def planes(self, planes):
        """Sets the planes of this CentralNetworkPolicyDocument.

        中心网络平面列表。

        :param planes: The planes of this CentralNetworkPolicyDocument.
        :type planes: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPlaneDocument`]
        """
        self._planes = planes

    @property
    def er_instances(self):
        """Gets the er_instances of this CentralNetworkPolicyDocument.

        中心网络ER实例列表。

        :return: The er_instances of this CentralNetworkPolicyDocument.
        :rtype: list[:class:`huaweicloudsdkcc.v3.AssociateErInstanceDocument`]
        """
        return self._er_instances

    @er_instances.setter
    def er_instances(self, er_instances):
        """Sets the er_instances of this CentralNetworkPolicyDocument.

        中心网络ER实例列表。

        :param er_instances: The er_instances of this CentralNetworkPolicyDocument.
        :type er_instances: list[:class:`huaweicloudsdkcc.v3.AssociateErInstanceDocument`]
        """
        self._er_instances = er_instances

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
        if not isinstance(other, CentralNetworkPolicyDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
