# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionUserRequestDingTalkBotEndpointInfo:

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
        'app_key': 'str',
        'app_secret': 'str',
        'robot_code': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'app_key': 'app_key',
        'app_secret': 'app_secret',
        'robot_code': 'robot_code'
    }

    def __init__(self, endpoint=None, app_key=None, app_secret=None, robot_code=None):
        r"""CreateSubscriptionUserRequestDingTalkBotEndpointInfo

        The model defined in huaweicloud sdk

        :param endpoint: 钉钉企业用户的userId。
        :type endpoint: str
        :param app_key: 个人钉钉appKey字段。
        :type app_key: str
        :param app_secret: 个人钉钉appSecret字段。
        :type app_secret: str
        :param robot_code: 个人钉钉robotCode字段。
        :type robot_code: str
        """
        
        

        self._endpoint = None
        self._app_key = None
        self._app_secret = None
        self._robot_code = None
        self.discriminator = None

        self.endpoint = endpoint
        self.app_key = app_key
        self.app_secret = app_secret
        self.robot_code = robot_code

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        钉钉企业用户的userId。

        :return: The endpoint of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        钉钉企业用户的userId。

        :param endpoint: The endpoint of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def app_key(self):
        r"""Gets the app_key of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        个人钉钉appKey字段。

        :return: The app_key of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        个人钉钉appKey字段。

        :param app_key: The app_key of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_secret(self):
        r"""Gets the app_secret of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        个人钉钉appSecret字段。

        :return: The app_secret of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        r"""Sets the app_secret of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        个人钉钉appSecret字段。

        :param app_secret: The app_secret of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
        :type app_secret: str
        """
        self._app_secret = app_secret

    @property
    def robot_code(self):
        r"""Gets the robot_code of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        个人钉钉robotCode字段。

        :return: The robot_code of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
        :rtype: str
        """
        return self._robot_code

    @robot_code.setter
    def robot_code(self, robot_code):
        r"""Sets the robot_code of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.

        个人钉钉robotCode字段。

        :param robot_code: The robot_code of this CreateSubscriptionUserRequestDingTalkBotEndpointInfo.
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
        if not isinstance(other, CreateSubscriptionUserRequestDingTalkBotEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
