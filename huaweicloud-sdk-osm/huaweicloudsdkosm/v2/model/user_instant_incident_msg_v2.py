# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserInstantIncidentMsgV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'incident_id': 'str',
        'message_list': 'list[QueryMessageInfoV2]'
    }

    attribute_map = {
        'incident_id': 'incident_id',
        'message_list': 'message_list'
    }

    def __init__(self, incident_id=None, message_list=None):
        """UserInstantIncidentMsgV2

        The model defined in huaweicloud sdk

        :param incident_id: 工单id
        :type incident_id: str
        :param message_list: 留言列表
        :type message_list: list[:class:`huaweicloudsdkosm.v2.QueryMessageInfoV2`]
        """
        
        

        self._incident_id = None
        self._message_list = None
        self.discriminator = None

        if incident_id is not None:
            self.incident_id = incident_id
        if message_list is not None:
            self.message_list = message_list

    @property
    def incident_id(self):
        """Gets the incident_id of this UserInstantIncidentMsgV2.

        工单id

        :return: The incident_id of this UserInstantIncidentMsgV2.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this UserInstantIncidentMsgV2.

        工单id

        :param incident_id: The incident_id of this UserInstantIncidentMsgV2.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def message_list(self):
        """Gets the message_list of this UserInstantIncidentMsgV2.

        留言列表

        :return: The message_list of this UserInstantIncidentMsgV2.
        :rtype: list[:class:`huaweicloudsdkosm.v2.QueryMessageInfoV2`]
        """
        return self._message_list

    @message_list.setter
    def message_list(self, message_list):
        """Sets the message_list of this UserInstantIncidentMsgV2.

        留言列表

        :param message_list: The message_list of this UserInstantIncidentMsgV2.
        :type message_list: list[:class:`huaweicloudsdkosm.v2.QueryMessageInfoV2`]
        """
        self._message_list = message_list

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
        if not isinstance(other, UserInstantIncidentMsgV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
