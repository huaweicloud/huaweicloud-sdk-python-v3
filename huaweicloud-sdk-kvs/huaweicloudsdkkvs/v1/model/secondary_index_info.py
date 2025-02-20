# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecondaryIndexInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_name': 'str',
        'index_status': 'str'
    }

    attribute_map = {
        'index_name': 'index_name',
        'index_status': 'index_status'
    }

    def __init__(self, index_name=None, index_status=None):
        """SecondaryIndexInfo

        The model defined in huaweicloud sdk

        :param index_name: 索引状态。 - 长度：[1, 255] - 取值字符限制：[a-z0-9_-]+
        :type index_name: str
        :param index_status: 索引状态。 - \&quot;creating\&quot; - \&quot;active\&quot; - \&quot;deleting\&quot;
        :type index_status: str
        """
        
        

        self._index_name = None
        self._index_status = None
        self.discriminator = None

        self.index_name = index_name
        self.index_status = index_status

    @property
    def index_name(self):
        """Gets the index_name of this SecondaryIndexInfo.

        索引状态。 - 长度：[1, 255] - 取值字符限制：[a-z0-9_-]+

        :return: The index_name of this SecondaryIndexInfo.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this SecondaryIndexInfo.

        索引状态。 - 长度：[1, 255] - 取值字符限制：[a-z0-9_-]+

        :param index_name: The index_name of this SecondaryIndexInfo.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def index_status(self):
        """Gets the index_status of this SecondaryIndexInfo.

        索引状态。 - \"creating\" - \"active\" - \"deleting\"

        :return: The index_status of this SecondaryIndexInfo.
        :rtype: str
        """
        return self._index_status

    @index_status.setter
    def index_status(self, index_status):
        """Sets the index_status of this SecondaryIndexInfo.

        索引状态。 - \"creating\" - \"active\" - \"deleting\"

        :param index_status: The index_status of this SecondaryIndexInfo.
        :type index_status: str
        """
        self._index_status = index_status

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
        if not isinstance(other, SecondaryIndexInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
