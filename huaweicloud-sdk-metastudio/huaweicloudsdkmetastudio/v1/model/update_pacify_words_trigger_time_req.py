# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePacifyWordsTriggerTimeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'language': 'LanguageEnum',
        'trigger_time': 'int'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'language': 'language',
        'trigger_time': 'trigger_time'
    }

    def __init__(self, robot_id=None, language=None, trigger_time=None):
        r"""UpdatePacifyWordsTriggerTimeReq

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param trigger_time: 安抚话术等待触发时长，单位毫秒
        :type trigger_time: int
        """
        
        

        self._robot_id = None
        self._language = None
        self._trigger_time = None
        self.discriminator = None

        self.robot_id = robot_id
        self.language = language
        self.trigger_time = trigger_time

    @property
    def robot_id(self):
        r"""Gets the robot_id of this UpdatePacifyWordsTriggerTimeReq.

        应用ID。

        :return: The robot_id of this UpdatePacifyWordsTriggerTimeReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this UpdatePacifyWordsTriggerTimeReq.

        应用ID。

        :param robot_id: The robot_id of this UpdatePacifyWordsTriggerTimeReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def language(self):
        r"""Gets the language of this UpdatePacifyWordsTriggerTimeReq.

        :return: The language of this UpdatePacifyWordsTriggerTimeReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this UpdatePacifyWordsTriggerTimeReq.

        :param language: The language of this UpdatePacifyWordsTriggerTimeReq.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this UpdatePacifyWordsTriggerTimeReq.

        安抚话术等待触发时长，单位毫秒

        :return: The trigger_time of this UpdatePacifyWordsTriggerTimeReq.
        :rtype: int
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this UpdatePacifyWordsTriggerTimeReq.

        安抚话术等待触发时长，单位毫秒

        :param trigger_time: The trigger_time of this UpdatePacifyWordsTriggerTimeReq.
        :type trigger_time: int
        """
        self._trigger_time = trigger_time

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
        if not isinstance(other, UpdatePacifyWordsTriggerTimeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
