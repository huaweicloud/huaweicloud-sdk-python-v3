# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'channel_id': 'str',
        'sources': 'list[SubscriptionSource]',
        'targets': 'list[SubscriptionTarget]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'channel_id': 'channel_id',
        'sources': 'sources',
        'targets': 'targets'
    }

    def __init__(self, name=None, description=None, channel_id=None, sources=None, targets=None):
        r"""SubscriptionCreateReq

        The model defined in huaweicloud sdk

        :param name: 订阅名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头
        :type name: str
        :param description: 订阅描述
        :type description: str
        :param channel_id: 所属事件通道ID
        :type channel_id: str
        :param sources: 订阅的事件源列表， 当前仅支持订阅一个事件源
        :type sources: list[:class:`huaweicloudsdkeg.v1.SubscriptionSource`]
        :param targets: 事件目标列表，至少订阅一个事件目标
        :type targets: list[:class:`huaweicloudsdkeg.v1.SubscriptionTarget`]
        """
        
        

        self._name = None
        self._description = None
        self._channel_id = None
        self._sources = None
        self._targets = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.channel_id = channel_id
        self.sources = sources
        self.targets = targets

    @property
    def name(self):
        r"""Gets the name of this SubscriptionCreateReq.

        订阅名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :return: The name of this SubscriptionCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubscriptionCreateReq.

        订阅名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :param name: The name of this SubscriptionCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SubscriptionCreateReq.

        订阅描述

        :return: The description of this SubscriptionCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SubscriptionCreateReq.

        订阅描述

        :param description: The description of this SubscriptionCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def channel_id(self):
        r"""Gets the channel_id of this SubscriptionCreateReq.

        所属事件通道ID

        :return: The channel_id of this SubscriptionCreateReq.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this SubscriptionCreateReq.

        所属事件通道ID

        :param channel_id: The channel_id of this SubscriptionCreateReq.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def sources(self):
        r"""Gets the sources of this SubscriptionCreateReq.

        订阅的事件源列表， 当前仅支持订阅一个事件源

        :return: The sources of this SubscriptionCreateReq.
        :rtype: list[:class:`huaweicloudsdkeg.v1.SubscriptionSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this SubscriptionCreateReq.

        订阅的事件源列表， 当前仅支持订阅一个事件源

        :param sources: The sources of this SubscriptionCreateReq.
        :type sources: list[:class:`huaweicloudsdkeg.v1.SubscriptionSource`]
        """
        self._sources = sources

    @property
    def targets(self):
        r"""Gets the targets of this SubscriptionCreateReq.

        事件目标列表，至少订阅一个事件目标

        :return: The targets of this SubscriptionCreateReq.
        :rtype: list[:class:`huaweicloudsdkeg.v1.SubscriptionTarget`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this SubscriptionCreateReq.

        事件目标列表，至少订阅一个事件目标

        :param targets: The targets of this SubscriptionCreateReq.
        :type targets: list[:class:`huaweicloudsdkeg.v1.SubscriptionTarget`]
        """
        self._targets = targets

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
        if not isinstance(other, SubscriptionCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
