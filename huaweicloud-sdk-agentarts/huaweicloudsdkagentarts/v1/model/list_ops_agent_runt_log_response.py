# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAgentRuntLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'is_query_complete': 'bool',
        'logs': 'list[AgentLogContent]',
        'scroll_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'is_query_complete': 'is_query_complete',
        'logs': 'logs',
        'scroll_id': 'scroll_id'
    }

    def __init__(self, count=None, is_query_complete=None, logs=None, scroll_id=None):
        r"""ListOpsAgentRuntLogResponse

        The model defined in huaweicloud sdk

        :param count: 日志数
        :type count: int
        :param is_query_complete: 是否查询完成
        :type is_query_complete: bool
        :param logs: 日志内容
        :type logs: list[:class:`huaweicloudsdkagentarts.v1.AgentLogContent`]
        :param scroll_id: 
        :type scroll_id: str
        """
        
        super().__init__()

        self._count = None
        self._is_query_complete = None
        self._logs = None
        self._scroll_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if is_query_complete is not None:
            self.is_query_complete = is_query_complete
        if logs is not None:
            self.logs = logs
        if scroll_id is not None:
            self.scroll_id = scroll_id

    @property
    def count(self):
        r"""Gets the count of this ListOpsAgentRuntLogResponse.

        日志数

        :return: The count of this ListOpsAgentRuntLogResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListOpsAgentRuntLogResponse.

        日志数

        :param count: The count of this ListOpsAgentRuntLogResponse.
        :type count: int
        """
        self._count = count

    @property
    def is_query_complete(self):
        r"""Gets the is_query_complete of this ListOpsAgentRuntLogResponse.

        是否查询完成

        :return: The is_query_complete of this ListOpsAgentRuntLogResponse.
        :rtype: bool
        """
        return self._is_query_complete

    @is_query_complete.setter
    def is_query_complete(self, is_query_complete):
        r"""Sets the is_query_complete of this ListOpsAgentRuntLogResponse.

        是否查询完成

        :param is_query_complete: The is_query_complete of this ListOpsAgentRuntLogResponse.
        :type is_query_complete: bool
        """
        self._is_query_complete = is_query_complete

    @property
    def logs(self):
        r"""Gets the logs of this ListOpsAgentRuntLogResponse.

        日志内容

        :return: The logs of this ListOpsAgentRuntLogResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.AgentLogContent`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this ListOpsAgentRuntLogResponse.

        日志内容

        :param logs: The logs of this ListOpsAgentRuntLogResponse.
        :type logs: list[:class:`huaweicloudsdkagentarts.v1.AgentLogContent`]
        """
        self._logs = logs

    @property
    def scroll_id(self):
        r"""Gets the scroll_id of this ListOpsAgentRuntLogResponse.

        :return: The scroll_id of this ListOpsAgentRuntLogResponse.
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        r"""Sets the scroll_id of this ListOpsAgentRuntLogResponse.

        :param scroll_id: The scroll_id of this ListOpsAgentRuntLogResponse.
        :type scroll_id: str
        """
        self._scroll_id = scroll_id

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsAgentRuntLogResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsAgentRuntLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
