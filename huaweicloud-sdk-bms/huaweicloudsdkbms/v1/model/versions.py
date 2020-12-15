# coding: utf-8

import pprint
import re

import six





class Versions:


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
        'links': 'list[VersionLinks]',
        'min_version': 'str',
        'status': 'str',
        'version': 'str',
        'updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'min_version': 'min_version',
        'status': 'status',
        'version': 'version',
        'updated': 'updated'
    }

    def __init__(self, id=None, links=None, min_version=None, status=None, version=None, updated=None):
        """Versions - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._links = None
        self._min_version = None
        self._status = None
        self._version = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if min_version is not None:
            self.min_version = min_version
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this Versions.

        API版本ID

        :return: The id of this Versions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Versions.

        API版本ID

        :param id: The id of this Versions.
        :type: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this Versions.

        API的url地址

        :return: The links of this Versions.
        :rtype: list[VersionLinks]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Versions.

        API的url地址

        :param links: The links of this Versions.
        :type: list[VersionLinks]
        """
        self._links = links

    @property
    def min_version(self):
        """Gets the min_version of this Versions.

        API支持的最小微版本号

        :return: The min_version of this Versions.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this Versions.

        API支持的最小微版本号

        :param min_version: The min_version of this Versions.
        :type: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this Versions.

        这个是API版本的状态。可以是：CURRENT这是使用的API的首选版本；SUPPORTED：这是一个较老的，但仍然支持的API版本；DEPRECATED：一个被废弃的API版本，该版本将被删除

        :return: The status of this Versions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Versions.

        这个是API版本的状态。可以是：CURRENT这是使用的API的首选版本；SUPPORTED：这是一个较老的，但仍然支持的API版本；DEPRECATED：一个被废弃的API版本，该版本将被删除

        :param status: The status of this Versions.
        :type: str
        """
        self._status = status

    @property
    def version(self):
        """Gets the version of this Versions.

        API支持的最大微版本号

        :return: The version of this Versions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Versions.

        API支持的最大微版本号

        :param version: The version of this Versions.
        :type: str
        """
        self._version = version

    @property
    def updated(self):
        """Gets the updated of this Versions.

        API版本发布时间

        :return: The updated of this Versions.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Versions.

        API版本发布时间

        :param updated: The updated of this Versions.
        :type: datetime
        """
        self._updated = updated

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
        if not isinstance(other, Versions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
