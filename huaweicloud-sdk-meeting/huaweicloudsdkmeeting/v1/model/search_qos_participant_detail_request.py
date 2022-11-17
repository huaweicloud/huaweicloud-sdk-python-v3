# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchQosParticipantDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'conf_type': 'str',
        'participant_id': 'str',
        'qos_type': 'str'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'conf_type': 'confType',
        'participant_id': 'participantID',
        'qos_type': 'qosType'
    }

    def __init__(self, conf_uuid=None, conf_type=None, participant_id=None, qos_type=None):
        """SearchQosParticipantDetailRequest

        The model defined in huaweicloud sdk

        :param conf_uuid: 会议UUID。
        :type conf_uuid: str
        :param conf_type: 会议类别。 * online：在线会议，在召开的会议 * history：历史会议，已召开的会议
        :type conf_type: str
        :param participant_id: 与会者标识。
        :type participant_id: str
        :param qos_type: Qos类型。 - audio：音频 - video：视频 - screen：屏幕共享 - cpu：cpu
        :type qos_type: str
        """
        
        

        self._conf_uuid = None
        self._conf_type = None
        self._participant_id = None
        self._qos_type = None
        self.discriminator = None

        self.conf_uuid = conf_uuid
        self.conf_type = conf_type
        self.participant_id = participant_id
        self.qos_type = qos_type

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this SearchQosParticipantDetailRequest.

        会议UUID。

        :return: The conf_uuid of this SearchQosParticipantDetailRequest.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this SearchQosParticipantDetailRequest.

        会议UUID。

        :param conf_uuid: The conf_uuid of this SearchQosParticipantDetailRequest.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def conf_type(self):
        """Gets the conf_type of this SearchQosParticipantDetailRequest.

        会议类别。 * online：在线会议，在召开的会议 * history：历史会议，已召开的会议

        :return: The conf_type of this SearchQosParticipantDetailRequest.
        :rtype: str
        """
        return self._conf_type

    @conf_type.setter
    def conf_type(self, conf_type):
        """Sets the conf_type of this SearchQosParticipantDetailRequest.

        会议类别。 * online：在线会议，在召开的会议 * history：历史会议，已召开的会议

        :param conf_type: The conf_type of this SearchQosParticipantDetailRequest.
        :type conf_type: str
        """
        self._conf_type = conf_type

    @property
    def participant_id(self):
        """Gets the participant_id of this SearchQosParticipantDetailRequest.

        与会者标识。

        :return: The participant_id of this SearchQosParticipantDetailRequest.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this SearchQosParticipantDetailRequest.

        与会者标识。

        :param participant_id: The participant_id of this SearchQosParticipantDetailRequest.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def qos_type(self):
        """Gets the qos_type of this SearchQosParticipantDetailRequest.

        Qos类型。 - audio：音频 - video：视频 - screen：屏幕共享 - cpu：cpu

        :return: The qos_type of this SearchQosParticipantDetailRequest.
        :rtype: str
        """
        return self._qos_type

    @qos_type.setter
    def qos_type(self, qos_type):
        """Sets the qos_type of this SearchQosParticipantDetailRequest.

        Qos类型。 - audio：音频 - video：视频 - screen：屏幕共享 - cpu：cpu

        :param qos_type: The qos_type of this SearchQosParticipantDetailRequest.
        :type qos_type: str
        """
        self._qos_type = qos_type

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
        if not isinstance(other, SearchQosParticipantDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
