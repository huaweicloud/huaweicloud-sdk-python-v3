# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryNavigationOutlineResponse(SdkResponse):

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
        'file_path': 'str',
        'revision': 'str',
        'symbols': 'list[SymbolNodeDto]'
    }

    attribute_map = {
        'result': 'result',
        'message': 'message',
        'file_path': 'file_path',
        'revision': 'revision',
        'symbols': 'symbols'
    }

    def __init__(self, result=None, message=None, file_path=None, revision=None, symbols=None):
        r"""ShowRepositoryNavigationOutlineResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释：** 结果标识。 **约束限制：** 不涉及。
        :type result: str
        :param message: **参数解释：** 结果消息。 **约束限制：** 不涉及。
        :type message: str
        :param file_path: **参数解释：** 文件路径。 **约束限制：** 不涉及。
        :type file_path: str
        :param revision: **参数解释：** 所在版本号（commit id）。 **约束限制：** 不涉及。
        :type revision: str
        :param symbols: **参数解释：** 符号列表。 **约束限制：** 不涉及。
        :type symbols: list[:class:`huaweicloudsdkcodeartsrepo.v4.SymbolNodeDto`]
        """
        
        super().__init__()

        self._result = None
        self._message = None
        self._file_path = None
        self._revision = None
        self._symbols = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if message is not None:
            self.message = message
        if file_path is not None:
            self.file_path = file_path
        if revision is not None:
            self.revision = revision
        if symbols is not None:
            self.symbols = symbols

    @property
    def result(self):
        r"""Gets the result of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :return: The result of this ShowRepositoryNavigationOutlineResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :param result: The result of this ShowRepositoryNavigationOutlineResponse.
        :type result: str
        """
        self._result = result

    @property
    def message(self):
        r"""Gets the message of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :return: The message of this ShowRepositoryNavigationOutlineResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :param message: The message of this ShowRepositoryNavigationOutlineResponse.
        :type message: str
        """
        self._message = message

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 文件路径。 **约束限制：** 不涉及。

        :return: The file_path of this ShowRepositoryNavigationOutlineResponse.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 文件路径。 **约束限制：** 不涉及。

        :param file_path: The file_path of this ShowRepositoryNavigationOutlineResponse.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def revision(self):
        r"""Gets the revision of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 所在版本号（commit id）。 **约束限制：** 不涉及。

        :return: The revision of this ShowRepositoryNavigationOutlineResponse.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 所在版本号（commit id）。 **约束限制：** 不涉及。

        :param revision: The revision of this ShowRepositoryNavigationOutlineResponse.
        :type revision: str
        """
        self._revision = revision

    @property
    def symbols(self):
        r"""Gets the symbols of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 符号列表。 **约束限制：** 不涉及。

        :return: The symbols of this ShowRepositoryNavigationOutlineResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.SymbolNodeDto`]
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        r"""Sets the symbols of this ShowRepositoryNavigationOutlineResponse.

        **参数解释：** 符号列表。 **约束限制：** 不涉及。

        :param symbols: The symbols of this ShowRepositoryNavigationOutlineResponse.
        :type symbols: list[:class:`huaweicloudsdkcodeartsrepo.v4.SymbolNodeDto`]
        """
        self._symbols = symbols

    def to_dict(self):
        import warnings
        warnings.warn("ShowRepositoryNavigationOutlineResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRepositoryNavigationOutlineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
