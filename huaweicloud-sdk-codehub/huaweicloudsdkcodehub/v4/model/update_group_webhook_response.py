# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupWebhookResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'push_events': 'bool',
        'push_events_branch_regex_filter': 'str',
        'tag_push_events': 'bool',
        'merge_requests_events': 'bool',
        'note_events': 'bool',
        'token': 'str',
        'token_type': 'str',
        'name': 'str',
        'description': 'str',
        'id': 'int',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'url': 'url',
        'push_events': 'push_events',
        'push_events_branch_regex_filter': 'push_events_branch_regex_filter',
        'tag_push_events': 'tag_push_events',
        'merge_requests_events': 'merge_requests_events',
        'note_events': 'note_events',
        'token': 'token',
        'token_type': 'token_type',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, url=None, push_events=None, push_events_branch_regex_filter=None, tag_push_events=None, merge_requests_events=None, note_events=None, token=None, token_type=None, name=None, description=None, id=None, created_at=None, updated_at=None):
        r"""UpdateGroupWebhookResponse

        The model defined in huaweicloud sdk

        :param url: **参数解释：** webhook地址。 **取值范围：** 字符串长度不少于0，不超过500。
        :type url: str
        :param push_events: **参数解释：** 是否启用推送事件。
        :type push_events: bool
        :param push_events_branch_regex_filter: **参数解释：** 推送事件分支过滤正则规则。 **取值范围：** 字符串长度不少于0，不超过500。                
        :type push_events_branch_regex_filter: str
        :param tag_push_events: **参数解释：** 是否启用Tag推送事件。
        :type tag_push_events: bool
        :param merge_requests_events: **参数解释：** 是否启用合并请求事件。
        :type merge_requests_events: bool
        :param note_events: **参数解释：** 是否启用评论事件。
        :type note_events: bool
        :param token: **参数解释：** token值，作为返回值时会使用掩码代替实际值。 **取值范围：** 字符串长度不少于0，不超过2000。
        :type token: str
        :param token_type: **参数解释：** token类型，默认为X-Repo-Token。 **取值范围：** 字符串长度不少于0，不超过200。
        :type token_type: str
        :param name: **参数解释：** 名称。 **取值范围：** 字符串长度不少于0，不超过200。
        :type name: str
        :param description: **参数解释：** 描述。 **取值范围：** 字符串长度不少于0，不超过200。
        :type description: str
        :param id: **参数解释：** Webhook id。
        :type id: int
        :param created_at: **参数解释：** 创建时间。 **参数解释：** yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 **参数解释：** yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX
        :type updated_at: str
        """
        
        super(UpdateGroupWebhookResponse, self).__init__()

        self._url = None
        self._push_events = None
        self._push_events_branch_regex_filter = None
        self._tag_push_events = None
        self._merge_requests_events = None
        self._note_events = None
        self._token = None
        self._token_type = None
        self._name = None
        self._description = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if push_events is not None:
            self.push_events = push_events
        if push_events_branch_regex_filter is not None:
            self.push_events_branch_regex_filter = push_events_branch_regex_filter
        if tag_push_events is not None:
            self.tag_push_events = tag_push_events
        if merge_requests_events is not None:
            self.merge_requests_events = merge_requests_events
        if note_events is not None:
            self.note_events = note_events
        if token is not None:
            self.token = token
        if token_type is not None:
            self.token_type = token_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def url(self):
        r"""Gets the url of this UpdateGroupWebhookResponse.

        **参数解释：** webhook地址。 **取值范围：** 字符串长度不少于0，不超过500。

        :return: The url of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UpdateGroupWebhookResponse.

        **参数解释：** webhook地址。 **取值范围：** 字符串长度不少于0，不超过500。

        :param url: The url of this UpdateGroupWebhookResponse.
        :type url: str
        """
        self._url = url

    @property
    def push_events(self):
        r"""Gets the push_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用推送事件。

        :return: The push_events of this UpdateGroupWebhookResponse.
        :rtype: bool
        """
        return self._push_events

    @push_events.setter
    def push_events(self, push_events):
        r"""Sets the push_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用推送事件。

        :param push_events: The push_events of this UpdateGroupWebhookResponse.
        :type push_events: bool
        """
        self._push_events = push_events

    @property
    def push_events_branch_regex_filter(self):
        r"""Gets the push_events_branch_regex_filter of this UpdateGroupWebhookResponse.

        **参数解释：** 推送事件分支过滤正则规则。 **取值范围：** 字符串长度不少于0，不超过500。                

        :return: The push_events_branch_regex_filter of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._push_events_branch_regex_filter

    @push_events_branch_regex_filter.setter
    def push_events_branch_regex_filter(self, push_events_branch_regex_filter):
        r"""Sets the push_events_branch_regex_filter of this UpdateGroupWebhookResponse.

        **参数解释：** 推送事件分支过滤正则规则。 **取值范围：** 字符串长度不少于0，不超过500。                

        :param push_events_branch_regex_filter: The push_events_branch_regex_filter of this UpdateGroupWebhookResponse.
        :type push_events_branch_regex_filter: str
        """
        self._push_events_branch_regex_filter = push_events_branch_regex_filter

    @property
    def tag_push_events(self):
        r"""Gets the tag_push_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用Tag推送事件。

        :return: The tag_push_events of this UpdateGroupWebhookResponse.
        :rtype: bool
        """
        return self._tag_push_events

    @tag_push_events.setter
    def tag_push_events(self, tag_push_events):
        r"""Sets the tag_push_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用Tag推送事件。

        :param tag_push_events: The tag_push_events of this UpdateGroupWebhookResponse.
        :type tag_push_events: bool
        """
        self._tag_push_events = tag_push_events

    @property
    def merge_requests_events(self):
        r"""Gets the merge_requests_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用合并请求事件。

        :return: The merge_requests_events of this UpdateGroupWebhookResponse.
        :rtype: bool
        """
        return self._merge_requests_events

    @merge_requests_events.setter
    def merge_requests_events(self, merge_requests_events):
        r"""Sets the merge_requests_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用合并请求事件。

        :param merge_requests_events: The merge_requests_events of this UpdateGroupWebhookResponse.
        :type merge_requests_events: bool
        """
        self._merge_requests_events = merge_requests_events

    @property
    def note_events(self):
        r"""Gets the note_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用评论事件。

        :return: The note_events of this UpdateGroupWebhookResponse.
        :rtype: bool
        """
        return self._note_events

    @note_events.setter
    def note_events(self, note_events):
        r"""Sets the note_events of this UpdateGroupWebhookResponse.

        **参数解释：** 是否启用评论事件。

        :param note_events: The note_events of this UpdateGroupWebhookResponse.
        :type note_events: bool
        """
        self._note_events = note_events

    @property
    def token(self):
        r"""Gets the token of this UpdateGroupWebhookResponse.

        **参数解释：** token值，作为返回值时会使用掩码代替实际值。 **取值范围：** 字符串长度不少于0，不超过2000。

        :return: The token of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this UpdateGroupWebhookResponse.

        **参数解释：** token值，作为返回值时会使用掩码代替实际值。 **取值范围：** 字符串长度不少于0，不超过2000。

        :param token: The token of this UpdateGroupWebhookResponse.
        :type token: str
        """
        self._token = token

    @property
    def token_type(self):
        r"""Gets the token_type of this UpdateGroupWebhookResponse.

        **参数解释：** token类型，默认为X-Repo-Token。 **取值范围：** 字符串长度不少于0，不超过200。

        :return: The token_type of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        r"""Sets the token_type of this UpdateGroupWebhookResponse.

        **参数解释：** token类型，默认为X-Repo-Token。 **取值范围：** 字符串长度不少于0，不超过200。

        :param token_type: The token_type of this UpdateGroupWebhookResponse.
        :type token_type: str
        """
        self._token_type = token_type

    @property
    def name(self):
        r"""Gets the name of this UpdateGroupWebhookResponse.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于0，不超过200。

        :return: The name of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateGroupWebhookResponse.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于0，不超过200。

        :param name: The name of this UpdateGroupWebhookResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateGroupWebhookResponse.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于0，不超过200。

        :return: The description of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateGroupWebhookResponse.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于0，不超过200。

        :param description: The description of this UpdateGroupWebhookResponse.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this UpdateGroupWebhookResponse.

        **参数解释：** Webhook id。

        :return: The id of this UpdateGroupWebhookResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateGroupWebhookResponse.

        **参数解释：** Webhook id。

        :param id: The id of this UpdateGroupWebhookResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateGroupWebhookResponse.

        **参数解释：** 创建时间。 **参数解释：** yyyy-MM-dd'T'HH:mm:ss.SSSXXX

        :return: The created_at of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateGroupWebhookResponse.

        **参数解释：** 创建时间。 **参数解释：** yyyy-MM-dd'T'HH:mm:ss.SSSXXX

        :param created_at: The created_at of this UpdateGroupWebhookResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateGroupWebhookResponse.

        **参数解释：** 更新时间。 **参数解释：** yyyy-MM-dd'T'HH:mm:ss.SSSXXX

        :return: The updated_at of this UpdateGroupWebhookResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateGroupWebhookResponse.

        **参数解释：** 更新时间。 **参数解释：** yyyy-MM-dd'T'HH:mm:ss.SSSXXX

        :param updated_at: The updated_at of this UpdateGroupWebhookResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, UpdateGroupWebhookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
