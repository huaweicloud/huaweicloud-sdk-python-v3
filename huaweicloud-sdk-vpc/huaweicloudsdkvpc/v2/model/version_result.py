# coding: utf-8

import pprint
import re

import six


class VersionResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'status': 'str',
        'id': 'str',
        'links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'links': 'links'
    }

    def __init__(self, status=None, id=None, links=None):  # noqa: E501
        """VersionResult - a model defined in huaweicloud sdk"""

        self._status = None
        self._id = None
        self._links = None
        self.discriminator = None

        self.status = status
        self.id = id
        self.links = links

    @property
    def status(self):
        """Gets the status of this VersionResult.

        API版本的状态：  - CURRENT（当前版本）  - STABLE（稳定版本）  - DEPRECATED（废弃版本）

        :return: The status of this VersionResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VersionResult.

        API版本的状态：  - CURRENT（当前版本）  - STABLE（稳定版本）  - DEPRECATED（废弃版本）

        :param status: The status of this VersionResult.
        :type: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this VersionResult.

        API版本

        :return: The id of this VersionResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionResult.

        API版本

        :param id: The id of this VersionResult.
        :type: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this VersionResult.

        链接列表

        :return: The links of this VersionResult.
        :rtype: list[NeutronPageLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VersionResult.

        链接列表

        :param links: The links of this VersionResult.
        :type: list[NeutronPageLink]
        """
        self._links = links

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
        if not isinstance(other, VersionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
