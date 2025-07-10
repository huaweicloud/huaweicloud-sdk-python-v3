# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronPort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'network_id': 'str',
        'device_id': 'str',
        'fixed_ips': 'list[FixedIp]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'network_id': 'network_id',
        'device_id': 'device_id',
        'fixed_ips': 'fixed_ips'
    }

    def __init__(self, id=None, status=None, network_id=None, device_id=None, fixed_ips=None):
        r"""NeutronPort

        The model defined in huaweicloud sdk

        :param id: 端口唯一标识。
        :type id: str
        :param status: 私有ip状态。
        :type status: str
        :param network_id: 端口所属网络的ID。
        :type network_id: str
        :param device_id: 端口所属设备的Id。
        :type device_id: str
        :param fixed_ips: 端口IP。
        :type fixed_ips: list[:class:`huaweicloudsdkworkspace.v2.FixedIp`]
        """
        
        

        self._id = None
        self._status = None
        self._network_id = None
        self._device_id = None
        self._fixed_ips = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if network_id is not None:
            self.network_id = network_id
        if device_id is not None:
            self.device_id = device_id
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips

    @property
    def id(self):
        r"""Gets the id of this NeutronPort.

        端口唯一标识。

        :return: The id of this NeutronPort.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NeutronPort.

        端口唯一标识。

        :param id: The id of this NeutronPort.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this NeutronPort.

        私有ip状态。

        :return: The status of this NeutronPort.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NeutronPort.

        私有ip状态。

        :param status: The status of this NeutronPort.
        :type status: str
        """
        self._status = status

    @property
    def network_id(self):
        r"""Gets the network_id of this NeutronPort.

        端口所属网络的ID。

        :return: The network_id of this NeutronPort.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this NeutronPort.

        端口所属网络的ID。

        :param network_id: The network_id of this NeutronPort.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def device_id(self):
        r"""Gets the device_id of this NeutronPort.

        端口所属设备的Id。

        :return: The device_id of this NeutronPort.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this NeutronPort.

        端口所属设备的Id。

        :param device_id: The device_id of this NeutronPort.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this NeutronPort.

        端口IP。

        :return: The fixed_ips of this NeutronPort.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this NeutronPort.

        端口IP。

        :param fixed_ips: The fixed_ips of this NeutronPort.
        :type fixed_ips: list[:class:`huaweicloudsdkworkspace.v2.FixedIp`]
        """
        self._fixed_ips = fixed_ips

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
        if not isinstance(other, NeutronPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
