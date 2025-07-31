# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterTimezoneReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_timezone': 'str'
    }

    attribute_map = {
        'cluster_timezone': 'cluster_timezone'
    }

    def __init__(self, cluster_timezone=None):
        r"""ClusterTimezoneReq

        The model defined in huaweicloud sdk

        :param cluster_timezone: **参数解释**：   时区。示例值：UTC。   **约束限制**：   不涉及。   **取值范围**：  ^(Etc/GMT\\+11|US/Hawaii|Etc/GMT\\+9|US/Alaska|US/Pacific|Etc/GMT\\+8|Canada/Mountain|US/Arizona|Canada/Saskatchewan|Etc/GMT\\+6|US/Central|EST|America/Bogota|Etc/GMT\\+5|Canada/Atlantic|America/Cuiaba|America/Buenos_Aires|Etc/GMT\\+3|Canada/Newfoundland|America/Santiago|Etc/GMT\\+2|Atlantic/Cape_Verde|Europe/London|Africa/Monrovia|UTC|Europe/Belgrade|CET|MET|Europe/Amsterdam|EET|Europe/Athens|Asia/Amman|Asia/Beirut|Europe/Minsk|Africa/Nairobi|Europe/Moscow|Etc/GMT-4|Asia/Tbilisi|Asia/Kabul|Etc/GMT-5|Asia/Calcutta|Etc/GMT-6|Etc/GMT-7|PRC|Asia/Shanghai|Etc/GMT-8|Australia/Perth|Asia/Seoul|Asia/Tokyo|Australia/Darwin|Australia/Adelaide|Australia/Sydney|Australia/Brisbane|Etc/GMT-11|Pacific/Auckland|Etc/GMT-12)$   **默认取值**：   不涉及。
        :type cluster_timezone: str
        """
        
        

        self._cluster_timezone = None
        self.discriminator = None

        if cluster_timezone is not None:
            self.cluster_timezone = cluster_timezone

    @property
    def cluster_timezone(self):
        r"""Gets the cluster_timezone of this ClusterTimezoneReq.

        **参数解释**：   时区。示例值：UTC。   **约束限制**：   不涉及。   **取值范围**：  ^(Etc/GMT\\+11|US/Hawaii|Etc/GMT\\+9|US/Alaska|US/Pacific|Etc/GMT\\+8|Canada/Mountain|US/Arizona|Canada/Saskatchewan|Etc/GMT\\+6|US/Central|EST|America/Bogota|Etc/GMT\\+5|Canada/Atlantic|America/Cuiaba|America/Buenos_Aires|Etc/GMT\\+3|Canada/Newfoundland|America/Santiago|Etc/GMT\\+2|Atlantic/Cape_Verde|Europe/London|Africa/Monrovia|UTC|Europe/Belgrade|CET|MET|Europe/Amsterdam|EET|Europe/Athens|Asia/Amman|Asia/Beirut|Europe/Minsk|Africa/Nairobi|Europe/Moscow|Etc/GMT-4|Asia/Tbilisi|Asia/Kabul|Etc/GMT-5|Asia/Calcutta|Etc/GMT-6|Etc/GMT-7|PRC|Asia/Shanghai|Etc/GMT-8|Australia/Perth|Asia/Seoul|Asia/Tokyo|Australia/Darwin|Australia/Adelaide|Australia/Sydney|Australia/Brisbane|Etc/GMT-11|Pacific/Auckland|Etc/GMT-12)$   **默认取值**：   不涉及。

        :return: The cluster_timezone of this ClusterTimezoneReq.
        :rtype: str
        """
        return self._cluster_timezone

    @cluster_timezone.setter
    def cluster_timezone(self, cluster_timezone):
        r"""Sets the cluster_timezone of this ClusterTimezoneReq.

        **参数解释**：   时区。示例值：UTC。   **约束限制**：   不涉及。   **取值范围**：  ^(Etc/GMT\\+11|US/Hawaii|Etc/GMT\\+9|US/Alaska|US/Pacific|Etc/GMT\\+8|Canada/Mountain|US/Arizona|Canada/Saskatchewan|Etc/GMT\\+6|US/Central|EST|America/Bogota|Etc/GMT\\+5|Canada/Atlantic|America/Cuiaba|America/Buenos_Aires|Etc/GMT\\+3|Canada/Newfoundland|America/Santiago|Etc/GMT\\+2|Atlantic/Cape_Verde|Europe/London|Africa/Monrovia|UTC|Europe/Belgrade|CET|MET|Europe/Amsterdam|EET|Europe/Athens|Asia/Amman|Asia/Beirut|Europe/Minsk|Africa/Nairobi|Europe/Moscow|Etc/GMT-4|Asia/Tbilisi|Asia/Kabul|Etc/GMT-5|Asia/Calcutta|Etc/GMT-6|Etc/GMT-7|PRC|Asia/Shanghai|Etc/GMT-8|Australia/Perth|Asia/Seoul|Asia/Tokyo|Australia/Darwin|Australia/Adelaide|Australia/Sydney|Australia/Brisbane|Etc/GMT-11|Pacific/Auckland|Etc/GMT-12)$   **默认取值**：   不涉及。

        :param cluster_timezone: The cluster_timezone of this ClusterTimezoneReq.
        :type cluster_timezone: str
        """
        self._cluster_timezone = cluster_timezone

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
        if not isinstance(other, ClusterTimezoneReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
