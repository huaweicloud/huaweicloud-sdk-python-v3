# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClusterGroupDescriptionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str'
    }

    attribute_map = {
        'description': 'description'
    }

    def __init__(self, description=None):
        r"""UpdateClusterGroupDescriptionRequest

        The model defined in huaweicloud sdk

        :param description: 容器舰队描述信息
        :type description: str
        """
        
        

        self._description = None
        self.discriminator = None

        self.description = description

    @property
    def description(self):
        r"""Gets the description of this UpdateClusterGroupDescriptionRequest.

        容器舰队描述信息

        :return: The description of this UpdateClusterGroupDescriptionRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateClusterGroupDescriptionRequest.

        容器舰队描述信息

        :param description: The description of this UpdateClusterGroupDescriptionRequest.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateClusterGroupDescriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
