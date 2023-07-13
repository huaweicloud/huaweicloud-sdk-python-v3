# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenewalResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_ids': 'list[str]',
        'fail_resource_infos': 'list[FailResourceInfo]'
    }

    attribute_map = {
        'order_ids': 'order_ids',
        'fail_resource_infos': 'fail_resource_infos'
    }

    def __init__(self, order_ids=None, fail_resource_infos=None):
        """RenewalResourcesResponse

        The model defined in huaweicloud sdk

        :param order_ids: 续订资源生成的订单ID的列表。
        :type order_ids: list[str]
        :param fail_resource_infos: |参数名称：失败的资源信息列表| |参数的约束及描述：套餐包使用量信息|
        :type fail_resource_infos: list[:class:`huaweicloudsdkbssintl.v2.FailResourceInfo`]
        """
        
        super(RenewalResourcesResponse, self).__init__()

        self._order_ids = None
        self._fail_resource_infos = None
        self.discriminator = None

        if order_ids is not None:
            self.order_ids = order_ids
        if fail_resource_infos is not None:
            self.fail_resource_infos = fail_resource_infos

    @property
    def order_ids(self):
        """Gets the order_ids of this RenewalResourcesResponse.

        续订资源生成的订单ID的列表。

        :return: The order_ids of this RenewalResourcesResponse.
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this RenewalResourcesResponse.

        续订资源生成的订单ID的列表。

        :param order_ids: The order_ids of this RenewalResourcesResponse.
        :type order_ids: list[str]
        """
        self._order_ids = order_ids

    @property
    def fail_resource_infos(self):
        """Gets the fail_resource_infos of this RenewalResourcesResponse.

        |参数名称：失败的资源信息列表| |参数的约束及描述：套餐包使用量信息|

        :return: The fail_resource_infos of this RenewalResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.FailResourceInfo`]
        """
        return self._fail_resource_infos

    @fail_resource_infos.setter
    def fail_resource_infos(self, fail_resource_infos):
        """Sets the fail_resource_infos of this RenewalResourcesResponse.

        |参数名称：失败的资源信息列表| |参数的约束及描述：套餐包使用量信息|

        :param fail_resource_infos: The fail_resource_infos of this RenewalResourcesResponse.
        :type fail_resource_infos: list[:class:`huaweicloudsdkbssintl.v2.FailResourceInfo`]
        """
        self._fail_resource_infos = fail_resource_infos

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
        if not isinstance(other, RenewalResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
