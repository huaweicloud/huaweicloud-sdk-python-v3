# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSyncTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'src_ak': 'str',
        'src_sk': 'str',
        'src_crypto_type': 'str',
        'src_kms_key_id': 'str',
        'dst_ak': 'str',
        'dst_sk': 'str',
        'dst_crypto_type': 'str',
        'dst_kms_key_id': 'str',
        'source_cdn_authentication_key': 'str',
        'source_cdn_crypto_type': 'str',
        'source_cdn_kms_key_id': 'str'
    }

    attribute_map = {
        'src_ak': 'src_ak',
        'src_sk': 'src_sk',
        'src_crypto_type': 'src_crypto_type',
        'src_kms_key_id': 'src_kms_key_id',
        'dst_ak': 'dst_ak',
        'dst_sk': 'dst_sk',
        'dst_crypto_type': 'dst_crypto_type',
        'dst_kms_key_id': 'dst_kms_key_id',
        'source_cdn_authentication_key': 'source_cdn_authentication_key',
        'source_cdn_crypto_type': 'source_cdn_crypto_type',
        'source_cdn_kms_key_id': 'source_cdn_kms_key_id'
    }

    def __init__(self, src_ak=None, src_sk=None, src_crypto_type=None, src_kms_key_id=None, dst_ak=None, dst_sk=None, dst_crypto_type=None, dst_kms_key_id=None, source_cdn_authentication_key=None, source_cdn_crypto_type=None, source_cdn_kms_key_id=None):
        r"""StartSyncTaskReq

        The model defined in huaweicloud sdk

        :param src_ak: 源端节点AK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。
        :type src_ak: str
        :param src_sk: 源端节点SK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。
        :type src_sk: str
        :param src_crypto_type: 加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS
        :type src_crypto_type: str
        :param src_kms_key_id: KMS密钥ID，36个字符
        :type src_kms_key_id: str
        :param dst_ak: 目的端节点AK（最大长度100个字符）。
        :type dst_ak: str
        :param dst_sk: 目的端节点SK（最大长度100个字符）。
        :type dst_sk: str
        :param dst_crypto_type: 加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS
        :type dst_crypto_type: str
        :param dst_kms_key_id: KMS密钥ID，36个字符
        :type dst_kms_key_id: str
        :param source_cdn_authentication_key: CDN鉴权密钥。
        :type source_cdn_authentication_key: str
        :param source_cdn_crypto_type: 加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS
        :type source_cdn_crypto_type: str
        :param source_cdn_kms_key_id: KMS密钥ID，36个字符
        :type source_cdn_kms_key_id: str
        """
        
        

        self._src_ak = None
        self._src_sk = None
        self._src_crypto_type = None
        self._src_kms_key_id = None
        self._dst_ak = None
        self._dst_sk = None
        self._dst_crypto_type = None
        self._dst_kms_key_id = None
        self._source_cdn_authentication_key = None
        self._source_cdn_crypto_type = None
        self._source_cdn_kms_key_id = None
        self.discriminator = None

        self.src_ak = src_ak
        self.src_sk = src_sk
        if src_crypto_type is not None:
            self.src_crypto_type = src_crypto_type
        if src_kms_key_id is not None:
            self.src_kms_key_id = src_kms_key_id
        self.dst_ak = dst_ak
        self.dst_sk = dst_sk
        if dst_crypto_type is not None:
            self.dst_crypto_type = dst_crypto_type
        if dst_kms_key_id is not None:
            self.dst_kms_key_id = dst_kms_key_id
        if source_cdn_authentication_key is not None:
            self.source_cdn_authentication_key = source_cdn_authentication_key
        if source_cdn_crypto_type is not None:
            self.source_cdn_crypto_type = source_cdn_crypto_type
        if source_cdn_kms_key_id is not None:
            self.source_cdn_kms_key_id = source_cdn_kms_key_id

    @property
    def src_ak(self):
        r"""Gets the src_ak of this StartSyncTaskReq.

        源端节点AK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :return: The src_ak of this StartSyncTaskReq.
        :rtype: str
        """
        return self._src_ak

    @src_ak.setter
    def src_ak(self, src_ak):
        r"""Sets the src_ak of this StartSyncTaskReq.

        源端节点AK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :param src_ak: The src_ak of this StartSyncTaskReq.
        :type src_ak: str
        """
        self._src_ak = src_ak

    @property
    def src_sk(self):
        r"""Gets the src_sk of this StartSyncTaskReq.

        源端节点SK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :return: The src_sk of this StartSyncTaskReq.
        :rtype: str
        """
        return self._src_sk

    @src_sk.setter
    def src_sk(self, src_sk):
        r"""Sets the src_sk of this StartSyncTaskReq.

        源端节点SK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :param src_sk: The src_sk of this StartSyncTaskReq.
        :type src_sk: str
        """
        self._src_sk = src_sk

    @property
    def src_crypto_type(self):
        r"""Gets the src_crypto_type of this StartSyncTaskReq.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :return: The src_crypto_type of this StartSyncTaskReq.
        :rtype: str
        """
        return self._src_crypto_type

    @src_crypto_type.setter
    def src_crypto_type(self, src_crypto_type):
        r"""Sets the src_crypto_type of this StartSyncTaskReq.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :param src_crypto_type: The src_crypto_type of this StartSyncTaskReq.
        :type src_crypto_type: str
        """
        self._src_crypto_type = src_crypto_type

    @property
    def src_kms_key_id(self):
        r"""Gets the src_kms_key_id of this StartSyncTaskReq.

        KMS密钥ID，36个字符

        :return: The src_kms_key_id of this StartSyncTaskReq.
        :rtype: str
        """
        return self._src_kms_key_id

    @src_kms_key_id.setter
    def src_kms_key_id(self, src_kms_key_id):
        r"""Sets the src_kms_key_id of this StartSyncTaskReq.

        KMS密钥ID，36个字符

        :param src_kms_key_id: The src_kms_key_id of this StartSyncTaskReq.
        :type src_kms_key_id: str
        """
        self._src_kms_key_id = src_kms_key_id

    @property
    def dst_ak(self):
        r"""Gets the dst_ak of this StartSyncTaskReq.

        目的端节点AK（最大长度100个字符）。

        :return: The dst_ak of this StartSyncTaskReq.
        :rtype: str
        """
        return self._dst_ak

    @dst_ak.setter
    def dst_ak(self, dst_ak):
        r"""Sets the dst_ak of this StartSyncTaskReq.

        目的端节点AK（最大长度100个字符）。

        :param dst_ak: The dst_ak of this StartSyncTaskReq.
        :type dst_ak: str
        """
        self._dst_ak = dst_ak

    @property
    def dst_sk(self):
        r"""Gets the dst_sk of this StartSyncTaskReq.

        目的端节点SK（最大长度100个字符）。

        :return: The dst_sk of this StartSyncTaskReq.
        :rtype: str
        """
        return self._dst_sk

    @dst_sk.setter
    def dst_sk(self, dst_sk):
        r"""Sets the dst_sk of this StartSyncTaskReq.

        目的端节点SK（最大长度100个字符）。

        :param dst_sk: The dst_sk of this StartSyncTaskReq.
        :type dst_sk: str
        """
        self._dst_sk = dst_sk

    @property
    def dst_crypto_type(self):
        r"""Gets the dst_crypto_type of this StartSyncTaskReq.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :return: The dst_crypto_type of this StartSyncTaskReq.
        :rtype: str
        """
        return self._dst_crypto_type

    @dst_crypto_type.setter
    def dst_crypto_type(self, dst_crypto_type):
        r"""Sets the dst_crypto_type of this StartSyncTaskReq.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :param dst_crypto_type: The dst_crypto_type of this StartSyncTaskReq.
        :type dst_crypto_type: str
        """
        self._dst_crypto_type = dst_crypto_type

    @property
    def dst_kms_key_id(self):
        r"""Gets the dst_kms_key_id of this StartSyncTaskReq.

        KMS密钥ID，36个字符

        :return: The dst_kms_key_id of this StartSyncTaskReq.
        :rtype: str
        """
        return self._dst_kms_key_id

    @dst_kms_key_id.setter
    def dst_kms_key_id(self, dst_kms_key_id):
        r"""Sets the dst_kms_key_id of this StartSyncTaskReq.

        KMS密钥ID，36个字符

        :param dst_kms_key_id: The dst_kms_key_id of this StartSyncTaskReq.
        :type dst_kms_key_id: str
        """
        self._dst_kms_key_id = dst_kms_key_id

    @property
    def source_cdn_authentication_key(self):
        r"""Gets the source_cdn_authentication_key of this StartSyncTaskReq.

        CDN鉴权密钥。

        :return: The source_cdn_authentication_key of this StartSyncTaskReq.
        :rtype: str
        """
        return self._source_cdn_authentication_key

    @source_cdn_authentication_key.setter
    def source_cdn_authentication_key(self, source_cdn_authentication_key):
        r"""Sets the source_cdn_authentication_key of this StartSyncTaskReq.

        CDN鉴权密钥。

        :param source_cdn_authentication_key: The source_cdn_authentication_key of this StartSyncTaskReq.
        :type source_cdn_authentication_key: str
        """
        self._source_cdn_authentication_key = source_cdn_authentication_key

    @property
    def source_cdn_crypto_type(self):
        r"""Gets the source_cdn_crypto_type of this StartSyncTaskReq.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :return: The source_cdn_crypto_type of this StartSyncTaskReq.
        :rtype: str
        """
        return self._source_cdn_crypto_type

    @source_cdn_crypto_type.setter
    def source_cdn_crypto_type(self, source_cdn_crypto_type):
        r"""Sets the source_cdn_crypto_type of this StartSyncTaskReq.

        加解密类型，默认为DEFAULT，可选类型为DEFAULT、KMS

        :param source_cdn_crypto_type: The source_cdn_crypto_type of this StartSyncTaskReq.
        :type source_cdn_crypto_type: str
        """
        self._source_cdn_crypto_type = source_cdn_crypto_type

    @property
    def source_cdn_kms_key_id(self):
        r"""Gets the source_cdn_kms_key_id of this StartSyncTaskReq.

        KMS密钥ID，36个字符

        :return: The source_cdn_kms_key_id of this StartSyncTaskReq.
        :rtype: str
        """
        return self._source_cdn_kms_key_id

    @source_cdn_kms_key_id.setter
    def source_cdn_kms_key_id(self, source_cdn_kms_key_id):
        r"""Sets the source_cdn_kms_key_id of this StartSyncTaskReq.

        KMS密钥ID，36个字符

        :param source_cdn_kms_key_id: The source_cdn_kms_key_id of this StartSyncTaskReq.
        :type source_cdn_kms_key_id: str
        """
        self._source_cdn_kms_key_id = source_cdn_kms_key_id

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
        if not isinstance(other, StartSyncTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
