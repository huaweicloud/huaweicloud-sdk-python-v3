# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBlackWhiteListsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'list_type': 'int',
        'address_type': 'int',
        'address': 'str',
        'port': 'str',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'list_type': 'list_type',
        'address_type': 'address_type',
        'address': 'address',
        'port': 'port',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, object_id=None, list_type=None, address_type=None, address=None, port=None, limit=None, offset=None, enterprise_project_id=None, fw_instance_id=None):
        r"""ListBlackWhiteListsRequest

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得
        :type object_id: str
        :param list_type: 黑白名单类型4：黑名单，5：白名单
        :type list_type: int
        :param address_type: ip地址类型0：ipv4，1:ipv6
        :type address_type: int
        :param address: ip地址
        :type address: str
        :param port: 端口
        :type port: str
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        """
        
        

        self._object_id = None
        self._list_type = None
        self._address_type = None
        self._address = None
        self._port = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self.discriminator = None

        self.object_id = object_id
        self.list_type = list_type
        if address_type is not None:
            self.address_type = address_type
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        self.limit = limit
        self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id

    @property
    def object_id(self):
        r"""Gets the object_id of this ListBlackWhiteListsRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :return: The object_id of this ListBlackWhiteListsRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ListBlackWhiteListsRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :param object_id: The object_id of this ListBlackWhiteListsRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def list_type(self):
        r"""Gets the list_type of this ListBlackWhiteListsRequest.

        黑白名单类型4：黑名单，5：白名单

        :return: The list_type of this ListBlackWhiteListsRequest.
        :rtype: int
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        r"""Sets the list_type of this ListBlackWhiteListsRequest.

        黑白名单类型4：黑名单，5：白名单

        :param list_type: The list_type of this ListBlackWhiteListsRequest.
        :type list_type: int
        """
        self._list_type = list_type

    @property
    def address_type(self):
        r"""Gets the address_type of this ListBlackWhiteListsRequest.

        ip地址类型0：ipv4，1:ipv6

        :return: The address_type of this ListBlackWhiteListsRequest.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this ListBlackWhiteListsRequest.

        ip地址类型0：ipv4，1:ipv6

        :param address_type: The address_type of this ListBlackWhiteListsRequest.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        r"""Gets the address of this ListBlackWhiteListsRequest.

        ip地址

        :return: The address of this ListBlackWhiteListsRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ListBlackWhiteListsRequest.

        ip地址

        :param address: The address of this ListBlackWhiteListsRequest.
        :type address: str
        """
        self._address = address

    @property
    def port(self):
        r"""Gets the port of this ListBlackWhiteListsRequest.

        端口

        :return: The port of this ListBlackWhiteListsRequest.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ListBlackWhiteListsRequest.

        端口

        :param port: The port of this ListBlackWhiteListsRequest.
        :type port: str
        """
        self._port = port

    @property
    def limit(self):
        r"""Gets the limit of this ListBlackWhiteListsRequest.

        每页显示个数，范围为1-1024

        :return: The limit of this ListBlackWhiteListsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBlackWhiteListsRequest.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListBlackWhiteListsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListBlackWhiteListsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListBlackWhiteListsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBlackWhiteListsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListBlackWhiteListsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListBlackWhiteListsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListBlackWhiteListsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListBlackWhiteListsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListBlackWhiteListsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListBlackWhiteListsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListBlackWhiteListsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListBlackWhiteListsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListBlackWhiteListsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, ListBlackWhiteListsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
