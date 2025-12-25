# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSearchConditionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_id': 'str'
    }

    attribute_map = {
        'condition_id': 'condition_id'
    }

    def __init__(self, condition_id=None):
        r"""CreateSearchConditionResponse

        The model defined in huaweicloud sdk

        :param condition_id: 检索条件ID
        :type condition_id: str
        """
        
        super().__init__()

        self._condition_id = None
        self.discriminator = None

        if condition_id is not None:
            self.condition_id = condition_id

    @property
    def condition_id(self):
        r"""Gets the condition_id of this CreateSearchConditionResponse.

        检索条件ID

        :return: The condition_id of this CreateSearchConditionResponse.
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        r"""Sets the condition_id of this CreateSearchConditionResponse.

        检索条件ID

        :param condition_id: The condition_id of this CreateSearchConditionResponse.
        :type condition_id: str
        """
        self._condition_id = condition_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateSearchConditionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateSearchConditionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
