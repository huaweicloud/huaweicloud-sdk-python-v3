# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskGroupDstNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ak': 'str',
        'sk': 'str',
        'crypto_type': 'str',
        'kms_key_id': 'str',
        'region': 'str',
        'bucket': 'str',
        'cloud_type': 'str',
        'save_prefix': 'str'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'sk',
        'crypto_type': 'crypto_type',
        'kms_key_id': 'kms_key_id',
        'region': 'region',
        'bucket': 'bucket',
        'cloud_type': 'cloud_type',
        'save_prefix': 'save_prefix'
    }

    def __init__(self, ak=None, sk=None, crypto_type=None, kms_key_id=None, region=None, bucket=None, cloud_type=None, save_prefix=None):
        r"""TaskGroupDstNode

        The model defined in huaweicloud sdk

        :param ak: 目的端桶的AK（最大长度100个字符）。
        :type ak: str
        :param sk: 目的端桶的SK（最大长度100个字符）。
        :type sk: str
        :param crypto_type: 加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS
        :type crypto_type: str
        :param kms_key_id: KMS密钥ID，36个字符
        :type kms_key_id: str
        :param region: 目的端桶所处的区域。  请与Endpoint对应的区域保持一致。
        :type region: str
        :param bucket: 目的端的桶名称
        :type bucket: str
        :param cloud_type: 华为云目的端信息，默认为HEC
        :type cloud_type: str
        :param save_prefix: 目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。
        :type save_prefix: str
        """
        
        

        self._ak = None
        self._sk = None
        self._crypto_type = None
        self._kms_key_id = None
        self._region = None
        self._bucket = None
        self._cloud_type = None
        self._save_prefix = None
        self.discriminator = None

        self.ak = ak
        self.sk = sk
        if crypto_type is not None:
            self.crypto_type = crypto_type
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        self.region = region
        self.bucket = bucket
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if save_prefix is not None:
            self.save_prefix = save_prefix

    @property
    def ak(self):
        r"""Gets the ak of this TaskGroupDstNode.

        目的端桶的AK（最大长度100个字符）。

        :return: The ak of this TaskGroupDstNode.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this TaskGroupDstNode.

        目的端桶的AK（最大长度100个字符）。

        :param ak: The ak of this TaskGroupDstNode.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this TaskGroupDstNode.

        目的端桶的SK（最大长度100个字符）。

        :return: The sk of this TaskGroupDstNode.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this TaskGroupDstNode.

        目的端桶的SK（最大长度100个字符）。

        :param sk: The sk of this TaskGroupDstNode.
        :type sk: str
        """
        self._sk = sk

    @property
    def crypto_type(self):
        r"""Gets the crypto_type of this TaskGroupDstNode.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :return: The crypto_type of this TaskGroupDstNode.
        :rtype: str
        """
        return self._crypto_type

    @crypto_type.setter
    def crypto_type(self, crypto_type):
        r"""Sets the crypto_type of this TaskGroupDstNode.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :param crypto_type: The crypto_type of this TaskGroupDstNode.
        :type crypto_type: str
        """
        self._crypto_type = crypto_type

    @property
    def kms_key_id(self):
        r"""Gets the kms_key_id of this TaskGroupDstNode.

        KMS密钥ID，36个字符

        :return: The kms_key_id of this TaskGroupDstNode.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        r"""Sets the kms_key_id of this TaskGroupDstNode.

        KMS密钥ID，36个字符

        :param kms_key_id: The kms_key_id of this TaskGroupDstNode.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def region(self):
        r"""Gets the region of this TaskGroupDstNode.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :return: The region of this TaskGroupDstNode.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TaskGroupDstNode.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :param region: The region of this TaskGroupDstNode.
        :type region: str
        """
        self._region = region

    @property
    def bucket(self):
        r"""Gets the bucket of this TaskGroupDstNode.

        目的端的桶名称

        :return: The bucket of this TaskGroupDstNode.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this TaskGroupDstNode.

        目的端的桶名称

        :param bucket: The bucket of this TaskGroupDstNode.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def cloud_type(self):
        r"""Gets the cloud_type of this TaskGroupDstNode.

        华为云目的端信息，默认为HEC

        :return: The cloud_type of this TaskGroupDstNode.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        r"""Sets the cloud_type of this TaskGroupDstNode.

        华为云目的端信息，默认为HEC

        :param cloud_type: The cloud_type of this TaskGroupDstNode.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def save_prefix(self):
        r"""Gets the save_prefix of this TaskGroupDstNode.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :return: The save_prefix of this TaskGroupDstNode.
        :rtype: str
        """
        return self._save_prefix

    @save_prefix.setter
    def save_prefix(self, save_prefix):
        r"""Sets the save_prefix of this TaskGroupDstNode.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :param save_prefix: The save_prefix of this TaskGroupDstNode.
        :type save_prefix: str
        """
        self._save_prefix = save_prefix

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
        if not isinstance(other, TaskGroupDstNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
