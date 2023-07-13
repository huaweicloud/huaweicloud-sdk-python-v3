# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShareFolderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'folder_name': 'str'
    }

    attribute_map = {
        'folder_name': 'folder_name'
    }

    def __init__(self, folder_name=None):
        """CreateShareFolderReq

        The model defined in huaweicloud sdk

        :param folder_name: - 仅支持创建单层级的文件夹 - 单个文件夹名称仅支持以下字符: 英文字母、数字、空格、下划线、中划线 - 名称不能超过32字符 - 不能为全空格或者以空格开头
        :type folder_name: str
        """
        
        

        self._folder_name = None
        self.discriminator = None

        if folder_name is not None:
            self.folder_name = folder_name

    @property
    def folder_name(self):
        """Gets the folder_name of this CreateShareFolderReq.

        - 仅支持创建单层级的文件夹 - 单个文件夹名称仅支持以下字符: 英文字母、数字、空格、下划线、中划线 - 名称不能超过32字符 - 不能为全空格或者以空格开头

        :return: The folder_name of this CreateShareFolderReq.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this CreateShareFolderReq.

        - 仅支持创建单层级的文件夹 - 单个文件夹名称仅支持以下字符: 英文字母、数字、空格、下划线、中划线 - 名称不能超过32字符 - 不能为全空格或者以空格开头

        :param folder_name: The folder_name of this CreateShareFolderReq.
        :type folder_name: str
        """
        self._folder_name = folder_name

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
        if not isinstance(other, CreateShareFolderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
