# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteRespsResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_address': 'str',
        'ip_net_mask': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'ip_address': 'ipAddress',
        'ip_net_mask': 'ipNetMask',
        'update_at': 'updateAt'
    }

    def __init__(self, ip_address=None, ip_net_mask=None, update_at=None):
        r"""RouteRespsResource

        The model defined in huaweicloud sdk

        :param ip_address: ip地址。
        :type ip_address: str
        :param ip_net_mask: 子网掩码。
        :type ip_net_mask: str
        :param update_at: 更新时间。
        :type update_at: str
        """
        
        

        self._ip_address = None
        self._ip_net_mask = None
        self._update_at = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        if ip_net_mask is not None:
            self.ip_net_mask = ip_net_mask
        if update_at is not None:
            self.update_at = update_at

    @property
    def ip_address(self):
        r"""Gets the ip_address of this RouteRespsResource.

        ip地址。

        :return: The ip_address of this RouteRespsResource.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this RouteRespsResource.

        ip地址。

        :param ip_address: The ip_address of this RouteRespsResource.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ip_net_mask(self):
        r"""Gets the ip_net_mask of this RouteRespsResource.

        子网掩码。

        :return: The ip_net_mask of this RouteRespsResource.
        :rtype: str
        """
        return self._ip_net_mask

    @ip_net_mask.setter
    def ip_net_mask(self, ip_net_mask):
        r"""Sets the ip_net_mask of this RouteRespsResource.

        子网掩码。

        :param ip_net_mask: The ip_net_mask of this RouteRespsResource.
        :type ip_net_mask: str
        """
        self._ip_net_mask = ip_net_mask

    @property
    def update_at(self):
        r"""Gets the update_at of this RouteRespsResource.

        更新时间。

        :return: The update_at of this RouteRespsResource.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this RouteRespsResource.

        更新时间。

        :param update_at: The update_at of this RouteRespsResource.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, RouteRespsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
