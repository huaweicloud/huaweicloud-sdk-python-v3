# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdpMetadataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'file_name': 'str',
        'content': 'str',
        'content_length': 'float',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'content': 'content',
        'content_length': 'content_length',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, file_name=None, content=None, content_length=None, create_time=None, update_time=None):
        r"""IdpMetadataInfo

        The model defined in huaweicloud sdk

        :param id: IDP元数据id。
        :type id: str
        :param file_name: IDP元数据文件名称。
        :type file_name: str
        :param content: IDP元数据内容（base64）。
        :type content: str
        :param content_length: 元数据大小（字节数），最大1M。
        :type content_length: float
        :param create_time: 创建时间戳。
        :type create_time: int
        :param update_time: 更新时间戳。
        :type update_time: int
        """
        
        

        self._id = None
        self._file_name = None
        self._content = None
        self._content_length = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if content is not None:
            self.content = content
        if content_length is not None:
            self.content_length = content_length
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this IdpMetadataInfo.

        IDP元数据id。

        :return: The id of this IdpMetadataInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IdpMetadataInfo.

        IDP元数据id。

        :param id: The id of this IdpMetadataInfo.
        :type id: str
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this IdpMetadataInfo.

        IDP元数据文件名称。

        :return: The file_name of this IdpMetadataInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this IdpMetadataInfo.

        IDP元数据文件名称。

        :param file_name: The file_name of this IdpMetadataInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def content(self):
        r"""Gets the content of this IdpMetadataInfo.

        IDP元数据内容（base64）。

        :return: The content of this IdpMetadataInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this IdpMetadataInfo.

        IDP元数据内容（base64）。

        :param content: The content of this IdpMetadataInfo.
        :type content: str
        """
        self._content = content

    @property
    def content_length(self):
        r"""Gets the content_length of this IdpMetadataInfo.

        元数据大小（字节数），最大1M。

        :return: The content_length of this IdpMetadataInfo.
        :rtype: float
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this IdpMetadataInfo.

        元数据大小（字节数），最大1M。

        :param content_length: The content_length of this IdpMetadataInfo.
        :type content_length: float
        """
        self._content_length = content_length

    @property
    def create_time(self):
        r"""Gets the create_time of this IdpMetadataInfo.

        创建时间戳。

        :return: The create_time of this IdpMetadataInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this IdpMetadataInfo.

        创建时间戳。

        :param create_time: The create_time of this IdpMetadataInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this IdpMetadataInfo.

        更新时间戳。

        :return: The update_time of this IdpMetadataInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this IdpMetadataInfo.

        更新时间戳。

        :param update_time: The update_time of this IdpMetadataInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, IdpMetadataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
