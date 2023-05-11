# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaAttachInterfaceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fixed_ips': 'list[NovaAttachInterfaceFixedIp]',
        'net_id': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'fixed_ips': 'fixed_ips',
        'net_id': 'net_id',
        'port_id': 'port_id'
    }

    def __init__(self, fixed_ips=None, net_id=None, port_id=None):
        """NovaAttachInterfaceOption

        The model defined in huaweicloud sdk

        :param fixed_ips: 私有IP。  有port_id时，该参数不起作用，并且有该参数时，必须有net_id。  只有列表中第一个元素有效。传入两个及以上元素会报错。
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.NovaAttachInterfaceFixedIp`]
        :param net_id:   Network ID。  有port_id时，该参数不起作用。
        :type net_id: str
        :param port_id:   Port ID。  port_id和net_id不能同时传入。
        :type port_id: str
        """
        
        

        self._fixed_ips = None
        self._net_id = None
        self._port_id = None
        self.discriminator = None

        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if net_id is not None:
            self.net_id = net_id
        if port_id is not None:
            self.port_id = port_id

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this NovaAttachInterfaceOption.

        私有IP。  有port_id时，该参数不起作用，并且有该参数时，必须有net_id。  只有列表中第一个元素有效。传入两个及以上元素会报错。

        :return: The fixed_ips of this NovaAttachInterfaceOption.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaAttachInterfaceFixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this NovaAttachInterfaceOption.

        私有IP。  有port_id时，该参数不起作用，并且有该参数时，必须有net_id。  只有列表中第一个元素有效。传入两个及以上元素会报错。

        :param fixed_ips: The fixed_ips of this NovaAttachInterfaceOption.
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.NovaAttachInterfaceFixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def net_id(self):
        """Gets the net_id of this NovaAttachInterfaceOption.

          Network ID。  有port_id时，该参数不起作用。

        :return: The net_id of this NovaAttachInterfaceOption.
        :rtype: str
        """
        return self._net_id

    @net_id.setter
    def net_id(self, net_id):
        """Sets the net_id of this NovaAttachInterfaceOption.

          Network ID。  有port_id时，该参数不起作用。

        :param net_id: The net_id of this NovaAttachInterfaceOption.
        :type net_id: str
        """
        self._net_id = net_id

    @property
    def port_id(self):
        """Gets the port_id of this NovaAttachInterfaceOption.

          Port ID。  port_id和net_id不能同时传入。

        :return: The port_id of this NovaAttachInterfaceOption.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this NovaAttachInterfaceOption.

          Port ID。  port_id和net_id不能同时传入。

        :param port_id: The port_id of this NovaAttachInterfaceOption.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, NovaAttachInterfaceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
