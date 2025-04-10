# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSampleItemInfo:

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
        'content': 'str',
        'event_type_id': 'str',
        'event_type_name': 'str',
        'event_source_id': 'str',
        'event_source_name': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'deleted_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'content': 'content',
        'event_type_id': 'event_type_id',
        'event_type_name': 'event_type_name',
        'event_source_id': 'event_source_id',
        'event_source_name': 'event_source_name',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'deleted_time': 'deleted_time'
    }

    def __init__(self, id=None, name=None, content=None, event_type_id=None, event_type_name=None, event_source_id=None, event_source_name=None, created_time=None, updated_time=None, deleted_time=None):
        r"""EventSampleItemInfo

        The model defined in huaweicloud sdk

        :param id: 事件示例ID
        :type id: str
        :param name: 事件示例名称
        :type name: str
        :param content: 事件示例内容
        :type content: str
        :param event_type_id: 事件示例对应的事件类型ID
        :type event_type_id: str
        :param event_type_name: 事件示例对应的事件类型名称
        :type event_type_name: str
        :param event_source_id: 事件示例对应的事件源ID
        :type event_source_id: str
        :param event_source_name: 事件示例对应的事件源名称
        :type event_source_name: str
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param deleted_time: 删除时间
        :type deleted_time: str
        """
        
        

        self._id = None
        self._name = None
        self._content = None
        self._event_type_id = None
        self._event_type_name = None
        self._event_source_id = None
        self._event_source_name = None
        self._created_time = None
        self._updated_time = None
        self._deleted_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if content is not None:
            self.content = content
        if event_type_id is not None:
            self.event_type_id = event_type_id
        if event_type_name is not None:
            self.event_type_name = event_type_name
        if event_source_id is not None:
            self.event_source_id = event_source_id
        if event_source_name is not None:
            self.event_source_name = event_source_name
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if deleted_time is not None:
            self.deleted_time = deleted_time

    @property
    def id(self):
        r"""Gets the id of this EventSampleItemInfo.

        事件示例ID

        :return: The id of this EventSampleItemInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EventSampleItemInfo.

        事件示例ID

        :param id: The id of this EventSampleItemInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EventSampleItemInfo.

        事件示例名称

        :return: The name of this EventSampleItemInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EventSampleItemInfo.

        事件示例名称

        :param name: The name of this EventSampleItemInfo.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        r"""Gets the content of this EventSampleItemInfo.

        事件示例内容

        :return: The content of this EventSampleItemInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this EventSampleItemInfo.

        事件示例内容

        :param content: The content of this EventSampleItemInfo.
        :type content: str
        """
        self._content = content

    @property
    def event_type_id(self):
        r"""Gets the event_type_id of this EventSampleItemInfo.

        事件示例对应的事件类型ID

        :return: The event_type_id of this EventSampleItemInfo.
        :rtype: str
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        r"""Sets the event_type_id of this EventSampleItemInfo.

        事件示例对应的事件类型ID

        :param event_type_id: The event_type_id of this EventSampleItemInfo.
        :type event_type_id: str
        """
        self._event_type_id = event_type_id

    @property
    def event_type_name(self):
        r"""Gets the event_type_name of this EventSampleItemInfo.

        事件示例对应的事件类型名称

        :return: The event_type_name of this EventSampleItemInfo.
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        r"""Sets the event_type_name of this EventSampleItemInfo.

        事件示例对应的事件类型名称

        :param event_type_name: The event_type_name of this EventSampleItemInfo.
        :type event_type_name: str
        """
        self._event_type_name = event_type_name

    @property
    def event_source_id(self):
        r"""Gets the event_source_id of this EventSampleItemInfo.

        事件示例对应的事件源ID

        :return: The event_source_id of this EventSampleItemInfo.
        :rtype: str
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        r"""Sets the event_source_id of this EventSampleItemInfo.

        事件示例对应的事件源ID

        :param event_source_id: The event_source_id of this EventSampleItemInfo.
        :type event_source_id: str
        """
        self._event_source_id = event_source_id

    @property
    def event_source_name(self):
        r"""Gets the event_source_name of this EventSampleItemInfo.

        事件示例对应的事件源名称

        :return: The event_source_name of this EventSampleItemInfo.
        :rtype: str
        """
        return self._event_source_name

    @event_source_name.setter
    def event_source_name(self, event_source_name):
        r"""Sets the event_source_name of this EventSampleItemInfo.

        事件示例对应的事件源名称

        :param event_source_name: The event_source_name of this EventSampleItemInfo.
        :type event_source_name: str
        """
        self._event_source_name = event_source_name

    @property
    def created_time(self):
        r"""Gets the created_time of this EventSampleItemInfo.

        创建时间

        :return: The created_time of this EventSampleItemInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this EventSampleItemInfo.

        创建时间

        :param created_time: The created_time of this EventSampleItemInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this EventSampleItemInfo.

        更新时间

        :return: The updated_time of this EventSampleItemInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this EventSampleItemInfo.

        更新时间

        :param updated_time: The updated_time of this EventSampleItemInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def deleted_time(self):
        r"""Gets the deleted_time of this EventSampleItemInfo.

        删除时间

        :return: The deleted_time of this EventSampleItemInfo.
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        r"""Sets the deleted_time of this EventSampleItemInfo.

        删除时间

        :param deleted_time: The deleted_time of this EventSampleItemInfo.
        :type deleted_time: str
        """
        self._deleted_time = deleted_time

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
        if not isinstance(other, EventSampleItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
