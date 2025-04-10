# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevicesInGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'int',
        'device_name': 'str',
        'product_id': 'int',
        'product_name': 'str',
        'status': 'int',
        'online_status': 'int'
    }

    attribute_map = {
        'device_id': 'device_id',
        'device_name': 'device_name',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'status': 'status',
        'online_status': 'online_status'
    }

    def __init__(self, device_id=None, device_name=None, product_id=None, product_name=None, status=None, online_status=None):
        r"""DevicesInGroup

        The model defined in huaweicloud sdk

        :param device_id: 设备ID
        :type device_id: int
        :param device_name: 设备名称
        :type device_name: str
        :param product_id: 产品ID
        :type product_id: int
        :param product_name: 产品名称
        :type product_name: str
        :param status: 设备状态 0-启用 1-禁用
        :type status: int
        :param online_status: 是否在线 0-未连接 1-在线 2-离线
        :type online_status: int
        """
        
        

        self._device_id = None
        self._device_name = None
        self._product_id = None
        self._product_name = None
        self._status = None
        self._online_status = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if device_name is not None:
            self.device_name = device_name
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if status is not None:
            self.status = status
        if online_status is not None:
            self.online_status = online_status

    @property
    def device_id(self):
        r"""Gets the device_id of this DevicesInGroup.

        设备ID

        :return: The device_id of this DevicesInGroup.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this DevicesInGroup.

        设备ID

        :param device_id: The device_id of this DevicesInGroup.
        :type device_id: int
        """
        self._device_id = device_id

    @property
    def device_name(self):
        r"""Gets the device_name of this DevicesInGroup.

        设备名称

        :return: The device_name of this DevicesInGroup.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this DevicesInGroup.

        设备名称

        :param device_name: The device_name of this DevicesInGroup.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def product_id(self):
        r"""Gets the product_id of this DevicesInGroup.

        产品ID

        :return: The product_id of this DevicesInGroup.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this DevicesInGroup.

        产品ID

        :param product_id: The product_id of this DevicesInGroup.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this DevicesInGroup.

        产品名称

        :return: The product_name of this DevicesInGroup.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this DevicesInGroup.

        产品名称

        :param product_name: The product_name of this DevicesInGroup.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def status(self):
        r"""Gets the status of this DevicesInGroup.

        设备状态 0-启用 1-禁用

        :return: The status of this DevicesInGroup.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DevicesInGroup.

        设备状态 0-启用 1-禁用

        :param status: The status of this DevicesInGroup.
        :type status: int
        """
        self._status = status

    @property
    def online_status(self):
        r"""Gets the online_status of this DevicesInGroup.

        是否在线 0-未连接 1-在线 2-离线

        :return: The online_status of this DevicesInGroup.
        :rtype: int
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        r"""Sets the online_status of this DevicesInGroup.

        是否在线 0-未连接 1-在线 2-离线

        :param online_status: The online_status of this DevicesInGroup.
        :type online_status: int
        """
        self._online_status = online_status

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
        if not isinstance(other, DevicesInGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
