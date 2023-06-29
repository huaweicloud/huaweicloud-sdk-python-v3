# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'availability_zone': 'str',
        'os_type': 'str',
        'charge_mode': 'str',
        'architecture': 'str',
        'package_type': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'availability_zone': 'availability_zone',
        'os_type': 'os_type',
        'charge_mode': 'charge_mode',
        'architecture': 'architecture',
        'package_type': 'package_type'
    }

    def __init__(self, product_id=None, availability_zone=None, os_type=None, charge_mode=None, architecture=None, package_type=None):
        """ListProductRequest

        The model defined in huaweicloud sdk

        :param product_id: 如果不为空，将按产品ID进行过滤后返回。
        :type product_id: str
        :param availability_zone: 可用分区，如果不为空，将按可用分区进行过滤后返回。 - 获取方式详见可用区管理ListAvailabilityZone：\&quot;GET  /v1/{project_id}/availability-zone\&quot;。
        :type availability_zone: str
        :param os_type: 产品套餐的操作系统类型，当前支持：Windows - Linux - Windows - Other
        :type os_type: str
        :param charge_mode: 套餐标识。 - 1：表示包周期。 - 0：表示按需。
        :type charge_mode: str
        :param architecture: 架构类型，当前支持：x86。 - x86 - arm
        :type architecture: str
        :param package_type: 套餐类型。 - general：表示产品通用套餐。 - dedicated：表示产品专属主机套餐。
        :type package_type: str
        """
        
        

        self._product_id = None
        self._availability_zone = None
        self._os_type = None
        self._charge_mode = None
        self._architecture = None
        self._package_type = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if os_type is not None:
            self.os_type = os_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if architecture is not None:
            self.architecture = architecture
        if package_type is not None:
            self.package_type = package_type

    @property
    def product_id(self):
        """Gets the product_id of this ListProductRequest.

        如果不为空，将按产品ID进行过滤后返回。

        :return: The product_id of this ListProductRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ListProductRequest.

        如果不为空，将按产品ID进行过滤后返回。

        :param product_id: The product_id of this ListProductRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListProductRequest.

        可用分区，如果不为空，将按可用分区进行过滤后返回。 - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :return: The availability_zone of this ListProductRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListProductRequest.

        可用分区，如果不为空，将按可用分区进行过滤后返回。 - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :param availability_zone: The availability_zone of this ListProductRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def os_type(self):
        """Gets the os_type of this ListProductRequest.

        产品套餐的操作系统类型，当前支持：Windows - Linux - Windows - Other

        :return: The os_type of this ListProductRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListProductRequest.

        产品套餐的操作系统类型，当前支持：Windows - Linux - Windows - Other

        :param os_type: The os_type of this ListProductRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListProductRequest.

        套餐标识。 - 1：表示包周期。 - 0：表示按需。

        :return: The charge_mode of this ListProductRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListProductRequest.

        套餐标识。 - 1：表示包周期。 - 0：表示按需。

        :param charge_mode: The charge_mode of this ListProductRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def architecture(self):
        """Gets the architecture of this ListProductRequest.

        架构类型，当前支持：x86。 - x86 - arm

        :return: The architecture of this ListProductRequest.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ListProductRequest.

        架构类型，当前支持：x86。 - x86 - arm

        :param architecture: The architecture of this ListProductRequest.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def package_type(self):
        """Gets the package_type of this ListProductRequest.

        套餐类型。 - general：表示产品通用套餐。 - dedicated：表示产品专属主机套餐。

        :return: The package_type of this ListProductRequest.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this ListProductRequest.

        套餐类型。 - general：表示产品通用套餐。 - dedicated：表示产品专属主机套餐。

        :param package_type: The package_type of this ListProductRequest.
        :type package_type: str
        """
        self._package_type = package_type

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
        if not isinstance(other, ListProductRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
