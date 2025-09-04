# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FolderInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prefix': 'str',
        'inode_no': 'int'
    }

    attribute_map = {
        'prefix': 'prefix',
        'inode_no': 'inode_no'
    }

    def __init__(self, prefix=None, inode_no=None):
        r"""FolderInfo

        The model defined in huaweicloud sdk

        :param prefix: 文件夹名称。
        :type prefix: str
        :param inode_no: 文件inode。
        :type inode_no: int
        """
        
        

        self._prefix = None
        self._inode_no = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if inode_no is not None:
            self.inode_no = inode_no

    @property
    def prefix(self):
        r"""Gets the prefix of this FolderInfo.

        文件夹名称。

        :return: The prefix of this FolderInfo.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this FolderInfo.

        文件夹名称。

        :param prefix: The prefix of this FolderInfo.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def inode_no(self):
        r"""Gets the inode_no of this FolderInfo.

        文件inode。

        :return: The inode_no of this FolderInfo.
        :rtype: int
        """
        return self._inode_no

    @inode_no.setter
    def inode_no(self, inode_no):
        r"""Sets the inode_no of this FolderInfo.

        文件inode。

        :param inode_no: The inode_no of this FolderInfo.
        :type inode_no: int
        """
        self._inode_no = inode_no

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
        if not isinstance(other, FolderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
