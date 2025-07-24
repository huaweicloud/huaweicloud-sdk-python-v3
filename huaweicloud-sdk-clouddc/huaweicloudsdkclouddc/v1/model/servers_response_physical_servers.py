# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServersResponsePhysicalServers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None):
        r"""ServersResponsePhysicalServers

        The model defined in huaweicloud sdk

        :param id: UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type id: str
        """
        
        

        self._id = None
        self.discriminator = None

        if id is not None:
            self.id = id

    @property
    def id(self):
        r"""Gets the id of this ServersResponsePhysicalServers.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :return: The id of this ServersResponsePhysicalServers.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServersResponsePhysicalServers.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :param id: The id of this ServersResponsePhysicalServers.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ServersResponsePhysicalServers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
