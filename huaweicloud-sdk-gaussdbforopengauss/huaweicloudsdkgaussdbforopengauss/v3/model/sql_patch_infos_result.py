# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlPatchInfosResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'patch_name': 'str',
        'sql_id': 'str',
        'enabled': 'bool',
        'patch_status': 'str',
        'abort_patch': 'bool',
        'hint': 'str',
        'sql_text': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'patch_name': 'patch_name',
        'sql_id': 'sql_id',
        'enabled': 'enabled',
        'patch_status': 'patch_status',
        'abort_patch': 'abort_patch',
        'hint': 'hint',
        'sql_text': 'sql_text',
        'node_id': 'node_id'
    }

    def __init__(self, patch_name=None, sql_id=None, enabled=None, patch_status=None, abort_patch=None, hint=None, sql_text=None, node_id=None):
        r"""SqlPatchInfosResult

        The model defined in huaweicloud sdk

        :param patch_name: **参数解释**: Patch名称。 **取值范围**: 不涉及。
        :type patch_name: str
        :param sql_id: **参数解释**: unique_sql_id，标识SQL文本的ID。 **取值范围**: 不涉及。
        :type sql_id: str
        :param enabled: **参数解释**: Patch是否生效。 **取值范围**: - true：生效 - false：不生效
        :type enabled: bool
        :param patch_status: **参数解释**: Patch的状态。d表示SQL ID模式，h表示SQL Hash模式。 **取值范围**: - d：SQL ID模式 - h：SQL Hash模式
        :type patch_status: str
        :param abort_patch: **参数解释**: 是否为Abort Patch。 **取值范围**: - true：是 - false：否
        :type abort_patch: bool
        :param hint: **参数解释**: Patch内容（Hint文本）。 **取值范围**: 不涉及。
        :type hint: str
        :param sql_text: **参数解释**: SQL文本。 **取值范围**: 不涉及。
        :type sql_text: str
        :param node_id: **参数解释**: SQL Patch所属的节点。主备版为主DN，分布式版为CN。 **取值范围**: 不涉及。
        :type node_id: str
        """
        
        

        self._patch_name = None
        self._sql_id = None
        self._enabled = None
        self._patch_status = None
        self._abort_patch = None
        self._hint = None
        self._sql_text = None
        self._node_id = None
        self.discriminator = None

        if patch_name is not None:
            self.patch_name = patch_name
        if sql_id is not None:
            self.sql_id = sql_id
        if enabled is not None:
            self.enabled = enabled
        if patch_status is not None:
            self.patch_status = patch_status
        if abort_patch is not None:
            self.abort_patch = abort_patch
        if hint is not None:
            self.hint = hint
        if sql_text is not None:
            self.sql_text = sql_text
        if node_id is not None:
            self.node_id = node_id

    @property
    def patch_name(self):
        r"""Gets the patch_name of this SqlPatchInfosResult.

        **参数解释**: Patch名称。 **取值范围**: 不涉及。

        :return: The patch_name of this SqlPatchInfosResult.
        :rtype: str
        """
        return self._patch_name

    @patch_name.setter
    def patch_name(self, patch_name):
        r"""Sets the patch_name of this SqlPatchInfosResult.

        **参数解释**: Patch名称。 **取值范围**: 不涉及。

        :param patch_name: The patch_name of this SqlPatchInfosResult.
        :type patch_name: str
        """
        self._patch_name = patch_name

    @property
    def sql_id(self):
        r"""Gets the sql_id of this SqlPatchInfosResult.

        **参数解释**: unique_sql_id，标识SQL文本的ID。 **取值范围**: 不涉及。

        :return: The sql_id of this SqlPatchInfosResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this SqlPatchInfosResult.

        **参数解释**: unique_sql_id，标识SQL文本的ID。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this SqlPatchInfosResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def enabled(self):
        r"""Gets the enabled of this SqlPatchInfosResult.

        **参数解释**: Patch是否生效。 **取值范围**: - true：生效 - false：不生效

        :return: The enabled of this SqlPatchInfosResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this SqlPatchInfosResult.

        **参数解释**: Patch是否生效。 **取值范围**: - true：生效 - false：不生效

        :param enabled: The enabled of this SqlPatchInfosResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def patch_status(self):
        r"""Gets the patch_status of this SqlPatchInfosResult.

        **参数解释**: Patch的状态。d表示SQL ID模式，h表示SQL Hash模式。 **取值范围**: - d：SQL ID模式 - h：SQL Hash模式

        :return: The patch_status of this SqlPatchInfosResult.
        :rtype: str
        """
        return self._patch_status

    @patch_status.setter
    def patch_status(self, patch_status):
        r"""Sets the patch_status of this SqlPatchInfosResult.

        **参数解释**: Patch的状态。d表示SQL ID模式，h表示SQL Hash模式。 **取值范围**: - d：SQL ID模式 - h：SQL Hash模式

        :param patch_status: The patch_status of this SqlPatchInfosResult.
        :type patch_status: str
        """
        self._patch_status = patch_status

    @property
    def abort_patch(self):
        r"""Gets the abort_patch of this SqlPatchInfosResult.

        **参数解释**: 是否为Abort Patch。 **取值范围**: - true：是 - false：否

        :return: The abort_patch of this SqlPatchInfosResult.
        :rtype: bool
        """
        return self._abort_patch

    @abort_patch.setter
    def abort_patch(self, abort_patch):
        r"""Sets the abort_patch of this SqlPatchInfosResult.

        **参数解释**: 是否为Abort Patch。 **取值范围**: - true：是 - false：否

        :param abort_patch: The abort_patch of this SqlPatchInfosResult.
        :type abort_patch: bool
        """
        self._abort_patch = abort_patch

    @property
    def hint(self):
        r"""Gets the hint of this SqlPatchInfosResult.

        **参数解释**: Patch内容（Hint文本）。 **取值范围**: 不涉及。

        :return: The hint of this SqlPatchInfosResult.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        r"""Sets the hint of this SqlPatchInfosResult.

        **参数解释**: Patch内容（Hint文本）。 **取值范围**: 不涉及。

        :param hint: The hint of this SqlPatchInfosResult.
        :type hint: str
        """
        self._hint = hint

    @property
    def sql_text(self):
        r"""Gets the sql_text of this SqlPatchInfosResult.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :return: The sql_text of this SqlPatchInfosResult.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        r"""Sets the sql_text of this SqlPatchInfosResult.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :param sql_text: The sql_text of this SqlPatchInfosResult.
        :type sql_text: str
        """
        self._sql_text = sql_text

    @property
    def node_id(self):
        r"""Gets the node_id of this SqlPatchInfosResult.

        **参数解释**: SQL Patch所属的节点。主备版为主DN，分布式版为CN。 **取值范围**: 不涉及。

        :return: The node_id of this SqlPatchInfosResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SqlPatchInfosResult.

        **参数解释**: SQL Patch所属的节点。主备版为主DN，分布式版为CN。 **取值范围**: 不涉及。

        :param node_id: The node_id of this SqlPatchInfosResult.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, SqlPatchInfosResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
