# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteResourceTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_resources': 'list[TagDeleteResponseItem]'
    }

    attribute_map = {
        'failed_resources': 'failed_resources'
    }

    def __init__(self, failed_resources=None):
        """DeleteResourceTagResponse

        The model defined in huaweicloud sdk

        :param failed_resources: 查询标签下的资源
        :type failed_resources: list[:class:`huaweicloudsdktms.v1.TagDeleteResponseItem`]
        """
        
        super(DeleteResourceTagResponse, self).__init__()

        self._failed_resources = None
        self.discriminator = None

        if failed_resources is not None:
            self.failed_resources = failed_resources

    @property
    def failed_resources(self):
        """Gets the failed_resources of this DeleteResourceTagResponse.

        查询标签下的资源

        :return: The failed_resources of this DeleteResourceTagResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.TagDeleteResponseItem`]
        """
        return self._failed_resources

    @failed_resources.setter
    def failed_resources(self, failed_resources):
        """Sets the failed_resources of this DeleteResourceTagResponse.

        查询标签下的资源

        :param failed_resources: The failed_resources of this DeleteResourceTagResponse.
        :type failed_resources: list[:class:`huaweicloudsdktms.v1.TagDeleteResponseItem`]
        """
        self._failed_resources = failed_resources

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
        if not isinstance(other, DeleteResourceTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
