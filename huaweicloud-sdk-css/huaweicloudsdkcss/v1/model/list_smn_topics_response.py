# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmnTopicsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics_name': 'list[str]'
    }

    attribute_map = {
        'topics_name': 'topicsName'
    }

    def __init__(self, topics_name=None):
        """ListSmnTopicsResponse

        The model defined in huaweicloud sdk

        :param topics_name: SMN主题名称列表。
        :type topics_name: list[str]
        """
        
        super(ListSmnTopicsResponse, self).__init__()

        self._topics_name = None
        self.discriminator = None

        if topics_name is not None:
            self.topics_name = topics_name

    @property
    def topics_name(self):
        """Gets the topics_name of this ListSmnTopicsResponse.

        SMN主题名称列表。

        :return: The topics_name of this ListSmnTopicsResponse.
        :rtype: list[str]
        """
        return self._topics_name

    @topics_name.setter
    def topics_name(self, topics_name):
        """Sets the topics_name of this ListSmnTopicsResponse.

        SMN主题名称列表。

        :param topics_name: The topics_name of this ListSmnTopicsResponse.
        :type topics_name: list[str]
        """
        self._topics_name = topics_name

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
        if not isinstance(other, ListSmnTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
