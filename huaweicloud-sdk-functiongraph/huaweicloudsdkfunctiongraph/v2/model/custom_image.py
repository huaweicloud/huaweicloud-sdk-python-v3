# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomImage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'image': 'str',
        'command': 'str',
        'args': 'str',
        'working_dir': 'str',
        'uid': 'str',
        'gid': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'image': 'image',
        'command': 'command',
        'args': 'args',
        'working_dir': 'working_dir',
        'uid': 'uid',
        'gid': 'gid'
    }

    def __init__(self, enabled=None, image=None, command=None, args=None, working_dir=None, uid=None, gid=None):
        """CustomImage

        The model defined in huaweicloud sdk

        :param enabled: 是否启用
        :type enabled: bool
        :param image: 镜像地址
        :type image: str
        :param command: 启动容器镜像的命令
        :type command: str
        :param args: 启动容器镜像的命令行参数
        :type args: str
        :param working_dir: 镜像容器工作目录
        :type working_dir: str
        :param uid: 镜像容器的用户id
        :type uid: str
        :param gid: 镜像容器的用户组id
        :type gid: str
        """
        
        

        self._enabled = None
        self._image = None
        self._command = None
        self._args = None
        self._working_dir = None
        self._uid = None
        self._gid = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if image is not None:
            self.image = image
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if working_dir is not None:
            self.working_dir = working_dir
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid

    @property
    def enabled(self):
        """Gets the enabled of this CustomImage.

        是否启用

        :return: The enabled of this CustomImage.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CustomImage.

        是否启用

        :param enabled: The enabled of this CustomImage.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def image(self):
        """Gets the image of this CustomImage.

        镜像地址

        :return: The image of this CustomImage.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CustomImage.

        镜像地址

        :param image: The image of this CustomImage.
        :type image: str
        """
        self._image = image

    @property
    def command(self):
        """Gets the command of this CustomImage.

        启动容器镜像的命令

        :return: The command of this CustomImage.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this CustomImage.

        启动容器镜像的命令

        :param command: The command of this CustomImage.
        :type command: str
        """
        self._command = command

    @property
    def args(self):
        """Gets the args of this CustomImage.

        启动容器镜像的命令行参数

        :return: The args of this CustomImage.
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this CustomImage.

        启动容器镜像的命令行参数

        :param args: The args of this CustomImage.
        :type args: str
        """
        self._args = args

    @property
    def working_dir(self):
        """Gets the working_dir of this CustomImage.

        镜像容器工作目录

        :return: The working_dir of this CustomImage.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this CustomImage.

        镜像容器工作目录

        :param working_dir: The working_dir of this CustomImage.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def uid(self):
        """Gets the uid of this CustomImage.

        镜像容器的用户id

        :return: The uid of this CustomImage.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CustomImage.

        镜像容器的用户id

        :param uid: The uid of this CustomImage.
        :type uid: str
        """
        self._uid = uid

    @property
    def gid(self):
        """Gets the gid of this CustomImage.

        镜像容器的用户组id

        :return: The gid of this CustomImage.
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this CustomImage.

        镜像容器的用户组id

        :param gid: The gid of this CustomImage.
        :type gid: str
        """
        self._gid = gid

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
        if not isinstance(other, CustomImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
