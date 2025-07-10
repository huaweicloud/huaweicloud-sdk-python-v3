# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionsCreateSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'mount_path': 'str',
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'file': 'FileCreateSrlz'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'mount_path': 'mount_path',
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'file': 'file'
    }

    def __init__(self, name=None, description=None, mount_path=None, url=None, id=None, created_at=None, updated_at=None, file=None):
        r"""ExtensionsCreateSrlz

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param mount_path: 挂载路径
        :type mount_path: str
        :param url: 扩展文件资源地址。
        :type url: str
        :param id: 扩展文件ID。
        :type id: int
        :param created_at: 创建时间。
        :type created_at: float
        :param updated_at: 更新时间。
        :type updated_at: float
        :param file: 
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        """
        
        

        self._name = None
        self._description = None
        self._mount_path = None
        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._file = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.mount_path = mount_path
        self.url = url
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.file = file

    @property
    def name(self):
        r"""Gets the name of this ExtensionsCreateSrlz.

        名称

        :return: The name of this ExtensionsCreateSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtensionsCreateSrlz.

        名称

        :param name: The name of this ExtensionsCreateSrlz.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ExtensionsCreateSrlz.

        描述

        :return: The description of this ExtensionsCreateSrlz.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExtensionsCreateSrlz.

        描述

        :param description: The description of this ExtensionsCreateSrlz.
        :type description: str
        """
        self._description = description

    @property
    def mount_path(self):
        r"""Gets the mount_path of this ExtensionsCreateSrlz.

        挂载路径

        :return: The mount_path of this ExtensionsCreateSrlz.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this ExtensionsCreateSrlz.

        挂载路径

        :param mount_path: The mount_path of this ExtensionsCreateSrlz.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def url(self):
        r"""Gets the url of this ExtensionsCreateSrlz.

        扩展文件资源地址。

        :return: The url of this ExtensionsCreateSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ExtensionsCreateSrlz.

        扩展文件资源地址。

        :param url: The url of this ExtensionsCreateSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this ExtensionsCreateSrlz.

        扩展文件ID。

        :return: The id of this ExtensionsCreateSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExtensionsCreateSrlz.

        扩展文件ID。

        :param id: The id of this ExtensionsCreateSrlz.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ExtensionsCreateSrlz.

        创建时间。

        :return: The created_at of this ExtensionsCreateSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ExtensionsCreateSrlz.

        创建时间。

        :param created_at: The created_at of this ExtensionsCreateSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ExtensionsCreateSrlz.

        更新时间。

        :return: The updated_at of this ExtensionsCreateSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ExtensionsCreateSrlz.

        更新时间。

        :param updated_at: The updated_at of this ExtensionsCreateSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def file(self):
        r"""Gets the file of this ExtensionsCreateSrlz.

        :return: The file of this ExtensionsCreateSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ExtensionsCreateSrlz.

        :param file: The file of this ExtensionsCreateSrlz.
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        """
        self._file = file

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
        if not isinstance(other, ExtensionsCreateSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
