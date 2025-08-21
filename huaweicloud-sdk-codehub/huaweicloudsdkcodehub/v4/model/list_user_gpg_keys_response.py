# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserGpgKeysResponse(SdkResponse):

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
        'created_at': 'str',
        'emails_with_verified_status': 'dict(str, bool)',
        'fingerprint': 'str',
        'key': 'str',
        'description': 'str',
        'title': 'str',
        'primary_keyid': 'str',
        'active': 'bool',
        'subkeys': 'list[GpgSubKeyDto]'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'emails_with_verified_status': 'emails_with_verified_status',
        'fingerprint': 'fingerprint',
        'key': 'key',
        'description': 'description',
        'title': 'title',
        'primary_keyid': 'primary_keyid',
        'active': 'active',
        'subkeys': 'subkeys'
    }

    def __init__(self, id=None, created_at=None, emails_with_verified_status=None, fingerprint=None, key=None, description=None, title=None, primary_keyid=None, active=None, subkeys=None):
        r"""ListUserGpgKeysResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 记录id。
        :type id: int
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param emails_with_verified_status: **参数解释：** 解析到的邮箱列表以及是否生效。
        :type emails_with_verified_status: dict(str, bool)
        :param fingerprint: **参数解释：** 主密/公钥的指纹格式。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type fingerprint: str
        :param key: **参数解释：** gpg的公钥。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type key: str
        :param description: **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type description: str
        :param title: **参数解释：** gpg_key的标题。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type title: str
        :param primary_keyid: **参数解释：** 主密/公钥primary_key的id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type primary_keyid: str
        :param active: **参数解释：** 是否生效。
        :type active: bool
        :param subkeys: **参数解释：** 子钥列表。 **取值范围：** 列表长度不少于0，不超过1000。
        :type subkeys: list[:class:`huaweicloudsdkcodehub.v4.GpgSubKeyDto`]
        """
        
        super(ListUserGpgKeysResponse, self).__init__()

        self._id = None
        self._created_at = None
        self._emails_with_verified_status = None
        self._fingerprint = None
        self._key = None
        self._description = None
        self._title = None
        self._primary_keyid = None
        self._active = None
        self._subkeys = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if emails_with_verified_status is not None:
            self.emails_with_verified_status = emails_with_verified_status
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if key is not None:
            self.key = key
        if description is not None:
            self.description = description
        if title is not None:
            self.title = title
        if primary_keyid is not None:
            self.primary_keyid = primary_keyid
        if active is not None:
            self.active = active
        if subkeys is not None:
            self.subkeys = subkeys

    @property
    def id(self):
        r"""Gets the id of this ListUserGpgKeysResponse.

        **参数解释：** 记录id。

        :return: The id of this ListUserGpgKeysResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListUserGpgKeysResponse.

        **参数解释：** 记录id。

        :param id: The id of this ListUserGpgKeysResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ListUserGpgKeysResponse.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this ListUserGpgKeysResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListUserGpgKeysResponse.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this ListUserGpgKeysResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def emails_with_verified_status(self):
        r"""Gets the emails_with_verified_status of this ListUserGpgKeysResponse.

        **参数解释：** 解析到的邮箱列表以及是否生效。

        :return: The emails_with_verified_status of this ListUserGpgKeysResponse.
        :rtype: dict(str, bool)
        """
        return self._emails_with_verified_status

    @emails_with_verified_status.setter
    def emails_with_verified_status(self, emails_with_verified_status):
        r"""Sets the emails_with_verified_status of this ListUserGpgKeysResponse.

        **参数解释：** 解析到的邮箱列表以及是否生效。

        :param emails_with_verified_status: The emails_with_verified_status of this ListUserGpgKeysResponse.
        :type emails_with_verified_status: dict(str, bool)
        """
        self._emails_with_verified_status = emails_with_verified_status

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this ListUserGpgKeysResponse.

        **参数解释：** 主密/公钥的指纹格式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The fingerprint of this ListUserGpgKeysResponse.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this ListUserGpgKeysResponse.

        **参数解释：** 主密/公钥的指纹格式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param fingerprint: The fingerprint of this ListUserGpgKeysResponse.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def key(self):
        r"""Gets the key of this ListUserGpgKeysResponse.

        **参数解释：** gpg的公钥。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The key of this ListUserGpgKeysResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ListUserGpgKeysResponse.

        **参数解释：** gpg的公钥。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param key: The key of this ListUserGpgKeysResponse.
        :type key: str
        """
        self._key = key

    @property
    def description(self):
        r"""Gets the description of this ListUserGpgKeysResponse.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The description of this ListUserGpgKeysResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListUserGpgKeysResponse.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param description: The description of this ListUserGpgKeysResponse.
        :type description: str
        """
        self._description = description

    @property
    def title(self):
        r"""Gets the title of this ListUserGpgKeysResponse.

        **参数解释：** gpg_key的标题。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The title of this ListUserGpgKeysResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ListUserGpgKeysResponse.

        **参数解释：** gpg_key的标题。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param title: The title of this ListUserGpgKeysResponse.
        :type title: str
        """
        self._title = title

    @property
    def primary_keyid(self):
        r"""Gets the primary_keyid of this ListUserGpgKeysResponse.

        **参数解释：** 主密/公钥primary_key的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The primary_keyid of this ListUserGpgKeysResponse.
        :rtype: str
        """
        return self._primary_keyid

    @primary_keyid.setter
    def primary_keyid(self, primary_keyid):
        r"""Sets the primary_keyid of this ListUserGpgKeysResponse.

        **参数解释：** 主密/公钥primary_key的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param primary_keyid: The primary_keyid of this ListUserGpgKeysResponse.
        :type primary_keyid: str
        """
        self._primary_keyid = primary_keyid

    @property
    def active(self):
        r"""Gets the active of this ListUserGpgKeysResponse.

        **参数解释：** 是否生效。

        :return: The active of this ListUserGpgKeysResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this ListUserGpgKeysResponse.

        **参数解释：** 是否生效。

        :param active: The active of this ListUserGpgKeysResponse.
        :type active: bool
        """
        self._active = active

    @property
    def subkeys(self):
        r"""Gets the subkeys of this ListUserGpgKeysResponse.

        **参数解释：** 子钥列表。 **取值范围：** 列表长度不少于0，不超过1000。

        :return: The subkeys of this ListUserGpgKeysResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.GpgSubKeyDto`]
        """
        return self._subkeys

    @subkeys.setter
    def subkeys(self, subkeys):
        r"""Sets the subkeys of this ListUserGpgKeysResponse.

        **参数解释：** 子钥列表。 **取值范围：** 列表长度不少于0，不超过1000。

        :param subkeys: The subkeys of this ListUserGpgKeysResponse.
        :type subkeys: list[:class:`huaweicloudsdkcodehub.v4.GpgSubKeyDto`]
        """
        self._subkeys = subkeys

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
        if not isinstance(other, ListUserGpgKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
