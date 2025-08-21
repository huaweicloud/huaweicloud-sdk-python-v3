# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSshKeyResponse(SdkResponse):

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
        'title': 'str',
        'key': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'key': 'key',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, title=None, key=None, created_at=None):
        r"""AddSshKeyResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 秘钥id。
        :type id: int
        :param title: **参数解释：** 秘钥名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type title: str
        :param key: **参数解释：** 公钥。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type key: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        """
        
        super(AddSshKeyResponse, self).__init__()

        self._id = None
        self._title = None
        self._key = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if key is not None:
            self.key = key
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this AddSshKeyResponse.

        **参数解释：** 秘钥id。

        :return: The id of this AddSshKeyResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AddSshKeyResponse.

        **参数解释：** 秘钥id。

        :param id: The id of this AddSshKeyResponse.
        :type id: int
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this AddSshKeyResponse.

        **参数解释：** 秘钥名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The title of this AddSshKeyResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this AddSshKeyResponse.

        **参数解释：** 秘钥名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param title: The title of this AddSshKeyResponse.
        :type title: str
        """
        self._title = title

    @property
    def key(self):
        r"""Gets the key of this AddSshKeyResponse.

        **参数解释：** 公钥。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The key of this AddSshKeyResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this AddSshKeyResponse.

        **参数解释：** 公钥。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param key: The key of this AddSshKeyResponse.
        :type key: str
        """
        self._key = key

    @property
    def created_at(self):
        r"""Gets the created_at of this AddSshKeyResponse.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this AddSshKeyResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AddSshKeyResponse.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this AddSshKeyResponse.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, AddSshKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
