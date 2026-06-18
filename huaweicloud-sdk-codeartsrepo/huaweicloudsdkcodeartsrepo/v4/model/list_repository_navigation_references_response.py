# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryNavigationReferencesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'message': 'str',
        'defs': 'list[DefEntryDto]',
        'refs': 'list[RefEntryDto]'
    }

    attribute_map = {
        'result': 'result',
        'message': 'message',
        'defs': 'defs',
        'refs': 'refs'
    }

    def __init__(self, result=None, message=None, defs=None, refs=None):
        r"""ListRepositoryNavigationReferencesResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释：** 结果标识。 **约束限制：** 不涉及。
        :type result: str
        :param message: **参数解释：** 结果消息。 **约束限制：** 不涉及。
        :type message: str
        :param defs: **参数解释：** def信息。 **约束限制：** 不涉及。
        :type defs: list[:class:`huaweicloudsdkcodeartsrepo.v4.DefEntryDto`]
        :param refs: **参数解释：** 索引信息列表。 **约束限制：** 不涉及。
        :type refs: list[:class:`huaweicloudsdkcodeartsrepo.v4.RefEntryDto`]
        """
        
        super().__init__()

        self._result = None
        self._message = None
        self._defs = None
        self._refs = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if message is not None:
            self.message = message
        if defs is not None:
            self.defs = defs
        if refs is not None:
            self.refs = refs

    @property
    def result(self):
        r"""Gets the result of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :return: The result of this ListRepositoryNavigationReferencesResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :param result: The result of this ListRepositoryNavigationReferencesResponse.
        :type result: str
        """
        self._result = result

    @property
    def message(self):
        r"""Gets the message of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :return: The message of this ListRepositoryNavigationReferencesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :param message: The message of this ListRepositoryNavigationReferencesResponse.
        :type message: str
        """
        self._message = message

    @property
    def defs(self):
        r"""Gets the defs of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** def信息。 **约束限制：** 不涉及。

        :return: The defs of this ListRepositoryNavigationReferencesResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.DefEntryDto`]
        """
        return self._defs

    @defs.setter
    def defs(self, defs):
        r"""Sets the defs of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** def信息。 **约束限制：** 不涉及。

        :param defs: The defs of this ListRepositoryNavigationReferencesResponse.
        :type defs: list[:class:`huaweicloudsdkcodeartsrepo.v4.DefEntryDto`]
        """
        self._defs = defs

    @property
    def refs(self):
        r"""Gets the refs of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** 索引信息列表。 **约束限制：** 不涉及。

        :return: The refs of this ListRepositoryNavigationReferencesResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.RefEntryDto`]
        """
        return self._refs

    @refs.setter
    def refs(self, refs):
        r"""Sets the refs of this ListRepositoryNavigationReferencesResponse.

        **参数解释：** 索引信息列表。 **约束限制：** 不涉及。

        :param refs: The refs of this ListRepositoryNavigationReferencesResponse.
        :type refs: list[:class:`huaweicloudsdkcodeartsrepo.v4.RefEntryDto`]
        """
        self._refs = refs

    def to_dict(self):
        import warnings
        warnings.warn("ListRepositoryNavigationReferencesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRepositoryNavigationReferencesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
