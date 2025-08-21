# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Overview:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_policies': 'AccessPolicy',
        'assets': 'ChangedVO',
        'attack_event': 'AttackEvent',
        'traffic_peak': 'TrendVO'
    }

    attribute_map = {
        'access_policies': 'access_policies',
        'assets': 'assets',
        'attack_event': 'attack_event',
        'traffic_peak': 'traffic_peak'
    }

    def __init__(self, access_policies=None, assets=None, attack_event=None, traffic_peak=None):
        r"""Overview

        The model defined in huaweicloud sdk

        :param access_policies: 
        :type access_policies: :class:`huaweicloudsdkcfw.v1.AccessPolicy`
        :param assets: 
        :type assets: :class:`huaweicloudsdkcfw.v1.ChangedVO`
        :param attack_event: 
        :type attack_event: :class:`huaweicloudsdkcfw.v1.AttackEvent`
        :param traffic_peak: 
        :type traffic_peak: :class:`huaweicloudsdkcfw.v1.TrendVO`
        """
        
        

        self._access_policies = None
        self._assets = None
        self._attack_event = None
        self._traffic_peak = None
        self.discriminator = None

        if access_policies is not None:
            self.access_policies = access_policies
        if assets is not None:
            self.assets = assets
        if attack_event is not None:
            self.attack_event = attack_event
        if traffic_peak is not None:
            self.traffic_peak = traffic_peak

    @property
    def access_policies(self):
        r"""Gets the access_policies of this Overview.

        :return: The access_policies of this Overview.
        :rtype: :class:`huaweicloudsdkcfw.v1.AccessPolicy`
        """
        return self._access_policies

    @access_policies.setter
    def access_policies(self, access_policies):
        r"""Sets the access_policies of this Overview.

        :param access_policies: The access_policies of this Overview.
        :type access_policies: :class:`huaweicloudsdkcfw.v1.AccessPolicy`
        """
        self._access_policies = access_policies

    @property
    def assets(self):
        r"""Gets the assets of this Overview.

        :return: The assets of this Overview.
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangedVO`
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        r"""Sets the assets of this Overview.

        :param assets: The assets of this Overview.
        :type assets: :class:`huaweicloudsdkcfw.v1.ChangedVO`
        """
        self._assets = assets

    @property
    def attack_event(self):
        r"""Gets the attack_event of this Overview.

        :return: The attack_event of this Overview.
        :rtype: :class:`huaweicloudsdkcfw.v1.AttackEvent`
        """
        return self._attack_event

    @attack_event.setter
    def attack_event(self, attack_event):
        r"""Sets the attack_event of this Overview.

        :param attack_event: The attack_event of this Overview.
        :type attack_event: :class:`huaweicloudsdkcfw.v1.AttackEvent`
        """
        self._attack_event = attack_event

    @property
    def traffic_peak(self):
        r"""Gets the traffic_peak of this Overview.

        :return: The traffic_peak of this Overview.
        :rtype: :class:`huaweicloudsdkcfw.v1.TrendVO`
        """
        return self._traffic_peak

    @traffic_peak.setter
    def traffic_peak(self, traffic_peak):
        r"""Sets the traffic_peak of this Overview.

        :param traffic_peak: The traffic_peak of this Overview.
        :type traffic_peak: :class:`huaweicloudsdkcfw.v1.TrendVO`
        """
        self._traffic_peak = traffic_peak

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
        if not isinstance(other, Overview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
