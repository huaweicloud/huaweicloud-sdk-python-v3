# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventResponse:

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
        'type': 'str',
        'state': 'str',
        'publish_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'not_before_deadline': 'str',
        'description': 'str',
        'instance_id': 'str',
        'execute_options': 'EventResponseExecuteOptions',
        'source': 'EventResponseSource'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'state': 'state',
        'publish_time': 'publish_time',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'not_before_deadline': 'not_before_deadline',
        'description': 'description',
        'instance_id': 'instance_id',
        'execute_options': 'execute_options',
        'source': 'source'
    }

    def __init__(self, id=None, type=None, state=None, publish_time=None, start_time=None, finish_time=None, not_before=None, not_after=None, not_before_deadline=None, description=None, instance_id=None, execute_options=None, source=None):
        r"""EventResponse

        The model defined in huaweicloud sdk

        :param id: 事件ID
        :type id: str
        :param type: 事件类型
        :type type: str
        :param state: 事件状态
        :type state: str
        :param publish_time: 事件发布时间
        :type publish_time: str
        :param start_time: 事件开始时间
        :type start_time: str
        :param finish_time: 事件完成时间
        :type finish_time: str
        :param not_before: 事件计划执行开始时间
        :type not_before: str
        :param not_after: 事件计划执行完成时间
        :type not_after: str
        :param not_before_deadline: 事件计划执行开始时间deadline
        :type not_before_deadline: str
        :param description: 事件描述
        :type description: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param execute_options: 
        :type execute_options: :class:`huaweicloudsdkecs.v2.EventResponseExecuteOptions`
        :param source: 
        :type source: :class:`huaweicloudsdkecs.v2.EventResponseSource`
        """
        
        

        self._id = None
        self._type = None
        self._state = None
        self._publish_time = None
        self._start_time = None
        self._finish_time = None
        self._not_before = None
        self._not_after = None
        self._not_before_deadline = None
        self._description = None
        self._instance_id = None
        self._execute_options = None
        self._source = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if publish_time is not None:
            self.publish_time = publish_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if not_before_deadline is not None:
            self.not_before_deadline = not_before_deadline
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if execute_options is not None:
            self.execute_options = execute_options
        if source is not None:
            self.source = source

    @property
    def id(self):
        r"""Gets the id of this EventResponse.

        事件ID

        :return: The id of this EventResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EventResponse.

        事件ID

        :param id: The id of this EventResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this EventResponse.

        事件类型

        :return: The type of this EventResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EventResponse.

        事件类型

        :param type: The type of this EventResponse.
        :type type: str
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this EventResponse.

        事件状态

        :return: The state of this EventResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this EventResponse.

        事件状态

        :param state: The state of this EventResponse.
        :type state: str
        """
        self._state = state

    @property
    def publish_time(self):
        r"""Gets the publish_time of this EventResponse.

        事件发布时间

        :return: The publish_time of this EventResponse.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this EventResponse.

        事件发布时间

        :param publish_time: The publish_time of this EventResponse.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def start_time(self):
        r"""Gets the start_time of this EventResponse.

        事件开始时间

        :return: The start_time of this EventResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this EventResponse.

        事件开始时间

        :param start_time: The start_time of this EventResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this EventResponse.

        事件完成时间

        :return: The finish_time of this EventResponse.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this EventResponse.

        事件完成时间

        :param finish_time: The finish_time of this EventResponse.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def not_before(self):
        r"""Gets the not_before of this EventResponse.

        事件计划执行开始时间

        :return: The not_before of this EventResponse.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this EventResponse.

        事件计划执行开始时间

        :param not_before: The not_before of this EventResponse.
        :type not_before: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        r"""Gets the not_after of this EventResponse.

        事件计划执行完成时间

        :return: The not_after of this EventResponse.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        r"""Sets the not_after of this EventResponse.

        事件计划执行完成时间

        :param not_after: The not_after of this EventResponse.
        :type not_after: str
        """
        self._not_after = not_after

    @property
    def not_before_deadline(self):
        r"""Gets the not_before_deadline of this EventResponse.

        事件计划执行开始时间deadline

        :return: The not_before_deadline of this EventResponse.
        :rtype: str
        """
        return self._not_before_deadline

    @not_before_deadline.setter
    def not_before_deadline(self, not_before_deadline):
        r"""Sets the not_before_deadline of this EventResponse.

        事件计划执行开始时间deadline

        :param not_before_deadline: The not_before_deadline of this EventResponse.
        :type not_before_deadline: str
        """
        self._not_before_deadline = not_before_deadline

    @property
    def description(self):
        r"""Gets the description of this EventResponse.

        事件描述

        :return: The description of this EventResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EventResponse.

        事件描述

        :param description: The description of this EventResponse.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        r"""Gets the instance_id of this EventResponse.

        实例ID

        :return: The instance_id of this EventResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this EventResponse.

        实例ID

        :param instance_id: The instance_id of this EventResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def execute_options(self):
        r"""Gets the execute_options of this EventResponse.

        :return: The execute_options of this EventResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.EventResponseExecuteOptions`
        """
        return self._execute_options

    @execute_options.setter
    def execute_options(self, execute_options):
        r"""Sets the execute_options of this EventResponse.

        :param execute_options: The execute_options of this EventResponse.
        :type execute_options: :class:`huaweicloudsdkecs.v2.EventResponseExecuteOptions`
        """
        self._execute_options = execute_options

    @property
    def source(self):
        r"""Gets the source of this EventResponse.

        :return: The source of this EventResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.EventResponseSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this EventResponse.

        :param source: The source of this EventResponse.
        :type source: :class:`huaweicloudsdkecs.v2.EventResponseSource`
        """
        self._source = source

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
        if not isinstance(other, EventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
