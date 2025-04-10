# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareDocsParamDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'structured_doc_id': 'str',
        'shared_user_id': 'str',
        'shared_user_name': 'str',
        'share_user_id': 'str',
        'share_user_name': 'str',
        'auth_type': 'str',
        'modifier': 'str'
    }

    attribute_map = {
        'structured_doc_id': 'structured_doc_id',
        'shared_user_id': 'shared_user_id',
        'shared_user_name': 'shared_user_name',
        'share_user_id': 'share_user_id',
        'share_user_name': 'share_user_name',
        'auth_type': 'auth_type',
        'modifier': 'modifier'
    }

    def __init__(self, structured_doc_id=None, shared_user_id=None, shared_user_name=None, share_user_id=None, share_user_name=None, auth_type=None, modifier=None):
        r"""ShareDocsParamDto

        The model defined in huaweicloud sdk

        :param structured_doc_id: **参数解释**：  结构化文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type structured_doc_id: str
        :param shared_user_id: **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。
        :type shared_user_id: str
        :param shared_user_name: **参数解释**：  被分享用户名。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。
        :type shared_user_name: str
        :param share_user_id: **参数解释**：  分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type share_user_id: str
        :param share_user_name: **参数解释**：  分享用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type share_user_name: str
        :param auth_type: **参数解释**：  认证类型。  **约束限制**：  不涉及。  **取值范围**：  - read：只读。 - write：读写。  **默认取值**：  不涉及。
        :type auth_type: str
        :param modifier: **参数解释**：  修改人。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type modifier: str
        """
        
        

        self._structured_doc_id = None
        self._shared_user_id = None
        self._shared_user_name = None
        self._share_user_id = None
        self._share_user_name = None
        self._auth_type = None
        self._modifier = None
        self.discriminator = None

        if structured_doc_id is not None:
            self.structured_doc_id = structured_doc_id
        if shared_user_id is not None:
            self.shared_user_id = shared_user_id
        if shared_user_name is not None:
            self.shared_user_name = shared_user_name
        if share_user_id is not None:
            self.share_user_id = share_user_id
        if share_user_name is not None:
            self.share_user_name = share_user_name
        if auth_type is not None:
            self.auth_type = auth_type
        if modifier is not None:
            self.modifier = modifier

    @property
    def structured_doc_id(self):
        r"""Gets the structured_doc_id of this ShareDocsParamDto.

        **参数解释**：  结构化文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The structured_doc_id of this ShareDocsParamDto.
        :rtype: str
        """
        return self._structured_doc_id

    @structured_doc_id.setter
    def structured_doc_id(self, structured_doc_id):
        r"""Sets the structured_doc_id of this ShareDocsParamDto.

        **参数解释**：  结构化文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param structured_doc_id: The structured_doc_id of this ShareDocsParamDto.
        :type structured_doc_id: str
        """
        self._structured_doc_id = structured_doc_id

    @property
    def shared_user_id(self):
        r"""Gets the shared_user_id of this ShareDocsParamDto.

        **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :return: The shared_user_id of this ShareDocsParamDto.
        :rtype: str
        """
        return self._shared_user_id

    @shared_user_id.setter
    def shared_user_id(self, shared_user_id):
        r"""Sets the shared_user_id of this ShareDocsParamDto.

        **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :param shared_user_id: The shared_user_id of this ShareDocsParamDto.
        :type shared_user_id: str
        """
        self._shared_user_id = shared_user_id

    @property
    def shared_user_name(self):
        r"""Gets the shared_user_name of this ShareDocsParamDto.

        **参数解释**：  被分享用户名。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :return: The shared_user_name of this ShareDocsParamDto.
        :rtype: str
        """
        return self._shared_user_name

    @shared_user_name.setter
    def shared_user_name(self, shared_user_name):
        r"""Sets the shared_user_name of this ShareDocsParamDto.

        **参数解释**：  被分享用户名。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :param shared_user_name: The shared_user_name of this ShareDocsParamDto.
        :type shared_user_name: str
        """
        self._shared_user_name = shared_user_name

    @property
    def share_user_id(self):
        r"""Gets the share_user_id of this ShareDocsParamDto.

        **参数解释**：  分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The share_user_id of this ShareDocsParamDto.
        :rtype: str
        """
        return self._share_user_id

    @share_user_id.setter
    def share_user_id(self, share_user_id):
        r"""Sets the share_user_id of this ShareDocsParamDto.

        **参数解释**：  分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param share_user_id: The share_user_id of this ShareDocsParamDto.
        :type share_user_id: str
        """
        self._share_user_id = share_user_id

    @property
    def share_user_name(self):
        r"""Gets the share_user_name of this ShareDocsParamDto.

        **参数解释**：  分享用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The share_user_name of this ShareDocsParamDto.
        :rtype: str
        """
        return self._share_user_name

    @share_user_name.setter
    def share_user_name(self, share_user_name):
        r"""Sets the share_user_name of this ShareDocsParamDto.

        **参数解释**：  分享用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param share_user_name: The share_user_name of this ShareDocsParamDto.
        :type share_user_name: str
        """
        self._share_user_name = share_user_name

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ShareDocsParamDto.

        **参数解释**：  认证类型。  **约束限制**：  不涉及。  **取值范围**：  - read：只读。 - write：读写。  **默认取值**：  不涉及。

        :return: The auth_type of this ShareDocsParamDto.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ShareDocsParamDto.

        **参数解释**：  认证类型。  **约束限制**：  不涉及。  **取值范围**：  - read：只读。 - write：读写。  **默认取值**：  不涉及。

        :param auth_type: The auth_type of this ShareDocsParamDto.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def modifier(self):
        r"""Gets the modifier of this ShareDocsParamDto.

        **参数解释**：  修改人。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The modifier of this ShareDocsParamDto.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this ShareDocsParamDto.

        **参数解释**：  修改人。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param modifier: The modifier of this ShareDocsParamDto.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, ShareDocsParamDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
