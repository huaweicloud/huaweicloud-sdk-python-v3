# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_tpm': 'bool'
    }

    attribute_map = {
        'enable_tpm': 'enable_tpm'
    }

    def __init__(self, enable_tpm=None):
        r"""RuntimeInfoDTO

        The model defined in huaweicloud sdk

        :param enable_tpm: 是否启用TPM
        :type enable_tpm: bool
        """
        
        

        self._enable_tpm = None
        self.discriminator = None

        if enable_tpm is not None:
            self.enable_tpm = enable_tpm

    @property
    def enable_tpm(self):
        r"""Gets the enable_tpm of this RuntimeInfoDTO.

        是否启用TPM

        :return: The enable_tpm of this RuntimeInfoDTO.
        :rtype: bool
        """
        return self._enable_tpm

    @enable_tpm.setter
    def enable_tpm(self, enable_tpm):
        r"""Sets the enable_tpm of this RuntimeInfoDTO.

        是否启用TPM

        :param enable_tpm: The enable_tpm of this RuntimeInfoDTO.
        :type enable_tpm: bool
        """
        self._enable_tpm = enable_tpm

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
        if not isinstance(other, RuntimeInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
