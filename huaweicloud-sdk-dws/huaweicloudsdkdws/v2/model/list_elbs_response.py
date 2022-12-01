# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListElbsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elbs': 'list[ClusterElbInfo]'
    }

    attribute_map = {
        'elbs': 'elbs'
    }

    def __init__(self, elbs=None):
        """ListElbsResponse

        The model defined in huaweicloud sdk

        :param elbs: 弹性负载均衡列表
        :type elbs: list[:class:`huaweicloudsdkdws.v2.ClusterElbInfo`]
        """
        
        super(ListElbsResponse, self).__init__()

        self._elbs = None
        self.discriminator = None

        if elbs is not None:
            self.elbs = elbs

    @property
    def elbs(self):
        """Gets the elbs of this ListElbsResponse.

        弹性负载均衡列表

        :return: The elbs of this ListElbsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ClusterElbInfo`]
        """
        return self._elbs

    @elbs.setter
    def elbs(self, elbs):
        """Sets the elbs of this ListElbsResponse.

        弹性负载均衡列表

        :param elbs: The elbs of this ListElbsResponse.
        :type elbs: list[:class:`huaweicloudsdkdws.v2.ClusterElbInfo`]
        """
        self._elbs = elbs

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
        if not isinstance(other, ListElbsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
