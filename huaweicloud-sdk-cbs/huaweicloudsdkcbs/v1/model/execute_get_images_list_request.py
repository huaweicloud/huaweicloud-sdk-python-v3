# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetImagesListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'resolution_type': 'int',
        'type': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'resolution_type': 'resolution_type',
        'type': 'type'
    }

    def __init__(self, limit=None, offset=None, resolution_type=None, type=None):
        """ExecuteGetImagesListRequest

        The model defined in huaweicloud sdk

        :param limit: 范围：大于等于1 默认：10
        :type limit: int
        :param offset: 范围：大于等于0 默认值：0
        :type offset: int
        :param resolution_type: 横竖屏模式 0：横屏（默认） 1：竖屏
        :type resolution_type: int
        :param type: 默认0 0：用户背景 1：系统背景 2：用户图标
        :type type: int
        """
        
        

        self._limit = None
        self._offset = None
        self._resolution_type = None
        self._type = None
        self.discriminator = None

        self.limit = limit
        self.offset = offset
        self.resolution_type = resolution_type
        self.type = type

    @property
    def limit(self):
        """Gets the limit of this ExecuteGetImagesListRequest.

        范围：大于等于1 默认：10

        :return: The limit of this ExecuteGetImagesListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ExecuteGetImagesListRequest.

        范围：大于等于1 默认：10

        :param limit: The limit of this ExecuteGetImagesListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ExecuteGetImagesListRequest.

        范围：大于等于0 默认值：0

        :return: The offset of this ExecuteGetImagesListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ExecuteGetImagesListRequest.

        范围：大于等于0 默认值：0

        :param offset: The offset of this ExecuteGetImagesListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def resolution_type(self):
        """Gets the resolution_type of this ExecuteGetImagesListRequest.

        横竖屏模式 0：横屏（默认） 1：竖屏

        :return: The resolution_type of this ExecuteGetImagesListRequest.
        :rtype: int
        """
        return self._resolution_type

    @resolution_type.setter
    def resolution_type(self, resolution_type):
        """Sets the resolution_type of this ExecuteGetImagesListRequest.

        横竖屏模式 0：横屏（默认） 1：竖屏

        :param resolution_type: The resolution_type of this ExecuteGetImagesListRequest.
        :type resolution_type: int
        """
        self._resolution_type = resolution_type

    @property
    def type(self):
        """Gets the type of this ExecuteGetImagesListRequest.

        默认0 0：用户背景 1：系统背景 2：用户图标

        :return: The type of this ExecuteGetImagesListRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExecuteGetImagesListRequest.

        默认0 0：用户背景 1：系统背景 2：用户图标

        :param type: The type of this ExecuteGetImagesListRequest.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ExecuteGetImagesListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
