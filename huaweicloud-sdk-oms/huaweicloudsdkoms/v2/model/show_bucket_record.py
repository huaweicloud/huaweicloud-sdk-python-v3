# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBucketRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'size': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size'
    }

    def __init__(self, name=None, size=None):
        r"""ShowBucketRecord

        The model defined in huaweicloud sdk

        :param name: 对象名
        :type name: str
        :param size: 对象大小，若对象无size属性，则返回--
        :type size: str
        """
        
        

        self._name = None
        self._size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size

    @property
    def name(self):
        r"""Gets the name of this ShowBucketRecord.

        对象名

        :return: The name of this ShowBucketRecord.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBucketRecord.

        对象名

        :param name: The name of this ShowBucketRecord.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this ShowBucketRecord.

        对象大小，若对象无size属性，则返回--

        :return: The size of this ShowBucketRecord.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowBucketRecord.

        对象大小，若对象无size属性，则返回--

        :param size: The size of this ShowBucketRecord.
        :type size: str
        """
        self._size = size

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
        if not isinstance(other, ShowBucketRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
