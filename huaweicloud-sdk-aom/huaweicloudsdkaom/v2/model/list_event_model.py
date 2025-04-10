# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventModel:

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
        'id': 'str',
        'event_sn': 'str',
        'arrives_at': 'int',
        'enterprise_project_id': 'str',
        'policy': 'dict(str, object)'
    }

    attribute_map = {
        'starts_at': 'starts_at',
        'ends_at': 'ends_at',
        'timeout': 'timeout',
        'metadata': 'metadata',
        'annotations': 'annotations',
        'attach_rule': 'attach_rule',
        'id': 'id',
        'event_sn': 'event_sn',
        'arrives_at': 'arrives_at',
        'enterprise_project_id': 'enterprise_project_id',
        'policy': 'policy'
    }

    def __init__(self, starts_at=None, ends_at=None, timeout=None, metadata=None, annotations=None, attach_rule=None, id=None, event_sn=None, arrives_at=None, enterprise_project_id=None, policy=None):
        r"""ListEventModel

        The model defined in huaweicloud sdk

        :param starts_at: 事件或者告警产生的时间，CST毫秒级时间戳。
        :type starts_at: int
        :param ends_at: 事件或者告警清除的时间，CST毫秒级时间戳，为0时表示未删除。
        :type ends_at: int
        :param timeout: 告警自动清除时间。毫秒数，例如一分钟则填写为60000。默认清除时间为3天,对应数字为 4320 * 1000（即：3天 * 24小时 * 60分钟 * 1000毫秒）。
        :type timeout: int
        :param metadata: 事件或者告警的详细信息，为键值对形式。必须字段为：  - event_name：事件或者告警名称,类型为String；  - event_severity：事件级别枚举值。类型为String，四种类型 \&quot;Critical\&quot;, \&quot;Major\&quot;, \&quot;Minor\&quot;, \&quot;Info\&quot;；  - event_type：事件类别枚举值。类型为String，event为告警事件，alarm为普通告警；  - resource_provider：事件对应云服务名称。类型为String；  - resource_type：事件对应资源类型。类型为String；  - resource_id：事件对应资源信息。类型为String。
        :type metadata: dict(str, str)
        :param annotations: 事件或者告警附加字段，可以为空。
        :type annotations: dict(str, object)
        :param attach_rule: 事件或者告警预留字段，为空。
        :type attach_rule: dict(str, object)
        :param id: 事件或者告警id，系统会自动生成，上报无须填写该字段。
        :type id: str
        :param event_sn: 告警流水号。
        :type event_sn: str
        :param arrives_at: 事件到达系统时间，CST毫秒级时间戳。
        :type arrives_at: int
        :param enterprise_project_id: 事件或告警所属企业项目id。
        :type enterprise_project_id: str
        :param policy: 开放告警策略
        :type policy: dict(str, object)
        """
        
        

        self._starts_at = None
        self._ends_at = None
        self._timeout = None
        self._metadata = None
        self._annotations = None
        self._attach_rule = None
        self._id = None
        self._event_sn = None
        self._arrives_at = None
        self._enterprise_project_id = None
        self._policy = None
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
        if event_sn is not None:
            self.event_sn = event_sn
        if arrives_at is not None:
            self.arrives_at = arrives_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if policy is not None:
            self.policy = policy

    @property
    def starts_at(self):
        r"""Gets the starts_at of this ListEventModel.

        事件或者告警产生的时间，CST毫秒级时间戳。

        :return: The starts_at of this ListEventModel.
        :rtype: int
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        r"""Sets the starts_at of this ListEventModel.

        事件或者告警产生的时间，CST毫秒级时间戳。

        :param starts_at: The starts_at of this ListEventModel.
        :type starts_at: int
        """
        self._starts_at = starts_at

    @property
    def ends_at(self):
        r"""Gets the ends_at of this ListEventModel.

        事件或者告警清除的时间，CST毫秒级时间戳，为0时表示未删除。

        :return: The ends_at of this ListEventModel.
        :rtype: int
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        r"""Sets the ends_at of this ListEventModel.

        事件或者告警清除的时间，CST毫秒级时间戳，为0时表示未删除。

        :param ends_at: The ends_at of this ListEventModel.
        :type ends_at: int
        """
        self._ends_at = ends_at

    @property
    def timeout(self):
        r"""Gets the timeout of this ListEventModel.

        告警自动清除时间。毫秒数，例如一分钟则填写为60000。默认清除时间为3天,对应数字为 4320 * 1000（即：3天 * 24小时 * 60分钟 * 1000毫秒）。

        :return: The timeout of this ListEventModel.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ListEventModel.

        告警自动清除时间。毫秒数，例如一分钟则填写为60000。默认清除时间为3天,对应数字为 4320 * 1000（即：3天 * 24小时 * 60分钟 * 1000毫秒）。

        :param timeout: The timeout of this ListEventModel.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def metadata(self):
        r"""Gets the metadata of this ListEventModel.

        事件或者告警的详细信息，为键值对形式。必须字段为：  - event_name：事件或者告警名称,类型为String；  - event_severity：事件级别枚举值。类型为String，四种类型 \"Critical\", \"Major\", \"Minor\", \"Info\"；  - event_type：事件类别枚举值。类型为String，event为告警事件，alarm为普通告警；  - resource_provider：事件对应云服务名称。类型为String；  - resource_type：事件对应资源类型。类型为String；  - resource_id：事件对应资源信息。类型为String。

        :return: The metadata of this ListEventModel.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListEventModel.

        事件或者告警的详细信息，为键值对形式。必须字段为：  - event_name：事件或者告警名称,类型为String；  - event_severity：事件级别枚举值。类型为String，四种类型 \"Critical\", \"Major\", \"Minor\", \"Info\"；  - event_type：事件类别枚举值。类型为String，event为告警事件，alarm为普通告警；  - resource_provider：事件对应云服务名称。类型为String；  - resource_type：事件对应资源类型。类型为String；  - resource_id：事件对应资源信息。类型为String。

        :param metadata: The metadata of this ListEventModel.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def annotations(self):
        r"""Gets the annotations of this ListEventModel.

        事件或者告警附加字段，可以为空。

        :return: The annotations of this ListEventModel.
        :rtype: dict(str, object)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this ListEventModel.

        事件或者告警附加字段，可以为空。

        :param annotations: The annotations of this ListEventModel.
        :type annotations: dict(str, object)
        """
        self._annotations = annotations

    @property
    def attach_rule(self):
        r"""Gets the attach_rule of this ListEventModel.

        事件或者告警预留字段，为空。

        :return: The attach_rule of this ListEventModel.
        :rtype: dict(str, object)
        """
        return self._attach_rule

    @attach_rule.setter
    def attach_rule(self, attach_rule):
        r"""Sets the attach_rule of this ListEventModel.

        事件或者告警预留字段，为空。

        :param attach_rule: The attach_rule of this ListEventModel.
        :type attach_rule: dict(str, object)
        """
        self._attach_rule = attach_rule

    @property
    def id(self):
        r"""Gets the id of this ListEventModel.

        事件或者告警id，系统会自动生成，上报无须填写该字段。

        :return: The id of this ListEventModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListEventModel.

        事件或者告警id，系统会自动生成，上报无须填写该字段。

        :param id: The id of this ListEventModel.
        :type id: str
        """
        self._id = id

    @property
    def event_sn(self):
        r"""Gets the event_sn of this ListEventModel.

        告警流水号。

        :return: The event_sn of this ListEventModel.
        :rtype: str
        """
        return self._event_sn

    @event_sn.setter
    def event_sn(self, event_sn):
        r"""Sets the event_sn of this ListEventModel.

        告警流水号。

        :param event_sn: The event_sn of this ListEventModel.
        :type event_sn: str
        """
        self._event_sn = event_sn

    @property
    def arrives_at(self):
        r"""Gets the arrives_at of this ListEventModel.

        事件到达系统时间，CST毫秒级时间戳。

        :return: The arrives_at of this ListEventModel.
        :rtype: int
        """
        return self._arrives_at

    @arrives_at.setter
    def arrives_at(self, arrives_at):
        r"""Sets the arrives_at of this ListEventModel.

        事件到达系统时间，CST毫秒级时间戳。

        :param arrives_at: The arrives_at of this ListEventModel.
        :type arrives_at: int
        """
        self._arrives_at = arrives_at

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEventModel.

        事件或告警所属企业项目id。

        :return: The enterprise_project_id of this ListEventModel.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEventModel.

        事件或告警所属企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ListEventModel.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy(self):
        r"""Gets the policy of this ListEventModel.

        开放告警策略

        :return: The policy of this ListEventModel.
        :rtype: dict(str, object)
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ListEventModel.

        开放告警策略

        :param policy: The policy of this ListEventModel.
        :type policy: dict(str, object)
        """
        self._policy = policy

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
        if not isinstance(other, ListEventModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
