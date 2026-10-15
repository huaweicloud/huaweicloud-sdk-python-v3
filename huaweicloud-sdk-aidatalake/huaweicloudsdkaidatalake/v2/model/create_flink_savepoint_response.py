# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkSavepointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'savepoint_id': 'str'
    }

    attribute_map = {
        'savepoint_id': 'savepoint_id'
    }

    def __init__(self, savepoint_id=None):
        r"""CreateFlinkSavepointResponse

        The model defined in huaweicloud sdk

        :param savepoint_id: **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type savepoint_id: str
        """
        
        super().__init__()

        self._savepoint_id = None
        self.discriminator = None

        if savepoint_id is not None:
            self.savepoint_id = savepoint_id

    @property
    def savepoint_id(self):
        r"""Gets the savepoint_id of this CreateFlinkSavepointResponse.

        **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The savepoint_id of this CreateFlinkSavepointResponse.
        :rtype: str
        """
        return self._savepoint_id

    @savepoint_id.setter
    def savepoint_id(self, savepoint_id):
        r"""Sets the savepoint_id of this CreateFlinkSavepointResponse.

        **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param savepoint_id: The savepoint_id of this CreateFlinkSavepointResponse.
        :type savepoint_id: str
        """
        self._savepoint_id = savepoint_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateFlinkSavepointResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateFlinkSavepointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
