# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinksItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'link': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'link': 'link'
    }

    def __init__(self, file_name=None, link=None):
        """LinksItem

        The model defined in huaweicloud sdk

        :param file_name: 备份文件名称。
        :type file_name: str
        :param link: 备份文件下载链接地址。
        :type link: str
        """
        
        

        self._file_name = None
        self._link = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if link is not None:
            self.link = link

    @property
    def file_name(self):
        """Gets the file_name of this LinksItem.

        备份文件名称。

        :return: The file_name of this LinksItem.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this LinksItem.

        备份文件名称。

        :param file_name: The file_name of this LinksItem.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def link(self):
        """Gets the link of this LinksItem.

        备份文件下载链接地址。

        :return: The link of this LinksItem.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this LinksItem.

        备份文件下载链接地址。

        :param link: The link of this LinksItem.
        :type link: str
        """
        self._link = link

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
        if not isinstance(other, LinksItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
