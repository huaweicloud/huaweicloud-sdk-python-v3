# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentAddPathReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_path': 'list[str]',
        'exclude_path': 'list[ExcludePath]'
    }

    attribute_map = {
        'add_path': 'add_path',
        'exclude_path': 'exclude_path'
    }

    def __init__(self, add_path=None, exclude_path=None):
        r"""AgentAddPathReq

        The model defined in huaweicloud sdk

        :param add_path: 增加备份路径详情
        :type add_path: list[str]
        :param exclude_path: 增加排除目录 &gt; 该特性目前处于公测阶段，部分region可能无法使用。
        :type exclude_path: list[:class:`huaweicloudsdkcbr.v1.ExcludePath`]
        """
        
        

        self._add_path = None
        self._exclude_path = None
        self.discriminator = None

        self.add_path = add_path
        if exclude_path is not None:
            self.exclude_path = exclude_path

    @property
    def add_path(self):
        r"""Gets the add_path of this AgentAddPathReq.

        增加备份路径详情

        :return: The add_path of this AgentAddPathReq.
        :rtype: list[str]
        """
        return self._add_path

    @add_path.setter
    def add_path(self, add_path):
        r"""Sets the add_path of this AgentAddPathReq.

        增加备份路径详情

        :param add_path: The add_path of this AgentAddPathReq.
        :type add_path: list[str]
        """
        self._add_path = add_path

    @property
    def exclude_path(self):
        r"""Gets the exclude_path of this AgentAddPathReq.

        增加排除目录 > 该特性目前处于公测阶段，部分region可能无法使用。

        :return: The exclude_path of this AgentAddPathReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ExcludePath`]
        """
        return self._exclude_path

    @exclude_path.setter
    def exclude_path(self, exclude_path):
        r"""Sets the exclude_path of this AgentAddPathReq.

        增加排除目录 > 该特性目前处于公测阶段，部分region可能无法使用。

        :param exclude_path: The exclude_path of this AgentAddPathReq.
        :type exclude_path: list[:class:`huaweicloudsdkcbr.v1.ExcludePath`]
        """
        self._exclude_path = exclude_path

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
        if not isinstance(other, AgentAddPathReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
