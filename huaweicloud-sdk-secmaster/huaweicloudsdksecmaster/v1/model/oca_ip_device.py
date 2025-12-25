# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIpDevice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'model': 'str',
        'vendor': 'OcaIpVendor'
    }

    attribute_map = {
        'type': 'type',
        'model': 'model',
        'vendor': 'vendor'
    }

    def __init__(self, type=None, model=None, vendor=None):
        r"""OcaIpDevice

        The model defined in huaweicloud sdk

        :param type: 设备类型
        :type type: str
        :param model: 设备型号
        :type model: str
        :param vendor: 
        :type vendor: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        
        

        self._type = None
        self._model = None
        self._vendor = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if model is not None:
            self.model = model
        if vendor is not None:
            self.vendor = vendor

    @property
    def type(self):
        r"""Gets the type of this OcaIpDevice.

        设备类型

        :return: The type of this OcaIpDevice.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OcaIpDevice.

        设备类型

        :param type: The type of this OcaIpDevice.
        :type type: str
        """
        self._type = type

    @property
    def model(self):
        r"""Gets the model of this OcaIpDevice.

        设备型号

        :return: The model of this OcaIpDevice.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this OcaIpDevice.

        设备型号

        :param model: The model of this OcaIpDevice.
        :type model: str
        """
        self._model = model

    @property
    def vendor(self):
        r"""Gets the vendor of this OcaIpDevice.

        :return: The vendor of this OcaIpDevice.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this OcaIpDevice.

        :param vendor: The vendor of this OcaIpDevice.
        :type vendor: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        self._vendor = vendor

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
        if not isinstance(other, OcaIpDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
