# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeScheduledEventRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization_type': 'str',
        'not_before': 'str'
    }

    attribute_map = {
        'authorization_type': 'authorization_type',
        'not_before': 'not_before'
    }

    def __init__(self, authorization_type=None, not_before=None):
        r"""AuthorizeScheduledEventRequestBody

        The model defined in huaweicloud sdk

        :param authorization_type: 授权类型。取值范围： maintenance：维护、 redeploy：重部署
        :type authorization_type: str
        :param not_before: 计划执行开始时间。仅maintenance类型的事件支持，预约的时间需要比当前时间多5分钟以上，传空字符串表示立即执行。
        :type not_before: str
        """
        
        

        self._authorization_type = None
        self._not_before = None
        self.discriminator = None

        self.authorization_type = authorization_type
        if not_before is not None:
            self.not_before = not_before

    @property
    def authorization_type(self):
        r"""Gets the authorization_type of this AuthorizeScheduledEventRequestBody.

        授权类型。取值范围： maintenance：维护、 redeploy：重部署

        :return: The authorization_type of this AuthorizeScheduledEventRequestBody.
        :rtype: str
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        r"""Sets the authorization_type of this AuthorizeScheduledEventRequestBody.

        授权类型。取值范围： maintenance：维护、 redeploy：重部署

        :param authorization_type: The authorization_type of this AuthorizeScheduledEventRequestBody.
        :type authorization_type: str
        """
        self._authorization_type = authorization_type

    @property
    def not_before(self):
        r"""Gets the not_before of this AuthorizeScheduledEventRequestBody.

        计划执行开始时间。仅maintenance类型的事件支持，预约的时间需要比当前时间多5分钟以上，传空字符串表示立即执行。

        :return: The not_before of this AuthorizeScheduledEventRequestBody.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this AuthorizeScheduledEventRequestBody.

        计划执行开始时间。仅maintenance类型的事件支持，预约的时间需要比当前时间多5分钟以上，传空字符串表示立即执行。

        :param not_before: The not_before of this AuthorizeScheduledEventRequestBody.
        :type not_before: str
        """
        self._not_before = not_before

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
        if not isinstance(other, AuthorizeScheduledEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
