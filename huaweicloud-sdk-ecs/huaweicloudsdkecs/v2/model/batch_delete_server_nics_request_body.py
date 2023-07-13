# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteServerNicsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nics': 'list[BatchDeleteServerNicOption]'
    }

    attribute_map = {
        'nics': 'nics'
    }

    def __init__(self, nics=None):
        """BatchDeleteServerNicsRequestBody

        The model defined in huaweicloud sdk

        :param nics: 需要删除的网卡列表信息。  说明： 主网卡是弹性云服务器上配置了路由规则的网卡，不可删除。
        :type nics: list[:class:`huaweicloudsdkecs.v2.BatchDeleteServerNicOption`]
        """
        
        

        self._nics = None
        self.discriminator = None

        self.nics = nics

    @property
    def nics(self):
        """Gets the nics of this BatchDeleteServerNicsRequestBody.

        需要删除的网卡列表信息。  说明： 主网卡是弹性云服务器上配置了路由规则的网卡，不可删除。

        :return: The nics of this BatchDeleteServerNicsRequestBody.
        :rtype: list[:class:`huaweicloudsdkecs.v2.BatchDeleteServerNicOption`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this BatchDeleteServerNicsRequestBody.

        需要删除的网卡列表信息。  说明： 主网卡是弹性云服务器上配置了路由规则的网卡，不可删除。

        :param nics: The nics of this BatchDeleteServerNicsRequestBody.
        :type nics: list[:class:`huaweicloudsdkecs.v2.BatchDeleteServerNicOption`]
        """
        self._nics = nics

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
        if not isinstance(other, BatchDeleteServerNicsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
