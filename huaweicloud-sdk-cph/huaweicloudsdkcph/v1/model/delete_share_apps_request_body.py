# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteShareAppsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_name': 'str',
        'server_ids': 'list[str]'
    }

    attribute_map = {
        'package_name': 'package_name',
        'server_ids': 'server_ids'
    }

    def __init__(self, package_name=None, server_ids=None):
        """DeleteShareAppsRequestBody

        The model defined in huaweicloud sdk

        :param package_name: 所需删除的共享应用的合法包名。最大长度128字节。只支持包含大小写字母、数字、下划线、点，其中不允许以数字和下划线开头，点不能作为结尾且包名中至少有一个点。
        :type package_name: str
        :param server_ids: 云手机服务器ID列表。
        :type server_ids: list[str]
        """
        
        

        self._package_name = None
        self._server_ids = None
        self.discriminator = None

        self.package_name = package_name
        self.server_ids = server_ids

    @property
    def package_name(self):
        """Gets the package_name of this DeleteShareAppsRequestBody.

        所需删除的共享应用的合法包名。最大长度128字节。只支持包含大小写字母、数字、下划线、点，其中不允许以数字和下划线开头，点不能作为结尾且包名中至少有一个点。

        :return: The package_name of this DeleteShareAppsRequestBody.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this DeleteShareAppsRequestBody.

        所需删除的共享应用的合法包名。最大长度128字节。只支持包含大小写字母、数字、下划线、点，其中不允许以数字和下划线开头，点不能作为结尾且包名中至少有一个点。

        :param package_name: The package_name of this DeleteShareAppsRequestBody.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def server_ids(self):
        """Gets the server_ids of this DeleteShareAppsRequestBody.

        云手机服务器ID列表。

        :return: The server_ids of this DeleteShareAppsRequestBody.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this DeleteShareAppsRequestBody.

        云手机服务器ID列表。

        :param server_ids: The server_ids of this DeleteShareAppsRequestBody.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

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
        if not isinstance(other, DeleteShareAppsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
