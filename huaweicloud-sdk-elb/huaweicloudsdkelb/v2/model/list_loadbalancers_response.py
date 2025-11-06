# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoadbalancersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancers': 'list[LoadbalancerResp]'
    }

    attribute_map = {
        'loadbalancers': 'loadbalancers'
    }

    def __init__(self, loadbalancers=None):
        r"""ListLoadbalancersResponse

        The model defined in huaweicloud sdk

        :param loadbalancers: 负载均衡器对象列表
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v2.LoadbalancerResp`]
        """
        
        super().__init__()

        self._loadbalancers = None
        self.discriminator = None

        if loadbalancers is not None:
            self.loadbalancers = loadbalancers

    @property
    def loadbalancers(self):
        r"""Gets the loadbalancers of this ListLoadbalancersResponse.

        负载均衡器对象列表

        :return: The loadbalancers of this ListLoadbalancersResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v2.LoadbalancerResp`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        r"""Sets the loadbalancers of this ListLoadbalancersResponse.

        负载均衡器对象列表

        :param loadbalancers: The loadbalancers of this ListLoadbalancersResponse.
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v2.LoadbalancerResp`]
        """
        self._loadbalancers = loadbalancers

    def to_dict(self):
        import warnings
        warnings.warn("ListLoadbalancersResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListLoadbalancersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
