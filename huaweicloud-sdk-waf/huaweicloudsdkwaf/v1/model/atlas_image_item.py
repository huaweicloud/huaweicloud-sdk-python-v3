# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtlasImageItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'name': 'str',
        'url': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'image_id': 'image_id',
        'name': 'name',
        'url': 'url',
        'create_time': 'create_time'
    }

    def __init__(self, image_id=None, name=None, url=None, create_time=None):
        r"""AtlasImageItem

        The model defined in huaweicloud sdk

        :param image_id: 图片ID
        :type image_id: str
        :param name: 图片名称
        :type name: str
        :param url: 图片查看的预签名下载地址（GET）
        :type url: str
        :param create_time: 图片创建时间（毫秒时间戳）
        :type create_time: int
        """
        
        

        self._image_id = None
        self._name = None
        self._url = None
        self._create_time = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if create_time is not None:
            self.create_time = create_time

    @property
    def image_id(self):
        r"""Gets the image_id of this AtlasImageItem.

        图片ID

        :return: The image_id of this AtlasImageItem.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this AtlasImageItem.

        图片ID

        :param image_id: The image_id of this AtlasImageItem.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def name(self):
        r"""Gets the name of this AtlasImageItem.

        图片名称

        :return: The name of this AtlasImageItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AtlasImageItem.

        图片名称

        :param name: The name of this AtlasImageItem.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        r"""Gets the url of this AtlasImageItem.

        图片查看的预签名下载地址（GET）

        :return: The url of this AtlasImageItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AtlasImageItem.

        图片查看的预签名下载地址（GET）

        :param url: The url of this AtlasImageItem.
        :type url: str
        """
        self._url = url

    @property
    def create_time(self):
        r"""Gets the create_time of this AtlasImageItem.

        图片创建时间（毫秒时间戳）

        :return: The create_time of this AtlasImageItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AtlasImageItem.

        图片创建时间（毫秒时间戳）

        :param create_time: The create_time of this AtlasImageItem.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, AtlasImageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
