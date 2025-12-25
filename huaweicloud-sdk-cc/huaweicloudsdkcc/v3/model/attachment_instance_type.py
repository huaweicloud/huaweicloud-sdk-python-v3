# coding: utf-8

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
        'attachment_instance_type': 'str'
    }

    attribute_map = {
        'attachment_instance_type': 'attachment_instance_type'
    }

    def __init__(self, attachment_instance_type=None):
        r"""AttachmentInstanceType

        The model defined in huaweicloud sdk

        :param attachment_instance_type: 接入网络实例类型，GDGW (专线)和ER_ROUTE_TABLE (路由表)。
        :type attachment_instance_type: str
        """
        
        

        self._attachment_instance_type = None
        self.discriminator = None

        self.attachment_instance_type = attachment_instance_type

    @property
    def attachment_instance_type(self):
        r"""Gets the attachment_instance_type of this AttachmentInstanceType.

        接入网络实例类型，GDGW (专线)和ER_ROUTE_TABLE (路由表)。

        :return: The attachment_instance_type of this AttachmentInstanceType.
        :rtype: str
        """
        return self._attachment_instance_type

    @attachment_instance_type.setter
    def attachment_instance_type(self, attachment_instance_type):
        r"""Sets the attachment_instance_type of this AttachmentInstanceType.

        接入网络实例类型，GDGW (专线)和ER_ROUTE_TABLE (路由表)。

        :param attachment_instance_type: The attachment_instance_type of this AttachmentInstanceType.
        :type attachment_instance_type: str
        """
        self._attachment_instance_type = attachment_instance_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
