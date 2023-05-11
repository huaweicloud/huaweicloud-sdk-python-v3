# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBandwidthRequest:

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
        'body': 'UpdateBandwidthRequestBody'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id',
        'body': 'body'
    }

    def __init__(self, bandwidth_id=None, body=None):
        """UpdateBandwidthRequest

        The model defined in huaweicloud sdk

        :param bandwidth_id: 带宽唯一标识
        :type bandwidth_id: str
        :param body: Body of the UpdateBandwidthRequest
        :type body: :class:`huaweicloudsdkeip.v2.UpdateBandwidthRequestBody`
        """
        
        

        self._bandwidth_id = None
        self._body = None
        self.discriminator = None

        self.bandwidth_id = bandwidth_id
        if body is not None:
            self.body = body

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this UpdateBandwidthRequest.

        带宽唯一标识

        :return: The bandwidth_id of this UpdateBandwidthRequest.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this UpdateBandwidthRequest.

        带宽唯一标识

        :param bandwidth_id: The bandwidth_id of this UpdateBandwidthRequest.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def body(self):
        """Gets the body of this UpdateBandwidthRequest.

        :return: The body of this UpdateBandwidthRequest.
        :rtype: :class:`huaweicloudsdkeip.v2.UpdateBandwidthRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateBandwidthRequest.

        :param body: The body of this UpdateBandwidthRequest.
        :type body: :class:`huaweicloudsdkeip.v2.UpdateBandwidthRequestBody`
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
        if not isinstance(other, UpdateBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
