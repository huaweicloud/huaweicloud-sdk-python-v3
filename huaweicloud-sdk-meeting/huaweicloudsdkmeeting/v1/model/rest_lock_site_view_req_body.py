# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestLockSiteViewReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'participant_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'participant_id': 'participantID'
    }

    def __init__(self, status=None, participant_id=None):
        """RestLockSiteViewReqBody

        The model defined in huaweicloud sdk

        :param status: 锁定标志。 - 0: 取消锁定 - 1: 锁定
        :type status: int
        :param participant_id: 被锁定视频源的与会者标识。
        :type participant_id: str
        """
        
        

        self._status = None
        self._participant_id = None
        self.discriminator = None

        self.status = status
        self.participant_id = participant_id

    @property
    def status(self):
        """Gets the status of this RestLockSiteViewReqBody.

        锁定标志。 - 0: 取消锁定 - 1: 锁定

        :return: The status of this RestLockSiteViewReqBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RestLockSiteViewReqBody.

        锁定标志。 - 0: 取消锁定 - 1: 锁定

        :param status: The status of this RestLockSiteViewReqBody.
        :type status: int
        """
        self._status = status

    @property
    def participant_id(self):
        """Gets the participant_id of this RestLockSiteViewReqBody.

        被锁定视频源的与会者标识。

        :return: The participant_id of this RestLockSiteViewReqBody.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this RestLockSiteViewReqBody.

        被锁定视频源的与会者标识。

        :param participant_id: The participant_id of this RestLockSiteViewReqBody.
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
        if not isinstance(other, RestLockSiteViewReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
