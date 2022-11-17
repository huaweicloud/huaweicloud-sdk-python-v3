# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataResponse(SdkResponse):

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
        'download_url': 'str',
        'allowed_operate': 'bool'
    }

    attribute_map = {
        'path': 'path',
        'name': 'name',
        'type': 'type',
        'size': 'size',
        'create_time': 'create_time',
        'download_url': 'download_url',
        'allowed_operate': 'allowed_operate'
    }

    def __init__(self, path=None, name=None, type=None, size=None, create_time=None, download_url=None, allowed_operate=None):
        """ShowDataResponse

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
        :param allowed_operate: 可操作标记
        :type allowed_operate: bool
        """
        
        super(ShowDataResponse, self).__init__()

        self._path = None
        self._name = None
        self._type = None
        self._size = None
        self._create_time = None
        self._download_url = None
        self._allowed_operate = None
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
        if allowed_operate is not None:
            self.allowed_operate = allowed_operate

    @property
    def path(self):
        """Gets the path of this ShowDataResponse.

        对象全路径（项目名称:/路径）

        :return: The path of this ShowDataResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowDataResponse.

        对象全路径（项目名称:/路径）

        :param path: The path of this ShowDataResponse.
        :type path: str
        """
        self._path = path

    @property
    def name(self):
        """Gets the name of this ShowDataResponse.

        名称

        :return: The name of this ShowDataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDataResponse.

        名称

        :param name: The name of this ShowDataResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ShowDataResponse.

        :return: The type of this ShowDataResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PathType`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowDataResponse.

        :param type: The type of this ShowDataResponse.
        :type type: :class:`huaweicloudsdkeihealth.v1.PathType`
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this ShowDataResponse.

        大小

        :return: The size of this ShowDataResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowDataResponse.

        大小

        :param size: The size of this ShowDataResponse.
        :type size: int
        """
        self._size = size

    @property
    def create_time(self):
        """Gets the create_time of this ShowDataResponse.

        创建时间

        :return: The create_time of this ShowDataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDataResponse.

        创建时间

        :param create_time: The create_time of this ShowDataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def download_url(self):
        """Gets the download_url of this ShowDataResponse.

        下载链接

        :return: The download_url of this ShowDataResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this ShowDataResponse.

        下载链接

        :param download_url: The download_url of this ShowDataResponse.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def allowed_operate(self):
        """Gets the allowed_operate of this ShowDataResponse.

        可操作标记

        :return: The allowed_operate of this ShowDataResponse.
        :rtype: bool
        """
        return self._allowed_operate

    @allowed_operate.setter
    def allowed_operate(self, allowed_operate):
        """Sets the allowed_operate of this ShowDataResponse.

        可操作标记

        :param allowed_operate: The allowed_operate of this ShowDataResponse.
        :type allowed_operate: bool
        """
        self._allowed_operate = allowed_operate

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
        if not isinstance(other, ShowDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
