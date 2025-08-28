# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAgencyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_session_duration': 'int',
        'description': 'str'
    }

    attribute_map = {
        'max_session_duration': 'max_session_duration',
        'description': 'description'
    }

    def __init__(self, max_session_duration=None, description=None):
        r"""UpdateAgencyReqBody

        The model defined in huaweicloud sdk

        :param max_session_duration: 信任委托最大会话时长，默认为3600秒，取值范围为[3600,43200]。
        :type max_session_duration: int
        :param description: 信任委托描述信息。
        :type description: str
        """
        
        

        self._max_session_duration = None
        self._description = None
        self.discriminator = None

        if max_session_duration is not None:
            self.max_session_duration = max_session_duration
        if description is not None:
            self.description = description

    @property
    def max_session_duration(self):
        r"""Gets the max_session_duration of this UpdateAgencyReqBody.

        信任委托最大会话时长，默认为3600秒，取值范围为[3600,43200]。

        :return: The max_session_duration of this UpdateAgencyReqBody.
        :rtype: int
        """
        return self._max_session_duration

    @max_session_duration.setter
    def max_session_duration(self, max_session_duration):
        r"""Sets the max_session_duration of this UpdateAgencyReqBody.

        信任委托最大会话时长，默认为3600秒，取值范围为[3600,43200]。

        :param max_session_duration: The max_session_duration of this UpdateAgencyReqBody.
        :type max_session_duration: int
        """
        self._max_session_duration = max_session_duration

    @property
    def description(self):
        r"""Gets the description of this UpdateAgencyReqBody.

        信任委托描述信息。

        :return: The description of this UpdateAgencyReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAgencyReqBody.

        信任委托描述信息。

        :param description: The description of this UpdateAgencyReqBody.
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
        if not isinstance(other, UpdateAgencyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
