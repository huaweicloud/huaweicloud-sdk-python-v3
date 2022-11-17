# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductDetailInfo:

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
        'flavor_id': 'str',
        'type': 'str',
        'cpu': 'str',
        'memory': 'str',
        'descriptions': 'str',
        'charge_mode': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'type': 'type',
        'cpu': 'cpu',
        'memory': 'memory',
        'descriptions': 'descriptions',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, product_id=None, flavor_id=None, type=None, cpu=None, memory=None, descriptions=None, charge_mode=None):
        """ProductDetailInfo

        The model defined in huaweicloud sdk

        :param product_id: 产品ID。
        :type product_id: str
        :param flavor_id: 产品规格ID。
        :type flavor_id: str
        :param type: 产品类型。  - BASE：表示产品基础套餐，套餐镜像中不包括除操作系统之外的其他商业软件，私有镜像场景只能使用此类套餐。
        :type type: str
        :param cpu: CPU
        :type cpu: str
        :param memory: 内存。
        :type memory: str
        :param descriptions: 产品描述。
        :type descriptions: str
        :param charge_mode: 周期套餐标识，1表示包周期，0表示按需。
        :type charge_mode: str
        """
        
        

        self._product_id = None
        self._flavor_id = None
        self._type = None
        self._cpu = None
        self._memory = None
        self._descriptions = None
        self._charge_mode = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if type is not None:
            self.type = type
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if descriptions is not None:
            self.descriptions = descriptions
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def product_id(self):
        """Gets the product_id of this ProductDetailInfo.

        产品ID。

        :return: The product_id of this ProductDetailInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductDetailInfo.

        产品ID。

        :param product_id: The product_id of this ProductDetailInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this ProductDetailInfo.

        产品规格ID。

        :return: The flavor_id of this ProductDetailInfo.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this ProductDetailInfo.

        产品规格ID。

        :param flavor_id: The flavor_id of this ProductDetailInfo.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def type(self):
        """Gets the type of this ProductDetailInfo.

        产品类型。  - BASE：表示产品基础套餐，套餐镜像中不包括除操作系统之外的其他商业软件，私有镜像场景只能使用此类套餐。

        :return: The type of this ProductDetailInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductDetailInfo.

        产品类型。  - BASE：表示产品基础套餐，套餐镜像中不包括除操作系统之外的其他商业软件，私有镜像场景只能使用此类套餐。

        :param type: The type of this ProductDetailInfo.
        :type type: str
        """
        self._type = type

    @property
    def cpu(self):
        """Gets the cpu of this ProductDetailInfo.

        CPU

        :return: The cpu of this ProductDetailInfo.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ProductDetailInfo.

        CPU

        :param cpu: The cpu of this ProductDetailInfo.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this ProductDetailInfo.

        内存。

        :return: The memory of this ProductDetailInfo.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ProductDetailInfo.

        内存。

        :param memory: The memory of this ProductDetailInfo.
        :type memory: str
        """
        self._memory = memory

    @property
    def descriptions(self):
        """Gets the descriptions of this ProductDetailInfo.

        产品描述。

        :return: The descriptions of this ProductDetailInfo.
        :rtype: str
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """Sets the descriptions of this ProductDetailInfo.

        产品描述。

        :param descriptions: The descriptions of this ProductDetailInfo.
        :type descriptions: str
        """
        self._descriptions = descriptions

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ProductDetailInfo.

        周期套餐标识，1表示包周期，0表示按需。

        :return: The charge_mode of this ProductDetailInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ProductDetailInfo.

        周期套餐标识，1表示包周期，0表示按需。

        :param charge_mode: The charge_mode of this ProductDetailInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, ProductDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
