# coding: utf-8

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
        'metadata': 'dict(str, str)',
        'annotations': 'dict(str, object)',
        'attach_rule': 'dict(str, object)',
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
        r"""EventModel

        The model defined in huaweicloud sdk

        :param starts_at: 指定上报的事件或者告警产生的时间。仅支持UTC毫秒级时间戳。  例如：2024-10-16 16:03:01需要通过工具转换成UTC毫秒级时间戳：1702759381000  当action值为空时，即上报事件或告警时需要时指定该参数。
        :type starts_at: int
        :param ends_at: 指定清除的事件或者告警清除的时间。仅支持UTC毫秒级时间戳。默认值为0，表示没有清除告警。  例如：2024-10-16 16:03:01需要通过工具转换成UTC毫秒级时间戳：1702759381000  当action值为clear时，即清除告警时需要时指定该参数。
        :type ends_at: int
        :param timeout: 指定AOM自动清除超期告警的时间，最长清除时间不超过15天。单位：毫秒数，一分钟则填写为60000。例如该时间设置为5天的告警，对应毫秒数：7200 * 60000（即：5天 * 24小时 * 60分钟 * 60000毫秒）。如果上报告警时没指定该时间，则默认清除时间为15天。 当action值为clear时，即清除告警时不需要指定该参数。
        :type timeout: int
        :param metadata: 待上报的事件或者告警的详细信息，为key:value键值对形式。支持如下必填字段： - event_name：事件或者告警名称，类型为String； - event_severity：事件或告警级别。类型为String，支持四种级别：    - Critical：紧急    - Major：重要    - Minor：次要    - Info：提示 - event_type：事件或告警类别。类型为String，支持两种类别：   - event：告警事件   - alarm：普通告警 - resource_provider：事件对应云服务名称。类型为String；  - resource_type：事件对应资源类型。类型为String；  - resource_id：事件对应资源信息。类型为String。 metadata中的value长度为1到2048字符串。
        :type metadata: dict(str, str)
        :param annotations: 事件或者告警附加字段，可以为空。
        :type annotations: dict(str, object)
        :param attach_rule: 事件或者告警预留字段，可以为空。
        :type attach_rule: dict(str, object)
        :param id: 事件或者告警id，产生事件或告警时，系统会自动生成。  当action值为clear时，即清除告警时需要时指定该参数。上报事件或告警时无需传入该参数。
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
        self.metadata = metadata
        if annotations is not None:
            self.annotations = annotations
        if attach_rule is not None:
            self.attach_rule = attach_rule
        if id is not None:
            self.id = id

    @property
    def starts_at(self):
        r"""Gets the starts_at of this EventModel.

        指定上报的事件或者告警产生的时间。仅支持UTC毫秒级时间戳。  例如：2024-10-16 16:03:01需要通过工具转换成UTC毫秒级时间戳：1702759381000  当action值为空时，即上报事件或告警时需要时指定该参数。

        :return: The starts_at of this EventModel.
        :rtype: int
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        r"""Sets the starts_at of this EventModel.

        指定上报的事件或者告警产生的时间。仅支持UTC毫秒级时间戳。  例如：2024-10-16 16:03:01需要通过工具转换成UTC毫秒级时间戳：1702759381000  当action值为空时，即上报事件或告警时需要时指定该参数。

        :param starts_at: The starts_at of this EventModel.
        :type starts_at: int
        """
        self._starts_at = starts_at

    @property
    def ends_at(self):
        r"""Gets the ends_at of this EventModel.

        指定清除的事件或者告警清除的时间。仅支持UTC毫秒级时间戳。默认值为0，表示没有清除告警。  例如：2024-10-16 16:03:01需要通过工具转换成UTC毫秒级时间戳：1702759381000  当action值为clear时，即清除告警时需要时指定该参数。

        :return: The ends_at of this EventModel.
        :rtype: int
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        r"""Sets the ends_at of this EventModel.

        指定清除的事件或者告警清除的时间。仅支持UTC毫秒级时间戳。默认值为0，表示没有清除告警。  例如：2024-10-16 16:03:01需要通过工具转换成UTC毫秒级时间戳：1702759381000  当action值为clear时，即清除告警时需要时指定该参数。

        :param ends_at: The ends_at of this EventModel.
        :type ends_at: int
        """
        self._ends_at = ends_at

    @property
    def timeout(self):
        r"""Gets the timeout of this EventModel.

        指定AOM自动清除超期告警的时间，最长清除时间不超过15天。单位：毫秒数，一分钟则填写为60000。例如该时间设置为5天的告警，对应毫秒数：7200 * 60000（即：5天 * 24小时 * 60分钟 * 60000毫秒）。如果上报告警时没指定该时间，则默认清除时间为15天。 当action值为clear时，即清除告警时不需要指定该参数。

        :return: The timeout of this EventModel.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this EventModel.

        指定AOM自动清除超期告警的时间，最长清除时间不超过15天。单位：毫秒数，一分钟则填写为60000。例如该时间设置为5天的告警，对应毫秒数：7200 * 60000（即：5天 * 24小时 * 60分钟 * 60000毫秒）。如果上报告警时没指定该时间，则默认清除时间为15天。 当action值为clear时，即清除告警时不需要指定该参数。

        :param timeout: The timeout of this EventModel.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def metadata(self):
        r"""Gets the metadata of this EventModel.

        待上报的事件或者告警的详细信息，为key:value键值对形式。支持如下必填字段： - event_name：事件或者告警名称，类型为String； - event_severity：事件或告警级别。类型为String，支持四种级别：    - Critical：紧急    - Major：重要    - Minor：次要    - Info：提示 - event_type：事件或告警类别。类型为String，支持两种类别：   - event：告警事件   - alarm：普通告警 - resource_provider：事件对应云服务名称。类型为String；  - resource_type：事件对应资源类型。类型为String；  - resource_id：事件对应资源信息。类型为String。 metadata中的value长度为1到2048字符串。

        :return: The metadata of this EventModel.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this EventModel.

        待上报的事件或者告警的详细信息，为key:value键值对形式。支持如下必填字段： - event_name：事件或者告警名称，类型为String； - event_severity：事件或告警级别。类型为String，支持四种级别：    - Critical：紧急    - Major：重要    - Minor：次要    - Info：提示 - event_type：事件或告警类别。类型为String，支持两种类别：   - event：告警事件   - alarm：普通告警 - resource_provider：事件对应云服务名称。类型为String；  - resource_type：事件对应资源类型。类型为String；  - resource_id：事件对应资源信息。类型为String。 metadata中的value长度为1到2048字符串。

        :param metadata: The metadata of this EventModel.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def annotations(self):
        r"""Gets the annotations of this EventModel.

        事件或者告警附加字段，可以为空。

        :return: The annotations of this EventModel.
        :rtype: dict(str, object)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this EventModel.

        事件或者告警附加字段，可以为空。

        :param annotations: The annotations of this EventModel.
        :type annotations: dict(str, object)
        """
        self._annotations = annotations

    @property
    def attach_rule(self):
        r"""Gets the attach_rule of this EventModel.

        事件或者告警预留字段，可以为空。

        :return: The attach_rule of this EventModel.
        :rtype: dict(str, object)
        """
        return self._attach_rule

    @attach_rule.setter
    def attach_rule(self, attach_rule):
        r"""Sets the attach_rule of this EventModel.

        事件或者告警预留字段，可以为空。

        :param attach_rule: The attach_rule of this EventModel.
        :type attach_rule: dict(str, object)
        """
        self._attach_rule = attach_rule

    @property
    def id(self):
        r"""Gets the id of this EventModel.

        事件或者告警id，产生事件或告警时，系统会自动生成。  当action值为clear时，即清除告警时需要时指定该参数。上报事件或告警时无需传入该参数。

        :return: The id of this EventModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EventModel.

        事件或者告警id，产生事件或告警时，系统会自动生成。  当action值为clear时，即清除告警时需要时指定该参数。上报事件或告警时无需传入该参数。

        :param id: The id of this EventModel.
        :type id: str
        """
        self._id = id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
