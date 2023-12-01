# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublisherResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publisher_detail_map': 'dict(str, PublisherVO)'
    }

    attribute_map = {
        'publisher_detail_map': 'publisher_detail_map'
    }

    def __init__(self, publisher_detail_map=None):
        """ShowPublisherResponse

        The model defined in huaweicloud sdk

        :param publisher_detail_map: 发布商详情
        :type publisher_detail_map: dict(str, PublisherVO)
        """
        
        super(ShowPublisherResponse, self).__init__()

        self._publisher_detail_map = None
        self.discriminator = None

        if publisher_detail_map is not None:
            self.publisher_detail_map = publisher_detail_map

    @property
    def publisher_detail_map(self):
        """Gets the publisher_detail_map of this ShowPublisherResponse.

        发布商详情

        :return: The publisher_detail_map of this ShowPublisherResponse.
        :rtype: dict(str, PublisherVO)
        """
        return self._publisher_detail_map

    @publisher_detail_map.setter
    def publisher_detail_map(self, publisher_detail_map):
        """Sets the publisher_detail_map of this ShowPublisherResponse.

        发布商详情

        :param publisher_detail_map: The publisher_detail_map of this ShowPublisherResponse.
        :type publisher_detail_map: dict(str, PublisherVO)
        """
        self._publisher_detail_map = publisher_detail_map

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
        if not isinstance(other, ShowPublisherResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
