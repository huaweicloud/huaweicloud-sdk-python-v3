# coding: utf-8

import re
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
        'name': 'str',
        'address_type': 'int'
    }

    attribute_map = {
        'set_id': 'set_id',
        'ref_count': 'ref_count',
        'description': 'description',
        'name': 'name',
        'address_type': 'address_type'
    }

    def __init__(self, set_id=None, ref_count=None, description=None, name=None, address_type=None):
        """AddressSetListResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param set_id: 地址组id
        :type set_id: str
        :param ref_count: 引用次数
        :type ref_count: int
        :param description: 描述信息
        :type description: str
        :param name: 地址组名称
        :type name: str
        :param address_type: 地址类型0 ipv4,1 ipv6
        :type address_type: int
        """
        
        

        self._set_id = None
        self._ref_count = None
        self._description = None
        self._name = None
        self._address_type = None
        self.discriminator = None

        if set_id is not None:
            self.set_id = set_id
        if ref_count is not None:
            self.ref_count = ref_count
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if address_type is not None:
            self.address_type = address_type

    @property
    def set_id(self):
        """Gets the set_id of this AddressSetListResponseDTODataRecords.

        地址组id

        :return: The set_id of this AddressSetListResponseDTODataRecords.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this AddressSetListResponseDTODataRecords.

        地址组id

        :param set_id: The set_id of this AddressSetListResponseDTODataRecords.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def ref_count(self):
        """Gets the ref_count of this AddressSetListResponseDTODataRecords.

        引用次数

        :return: The ref_count of this AddressSetListResponseDTODataRecords.
        :rtype: int
        """
        return self._ref_count

    @ref_count.setter
    def ref_count(self, ref_count):
        """Sets the ref_count of this AddressSetListResponseDTODataRecords.

        引用次数

        :param ref_count: The ref_count of this AddressSetListResponseDTODataRecords.
        :type ref_count: int
        """
        self._ref_count = ref_count

    @property
    def description(self):
        """Gets the description of this AddressSetListResponseDTODataRecords.

        描述信息

        :return: The description of this AddressSetListResponseDTODataRecords.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddressSetListResponseDTODataRecords.

        描述信息

        :param description: The description of this AddressSetListResponseDTODataRecords.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this AddressSetListResponseDTODataRecords.

        地址组名称

        :return: The name of this AddressSetListResponseDTODataRecords.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressSetListResponseDTODataRecords.

        地址组名称

        :param name: The name of this AddressSetListResponseDTODataRecords.
        :type name: str
        """
        self._name = name

    @property
    def address_type(self):
        """Gets the address_type of this AddressSetListResponseDTODataRecords.

        地址类型0 ipv4,1 ipv6

        :return: The address_type of this AddressSetListResponseDTODataRecords.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this AddressSetListResponseDTODataRecords.

        地址类型0 ipv4,1 ipv6

        :param address_type: The address_type of this AddressSetListResponseDTODataRecords.
        :type address_type: int
        """
        self._address_type = address_type

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
