# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePublicZoneRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_id': 'str',
        'body': 'UpdatePublicZoneInfo'
    }

    attribute_map = {
        'zone_id': 'zone_id',
        'body': 'body'
    }

    def __init__(self, zone_id=None, body=None):
        r"""UpdatePublicZoneRequest

        The model defined in huaweicloud sdk

        :param zone_id: 域名ID。
        :type zone_id: str
        :param body: Body of the UpdatePublicZoneRequest
        :type body: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneInfo`
        """
        
        

        self._zone_id = None
        self._body = None
        self.discriminator = None

        self.zone_id = zone_id
        if body is not None:
            self.body = body

    @property
    def zone_id(self):
        r"""Gets the zone_id of this UpdatePublicZoneRequest.

        域名ID。

        :return: The zone_id of this UpdatePublicZoneRequest.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this UpdatePublicZoneRequest.

        域名ID。

        :param zone_id: The zone_id of this UpdatePublicZoneRequest.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePublicZoneRequest.

        :return: The body of this UpdatePublicZoneRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePublicZoneRequest.

        :param body: The body of this UpdatePublicZoneRequest.
        :type body: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneInfo`
        """
        self._body = body

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
        if not isinstance(other, UpdatePublicZoneRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
