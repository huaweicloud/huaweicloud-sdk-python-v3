# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GpgSubKeyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'fingerprint': 'str',
        'gpg_key_id': 'int',
        'keyid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'fingerprint': 'fingerprint',
        'gpg_key_id': 'gpg_key_id',
        'keyid': 'keyid'
    }

    def __init__(self, id=None, fingerprint=None, gpg_key_id=None, keyid=None):
        r"""GpgSubKeyDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 子公钥subkey的id。
        :type id: int
        :param fingerprint: **参数解释：** 子公钥的指纹格式。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type fingerprint: str
        :param gpg_key_id: **参数解释：** gpg_key的id。
        :type gpg_key_id: int
        :param keyid: **参数解释：** 子秘钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type keyid: str
        """
        
        

        self._id = None
        self._fingerprint = None
        self._gpg_key_id = None
        self._keyid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if gpg_key_id is not None:
            self.gpg_key_id = gpg_key_id
        if keyid is not None:
            self.keyid = keyid

    @property
    def id(self):
        r"""Gets the id of this GpgSubKeyDto.

        **参数解释：** 子公钥subkey的id。

        :return: The id of this GpgSubKeyDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GpgSubKeyDto.

        **参数解释：** 子公钥subkey的id。

        :param id: The id of this GpgSubKeyDto.
        :type id: int
        """
        self._id = id

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this GpgSubKeyDto.

        **参数解释：** 子公钥的指纹格式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The fingerprint of this GpgSubKeyDto.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this GpgSubKeyDto.

        **参数解释：** 子公钥的指纹格式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param fingerprint: The fingerprint of this GpgSubKeyDto.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def gpg_key_id(self):
        r"""Gets the gpg_key_id of this GpgSubKeyDto.

        **参数解释：** gpg_key的id。

        :return: The gpg_key_id of this GpgSubKeyDto.
        :rtype: int
        """
        return self._gpg_key_id

    @gpg_key_id.setter
    def gpg_key_id(self, gpg_key_id):
        r"""Sets the gpg_key_id of this GpgSubKeyDto.

        **参数解释：** gpg_key的id。

        :param gpg_key_id: The gpg_key_id of this GpgSubKeyDto.
        :type gpg_key_id: int
        """
        self._gpg_key_id = gpg_key_id

    @property
    def keyid(self):
        r"""Gets the keyid of this GpgSubKeyDto.

        **参数解释：** 子秘钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The keyid of this GpgSubKeyDto.
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        r"""Sets the keyid of this GpgSubKeyDto.

        **参数解释：** 子秘钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param keyid: The keyid of this GpgSubKeyDto.
        :type keyid: str
        """
        self._keyid = keyid

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
        if not isinstance(other, GpgSubKeyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
