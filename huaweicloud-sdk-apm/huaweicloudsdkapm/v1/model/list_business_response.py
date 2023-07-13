# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBusinessResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_nodes': 'list[BusinessNodeModel]'
    }

    attribute_map = {
        'business_nodes': 'business_nodes'
    }

    def __init__(self, business_nodes=None):
        """ListBusinessResponse

        The model defined in huaweicloud sdk

        :param business_nodes: 获取应用列表数据结构。
        :type business_nodes: list[:class:`huaweicloudsdkapm.v1.BusinessNodeModel`]
        """
        
        super(ListBusinessResponse, self).__init__()

        self._business_nodes = None
        self.discriminator = None

        if business_nodes is not None:
            self.business_nodes = business_nodes

    @property
    def business_nodes(self):
        """Gets the business_nodes of this ListBusinessResponse.

        获取应用列表数据结构。

        :return: The business_nodes of this ListBusinessResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.BusinessNodeModel`]
        """
        return self._business_nodes

    @business_nodes.setter
    def business_nodes(self, business_nodes):
        """Sets the business_nodes of this ListBusinessResponse.

        获取应用列表数据结构。

        :param business_nodes: The business_nodes of this ListBusinessResponse.
        :type business_nodes: list[:class:`huaweicloudsdkapm.v1.BusinessNodeModel`]
        """
        self._business_nodes = business_nodes

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
        if not isinstance(other, ListBusinessResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
