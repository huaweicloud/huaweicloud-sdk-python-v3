# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFeaturesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'features': 'list[FeatureResult]'
    }

    attribute_map = {
        'features': 'features'
    }

    def __init__(self, features=None):
        r"""ListFeaturesResponse

        The model defined in huaweicloud sdk

        :param features: 高级特性列表。
        :type features: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FeatureResult`]
        """
        
        super(ListFeaturesResponse, self).__init__()

        self._features = None
        self.discriminator = None

        if features is not None:
            self.features = features

    @property
    def features(self):
        r"""Gets the features of this ListFeaturesResponse.

        高级特性列表。

        :return: The features of this ListFeaturesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FeatureResult`]
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ListFeaturesResponse.

        高级特性列表。

        :param features: The features of this ListFeaturesResponse.
        :type features: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FeatureResult`]
        """
        self._features = features

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
        if not isinstance(other, ListFeaturesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
