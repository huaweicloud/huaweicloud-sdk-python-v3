# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDeviceInfoResultDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model': 'str',
        'device_size': 'str',
        'purchase_channel': 'str'
    }

    attribute_map = {
        'model': 'model',
        'device_size': 'deviceSize',
        'purchase_channel': 'purchaseChannel'
    }

    def __init__(self, model=None, device_size=None, purchase_channel=None):
        """QueryDeviceInfoResultDTO

        The model defined in huaweicloud sdk

        :param model: 终端型号。
        :type model: str
        :param device_size: 设备终端产品尺寸。
        :type device_size: str
        :param purchase_channel: 终端设备购买渠道。
        :type purchase_channel: str
        """
        
        

        self._model = None
        self._device_size = None
        self._purchase_channel = None
        self.discriminator = None

        if model is not None:
            self.model = model
        if device_size is not None:
            self.device_size = device_size
        if purchase_channel is not None:
            self.purchase_channel = purchase_channel

    @property
    def model(self):
        """Gets the model of this QueryDeviceInfoResultDTO.

        终端型号。

        :return: The model of this QueryDeviceInfoResultDTO.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this QueryDeviceInfoResultDTO.

        终端型号。

        :param model: The model of this QueryDeviceInfoResultDTO.
        :type model: str
        """
        self._model = model

    @property
    def device_size(self):
        """Gets the device_size of this QueryDeviceInfoResultDTO.

        设备终端产品尺寸。

        :return: The device_size of this QueryDeviceInfoResultDTO.
        :rtype: str
        """
        return self._device_size

    @device_size.setter
    def device_size(self, device_size):
        """Sets the device_size of this QueryDeviceInfoResultDTO.

        设备终端产品尺寸。

        :param device_size: The device_size of this QueryDeviceInfoResultDTO.
        :type device_size: str
        """
        self._device_size = device_size

    @property
    def purchase_channel(self):
        """Gets the purchase_channel of this QueryDeviceInfoResultDTO.

        终端设备购买渠道。

        :return: The purchase_channel of this QueryDeviceInfoResultDTO.
        :rtype: str
        """
        return self._purchase_channel

    @purchase_channel.setter
    def purchase_channel(self, purchase_channel):
        """Sets the purchase_channel of this QueryDeviceInfoResultDTO.

        终端设备购买渠道。

        :param purchase_channel: The purchase_channel of this QueryDeviceInfoResultDTO.
        :type purchase_channel: str
        """
        self._purchase_channel = purchase_channel

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
        if not isinstance(other, QueryDeviceInfoResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
