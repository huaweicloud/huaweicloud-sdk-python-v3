# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTrafficMirrorFilterRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_mirror_filter_id': 'str'
    }

    attribute_map = {
        'traffic_mirror_filter_id': 'traffic_mirror_filter_id'
    }

    def __init__(self, traffic_mirror_filter_id=None):
        r"""DeleteTrafficMirrorFilterRequest

        The model defined in huaweicloud sdk

        :param traffic_mirror_filter_id: 流量镜像筛选条件ID
        :type traffic_mirror_filter_id: str
        """
        
        

        self._traffic_mirror_filter_id = None
        self.discriminator = None

        self.traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def traffic_mirror_filter_id(self):
        r"""Gets the traffic_mirror_filter_id of this DeleteTrafficMirrorFilterRequest.

        流量镜像筛选条件ID

        :return: The traffic_mirror_filter_id of this DeleteTrafficMirrorFilterRequest.
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        r"""Sets the traffic_mirror_filter_id of this DeleteTrafficMirrorFilterRequest.

        流量镜像筛选条件ID

        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this DeleteTrafficMirrorFilterRequest.
        :type traffic_mirror_filter_id: str
        """
        self._traffic_mirror_filter_id = traffic_mirror_filter_id

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
        if not isinstance(other, DeleteTrafficMirrorFilterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
