# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotificationSubscriptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'enabled': 'bool',
        'config_source': 'str',
        'webhook_config': 'RepoWebHookSubscriptionDto',
        'waring_repo_usage_rate': 'int',
        'subscript_events': 'list[RepoSubscriptionEventDto]'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'enabled': 'enabled',
        'config_source': 'config_source',
        'webhook_config': 'webhook_config',
        'waring_repo_usage_rate': 'waring_repo_usage_rate',
        'subscript_events': 'subscript_events'
    }

    def __init__(self, repository_id=None, enabled=None, config_source=None, webhook_config=None, waring_repo_usage_rate=None, subscript_events=None):
        r"""UpdateNotificationSubscriptionResponse

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库ID。
        :type repository_id: int
        :param enabled: **参数解释：** 开启通知。
        :type enabled: bool
        :param config_source: **参数解释：** 配资源。
        :type config_source: str
        :param webhook_config: 
        :type webhook_config: :class:`huaweicloudsdkcodehub.v4.RepoWebHookSubscriptionDto`
        :param waring_repo_usage_rate: **参数解释：** 仓库使用量告警阀值（百分比）。
        :type waring_repo_usage_rate: int
        :param subscript_events: **参数解释：** 通知事件。
        :type subscript_events: list[:class:`huaweicloudsdkcodehub.v4.RepoSubscriptionEventDto`]
        """
        
        super(UpdateNotificationSubscriptionResponse, self).__init__()

        self._repository_id = None
        self._enabled = None
        self._config_source = None
        self._webhook_config = None
        self._waring_repo_usage_rate = None
        self._subscript_events = None
        self.discriminator = None

        if repository_id is not None:
            self.repository_id = repository_id
        if enabled is not None:
            self.enabled = enabled
        if config_source is not None:
            self.config_source = config_source
        if webhook_config is not None:
            self.webhook_config = webhook_config
        if waring_repo_usage_rate is not None:
            self.waring_repo_usage_rate = waring_repo_usage_rate
        if subscript_events is not None:
            self.subscript_events = subscript_events

    @property
    def repository_id(self):
        r"""Gets the repository_id of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 仓库ID。

        :return: The repository_id of this UpdateNotificationSubscriptionResponse.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 仓库ID。

        :param repository_id: The repository_id of this UpdateNotificationSubscriptionResponse.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 开启通知。

        :return: The enabled of this UpdateNotificationSubscriptionResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 开启通知。

        :param enabled: The enabled of this UpdateNotificationSubscriptionResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def config_source(self):
        r"""Gets the config_source of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 配资源。

        :return: The config_source of this UpdateNotificationSubscriptionResponse.
        :rtype: str
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source):
        r"""Sets the config_source of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 配资源。

        :param config_source: The config_source of this UpdateNotificationSubscriptionResponse.
        :type config_source: str
        """
        self._config_source = config_source

    @property
    def webhook_config(self):
        r"""Gets the webhook_config of this UpdateNotificationSubscriptionResponse.

        :return: The webhook_config of this UpdateNotificationSubscriptionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepoWebHookSubscriptionDto`
        """
        return self._webhook_config

    @webhook_config.setter
    def webhook_config(self, webhook_config):
        r"""Sets the webhook_config of this UpdateNotificationSubscriptionResponse.

        :param webhook_config: The webhook_config of this UpdateNotificationSubscriptionResponse.
        :type webhook_config: :class:`huaweicloudsdkcodehub.v4.RepoWebHookSubscriptionDto`
        """
        self._webhook_config = webhook_config

    @property
    def waring_repo_usage_rate(self):
        r"""Gets the waring_repo_usage_rate of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 仓库使用量告警阀值（百分比）。

        :return: The waring_repo_usage_rate of this UpdateNotificationSubscriptionResponse.
        :rtype: int
        """
        return self._waring_repo_usage_rate

    @waring_repo_usage_rate.setter
    def waring_repo_usage_rate(self, waring_repo_usage_rate):
        r"""Sets the waring_repo_usage_rate of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 仓库使用量告警阀值（百分比）。

        :param waring_repo_usage_rate: The waring_repo_usage_rate of this UpdateNotificationSubscriptionResponse.
        :type waring_repo_usage_rate: int
        """
        self._waring_repo_usage_rate = waring_repo_usage_rate

    @property
    def subscript_events(self):
        r"""Gets the subscript_events of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 通知事件。

        :return: The subscript_events of this UpdateNotificationSubscriptionResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RepoSubscriptionEventDto`]
        """
        return self._subscript_events

    @subscript_events.setter
    def subscript_events(self, subscript_events):
        r"""Sets the subscript_events of this UpdateNotificationSubscriptionResponse.

        **参数解释：** 通知事件。

        :param subscript_events: The subscript_events of this UpdateNotificationSubscriptionResponse.
        :type subscript_events: list[:class:`huaweicloudsdkcodehub.v4.RepoSubscriptionEventDto`]
        """
        self._subscript_events = subscript_events

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
        if not isinstance(other, UpdateNotificationSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
