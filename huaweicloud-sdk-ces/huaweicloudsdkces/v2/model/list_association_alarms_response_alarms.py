# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociationAlarmsResponseAlarms:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, alarm_id=None, name=None, description=None):
        """ListAssociationAlarmsResponseAlarms

        The model defined in huaweicloud sdk

        :param alarm_id: 告警规则ID
        :type alarm_id: str
        :param name: 告警规则名称
        :type name: str
        :param description: 告警规则描述
        :type description: str
        """
        
        

        self._alarm_id = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.alarm_id = alarm_id
        self.name = name
        self.description = description

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAssociationAlarmsResponseAlarms.

        告警规则ID

        :return: The alarm_id of this ListAssociationAlarmsResponseAlarms.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAssociationAlarmsResponseAlarms.

        告警规则ID

        :param alarm_id: The alarm_id of this ListAssociationAlarmsResponseAlarms.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        """Gets the name of this ListAssociationAlarmsResponseAlarms.

        告警规则名称

        :return: The name of this ListAssociationAlarmsResponseAlarms.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAssociationAlarmsResponseAlarms.

        告警规则名称

        :param name: The name of this ListAssociationAlarmsResponseAlarms.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListAssociationAlarmsResponseAlarms.

        告警规则描述

        :return: The description of this ListAssociationAlarmsResponseAlarms.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListAssociationAlarmsResponseAlarms.

        告警规则描述

        :param description: The description of this ListAssociationAlarmsResponseAlarms.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ListAssociationAlarmsResponseAlarms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
