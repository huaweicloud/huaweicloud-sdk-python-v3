# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderAlertIncidentContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'incident_type': 'OrderAlertIncidentContentIncidentType'
    }

    attribute_map = {
        'title': 'title',
        'incident_type': 'incident_type'
    }

    def __init__(self, title=None, incident_type=None):
        """OrderAlertIncidentContent

        The model defined in huaweicloud sdk

        :param title: 事件名称
        :type title: str
        :param incident_type: 
        :type incident_type: :class:`huaweicloudsdksecmaster.v2.OrderAlertIncidentContentIncidentType`
        """
        
        

        self._title = None
        self._incident_type = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if incident_type is not None:
            self.incident_type = incident_type

    @property
    def title(self):
        """Gets the title of this OrderAlertIncidentContent.

        事件名称

        :return: The title of this OrderAlertIncidentContent.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OrderAlertIncidentContent.

        事件名称

        :param title: The title of this OrderAlertIncidentContent.
        :type title: str
        """
        self._title = title

    @property
    def incident_type(self):
        """Gets the incident_type of this OrderAlertIncidentContent.

        :return: The incident_type of this OrderAlertIncidentContent.
        :rtype: :class:`huaweicloudsdksecmaster.v2.OrderAlertIncidentContentIncidentType`
        """
        return self._incident_type

    @incident_type.setter
    def incident_type(self, incident_type):
        """Sets the incident_type of this OrderAlertIncidentContent.

        :param incident_type: The incident_type of this OrderAlertIncidentContent.
        :type incident_type: :class:`huaweicloudsdksecmaster.v2.OrderAlertIncidentContentIncidentType`
        """
        self._incident_type = incident_type

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
        if not isinstance(other, OrderAlertIncidentContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
