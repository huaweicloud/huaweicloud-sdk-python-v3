# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSimSmScenariosFilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'sha256': 'str',
        'created_at': 'float',
        'updated_at': 'float',
        'post': 'PostResponse',
        'put_url': 'str',
        'get_url': 'str',
        'expire': 'int',
        'ready': 'bool',
        'filename': 'str'
    }

    attribute_map = {
        'url': 'url',
        'sha256': 'sha256',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'post': 'post',
        'put_url': 'put_url',
        'get_url': 'get_url',
        'expire': 'expire',
        'ready': 'ready',
        'filename': 'filename'
    }

    def __init__(self, url=None, sha256=None, created_at=None, updated_at=None, post=None, put_url=None, get_url=None, expire=None, ready=None, filename=None):
        """CreateSimSmScenariosFilesResponse

        The model defined in huaweicloud sdk

        :param url: 地址
        :type url: str
        :param sha256: 文件sha256值
        :type sha256: str
        :param created_at: 创建时间
        :type created_at: float
        :param updated_at: 更新时间
        :type updated_at: float
        :param post: POST地址
        :type post: :class:`huaweicloudsdkoctopus.v2.PostResponse`
        :param put_url: PUT地址
        :type put_url: str
        :param get_url: GET地址
        :type get_url: str
        :param expire: 默认失效时间为600秒.
        :type expire: int
        :param ready: 状态
        :type ready: bool
        :param filename: 文件名
        :type filename: str
        """
        
        super(CreateSimSmScenariosFilesResponse, self).__init__()

        self._url = None
        self._sha256 = None
        self._created_at = None
        self._updated_at = None
        self._post = None
        self._put_url = None
        self._get_url = None
        self._expire = None
        self._ready = None
        self._filename = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if sha256 is not None:
            self.sha256 = sha256
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if post is not None:
            self.post = post
        if put_url is not None:
            self.put_url = put_url
        if get_url is not None:
            self.get_url = get_url
        if expire is not None:
            self.expire = expire
        if ready is not None:
            self.ready = ready
        if filename is not None:
            self.filename = filename

    @property
    def url(self):
        """Gets the url of this CreateSimSmScenariosFilesResponse.

        地址

        :return: The url of this CreateSimSmScenariosFilesResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateSimSmScenariosFilesResponse.

        地址

        :param url: The url of this CreateSimSmScenariosFilesResponse.
        :type url: str
        """
        self._url = url

    @property
    def sha256(self):
        """Gets the sha256 of this CreateSimSmScenariosFilesResponse.

        文件sha256值

        :return: The sha256 of this CreateSimSmScenariosFilesResponse.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this CreateSimSmScenariosFilesResponse.

        文件sha256值

        :param sha256: The sha256 of this CreateSimSmScenariosFilesResponse.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def created_at(self):
        """Gets the created_at of this CreateSimSmScenariosFilesResponse.

        创建时间

        :return: The created_at of this CreateSimSmScenariosFilesResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateSimSmScenariosFilesResponse.

        创建时间

        :param created_at: The created_at of this CreateSimSmScenariosFilesResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateSimSmScenariosFilesResponse.

        更新时间

        :return: The updated_at of this CreateSimSmScenariosFilesResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateSimSmScenariosFilesResponse.

        更新时间

        :param updated_at: The updated_at of this CreateSimSmScenariosFilesResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def post(self):
        """Gets the post of this CreateSimSmScenariosFilesResponse.

        POST地址

        :return: The post of this CreateSimSmScenariosFilesResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.PostResponse`
        """
        return self._post

    @post.setter
    def post(self, post):
        """Sets the post of this CreateSimSmScenariosFilesResponse.

        POST地址

        :param post: The post of this CreateSimSmScenariosFilesResponse.
        :type post: :class:`huaweicloudsdkoctopus.v2.PostResponse`
        """
        self._post = post

    @property
    def put_url(self):
        """Gets the put_url of this CreateSimSmScenariosFilesResponse.

        PUT地址

        :return: The put_url of this CreateSimSmScenariosFilesResponse.
        :rtype: str
        """
        return self._put_url

    @put_url.setter
    def put_url(self, put_url):
        """Sets the put_url of this CreateSimSmScenariosFilesResponse.

        PUT地址

        :param put_url: The put_url of this CreateSimSmScenariosFilesResponse.
        :type put_url: str
        """
        self._put_url = put_url

    @property
    def get_url(self):
        """Gets the get_url of this CreateSimSmScenariosFilesResponse.

        GET地址

        :return: The get_url of this CreateSimSmScenariosFilesResponse.
        :rtype: str
        """
        return self._get_url

    @get_url.setter
    def get_url(self, get_url):
        """Sets the get_url of this CreateSimSmScenariosFilesResponse.

        GET地址

        :param get_url: The get_url of this CreateSimSmScenariosFilesResponse.
        :type get_url: str
        """
        self._get_url = get_url

    @property
    def expire(self):
        """Gets the expire of this CreateSimSmScenariosFilesResponse.

        默认失效时间为600秒.

        :return: The expire of this CreateSimSmScenariosFilesResponse.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this CreateSimSmScenariosFilesResponse.

        默认失效时间为600秒.

        :param expire: The expire of this CreateSimSmScenariosFilesResponse.
        :type expire: int
        """
        self._expire = expire

    @property
    def ready(self):
        """Gets the ready of this CreateSimSmScenariosFilesResponse.

        状态

        :return: The ready of this CreateSimSmScenariosFilesResponse.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this CreateSimSmScenariosFilesResponse.

        状态

        :param ready: The ready of this CreateSimSmScenariosFilesResponse.
        :type ready: bool
        """
        self._ready = ready

    @property
    def filename(self):
        """Gets the filename of this CreateSimSmScenariosFilesResponse.

        文件名

        :return: The filename of this CreateSimSmScenariosFilesResponse.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this CreateSimSmScenariosFilesResponse.

        文件名

        :param filename: The filename of this CreateSimSmScenariosFilesResponse.
        :type filename: str
        """
        self._filename = filename

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
        if not isinstance(other, CreateSimSmScenariosFilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
