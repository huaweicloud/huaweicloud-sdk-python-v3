# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TreeObjectDto:

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
        'name': 'str',
        'type': 'str',
        'path': 'str',
        'mode': 'str',
        'submodule_link': 'str',
        'submodule_branch': 'str',
        'md5': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'path': 'path',
        'mode': 'mode',
        'submodule_link': 'submodule_link',
        'submodule_branch': 'submodule_branch',
        'md5': 'md5'
    }

    def __init__(self, id=None, name=None, type=None, path=None, mode=None, submodule_link=None, submodule_branch=None, md5=None):
        r"""TreeObjectDto

        The model defined in huaweicloud sdk

        :param id: 文件唯一标识
        :type id: str
        :param name: 文件名称
        :type name: str
        :param type: 对象类型
        :type type: str
        :param path: 文件路径
        :type path: str
        :param mode: 模式结构
        :type mode: str
        :param submodule_link: 子模块链接
        :type submodule_link: str
        :param submodule_branch: 子模块分支
        :type submodule_branch: str
        :param md5: md5值
        :type md5: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._path = None
        self._mode = None
        self._submodule_link = None
        self._submodule_branch = None
        self._md5 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if mode is not None:
            self.mode = mode
        if submodule_link is not None:
            self.submodule_link = submodule_link
        if submodule_branch is not None:
            self.submodule_branch = submodule_branch
        if md5 is not None:
            self.md5 = md5

    @property
    def id(self):
        r"""Gets the id of this TreeObjectDto.

        文件唯一标识

        :return: The id of this TreeObjectDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TreeObjectDto.

        文件唯一标识

        :param id: The id of this TreeObjectDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TreeObjectDto.

        文件名称

        :return: The name of this TreeObjectDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TreeObjectDto.

        文件名称

        :param name: The name of this TreeObjectDto.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this TreeObjectDto.

        对象类型

        :return: The type of this TreeObjectDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TreeObjectDto.

        对象类型

        :param type: The type of this TreeObjectDto.
        :type type: str
        """
        self._type = type

    @property
    def path(self):
        r"""Gets the path of this TreeObjectDto.

        文件路径

        :return: The path of this TreeObjectDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this TreeObjectDto.

        文件路径

        :param path: The path of this TreeObjectDto.
        :type path: str
        """
        self._path = path

    @property
    def mode(self):
        r"""Gets the mode of this TreeObjectDto.

        模式结构

        :return: The mode of this TreeObjectDto.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this TreeObjectDto.

        模式结构

        :param mode: The mode of this TreeObjectDto.
        :type mode: str
        """
        self._mode = mode

    @property
    def submodule_link(self):
        r"""Gets the submodule_link of this TreeObjectDto.

        子模块链接

        :return: The submodule_link of this TreeObjectDto.
        :rtype: str
        """
        return self._submodule_link

    @submodule_link.setter
    def submodule_link(self, submodule_link):
        r"""Sets the submodule_link of this TreeObjectDto.

        子模块链接

        :param submodule_link: The submodule_link of this TreeObjectDto.
        :type submodule_link: str
        """
        self._submodule_link = submodule_link

    @property
    def submodule_branch(self):
        r"""Gets the submodule_branch of this TreeObjectDto.

        子模块分支

        :return: The submodule_branch of this TreeObjectDto.
        :rtype: str
        """
        return self._submodule_branch

    @submodule_branch.setter
    def submodule_branch(self, submodule_branch):
        r"""Sets the submodule_branch of this TreeObjectDto.

        子模块分支

        :param submodule_branch: The submodule_branch of this TreeObjectDto.
        :type submodule_branch: str
        """
        self._submodule_branch = submodule_branch

    @property
    def md5(self):
        r"""Gets the md5 of this TreeObjectDto.

        md5值

        :return: The md5 of this TreeObjectDto.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        r"""Sets the md5 of this TreeObjectDto.

        md5值

        :param md5: The md5 of this TreeObjectDto.
        :type md5: str
        """
        self._md5 = md5

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
        if not isinstance(other, TreeObjectDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
