# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Contents:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Contents"

    sensitive_list = []

    openapi_types = {
        'owner': 'Owner',
        'e_tag': 'str',
        'type': 'str',
        'key': 'str',
        'last_modified': 'str',
        'size': 'str',
        'storage_class': 'str'
    }

    attribute_map = {
        'owner': 'Owner',
        'e_tag': 'ETag',
        'type': 'Type',
        'key': 'Key',
        'last_modified': 'LastModified',
        'size': 'Size',
        'storage_class': 'StorageClass'
    }

    def __init__(self, owner=None, e_tag=None, type=None, key=None, last_modified=None, size=None, storage_class=None):
        r"""Contents

        The model defined in huaweicloud sdk

        :param owner: 
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        :param e_tag: Base64-encoded 128-bit MD5 digest of an object. ETag is the unique identifier of the object content. It determines whether the object content changes. For example, when an object is uploaded, its ETag value is **A**, but when it is downloaded, its ETag value is **B**, this indicates that the object content changes. The ETag is a hash of the object. The ETag reflects changes only to the object content, rather than its metadata. An uploaded object or copied object has a unique ETag after being encrypted with MD5. (If the object is encrypted on the server side, the ETag value is not the MD5 digest of the object, but the unique identifier calculated through server-side encryption.)
        :type e_tag: str
        :param type: Object type. This parameter is returned when the object type is not **Normal**.
        :type type: str
        :param key: Name of the object
        :type key: str
        :param last_modified: Time (UTC) when the object was last modified
        :type last_modified: str
        :param size: Object size in bytes
        :type size: str
        :param storage_class: Storage class of the object
        :type storage_class: str
        """
        
        

        self._owner = None
        self._e_tag = None
        self._type = None
        self._key = None
        self._last_modified = None
        self._size = None
        self._storage_class = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if e_tag is not None:
            self.e_tag = e_tag
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
        r"""Gets the owner of this Contents.

        :return: The owner of this Contents.
        :rtype: :class:`huaweicloudsdkobs.v1.Owner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this Contents.

        :param owner: The owner of this Contents.
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        """
        self._owner = owner

    @property
    def e_tag(self):
        r"""Gets the e_tag of this Contents.

        Base64-encoded 128-bit MD5 digest of an object. ETag is the unique identifier of the object content. It determines whether the object content changes. For example, when an object is uploaded, its ETag value is **A**, but when it is downloaded, its ETag value is **B**, this indicates that the object content changes. The ETag is a hash of the object. The ETag reflects changes only to the object content, rather than its metadata. An uploaded object or copied object has a unique ETag after being encrypted with MD5. (If the object is encrypted on the server side, the ETag value is not the MD5 digest of the object, but the unique identifier calculated through server-side encryption.)

        :return: The e_tag of this Contents.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this Contents.

        Base64-encoded 128-bit MD5 digest of an object. ETag is the unique identifier of the object content. It determines whether the object content changes. For example, when an object is uploaded, its ETag value is **A**, but when it is downloaded, its ETag value is **B**, this indicates that the object content changes. The ETag is a hash of the object. The ETag reflects changes only to the object content, rather than its metadata. An uploaded object or copied object has a unique ETag after being encrypted with MD5. (If the object is encrypted on the server side, the ETag value is not the MD5 digest of the object, but the unique identifier calculated through server-side encryption.)

        :param e_tag: The e_tag of this Contents.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def type(self):
        r"""Gets the type of this Contents.

        Object type. This parameter is returned when the object type is not **Normal**.

        :return: The type of this Contents.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Contents.

        Object type. This parameter is returned when the object type is not **Normal**.

        :param type: The type of this Contents.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        r"""Gets the key of this Contents.

        Name of the object

        :return: The key of this Contents.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Contents.

        Name of the object

        :param key: The key of this Contents.
        :type key: str
        """
        self._key = key

    @property
    def last_modified(self):
        r"""Gets the last_modified of this Contents.

        Time (UTC) when the object was last modified

        :return: The last_modified of this Contents.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this Contents.

        Time (UTC) when the object was last modified

        :param last_modified: The last_modified of this Contents.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def size(self):
        r"""Gets the size of this Contents.

        Object size in bytes

        :return: The size of this Contents.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Contents.

        Object size in bytes

        :param size: The size of this Contents.
        :type size: str
        """
        self._size = size

    @property
    def storage_class(self):
        r"""Gets the storage_class of this Contents.

        Storage class of the object

        :return: The storage_class of this Contents.
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        r"""Sets the storage_class of this Contents.

        Storage class of the object

        :param storage_class: The storage_class of this Contents.
        :type storage_class: str
        """
        self._storage_class = storage_class

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
        if not isinstance(other, Contents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
