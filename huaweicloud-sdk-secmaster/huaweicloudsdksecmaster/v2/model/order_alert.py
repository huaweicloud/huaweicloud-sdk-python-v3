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
        'incident_content': 'OrderAlertIncidentContent'
    }

    attribute_map = {
        'ids': 'ids',
        'incident_content': 'incident_content'
    }

    def __init__(self, ids=None, incident_content=None):
        """OrderAlert

        The model defined in huaweicloud sdk

        :param ids: 转事件的告警id列表
        :type ids: list[str]
        :param incident_content: 
        :type incident_content: :class:`huaweicloudsdksecmaster.v2.OrderAlertIncidentContent`
        """
        
        

        self._ids = None
        self._incident_content = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if incident_content is not None:
            self.incident_content = incident_content

    @property
    def ids(self):
        """Gets the ids of this OrderAlert.

        转事件的告警id列表

        :return: The ids of this OrderAlert.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this OrderAlert.

        转事件的告警id列表

        :param ids: The ids of this OrderAlert.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def incident_content(self):
        """Gets the incident_content of this OrderAlert.

        :return: The incident_content of this OrderAlert.
        :rtype: :class:`huaweicloudsdksecmaster.v2.OrderAlertIncidentContent`
        """
        return self._incident_content

    @incident_content.setter
    def incident_content(self, incident_content):
        """Sets the incident_content of this OrderAlert.

        :param incident_content: The incident_content of this OrderAlert.
        :type incident_content: :class:`huaweicloudsdksecmaster.v2.OrderAlertIncidentContent`
        """
        self._incident_content = incident_content

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
