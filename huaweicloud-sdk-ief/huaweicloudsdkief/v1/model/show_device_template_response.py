# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeviceTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_template': 'EdgemgrDevice'
    }

    attribute_map = {
        'device_template': 'device_template'
    }

    def __init__(self, device_template=None):
        """ShowDeviceTemplateResponse

        The model defined in huaweicloud sdk

        :param device_template: 
        :type device_template: :class:`huaweicloudsdkief.v1.EdgemgrDevice`
        """
        
        super(ShowDeviceTemplateResponse, self).__init__()

        self._device_template = None
        self.discriminator = None

        if device_template is not None:
            self.device_template = device_template

    @property
    def device_template(self):
        """Gets the device_template of this ShowDeviceTemplateResponse.

        :return: The device_template of this ShowDeviceTemplateResponse.
        :rtype: :class:`huaweicloudsdkief.v1.EdgemgrDevice`
        """
        return self._device_template

    @device_template.setter
    def device_template(self, device_template):
        """Sets the device_template of this ShowDeviceTemplateResponse.

        :param device_template: The device_template of this ShowDeviceTemplateResponse.
        :type device_template: :class:`huaweicloudsdkief.v1.EdgemgrDevice`
        """
        self._device_template = device_template

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
        if not isinstance(other, ShowDeviceTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
