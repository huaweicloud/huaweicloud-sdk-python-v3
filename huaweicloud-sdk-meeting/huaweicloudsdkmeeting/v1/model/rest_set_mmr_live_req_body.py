# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestSetMmrLiveReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'live_state': 'int'
    }

    attribute_map = {
        'live_state': 'liveState'
    }

    def __init__(self, live_state=None):
        r"""RestSetMmrLiveReqBody

        The model defined in huaweicloud sdk

        :param live_state: 0：停止Mmr会议直播 1：启动Mmr会议直播
        :type live_state: int
        """
        
        

        self._live_state = None
        self.discriminator = None

        self.live_state = live_state

    @property
    def live_state(self):
        r"""Gets the live_state of this RestSetMmrLiveReqBody.

        0：停止Mmr会议直播 1：启动Mmr会议直播

        :return: The live_state of this RestSetMmrLiveReqBody.
        :rtype: int
        """
        return self._live_state

    @live_state.setter
    def live_state(self, live_state):
        r"""Sets the live_state of this RestSetMmrLiveReqBody.

        0：停止Mmr会议直播 1：启动Mmr会议直播

        :param live_state: The live_state of this RestSetMmrLiveReqBody.
        :type live_state: int
        """
        self._live_state = live_state

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
        if not isinstance(other, RestSetMmrLiveReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
