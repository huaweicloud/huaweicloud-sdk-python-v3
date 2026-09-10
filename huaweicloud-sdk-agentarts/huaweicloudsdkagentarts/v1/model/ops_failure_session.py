# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFailureSession:

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
        'explanation': 'str',
        'failure_spans': 'list[OpsFailureSpan]'
    }

    attribute_map = {
        'session_id': 'session_id',
        'explanation': 'explanation',
        'failure_spans': 'failure_spans'
    }

    def __init__(self, session_id=None, explanation=None, failure_spans=None):
        r"""OpsFailureSession

        The model defined in huaweicloud sdk

        :param session_id: **参数解释：** 故障的session ID。  **取值范围：** 长度1-64个字符。
        :type session_id: str
        :param explanation: **参数解释：** session故障的描述信息。  **取值范围：** 长度1-1024个字符。
        :type explanation: str
        :param failure_spans: **参数解释：** 故障的span列表。  **取值范围：** 长度0-100的数组。
        :type failure_spans: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSpan`]
        """
        
        

        self._session_id = None
        self._explanation = None
        self._failure_spans = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if explanation is not None:
            self.explanation = explanation
        if failure_spans is not None:
            self.failure_spans = failure_spans

    @property
    def session_id(self):
        r"""Gets the session_id of this OpsFailureSession.

        **参数解释：** 故障的session ID。  **取值范围：** 长度1-64个字符。

        :return: The session_id of this OpsFailureSession.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this OpsFailureSession.

        **参数解释：** 故障的session ID。  **取值范围：** 长度1-64个字符。

        :param session_id: The session_id of this OpsFailureSession.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def explanation(self):
        r"""Gets the explanation of this OpsFailureSession.

        **参数解释：** session故障的描述信息。  **取值范围：** 长度1-1024个字符。

        :return: The explanation of this OpsFailureSession.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        r"""Sets the explanation of this OpsFailureSession.

        **参数解释：** session故障的描述信息。  **取值范围：** 长度1-1024个字符。

        :param explanation: The explanation of this OpsFailureSession.
        :type explanation: str
        """
        self._explanation = explanation

    @property
    def failure_spans(self):
        r"""Gets the failure_spans of this OpsFailureSession.

        **参数解释：** 故障的span列表。  **取值范围：** 长度0-100的数组。

        :return: The failure_spans of this OpsFailureSession.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSpan`]
        """
        return self._failure_spans

    @failure_spans.setter
    def failure_spans(self, failure_spans):
        r"""Sets the failure_spans of this OpsFailureSession.

        **参数解释：** 故障的span列表。  **取值范围：** 长度0-100的数组。

        :param failure_spans: The failure_spans of this OpsFailureSession.
        :type failure_spans: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSpan`]
        """
        self._failure_spans = failure_spans

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
        if not isinstance(other, OpsFailureSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
