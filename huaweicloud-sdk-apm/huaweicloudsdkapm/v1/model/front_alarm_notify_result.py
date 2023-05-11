# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrontAlarmNotifyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'gmt_create': 'str',
        'notify_type': 'str',
        'alarm_rule_id': 'int',
        'template_id': 'int',
        'alarm_data_event_id': 'int',
        'notify_status': 'bool',
        'alarm_content': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'notify_type': 'notify_type',
        'alarm_rule_id': 'alarm_rule_id',
        'template_id': 'template_id',
        'alarm_data_event_id': 'alarm_data_event_id',
        'notify_status': 'notify_status',
        'alarm_content': 'alarm_content'
    }

    def __init__(self, id=None, gmt_create=None, notify_type=None, alarm_rule_id=None, template_id=None, alarm_data_event_id=None, notify_status=None, alarm_content=None):
        """FrontAlarmNotifyResult

        The model defined in huaweicloud sdk

        :param id: 告警通知id。
        :type id: int
        :param gmt_create: 创建时间。
        :type gmt_create: str
        :param notify_type: 通知类型。
        :type notify_type: str
        :param alarm_rule_id: 告警规则id。
        :type alarm_rule_id: int
        :param template_id: 模板id。
        :type template_id: int
        :param alarm_data_event_id: 关联事件id。
        :type alarm_data_event_id: int
        :param notify_status: 通知结果。
        :type notify_status: bool
        :param alarm_content: 通知内容。
        :type alarm_content: str
        """
        
        

        self._id = None
        self._gmt_create = None
        self._notify_type = None
        self._alarm_rule_id = None
        self._template_id = None
        self._alarm_data_event_id = None
        self._notify_status = None
        self._alarm_content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if notify_type is not None:
            self.notify_type = notify_type
        if alarm_rule_id is not None:
            self.alarm_rule_id = alarm_rule_id
        if template_id is not None:
            self.template_id = template_id
        if alarm_data_event_id is not None:
            self.alarm_data_event_id = alarm_data_event_id
        if notify_status is not None:
            self.notify_status = notify_status
        if alarm_content is not None:
            self.alarm_content = alarm_content

    @property
    def id(self):
        """Gets the id of this FrontAlarmNotifyResult.

        告警通知id。

        :return: The id of this FrontAlarmNotifyResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FrontAlarmNotifyResult.

        告警通知id。

        :param id: The id of this FrontAlarmNotifyResult.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this FrontAlarmNotifyResult.

        创建时间。

        :return: The gmt_create of this FrontAlarmNotifyResult.
        :rtype: str
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this FrontAlarmNotifyResult.

        创建时间。

        :param gmt_create: The gmt_create of this FrontAlarmNotifyResult.
        :type gmt_create: str
        """
        self._gmt_create = gmt_create

    @property
    def notify_type(self):
        """Gets the notify_type of this FrontAlarmNotifyResult.

        通知类型。

        :return: The notify_type of this FrontAlarmNotifyResult.
        :rtype: str
        """
        return self._notify_type

    @notify_type.setter
    def notify_type(self, notify_type):
        """Sets the notify_type of this FrontAlarmNotifyResult.

        通知类型。

        :param notify_type: The notify_type of this FrontAlarmNotifyResult.
        :type notify_type: str
        """
        self._notify_type = notify_type

    @property
    def alarm_rule_id(self):
        """Gets the alarm_rule_id of this FrontAlarmNotifyResult.

        告警规则id。

        :return: The alarm_rule_id of this FrontAlarmNotifyResult.
        :rtype: int
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        """Sets the alarm_rule_id of this FrontAlarmNotifyResult.

        告警规则id。

        :param alarm_rule_id: The alarm_rule_id of this FrontAlarmNotifyResult.
        :type alarm_rule_id: int
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def template_id(self):
        """Gets the template_id of this FrontAlarmNotifyResult.

        模板id。

        :return: The template_id of this FrontAlarmNotifyResult.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this FrontAlarmNotifyResult.

        模板id。

        :param template_id: The template_id of this FrontAlarmNotifyResult.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def alarm_data_event_id(self):
        """Gets the alarm_data_event_id of this FrontAlarmNotifyResult.

        关联事件id。

        :return: The alarm_data_event_id of this FrontAlarmNotifyResult.
        :rtype: int
        """
        return self._alarm_data_event_id

    @alarm_data_event_id.setter
    def alarm_data_event_id(self, alarm_data_event_id):
        """Sets the alarm_data_event_id of this FrontAlarmNotifyResult.

        关联事件id。

        :param alarm_data_event_id: The alarm_data_event_id of this FrontAlarmNotifyResult.
        :type alarm_data_event_id: int
        """
        self._alarm_data_event_id = alarm_data_event_id

    @property
    def notify_status(self):
        """Gets the notify_status of this FrontAlarmNotifyResult.

        通知结果。

        :return: The notify_status of this FrontAlarmNotifyResult.
        :rtype: bool
        """
        return self._notify_status

    @notify_status.setter
    def notify_status(self, notify_status):
        """Sets the notify_status of this FrontAlarmNotifyResult.

        通知结果。

        :param notify_status: The notify_status of this FrontAlarmNotifyResult.
        :type notify_status: bool
        """
        self._notify_status = notify_status

    @property
    def alarm_content(self):
        """Gets the alarm_content of this FrontAlarmNotifyResult.

        通知内容。

        :return: The alarm_content of this FrontAlarmNotifyResult.
        :rtype: str
        """
        return self._alarm_content

    @alarm_content.setter
    def alarm_content(self, alarm_content):
        """Sets the alarm_content of this FrontAlarmNotifyResult.

        通知内容。

        :param alarm_content: The alarm_content of this FrontAlarmNotifyResult.
        :type alarm_content: str
        """
        self._alarm_content = alarm_content

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
        if not isinstance(other, FrontAlarmNotifyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
