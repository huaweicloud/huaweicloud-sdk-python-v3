# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDeviceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_name': 'str',
        'status': 'int',
        'description': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'device_name': 'device_name',
        'status': 'status',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, device_name=None, status=None, description=None, tags=None):
        """UpdateDeviceRequestBody

        The model defined in huaweicloud sdk

        :param device_name: 设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?&#39;-@%&amp;!, 长度2-64
        :type device_name: str
        :param status: 设备状态 0启用 1禁用
        :type status: int
        :param description: 备注
        :type description: str
        :param tags: 标签
        :type tags: list[str]
        """
        
        

        self._device_name = None
        self._status = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.device_name = device_name
        self.status = status
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def device_name(self):
        """Gets the device_name of this UpdateDeviceRequestBody.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :return: The device_name of this UpdateDeviceRequestBody.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this UpdateDeviceRequestBody.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :param device_name: The device_name of this UpdateDeviceRequestBody.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def status(self):
        """Gets the status of this UpdateDeviceRequestBody.

        设备状态 0启用 1禁用

        :return: The status of this UpdateDeviceRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateDeviceRequestBody.

        设备状态 0启用 1禁用

        :param status: The status of this UpdateDeviceRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this UpdateDeviceRequestBody.

        备注

        :return: The description of this UpdateDeviceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDeviceRequestBody.

        备注

        :param description: The description of this UpdateDeviceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UpdateDeviceRequestBody.

        标签

        :return: The tags of this UpdateDeviceRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateDeviceRequestBody.

        标签

        :param tags: The tags of this UpdateDeviceRequestBody.
        :type tags: list[str]
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
        if not isinstance(other, UpdateDeviceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
