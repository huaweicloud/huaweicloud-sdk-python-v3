# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlaOrderResponse(SdkResponse):

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
        'order_title': 'str',
        'order_id': 'str',
        'trigger_type': 'str',
        'order_level': 'str',
        'create_time': 'str',
        'sla_record': 'list[SlaRecord]'
    }

    attribute_map = {
        'id': 'id',
        'order_title': 'order_title',
        'order_id': 'order_id',
        'trigger_type': 'trigger_type',
        'order_level': 'order_level',
        'create_time': 'create_time',
        'sla_record': 'sla_record'
    }

    def __init__(self, id=None, order_title=None, order_id=None, trigger_type=None, order_level=None, create_time=None, sla_record=None):
        r"""ShowSlaOrderResponse

        The model defined in huaweicloud sdk

        :param id: 主键
        :type id: str
        :param order_title: 工单标题
        :type order_title: str
        :param order_id: 工单ID
        :type order_id: str
        :param trigger_type: 触发类型(EVENT_TICKET,ALARM_TICKET,CHANGE_NOTE,TO_DO_TASKS,ISSUE_TICKET)
        :type trigger_type: str
        :param order_level: 工单等级
        :type order_level: str
        :param create_time: 工单开始时间
        :type create_time: str
        :param sla_record: SLA规则记录
        :type sla_record: list[:class:`huaweicloudsdkcoc.v1.SlaRecord`]
        """
        
        super(ShowSlaOrderResponse, self).__init__()

        self._id = None
        self._order_title = None
        self._order_id = None
        self._trigger_type = None
        self._order_level = None
        self._create_time = None
        self._sla_record = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if order_title is not None:
            self.order_title = order_title
        if order_id is not None:
            self.order_id = order_id
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if order_level is not None:
            self.order_level = order_level
        if create_time is not None:
            self.create_time = create_time
        if sla_record is not None:
            self.sla_record = sla_record

    @property
    def id(self):
        r"""Gets the id of this ShowSlaOrderResponse.

        主键

        :return: The id of this ShowSlaOrderResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSlaOrderResponse.

        主键

        :param id: The id of this ShowSlaOrderResponse.
        :type id: str
        """
        self._id = id

    @property
    def order_title(self):
        r"""Gets the order_title of this ShowSlaOrderResponse.

        工单标题

        :return: The order_title of this ShowSlaOrderResponse.
        :rtype: str
        """
        return self._order_title

    @order_title.setter
    def order_title(self, order_title):
        r"""Sets the order_title of this ShowSlaOrderResponse.

        工单标题

        :param order_title: The order_title of this ShowSlaOrderResponse.
        :type order_title: str
        """
        self._order_title = order_title

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowSlaOrderResponse.

        工单ID

        :return: The order_id of this ShowSlaOrderResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowSlaOrderResponse.

        工单ID

        :param order_id: The order_id of this ShowSlaOrderResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ShowSlaOrderResponse.

        触发类型(EVENT_TICKET,ALARM_TICKET,CHANGE_NOTE,TO_DO_TASKS,ISSUE_TICKET)

        :return: The trigger_type of this ShowSlaOrderResponse.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ShowSlaOrderResponse.

        触发类型(EVENT_TICKET,ALARM_TICKET,CHANGE_NOTE,TO_DO_TASKS,ISSUE_TICKET)

        :param trigger_type: The trigger_type of this ShowSlaOrderResponse.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def order_level(self):
        r"""Gets the order_level of this ShowSlaOrderResponse.

        工单等级

        :return: The order_level of this ShowSlaOrderResponse.
        :rtype: str
        """
        return self._order_level

    @order_level.setter
    def order_level(self, order_level):
        r"""Sets the order_level of this ShowSlaOrderResponse.

        工单等级

        :param order_level: The order_level of this ShowSlaOrderResponse.
        :type order_level: str
        """
        self._order_level = order_level

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSlaOrderResponse.

        工单开始时间

        :return: The create_time of this ShowSlaOrderResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSlaOrderResponse.

        工单开始时间

        :param create_time: The create_time of this ShowSlaOrderResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def sla_record(self):
        r"""Gets the sla_record of this ShowSlaOrderResponse.

        SLA规则记录

        :return: The sla_record of this ShowSlaOrderResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.SlaRecord`]
        """
        return self._sla_record

    @sla_record.setter
    def sla_record(self, sla_record):
        r"""Sets the sla_record of this ShowSlaOrderResponse.

        SLA规则记录

        :param sla_record: The sla_record of this ShowSlaOrderResponse.
        :type sla_record: list[:class:`huaweicloudsdkcoc.v1.SlaRecord`]
        """
        self._sla_record = sla_record

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
        if not isinstance(other, ShowSlaOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
