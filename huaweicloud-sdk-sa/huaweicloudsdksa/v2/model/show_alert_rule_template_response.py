# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRuleTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'update_time': 'int',
        'template_name': 'str',
        'data_source': 'str',
        'version': 'str',
        'query': 'str',
        'query_type': 'str',
        'severity': 'str',
        'custom_properties': 'dict(str, str)',
        'event_grouping': 'bool',
        'schedule': 'Schedule',
        'triggers': 'list[AlertRuleTrigger]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'update_time': 'update_time',
        'template_name': 'template_name',
        'data_source': 'data_source',
        'version': 'version',
        'query': 'query',
        'query_type': 'query_type',
        'severity': 'severity',
        'custom_properties': 'custom_properties',
        'event_grouping': 'event_grouping',
        'schedule': 'schedule',
        'triggers': 'triggers',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, template_id=None, update_time=None, template_name=None, data_source=None, version=None, query=None, query_type=None, severity=None, custom_properties=None, event_grouping=None, schedule=None, triggers=None, x_request_id=None):
        r"""ShowAlertRuleTemplateResponse

        The model defined in huaweicloud sdk

        :param template_id: template_id
        :type template_id: str
        :param update_time: update_time
        :type update_time: int
        :param template_name: template_name
        :type template_name: str
        :param data_source: data_source
        :type data_source: str
        :param version: version
        :type version: str
        :param query: query
        :type query: str
        :param query_type: query_type. SQL, CBSL.
        :type query_type: str
        :param severity: severity. TIPS, LOW, MEDIUM, HIGH, FATAL
        :type severity: str
        :param custom_properties: custom_properties
        :type custom_properties: dict(str, str)
        :param event_grouping: event_grouping
        :type event_grouping: bool
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        :param triggers: triggers
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowAlertRuleTemplateResponse, self).__init__()

        self._template_id = None
        self._update_time = None
        self._template_name = None
        self._data_source = None
        self._version = None
        self._query = None
        self._query_type = None
        self._severity = None
        self._custom_properties = None
        self._event_grouping = None
        self._schedule = None
        self._triggers = None
        self._x_request_id = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if update_time is not None:
            self.update_time = update_time
        if template_name is not None:
            self.template_name = template_name
        if data_source is not None:
            self.data_source = data_source
        if version is not None:
            self.version = version
        if query is not None:
            self.query = query
        if query_type is not None:
            self.query_type = query_type
        if severity is not None:
            self.severity = severity
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if event_grouping is not None:
            self.event_grouping = event_grouping
        if schedule is not None:
            self.schedule = schedule
        if triggers is not None:
            self.triggers = triggers
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowAlertRuleTemplateResponse.

        template_id

        :return: The template_id of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowAlertRuleTemplateResponse.

        template_id

        :param template_id: The template_id of this ShowAlertRuleTemplateResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAlertRuleTemplateResponse.

        update_time

        :return: The update_time of this ShowAlertRuleTemplateResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAlertRuleTemplateResponse.

        update_time

        :param update_time: The update_time of this ShowAlertRuleTemplateResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowAlertRuleTemplateResponse.

        template_name

        :return: The template_name of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowAlertRuleTemplateResponse.

        template_name

        :param template_name: The template_name of this ShowAlertRuleTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def data_source(self):
        r"""Gets the data_source of this ShowAlertRuleTemplateResponse.

        data_source

        :return: The data_source of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this ShowAlertRuleTemplateResponse.

        data_source

        :param data_source: The data_source of this ShowAlertRuleTemplateResponse.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def version(self):
        r"""Gets the version of this ShowAlertRuleTemplateResponse.

        version

        :return: The version of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowAlertRuleTemplateResponse.

        version

        :param version: The version of this ShowAlertRuleTemplateResponse.
        :type version: str
        """
        self._version = version

    @property
    def query(self):
        r"""Gets the query of this ShowAlertRuleTemplateResponse.

        query

        :return: The query of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ShowAlertRuleTemplateResponse.

        query

        :param query: The query of this ShowAlertRuleTemplateResponse.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this ShowAlertRuleTemplateResponse.

        query_type. SQL, CBSL.

        :return: The query_type of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ShowAlertRuleTemplateResponse.

        query_type. SQL, CBSL.

        :param query_type: The query_type of this ShowAlertRuleTemplateResponse.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def severity(self):
        r"""Gets the severity of this ShowAlertRuleTemplateResponse.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowAlertRuleTemplateResponse.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this ShowAlertRuleTemplateResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this ShowAlertRuleTemplateResponse.

        custom_properties

        :return: The custom_properties of this ShowAlertRuleTemplateResponse.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this ShowAlertRuleTemplateResponse.

        custom_properties

        :param custom_properties: The custom_properties of this ShowAlertRuleTemplateResponse.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this ShowAlertRuleTemplateResponse.

        event_grouping

        :return: The event_grouping of this ShowAlertRuleTemplateResponse.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this ShowAlertRuleTemplateResponse.

        event_grouping

        :param event_grouping: The event_grouping of this ShowAlertRuleTemplateResponse.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def schedule(self):
        r"""Gets the schedule of this ShowAlertRuleTemplateResponse.

        :return: The schedule of this ShowAlertRuleTemplateResponse.
        :rtype: :class:`huaweicloudsdksa.v2.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this ShowAlertRuleTemplateResponse.

        :param schedule: The schedule of this ShowAlertRuleTemplateResponse.
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        """
        self._schedule = schedule

    @property
    def triggers(self):
        r"""Gets the triggers of this ShowAlertRuleTemplateResponse.

        triggers

        :return: The triggers of this ShowAlertRuleTemplateResponse.
        :rtype: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this ShowAlertRuleTemplateResponse.

        triggers

        :param triggers: The triggers of this ShowAlertRuleTemplateResponse.
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        self._triggers = triggers

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowAlertRuleTemplateResponse.

        :return: The x_request_id of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowAlertRuleTemplateResponse.

        :param x_request_id: The x_request_id of this ShowAlertRuleTemplateResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowAlertRuleTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
