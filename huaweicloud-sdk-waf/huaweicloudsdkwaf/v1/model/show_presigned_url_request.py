# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPresignedUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_name': 'str'
    }

    attribute_map = {
        'operation_name': 'operation_name'
    }

    def __init__(self, operation_name=None):
        r"""ShowPresignedUrlRequest

        The model defined in huaweicloud sdk

        :param operation_name: **参数解释：** 操作名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type operation_name: str
        """
        
        

        self._operation_name = None
        self.discriminator = None

        self.operation_name = operation_name

    @property
    def operation_name(self):
        r"""Gets the operation_name of this ShowPresignedUrlRequest.

        **参数解释：** 操作名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The operation_name of this ShowPresignedUrlRequest.
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        r"""Sets the operation_name of this ShowPresignedUrlRequest.

        **参数解释：** 操作名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param operation_name: The operation_name of this ShowPresignedUrlRequest.
        :type operation_name: str
        """
        self._operation_name = operation_name

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
        if not isinstance(other, ShowPresignedUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
