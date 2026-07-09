# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadDatabaseSslFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pem_key_txt': 'str'
    }

    attribute_map = {
        'pem_key_txt': 'pem_key_txt'
    }

    def __init__(self, pem_key_txt=None):
        r"""UploadDatabaseSslFileRequest

        The model defined in huaweicloud sdk

        :param pem_key_txt: 私钥文本内容
        :type pem_key_txt: str
        """
        
        

        self._pem_key_txt = None
        self.discriminator = None

        self.pem_key_txt = pem_key_txt

    @property
    def pem_key_txt(self):
        r"""Gets the pem_key_txt of this UploadDatabaseSslFileRequest.

        私钥文本内容

        :return: The pem_key_txt of this UploadDatabaseSslFileRequest.
        :rtype: str
        """
        return self._pem_key_txt

    @pem_key_txt.setter
    def pem_key_txt(self, pem_key_txt):
        r"""Sets the pem_key_txt of this UploadDatabaseSslFileRequest.

        私钥文本内容

        :param pem_key_txt: The pem_key_txt of this UploadDatabaseSslFileRequest.
        :type pem_key_txt: str
        """
        self._pem_key_txt = pem_key_txt

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
        if not isinstance(other, UploadDatabaseSslFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
