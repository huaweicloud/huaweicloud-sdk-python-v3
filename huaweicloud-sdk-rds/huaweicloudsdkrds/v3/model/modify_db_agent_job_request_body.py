# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyDbAgentJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'profile_id': 'str'
    }

    attribute_map = {
        'profile_id': 'profile_id'
    }

    def __init__(self, profile_id=None):
        r"""ModifyDbAgentJobRequestBody

        The model defined in huaweicloud sdk

        :param profile_id: 配置文件id。
        :type profile_id: str
        """
        
        

        self._profile_id = None
        self.discriminator = None

        self.profile_id = profile_id

    @property
    def profile_id(self):
        r"""Gets the profile_id of this ModifyDbAgentJobRequestBody.

        配置文件id。

        :return: The profile_id of this ModifyDbAgentJobRequestBody.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        r"""Sets the profile_id of this ModifyDbAgentJobRequestBody.

        配置文件id。

        :param profile_id: The profile_id of this ModifyDbAgentJobRequestBody.
        :type profile_id: str
        """
        self._profile_id = profile_id

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
        if not isinstance(other, ModifyDbAgentJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
