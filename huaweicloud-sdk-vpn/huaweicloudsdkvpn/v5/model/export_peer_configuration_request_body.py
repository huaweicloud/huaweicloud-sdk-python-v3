# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportPeerConfigurationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor': 'str',
        'type': 'str',
        'model': 'str',
        'version': 'str'
    }

    attribute_map = {
        'vendor': 'vendor',
        'type': 'type',
        'model': 'model',
        'version': 'version'
    }

    def __init__(self, vendor=None, type=None, model=None, version=None):
        r"""ExportPeerConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param vendor: 设备厂商
        :type vendor: str
        :param type: 设备系列
        :type type: str
        :param model: 设备型号
        :type model: str
        :param version: 设备版本
        :type version: str
        """
        
        

        self._vendor = None
        self._type = None
        self._model = None
        self._version = None
        self.discriminator = None

        self.vendor = vendor
        self.type = type
        self.model = model
        self.version = version

    @property
    def vendor(self):
        r"""Gets the vendor of this ExportPeerConfigurationRequestBody.

        设备厂商

        :return: The vendor of this ExportPeerConfigurationRequestBody.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this ExportPeerConfigurationRequestBody.

        设备厂商

        :param vendor: The vendor of this ExportPeerConfigurationRequestBody.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def type(self):
        r"""Gets the type of this ExportPeerConfigurationRequestBody.

        设备系列

        :return: The type of this ExportPeerConfigurationRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExportPeerConfigurationRequestBody.

        设备系列

        :param type: The type of this ExportPeerConfigurationRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def model(self):
        r"""Gets the model of this ExportPeerConfigurationRequestBody.

        设备型号

        :return: The model of this ExportPeerConfigurationRequestBody.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this ExportPeerConfigurationRequestBody.

        设备型号

        :param model: The model of this ExportPeerConfigurationRequestBody.
        :type model: str
        """
        self._model = model

    @property
    def version(self):
        r"""Gets the version of this ExportPeerConfigurationRequestBody.

        设备版本

        :return: The version of this ExportPeerConfigurationRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ExportPeerConfigurationRequestBody.

        设备版本

        :param version: The version of this ExportPeerConfigurationRequestBody.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ExportPeerConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
