# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectWebhookLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'hook_id': 'int',
        'offset': 'int',
        'limit': 'int',
        'repository_id': 'int',
        'uuid': 'str',
        'created_after': 'datetime',
        'created_before': 'datetime'
    }

    attribute_map = {
        'project_id': 'project_id',
        'hook_id': 'hook_id',
        'offset': 'offset',
        'limit': 'limit',
        'repository_id': 'repository_id',
        'uuid': 'uuid',
        'created_after': 'created_after',
        'created_before': 'created_before'
    }

    def __init__(self, project_id=None, hook_id=None, offset=None, limit=None, repository_id=None, uuid=None, created_after=None, created_before=None):
        r"""ListProjectWebhookLogsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
        :param hook_id: **参数解释：**  Webhook id。
        :type hook_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param repository_id: **参数解释：** 仓库ID
        :type repository_id: int
        :param uuid: **参数解释：** Webhook每次发送消息时会在请求体中带上uuid字段。uuid具有唯一性，合并请求相关的Webhook事件中的uuid会包含合并请求iid。此处可以使用完整的uuid或者合并请求iid。 **约束限制：** 可选。 **取值范围：** 字符串长度不少于1，不超过100。 **默认取值：** 不涉及。
        :type uuid: str
        :param created_after: **参数解释：** 检索执行时间段的起始时间
        :type created_after: datetime
        :param created_before: **参数解释：** 检索执行时间段的结束时间
        :type created_before: datetime
        """
        
        

        self._project_id = None
        self._hook_id = None
        self._offset = None
        self._limit = None
        self._repository_id = None
        self._uuid = None
        self._created_after = None
        self._created_before = None
        self.discriminator = None

        self.project_id = project_id
        self.hook_id = hook_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if repository_id is not None:
            self.repository_id = repository_id
        if uuid is not None:
            self.uuid = uuid
        if created_after is not None:
            self.created_after = created_after
        if created_before is not None:
            self.created_before = created_before

    @property
    def project_id(self):
        r"""Gets the project_id of this ListProjectWebhookLogsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ListProjectWebhookLogsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectWebhookLogsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ListProjectWebhookLogsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def hook_id(self):
        r"""Gets the hook_id of this ListProjectWebhookLogsRequest.

        **参数解释：**  Webhook id。

        :return: The hook_id of this ListProjectWebhookLogsRequest.
        :rtype: int
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        r"""Sets the hook_id of this ListProjectWebhookLogsRequest.

        **参数解释：**  Webhook id。

        :param hook_id: The hook_id of this ListProjectWebhookLogsRequest.
        :type hook_id: int
        """
        self._hook_id = hook_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProjectWebhookLogsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListProjectWebhookLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProjectWebhookLogsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListProjectWebhookLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProjectWebhookLogsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListProjectWebhookLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProjectWebhookLogsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListProjectWebhookLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListProjectWebhookLogsRequest.

        **参数解释：** 仓库ID

        :return: The repository_id of this ListProjectWebhookLogsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListProjectWebhookLogsRequest.

        **参数解释：** 仓库ID

        :param repository_id: The repository_id of this ListProjectWebhookLogsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def uuid(self):
        r"""Gets the uuid of this ListProjectWebhookLogsRequest.

        **参数解释：** Webhook每次发送消息时会在请求体中带上uuid字段。uuid具有唯一性，合并请求相关的Webhook事件中的uuid会包含合并请求iid。此处可以使用完整的uuid或者合并请求iid。 **约束限制：** 可选。 **取值范围：** 字符串长度不少于1，不超过100。 **默认取值：** 不涉及。

        :return: The uuid of this ListProjectWebhookLogsRequest.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ListProjectWebhookLogsRequest.

        **参数解释：** Webhook每次发送消息时会在请求体中带上uuid字段。uuid具有唯一性，合并请求相关的Webhook事件中的uuid会包含合并请求iid。此处可以使用完整的uuid或者合并请求iid。 **约束限制：** 可选。 **取值范围：** 字符串长度不少于1，不超过100。 **默认取值：** 不涉及。

        :param uuid: The uuid of this ListProjectWebhookLogsRequest.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def created_after(self):
        r"""Gets the created_after of this ListProjectWebhookLogsRequest.

        **参数解释：** 检索执行时间段的起始时间

        :return: The created_after of this ListProjectWebhookLogsRequest.
        :rtype: datetime
        """
        return self._created_after

    @created_after.setter
    def created_after(self, created_after):
        r"""Sets the created_after of this ListProjectWebhookLogsRequest.

        **参数解释：** 检索执行时间段的起始时间

        :param created_after: The created_after of this ListProjectWebhookLogsRequest.
        :type created_after: datetime
        """
        self._created_after = created_after

    @property
    def created_before(self):
        r"""Gets the created_before of this ListProjectWebhookLogsRequest.

        **参数解释：** 检索执行时间段的结束时间

        :return: The created_before of this ListProjectWebhookLogsRequest.
        :rtype: datetime
        """
        return self._created_before

    @created_before.setter
    def created_before(self, created_before):
        r"""Sets the created_before of this ListProjectWebhookLogsRequest.

        **参数解释：** 检索执行时间段的结束时间

        :param created_before: The created_before of this ListProjectWebhookLogsRequest.
        :type created_before: datetime
        """
        self._created_before = created_before

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
        if not isinstance(other, ListProjectWebhookLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
