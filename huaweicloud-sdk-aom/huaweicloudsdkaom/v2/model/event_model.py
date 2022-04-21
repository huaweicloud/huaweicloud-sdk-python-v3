# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'starts_at': 'int',
        'ends_at': 'int',
        'timeout': 'int',
        'metadata': 'object',
        'annotations': 'object',
        'attach_rule': 'object',
        'id': 'str'
    }

    attribute_map = {
        'starts_at': 'starts_at',
        'ends_at': 'ends_at',
        'timeout': 'timeout',
        'metadata': 'metadata',
        'annotations': 'annotations',
        'attach_rule': 'attach_rule',
        'id': 'id'
    }

    def __init__(self, starts_at=None, ends_at=None, timeout=None, metadata=None, annotations=None, attach_rule=None, id=None):
        """EventModel

        The model defined in huaweicloud sdk

        :param starts_at: 事件或者告警产生的时间，CST毫秒级时间戳。
        :type starts_at: int
        :param ends_at: 事件或者告警清除的时间，CST毫秒级时间戳，为0时表示未删除。
        :type ends_at: int
        :param timeout: 告警自动清除时间。毫秒数，例如一分钟则填写为60000。默认清除时间为3天,对应数字为 4320 * 1000（即：3天 * 24小时 * 60分钟 * 1000毫秒）。
        :type timeout: int
        :param metadata: 事件或者告警的详细信息，为键值对形式。必须字段为： - event_name：事件或者告警名称,类型为String； - event_severity：事件级别枚举值。类型为String，四种类型 \&quot;Critical\&quot;, \&quot;Major\&quot;, \&quot;Minor\&quot;, \&quot;Info\&quot;； - event_type：事件类别枚举值。类型为String，event为普通告警，alarm为告警事件； - resource_provider：事件对应云服务名称。类型为String； - resource_type：事件对应资源类型。类型为String； - resource_id：事件对应资源信息。类型为String。
        :type metadata: object
        :param annotations: 事件或者告警附加字段，可以为空。
        :type annotations: object
        :param attach_rule: 事件或者告警预留字段，为空。
        :type attach_rule: object
        :param id: 事件或者告警id，系统会自动生成，上报无须填写该字段。
        :type id: str
        """
        
        

        self._starts_at = None
        self._ends_at = None
        self._timeout = None
        self._metadata = None
        self._annotations = None
        self._attach_rule = None
        self._id = None
        self.discriminator = None

        if starts_at is not None:
            self.starts_at = starts_at
        if ends_at is not None:
            self.ends_at = ends_at
        if timeout is not None:
            self.timeout = timeout
        if metadata is not None:
            self.metadata = metadata
        if annotations is not None:
            self.annotations = annotations
        if attach_rule is not None:
            self.attach_rule = attach_rule
        if id is not None:
            self.id = id

    @property
    def starts_at(self):
        """Gets the starts_at of this EventModel.

        事件或者告警产生的时间，CST毫秒级时间戳。

        :return: The starts_at of this EventModel.
        :rtype: int
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this EventModel.

        事件或者告警产生的时间，CST毫秒级时间戳。

        :param starts_at: The starts_at of this EventModel.
        :type starts_at: int
        """
        self._starts_at = starts_at

    @property
    def ends_at(self):
        """Gets the ends_at of this EventModel.

        事件或者告警清除的时间，CST毫秒级时间戳，为0时表示未删除。

        :return: The ends_at of this EventModel.
        :rtype: int
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this EventModel.

        事件或者告警清除的时间，CST毫秒级时间戳，为0时表示未删除。

        :param ends_at: The ends_at of this EventModel.
        :type ends_at: int
        """
        self._ends_at = ends_at

    @property
    def timeout(self):
        """Gets the timeout of this EventModel.

        告警自动清除时间。毫秒数，例如一分钟则填写为60000。默认清除时间为3天,对应数字为 4320 * 1000（即：3天 * 24小时 * 60分钟 * 1000毫秒）。

        :return: The timeout of this EventModel.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this EventModel.

        告警自动清除时间。毫秒数，例如一分钟则填写为60000。默认清除时间为3天,对应数字为 4320 * 1000（即：3天 * 24小时 * 60分钟 * 1000毫秒）。

        :param timeout: The timeout of this EventModel.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def metadata(self):
        """Gets the metadata of this EventModel.

        事件或者告警的详细信息，为键值对形式。必须字段为： - event_name：事件或者告警名称,类型为String； - event_severity：事件级别枚举值。类型为String，四种类型 \"Critical\", \"Major\", \"Minor\", \"Info\"； - event_type：事件类别枚举值。类型为String，event为普通告警，alarm为告警事件； - resource_provider：事件对应云服务名称。类型为String； - resource_type：事件对应资源类型。类型为String； - resource_id：事件对应资源信息。类型为String。

        :return: The metadata of this EventModel.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this EventModel.

        事件或者告警的详细信息，为键值对形式。必须字段为： - event_name：事件或者告警名称,类型为String； - event_severity：事件级别枚举值。类型为String，四种类型 \"Critical\", \"Major\", \"Minor\", \"Info\"； - event_type：事件类别枚举值。类型为String，event为普通告警，alarm为告警事件； - resource_provider：事件对应云服务名称。类型为String； - resource_type：事件对应资源类型。类型为String； - resource_id：事件对应资源信息。类型为String。

        :param metadata: The metadata of this EventModel.
        :type metadata: object
        """
        self._metadata = metadata

    @property
    def annotations(self):
        """Gets the annotations of this EventModel.

        事件或者告警附加字段，可以为空。

        :return: The annotations of this EventModel.
        :rtype: object
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this EventModel.

        事件或者告警附加字段，可以为空。

        :param annotations: The annotations of this EventModel.
        :type annotations: object
        """
        self._annotations = annotations

    @property
    def attach_rule(self):
        """Gets the attach_rule of this EventModel.

        事件或者告警预留字段，为空。

        :return: The attach_rule of this EventModel.
        :rtype: object
        """
        return self._attach_rule

    @attach_rule.setter
    def attach_rule(self, attach_rule):
        """Sets the attach_rule of this EventModel.

        事件或者告警预留字段，为空。

        :param attach_rule: The attach_rule of this EventModel.
        :type attach_rule: object
        """
        self._attach_rule = attach_rule

    @property
    def id(self):
        """Gets the id of this EventModel.

        事件或者告警id，系统会自动生成，上报无须填写该字段。

        :return: The id of this EventModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventModel.

        事件或者告警id，系统会自动生成，上报无须填写该字段。

        :param id: The id of this EventModel.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, EventModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
