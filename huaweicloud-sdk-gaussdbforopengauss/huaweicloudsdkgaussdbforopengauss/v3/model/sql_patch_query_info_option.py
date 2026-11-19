# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlPatchQueryInfoOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_id': 'str',
        'sql_text': 'str',
        'patch_name': 'str',
        'node_id': 'str',
        'enabled': 'bool',
        'abort_patch': 'bool'
    }

    attribute_map = {
        'sql_id': 'sql_id',
        'sql_text': 'sql_text',
        'patch_name': 'patch_name',
        'node_id': 'node_id',
        'enabled': 'enabled',
        'abort_patch': 'abort_patch'
    }

    def __init__(self, sql_id=None, sql_text=None, patch_name=None, node_id=None, enabled=None, abort_patch=None):
        r"""SqlPatchQueryInfoOption

        The model defined in huaweicloud sdk

        :param sql_id: **参数解释**: unique_sql_id。 **取值范围**: 不涉及。
        :type sql_id: str
        :param sql_text: **参数解释**: SQL文本。 **取值范围**: 不涉及。
        :type sql_text: str
        :param patch_name: **参数解释**: SQL Patch名称。 **取值范围**: 不涉及。
        :type patch_name: str
        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param enabled: **参数解释**: Patch是否生效。 **取值范围**: - true：生效 - false：不生效
        :type enabled: bool
        :param abort_patch: **参数解释**: Patch类型。 **取值范围**: - true：Abort Patch - false：非Abort Patch
        :type abort_patch: bool
        """
        
        

        self._sql_id = None
        self._sql_text = None
        self._patch_name = None
        self._node_id = None
        self._enabled = None
        self._abort_patch = None
        self.discriminator = None

        if sql_id is not None:
            self.sql_id = sql_id
        if sql_text is not None:
            self.sql_text = sql_text
        if patch_name is not None:
            self.patch_name = patch_name
        if node_id is not None:
            self.node_id = node_id
        if enabled is not None:
            self.enabled = enabled
        if abort_patch is not None:
            self.abort_patch = abort_patch

    @property
    def sql_id(self):
        r"""Gets the sql_id of this SqlPatchQueryInfoOption.

        **参数解释**: unique_sql_id。 **取值范围**: 不涉及。

        :return: The sql_id of this SqlPatchQueryInfoOption.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this SqlPatchQueryInfoOption.

        **参数解释**: unique_sql_id。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this SqlPatchQueryInfoOption.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_text(self):
        r"""Gets the sql_text of this SqlPatchQueryInfoOption.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :return: The sql_text of this SqlPatchQueryInfoOption.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        r"""Sets the sql_text of this SqlPatchQueryInfoOption.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :param sql_text: The sql_text of this SqlPatchQueryInfoOption.
        :type sql_text: str
        """
        self._sql_text = sql_text

    @property
    def patch_name(self):
        r"""Gets the patch_name of this SqlPatchQueryInfoOption.

        **参数解释**: SQL Patch名称。 **取值范围**: 不涉及。

        :return: The patch_name of this SqlPatchQueryInfoOption.
        :rtype: str
        """
        return self._patch_name

    @patch_name.setter
    def patch_name(self, patch_name):
        r"""Sets the patch_name of this SqlPatchQueryInfoOption.

        **参数解释**: SQL Patch名称。 **取值范围**: 不涉及。

        :param patch_name: The patch_name of this SqlPatchQueryInfoOption.
        :type patch_name: str
        """
        self._patch_name = patch_name

    @property
    def node_id(self):
        r"""Gets the node_id of this SqlPatchQueryInfoOption.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this SqlPatchQueryInfoOption.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SqlPatchQueryInfoOption.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this SqlPatchQueryInfoOption.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def enabled(self):
        r"""Gets the enabled of this SqlPatchQueryInfoOption.

        **参数解释**: Patch是否生效。 **取值范围**: - true：生效 - false：不生效

        :return: The enabled of this SqlPatchQueryInfoOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this SqlPatchQueryInfoOption.

        **参数解释**: Patch是否生效。 **取值范围**: - true：生效 - false：不生效

        :param enabled: The enabled of this SqlPatchQueryInfoOption.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def abort_patch(self):
        r"""Gets the abort_patch of this SqlPatchQueryInfoOption.

        **参数解释**: Patch类型。 **取值范围**: - true：Abort Patch - false：非Abort Patch

        :return: The abort_patch of this SqlPatchQueryInfoOption.
        :rtype: bool
        """
        return self._abort_patch

    @abort_patch.setter
    def abort_patch(self, abort_patch):
        r"""Sets the abort_patch of this SqlPatchQueryInfoOption.

        **参数解释**: Patch类型。 **取值范围**: - true：Abort Patch - false：非Abort Patch

        :param abort_patch: The abort_patch of this SqlPatchQueryInfoOption.
        :type abort_patch: bool
        """
        self._abort_patch = abort_patch

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
        if not isinstance(other, SqlPatchQueryInfoOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
