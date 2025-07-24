# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PauseConferenceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pause': 'int'
    }

    attribute_map = {
        'pause': 'pause'
    }

    def __init__(self, pause=None):
        r"""PauseConferenceReq

        The model defined in huaweicloud sdk

        :param pause: 主持人暂停/取消暂停会议 0：会议正常 1：会议暂停
        :type pause: int
        """
        
        

        self._pause = None
        self.discriminator = None

        self.pause = pause

    @property
    def pause(self):
        r"""Gets the pause of this PauseConferenceReq.

        主持人暂停/取消暂停会议 0：会议正常 1：会议暂停

        :return: The pause of this PauseConferenceReq.
        :rtype: int
        """
        return self._pause

    @pause.setter
    def pause(self, pause):
        r"""Sets the pause of this PauseConferenceReq.

        主持人暂停/取消暂停会议 0：会议正常 1：会议暂停

        :param pause: The pause of this PauseConferenceReq.
        :type pause: int
        """
        self._pause = pause

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
        if not isinstance(other, PauseConferenceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
