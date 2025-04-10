# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderAlert:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'incident_id': 'str',
        'event_content': 'OrderAlertEventContent',
        'incident_content': 'OrderAlertIncidentContent',
        'marked_evidence': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'incident_id': 'incident_id',
        'event_content': 'event_content',
        'incident_content': 'incident_content',
        'marked_evidence': 'marked_evidence'
    }

    def __init__(self, ids=None, incident_id=None, event_content=None, incident_content=None, marked_evidence=None):
        r"""OrderAlert

        The model defined in huaweicloud sdk

        :param ids: 转事件的ID列表
        :type ids: list[str]
        :param incident_id: 事件id
        :type incident_id: str
        :param event_content: 
        :type event_content: :class:`huaweicloudsdksa.v2.OrderAlertEventContent`
        :param incident_content: 
        :type incident_content: :class:`huaweicloudsdksa.v2.OrderAlertIncidentContent`
        :param marked_evidence: 标记为证据
        :type marked_evidence: bool
        """
        
        

        self._ids = None
        self._incident_id = None
        self._event_content = None
        self._incident_content = None
        self._marked_evidence = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if incident_id is not None:
            self.incident_id = incident_id
        if event_content is not None:
            self.event_content = event_content
        if incident_content is not None:
            self.incident_content = incident_content
        if marked_evidence is not None:
            self.marked_evidence = marked_evidence

    @property
    def ids(self):
        r"""Gets the ids of this OrderAlert.

        转事件的ID列表

        :return: The ids of this OrderAlert.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this OrderAlert.

        转事件的ID列表

        :param ids: The ids of this OrderAlert.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def incident_id(self):
        r"""Gets the incident_id of this OrderAlert.

        事件id

        :return: The incident_id of this OrderAlert.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        r"""Sets the incident_id of this OrderAlert.

        事件id

        :param incident_id: The incident_id of this OrderAlert.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def event_content(self):
        r"""Gets the event_content of this OrderAlert.

        :return: The event_content of this OrderAlert.
        :rtype: :class:`huaweicloudsdksa.v2.OrderAlertEventContent`
        """
        return self._event_content

    @event_content.setter
    def event_content(self, event_content):
        r"""Sets the event_content of this OrderAlert.

        :param event_content: The event_content of this OrderAlert.
        :type event_content: :class:`huaweicloudsdksa.v2.OrderAlertEventContent`
        """
        self._event_content = event_content

    @property
    def incident_content(self):
        r"""Gets the incident_content of this OrderAlert.

        :return: The incident_content of this OrderAlert.
        :rtype: :class:`huaweicloudsdksa.v2.OrderAlertIncidentContent`
        """
        return self._incident_content

    @incident_content.setter
    def incident_content(self, incident_content):
        r"""Sets the incident_content of this OrderAlert.

        :param incident_content: The incident_content of this OrderAlert.
        :type incident_content: :class:`huaweicloudsdksa.v2.OrderAlertIncidentContent`
        """
        self._incident_content = incident_content

    @property
    def marked_evidence(self):
        r"""Gets the marked_evidence of this OrderAlert.

        标记为证据

        :return: The marked_evidence of this OrderAlert.
        :rtype: bool
        """
        return self._marked_evidence

    @marked_evidence.setter
    def marked_evidence(self, marked_evidence):
        r"""Sets the marked_evidence of this OrderAlert.

        标记为证据

        :param marked_evidence: The marked_evidence of this OrderAlert.
        :type marked_evidence: bool
        """
        self._marked_evidence = marked_evidence

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
        if not isinstance(other, OrderAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
