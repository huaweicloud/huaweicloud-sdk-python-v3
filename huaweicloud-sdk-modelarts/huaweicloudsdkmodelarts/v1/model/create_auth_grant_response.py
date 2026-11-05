# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuthGrantResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'status': 'bool'
    }

    attribute_map = {
        'service_name': 'service_name',
        'status': 'status'
    }

    def __init__(self, service_name=None, status=None):
        r"""CreateAuthGrantResponse

        The model defined in huaweicloud sdk

        :param service_name: **参数解释**：服务名称。 **取值范围**：不涉及。
        :type service_name: str
        :param status: **参数解释**：授权状态，true表示已授权，false表示未授权。 **取值范围**： - true：已授权。 - false：未授权。
        :type status: bool
        """
        
        super().__init__()

        self._service_name = None
        self._status = None
        self.discriminator = None

        if service_name is not None:
            self.service_name = service_name
        if status is not None:
            self.status = status

    @property
    def service_name(self):
        r"""Gets the service_name of this CreateAuthGrantResponse.

        **参数解释**：服务名称。 **取值范围**：不涉及。

        :return: The service_name of this CreateAuthGrantResponse.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this CreateAuthGrantResponse.

        **参数解释**：服务名称。 **取值范围**：不涉及。

        :param service_name: The service_name of this CreateAuthGrantResponse.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def status(self):
        r"""Gets the status of this CreateAuthGrantResponse.

        **参数解释**：授权状态，true表示已授权，false表示未授权。 **取值范围**： - true：已授权。 - false：未授权。

        :return: The status of this CreateAuthGrantResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAuthGrantResponse.

        **参数解释**：授权状态，true表示已授权，false表示未授权。 **取值范围**： - true：已授权。 - false：未授权。

        :param status: The status of this CreateAuthGrantResponse.
        :type status: bool
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("CreateAuthGrantResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateAuthGrantResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
