# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryHookRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hook_url': 'str',
        'service': 'str',
        'token': 'str',
        'hook_events': 'list[str]'
    }

    attribute_map = {
        'hook_url': 'hook_url',
        'service': 'service',
        'token': 'token',
        'hook_events': 'hook_events'
    }

    def __init__(self, hook_url=None, service=None, token=None, hook_events=None):
        r"""RepositoryHookRequest

        The model defined in huaweicloud sdk

        :param hook_url: 触发url
        :type hook_url: str
        :param service: 事件来源
        :type service: str
        :param token: 安全令牌
        :type token: str
        :param hook_events: 触发事件
        :type hook_events: list[str]
        """
        
        

        self._hook_url = None
        self._service = None
        self._token = None
        self._hook_events = None
        self.discriminator = None

        self.hook_url = hook_url
        self.service = service
        if token is not None:
            self.token = token
        self.hook_events = hook_events

    @property
    def hook_url(self):
        r"""Gets the hook_url of this RepositoryHookRequest.

        触发url

        :return: The hook_url of this RepositoryHookRequest.
        :rtype: str
        """
        return self._hook_url

    @hook_url.setter
    def hook_url(self, hook_url):
        r"""Sets the hook_url of this RepositoryHookRequest.

        触发url

        :param hook_url: The hook_url of this RepositoryHookRequest.
        :type hook_url: str
        """
        self._hook_url = hook_url

    @property
    def service(self):
        r"""Gets the service of this RepositoryHookRequest.

        事件来源

        :return: The service of this RepositoryHookRequest.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this RepositoryHookRequest.

        事件来源

        :param service: The service of this RepositoryHookRequest.
        :type service: str
        """
        self._service = service

    @property
    def token(self):
        r"""Gets the token of this RepositoryHookRequest.

        安全令牌

        :return: The token of this RepositoryHookRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this RepositoryHookRequest.

        安全令牌

        :param token: The token of this RepositoryHookRequest.
        :type token: str
        """
        self._token = token

    @property
    def hook_events(self):
        r"""Gets the hook_events of this RepositoryHookRequest.

        触发事件

        :return: The hook_events of this RepositoryHookRequest.
        :rtype: list[str]
        """
        return self._hook_events

    @hook_events.setter
    def hook_events(self, hook_events):
        r"""Sets the hook_events of this RepositoryHookRequest.

        触发事件

        :param hook_events: The hook_events of this RepositoryHookRequest.
        :type hook_events: list[str]
        """
        self._hook_events = hook_events

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
        if not isinstance(other, RepositoryHookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
