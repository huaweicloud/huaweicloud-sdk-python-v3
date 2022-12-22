# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEipResourcesRequest:

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
        'address_type': 'int'
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
        'address_type': 'address_type'
    }

    def __init__(self, object_id=None, key_word=None, status=None, sync=None, limit=None, offset=None, enterprise_project_id=None, device_key=None, address_type=None):
        """ListEipResourcesRequest

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。
        :type object_id: str
        :param key_word: 弹性公网ID/弹性公网IP
        :type key_word: str
        :param status: 防护状态 null-全部 0-开启防护 1-关闭防护
        :type status: str
        :param sync: 是否同步租户EIP数据 0-不同步 1-同步
        :type sync: int
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param device_key: 设备键
        :type device_key: str
        :param address_type: 地址类型0 ipv4,1 ipv6
        :type address_type: int
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

    @property
    def object_id(self):
        """Gets the object_id of this ListEipResourcesRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :return: The object_id of this ListEipResourcesRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ListEipResourcesRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :param object_id: The object_id of this ListEipResourcesRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def key_word(self):
        """Gets the key_word of this ListEipResourcesRequest.

        弹性公网ID/弹性公网IP

        :return: The key_word of this ListEipResourcesRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this ListEipResourcesRequest.

        弹性公网ID/弹性公网IP

        :param key_word: The key_word of this ListEipResourcesRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def status(self):
        """Gets the status of this ListEipResourcesRequest.

        防护状态 null-全部 0-开启防护 1-关闭防护

        :return: The status of this ListEipResourcesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEipResourcesRequest.

        防护状态 null-全部 0-开启防护 1-关闭防护

        :param status: The status of this ListEipResourcesRequest.
        :type status: str
        """
        self._status = status

    @property
    def sync(self):
        """Gets the sync of this ListEipResourcesRequest.

        是否同步租户EIP数据 0-不同步 1-同步

        :return: The sync of this ListEipResourcesRequest.
        :rtype: int
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this ListEipResourcesRequest.

        是否同步租户EIP数据 0-不同步 1-同步

        :param sync: The sync of this ListEipResourcesRequest.
        :type sync: int
        """
        self._sync = sync

    @property
    def limit(self):
        """Gets the limit of this ListEipResourcesRequest.

        每页显示个数

        :return: The limit of this ListEipResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEipResourcesRequest.

        每页显示个数

        :param limit: The limit of this ListEipResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEipResourcesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListEipResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEipResourcesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListEipResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListEipResourcesRequest.

        企业项目id

        :return: The enterprise_project_id of this ListEipResourcesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListEipResourcesRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListEipResourcesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def device_key(self):
        """Gets the device_key of this ListEipResourcesRequest.

        设备键

        :return: The device_key of this ListEipResourcesRequest.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """Sets the device_key of this ListEipResourcesRequest.

        设备键

        :param device_key: The device_key of this ListEipResourcesRequest.
        :type device_key: str
        """
        self._device_key = device_key

    @property
    def address_type(self):
        """Gets the address_type of this ListEipResourcesRequest.

        地址类型0 ipv4,1 ipv6

        :return: The address_type of this ListEipResourcesRequest.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this ListEipResourcesRequest.

        地址类型0 ipv4,1 ipv6

        :param address_type: The address_type of this ListEipResourcesRequest.
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
        if not isinstance(other, ListEipResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
