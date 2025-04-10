# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalEipSegmentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_eip_segment': 'CreateGlobalEipSegmentRequestBodyGlobalEipSegment'
    }

    attribute_map = {
        'global_eip_segment': 'global_eip_segment'
    }

    def __init__(self, global_eip_segment=None):
        r"""CreateGlobalEipSegmentRequestBody

        The model defined in huaweicloud sdk

        :param global_eip_segment: 
        :type global_eip_segment: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentRequestBodyGlobalEipSegment`
        """
        
        

        self._global_eip_segment = None
        self.discriminator = None

        self.global_eip_segment = global_eip_segment

    @property
    def global_eip_segment(self):
        r"""Gets the global_eip_segment of this CreateGlobalEipSegmentRequestBody.

        :return: The global_eip_segment of this CreateGlobalEipSegmentRequestBody.
        :rtype: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentRequestBodyGlobalEipSegment`
        """
        return self._global_eip_segment

    @global_eip_segment.setter
    def global_eip_segment(self, global_eip_segment):
        r"""Sets the global_eip_segment of this CreateGlobalEipSegmentRequestBody.

        :param global_eip_segment: The global_eip_segment of this CreateGlobalEipSegmentRequestBody.
        :type global_eip_segment: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentRequestBodyGlobalEipSegment`
        """
        self._global_eip_segment = global_eip_segment

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
        if not isinstance(other, CreateGlobalEipSegmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
