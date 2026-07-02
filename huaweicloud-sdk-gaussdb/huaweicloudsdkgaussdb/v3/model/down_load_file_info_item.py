# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownLoadFileInfoItem:

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
        'file_size': 'int',
        'download_url': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'file_size': 'file_size',
        'download_url': 'download_url',
        'expire_time': 'expire_time'
    }

    def __init__(self, id=None, file_name=None, file_size=None, download_url=None, expire_time=None):
        r"""DownLoadFileInfoItem

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  日志文件ID。  **取值范围**：  不涉及。 
        :type id: str
        :param file_name: **参数解释**：  日志文件名称。  **取值范围**：  不涉及。 
        :type file_name: str
        :param file_size: **参数解释**：  日志文件大小，单位为字节。  **取值范围**：  不涉及。 
        :type file_size: int
        :param download_url: **参数解释**：  日志下载链接。  **取值范围**：  不涉及。 
        :type download_url: str
        :param expire_time: **参数解释**：  下载链接过期时间，格式为\&quot;yyyy-MM-dd HH:mm:ss\&quot;。  **取值范围**：  不涉及。 
        :type expire_time: str
        """
        
        

        self._id = None
        self._file_name = None
        self._file_size = None
        self._download_url = None
        self._expire_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if download_url is not None:
            self.download_url = download_url
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def id(self):
        r"""Gets the id of this DownLoadFileInfoItem.

        **参数解释**：  日志文件ID。  **取值范围**：  不涉及。 

        :return: The id of this DownLoadFileInfoItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DownLoadFileInfoItem.

        **参数解释**：  日志文件ID。  **取值范围**：  不涉及。 

        :param id: The id of this DownLoadFileInfoItem.
        :type id: str
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this DownLoadFileInfoItem.

        **参数解释**：  日志文件名称。  **取值范围**：  不涉及。 

        :return: The file_name of this DownLoadFileInfoItem.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DownLoadFileInfoItem.

        **参数解释**：  日志文件名称。  **取值范围**：  不涉及。 

        :param file_name: The file_name of this DownLoadFileInfoItem.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        r"""Gets the file_size of this DownLoadFileInfoItem.

        **参数解释**：  日志文件大小，单位为字节。  **取值范围**：  不涉及。 

        :return: The file_size of this DownLoadFileInfoItem.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this DownLoadFileInfoItem.

        **参数解释**：  日志文件大小，单位为字节。  **取值范围**：  不涉及。 

        :param file_size: The file_size of this DownLoadFileInfoItem.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def download_url(self):
        r"""Gets the download_url of this DownLoadFileInfoItem.

        **参数解释**：  日志下载链接。  **取值范围**：  不涉及。 

        :return: The download_url of this DownLoadFileInfoItem.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this DownLoadFileInfoItem.

        **参数解释**：  日志下载链接。  **取值范围**：  不涉及。 

        :param download_url: The download_url of this DownLoadFileInfoItem.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def expire_time(self):
        r"""Gets the expire_time of this DownLoadFileInfoItem.

        **参数解释**：  下载链接过期时间，格式为\"yyyy-MM-dd HH:mm:ss\"。  **取值范围**：  不涉及。 

        :return: The expire_time of this DownLoadFileInfoItem.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this DownLoadFileInfoItem.

        **参数解释**：  下载链接过期时间，格式为\"yyyy-MM-dd HH:mm:ss\"。  **取值范围**：  不涉及。 

        :param expire_time: The expire_time of this DownLoadFileInfoItem.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, DownLoadFileInfoItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
