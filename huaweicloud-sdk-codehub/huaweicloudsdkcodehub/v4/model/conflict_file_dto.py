# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConflictFileDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_path': 'str',
        'new_path': 'str'
    }

    attribute_map = {
        'old_path': 'old_path',
        'new_path': 'new_path'
    }

    def __init__(self, old_path=None, new_path=None):
        r"""ConflictFileDto

        The model defined in huaweicloud sdk

        :param old_path: 旧文件
        :type old_path: str
        :param new_path: 新文件
        :type new_path: str
        """
        
        

        self._old_path = None
        self._new_path = None
        self.discriminator = None

        if old_path is not None:
            self.old_path = old_path
        if new_path is not None:
            self.new_path = new_path

    @property
    def old_path(self):
        r"""Gets the old_path of this ConflictFileDto.

        旧文件

        :return: The old_path of this ConflictFileDto.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        r"""Sets the old_path of this ConflictFileDto.

        旧文件

        :param old_path: The old_path of this ConflictFileDto.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        r"""Gets the new_path of this ConflictFileDto.

        新文件

        :return: The new_path of this ConflictFileDto.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        r"""Sets the new_path of this ConflictFileDto.

        新文件

        :param new_path: The new_path of this ConflictFileDto.
        :type new_path: str
        """
        self._new_path = new_path

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
        if not isinstance(other, ConflictFileDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
