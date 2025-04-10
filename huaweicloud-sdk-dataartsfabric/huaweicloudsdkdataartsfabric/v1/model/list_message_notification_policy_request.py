# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessageNotificationPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'message_type': 'str',
        'name_pattern': 'str',
        'notify_type': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'message_type': 'message_type',
        'name_pattern': 'name_pattern',
        'notify_type': 'notify_type'
    }

    def __init__(self, workspace_id=None, offset=None, limit=None, message_type=None, name_pattern=None, notify_type=None):
        r"""ListMessageNotificationPolicyRequest

        The model defined in huaweicloud sdk

        :param workspace_id: Workspace的ID
        :type workspace_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param message_type: 消息类型。job:任务执行结果消息。
        :type message_type: str
        :param name_pattern: 名称样式。支持模糊匹配，区分大小写
        :type name_pattern: str
        :param notify_type: 消息类型。SUCCESS:成功通知；FAILED：失败通知
        :type notify_type: str
        """
        
        

        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._message_type = None
        self._name_pattern = None
        self._notify_type = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if message_type is not None:
            self.message_type = message_type
        if name_pattern is not None:
            self.name_pattern = name_pattern
        if notify_type is not None:
            self.notify_type = notify_type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListMessageNotificationPolicyRequest.

        Workspace的ID

        :return: The workspace_id of this ListMessageNotificationPolicyRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListMessageNotificationPolicyRequest.

        Workspace的ID

        :param workspace_id: The workspace_id of this ListMessageNotificationPolicyRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListMessageNotificationPolicyRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListMessageNotificationPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMessageNotificationPolicyRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListMessageNotificationPolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMessageNotificationPolicyRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListMessageNotificationPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMessageNotificationPolicyRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListMessageNotificationPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def message_type(self):
        r"""Gets the message_type of this ListMessageNotificationPolicyRequest.

        消息类型。job:任务执行结果消息。

        :return: The message_type of this ListMessageNotificationPolicyRequest.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        r"""Sets the message_type of this ListMessageNotificationPolicyRequest.

        消息类型。job:任务执行结果消息。

        :param message_type: The message_type of this ListMessageNotificationPolicyRequest.
        :type message_type: str
        """
        self._message_type = message_type

    @property
    def name_pattern(self):
        r"""Gets the name_pattern of this ListMessageNotificationPolicyRequest.

        名称样式。支持模糊匹配，区分大小写

        :return: The name_pattern of this ListMessageNotificationPolicyRequest.
        :rtype: str
        """
        return self._name_pattern

    @name_pattern.setter
    def name_pattern(self, name_pattern):
        r"""Sets the name_pattern of this ListMessageNotificationPolicyRequest.

        名称样式。支持模糊匹配，区分大小写

        :param name_pattern: The name_pattern of this ListMessageNotificationPolicyRequest.
        :type name_pattern: str
        """
        self._name_pattern = name_pattern

    @property
    def notify_type(self):
        r"""Gets the notify_type of this ListMessageNotificationPolicyRequest.

        消息类型。SUCCESS:成功通知；FAILED：失败通知

        :return: The notify_type of this ListMessageNotificationPolicyRequest.
        :rtype: str
        """
        return self._notify_type

    @notify_type.setter
    def notify_type(self, notify_type):
        r"""Sets the notify_type of this ListMessageNotificationPolicyRequest.

        消息类型。SUCCESS:成功通知；FAILED：失败通知

        :param notify_type: The notify_type of this ListMessageNotificationPolicyRequest.
        :type notify_type: str
        """
        self._notify_type = notify_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListMessageNotificationPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
