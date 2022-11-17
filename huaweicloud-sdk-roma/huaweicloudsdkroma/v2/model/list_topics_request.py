# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicsRequest:

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
        'offset': 'int',
        'name': 'str',
        'topic_permission': 'int',
        'topic_type': 'int',
        'is_private': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'device_id': 'device_id',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'topic_permission': 'topic_permission',
        'topic_type': 'topic_type',
        'is_private': 'is_private'
    }

    def __init__(self, instance_id=None, device_id=None, limit=None, offset=None, name=None, topic_permission=None, topic_type=None, is_private=None):
        """ListTopicsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param device_id: 设备ID
        :type device_id: int
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param name: topic名称
        :type name: str
        :param topic_permission: topic权限，0为发布，1为订阅
        :type topic_permission: int
        :param topic_type: topic类型，0为设备类topic，1为产品类topic
        :type topic_type: int
        :param is_private: topic是否为自定义，0为基础topic，1为自定义topic
        :type is_private: int
        """
        
        

        self._instance_id = None
        self._device_id = None
        self._limit = None
        self._offset = None
        self._name = None
        self._topic_permission = None
        self._topic_type = None
        self._is_private = None
        self.discriminator = None

        self.instance_id = instance_id
        self.device_id = device_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if topic_permission is not None:
            self.topic_permission = topic_permission
        if topic_type is not None:
            self.topic_type = topic_type
        if is_private is not None:
            self.is_private = is_private

    @property
    def instance_id(self):
        """Gets the instance_id of this ListTopicsRequest.

        实例ID

        :return: The instance_id of this ListTopicsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListTopicsRequest.

        实例ID

        :param instance_id: The instance_id of this ListTopicsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def device_id(self):
        """Gets the device_id of this ListTopicsRequest.

        设备ID

        :return: The device_id of this ListTopicsRequest.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListTopicsRequest.

        设备ID

        :param device_id: The device_id of this ListTopicsRequest.
        :type device_id: int
        """
        self._device_id = device_id

    @property
    def limit(self):
        """Gets the limit of this ListTopicsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListTopicsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTopicsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListTopicsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTopicsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListTopicsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTopicsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListTopicsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        """Gets the name of this ListTopicsRequest.

        topic名称

        :return: The name of this ListTopicsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTopicsRequest.

        topic名称

        :param name: The name of this ListTopicsRequest.
        :type name: str
        """
        self._name = name

    @property
    def topic_permission(self):
        """Gets the topic_permission of this ListTopicsRequest.

        topic权限，0为发布，1为订阅

        :return: The topic_permission of this ListTopicsRequest.
        :rtype: int
        """
        return self._topic_permission

    @topic_permission.setter
    def topic_permission(self, topic_permission):
        """Sets the topic_permission of this ListTopicsRequest.

        topic权限，0为发布，1为订阅

        :param topic_permission: The topic_permission of this ListTopicsRequest.
        :type topic_permission: int
        """
        self._topic_permission = topic_permission

    @property
    def topic_type(self):
        """Gets the topic_type of this ListTopicsRequest.

        topic类型，0为设备类topic，1为产品类topic

        :return: The topic_type of this ListTopicsRequest.
        :rtype: int
        """
        return self._topic_type

    @topic_type.setter
    def topic_type(self, topic_type):
        """Sets the topic_type of this ListTopicsRequest.

        topic类型，0为设备类topic，1为产品类topic

        :param topic_type: The topic_type of this ListTopicsRequest.
        :type topic_type: int
        """
        self._topic_type = topic_type

    @property
    def is_private(self):
        """Gets the is_private of this ListTopicsRequest.

        topic是否为自定义，0为基础topic，1为自定义topic

        :return: The is_private of this ListTopicsRequest.
        :rtype: int
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this ListTopicsRequest.

        topic是否为自定义，0为基础topic，1为自定义topic

        :param is_private: The is_private of this ListTopicsRequest.
        :type is_private: int
        """
        self._is_private = is_private

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
        if not isinstance(other, ListTopicsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
