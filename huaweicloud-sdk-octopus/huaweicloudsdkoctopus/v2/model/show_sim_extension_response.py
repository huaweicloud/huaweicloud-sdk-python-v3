# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSimExtensionResponse(SdkResponse):

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
        'file': 'FileRetrieveSrlz',
        'name': 'str',
        'description': 'str',
        'filename': 'str',
        'mount_path': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'file': 'file',
        'name': 'name',
        'description': 'description',
        'filename': 'filename',
        'mount_path': 'mount_path'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, status=None, file=None, name=None, description=None, filename=None, mount_path=None):
        r"""ShowSimExtensionResponse

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
        :param file: 
        :type file: :class:`huaweicloudsdkoctopus.v2.FileRetrieveSrlz`
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param filename: 文件名称
        :type filename: str
        :param mount_path: 加载路径
        :type mount_path: str
        """
        
        super(ShowSimExtensionResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._file = None
        self._name = None
        self._description = None
        self._filename = None
        self._mount_path = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if file is not None:
            self.file = file
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if filename is not None:
            self.filename = filename
        if mount_path is not None:
            self.mount_path = mount_path

    @property
    def url(self):
        r"""Gets the url of this ShowSimExtensionResponse.

        :return: The url of this ShowSimExtensionResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowSimExtensionResponse.

        :param url: The url of this ShowSimExtensionResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this ShowSimExtensionResponse.

        :return: The id of this ShowSimExtensionResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSimExtensionResponse.

        :param id: The id of this ShowSimExtensionResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowSimExtensionResponse.

        :return: The created_at of this ShowSimExtensionResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowSimExtensionResponse.

        :param created_at: The created_at of this ShowSimExtensionResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowSimExtensionResponse.

        :return: The updated_at of this ShowSimExtensionResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowSimExtensionResponse.

        :param updated_at: The updated_at of this ShowSimExtensionResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def status(self):
        r"""Gets the status of this ShowSimExtensionResponse.

        :return: The status of this ShowSimExtensionResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSimExtensionResponse.

        :param status: The status of this ShowSimExtensionResponse.
        :type status: int
        """
        self._status = status

    @property
    def file(self):
        r"""Gets the file of this ShowSimExtensionResponse.

        :return: The file of this ShowSimExtensionResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.FileRetrieveSrlz`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ShowSimExtensionResponse.

        :param file: The file of this ShowSimExtensionResponse.
        :type file: :class:`huaweicloudsdkoctopus.v2.FileRetrieveSrlz`
        """
        self._file = file

    @property
    def name(self):
        r"""Gets the name of this ShowSimExtensionResponse.

        名称

        :return: The name of this ShowSimExtensionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowSimExtensionResponse.

        名称

        :param name: The name of this ShowSimExtensionResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowSimExtensionResponse.

        描述

        :return: The description of this ShowSimExtensionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowSimExtensionResponse.

        描述

        :param description: The description of this ShowSimExtensionResponse.
        :type description: str
        """
        self._description = description

    @property
    def filename(self):
        r"""Gets the filename of this ShowSimExtensionResponse.

        文件名称

        :return: The filename of this ShowSimExtensionResponse.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this ShowSimExtensionResponse.

        文件名称

        :param filename: The filename of this ShowSimExtensionResponse.
        :type filename: str
        """
        self._filename = filename

    @property
    def mount_path(self):
        r"""Gets the mount_path of this ShowSimExtensionResponse.

        加载路径

        :return: The mount_path of this ShowSimExtensionResponse.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this ShowSimExtensionResponse.

        加载路径

        :param mount_path: The mount_path of this ShowSimExtensionResponse.
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
        if not isinstance(other, ShowSimExtensionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
