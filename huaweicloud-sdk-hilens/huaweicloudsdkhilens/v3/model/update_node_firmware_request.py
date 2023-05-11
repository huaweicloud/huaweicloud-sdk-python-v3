# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNodeFirmwareRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'firmware_id': 'str',
        'x_expired_time': 'int'
    }

    attribute_map = {
        'node_id': 'node_id',
        'firmware_id': 'firmware_id',
        'x_expired_time': 'X-Expired-Time'
    }

    def __init__(self, node_id=None, firmware_id=None, x_expired_time=None):
        """UpdateNodeFirmwareRequest

        The model defined in huaweicloud sdk

        :param node_id: 设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取
        :type node_id: str
        :param firmware_id: 固件ID,，从专业版HiLens控制台固件管理[查询固件列表](ListFirmwares.xml)获取
        :type firmware_id: str
        :param x_expired_time: 离线场景超期时间，单位分钟，范围在1-86400
        :type x_expired_time: int
        """
        
        

        self._node_id = None
        self._firmware_id = None
        self._x_expired_time = None
        self.discriminator = None

        self.node_id = node_id
        self.firmware_id = firmware_id
        if x_expired_time is not None:
            self.x_expired_time = x_expired_time

    @property
    def node_id(self):
        """Gets the node_id of this UpdateNodeFirmwareRequest.

        设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取

        :return: The node_id of this UpdateNodeFirmwareRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UpdateNodeFirmwareRequest.

        设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取

        :param node_id: The node_id of this UpdateNodeFirmwareRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def firmware_id(self):
        """Gets the firmware_id of this UpdateNodeFirmwareRequest.

        固件ID,，从专业版HiLens控制台固件管理[查询固件列表](ListFirmwares.xml)获取

        :return: The firmware_id of this UpdateNodeFirmwareRequest.
        :rtype: str
        """
        return self._firmware_id

    @firmware_id.setter
    def firmware_id(self, firmware_id):
        """Sets the firmware_id of this UpdateNodeFirmwareRequest.

        固件ID,，从专业版HiLens控制台固件管理[查询固件列表](ListFirmwares.xml)获取

        :param firmware_id: The firmware_id of this UpdateNodeFirmwareRequest.
        :type firmware_id: str
        """
        self._firmware_id = firmware_id

    @property
    def x_expired_time(self):
        """Gets the x_expired_time of this UpdateNodeFirmwareRequest.

        离线场景超期时间，单位分钟，范围在1-86400

        :return: The x_expired_time of this UpdateNodeFirmwareRequest.
        :rtype: int
        """
        return self._x_expired_time

    @x_expired_time.setter
    def x_expired_time(self, x_expired_time):
        """Sets the x_expired_time of this UpdateNodeFirmwareRequest.

        离线场景超期时间，单位分钟，范围在1-86400

        :param x_expired_time: The x_expired_time of this UpdateNodeFirmwareRequest.
        :type x_expired_time: int
        """
        self._x_expired_time = x_expired_time

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
        if not isinstance(other, UpdateNodeFirmwareRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
