# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressSetListResponseDTODataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'ref_count': 'int',
        'description': 'str',
        'address_type': 'int',
        'object_id': 'str',
        'address_set_type': 'int',
        'name': 'str'
    }

    attribute_map = {
        'set_id': 'set_id',
        'ref_count': 'ref_count',
        'description': 'description',
        'address_type': 'address_type',
        'object_id': 'object_id',
        'address_set_type': 'address_set_type',
        'name': 'name'
    }

    def __init__(self, set_id=None, ref_count=None, description=None, address_type=None, object_id=None, address_set_type=None, name=None):
        r"""AddressSetListResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param set_id: 地址组id
        :type set_id: str
        :param ref_count: 地址组被规则引用次数
        :type ref_count: int
        :param description: 描述信息
        :type description: str
        :param address_type: 地址类型0 ipv4，1 ipv6
        :type address_type: int
        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得
        :type object_id: str
        :param address_set_type: 地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组
        :type address_set_type: int
        :param name: 地址组名称
        :type name: str
        """
        
        

        self._set_id = None
        self._ref_count = None
        self._description = None
        self._address_type = None
        self._object_id = None
        self._address_set_type = None
        self._name = None
        self.discriminator = None

        if set_id is not None:
            self.set_id = set_id
        if ref_count is not None:
            self.ref_count = ref_count
        if description is not None:
            self.description = description
        if address_type is not None:
            self.address_type = address_type
        if object_id is not None:
            self.object_id = object_id
        if address_set_type is not None:
            self.address_set_type = address_set_type
        if name is not None:
            self.name = name

    @property
    def set_id(self):
        r"""Gets the set_id of this AddressSetListResponseDTODataRecords.

        地址组id

        :return: The set_id of this AddressSetListResponseDTODataRecords.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this AddressSetListResponseDTODataRecords.

        地址组id

        :param set_id: The set_id of this AddressSetListResponseDTODataRecords.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def ref_count(self):
        r"""Gets the ref_count of this AddressSetListResponseDTODataRecords.

        地址组被规则引用次数

        :return: The ref_count of this AddressSetListResponseDTODataRecords.
        :rtype: int
        """
        return self._ref_count

    @ref_count.setter
    def ref_count(self, ref_count):
        r"""Sets the ref_count of this AddressSetListResponseDTODataRecords.

        地址组被规则引用次数

        :param ref_count: The ref_count of this AddressSetListResponseDTODataRecords.
        :type ref_count: int
        """
        self._ref_count = ref_count

    @property
    def description(self):
        r"""Gets the description of this AddressSetListResponseDTODataRecords.

        描述信息

        :return: The description of this AddressSetListResponseDTODataRecords.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddressSetListResponseDTODataRecords.

        描述信息

        :param description: The description of this AddressSetListResponseDTODataRecords.
        :type description: str
        """
        self._description = description

    @property
    def address_type(self):
        r"""Gets the address_type of this AddressSetListResponseDTODataRecords.

        地址类型0 ipv4，1 ipv6

        :return: The address_type of this AddressSetListResponseDTODataRecords.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this AddressSetListResponseDTODataRecords.

        地址类型0 ipv4，1 ipv6

        :param address_type: The address_type of this AddressSetListResponseDTODataRecords.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def object_id(self):
        r"""Gets the object_id of this AddressSetListResponseDTODataRecords.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :return: The object_id of this AddressSetListResponseDTODataRecords.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AddressSetListResponseDTODataRecords.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :param object_id: The object_id of this AddressSetListResponseDTODataRecords.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def address_set_type(self):
        r"""Gets the address_set_type of this AddressSetListResponseDTODataRecords.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :return: The address_set_type of this AddressSetListResponseDTODataRecords.
        :rtype: int
        """
        return self._address_set_type

    @address_set_type.setter
    def address_set_type(self, address_set_type):
        r"""Sets the address_set_type of this AddressSetListResponseDTODataRecords.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :param address_set_type: The address_set_type of this AddressSetListResponseDTODataRecords.
        :type address_set_type: int
        """
        self._address_set_type = address_set_type

    @property
    def name(self):
        r"""Gets the name of this AddressSetListResponseDTODataRecords.

        地址组名称

        :return: The name of this AddressSetListResponseDTODataRecords.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddressSetListResponseDTODataRecords.

        地址组名称

        :param name: The name of this AddressSetListResponseDTODataRecords.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AddressSetListResponseDTODataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
