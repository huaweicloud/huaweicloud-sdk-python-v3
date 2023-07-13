# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetTagDetailRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag': 'str',
        'size': 'int',
        'create_time': 'str',
        'update_time': 'str',
        'path': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'size': 'size',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'path': 'path'
    }

    def __init__(self, tag=None, size=None, create_time=None, update_time=None, path=None):
        """GetTagDetailRsp

        The model defined in huaweicloud sdk

        :param tag: 镜像版本名称
        :type tag: str
        :param size: 镜像版本大小
        :type size: int
        :param create_time: 镜像版本创建时间
        :type create_time: str
        :param update_time: 镜像版本更新时间
        :type update_time: str
        :param path: 镜像地址
        :type path: str
        """
        
        

        self._tag = None
        self._size = None
        self._create_time = None
        self._update_time = None
        self._path = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if size is not None:
            self.size = size
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if path is not None:
            self.path = path

    @property
    def tag(self):
        """Gets the tag of this GetTagDetailRsp.

        镜像版本名称

        :return: The tag of this GetTagDetailRsp.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this GetTagDetailRsp.

        镜像版本名称

        :param tag: The tag of this GetTagDetailRsp.
        :type tag: str
        """
        self._tag = tag

    @property
    def size(self):
        """Gets the size of this GetTagDetailRsp.

        镜像版本大小

        :return: The size of this GetTagDetailRsp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this GetTagDetailRsp.

        镜像版本大小

        :param size: The size of this GetTagDetailRsp.
        :type size: int
        """
        self._size = size

    @property
    def create_time(self):
        """Gets the create_time of this GetTagDetailRsp.

        镜像版本创建时间

        :return: The create_time of this GetTagDetailRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetTagDetailRsp.

        镜像版本创建时间

        :param create_time: The create_time of this GetTagDetailRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this GetTagDetailRsp.

        镜像版本更新时间

        :return: The update_time of this GetTagDetailRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetTagDetailRsp.

        镜像版本更新时间

        :param update_time: The update_time of this GetTagDetailRsp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def path(self):
        """Gets the path of this GetTagDetailRsp.

        镜像地址

        :return: The path of this GetTagDetailRsp.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this GetTagDetailRsp.

        镜像地址

        :param path: The path of this GetTagDetailRsp.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, GetTagDetailRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
