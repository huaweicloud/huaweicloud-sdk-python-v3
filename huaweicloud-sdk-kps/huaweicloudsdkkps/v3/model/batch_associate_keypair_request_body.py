# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAssociateKeypairRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_keypairs': 'list[AssociateKeypairRequestBody]'
    }

    attribute_map = {
        'batch_keypairs': 'batch_keypairs'
    }

    def __init__(self, batch_keypairs=None):
        r"""BatchAssociateKeypairRequestBody

        The model defined in huaweicloud sdk

        :param batch_keypairs: 最多可同时选择10个弹性云服务器绑定密钥对。  约束：只支持选择相同的密钥对，弹性云服务器处于“运行中”状态，并未绑定密钥对。
        :type batch_keypairs: list[:class:`huaweicloudsdkkps.v3.AssociateKeypairRequestBody`]
        """
        
        

        self._batch_keypairs = None
        self.discriminator = None

        self.batch_keypairs = batch_keypairs

    @property
    def batch_keypairs(self):
        r"""Gets the batch_keypairs of this BatchAssociateKeypairRequestBody.

        最多可同时选择10个弹性云服务器绑定密钥对。  约束：只支持选择相同的密钥对，弹性云服务器处于“运行中”状态，并未绑定密钥对。

        :return: The batch_keypairs of this BatchAssociateKeypairRequestBody.
        :rtype: list[:class:`huaweicloudsdkkps.v3.AssociateKeypairRequestBody`]
        """
        return self._batch_keypairs

    @batch_keypairs.setter
    def batch_keypairs(self, batch_keypairs):
        r"""Sets the batch_keypairs of this BatchAssociateKeypairRequestBody.

        最多可同时选择10个弹性云服务器绑定密钥对。  约束：只支持选择相同的密钥对，弹性云服务器处于“运行中”状态，并未绑定密钥对。

        :param batch_keypairs: The batch_keypairs of this BatchAssociateKeypairRequestBody.
        :type batch_keypairs: list[:class:`huaweicloudsdkkps.v3.AssociateKeypairRequestBody`]
        """
        self._batch_keypairs = batch_keypairs

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
        if not isinstance(other, BatchAssociateKeypairRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
