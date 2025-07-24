# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirmwareDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_name': 'str',
        'model': 'str',
        'manufacturer': 'str',
        'version': 'str'
    }

    attribute_map = {
        'component_name': 'component_name',
        'model': 'model',
        'manufacturer': 'manufacturer',
        'version': 'version'
    }

    def __init__(self, component_name=None, model=None, manufacturer=None, version=None):
        r"""FirmwareDetails

        The model defined in huaweicloud sdk

        :param component_name: 组件
        :type component_name: str
        :param model: 型号
        :type model: str
        :param manufacturer: 制造商
        :type manufacturer: str
        :param version: 版本
        :type version: str
        """
        
        

        self._component_name = None
        self._model = None
        self._manufacturer = None
        self._version = None
        self.discriminator = None

        if component_name is not None:
            self.component_name = component_name
        if model is not None:
            self.model = model
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if version is not None:
            self.version = version

    @property
    def component_name(self):
        r"""Gets the component_name of this FirmwareDetails.

        组件

        :return: The component_name of this FirmwareDetails.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this FirmwareDetails.

        组件

        :param component_name: The component_name of this FirmwareDetails.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def model(self):
        r"""Gets the model of this FirmwareDetails.

        型号

        :return: The model of this FirmwareDetails.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this FirmwareDetails.

        型号

        :param model: The model of this FirmwareDetails.
        :type model: str
        """
        self._model = model

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this FirmwareDetails.

        制造商

        :return: The manufacturer of this FirmwareDetails.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this FirmwareDetails.

        制造商

        :param manufacturer: The manufacturer of this FirmwareDetails.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def version(self):
        r"""Gets the version of this FirmwareDetails.

        版本

        :return: The version of this FirmwareDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this FirmwareDetails.

        版本

        :param version: The version of this FirmwareDetails.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, FirmwareDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
