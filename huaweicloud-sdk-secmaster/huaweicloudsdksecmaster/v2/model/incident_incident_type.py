# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentIncidentType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'incident_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'incident_type': 'incident_type'
    }

    def __init__(self, category=None, incident_type=None):
        """IncidentIncidentType

        The model defined in huaweicloud sdk

        :param category: 类别
        :type category: str
        :param incident_type: 事件类型
        :type incident_type: str
        """
        
        

        self._category = None
        self._incident_type = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if incident_type is not None:
            self.incident_type = incident_type

    @property
    def category(self):
        """Gets the category of this IncidentIncidentType.

        类别

        :return: The category of this IncidentIncidentType.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this IncidentIncidentType.

        类别

        :param category: The category of this IncidentIncidentType.
        :type category: str
        """
        self._category = category

    @property
    def incident_type(self):
        """Gets the incident_type of this IncidentIncidentType.

        事件类型

        :return: The incident_type of this IncidentIncidentType.
        :rtype: str
        """
        return self._incident_type

    @incident_type.setter
    def incident_type(self, incident_type):
        """Sets the incident_type of this IncidentIncidentType.

        事件类型

        :param incident_type: The incident_type of this IncidentIncidentType.
        :type incident_type: str
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
        if not isinstance(other, IncidentIncidentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
