# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNicInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interface_attachment': 'InterfaceAttachment'
    }

    attribute_map = {
        'interface_attachment': 'interface_attachment'
    }

    def __init__(self, interface_attachment=None):
        r"""UpdateNicInfoRequestBody

        The model defined in huaweicloud sdk

        :param interface_attachment: 
        :type interface_attachment: :class:`huaweicloudsdkecs.v2.InterfaceAttachment`
        """
        
        

        self._interface_attachment = None
        self.discriminator = None

        self.interface_attachment = interface_attachment

    @property
    def interface_attachment(self):
        r"""Gets the interface_attachment of this UpdateNicInfoRequestBody.

        :return: The interface_attachment of this UpdateNicInfoRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.InterfaceAttachment`
        """
        return self._interface_attachment

    @interface_attachment.setter
    def interface_attachment(self, interface_attachment):
        r"""Sets the interface_attachment of this UpdateNicInfoRequestBody.

        :param interface_attachment: The interface_attachment of this UpdateNicInfoRequestBody.
        :type interface_attachment: :class:`huaweicloudsdkecs.v2.InterfaceAttachment`
        """
        self._interface_attachment = interface_attachment

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
        if not isinstance(other, UpdateNicInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
