# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlPatchResponse(SdkResponse):

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
        'hint': 'str',
        'patch_status': 'str'
    }

    attribute_map = {
        'patch_name': 'patch_name',
        'hint': 'hint',
        'patch_status': 'patch_status'
    }

    def __init__(self, patch_name=None, hint=None, patch_status=None):
        r"""ShowSqlPatchResponse

        The model defined in huaweicloud sdk

        :param patch_name: **参数解释**: PATCH名称。 **取值范围**: 不涉及。
        :type patch_name: str
        :param hint: **参数解释**: PATCH内容（Hint文本）。对于abort 类型的SQL PATCH此字段为空。 **取值范围**: 不涉及。
        :type hint: str
        :param patch_status: **参数解释**: PATCH状态。 **取值范围**: - enabled：表示SQL PATCH生效。 - disabled：表示SQL PATCH失效。
        :type patch_status: str
        """
        
        super(ShowSqlPatchResponse, self).__init__()

        self._patch_name = None
        self._hint = None
        self._patch_status = None
        self.discriminator = None

        if patch_name is not None:
            self.patch_name = patch_name
        if hint is not None:
            self.hint = hint
        if patch_status is not None:
            self.patch_status = patch_status

    @property
    def patch_name(self):
        r"""Gets the patch_name of this ShowSqlPatchResponse.

        **参数解释**: PATCH名称。 **取值范围**: 不涉及。

        :return: The patch_name of this ShowSqlPatchResponse.
        :rtype: str
        """
        return self._patch_name

    @patch_name.setter
    def patch_name(self, patch_name):
        r"""Sets the patch_name of this ShowSqlPatchResponse.

        **参数解释**: PATCH名称。 **取值范围**: 不涉及。

        :param patch_name: The patch_name of this ShowSqlPatchResponse.
        :type patch_name: str
        """
        self._patch_name = patch_name

    @property
    def hint(self):
        r"""Gets the hint of this ShowSqlPatchResponse.

        **参数解释**: PATCH内容（Hint文本）。对于abort 类型的SQL PATCH此字段为空。 **取值范围**: 不涉及。

        :return: The hint of this ShowSqlPatchResponse.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        r"""Sets the hint of this ShowSqlPatchResponse.

        **参数解释**: PATCH内容（Hint文本）。对于abort 类型的SQL PATCH此字段为空。 **取值范围**: 不涉及。

        :param hint: The hint of this ShowSqlPatchResponse.
        :type hint: str
        """
        self._hint = hint

    @property
    def patch_status(self):
        r"""Gets the patch_status of this ShowSqlPatchResponse.

        **参数解释**: PATCH状态。 **取值范围**: - enabled：表示SQL PATCH生效。 - disabled：表示SQL PATCH失效。

        :return: The patch_status of this ShowSqlPatchResponse.
        :rtype: str
        """
        return self._patch_status

    @patch_status.setter
    def patch_status(self, patch_status):
        r"""Sets the patch_status of this ShowSqlPatchResponse.

        **参数解释**: PATCH状态。 **取值范围**: - enabled：表示SQL PATCH生效。 - disabled：表示SQL PATCH失效。

        :param patch_status: The patch_status of this ShowSqlPatchResponse.
        :type patch_status: str
        """
        self._patch_status = patch_status

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
        if not isinstance(other, ShowSqlPatchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
