# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'created_by': 'str',
        'empty_layer': 'bool',
        'media_type': 'str',
        'size': 'int',
        'digest': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'created_by': 'created_by',
        'empty_layer': 'empty_layer',
        'media_type': 'mediaType',
        'size': 'size',
        'digest': 'digest'
    }

    def __init__(self, created_at=None, created_by=None, empty_layer=None, media_type=None, size=None, digest=None):
        r"""BuildHistory

        The model defined in huaweicloud sdk

        :param created_at: 构建时间
        :type created_at: str
        :param created_by: 构建命令
        :type created_by: str
        :param empty_layer: 是否空层
        :type empty_layer: bool
        :param media_type: 层格式
        :type media_type: str
        :param size: 层大小
        :type size: int
        :param digest: 层sha256信息
        :type digest: str
        """
        
        

        self._created_at = None
        self._created_by = None
        self._empty_layer = None
        self._media_type = None
        self._size = None
        self._digest = None
        self.discriminator = None

        self.created_at = created_at
        self.created_by = created_by
        self.empty_layer = empty_layer
        self.media_type = media_type
        self.size = size
        self.digest = digest

    @property
    def created_at(self):
        r"""Gets the created_at of this BuildHistory.

        构建时间

        :return: The created_at of this BuildHistory.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BuildHistory.

        构建时间

        :param created_at: The created_at of this BuildHistory.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def created_by(self):
        r"""Gets the created_by of this BuildHistory.

        构建命令

        :return: The created_by of this BuildHistory.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this BuildHistory.

        构建命令

        :param created_by: The created_by of this BuildHistory.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def empty_layer(self):
        r"""Gets the empty_layer of this BuildHistory.

        是否空层

        :return: The empty_layer of this BuildHistory.
        :rtype: bool
        """
        return self._empty_layer

    @empty_layer.setter
    def empty_layer(self, empty_layer):
        r"""Sets the empty_layer of this BuildHistory.

        是否空层

        :param empty_layer: The empty_layer of this BuildHistory.
        :type empty_layer: bool
        """
        self._empty_layer = empty_layer

    @property
    def media_type(self):
        r"""Gets the media_type of this BuildHistory.

        层格式

        :return: The media_type of this BuildHistory.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        r"""Sets the media_type of this BuildHistory.

        层格式

        :param media_type: The media_type of this BuildHistory.
        :type media_type: str
        """
        self._media_type = media_type

    @property
    def size(self):
        r"""Gets the size of this BuildHistory.

        层大小

        :return: The size of this BuildHistory.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BuildHistory.

        层大小

        :param size: The size of this BuildHistory.
        :type size: int
        """
        self._size = size

    @property
    def digest(self):
        r"""Gets the digest of this BuildHistory.

        层sha256信息

        :return: The digest of this BuildHistory.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this BuildHistory.

        层sha256信息

        :param digest: The digest of this BuildHistory.
        :type digest: str
        """
        self._digest = digest

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
        if not isinstance(other, BuildHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
