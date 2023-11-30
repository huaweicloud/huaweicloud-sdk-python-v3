# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchModifyBandwidthResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_resources': 'list[SuccessResources]',
        'failure_resources': 'list[FailureResources]'
    }

    attribute_map = {
        'success_resources': 'success_resources',
        'failure_resources': 'failure_resources'
    }

    def __init__(self, success_resources=None, failure_resources=None):
        """BatchModifyBandwidthResponse

        The model defined in huaweicloud sdk

        :param success_resources: 成功资源
        :type success_resources: list[:class:`huaweicloudsdkeip.v2.SuccessResources`]
        :param failure_resources: 失败资源
        :type failure_resources: list[:class:`huaweicloudsdkeip.v2.FailureResources`]
        """
        
        super(BatchModifyBandwidthResponse, self).__init__()

        self._success_resources = None
        self._failure_resources = None
        self.discriminator = None

        if success_resources is not None:
            self.success_resources = success_resources
        if failure_resources is not None:
            self.failure_resources = failure_resources

    @property
    def success_resources(self):
        """Gets the success_resources of this BatchModifyBandwidthResponse.

        成功资源

        :return: The success_resources of this BatchModifyBandwidthResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v2.SuccessResources`]
        """
        return self._success_resources

    @success_resources.setter
    def success_resources(self, success_resources):
        """Sets the success_resources of this BatchModifyBandwidthResponse.

        成功资源

        :param success_resources: The success_resources of this BatchModifyBandwidthResponse.
        :type success_resources: list[:class:`huaweicloudsdkeip.v2.SuccessResources`]
        """
        self._success_resources = success_resources

    @property
    def failure_resources(self):
        """Gets the failure_resources of this BatchModifyBandwidthResponse.

        失败资源

        :return: The failure_resources of this BatchModifyBandwidthResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v2.FailureResources`]
        """
        return self._failure_resources

    @failure_resources.setter
    def failure_resources(self, failure_resources):
        """Sets the failure_resources of this BatchModifyBandwidthResponse.

        失败资源

        :param failure_resources: The failure_resources of this BatchModifyBandwidthResponse.
        :type failure_resources: list[:class:`huaweicloudsdkeip.v2.FailureResources`]
        """
        self._failure_resources = failure_resources

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
        if not isinstance(other, BatchModifyBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
