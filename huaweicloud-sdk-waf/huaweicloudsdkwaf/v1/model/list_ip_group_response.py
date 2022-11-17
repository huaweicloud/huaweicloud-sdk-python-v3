# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'items': 'list[IpGroupBody]',
        'cloud_total': 'int'
    }

    attribute_map = {
        'total': 'total',
        'items': 'items',
        'cloud_total': 'cloudTotal'
    }

    def __init__(self, total=None, items=None, cloud_total=None):
        """ListIpGroupResponse

        The model defined in huaweicloud sdk

        :param total: 该用户当前企业项目下Ip地址组数量，只包含本地地址组
        :type total: int
        :param items: 地址组信息列表
        :type items: list[:class:`huaweicloudsdkwaf.v1.IpGroupBody`]
        :param cloud_total: 该用户总的Ip地址组数量，包含本地与共享地址组
        :type cloud_total: int
        """
        
        super(ListIpGroupResponse, self).__init__()

        self._total = None
        self._items = None
        self._cloud_total = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if items is not None:
            self.items = items
        if cloud_total is not None:
            self.cloud_total = cloud_total

    @property
    def total(self):
        """Gets the total of this ListIpGroupResponse.

        该用户当前企业项目下Ip地址组数量，只包含本地地址组

        :return: The total of this ListIpGroupResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListIpGroupResponse.

        该用户当前企业项目下Ip地址组数量，只包含本地地址组

        :param total: The total of this ListIpGroupResponse.
        :type total: int
        """
        self._total = total

    @property
    def items(self):
        """Gets the items of this ListIpGroupResponse.

        地址组信息列表

        :return: The items of this ListIpGroupResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.IpGroupBody`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListIpGroupResponse.

        地址组信息列表

        :param items: The items of this ListIpGroupResponse.
        :type items: list[:class:`huaweicloudsdkwaf.v1.IpGroupBody`]
        """
        self._items = items

    @property
    def cloud_total(self):
        """Gets the cloud_total of this ListIpGroupResponse.

        该用户总的Ip地址组数量，包含本地与共享地址组

        :return: The cloud_total of this ListIpGroupResponse.
        :rtype: int
        """
        return self._cloud_total

    @cloud_total.setter
    def cloud_total(self, cloud_total):
        """Sets the cloud_total of this ListIpGroupResponse.

        该用户总的Ip地址组数量，包含本地与共享地址组

        :param cloud_total: The cloud_total of this ListIpGroupResponse.
        :type cloud_total: int
        """
        self._cloud_total = cloud_total

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
        if not isinstance(other, ListIpGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
