# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderAlertIncidentContentIncidentType:

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
        'layout_id': 'str',
        'incident_type': 'str',
        'category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'layout_id': 'layoutId',
        'incident_type': 'incident_type',
        'category': 'category'
    }

    def __init__(self, id=None, layout_id=None, incident_type=None, category=None):
        r"""OrderAlertIncidentContentIncidentType

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param layout_id: Id value
        :type layout_id: str
        :param incident_type: Id value
        :type incident_type: str
        :param category: Id value
        :type category: str
        """
        
        

        self._id = None
        self._layout_id = None
        self._incident_type = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if layout_id is not None:
            self.layout_id = layout_id
        if incident_type is not None:
            self.incident_type = incident_type
        if category is not None:
            self.category = category

    @property
    def id(self):
        r"""Gets the id of this OrderAlertIncidentContentIncidentType.

        Id value

        :return: The id of this OrderAlertIncidentContentIncidentType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OrderAlertIncidentContentIncidentType.

        Id value

        :param id: The id of this OrderAlertIncidentContentIncidentType.
        :type id: str
        """
        self._id = id

    @property
    def layout_id(self):
        r"""Gets the layout_id of this OrderAlertIncidentContentIncidentType.

        Id value

        :return: The layout_id of this OrderAlertIncidentContentIncidentType.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this OrderAlertIncidentContentIncidentType.

        Id value

        :param layout_id: The layout_id of this OrderAlertIncidentContentIncidentType.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def incident_type(self):
        r"""Gets the incident_type of this OrderAlertIncidentContentIncidentType.

        Id value

        :return: The incident_type of this OrderAlertIncidentContentIncidentType.
        :rtype: str
        """
        return self._incident_type

    @incident_type.setter
    def incident_type(self, incident_type):
        r"""Sets the incident_type of this OrderAlertIncidentContentIncidentType.

        Id value

        :param incident_type: The incident_type of this OrderAlertIncidentContentIncidentType.
        :type incident_type: str
        """
        self._incident_type = incident_type

    @property
    def category(self):
        r"""Gets the category of this OrderAlertIncidentContentIncidentType.

        Id value

        :return: The category of this OrderAlertIncidentContentIncidentType.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this OrderAlertIncidentContentIncidentType.

        Id value

        :param category: The category of this OrderAlertIncidentContentIncidentType.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, OrderAlertIncidentContentIncidentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
