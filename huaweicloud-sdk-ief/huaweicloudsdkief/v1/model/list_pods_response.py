# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPodsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'pods': 'list[PodResp]'
    }

    attribute_map = {
        'count': 'count',
        'pods': 'pods'
    }

    def __init__(self, count=None, pods=None):
        """ListPodsResponse

        The model defined in huaweicloud sdk

        :param count: 应用实例总数
        :type count: int
        :param pods: 应用实例列表
        :type pods: list[:class:`huaweicloudsdkief.v1.PodResp`]
        """
        
        super(ListPodsResponse, self).__init__()

        self._count = None
        self._pods = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if pods is not None:
            self.pods = pods

    @property
    def count(self):
        """Gets the count of this ListPodsResponse.

        应用实例总数

        :return: The count of this ListPodsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListPodsResponse.

        应用实例总数

        :param count: The count of this ListPodsResponse.
        :type count: int
        """
        self._count = count

    @property
    def pods(self):
        """Gets the pods of this ListPodsResponse.

        应用实例列表

        :return: The pods of this ListPodsResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.PodResp`]
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """Sets the pods of this ListPodsResponse.

        应用实例列表

        :param pods: The pods of this ListPodsResponse.
        :type pods: list[:class:`huaweicloudsdkief.v1.PodResp`]
        """
        self._pods = pods

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
        if not isinstance(other, ListPodsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
