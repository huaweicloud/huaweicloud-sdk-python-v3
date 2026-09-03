# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlSessionInfo:

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
        'status': 'SqlSessionStatus',
        'create_time': 'datetime',
        'endpoint_info': 'object'
    }

    attribute_map = {
        'session_id': 'session_id',
        'status': 'status',
        'create_time': 'create_time',
        'endpoint_info': 'endpoint_info'
    }

    def __init__(self, session_id=None, status=None, create_time=None, endpoint_info=None):
        r"""SqlSessionInfo

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type session_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.SqlSessionStatus`
        :param create_time: **参数解释**：session创建时间。 **取值范围**：不涉及。
        :type create_time: datetime
        :param endpoint_info: **参数解释**：端点信息。
        :type endpoint_info: :class:`huaweicloudsdkaidatalake.v2.object`
        """
        
        

        self._session_id = None
        self._status = None
        self._create_time = None
        self._endpoint_info = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if endpoint_info is not None:
            self.endpoint_info = endpoint_info

    @property
    def session_id(self):
        r"""Gets the session_id of this SqlSessionInfo.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The session_id of this SqlSessionInfo.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this SqlSessionInfo.

        **参数解释**：Session的ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param session_id: The session_id of this SqlSessionInfo.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def status(self):
        r"""Gets the status of this SqlSessionInfo.

        :return: The status of this SqlSessionInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SqlSessionStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlSessionInfo.

        :param status: The status of this SqlSessionInfo.
        :type status: :class:`huaweicloudsdkaidatalake.v2.SqlSessionStatus`
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this SqlSessionInfo.

        **参数解释**：session创建时间。 **取值范围**：不涉及。

        :return: The create_time of this SqlSessionInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SqlSessionInfo.

        **参数解释**：session创建时间。 **取值范围**：不涉及。

        :param create_time: The create_time of this SqlSessionInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def endpoint_info(self):
        r"""Gets the endpoint_info of this SqlSessionInfo.

        **参数解释**：端点信息。

        :return: The endpoint_info of this SqlSessionInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.object`
        """
        return self._endpoint_info

    @endpoint_info.setter
    def endpoint_info(self, endpoint_info):
        r"""Sets the endpoint_info of this SqlSessionInfo.

        **参数解释**：端点信息。

        :param endpoint_info: The endpoint_info of this SqlSessionInfo.
        :type endpoint_info: :class:`huaweicloudsdkaidatalake.v2.object`
        """
        self._endpoint_info = endpoint_info

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
        if not isinstance(other, SqlSessionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
