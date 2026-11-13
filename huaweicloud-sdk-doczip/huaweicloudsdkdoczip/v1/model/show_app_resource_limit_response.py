# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppResourceLimitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allowed_resource_number': 'int',
        'x_trace_id': 'str'
    }

    attribute_map = {
        'allowed_resource_number': 'allowed_resource_number',
        'x_trace_id': 'X-Trace-Id'
    }

    def __init__(self, allowed_resource_number=None, x_trace_id=None):
        r"""ShowAppResourceLimitResponse

        The model defined in huaweicloud sdk

        :param allowed_resource_number: **参数解释**： 允许创建的应用数量。 **取值范围**： - 0：不支持创建。 - 大于0：允许创建的应用数量。
        :type allowed_resource_number: int
        :param x_trace_id: 
        :type x_trace_id: str
        """
        
        super().__init__()

        self._allowed_resource_number = None
        self._x_trace_id = None
        self.discriminator = None

        if allowed_resource_number is not None:
            self.allowed_resource_number = allowed_resource_number
        if x_trace_id is not None:
            self.x_trace_id = x_trace_id

    @property
    def allowed_resource_number(self):
        r"""Gets the allowed_resource_number of this ShowAppResourceLimitResponse.

        **参数解释**： 允许创建的应用数量。 **取值范围**： - 0：不支持创建。 - 大于0：允许创建的应用数量。

        :return: The allowed_resource_number of this ShowAppResourceLimitResponse.
        :rtype: int
        """
        return self._allowed_resource_number

    @allowed_resource_number.setter
    def allowed_resource_number(self, allowed_resource_number):
        r"""Sets the allowed_resource_number of this ShowAppResourceLimitResponse.

        **参数解释**： 允许创建的应用数量。 **取值范围**： - 0：不支持创建。 - 大于0：允许创建的应用数量。

        :param allowed_resource_number: The allowed_resource_number of this ShowAppResourceLimitResponse.
        :type allowed_resource_number: int
        """
        self._allowed_resource_number = allowed_resource_number

    @property
    def x_trace_id(self):
        r"""Gets the x_trace_id of this ShowAppResourceLimitResponse.

        :return: The x_trace_id of this ShowAppResourceLimitResponse.
        :rtype: str
        """
        return self._x_trace_id

    @x_trace_id.setter
    def x_trace_id(self, x_trace_id):
        r"""Sets the x_trace_id of this ShowAppResourceLimitResponse.

        :param x_trace_id: The x_trace_id of this ShowAppResourceLimitResponse.
        :type x_trace_id: str
        """
        self._x_trace_id = x_trace_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowAppResourceLimitResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAppResourceLimitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
