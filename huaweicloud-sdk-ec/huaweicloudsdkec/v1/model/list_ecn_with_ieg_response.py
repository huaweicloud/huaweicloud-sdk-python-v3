# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEcnWithIegResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecn_ieg_relationships': 'list[EcnIegItem]'
    }

    attribute_map = {
        'ecn_ieg_relationships': 'ecn_ieg_relationships'
    }

    def __init__(self, ecn_ieg_relationships=None):
        """ListEcnWithIegResponse

        The model defined in huaweicloud sdk

        :param ecn_ieg_relationships: 企业连接网络与智能企业网关的绑定关系列表
        :type ecn_ieg_relationships: list[:class:`huaweicloudsdkec.v1.EcnIegItem`]
        """
        
        super(ListEcnWithIegResponse, self).__init__()

        self._ecn_ieg_relationships = None
        self.discriminator = None

        if ecn_ieg_relationships is not None:
            self.ecn_ieg_relationships = ecn_ieg_relationships

    @property
    def ecn_ieg_relationships(self):
        """Gets the ecn_ieg_relationships of this ListEcnWithIegResponse.

        企业连接网络与智能企业网关的绑定关系列表

        :return: The ecn_ieg_relationships of this ListEcnWithIegResponse.
        :rtype: list[:class:`huaweicloudsdkec.v1.EcnIegItem`]
        """
        return self._ecn_ieg_relationships

    @ecn_ieg_relationships.setter
    def ecn_ieg_relationships(self, ecn_ieg_relationships):
        """Sets the ecn_ieg_relationships of this ListEcnWithIegResponse.

        企业连接网络与智能企业网关的绑定关系列表

        :param ecn_ieg_relationships: The ecn_ieg_relationships of this ListEcnWithIegResponse.
        :type ecn_ieg_relationships: list[:class:`huaweicloudsdkec.v1.EcnIegItem`]
        """
        self._ecn_ieg_relationships = ecn_ieg_relationships

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
        if not isinstance(other, ListEcnWithIegResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
