# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadCertsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'certs_object': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'certs_object': 'certs_object'
    }

    def __init__(self, bucket_name=None, certs_object=None):
        r"""UploadCertsRequestBody

        The model defined in huaweicloud sdk

        :param bucket_name: 证书文件存放的OBS桶（桶类型必须为标准存储或者低频存储，不支持归档存储）。
        :type bucket_name: str
        :param certs_object: 证书文件对象。证书文件大小不能超过1M。证书名称在4位到32位之间，必须以字母开头，以（.cer|.crt|.rsa|.jks|.pem|.p10|.pfx|.p12|.csr|.der|.keystore）结尾，可以包含字母、数字、中划线、下划线或者小数点，不能包含其他的特殊字符。
        :type certs_object: str
        """
        
        

        self._bucket_name = None
        self._certs_object = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.certs_object = certs_object

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this UploadCertsRequestBody.

        证书文件存放的OBS桶（桶类型必须为标准存储或者低频存储，不支持归档存储）。

        :return: The bucket_name of this UploadCertsRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this UploadCertsRequestBody.

        证书文件存放的OBS桶（桶类型必须为标准存储或者低频存储，不支持归档存储）。

        :param bucket_name: The bucket_name of this UploadCertsRequestBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def certs_object(self):
        r"""Gets the certs_object of this UploadCertsRequestBody.

        证书文件对象。证书文件大小不能超过1M。证书名称在4位到32位之间，必须以字母开头，以（.cer|.crt|.rsa|.jks|.pem|.p10|.pfx|.p12|.csr|.der|.keystore）结尾，可以包含字母、数字、中划线、下划线或者小数点，不能包含其他的特殊字符。

        :return: The certs_object of this UploadCertsRequestBody.
        :rtype: str
        """
        return self._certs_object

    @certs_object.setter
    def certs_object(self, certs_object):
        r"""Sets the certs_object of this UploadCertsRequestBody.

        证书文件对象。证书文件大小不能超过1M。证书名称在4位到32位之间，必须以字母开头，以（.cer|.crt|.rsa|.jks|.pem|.p10|.pfx|.p12|.csr|.der|.keystore）结尾，可以包含字母、数字、中划线、下划线或者小数点，不能包含其他的特殊字符。

        :param certs_object: The certs_object of this UploadCertsRequestBody.
        :type certs_object: str
        """
        self._certs_object = certs_object

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
        if not isinstance(other, UploadCertsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
