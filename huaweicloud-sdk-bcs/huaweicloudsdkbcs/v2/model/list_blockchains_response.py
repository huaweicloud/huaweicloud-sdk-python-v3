# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBlockchainsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blockchains': 'list[BlockchainInfo]',
        'count': 'int'
    }

    attribute_map = {
        'blockchains': 'blockchains',
        'count': 'count'
    }

    def __init__(self, blockchains=None, count=None):
        """ListBlockchainsResponse

        The model defined in huaweicloud sdk

        :param blockchains: 服务实例简要信息
        :type blockchains: list[:class:`huaweicloudsdkbcs.v2.BlockchainInfo`]
        :param count: 实例总数
        :type count: int
        """
        
        super(ListBlockchainsResponse, self).__init__()

        self._blockchains = None
        self._count = None
        self.discriminator = None

        if blockchains is not None:
            self.blockchains = blockchains
        if count is not None:
            self.count = count

    @property
    def blockchains(self):
        """Gets the blockchains of this ListBlockchainsResponse.

        服务实例简要信息

        :return: The blockchains of this ListBlockchainsResponse.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.BlockchainInfo`]
        """
        return self._blockchains

    @blockchains.setter
    def blockchains(self, blockchains):
        """Sets the blockchains of this ListBlockchainsResponse.

        服务实例简要信息

        :param blockchains: The blockchains of this ListBlockchainsResponse.
        :type blockchains: list[:class:`huaweicloudsdkbcs.v2.BlockchainInfo`]
        """
        self._blockchains = blockchains

    @property
    def count(self):
        """Gets the count of this ListBlockchainsResponse.

        实例总数

        :return: The count of this ListBlockchainsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListBlockchainsResponse.

        实例总数

        :param count: The count of this ListBlockchainsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListBlockchainsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
