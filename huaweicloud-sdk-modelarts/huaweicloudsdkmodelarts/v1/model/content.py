# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Content:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'Owner',
        'etag': 'str',
        'type': 'str',
        'key': 'str',
        'last_modified': 'str',
        'size': 'int',
        'storage_class': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'etag': 'etag',
        'type': 'type',
        'key': 'key',
        'last_modified': 'last_modified',
        'size': 'size',
        'storage_class': 'storage_class'
    }

    def __init__(self, owner=None, etag=None, type=None, key=None, last_modified=None, size=None, storage_class=None):
        r"""Content

        The model defined in huaweicloud sdk

        :param owner: 
        :type owner: :class:`huaweicloudsdkmodelarts.v1.Owner`
        :param etag: **参数解释**：对象的base64编码的128位MD5摘要。ETag是对象内容的唯一标识，可以通过该值识别对象内容是否有变化。比如上传对象时ETag为A，下载对象时ETag为B，则说明对象内容发生了变化。实际的ETag是对象的哈希值。ETag只反映变化的内容，而不是其元数据。上传的对象或拷贝操作创建的对象，通过MD5加密后都有唯一的ETag。 **约束限制**：当对象是服务端加密的对象时，ETag值不是对象的MD5值，而是通过服务端加密计算出的唯一标识。 **取值范围**：长度为32的字符串。
        :type etag: str
        :param type: **参数解释**：对象类型。 **约束限制**：非Normal对象时返回。 **取值范围**：不涉及。
        :type type: str
        :param key: **参数解释**：对象名。对象名是对象在存储桶中的唯一标识。对象名是对象在桶中的完整路径，路径中不包含桶名。 **取值范围**：长度大于0且不超过1024的字符串。
        :type key: str
        :param last_modified: **参数解释**：对象最近一次被修改的时间（UTC时间）。 **约束限制**：日期格式为ISO8601的格式。 **取值范围**：不涉及。
        :type last_modified: str
        :param size: **参数解释**：对象的字节数。 **取值范围**：0~48.8TB，单位：字节。
        :type size: int
        :param storage_class: **参数解释**：对象的存储类型。 **取值范围**：不涉及。
        :type storage_class: str
        """
        
        

        self._owner = None
        self._etag = None
        self._type = None
        self._key = None
        self._last_modified = None
        self._size = None
        self._storage_class = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if etag is not None:
            self.etag = etag
        if type is not None:
            self.type = type
        if key is not None:
            self.key = key
        if last_modified is not None:
            self.last_modified = last_modified
        if size is not None:
            self.size = size
        if storage_class is not None:
            self.storage_class = storage_class

    @property
    def owner(self):
        r"""Gets the owner of this Content.

        :return: The owner of this Content.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Owner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this Content.

        :param owner: The owner of this Content.
        :type owner: :class:`huaweicloudsdkmodelarts.v1.Owner`
        """
        self._owner = owner

    @property
    def etag(self):
        r"""Gets the etag of this Content.

        **参数解释**：对象的base64编码的128位MD5摘要。ETag是对象内容的唯一标识，可以通过该值识别对象内容是否有变化。比如上传对象时ETag为A，下载对象时ETag为B，则说明对象内容发生了变化。实际的ETag是对象的哈希值。ETag只反映变化的内容，而不是其元数据。上传的对象或拷贝操作创建的对象，通过MD5加密后都有唯一的ETag。 **约束限制**：当对象是服务端加密的对象时，ETag值不是对象的MD5值，而是通过服务端加密计算出的唯一标识。 **取值范围**：长度为32的字符串。

        :return: The etag of this Content.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        r"""Sets the etag of this Content.

        **参数解释**：对象的base64编码的128位MD5摘要。ETag是对象内容的唯一标识，可以通过该值识别对象内容是否有变化。比如上传对象时ETag为A，下载对象时ETag为B，则说明对象内容发生了变化。实际的ETag是对象的哈希值。ETag只反映变化的内容，而不是其元数据。上传的对象或拷贝操作创建的对象，通过MD5加密后都有唯一的ETag。 **约束限制**：当对象是服务端加密的对象时，ETag值不是对象的MD5值，而是通过服务端加密计算出的唯一标识。 **取值范围**：长度为32的字符串。

        :param etag: The etag of this Content.
        :type etag: str
        """
        self._etag = etag

    @property
    def type(self):
        r"""Gets the type of this Content.

        **参数解释**：对象类型。 **约束限制**：非Normal对象时返回。 **取值范围**：不涉及。

        :return: The type of this Content.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Content.

        **参数解释**：对象类型。 **约束限制**：非Normal对象时返回。 **取值范围**：不涉及。

        :param type: The type of this Content.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        r"""Gets the key of this Content.

        **参数解释**：对象名。对象名是对象在存储桶中的唯一标识。对象名是对象在桶中的完整路径，路径中不包含桶名。 **取值范围**：长度大于0且不超过1024的字符串。

        :return: The key of this Content.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Content.

        **参数解释**：对象名。对象名是对象在存储桶中的唯一标识。对象名是对象在桶中的完整路径，路径中不包含桶名。 **取值范围**：长度大于0且不超过1024的字符串。

        :param key: The key of this Content.
        :type key: str
        """
        self._key = key

    @property
    def last_modified(self):
        r"""Gets the last_modified of this Content.

        **参数解释**：对象最近一次被修改的时间（UTC时间）。 **约束限制**：日期格式为ISO8601的格式。 **取值范围**：不涉及。

        :return: The last_modified of this Content.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this Content.

        **参数解释**：对象最近一次被修改的时间（UTC时间）。 **约束限制**：日期格式为ISO8601的格式。 **取值范围**：不涉及。

        :param last_modified: The last_modified of this Content.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def size(self):
        r"""Gets the size of this Content.

        **参数解释**：对象的字节数。 **取值范围**：0~48.8TB，单位：字节。

        :return: The size of this Content.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Content.

        **参数解释**：对象的字节数。 **取值范围**：0~48.8TB，单位：字节。

        :param size: The size of this Content.
        :type size: int
        """
        self._size = size

    @property
    def storage_class(self):
        r"""Gets the storage_class of this Content.

        **参数解释**：对象的存储类型。 **取值范围**：不涉及。

        :return: The storage_class of this Content.
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        r"""Sets the storage_class of this Content.

        **参数解释**：对象的存储类型。 **取值范围**：不涉及。

        :param storage_class: The storage_class of this Content.
        :type storage_class: str
        """
        self._storage_class = storage_class

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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
