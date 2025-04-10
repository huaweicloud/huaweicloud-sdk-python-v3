# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressGroupVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address_set_type': 'int',
        'name': 'str',
        'set_id': 'str'
    }

    attribute_map = {
        'address_set_type': 'address_set_type',
        'name': 'name',
        'set_id': 'set_id'
    }

    def __init__(self, address_set_type=None, name=None, set_id=None):
        r"""AddressGroupVO

        The model defined in huaweicloud sdk

        :param address_set_type: 地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组
        :type address_set_type: int
        :param name: 关联IP地址组名称，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.name（.表示各对象之间层级的区分）获得。
        :type name: str
        :param set_id: 关联IP地址组ID，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。
        :type set_id: str
        """
        
        

        self._address_set_type = None
        self._name = None
        self._set_id = None
        self.discriminator = None

        if address_set_type is not None:
            self.address_set_type = address_set_type
        if name is not None:
            self.name = name
        if set_id is not None:
            self.set_id = set_id

    @property
    def address_set_type(self):
        r"""Gets the address_set_type of this AddressGroupVO.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :return: The address_set_type of this AddressGroupVO.
        :rtype: int
        """
        return self._address_set_type

    @address_set_type.setter
    def address_set_type(self, address_set_type):
        r"""Sets the address_set_type of this AddressGroupVO.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :param address_set_type: The address_set_type of this AddressGroupVO.
        :type address_set_type: int
        """
        self._address_set_type = address_set_type

    @property
    def name(self):
        r"""Gets the name of this AddressGroupVO.

        关联IP地址组名称，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.name（.表示各对象之间层级的区分）获得。

        :return: The name of this AddressGroupVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddressGroupVO.

        关联IP地址组名称，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.name（.表示各对象之间层级的区分）获得。

        :param name: The name of this AddressGroupVO.
        :type name: str
        """
        self._name = name

    @property
    def set_id(self):
        r"""Gets the set_id of this AddressGroupVO.

        关联IP地址组ID，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :return: The set_id of this AddressGroupVO.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this AddressGroupVO.

        关联IP地址组ID，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :param set_id: The set_id of this AddressGroupVO.
        :type set_id: str
        """
        self._set_id = set_id

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
        if not isinstance(other, AddressGroupVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
