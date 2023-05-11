# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDevicesInGroupRequest:

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
        'group_id': 'int',
        'limit': 'int',
        'product_name': 'str',
        'device_name': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'limit': 'limit',
        'product_name': 'product_name',
        'device_name': 'device_name',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, group_id=None, limit=None, product_name=None, device_name=None, offset=None):
        """ShowDevicesInGroupRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param group_id: 设备分组ID
        :type group_id: int
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param product_name: 产品名称
        :type product_name: str
        :param device_name: 设备名称
        :type device_name: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        """
        
        

        self._instance_id = None
        self._group_id = None
        self._limit = None
        self._product_name = None
        self._device_name = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group_id = group_id
        if limit is not None:
            self.limit = limit
        if product_name is not None:
            self.product_name = product_name
        if device_name is not None:
            self.device_name = device_name
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowDevicesInGroupRequest.

        实例ID

        :return: The instance_id of this ShowDevicesInGroupRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowDevicesInGroupRequest.

        实例ID

        :param instance_id: The instance_id of this ShowDevicesInGroupRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        """Gets the group_id of this ShowDevicesInGroupRequest.

        设备分组ID

        :return: The group_id of this ShowDevicesInGroupRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowDevicesInGroupRequest.

        设备分组ID

        :param group_id: The group_id of this ShowDevicesInGroupRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def limit(self):
        """Gets the limit of this ShowDevicesInGroupRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ShowDevicesInGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowDevicesInGroupRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ShowDevicesInGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def product_name(self):
        """Gets the product_name of this ShowDevicesInGroupRequest.

        产品名称

        :return: The product_name of this ShowDevicesInGroupRequest.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ShowDevicesInGroupRequest.

        产品名称

        :param product_name: The product_name of this ShowDevicesInGroupRequest.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def device_name(self):
        """Gets the device_name of this ShowDevicesInGroupRequest.

        设备名称

        :return: The device_name of this ShowDevicesInGroupRequest.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ShowDevicesInGroupRequest.

        设备名称

        :param device_name: The device_name of this ShowDevicesInGroupRequest.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def offset(self):
        """Gets the offset of this ShowDevicesInGroupRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ShowDevicesInGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowDevicesInGroupRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ShowDevicesInGroupRequest.
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
        if not isinstance(other, ShowDevicesInGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
