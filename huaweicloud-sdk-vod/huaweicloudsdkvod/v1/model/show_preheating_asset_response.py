# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPreheatingAssetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'preheating_results': 'list[PreheatingResult]'
    }

    attribute_map = {
        'preheating_results': 'preheating_results'
    }

    def __init__(self, preheating_results=None):
        """ShowPreheatingAssetResponse

        The model defined in huaweicloud sdk

        :param preheating_results: 预热任务数组 
        :type preheating_results: list[:class:`huaweicloudsdkvod.v1.PreheatingResult`]
        """
        
        super(ShowPreheatingAssetResponse, self).__init__()

        self._preheating_results = None
        self.discriminator = None

        if preheating_results is not None:
            self.preheating_results = preheating_results

    @property
    def preheating_results(self):
        """Gets the preheating_results of this ShowPreheatingAssetResponse.

        预热任务数组 

        :return: The preheating_results of this ShowPreheatingAssetResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.PreheatingResult`]
        """
        return self._preheating_results

    @preheating_results.setter
    def preheating_results(self, preheating_results):
        """Sets the preheating_results of this ShowPreheatingAssetResponse.

        预热任务数组 

        :param preheating_results: The preheating_results of this ShowPreheatingAssetResponse.
        :type preheating_results: list[:class:`huaweicloudsdkvod.v1.PreheatingResult`]
        """
        self._preheating_results = preheating_results

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
        if not isinstance(other, ShowPreheatingAssetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
