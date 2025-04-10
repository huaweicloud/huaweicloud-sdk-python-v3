# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentInstanceType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachment_instance_type': 'AttachmentInstanceTypeEnum'
    }

    attribute_map = {
        'attachment_instance_type': 'attachment_instance_type'
    }

    def __init__(self, attachment_instance_type=None):
        r"""AttachmentInstanceType

        The model defined in huaweicloud sdk

        :param attachment_instance_type: 
        :type attachment_instance_type: :class:`huaweicloudsdkcc.v3.AttachmentInstanceTypeEnum`
        """
        
        

        self._attachment_instance_type = None
        self.discriminator = None

        self.attachment_instance_type = attachment_instance_type

    @property
    def attachment_instance_type(self):
        r"""Gets the attachment_instance_type of this AttachmentInstanceType.

        :return: The attachment_instance_type of this AttachmentInstanceType.
        :rtype: :class:`huaweicloudsdkcc.v3.AttachmentInstanceTypeEnum`
        """
        return self._attachment_instance_type

    @attachment_instance_type.setter
    def attachment_instance_type(self, attachment_instance_type):
        r"""Sets the attachment_instance_type of this AttachmentInstanceType.

        :param attachment_instance_type: The attachment_instance_type of this AttachmentInstanceType.
        :type attachment_instance_type: :class:`huaweicloudsdkcc.v3.AttachmentInstanceTypeEnum`
        """
        self._attachment_instance_type = attachment_instance_type

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
        if not isinstance(other, AttachmentInstanceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
