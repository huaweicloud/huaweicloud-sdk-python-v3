# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirmwaresRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_type': 'str',
        'arch': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'device_type': 'device_type',
        'arch': 'arch',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, device_type=None, arch=None, os_name=None, os_version=None, offset=None, limit=None):
        """ListFirmwaresRequest

        The model defined in huaweicloud sdk

        :param device_type: 固件适用设备类型
        :type device_type: str
        :param arch: 边缘节点架构
        :type arch: str
        :param os_name: 边缘设备操作系统名称
        :type os_name: str
        :param os_version: 边缘设备操作系统版本
        :type os_version: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页显示的条目数量，取值范围1~100，默认为100
        :type limit: int
        """
        
        

        self._device_type = None
        self._arch = None
        self._os_name = None
        self._os_version = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.device_type = device_type
        if arch is not None:
            self.arch = arch
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def device_type(self):
        """Gets the device_type of this ListFirmwaresRequest.

        固件适用设备类型

        :return: The device_type of this ListFirmwaresRequest.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ListFirmwaresRequest.

        固件适用设备类型

        :param device_type: The device_type of this ListFirmwaresRequest.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def arch(self):
        """Gets the arch of this ListFirmwaresRequest.

        边缘节点架构

        :return: The arch of this ListFirmwaresRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ListFirmwaresRequest.

        边缘节点架构

        :param arch: The arch of this ListFirmwaresRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def os_name(self):
        """Gets the os_name of this ListFirmwaresRequest.

        边缘设备操作系统名称

        :return: The os_name of this ListFirmwaresRequest.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this ListFirmwaresRequest.

        边缘设备操作系统名称

        :param os_name: The os_name of this ListFirmwaresRequest.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        """Gets the os_version of this ListFirmwaresRequest.

        边缘设备操作系统版本

        :return: The os_version of this ListFirmwaresRequest.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ListFirmwaresRequest.

        边缘设备操作系统版本

        :param os_version: The os_version of this ListFirmwaresRequest.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def offset(self):
        """Gets the offset of this ListFirmwaresRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListFirmwaresRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFirmwaresRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListFirmwaresRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFirmwaresRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :return: The limit of this ListFirmwaresRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFirmwaresRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :param limit: The limit of this ListFirmwaresRequest.
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
        if not isinstance(other, ListFirmwaresRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
