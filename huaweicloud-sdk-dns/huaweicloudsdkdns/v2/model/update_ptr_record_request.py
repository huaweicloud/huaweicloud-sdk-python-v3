# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePtrRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'floatingip_id': 'str',
        'body': 'UpdatePtrReq'
    }

    attribute_map = {
        'region': 'region',
        'floatingip_id': 'floatingip_id',
        'body': 'body'
    }

    def __init__(self, region=None, floatingip_id=None, body=None):
        r"""UpdatePtrRecordRequest

        The model defined in huaweicloud sdk

        :param region: 域名所属的区域。
        :type region: str
        :param floatingip_id: 弹性公网IP（EIP）的ID。
        :type floatingip_id: str
        :param body: Body of the UpdatePtrRecordRequest
        :type body: :class:`huaweicloudsdkdns.v2.UpdatePtrReq`
        """
        
        

        self._region = None
        self._floatingip_id = None
        self._body = None
        self.discriminator = None

        self.region = region
        self.floatingip_id = floatingip_id
        if body is not None:
            self.body = body

    @property
    def region(self):
        r"""Gets the region of this UpdatePtrRecordRequest.

        域名所属的区域。

        :return: The region of this UpdatePtrRecordRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this UpdatePtrRecordRequest.

        域名所属的区域。

        :param region: The region of this UpdatePtrRecordRequest.
        :type region: str
        """
        self._region = region

    @property
    def floatingip_id(self):
        r"""Gets the floatingip_id of this UpdatePtrRecordRequest.

        弹性公网IP（EIP）的ID。

        :return: The floatingip_id of this UpdatePtrRecordRequest.
        :rtype: str
        """
        return self._floatingip_id

    @floatingip_id.setter
    def floatingip_id(self, floatingip_id):
        r"""Sets the floatingip_id of this UpdatePtrRecordRequest.

        弹性公网IP（EIP）的ID。

        :param floatingip_id: The floatingip_id of this UpdatePtrRecordRequest.
        :type floatingip_id: str
        """
        self._floatingip_id = floatingip_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePtrRecordRequest.

        :return: The body of this UpdatePtrRecordRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePtrReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePtrRecordRequest.

        :param body: The body of this UpdatePtrRecordRequest.
        :type body: :class:`huaweicloudsdkdns.v2.UpdatePtrReq`
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
        if not isinstance(other, UpdatePtrRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
