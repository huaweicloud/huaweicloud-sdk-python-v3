# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubnetBandwidthRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_id': 'str',
        'body': 'UpdateSubnetBandwidthReq'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id',
        'body': 'body'
    }

    def __init__(self, bandwidth_id=None, body=None):
        r"""UpdateSubnetBandwidthRequest

        The model defined in huaweicloud sdk

        :param bandwidth_id: 云办公带宽id。
        :type bandwidth_id: str
        :param body: Body of the UpdateSubnetBandwidthRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetBandwidthReq`
        """
        
        

        self._bandwidth_id = None
        self._body = None
        self.discriminator = None

        self.bandwidth_id = bandwidth_id
        if body is not None:
            self.body = body

    @property
    def bandwidth_id(self):
        r"""Gets the bandwidth_id of this UpdateSubnetBandwidthRequest.

        云办公带宽id。

        :return: The bandwidth_id of this UpdateSubnetBandwidthRequest.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        r"""Sets the bandwidth_id of this UpdateSubnetBandwidthRequest.

        云办公带宽id。

        :param bandwidth_id: The bandwidth_id of this UpdateSubnetBandwidthRequest.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def body(self):
        r"""Gets the body of this UpdateSubnetBandwidthRequest.

        :return: The body of this UpdateSubnetBandwidthRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetBandwidthReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateSubnetBandwidthRequest.

        :param body: The body of this UpdateSubnetBandwidthRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateSubnetBandwidthReq`
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
        if not isinstance(other, UpdateSubnetBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
