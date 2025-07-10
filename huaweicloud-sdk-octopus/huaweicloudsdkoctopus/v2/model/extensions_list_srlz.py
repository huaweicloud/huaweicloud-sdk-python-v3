# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionsListSrlz:

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
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'status': 'int',
        'name': 'str',
        'filename': 'str',
        'mount_path': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'name': 'name',
        'filename': 'filename',
        'mount_path': 'mount_path'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, status=None, name=None, filename=None, mount_path=None):
        r"""ExtensionsListSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param status: 
        :type status: int
        :param name: 名称
        :type name: str
        :param filename: 文件名称
        :type filename: str
        :param mount_path: 加载路径
        :type mount_path: str
        """
        
        

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._name = None
        self._filename = None
        self._mount_path = None
        self.discriminator = None

        self.url = url
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status
        self.name = name
        if filename is not None:
            self.filename = filename
        self.mount_path = mount_path

    @property
    def url(self):
        r"""Gets the url of this ExtensionsListSrlz.

        :return: The url of this ExtensionsListSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ExtensionsListSrlz.

        :param url: The url of this ExtensionsListSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this ExtensionsListSrlz.

        :return: The id of this ExtensionsListSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExtensionsListSrlz.

        :param id: The id of this ExtensionsListSrlz.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ExtensionsListSrlz.

        :return: The created_at of this ExtensionsListSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ExtensionsListSrlz.

        :param created_at: The created_at of this ExtensionsListSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ExtensionsListSrlz.

        :return: The updated_at of this ExtensionsListSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ExtensionsListSrlz.

        :param updated_at: The updated_at of this ExtensionsListSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def status(self):
        r"""Gets the status of this ExtensionsListSrlz.

        :return: The status of this ExtensionsListSrlz.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExtensionsListSrlz.

        :param status: The status of this ExtensionsListSrlz.
        :type status: int
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ExtensionsListSrlz.

        名称

        :return: The name of this ExtensionsListSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtensionsListSrlz.

        名称

        :param name: The name of this ExtensionsListSrlz.
        :type name: str
        """
        self._name = name

    @property
    def filename(self):
        r"""Gets the filename of this ExtensionsListSrlz.

        文件名称

        :return: The filename of this ExtensionsListSrlz.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this ExtensionsListSrlz.

        文件名称

        :param filename: The filename of this ExtensionsListSrlz.
        :type filename: str
        """
        self._filename = filename

    @property
    def mount_path(self):
        r"""Gets the mount_path of this ExtensionsListSrlz.

        加载路径

        :return: The mount_path of this ExtensionsListSrlz.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this ExtensionsListSrlz.

        加载路径

        :param mount_path: The mount_path of this ExtensionsListSrlz.
        :type mount_path: str
        """
        self._mount_path = mount_path

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
        if not isinstance(other, ExtensionsListSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
