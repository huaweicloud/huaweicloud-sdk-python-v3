# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGlobalEipSegmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_eip_segment_id': 'str',
        'body': 'UpdateGlobalEipSegmentRequestBody'
    }

    attribute_map = {
        'global_eip_segment_id': 'global_eip_segment_id',
        'body': 'body'
    }

    def __init__(self, global_eip_segment_id=None, body=None):
        """UpdateGlobalEipSegmentRequest

        The model defined in huaweicloud sdk

        :param global_eip_segment_id: global_eip_segment_id
        :type global_eip_segment_id: str
        :param body: Body of the UpdateGlobalEipSegmentRequest
        :type body: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipSegmentRequestBody`
        """
        
        

        self._global_eip_segment_id = None
        self._body = None
        self.discriminator = None

        self.global_eip_segment_id = global_eip_segment_id
        if body is not None:
            self.body = body

    @property
    def global_eip_segment_id(self):
        """Gets the global_eip_segment_id of this UpdateGlobalEipSegmentRequest.

        global_eip_segment_id

        :return: The global_eip_segment_id of this UpdateGlobalEipSegmentRequest.
        :rtype: str
        """
        return self._global_eip_segment_id

    @global_eip_segment_id.setter
    def global_eip_segment_id(self, global_eip_segment_id):
        """Sets the global_eip_segment_id of this UpdateGlobalEipSegmentRequest.

        global_eip_segment_id

        :param global_eip_segment_id: The global_eip_segment_id of this UpdateGlobalEipSegmentRequest.
        :type global_eip_segment_id: str
        """
        self._global_eip_segment_id = global_eip_segment_id

    @property
    def body(self):
        """Gets the body of this UpdateGlobalEipSegmentRequest.

        :return: The body of this UpdateGlobalEipSegmentRequest.
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipSegmentRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateGlobalEipSegmentRequest.

        :param body: The body of this UpdateGlobalEipSegmentRequest.
        :type body: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipSegmentRequestBody`
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
        if not isinstance(other, UpdateGlobalEipSegmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
