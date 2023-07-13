# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventItem:

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
        'involved_object_kind': 'str',
        'involved_object': 'str',
        'message': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'status': 'str',
        'count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'involved_object_kind': 'involved_object_kind',
        'involved_object': 'involved_object',
        'message': 'message',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'count': 'count'
    }

    def __init__(self, name=None, involved_object_kind=None, involved_object=None, message=None, created_at=None, updated_at=None, status=None, count=None):
        """EventItem

        The model defined in huaweicloud sdk

        :param name: 事件名称。
        :type name: str
        :param involved_object_kind: 涉及对象类型。
        :type involved_object_kind: str
        :param involved_object: 涉及对象。
        :type involved_object: str
        :param message: 组件事件信息。
        :type message: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        :param status: 组件事件状态。
        :type status: str
        :param count: 事件发生次数。
        :type count: int
        """
        
        

        self._name = None
        self._involved_object_kind = None
        self._involved_object = None
        self._message = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._count = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if involved_object_kind is not None:
            self.involved_object_kind = involved_object_kind
        if involved_object is not None:
            self.involved_object = involved_object
        if message is not None:
            self.message = message
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if count is not None:
            self.count = count

    @property
    def name(self):
        """Gets the name of this EventItem.

        事件名称。

        :return: The name of this EventItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventItem.

        事件名称。

        :param name: The name of this EventItem.
        :type name: str
        """
        self._name = name

    @property
    def involved_object_kind(self):
        """Gets the involved_object_kind of this EventItem.

        涉及对象类型。

        :return: The involved_object_kind of this EventItem.
        :rtype: str
        """
        return self._involved_object_kind

    @involved_object_kind.setter
    def involved_object_kind(self, involved_object_kind):
        """Sets the involved_object_kind of this EventItem.

        涉及对象类型。

        :param involved_object_kind: The involved_object_kind of this EventItem.
        :type involved_object_kind: str
        """
        self._involved_object_kind = involved_object_kind

    @property
    def involved_object(self):
        """Gets the involved_object of this EventItem.

        涉及对象。

        :return: The involved_object of this EventItem.
        :rtype: str
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """Sets the involved_object of this EventItem.

        涉及对象。

        :param involved_object: The involved_object of this EventItem.
        :type involved_object: str
        """
        self._involved_object = involved_object

    @property
    def message(self):
        """Gets the message of this EventItem.

        组件事件信息。

        :return: The message of this EventItem.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EventItem.

        组件事件信息。

        :param message: The message of this EventItem.
        :type message: str
        """
        self._message = message

    @property
    def created_at(self):
        """Gets the created_at of this EventItem.

        创建时间。

        :return: The created_at of this EventItem.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EventItem.

        创建时间。

        :param created_at: The created_at of this EventItem.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EventItem.

        更新时间。

        :return: The updated_at of this EventItem.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EventItem.

        更新时间。

        :param updated_at: The updated_at of this EventItem.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this EventItem.

        组件事件状态。

        :return: The status of this EventItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventItem.

        组件事件状态。

        :param status: The status of this EventItem.
        :type status: str
        """
        self._status = status

    @property
    def count(self):
        """Gets the count of this EventItem.

        事件发生次数。

        :return: The count of this EventItem.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EventItem.

        事件发生次数。

        :param count: The count of this EventItem.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, EventItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
