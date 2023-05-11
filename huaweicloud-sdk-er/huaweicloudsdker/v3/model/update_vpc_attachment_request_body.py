# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpcAttachmentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_attachment': 'UpdateVpcAttachmentBody'
    }

    attribute_map = {
        'vpc_attachment': 'vpc_attachment'
    }

    def __init__(self, vpc_attachment=None):
        """UpdateVpcAttachmentRequestBody

        The model defined in huaweicloud sdk

        :param vpc_attachment: 
        :type vpc_attachment: :class:`huaweicloudsdker.v3.UpdateVpcAttachmentBody`
        """
        
        

        self._vpc_attachment = None
        self.discriminator = None

        if vpc_attachment is not None:
            self.vpc_attachment = vpc_attachment

    @property
    def vpc_attachment(self):
        """Gets the vpc_attachment of this UpdateVpcAttachmentRequestBody.

        :return: The vpc_attachment of this UpdateVpcAttachmentRequestBody.
        :rtype: :class:`huaweicloudsdker.v3.UpdateVpcAttachmentBody`
        """
        return self._vpc_attachment

    @vpc_attachment.setter
    def vpc_attachment(self, vpc_attachment):
        """Sets the vpc_attachment of this UpdateVpcAttachmentRequestBody.

        :param vpc_attachment: The vpc_attachment of this UpdateVpcAttachmentRequestBody.
        :type vpc_attachment: :class:`huaweicloudsdker.v3.UpdateVpcAttachmentBody`
        """
        self._vpc_attachment = vpc_attachment

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
        if not isinstance(other, UpdateVpcAttachmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
