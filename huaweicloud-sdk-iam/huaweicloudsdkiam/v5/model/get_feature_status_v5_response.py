# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetFeatureStatusV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature_status': 'FeatureStatus'
    }

    attribute_map = {
        'feature_status': 'feature_status'
    }

    def __init__(self, feature_status=None):
        r"""GetFeatureStatusV5Response

        The model defined in huaweicloud sdk

        :param feature_status: 
        :type feature_status: :class:`huaweicloudsdkiam.v5.FeatureStatus`
        """
        
        super(GetFeatureStatusV5Response, self).__init__()

        self._feature_status = None
        self.discriminator = None

        if feature_status is not None:
            self.feature_status = feature_status

    @property
    def feature_status(self):
        r"""Gets the feature_status of this GetFeatureStatusV5Response.

        :return: The feature_status of this GetFeatureStatusV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.FeatureStatus`
        """
        return self._feature_status

    @feature_status.setter
    def feature_status(self, feature_status):
        r"""Sets the feature_status of this GetFeatureStatusV5Response.

        :param feature_status: The feature_status of this GetFeatureStatusV5Response.
        :type feature_status: :class:`huaweicloudsdkiam.v5.FeatureStatus`
        """
        self._feature_status = feature_status

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
        if not isinstance(other, GetFeatureStatusV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
