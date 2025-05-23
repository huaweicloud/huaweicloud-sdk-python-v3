# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectTraceDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'name': 'str',
        'type': 'PathType',
        'size': 'int',
        'create_time': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'path': 'path',
        'name': 'name',
        'type': 'type',
        'size': 'size',
        'create_time': 'create_time',
        'download_url': 'download_url'
    }

    def __init__(self, path=None, name=None, type=None, size=None, create_time=None, download_url=None):
        r"""ShowProjectTraceDataResponse

        The model defined in huaweicloud sdk

        :param path: 对象全路径（项目名称:/路径）
        :type path: str
        :param name: 名称
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.PathType`
        :param size: 大小
        :type size: int
        :param create_time: 创建时间
        :type create_time: str
        :param download_url: 下载链接
        :type download_url: str
        """
        
        super(ShowProjectTraceDataResponse, self).__init__()

        self._path = None
        self._name = None
        self._type = None
        self._size = None
        self._create_time = None
        self._download_url = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if create_time is not None:
            self.create_time = create_time
        if download_url is not None:
            self.download_url = download_url

    @property
    def path(self):
        r"""Gets the path of this ShowProjectTraceDataResponse.

        对象全路径（项目名称:/路径）

        :return: The path of this ShowProjectTraceDataResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowProjectTraceDataResponse.

        对象全路径（项目名称:/路径）

        :param path: The path of this ShowProjectTraceDataResponse.
        :type path: str
        """
        self._path = path

    @property
    def name(self):
        r"""Gets the name of this ShowProjectTraceDataResponse.

        名称

        :return: The name of this ShowProjectTraceDataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowProjectTraceDataResponse.

        名称

        :param name: The name of this ShowProjectTraceDataResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowProjectTraceDataResponse.

        :return: The type of this ShowProjectTraceDataResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PathType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowProjectTraceDataResponse.

        :param type: The type of this ShowProjectTraceDataResponse.
        :type type: :class:`huaweicloudsdkeihealth.v1.PathType`
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this ShowProjectTraceDataResponse.

        大小

        :return: The size of this ShowProjectTraceDataResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowProjectTraceDataResponse.

        大小

        :param size: The size of this ShowProjectTraceDataResponse.
        :type size: int
        """
        self._size = size

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowProjectTraceDataResponse.

        创建时间

        :return: The create_time of this ShowProjectTraceDataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowProjectTraceDataResponse.

        创建时间

        :param create_time: The create_time of this ShowProjectTraceDataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def download_url(self):
        r"""Gets the download_url of this ShowProjectTraceDataResponse.

        下载链接

        :return: The download_url of this ShowProjectTraceDataResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this ShowProjectTraceDataResponse.

        下载链接

        :param download_url: The download_url of this ShowProjectTraceDataResponse.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, ShowProjectTraceDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
