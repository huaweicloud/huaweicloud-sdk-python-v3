# coding: utf-8

import pprint
import re

import six





class DeleteStatus:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'added': 'int',
        'current_total': 'int',
        'deleted': 'int',
        'previous_total': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'added': 'added',
        'current_total': 'current_total',
        'deleted': 'deleted',
        'previous_total': 'previous_total',
        'updated': 'updated'
    }

    def __init__(self, added=None, current_total=None, deleted=None, previous_total=None, updated=None):
        """DeleteStatus - a model defined in huaweicloud sdk"""
        
        

        self._added = None
        self._current_total = None
        self._deleted = None
        self._previous_total = None
        self._updated = None
        self.discriminator = None

        if added is not None:
            self.added = added
        if current_total is not None:
            self.current_total = current_total
        if deleted is not None:
            self.deleted = deleted
        if previous_total is not None:
            self.previous_total = previous_total
        if updated is not None:
            self.updated = updated

    @property
    def added(self):
        """Gets the added of this DeleteStatus.

        集群删除时更新的资源记录总数

        :return: The added of this DeleteStatus.
        :rtype: int
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this DeleteStatus.

        集群删除时更新的资源记录总数

        :param added: The added of this DeleteStatus.
        :type: int
        """
        self._added = added

    @property
    def current_total(self):
        """Gets the current_total of this DeleteStatus.

        基于当前集群资源记录信息，生成实际最新资源记录总数

        :return: The current_total of this DeleteStatus.
        :rtype: int
        """
        return self._current_total

    @current_total.setter
    def current_total(self, current_total):
        """Sets the current_total of this DeleteStatus.

        基于当前集群资源记录信息，生成实际最新资源记录总数

        :param current_total: The current_total of this DeleteStatus.
        :type: int
        """
        self._current_total = current_total

    @property
    def deleted(self):
        """Gets the deleted of this DeleteStatus.

        集群删除时删除的资源记录总数

        :return: The deleted of this DeleteStatus.
        :rtype: int
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DeleteStatus.

        集群删除时删除的资源记录总数

        :param deleted: The deleted of this DeleteStatus.
        :type: int
        """
        self._deleted = deleted

    @property
    def previous_total(self):
        """Gets the previous_total of this DeleteStatus.

        集群删除时已经存在的集群资源记录总数

        :return: The previous_total of this DeleteStatus.
        :rtype: int
        """
        return self._previous_total

    @previous_total.setter
    def previous_total(self, previous_total):
        """Sets the previous_total of this DeleteStatus.

        集群删除时已经存在的集群资源记录总数

        :param previous_total: The previous_total of this DeleteStatus.
        :type: int
        """
        self._previous_total = previous_total

    @property
    def updated(self):
        """Gets the updated of this DeleteStatus.

        集群删除时更新的资源记录总数

        :return: The updated of this DeleteStatus.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this DeleteStatus.

        集群删除时更新的资源记录总数

        :param updated: The updated of this DeleteStatus.
        :type: int
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
        if not isinstance(other, DeleteStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
