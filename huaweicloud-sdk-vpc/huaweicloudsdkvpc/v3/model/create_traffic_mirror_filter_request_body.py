# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrafficMirrorFilterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_mirror_filter': 'CreateTrafficMirrorFilterOption'
    }

    attribute_map = {
        'traffic_mirror_filter': 'traffic_mirror_filter'
    }

    def __init__(self, traffic_mirror_filter=None):
        """CreateTrafficMirrorFilterRequestBody

        The model defined in huaweicloud sdk

        :param traffic_mirror_filter: 
        :type traffic_mirror_filter: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorFilterOption`
        """
        
        

        self._traffic_mirror_filter = None
        self.discriminator = None

        self.traffic_mirror_filter = traffic_mirror_filter

    @property
    def traffic_mirror_filter(self):
        """Gets the traffic_mirror_filter of this CreateTrafficMirrorFilterRequestBody.

        :return: The traffic_mirror_filter of this CreateTrafficMirrorFilterRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorFilterOption`
        """
        return self._traffic_mirror_filter

    @traffic_mirror_filter.setter
    def traffic_mirror_filter(self, traffic_mirror_filter):
        """Sets the traffic_mirror_filter of this CreateTrafficMirrorFilterRequestBody.

        :param traffic_mirror_filter: The traffic_mirror_filter of this CreateTrafficMirrorFilterRequestBody.
        :type traffic_mirror_filter: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorFilterOption`
        """
        self._traffic_mirror_filter = traffic_mirror_filter

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
        if not isinstance(other, CreateTrafficMirrorFilterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
