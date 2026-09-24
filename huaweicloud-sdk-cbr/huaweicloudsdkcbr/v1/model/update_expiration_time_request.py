# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateExpirationTimeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vault_id': 'str',
        'body': 'UpdateExpirationTimeReq'
    }

    attribute_map = {
        'vault_id': 'vault_id',
        'body': 'body'
    }

    def __init__(self, vault_id=None, body=None):
        r"""UpdateExpirationTimeRequest

        The model defined in huaweicloud sdk

        :param vault_id: 存储库ID，默认取值不涉及。 [获取方法请参见\&quot;[获取存储库ID](https://support.huaweicloud.com/api-cbr/ListVault.html)\&quot;。](tag:hws) [获取方法请参见\&quot;[获取存储库ID](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ListVault.html)\&quot;。](tag:hws_hk)
        :type vault_id: str
        :param body: Body of the UpdateExpirationTimeRequest
        :type body: :class:`huaweicloudsdkcbr.v1.UpdateExpirationTimeReq`
        """
        
        

        self._vault_id = None
        self._body = None
        self.discriminator = None

        self.vault_id = vault_id
        if body is not None:
            self.body = body

    @property
    def vault_id(self):
        r"""Gets the vault_id of this UpdateExpirationTimeRequest.

        存储库ID，默认取值不涉及。 [获取方法请参见\"[获取存储库ID](https://support.huaweicloud.com/api-cbr/ListVault.html)\"。](tag:hws) [获取方法请参见\"[获取存储库ID](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ListVault.html)\"。](tag:hws_hk)

        :return: The vault_id of this UpdateExpirationTimeRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this UpdateExpirationTimeRequest.

        存储库ID，默认取值不涉及。 [获取方法请参见\"[获取存储库ID](https://support.huaweicloud.com/api-cbr/ListVault.html)\"。](tag:hws) [获取方法请参见\"[获取存储库ID](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ListVault.html)\"。](tag:hws_hk)

        :param vault_id: The vault_id of this UpdateExpirationTimeRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def body(self):
        r"""Gets the body of this UpdateExpirationTimeRequest.

        :return: The body of this UpdateExpirationTimeRequest.
        :rtype: :class:`huaweicloudsdkcbr.v1.UpdateExpirationTimeReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateExpirationTimeRequest.

        :param body: The body of this UpdateExpirationTimeRequest.
        :type body: :class:`huaweicloudsdkcbr.v1.UpdateExpirationTimeReq`
        """
        self._body = body

    def to_dict(self):
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
        if not isinstance(other, UpdateExpirationTimeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
