# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncLogConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'stream_name': 'str',
        'stream_id': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'stream_name': 'stream_name',
        'stream_id': 'stream_id'
    }

    def __init__(self, group_name=None, group_id=None, stream_name=None, stream_id=None):
        r"""FuncLogConfig

        The model defined in huaweicloud sdk

        :param group_name: 函数绑定日志组名。
        :type group_name: str
        :param group_id: 函数绑定日志组ID。
        :type group_id: str
        :param stream_name: 函数绑定日志流名。
        :type stream_name: str
        :param stream_id: 函数绑定日志流ID。
        :type stream_id: str
        """
        
        

        self._group_name = None
        self._group_id = None
        self._stream_name = None
        self._stream_id = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if stream_name is not None:
            self.stream_name = stream_name
        if stream_id is not None:
            self.stream_id = stream_id

    @property
    def group_name(self):
        r"""Gets the group_name of this FuncLogConfig.

        函数绑定日志组名。

        :return: The group_name of this FuncLogConfig.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this FuncLogConfig.

        函数绑定日志组名。

        :param group_name: The group_name of this FuncLogConfig.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this FuncLogConfig.

        函数绑定日志组ID。

        :return: The group_id of this FuncLogConfig.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this FuncLogConfig.

        函数绑定日志组ID。

        :param group_id: The group_id of this FuncLogConfig.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_name(self):
        r"""Gets the stream_name of this FuncLogConfig.

        函数绑定日志流名。

        :return: The stream_name of this FuncLogConfig.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this FuncLogConfig.

        函数绑定日志流名。

        :param stream_name: The stream_name of this FuncLogConfig.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def stream_id(self):
        r"""Gets the stream_id of this FuncLogConfig.

        函数绑定日志流ID。

        :return: The stream_id of this FuncLogConfig.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this FuncLogConfig.

        函数绑定日志流ID。

        :param stream_id: The stream_id of this FuncLogConfig.
        :type stream_id: str
        """
        self._stream_id = stream_id

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
        if not isinstance(other, FuncLogConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
