# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEipsRequest:

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
        'key_word': 'str',
        'status': 'str',
        'sync': 'int',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str',
        'device_key': 'str',
        'address_type': 'int',
        'fw_instance_id': 'str',
        'fw_key_word': 'str',
        'eps_id': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'key_word': 'key_word',
        'status': 'status',
        'sync': 'sync',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id',
        'device_key': 'device_key',
        'address_type': 'address_type',
        'fw_instance_id': 'fw_instance_id',
        'fw_key_word': 'fw_key_word',
        'eps_id': 'eps_id',
        'tags': 'tags'
    }

    def __init__(self, object_id=None, key_word=None, status=None, sync=None, limit=None, offset=None, enterprise_project_id=None, device_key=None, address_type=None, fw_instance_id=None, fw_key_word=None, eps_id=None, tags=None):
        r"""ListEipsRequest

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。
        :type object_id: str
        :param key_word: 查询防护EIP列表关键字，可选用弹性公网ID和弹性公网IP
        :type key_word: str
        :param status: 防护状态 null-全部 0-开启防护 1-关闭防护
        :type status: str
        :param sync: 是否同步租户EIP数据 0-不同步 1-同步
        :type sync: int
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param device_key: 设备关键字，是eip绑定的资产的名称或id
        :type device_key: str
        :param address_type: 地址类型0 ipv4，1 ipv6
        :type address_type: int
        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param fw_key_word: 防火墙关键字，可使用防火墙id或名称查询，可通过[防火墙ID获取方式](cfw_02_0028.xml)
        :type fw_key_word: str
        :param eps_id: 弹性公网ip的企业项目id，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，租户未开启企业项目时为0
        :type eps_id: str
        :param tags: 标签列表信息可通过查询EIP服务界面列表标签页签获得
        :type tags: str
        """
        
        

        self._object_id = None
        self._key_word = None
        self._status = None
        self._sync = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self._device_key = None
        self._address_type = None
        self._fw_instance_id = None
        self._fw_key_word = None
        self._eps_id = None
        self._tags = None
        self.discriminator = None

        self.object_id = object_id
        if key_word is not None:
            self.key_word = key_word
        if status is not None:
            self.status = status
        if sync is not None:
            self.sync = sync
        self.limit = limit
        self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if device_key is not None:
            self.device_key = device_key
        if address_type is not None:
            self.address_type = address_type
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if fw_key_word is not None:
            self.fw_key_word = fw_key_word
        if eps_id is not None:
            self.eps_id = eps_id
        if tags is not None:
            self.tags = tags

    @property
    def object_id(self):
        r"""Gets the object_id of this ListEipsRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :return: The object_id of this ListEipsRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ListEipsRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :param object_id: The object_id of this ListEipsRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def key_word(self):
        r"""Gets the key_word of this ListEipsRequest.

        查询防护EIP列表关键字，可选用弹性公网ID和弹性公网IP

        :return: The key_word of this ListEipsRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListEipsRequest.

        查询防护EIP列表关键字，可选用弹性公网ID和弹性公网IP

        :param key_word: The key_word of this ListEipsRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def status(self):
        r"""Gets the status of this ListEipsRequest.

        防护状态 null-全部 0-开启防护 1-关闭防护

        :return: The status of this ListEipsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListEipsRequest.

        防护状态 null-全部 0-开启防护 1-关闭防护

        :param status: The status of this ListEipsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sync(self):
        r"""Gets the sync of this ListEipsRequest.

        是否同步租户EIP数据 0-不同步 1-同步

        :return: The sync of this ListEipsRequest.
        :rtype: int
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        r"""Sets the sync of this ListEipsRequest.

        是否同步租户EIP数据 0-不同步 1-同步

        :param sync: The sync of this ListEipsRequest.
        :type sync: int
        """
        self._sync = sync

    @property
    def limit(self):
        r"""Gets the limit of this ListEipsRequest.

        每页显示个数，范围为1-1024

        :return: The limit of this ListEipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEipsRequest.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListEipsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListEipsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListEipsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEipsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListEipsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEipsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListEipsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEipsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListEipsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def device_key(self):
        r"""Gets the device_key of this ListEipsRequest.

        设备关键字，是eip绑定的资产的名称或id

        :return: The device_key of this ListEipsRequest.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        r"""Sets the device_key of this ListEipsRequest.

        设备关键字，是eip绑定的资产的名称或id

        :param device_key: The device_key of this ListEipsRequest.
        :type device_key: str
        """
        self._device_key = device_key

    @property
    def address_type(self):
        r"""Gets the address_type of this ListEipsRequest.

        地址类型0 ipv4，1 ipv6

        :return: The address_type of this ListEipsRequest.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this ListEipsRequest.

        地址类型0 ipv4，1 ipv6

        :param address_type: The address_type of this ListEipsRequest.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListEipsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListEipsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListEipsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListEipsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def fw_key_word(self):
        r"""Gets the fw_key_word of this ListEipsRequest.

        防火墙关键字，可使用防火墙id或名称查询，可通过[防火墙ID获取方式](cfw_02_0028.xml)

        :return: The fw_key_word of this ListEipsRequest.
        :rtype: str
        """
        return self._fw_key_word

    @fw_key_word.setter
    def fw_key_word(self, fw_key_word):
        r"""Sets the fw_key_word of this ListEipsRequest.

        防火墙关键字，可使用防火墙id或名称查询，可通过[防火墙ID获取方式](cfw_02_0028.xml)

        :param fw_key_word: The fw_key_word of this ListEipsRequest.
        :type fw_key_word: str
        """
        self._fw_key_word = fw_key_word

    @property
    def eps_id(self):
        r"""Gets the eps_id of this ListEipsRequest.

        弹性公网ip的企业项目id，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，租户未开启企业项目时为0

        :return: The eps_id of this ListEipsRequest.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this ListEipsRequest.

        弹性公网ip的企业项目id，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，租户未开启企业项目时为0

        :param eps_id: The eps_id of this ListEipsRequest.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def tags(self):
        r"""Gets the tags of this ListEipsRequest.

        标签列表信息可通过查询EIP服务界面列表标签页签获得

        :return: The tags of this ListEipsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListEipsRequest.

        标签列表信息可通过查询EIP服务界面列表标签页签获得

        :param tags: The tags of this ListEipsRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListEipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
