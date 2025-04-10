# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionUpdateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'sources': 'list[SubscriptionSource]',
        'targets': 'list[SubscriptionTarget]'
    }

    attribute_map = {
        'description': 'description',
        'sources': 'sources',
        'targets': 'targets'
    }

    def __init__(self, description=None, sources=None, targets=None):
        r"""SubscriptionUpdateReq

        The model defined in huaweicloud sdk

        :param description: 订阅描述
        :type description: str
        :param sources: 订阅事件源列表，字段存在则代表全量更新订阅源
        :type sources: list[:class:`huaweicloudsdkeg.v1.SubscriptionSource`]
        :param targets: 订阅事件目标列表，字段存在则代表全量更新订阅目标
        :type targets: list[:class:`huaweicloudsdkeg.v1.SubscriptionTarget`]
        """
        
        

        self._description = None
        self._sources = None
        self._targets = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if sources is not None:
            self.sources = sources
        if targets is not None:
            self.targets = targets

    @property
    def description(self):
        r"""Gets the description of this SubscriptionUpdateReq.

        订阅描述

        :return: The description of this SubscriptionUpdateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SubscriptionUpdateReq.

        订阅描述

        :param description: The description of this SubscriptionUpdateReq.
        :type description: str
        """
        self._description = description

    @property
    def sources(self):
        r"""Gets the sources of this SubscriptionUpdateReq.

        订阅事件源列表，字段存在则代表全量更新订阅源

        :return: The sources of this SubscriptionUpdateReq.
        :rtype: list[:class:`huaweicloudsdkeg.v1.SubscriptionSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this SubscriptionUpdateReq.

        订阅事件源列表，字段存在则代表全量更新订阅源

        :param sources: The sources of this SubscriptionUpdateReq.
        :type sources: list[:class:`huaweicloudsdkeg.v1.SubscriptionSource`]
        """
        self._sources = sources

    @property
    def targets(self):
        r"""Gets the targets of this SubscriptionUpdateReq.

        订阅事件目标列表，字段存在则代表全量更新订阅目标

        :return: The targets of this SubscriptionUpdateReq.
        :rtype: list[:class:`huaweicloudsdkeg.v1.SubscriptionTarget`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this SubscriptionUpdateReq.

        订阅事件目标列表，字段存在则代表全量更新订阅目标

        :param targets: The targets of this SubscriptionUpdateReq.
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
        if not isinstance(other, SubscriptionUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
