# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDnssecConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_name': 'str',
        'key_tag': 'int',
        'flag': 'int',
        'digest_algorithm': 'str',
        'digest_type': 'int',
        'digest': 'str',
        'signature': 'str',
        'signature_type': 'int',
        'ksk_public_key': 'str',
        'ds_record': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'status': 'str'
    }

    attribute_map = {
        'zone_name': 'zone_name',
        'key_tag': 'key_tag',
        'flag': 'flag',
        'digest_algorithm': 'digest_algorithm',
        'digest_type': 'digest_type',
        'digest': 'digest',
        'signature': 'signature',
        'signature_type': 'signature_type',
        'ksk_public_key': 'ksk_public_key',
        'ds_record': 'ds_record',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status'
    }

    def __init__(self, zone_name=None, key_tag=None, flag=None, digest_algorithm=None, digest_type=None, digest=None, signature=None, signature_type=None, ksk_public_key=None, ds_record=None, created_at=None, updated_at=None, status=None):
        r"""ShowDnssecConfigResponse

        The model defined in huaweicloud sdk

        :param zone_name: 域名。
        :type zone_name: str
        :param key_tag: 密钥标签。
        :type key_tag: int
        :param flag: 旗标。
        :type flag: int
        :param digest_algorithm: 摘要算法。
        :type digest_algorithm: str
        :param digest_type: 摘要算法类型。
        :type digest_type: int
        :param digest: 摘要。
        :type digest: str
        :param signature: 签名算法。
        :type signature: str
        :param signature_type: 签名算法类型。
        :type signature_type: int
        :param ksk_public_key: 公有密钥。
        :type ksk_public_key: str
        :param ds_record: DS记录。
        :type ds_record: str
        :param created_at: 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type created_at: str
        :param updated_at: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type updated_at: str
        :param status: 状态。  取值范围：  ENABLE：启用 DISABLE：关闭
        :type status: str
        """
        
        super(ShowDnssecConfigResponse, self).__init__()

        self._zone_name = None
        self._key_tag = None
        self._flag = None
        self._digest_algorithm = None
        self._digest_type = None
        self._digest = None
        self._signature = None
        self._signature_type = None
        self._ksk_public_key = None
        self._ds_record = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self.discriminator = None

        if zone_name is not None:
            self.zone_name = zone_name
        if key_tag is not None:
            self.key_tag = key_tag
        if flag is not None:
            self.flag = flag
        if digest_algorithm is not None:
            self.digest_algorithm = digest_algorithm
        if digest_type is not None:
            self.digest_type = digest_type
        if digest is not None:
            self.digest = digest
        if signature is not None:
            self.signature = signature
        if signature_type is not None:
            self.signature_type = signature_type
        if ksk_public_key is not None:
            self.ksk_public_key = ksk_public_key
        if ds_record is not None:
            self.ds_record = ds_record
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status

    @property
    def zone_name(self):
        r"""Gets the zone_name of this ShowDnssecConfigResponse.

        域名。

        :return: The zone_name of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this ShowDnssecConfigResponse.

        域名。

        :param zone_name: The zone_name of this ShowDnssecConfigResponse.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def key_tag(self):
        r"""Gets the key_tag of this ShowDnssecConfigResponse.

        密钥标签。

        :return: The key_tag of this ShowDnssecConfigResponse.
        :rtype: int
        """
        return self._key_tag

    @key_tag.setter
    def key_tag(self, key_tag):
        r"""Sets the key_tag of this ShowDnssecConfigResponse.

        密钥标签。

        :param key_tag: The key_tag of this ShowDnssecConfigResponse.
        :type key_tag: int
        """
        self._key_tag = key_tag

    @property
    def flag(self):
        r"""Gets the flag of this ShowDnssecConfigResponse.

        旗标。

        :return: The flag of this ShowDnssecConfigResponse.
        :rtype: int
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this ShowDnssecConfigResponse.

        旗标。

        :param flag: The flag of this ShowDnssecConfigResponse.
        :type flag: int
        """
        self._flag = flag

    @property
    def digest_algorithm(self):
        r"""Gets the digest_algorithm of this ShowDnssecConfigResponse.

        摘要算法。

        :return: The digest_algorithm of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._digest_algorithm

    @digest_algorithm.setter
    def digest_algorithm(self, digest_algorithm):
        r"""Sets the digest_algorithm of this ShowDnssecConfigResponse.

        摘要算法。

        :param digest_algorithm: The digest_algorithm of this ShowDnssecConfigResponse.
        :type digest_algorithm: str
        """
        self._digest_algorithm = digest_algorithm

    @property
    def digest_type(self):
        r"""Gets the digest_type of this ShowDnssecConfigResponse.

        摘要算法类型。

        :return: The digest_type of this ShowDnssecConfigResponse.
        :rtype: int
        """
        return self._digest_type

    @digest_type.setter
    def digest_type(self, digest_type):
        r"""Sets the digest_type of this ShowDnssecConfigResponse.

        摘要算法类型。

        :param digest_type: The digest_type of this ShowDnssecConfigResponse.
        :type digest_type: int
        """
        self._digest_type = digest_type

    @property
    def digest(self):
        r"""Gets the digest of this ShowDnssecConfigResponse.

        摘要。

        :return: The digest of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this ShowDnssecConfigResponse.

        摘要。

        :param digest: The digest of this ShowDnssecConfigResponse.
        :type digest: str
        """
        self._digest = digest

    @property
    def signature(self):
        r"""Gets the signature of this ShowDnssecConfigResponse.

        签名算法。

        :return: The signature of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        r"""Sets the signature of this ShowDnssecConfigResponse.

        签名算法。

        :param signature: The signature of this ShowDnssecConfigResponse.
        :type signature: str
        """
        self._signature = signature

    @property
    def signature_type(self):
        r"""Gets the signature_type of this ShowDnssecConfigResponse.

        签名算法类型。

        :return: The signature_type of this ShowDnssecConfigResponse.
        :rtype: int
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        r"""Sets the signature_type of this ShowDnssecConfigResponse.

        签名算法类型。

        :param signature_type: The signature_type of this ShowDnssecConfigResponse.
        :type signature_type: int
        """
        self._signature_type = signature_type

    @property
    def ksk_public_key(self):
        r"""Gets the ksk_public_key of this ShowDnssecConfigResponse.

        公有密钥。

        :return: The ksk_public_key of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._ksk_public_key

    @ksk_public_key.setter
    def ksk_public_key(self, ksk_public_key):
        r"""Sets the ksk_public_key of this ShowDnssecConfigResponse.

        公有密钥。

        :param ksk_public_key: The ksk_public_key of this ShowDnssecConfigResponse.
        :type ksk_public_key: str
        """
        self._ksk_public_key = ksk_public_key

    @property
    def ds_record(self):
        r"""Gets the ds_record of this ShowDnssecConfigResponse.

        DS记录。

        :return: The ds_record of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._ds_record

    @ds_record.setter
    def ds_record(self, ds_record):
        r"""Sets the ds_record of this ShowDnssecConfigResponse.

        DS记录。

        :param ds_record: The ds_record of this ShowDnssecConfigResponse.
        :type ds_record: str
        """
        self._ds_record = ds_record

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowDnssecConfigResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The created_at of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowDnssecConfigResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param created_at: The created_at of this ShowDnssecConfigResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowDnssecConfigResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The updated_at of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowDnssecConfigResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param updated_at: The updated_at of this ShowDnssecConfigResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def status(self):
        r"""Gets the status of this ShowDnssecConfigResponse.

        状态。  取值范围：  ENABLE：启用 DISABLE：关闭

        :return: The status of this ShowDnssecConfigResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDnssecConfigResponse.

        状态。  取值范围：  ENABLE：启用 DISABLE：关闭

        :param status: The status of this ShowDnssecConfigResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowDnssecConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
