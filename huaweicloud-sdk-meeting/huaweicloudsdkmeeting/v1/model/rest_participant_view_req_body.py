# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestParticipantViewReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'view_type': 'int',
        'participant_id': 'str'
    }

    attribute_map = {
        'view_type': 'viewType',
        'participant_id': 'participantID'
    }

    def __init__(self, view_type=None, participant_id=None):
        """RestParticipantViewReqBody

        The model defined in huaweicloud sdk

        :param view_type: 选看类型。 - 2: 选看会场
        :type view_type: int
        :param participant_id: 被选看的与会者标识。
        :type participant_id: str
        """
        
        

        self._view_type = None
        self._participant_id = None
        self.discriminator = None

        self.view_type = view_type
        self.participant_id = participant_id

    @property
    def view_type(self):
        """Gets the view_type of this RestParticipantViewReqBody.

        选看类型。 - 2: 选看会场

        :return: The view_type of this RestParticipantViewReqBody.
        :rtype: int
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """Sets the view_type of this RestParticipantViewReqBody.

        选看类型。 - 2: 选看会场

        :param view_type: The view_type of this RestParticipantViewReqBody.
        :type view_type: int
        """
        self._view_type = view_type

    @property
    def participant_id(self):
        """Gets the participant_id of this RestParticipantViewReqBody.

        被选看的与会者标识。

        :return: The participant_id of this RestParticipantViewReqBody.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this RestParticipantViewReqBody.

        被选看的与会者标识。

        :param participant_id: The participant_id of this RestParticipantViewReqBody.
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
        if not isinstance(other, RestParticipantViewReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
