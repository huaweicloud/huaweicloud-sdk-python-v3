# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInsertCommandsResponse(SdkResponse):

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
        'insert_commands': 'list[InsertCommandItem]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'insert_commands': 'insert_commands',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, count=None, insert_commands=None, x_request_id=None):
        r"""ListInsertCommandsResponse

        The model defined in huaweicloud sdk

        :param count: 命令总数。
        :type count: int
        :param insert_commands: 插入播放命令列表。
        :type insert_commands: list[:class:`huaweicloudsdkmetastudio.v1.InsertCommandItem`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._count = None
        self._insert_commands = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if insert_commands is not None:
            self.insert_commands = insert_commands
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ListInsertCommandsResponse.

        命令总数。

        :return: The count of this ListInsertCommandsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListInsertCommandsResponse.

        命令总数。

        :param count: The count of this ListInsertCommandsResponse.
        :type count: int
        """
        self._count = count

    @property
    def insert_commands(self):
        r"""Gets the insert_commands of this ListInsertCommandsResponse.

        插入播放命令列表。

        :return: The insert_commands of this ListInsertCommandsResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InsertCommandItem`]
        """
        return self._insert_commands

    @insert_commands.setter
    def insert_commands(self, insert_commands):
        r"""Sets the insert_commands of this ListInsertCommandsResponse.

        插入播放命令列表。

        :param insert_commands: The insert_commands of this ListInsertCommandsResponse.
        :type insert_commands: list[:class:`huaweicloudsdkmetastudio.v1.InsertCommandItem`]
        """
        self._insert_commands = insert_commands

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListInsertCommandsResponse.

        :return: The x_request_id of this ListInsertCommandsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListInsertCommandsResponse.

        :param x_request_id: The x_request_id of this ListInsertCommandsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListInsertCommandsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInsertCommandsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
