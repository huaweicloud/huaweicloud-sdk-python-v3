# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubsetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'device_id': 'int',
        'limit': 'int',
        'device_name': 'str',
        'status': 'int',
        'online_status': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'device_id': 'device_id',
        'limit': 'limit',
        'device_name': 'device_name',
        'status': 'status',
        'online_status': 'online_status',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, device_id=None, limit=None, device_name=None, status=None, online_status=None, offset=None):
        """ListSubsetsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param device_id: 设备ID
        :type device_id: int
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param device_name: 设备名称
        :type device_name: str
        :param status: 设备状态 0-启动 1-停用
        :type status: int
        :param online_status: 设备状态 0-未连接 1-在线 2-离线
        :type online_status: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        """
        
        

        self._instance_id = None
        self._device_id = None
        self._limit = None
        self._device_name = None
        self._status = None
        self._online_status = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        self.device_id = device_id
        if limit is not None:
            self.limit = limit
        if device_name is not None:
            self.device_name = device_name
        if status is not None:
            self.status = status
        if online_status is not None:
            self.online_status = online_status
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSubsetsRequest.

        实例ID

        :return: The instance_id of this ListSubsetsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSubsetsRequest.

        实例ID

        :param instance_id: The instance_id of this ListSubsetsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def device_id(self):
        """Gets the device_id of this ListSubsetsRequest.

        设备ID

        :return: The device_id of this ListSubsetsRequest.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListSubsetsRequest.

        设备ID

        :param device_id: The device_id of this ListSubsetsRequest.
        :type device_id: int
        """
        self._device_id = device_id

    @property
    def limit(self):
        """Gets the limit of this ListSubsetsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListSubsetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubsetsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListSubsetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def device_name(self):
        """Gets the device_name of this ListSubsetsRequest.

        设备名称

        :return: The device_name of this ListSubsetsRequest.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ListSubsetsRequest.

        设备名称

        :param device_name: The device_name of this ListSubsetsRequest.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def status(self):
        """Gets the status of this ListSubsetsRequest.

        设备状态 0-启动 1-停用

        :return: The status of this ListSubsetsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSubsetsRequest.

        设备状态 0-启动 1-停用

        :param status: The status of this ListSubsetsRequest.
        :type status: int
        """
        self._status = status

    @property
    def online_status(self):
        """Gets the online_status of this ListSubsetsRequest.

        设备状态 0-未连接 1-在线 2-离线

        :return: The online_status of this ListSubsetsRequest.
        :rtype: int
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """Sets the online_status of this ListSubsetsRequest.

        设备状态 0-未连接 1-在线 2-离线

        :param online_status: The online_status of this ListSubsetsRequest.
        :type online_status: int
        """
        self._online_status = online_status

    @property
    def offset(self):
        """Gets the offset of this ListSubsetsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListSubsetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubsetsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListSubsetsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListSubsetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
