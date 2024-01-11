# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEcnWithVpcResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecn_vpc_relationships': 'list[EcnWithVpcItem]'
    }

    attribute_map = {
        'ecn_vpc_relationships': 'ecn_vpc_relationships'
    }

    def __init__(self, ecn_vpc_relationships=None):
        """ListEcnWithVpcResponse

        The model defined in huaweicloud sdk

        :param ecn_vpc_relationships: 企业连接网络与虚拟私有云的绑定关系列表
        :type ecn_vpc_relationships: list[:class:`huaweicloudsdkec.v1.EcnWithVpcItem`]
        """
        
        super(ListEcnWithVpcResponse, self).__init__()

        self._ecn_vpc_relationships = None
        self.discriminator = None

        if ecn_vpc_relationships is not None:
            self.ecn_vpc_relationships = ecn_vpc_relationships

    @property
    def ecn_vpc_relationships(self):
        """Gets the ecn_vpc_relationships of this ListEcnWithVpcResponse.

        企业连接网络与虚拟私有云的绑定关系列表

        :return: The ecn_vpc_relationships of this ListEcnWithVpcResponse.
        :rtype: list[:class:`huaweicloudsdkec.v1.EcnWithVpcItem`]
        """
        return self._ecn_vpc_relationships

    @ecn_vpc_relationships.setter
    def ecn_vpc_relationships(self, ecn_vpc_relationships):
        """Sets the ecn_vpc_relationships of this ListEcnWithVpcResponse.

        企业连接网络与虚拟私有云的绑定关系列表

        :param ecn_vpc_relationships: The ecn_vpc_relationships of this ListEcnWithVpcResponse.
        :type ecn_vpc_relationships: list[:class:`huaweicloudsdkec.v1.EcnWithVpcItem`]
        """
        self._ecn_vpc_relationships = ecn_vpc_relationships

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
        if not isinstance(other, ListEcnWithVpcResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
