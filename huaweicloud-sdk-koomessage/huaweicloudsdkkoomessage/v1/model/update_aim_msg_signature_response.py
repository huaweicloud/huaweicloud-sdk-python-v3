# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAimMsgSignatureResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'signature_id': 'str',
        'signature_name': 'str'
    }

    attribute_map = {
        'signature_id': 'signature_id',
        'signature_name': 'signature_name'
    }

    def __init__(self, signature_id=None, signature_name=None):
        r"""UpdateAimMsgSignatureResponse

        The model defined in huaweicloud sdk

        :param signature_id: 签名ID。
        :type signature_id: str
        :param signature_name: 签名名称。
        :type signature_name: str
        """
        
        super(UpdateAimMsgSignatureResponse, self).__init__()

        self._signature_id = None
        self._signature_name = None
        self.discriminator = None

        if signature_id is not None:
            self.signature_id = signature_id
        if signature_name is not None:
            self.signature_name = signature_name

    @property
    def signature_id(self):
        r"""Gets the signature_id of this UpdateAimMsgSignatureResponse.

        签名ID。

        :return: The signature_id of this UpdateAimMsgSignatureResponse.
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        r"""Sets the signature_id of this UpdateAimMsgSignatureResponse.

        签名ID。

        :param signature_id: The signature_id of this UpdateAimMsgSignatureResponse.
        :type signature_id: str
        """
        self._signature_id = signature_id

    @property
    def signature_name(self):
        r"""Gets the signature_name of this UpdateAimMsgSignatureResponse.

        签名名称。

        :return: The signature_name of this UpdateAimMsgSignatureResponse.
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        r"""Sets the signature_name of this UpdateAimMsgSignatureResponse.

        签名名称。

        :param signature_name: The signature_name of this UpdateAimMsgSignatureResponse.
        :type signature_name: str
        """
        self._signature_name = signature_name

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
        if not isinstance(other, UpdateAimMsgSignatureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
