# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateDependencyResponse(SdkResponse):


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
        'owner': 'str',
        'link': 'str',
        'runtime': 'str',
        'etag': 'str',
        'size': 'str',
        'name': 'str',
        'description': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'link': 'link',
        'runtime': 'runtime',
        'etag': 'etag',
        'size': 'size',
        'name': 'name',
        'description': 'description',
        'file_name': 'file_name'
    }

    def __init__(self, id=None, owner=None, link=None, runtime=None, etag=None, size=None, name=None, description=None, file_name=None):
        """CreateDependencyResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._id = None
        self._owner = None
        self._link = None
        self._runtime = None
        self._etag = None
        self._size = None
        self._name = None
        self._description = None
        self._file_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if link is not None:
            self.link = link
        if runtime is not None:
            self.runtime = runtime
        if etag is not None:
            self.etag = etag
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if file_name is not None:
            self.file_name = file_name

    @property
    def id(self):
        """Gets the id of this CreateDependencyResponse.

        依赖包ID。

        :return: The id of this CreateDependencyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateDependencyResponse.

        依赖包ID。

        :param id: The id of this CreateDependencyResponse.
        :type: str
        """
        self._id = id

    @property
    def owner(self):
        """Gets the owner of this CreateDependencyResponse.

        依赖包拥有者。

        :return: The owner of this CreateDependencyResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateDependencyResponse.

        依赖包拥有者。

        :param owner: The owner of this CreateDependencyResponse.
        :type: str
        """
        self._owner = owner

    @property
    def link(self):
        """Gets the link of this CreateDependencyResponse.

        依赖包在obs的存储地址。

        :return: The link of this CreateDependencyResponse.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this CreateDependencyResponse.

        依赖包在obs的存储地址。

        :param link: The link of this CreateDependencyResponse.
        :type: str
        """
        self._link = link

    @property
    def runtime(self):
        """Gets the runtime of this CreateDependencyResponse.

        运行时语言。

        :return: The runtime of this CreateDependencyResponse.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this CreateDependencyResponse.

        运行时语言。

        :param runtime: The runtime of this CreateDependencyResponse.
        :type: str
        """
        self._runtime = runtime

    @property
    def etag(self):
        """Gets the etag of this CreateDependencyResponse.

        依赖包唯一标志。

        :return: The etag of this CreateDependencyResponse.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this CreateDependencyResponse.

        依赖包唯一标志。

        :param etag: The etag of this CreateDependencyResponse.
        :type: str
        """
        self._etag = etag

    @property
    def size(self):
        """Gets the size of this CreateDependencyResponse.

        依赖包大小。

        :return: The size of this CreateDependencyResponse.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateDependencyResponse.

        依赖包大小。

        :param size: The size of this CreateDependencyResponse.
        :type: str
        """
        self._size = size

    @property
    def name(self):
        """Gets the name of this CreateDependencyResponse.

        依赖包名。

        :return: The name of this CreateDependencyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDependencyResponse.

        依赖包名。

        :param name: The name of this CreateDependencyResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateDependencyResponse.

        依赖包描述。

        :return: The description of this CreateDependencyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDependencyResponse.

        依赖包描述。

        :param description: The description of this CreateDependencyResponse.
        :type: str
        """
        self._description = description

    @property
    def file_name(self):
        """Gets the file_name of this CreateDependencyResponse.

        依赖包文件名。

        :return: The file_name of this CreateDependencyResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CreateDependencyResponse.

        依赖包文件名。

        :param file_name: The file_name of this CreateDependencyResponse.
        :type: str
        """
        self._file_name = file_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDependencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
