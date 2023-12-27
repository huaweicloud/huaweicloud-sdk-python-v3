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
        """Contents

        The model defined in huaweicloud sdk

        :param owner: 
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        :param e_tag: 对象的base64编码的128位MD5摘要。ETag是对象内容的唯一标识，可以通过该值识别对象内容是否有变化。比如上传对象时ETag为A，下载对象时ETag为B，则说明对象内容发生了变化。实际的ETag是对象的哈希值。ETag只反映变化的内容，而不是其元数据。上传的对象或拷贝操作创建的对象，通过MD5加密后都有唯一的ETag。（当对象是服务端加密的对象时，ETag值不是对象的MD5值，而是通过服务端加密计算出的唯一标识。） 
        :type e_tag: str
        :param type: 对象类型，非Normal对象时返回。 
        :type type: str
        :param key: 对象名。 
        :type key: str
        :param last_modified: 对象最近一次被修改的时间（UTC时间）。 
        :type last_modified: str
        :param size: 对象的字节数。 
        :type size: str
        :param storage_class: 对象的存储类型。 
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
        """Gets the owner of this Contents.

        :return: The owner of this Contents.
        :rtype: :class:`huaweicloudsdkobs.v1.Owner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Contents.

        :param owner: The owner of this Contents.
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        """
        self._owner = owner

    @property
    def e_tag(self):
        """Gets the e_tag of this Contents.

        对象的base64编码的128位MD5摘要。ETag是对象内容的唯一标识，可以通过该值识别对象内容是否有变化。比如上传对象时ETag为A，下载对象时ETag为B，则说明对象内容发生了变化。实际的ETag是对象的哈希值。ETag只反映变化的内容，而不是其元数据。上传的对象或拷贝操作创建的对象，通过MD5加密后都有唯一的ETag。（当对象是服务端加密的对象时，ETag值不是对象的MD5值，而是通过服务端加密计算出的唯一标识。） 

        :return: The e_tag of this Contents.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        """Sets the e_tag of this Contents.

        对象的base64编码的128位MD5摘要。ETag是对象内容的唯一标识，可以通过该值识别对象内容是否有变化。比如上传对象时ETag为A，下载对象时ETag为B，则说明对象内容发生了变化。实际的ETag是对象的哈希值。ETag只反映变化的内容，而不是其元数据。上传的对象或拷贝操作创建的对象，通过MD5加密后都有唯一的ETag。（当对象是服务端加密的对象时，ETag值不是对象的MD5值，而是通过服务端加密计算出的唯一标识。） 

        :param e_tag: The e_tag of this Contents.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def type(self):
        """Gets the type of this Contents.

        对象类型，非Normal对象时返回。 

        :return: The type of this Contents.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Contents.

        对象类型，非Normal对象时返回。 

        :param type: The type of this Contents.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        """Gets the key of this Contents.

        对象名。 

        :return: The key of this Contents.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Contents.

        对象名。 

        :param key: The key of this Contents.
        :type key: str
        """
        self._key = key

    @property
    def last_modified(self):
        """Gets the last_modified of this Contents.

        对象最近一次被修改的时间（UTC时间）。 

        :return: The last_modified of this Contents.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Contents.

        对象最近一次被修改的时间（UTC时间）。 

        :param last_modified: The last_modified of this Contents.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def size(self):
        """Gets the size of this Contents.

        对象的字节数。 

        :return: The size of this Contents.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Contents.

        对象的字节数。 

        :param size: The size of this Contents.
        :type size: str
        """
        self._size = size

    @property
    def storage_class(self):
        """Gets the storage_class of this Contents.

        对象的存储类型。 

        :return: The storage_class of this Contents.
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this Contents.

        对象的存储类型。 

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
