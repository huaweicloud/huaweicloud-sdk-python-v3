# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadSecretBlobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secret_blob': 'str'
    }

    attribute_map = {
        'secret_blob': 'secret_blob'
    }

    def __init__(self, secret_blob=None):
        """DownloadSecretBlobResponse

        The model defined in huaweicloud sdk

        :param secret_blob: 将指定凭据对象进行备份后得到的凭据备份文件，备份文件包含有凭据当前所有的凭据版本信息，备份文件经过加密与编码，内容不可直接读。 
        :type secret_blob: str
        """
        
        super(DownloadSecretBlobResponse, self).__init__()

        self._secret_blob = None
        self.discriminator = None

        if secret_blob is not None:
            self.secret_blob = secret_blob

    @property
    def secret_blob(self):
        """Gets the secret_blob of this DownloadSecretBlobResponse.

        将指定凭据对象进行备份后得到的凭据备份文件，备份文件包含有凭据当前所有的凭据版本信息，备份文件经过加密与编码，内容不可直接读。 

        :return: The secret_blob of this DownloadSecretBlobResponse.
        :rtype: str
        """
        return self._secret_blob

    @secret_blob.setter
    def secret_blob(self, secret_blob):
        """Sets the secret_blob of this DownloadSecretBlobResponse.

        将指定凭据对象进行备份后得到的凭据备份文件，备份文件包含有凭据当前所有的凭据版本信息，备份文件经过加密与编码，内容不可直接读。 

        :param secret_blob: The secret_blob of this DownloadSecretBlobResponse.
        :type secret_blob: str
        """
        self._secret_blob = secret_blob

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
        if not isinstance(other, DownloadSecretBlobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
