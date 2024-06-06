# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableFlavorInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'az_status': 'dict(str, str)'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'az_status': 'az_status'
    }

    def __init__(self, spec_code=None, vcpus=None, ram=None, az_status=None):
        """AvailableFlavorInfoResult

        The model defined in huaweicloud sdk

        :param spec_code: 资源规格编码。
        :type spec_code: str
        :param vcpus: CPU核数。
        :type vcpus: str
        :param ram: 内存大小，单位：GB。
        :type ram: str
        :param az_status: 其中key是可用区编号，value是规格所在az的状态。
        :type az_status: dict(str, str)
        """
        
        

        self._spec_code = None
        self._vcpus = None
        self._ram = None
        self._az_status = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if az_status is not None:
            self.az_status = az_status

    @property
    def spec_code(self):
        """Gets the spec_code of this AvailableFlavorInfoResult.

        资源规格编码。

        :return: The spec_code of this AvailableFlavorInfoResult.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this AvailableFlavorInfoResult.

        资源规格编码。

        :param spec_code: The spec_code of this AvailableFlavorInfoResult.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def vcpus(self):
        """Gets the vcpus of this AvailableFlavorInfoResult.

        CPU核数。

        :return: The vcpus of this AvailableFlavorInfoResult.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this AvailableFlavorInfoResult.

        CPU核数。

        :param vcpus: The vcpus of this AvailableFlavorInfoResult.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this AvailableFlavorInfoResult.

        内存大小，单位：GB。

        :return: The ram of this AvailableFlavorInfoResult.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this AvailableFlavorInfoResult.

        内存大小，单位：GB。

        :param ram: The ram of this AvailableFlavorInfoResult.
        :type ram: str
        """
        self._ram = ram

    @property
    def az_status(self):
        """Gets the az_status of this AvailableFlavorInfoResult.

        其中key是可用区编号，value是规格所在az的状态。

        :return: The az_status of this AvailableFlavorInfoResult.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this AvailableFlavorInfoResult.

        其中key是可用区编号，value是规格所在az的状态。

        :param az_status: The az_status of this AvailableFlavorInfoResult.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

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
        if not isinstance(other, AvailableFlavorInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
