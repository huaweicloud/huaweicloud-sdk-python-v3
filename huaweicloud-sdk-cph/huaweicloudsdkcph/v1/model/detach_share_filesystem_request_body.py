# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachShareFilesystemRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'id': 'str',
        'server_ids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'server_ids': 'server_ids'
    }

    def __init__(self, type=None, id=None, server_ids=None):
        r"""DetachShareFilesystemRequestBody

        The model defined in huaweicloud sdk

        :param type: 共享文件系统类型，当前仅支持“sfs_turbo”。
        :type type: str
        :param id: 共享文件系统id。
        :type id: str
        :param server_ids: 云手机服务器id列表。一次最多卸载20台。
        :type server_ids: list[str]
        """
        
        

        self._type = None
        self._id = None
        self._server_ids = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.server_ids = server_ids

    @property
    def type(self):
        r"""Gets the type of this DetachShareFilesystemRequestBody.

        共享文件系统类型，当前仅支持“sfs_turbo”。

        :return: The type of this DetachShareFilesystemRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DetachShareFilesystemRequestBody.

        共享文件系统类型，当前仅支持“sfs_turbo”。

        :param type: The type of this DetachShareFilesystemRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this DetachShareFilesystemRequestBody.

        共享文件系统id。

        :return: The id of this DetachShareFilesystemRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DetachShareFilesystemRequestBody.

        共享文件系统id。

        :param id: The id of this DetachShareFilesystemRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def server_ids(self):
        r"""Gets the server_ids of this DetachShareFilesystemRequestBody.

        云手机服务器id列表。一次最多卸载20台。

        :return: The server_ids of this DetachShareFilesystemRequestBody.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this DetachShareFilesystemRequestBody.

        云手机服务器id列表。一次最多卸载20台。

        :param server_ids: The server_ids of this DetachShareFilesystemRequestBody.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

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
        if not isinstance(other, DetachShareFilesystemRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
