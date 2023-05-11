# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelAttendInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'participant_id': 'str'
    }

    attribute_map = {
        'number': 'number',
        'participant_id': 'participantID'
    }

    def __init__(self, number=None, participant_id=None):
        """DelAttendInfo

        The model defined in huaweicloud sdk

        :param number: 会场号码。
        :type number: str
        :param participant_id: 与会者标识，已入会的必须填写该字段。
        :type participant_id: str
        """
        
        

        self._number = None
        self._participant_id = None
        self.discriminator = None

        self.number = number
        if participant_id is not None:
            self.participant_id = participant_id

    @property
    def number(self):
        """Gets the number of this DelAttendInfo.

        会场号码。

        :return: The number of this DelAttendInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this DelAttendInfo.

        会场号码。

        :param number: The number of this DelAttendInfo.
        :type number: str
        """
        self._number = number

    @property
    def participant_id(self):
        """Gets the participant_id of this DelAttendInfo.

        与会者标识，已入会的必须填写该字段。

        :return: The participant_id of this DelAttendInfo.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this DelAttendInfo.

        与会者标识，已入会的必须填写该字段。

        :param participant_id: The participant_id of this DelAttendInfo.
        :type participant_id: str
        """
        self._participant_id = participant_id

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
        if not isinstance(other, DelAttendInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
