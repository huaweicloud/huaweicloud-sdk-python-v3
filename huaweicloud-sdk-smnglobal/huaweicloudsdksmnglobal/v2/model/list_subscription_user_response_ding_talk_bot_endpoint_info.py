# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionUserResponseDingTalkBotEndpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'robot_code': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'robot_code': 'robot_code'
    }

    def __init__(self, endpoint=None, robot_code=None):
        r"""ListSubscriptionUserResponseDingTalkBotEndpointInfo

        The model defined in huaweicloud sdk

        :param endpoint: 钉钉企业用户的userId。
        :type endpoint: str
        :param robot_code: 钉钉创建的机器人编码。
        :type robot_code: str
        """
        
        

        self._endpoint = None
        self._robot_code = None
        self.discriminator = None

        if endpoint is not None:
            self.endpoint = endpoint
        if robot_code is not None:
            self.robot_code = robot_code

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.

        钉钉企业用户的userId。

        :return: The endpoint of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.

        钉钉企业用户的userId。

        :param endpoint: The endpoint of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def robot_code(self):
        r"""Gets the robot_code of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.

        钉钉创建的机器人编码。

        :return: The robot_code of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.
        :rtype: str
        """
        return self._robot_code

    @robot_code.setter
    def robot_code(self, robot_code):
        r"""Sets the robot_code of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.

        钉钉创建的机器人编码。

        :param robot_code: The robot_code of this ListSubscriptionUserResponseDingTalkBotEndpointInfo.
        :type robot_code: str
        """
        self._robot_code = robot_code

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSubscriptionUserResponseDingTalkBotEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
