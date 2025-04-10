# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'flavor_ref': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'flavor_ref': 'flavorRef'
    }

    def __init__(self, server_id=None, flavor_ref=None):
        r"""ServerInfo

        The model defined in huaweicloud sdk

        :param server_id: 指定的生产站点云服务器ID。
        :type server_id: str
        :param flavor_ref: 指定的容灾站点云服务器的flavor ID。
        :type flavor_ref: str
        """
        
        

        self._server_id = None
        self._flavor_ref = None
        self.discriminator = None

        self.server_id = server_id
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref

    @property
    def server_id(self):
        r"""Gets the server_id of this ServerInfo.

        指定的生产站点云服务器ID。

        :return: The server_id of this ServerInfo.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ServerInfo.

        指定的生产站点云服务器ID。

        :param server_id: The server_id of this ServerInfo.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this ServerInfo.

        指定的容灾站点云服务器的flavor ID。

        :return: The flavor_ref of this ServerInfo.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this ServerInfo.

        指定的容灾站点云服务器的flavor ID。

        :param flavor_ref: The flavor_ref of this ServerInfo.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

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
        if not isinstance(other, ServerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
