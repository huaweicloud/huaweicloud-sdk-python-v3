# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchImportKeypairResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_keypairs': 'list[FailedKeypair]',
        'succeeded_keypairs': 'list[CreateKeypairResponseBody]'
    }

    attribute_map = {
        'failed_keypairs': 'failed_keypairs',
        'succeeded_keypairs': 'succeeded_keypairs'
    }

    def __init__(self, failed_keypairs=None, succeeded_keypairs=None):
        r"""BatchImportKeypairResponse

        The model defined in huaweicloud sdk

        :param failed_keypairs: 导入失败的SSH密钥对信息及导入失败的原因
        :type failed_keypairs: list[:class:`huaweicloudsdkkps.v3.FailedKeypair`]
        :param succeeded_keypairs: 成功导入的SSH密钥对信息
        :type succeeded_keypairs: list[:class:`huaweicloudsdkkps.v3.CreateKeypairResponseBody`]
        """
        
        super(BatchImportKeypairResponse, self).__init__()

        self._failed_keypairs = None
        self._succeeded_keypairs = None
        self.discriminator = None

        if failed_keypairs is not None:
            self.failed_keypairs = failed_keypairs
        if succeeded_keypairs is not None:
            self.succeeded_keypairs = succeeded_keypairs

    @property
    def failed_keypairs(self):
        r"""Gets the failed_keypairs of this BatchImportKeypairResponse.

        导入失败的SSH密钥对信息及导入失败的原因

        :return: The failed_keypairs of this BatchImportKeypairResponse.
        :rtype: list[:class:`huaweicloudsdkkps.v3.FailedKeypair`]
        """
        return self._failed_keypairs

    @failed_keypairs.setter
    def failed_keypairs(self, failed_keypairs):
        r"""Sets the failed_keypairs of this BatchImportKeypairResponse.

        导入失败的SSH密钥对信息及导入失败的原因

        :param failed_keypairs: The failed_keypairs of this BatchImportKeypairResponse.
        :type failed_keypairs: list[:class:`huaweicloudsdkkps.v3.FailedKeypair`]
        """
        self._failed_keypairs = failed_keypairs

    @property
    def succeeded_keypairs(self):
        r"""Gets the succeeded_keypairs of this BatchImportKeypairResponse.

        成功导入的SSH密钥对信息

        :return: The succeeded_keypairs of this BatchImportKeypairResponse.
        :rtype: list[:class:`huaweicloudsdkkps.v3.CreateKeypairResponseBody`]
        """
        return self._succeeded_keypairs

    @succeeded_keypairs.setter
    def succeeded_keypairs(self, succeeded_keypairs):
        r"""Sets the succeeded_keypairs of this BatchImportKeypairResponse.

        成功导入的SSH密钥对信息

        :param succeeded_keypairs: The succeeded_keypairs of this BatchImportKeypairResponse.
        :type succeeded_keypairs: list[:class:`huaweicloudsdkkps.v3.CreateKeypairResponseBody`]
        """
        self._succeeded_keypairs = succeeded_keypairs

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
        if not isinstance(other, BatchImportKeypairResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
