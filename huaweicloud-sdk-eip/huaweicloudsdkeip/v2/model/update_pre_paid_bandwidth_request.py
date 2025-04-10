# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrePaidBandwidthRequest:

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
        'body': 'UpdatePrePaidBandwidthRequestBody'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id',
        'body': 'body'
    }

    def __init__(self, bandwidth_id=None, body=None):
        r"""UpdatePrePaidBandwidthRequest

        The model defined in huaweicloud sdk

        :param bandwidth_id: 带宽唯一标识。通过弹性公网IP详情获取，且此弹性公网IP是包周期的。
        :type bandwidth_id: str
        :param body: Body of the UpdatePrePaidBandwidthRequest
        :type body: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthRequestBody`
        """
        
        

        self._bandwidth_id = None
        self._body = None
        self.discriminator = None

        self.bandwidth_id = bandwidth_id
        if body is not None:
            self.body = body

    @property
    def bandwidth_id(self):
        r"""Gets the bandwidth_id of this UpdatePrePaidBandwidthRequest.

        带宽唯一标识。通过弹性公网IP详情获取，且此弹性公网IP是包周期的。

        :return: The bandwidth_id of this UpdatePrePaidBandwidthRequest.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        r"""Sets the bandwidth_id of this UpdatePrePaidBandwidthRequest.

        带宽唯一标识。通过弹性公网IP详情获取，且此弹性公网IP是包周期的。

        :param bandwidth_id: The bandwidth_id of this UpdatePrePaidBandwidthRequest.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePrePaidBandwidthRequest.

        :return: The body of this UpdatePrePaidBandwidthRequest.
        :rtype: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePrePaidBandwidthRequest.

        :param body: The body of this UpdatePrePaidBandwidthRequest.
        :type body: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthRequestBody`
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
        if not isinstance(other, UpdatePrePaidBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
