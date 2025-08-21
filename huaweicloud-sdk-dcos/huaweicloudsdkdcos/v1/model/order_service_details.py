# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderServiceDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'devices': 'list[DeviceServiceDetails]',
        'assets': 'list[AssetServiceDetails]',
        'contacts': 'list[ContactServiceDetails]'
    }

    attribute_map = {
        'devices': 'devices',
        'assets': 'assets',
        'contacts': 'contacts'
    }

    def __init__(self, devices=None, assets=None, contacts=None):
        r"""OrderServiceDetails

        The model defined in huaweicloud sdk

        :param devices: 服务设备对象
        :type devices: list[:class:`huaweicloudsdkdcos.v1.DeviceServiceDetails`]
        :param assets: 资产对象
        :type assets: list[:class:`huaweicloudsdkdcos.v1.AssetServiceDetails`]
        :param contacts: 人员信息
        :type contacts: list[:class:`huaweicloudsdkdcos.v1.ContactServiceDetails`]
        """
        
        

        self._devices = None
        self._assets = None
        self._contacts = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if assets is not None:
            self.assets = assets
        if contacts is not None:
            self.contacts = contacts

    @property
    def devices(self):
        r"""Gets the devices of this OrderServiceDetails.

        服务设备对象

        :return: The devices of this OrderServiceDetails.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.DeviceServiceDetails`]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        r"""Sets the devices of this OrderServiceDetails.

        服务设备对象

        :param devices: The devices of this OrderServiceDetails.
        :type devices: list[:class:`huaweicloudsdkdcos.v1.DeviceServiceDetails`]
        """
        self._devices = devices

    @property
    def assets(self):
        r"""Gets the assets of this OrderServiceDetails.

        资产对象

        :return: The assets of this OrderServiceDetails.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.AssetServiceDetails`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        r"""Sets the assets of this OrderServiceDetails.

        资产对象

        :param assets: The assets of this OrderServiceDetails.
        :type assets: list[:class:`huaweicloudsdkdcos.v1.AssetServiceDetails`]
        """
        self._assets = assets

    @property
    def contacts(self):
        r"""Gets the contacts of this OrderServiceDetails.

        人员信息

        :return: The contacts of this OrderServiceDetails.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.ContactServiceDetails`]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        r"""Sets the contacts of this OrderServiceDetails.

        人员信息

        :param contacts: The contacts of this OrderServiceDetails.
        :type contacts: list[:class:`huaweicloudsdkdcos.v1.ContactServiceDetails`]
        """
        self._contacts = contacts

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
        if not isinstance(other, OrderServiceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
