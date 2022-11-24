# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetZoneStatusReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'zone_ids': 'zone_ids'
    }

    def __init__(self, status=None, zone_ids=None):
        """BatchSetZoneStatusReq

        The model defined in huaweicloud sdk

        :param status: 待设置Zone状态，当前仅支持DISABLE或ENABLE。
        :type status: str
        :param zone_ids: 待设置Zone状态，当前仅支持DISABLE或ENABLE。
        :type zone_ids: list[str]
        """
        
        

        self._status = None
        self._zone_ids = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def status(self):
        """Gets the status of this BatchSetZoneStatusReq.

        待设置Zone状态，当前仅支持DISABLE或ENABLE。

        :return: The status of this BatchSetZoneStatusReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchSetZoneStatusReq.

        待设置Zone状态，当前仅支持DISABLE或ENABLE。

        :param status: The status of this BatchSetZoneStatusReq.
        :type status: str
        """
        self._status = status

    @property
    def zone_ids(self):
        """Gets the zone_ids of this BatchSetZoneStatusReq.

        待设置Zone状态，当前仅支持DISABLE或ENABLE。

        :return: The zone_ids of this BatchSetZoneStatusReq.
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this BatchSetZoneStatusReq.

        待设置Zone状态，当前仅支持DISABLE或ENABLE。

        :param zone_ids: The zone_ids of this BatchSetZoneStatusReq.
        :type zone_ids: list[str]
        """
        self._zone_ids = zone_ids

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
        if not isinstance(other, BatchSetZoneStatusReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
