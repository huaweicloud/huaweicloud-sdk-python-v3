# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlatformManagerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'device_type': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'device_type': 'device_type',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, id=None, device_type=None, type=None, offset=None, limit=None):
        """ListPlatformManagerRequest

        The model defined in huaweicloud sdk

        :param id: 订单Id，可以根据订单Id查询
        :type id: str
        :param device_type: 设备类别：lite_device轻量型设备，small_device小型设备，large_device大型设备，large_device_cpu CPU大型设备， large_device_gpu_npu CPU,NPU大型设备
        :type device_type: str
        :param type: 运行服务费类别，专业版为running_service，标准版为development_service
        :type type: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页显示的条目数量，取值范围1~100，默认为100
        :type limit: int
        """
        
        

        self._id = None
        self._device_type = None
        self._type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if device_type is not None:
            self.device_type = device_type
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        """Gets the id of this ListPlatformManagerRequest.

        订单Id，可以根据订单Id查询

        :return: The id of this ListPlatformManagerRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPlatformManagerRequest.

        订单Id，可以根据订单Id查询

        :param id: The id of this ListPlatformManagerRequest.
        :type id: str
        """
        self._id = id

    @property
    def device_type(self):
        """Gets the device_type of this ListPlatformManagerRequest.

        设备类别：lite_device轻量型设备，small_device小型设备，large_device大型设备，large_device_cpu CPU大型设备， large_device_gpu_npu CPU,NPU大型设备

        :return: The device_type of this ListPlatformManagerRequest.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ListPlatformManagerRequest.

        设备类别：lite_device轻量型设备，small_device小型设备，large_device大型设备，large_device_cpu CPU大型设备， large_device_gpu_npu CPU,NPU大型设备

        :param device_type: The device_type of this ListPlatformManagerRequest.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def type(self):
        """Gets the type of this ListPlatformManagerRequest.

        运行服务费类别，专业版为running_service，标准版为development_service

        :return: The type of this ListPlatformManagerRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPlatformManagerRequest.

        运行服务费类别，专业版为running_service，标准版为development_service

        :param type: The type of this ListPlatformManagerRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        """Gets the offset of this ListPlatformManagerRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListPlatformManagerRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPlatformManagerRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListPlatformManagerRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPlatformManagerRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :return: The limit of this ListPlatformManagerRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPlatformManagerRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :param limit: The limit of this ListPlatformManagerRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPlatformManagerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
