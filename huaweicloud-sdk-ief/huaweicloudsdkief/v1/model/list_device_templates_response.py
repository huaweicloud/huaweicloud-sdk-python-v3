# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeviceTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_templates': 'list[EdgemgrDevice]',
        'count': 'int'
    }

    attribute_map = {
        'device_templates': 'device_templates',
        'count': 'count'
    }

    def __init__(self, device_templates=None, count=None):
        """ListDeviceTemplatesResponse

        The model defined in huaweicloud sdk

        :param device_templates: 终端设备属性
        :type device_templates: list[:class:`huaweicloudsdkief.v1.EdgemgrDevice`]
        :param count: 模板数量
        :type count: int
        """
        
        super(ListDeviceTemplatesResponse, self).__init__()

        self._device_templates = None
        self._count = None
        self.discriminator = None

        if device_templates is not None:
            self.device_templates = device_templates
        if count is not None:
            self.count = count

    @property
    def device_templates(self):
        """Gets the device_templates of this ListDeviceTemplatesResponse.

        终端设备属性

        :return: The device_templates of this ListDeviceTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.EdgemgrDevice`]
        """
        return self._device_templates

    @device_templates.setter
    def device_templates(self, device_templates):
        """Sets the device_templates of this ListDeviceTemplatesResponse.

        终端设备属性

        :param device_templates: The device_templates of this ListDeviceTemplatesResponse.
        :type device_templates: list[:class:`huaweicloudsdkief.v1.EdgemgrDevice`]
        """
        self._device_templates = device_templates

    @property
    def count(self):
        """Gets the count of this ListDeviceTemplatesResponse.

        模板数量

        :return: The count of this ListDeviceTemplatesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDeviceTemplatesResponse.

        模板数量

        :param count: The count of this ListDeviceTemplatesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListDeviceTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
