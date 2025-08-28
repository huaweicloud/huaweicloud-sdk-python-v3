# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoadbalancerFeatureResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'features': 'list[LoadbalancerFeature]',
        'request_id': 'str'
    }

    attribute_map = {
        'features': 'features',
        'request_id': 'request_id'
    }

    def __init__(self, features=None, request_id=None):
        r"""ListLoadbalancerFeatureResponse

        The model defined in huaweicloud sdk

        :param features: **参数解释**：ELB实例特性信息列表。
        :type features: list[:class:`huaweicloudsdkelb.v3.LoadbalancerFeature`]
        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        """
        
        super(ListLoadbalancerFeatureResponse, self).__init__()

        self._features = None
        self._request_id = None
        self.discriminator = None

        if features is not None:
            self.features = features
        if request_id is not None:
            self.request_id = request_id

    @property
    def features(self):
        r"""Gets the features of this ListLoadbalancerFeatureResponse.

        **参数解释**：ELB实例特性信息列表。

        :return: The features of this ListLoadbalancerFeatureResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadbalancerFeature`]
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ListLoadbalancerFeatureResponse.

        **参数解释**：ELB实例特性信息列表。

        :param features: The features of this ListLoadbalancerFeatureResponse.
        :type features: list[:class:`huaweicloudsdkelb.v3.LoadbalancerFeature`]
        """
        self._features = features

    @property
    def request_id(self):
        r"""Gets the request_id of this ListLoadbalancerFeatureResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this ListLoadbalancerFeatureResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListLoadbalancerFeatureResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this ListLoadbalancerFeatureResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListLoadbalancerFeatureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
