# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuraSqlSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'status': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'status': 'status',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, session_id=None, status=None, x_request_id=None):
        r"""CreateAuraSqlSessionResponse

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：Session的ID。 **取值范围**：长度为1~32个字符，支持大小写英文字母、数字、连字符。
        :type session_id: str
        :param status: **参数解释**：session的状态。 **取值范围**：   - RUNNING：运行中。   - CLOSED：已关闭。   - WAITING：等待中。   - CREATING：创建中。   - FAIL：失败。
        :type status: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._session_id = None
        self._status = None
        self._x_request_id = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if status is not None:
            self.status = status
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def session_id(self):
        r"""Gets the session_id of this CreateAuraSqlSessionResponse.

        **参数解释**：Session的ID。 **取值范围**：长度为1~32个字符，支持大小写英文字母、数字、连字符。

        :return: The session_id of this CreateAuraSqlSessionResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this CreateAuraSqlSessionResponse.

        **参数解释**：Session的ID。 **取值范围**：长度为1~32个字符，支持大小写英文字母、数字、连字符。

        :param session_id: The session_id of this CreateAuraSqlSessionResponse.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def status(self):
        r"""Gets the status of this CreateAuraSqlSessionResponse.

        **参数解释**：session的状态。 **取值范围**：   - RUNNING：运行中。   - CLOSED：已关闭。   - WAITING：等待中。   - CREATING：创建中。   - FAIL：失败。

        :return: The status of this CreateAuraSqlSessionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAuraSqlSessionResponse.

        **参数解释**：session的状态。 **取值范围**：   - RUNNING：运行中。   - CLOSED：已关闭。   - WAITING：等待中。   - CREATING：创建中。   - FAIL：失败。

        :param status: The status of this CreateAuraSqlSessionResponse.
        :type status: str
        """
        self._status = status

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateAuraSqlSessionResponse.

        :return: The x_request_id of this CreateAuraSqlSessionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateAuraSqlSessionResponse.

        :param x_request_id: The x_request_id of this CreateAuraSqlSessionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateAuraSqlSessionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateAuraSqlSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
