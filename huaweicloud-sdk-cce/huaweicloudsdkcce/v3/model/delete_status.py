# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'previous_total': 'int',
        'current_total': 'int',
        'updated': 'int',
        'added': 'int',
        'deleted': 'int'
    }

    attribute_map = {
        'previous_total': 'previous_total',
        'current_total': 'current_total',
        'updated': 'updated',
        'added': 'added',
        'deleted': 'deleted'
    }

    def __init__(self, previous_total=None, current_total=None, updated=None, added=None, deleted=None):
        """DeleteStatus

        The model defined in huaweicloud sdk

        :param previous_total: 集群删除时已经存在的集群资源记录总数
        :type previous_total: int
        :param current_total: 基于当前集群资源记录信息，生成实际最新资源记录总数
        :type current_total: int
        :param updated: 集群删除时更新的资源记录总数
        :type updated: int
        :param added: 集群删除时更新的资源记录总数
        :type added: int
        :param deleted: 集群删除时删除的资源记录总数
        :type deleted: int
        """
        
        

        self._previous_total = None
        self._current_total = None
        self._updated = None
        self._added = None
        self._deleted = None
        self.discriminator = None

        if previous_total is not None:
            self.previous_total = previous_total
        if current_total is not None:
            self.current_total = current_total
        if updated is not None:
            self.updated = updated
        if added is not None:
            self.added = added
        if deleted is not None:
            self.deleted = deleted

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
        :type previous_total: int
        """
        self._previous_total = previous_total

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
        :type current_total: int
        """
        self._current_total = current_total

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
        :type updated: int
        """
        self._updated = updated

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
        :type added: int
        """
        self._added = added

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
        :type deleted: int
        """
        self._deleted = deleted

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
        if not isinstance(other, DeleteStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
