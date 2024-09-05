# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrackerConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel': 'ChannelConfigBody',
        'selector': 'SelectorConfigBody',
        'retention_period_in_days': 'int',
        'agency_name': 'str',
        'domain_id': 'str',
        'frozen_status': 'FrozenStatus'
    }

    attribute_map = {
        'channel': 'channel',
        'selector': 'selector',
        'retention_period_in_days': 'retention_period_in_days',
        'agency_name': 'agency_name',
        'domain_id': 'domain_id',
        'frozen_status': 'frozen_status'
    }

    def __init__(self, channel=None, selector=None, retention_period_in_days=None, agency_name=None, domain_id=None, frozen_status=None):
        """TrackerConfigBody

        The model defined in huaweicloud sdk

        :param channel: 
        :type channel: :class:`huaweicloudsdkconfig.v1.ChannelConfigBody`
        :param selector: 
        :type selector: :class:`huaweicloudsdkconfig.v1.SelectorConfigBody`
        :param retention_period_in_days: 存储历史信息的天数
        :type retention_period_in_days: int
        :param agency_name: IAM委托名称
        :type agency_name: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param frozen_status: 
        :type frozen_status: :class:`huaweicloudsdkconfig.v1.FrozenStatus`
        """
        
        

        self._channel = None
        self._selector = None
        self._retention_period_in_days = None
        self._agency_name = None
        self._domain_id = None
        self._frozen_status = None
        self.discriminator = None

        self.channel = channel
        self.selector = selector
        if retention_period_in_days is not None:
            self.retention_period_in_days = retention_period_in_days
        self.agency_name = agency_name
        if domain_id is not None:
            self.domain_id = domain_id
        if frozen_status is not None:
            self.frozen_status = frozen_status

    @property
    def channel(self):
        """Gets the channel of this TrackerConfigBody.

        :return: The channel of this TrackerConfigBody.
        :rtype: :class:`huaweicloudsdkconfig.v1.ChannelConfigBody`
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this TrackerConfigBody.

        :param channel: The channel of this TrackerConfigBody.
        :type channel: :class:`huaweicloudsdkconfig.v1.ChannelConfigBody`
        """
        self._channel = channel

    @property
    def selector(self):
        """Gets the selector of this TrackerConfigBody.

        :return: The selector of this TrackerConfigBody.
        :rtype: :class:`huaweicloudsdkconfig.v1.SelectorConfigBody`
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this TrackerConfigBody.

        :param selector: The selector of this TrackerConfigBody.
        :type selector: :class:`huaweicloudsdkconfig.v1.SelectorConfigBody`
        """
        self._selector = selector

    @property
    def retention_period_in_days(self):
        """Gets the retention_period_in_days of this TrackerConfigBody.

        存储历史信息的天数

        :return: The retention_period_in_days of this TrackerConfigBody.
        :rtype: int
        """
        return self._retention_period_in_days

    @retention_period_in_days.setter
    def retention_period_in_days(self, retention_period_in_days):
        """Sets the retention_period_in_days of this TrackerConfigBody.

        存储历史信息的天数

        :param retention_period_in_days: The retention_period_in_days of this TrackerConfigBody.
        :type retention_period_in_days: int
        """
        self._retention_period_in_days = retention_period_in_days

    @property
    def agency_name(self):
        """Gets the agency_name of this TrackerConfigBody.

        IAM委托名称

        :return: The agency_name of this TrackerConfigBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this TrackerConfigBody.

        IAM委托名称

        :param agency_name: The agency_name of this TrackerConfigBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def domain_id(self):
        """Gets the domain_id of this TrackerConfigBody.

        账号ID

        :return: The domain_id of this TrackerConfigBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this TrackerConfigBody.

        账号ID

        :param domain_id: The domain_id of this TrackerConfigBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def frozen_status(self):
        """Gets the frozen_status of this TrackerConfigBody.

        :return: The frozen_status of this TrackerConfigBody.
        :rtype: :class:`huaweicloudsdkconfig.v1.FrozenStatus`
        """
        return self._frozen_status

    @frozen_status.setter
    def frozen_status(self, frozen_status):
        """Sets the frozen_status of this TrackerConfigBody.

        :param frozen_status: The frozen_status of this TrackerConfigBody.
        :type frozen_status: :class:`huaweicloudsdkconfig.v1.FrozenStatus`
        """
        self._frozen_status = frozen_status

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
        if not isinstance(other, TrackerConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
