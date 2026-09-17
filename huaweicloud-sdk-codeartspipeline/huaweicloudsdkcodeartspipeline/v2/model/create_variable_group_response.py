# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVariableGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_variable_group_id': 'str'
    }

    attribute_map = {
        'pipeline_variable_group_id': 'pipeline_variable_group_id'
    }

    def __init__(self, pipeline_variable_group_id=None):
        r"""CreateVariableGroupResponse

        The model defined in huaweicloud sdk

        :param pipeline_variable_group_id: **参数解释**： 参数组ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type pipeline_variable_group_id: str
        """
        
        super().__init__()

        self._pipeline_variable_group_id = None
        self.discriminator = None

        if pipeline_variable_group_id is not None:
            self.pipeline_variable_group_id = pipeline_variable_group_id

    @property
    def pipeline_variable_group_id(self):
        r"""Gets the pipeline_variable_group_id of this CreateVariableGroupResponse.

        **参数解释**： 参数组ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The pipeline_variable_group_id of this CreateVariableGroupResponse.
        :rtype: str
        """
        return self._pipeline_variable_group_id

    @pipeline_variable_group_id.setter
    def pipeline_variable_group_id(self, pipeline_variable_group_id):
        r"""Sets the pipeline_variable_group_id of this CreateVariableGroupResponse.

        **参数解释**： 参数组ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param pipeline_variable_group_id: The pipeline_variable_group_id of this CreateVariableGroupResponse.
        :type pipeline_variable_group_id: str
        """
        self._pipeline_variable_group_id = pipeline_variable_group_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateVariableGroupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateVariableGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
