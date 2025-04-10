# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAggregationAuthorizationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregation_authorizations': 'list[AggregationAuthorizationResp]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'aggregation_authorizations': 'aggregation_authorizations',
        'page_info': 'page_info'
    }

    def __init__(self, aggregation_authorizations=None, page_info=None):
        r"""ListAggregationAuthorizationsResponse

        The model defined in huaweicloud sdk

        :param aggregation_authorizations: 授权过的资源聚合器帐号列表。
        :type aggregation_authorizations: list[:class:`huaweicloudsdkconfig.v1.AggregationAuthorizationResp`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        
        super(ListAggregationAuthorizationsResponse, self).__init__()

        self._aggregation_authorizations = None
        self._page_info = None
        self.discriminator = None

        if aggregation_authorizations is not None:
            self.aggregation_authorizations = aggregation_authorizations
        if page_info is not None:
            self.page_info = page_info

    @property
    def aggregation_authorizations(self):
        r"""Gets the aggregation_authorizations of this ListAggregationAuthorizationsResponse.

        授权过的资源聚合器帐号列表。

        :return: The aggregation_authorizations of this ListAggregationAuthorizationsResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.AggregationAuthorizationResp`]
        """
        return self._aggregation_authorizations

    @aggregation_authorizations.setter
    def aggregation_authorizations(self, aggregation_authorizations):
        r"""Sets the aggregation_authorizations of this ListAggregationAuthorizationsResponse.

        授权过的资源聚合器帐号列表。

        :param aggregation_authorizations: The aggregation_authorizations of this ListAggregationAuthorizationsResponse.
        :type aggregation_authorizations: list[:class:`huaweicloudsdkconfig.v1.AggregationAuthorizationResp`]
        """
        self._aggregation_authorizations = aggregation_authorizations

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAggregationAuthorizationsResponse.

        :return: The page_info of this ListAggregationAuthorizationsResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAggregationAuthorizationsResponse.

        :param page_info: The page_info of this ListAggregationAuthorizationsResponse.
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAggregationAuthorizationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
