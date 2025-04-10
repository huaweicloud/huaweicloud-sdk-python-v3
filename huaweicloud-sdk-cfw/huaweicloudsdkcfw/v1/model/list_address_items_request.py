# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAddressItemsRequest:

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
        'key_word': 'str',
        'limit': 'int',
        'offset': 'int',
        'address': 'str',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str',
        'query_address_set_type': 'int'
    }

    attribute_map = {
        'set_id': 'set_id',
        'key_word': 'key_word',
        'limit': 'limit',
        'offset': 'offset',
        'address': 'address',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id',
        'query_address_set_type': 'query_address_set_type'
    }

    def __init__(self, set_id=None, key_word=None, limit=None, offset=None, address=None, enterprise_project_id=None, fw_instance_id=None, query_address_set_type=None):
        r"""ListAddressItemsRequest

        The model defined in huaweicloud sdk

        :param set_id: 地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。
        :type set_id: str
        :param key_word: 关键字，包括地址组成员名称或描述的一部分
        :type key_word: str
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param address: ip地址
        :type address: str
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param query_address_set_type: 查询地址组类型，0表示自定义地址组，1表示预定义地址组
        :type query_address_set_type: int
        """
        
        

        self._set_id = None
        self._key_word = None
        self._limit = None
        self._offset = None
        self._address = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self._query_address_set_type = None
        self.discriminator = None

        self.set_id = set_id
        if key_word is not None:
            self.key_word = key_word
        self.limit = limit
        self.offset = offset
        if address is not None:
            self.address = address
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if query_address_set_type is not None:
            self.query_address_set_type = query_address_set_type

    @property
    def set_id(self):
        r"""Gets the set_id of this ListAddressItemsRequest.

        地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :return: The set_id of this ListAddressItemsRequest.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this ListAddressItemsRequest.

        地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :param set_id: The set_id of this ListAddressItemsRequest.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def key_word(self):
        r"""Gets the key_word of this ListAddressItemsRequest.

        关键字，包括地址组成员名称或描述的一部分

        :return: The key_word of this ListAddressItemsRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListAddressItemsRequest.

        关键字，包括地址组成员名称或描述的一部分

        :param key_word: The key_word of this ListAddressItemsRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def limit(self):
        r"""Gets the limit of this ListAddressItemsRequest.

        每页显示个数，范围为1-1024

        :return: The limit of this ListAddressItemsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAddressItemsRequest.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListAddressItemsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAddressItemsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListAddressItemsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAddressItemsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListAddressItemsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def address(self):
        r"""Gets the address of this ListAddressItemsRequest.

        ip地址

        :return: The address of this ListAddressItemsRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ListAddressItemsRequest.

        ip地址

        :param address: The address of this ListAddressItemsRequest.
        :type address: str
        """
        self._address = address

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAddressItemsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListAddressItemsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAddressItemsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListAddressItemsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListAddressItemsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListAddressItemsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListAddressItemsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListAddressItemsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def query_address_set_type(self):
        r"""Gets the query_address_set_type of this ListAddressItemsRequest.

        查询地址组类型，0表示自定义地址组，1表示预定义地址组

        :return: The query_address_set_type of this ListAddressItemsRequest.
        :rtype: int
        """
        return self._query_address_set_type

    @query_address_set_type.setter
    def query_address_set_type(self, query_address_set_type):
        r"""Sets the query_address_set_type of this ListAddressItemsRequest.

        查询地址组类型，0表示自定义地址组，1表示预定义地址组

        :param query_address_set_type: The query_address_set_type of this ListAddressItemsRequest.
        :type query_address_set_type: int
        """
        self._query_address_set_type = query_address_set_type

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
        if not isinstance(other, ListAddressItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
