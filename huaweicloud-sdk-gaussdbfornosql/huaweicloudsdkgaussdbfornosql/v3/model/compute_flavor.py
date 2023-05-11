# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpus': 'str',
        'ram': 'str',
        'spec_code': 'str',
        'az_status': 'dict(str, str)',
        'region_status': 'str'
    }

    attribute_map = {
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'az_status': 'az_status',
        'region_status': 'region_status'
    }

    def __init__(self, vcpus=None, ram=None, spec_code=None, az_status=None, region_status=None):
        """ComputeFlavor

        The model defined in huaweicloud sdk

        :param vcpus: cpu核数。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param spec_code: 规格码。
        :type spec_code: str
        :param az_status: 可用区状态。
        :type az_status: dict(str, str)
        :param region_status: Region状态。
        :type region_status: str
        """
        
        

        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._az_status = None
        self._region_status = None
        self.discriminator = None

        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.az_status = az_status
        self.region_status = region_status

    @property
    def vcpus(self):
        """Gets the vcpus of this ComputeFlavor.

        cpu核数。

        :return: The vcpus of this ComputeFlavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this ComputeFlavor.

        cpu核数。

        :param vcpus: The vcpus of this ComputeFlavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this ComputeFlavor.

        内存大小，单位为GB。

        :return: The ram of this ComputeFlavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ComputeFlavor.

        内存大小，单位为GB。

        :param ram: The ram of this ComputeFlavor.
        :type ram: str
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this ComputeFlavor.

        规格码。

        :return: The spec_code of this ComputeFlavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ComputeFlavor.

        规格码。

        :param spec_code: The spec_code of this ComputeFlavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def az_status(self):
        """Gets the az_status of this ComputeFlavor.

        可用区状态。

        :return: The az_status of this ComputeFlavor.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this ComputeFlavor.

        可用区状态。

        :param az_status: The az_status of this ComputeFlavor.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def region_status(self):
        """Gets the region_status of this ComputeFlavor.

        Region状态。

        :return: The region_status of this ComputeFlavor.
        :rtype: str
        """
        return self._region_status

    @region_status.setter
    def region_status(self, region_status):
        """Sets the region_status of this ComputeFlavor.

        Region状态。

        :param region_status: The region_status of this ComputeFlavor.
        :type region_status: str
        """
        self._region_status = region_status

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
        if not isinstance(other, ComputeFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
