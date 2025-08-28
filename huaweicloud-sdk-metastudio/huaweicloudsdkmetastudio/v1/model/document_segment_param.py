# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentSegmentParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'split_type': 'int',
        'chunk_size': 'int',
        'chunk_type': 'str',
        'separators': 'list[str]'
    }

    attribute_map = {
        'split_type': 'split_type',
        'chunk_size': 'chunk_size',
        'chunk_type': 'chunk_type',
        'separators': 'separators'
    }

    def __init__(self, split_type=None, chunk_size=None, chunk_type=None, separators=None):
        r"""DocumentSegmentParam

        The model defined in huaweicloud sdk

        :param split_type: 分段类型 * 1: 自动分段 * 2: 手动分段
        :type split_type: int
        :param chunk_size: 分段长度。
        :type chunk_size: int
        :param chunk_type: 分段策略，多个策略之间用逗号分割。 &gt; title:标题分割；separator:分隔符分割
        :type chunk_type: str
        :param separators: 分隔符
        :type separators: list[str]
        """
        
        

        self._split_type = None
        self._chunk_size = None
        self._chunk_type = None
        self._separators = None
        self.discriminator = None

        self.split_type = split_type
        if chunk_size is not None:
            self.chunk_size = chunk_size
        if chunk_type is not None:
            self.chunk_type = chunk_type
        if separators is not None:
            self.separators = separators

    @property
    def split_type(self):
        r"""Gets the split_type of this DocumentSegmentParam.

        分段类型 * 1: 自动分段 * 2: 手动分段

        :return: The split_type of this DocumentSegmentParam.
        :rtype: int
        """
        return self._split_type

    @split_type.setter
    def split_type(self, split_type):
        r"""Sets the split_type of this DocumentSegmentParam.

        分段类型 * 1: 自动分段 * 2: 手动分段

        :param split_type: The split_type of this DocumentSegmentParam.
        :type split_type: int
        """
        self._split_type = split_type

    @property
    def chunk_size(self):
        r"""Gets the chunk_size of this DocumentSegmentParam.

        分段长度。

        :return: The chunk_size of this DocumentSegmentParam.
        :rtype: int
        """
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, chunk_size):
        r"""Sets the chunk_size of this DocumentSegmentParam.

        分段长度。

        :param chunk_size: The chunk_size of this DocumentSegmentParam.
        :type chunk_size: int
        """
        self._chunk_size = chunk_size

    @property
    def chunk_type(self):
        r"""Gets the chunk_type of this DocumentSegmentParam.

        分段策略，多个策略之间用逗号分割。 > title:标题分割；separator:分隔符分割

        :return: The chunk_type of this DocumentSegmentParam.
        :rtype: str
        """
        return self._chunk_type

    @chunk_type.setter
    def chunk_type(self, chunk_type):
        r"""Sets the chunk_type of this DocumentSegmentParam.

        分段策略，多个策略之间用逗号分割。 > title:标题分割；separator:分隔符分割

        :param chunk_type: The chunk_type of this DocumentSegmentParam.
        :type chunk_type: str
        """
        self._chunk_type = chunk_type

    @property
    def separators(self):
        r"""Gets the separators of this DocumentSegmentParam.

        分隔符

        :return: The separators of this DocumentSegmentParam.
        :rtype: list[str]
        """
        return self._separators

    @separators.setter
    def separators(self, separators):
        r"""Sets the separators of this DocumentSegmentParam.

        分隔符

        :param separators: The separators of this DocumentSegmentParam.
        :type separators: list[str]
        """
        self._separators = separators

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
        if not isinstance(other, DocumentSegmentParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
