# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSensitiveOperationSwitchRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_open': 'bool'
    }

    attribute_map = {
        'is_open': 'is_open'
    }

    def __init__(self, is_open=None):
        r"""UpdateSensitiveOperationSwitchRequestBody

        The model defined in huaweicloud sdk

        :param is_open: 是否开启
        :type is_open: bool
        """
        
        

        self._is_open = None
        self.discriminator = None

        self.is_open = is_open

    @property
    def is_open(self):
        r"""Gets the is_open of this UpdateSensitiveOperationSwitchRequestBody.

        是否开启

        :return: The is_open of this UpdateSensitiveOperationSwitchRequestBody.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        r"""Sets the is_open of this UpdateSensitiveOperationSwitchRequestBody.

        是否开启

        :param is_open: The is_open of this UpdateSensitiveOperationSwitchRequestBody.
        :type is_open: bool
        """
        self._is_open = is_open

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
        if not isinstance(other, UpdateSensitiveOperationSwitchRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
