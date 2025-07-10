# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsDriverInterfaceRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_redir_driver_list': 'str'
    }

    attribute_map = {
        'api_redir_driver_list': 'api_redir_driver_list'
    }

    def __init__(self, api_redir_driver_list=None):
        r"""PoliciesPeripheralsDriverInterfaceRedirection

        The model defined in huaweicloud sdk

        :param api_redir_driver_list: 自定义驱动列表。（填写安装在终端的驱动文件名或驱动文件的全路径，支持配置多个，多个之间以\&quot;;\&quot;隔开），长度不能超过1000个字符。
        :type api_redir_driver_list: str
        """
        
        

        self._api_redir_driver_list = None
        self.discriminator = None

        if api_redir_driver_list is not None:
            self.api_redir_driver_list = api_redir_driver_list

    @property
    def api_redir_driver_list(self):
        r"""Gets the api_redir_driver_list of this PoliciesPeripheralsDriverInterfaceRedirection.

        自定义驱动列表。（填写安装在终端的驱动文件名或驱动文件的全路径，支持配置多个，多个之间以\";\"隔开），长度不能超过1000个字符。

        :return: The api_redir_driver_list of this PoliciesPeripheralsDriverInterfaceRedirection.
        :rtype: str
        """
        return self._api_redir_driver_list

    @api_redir_driver_list.setter
    def api_redir_driver_list(self, api_redir_driver_list):
        r"""Sets the api_redir_driver_list of this PoliciesPeripheralsDriverInterfaceRedirection.

        自定义驱动列表。（填写安装在终端的驱动文件名或驱动文件的全路径，支持配置多个，多个之间以\";\"隔开），长度不能超过1000个字符。

        :param api_redir_driver_list: The api_redir_driver_list of this PoliciesPeripheralsDriverInterfaceRedirection.
        :type api_redir_driver_list: str
        """
        self._api_redir_driver_list = api_redir_driver_list

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
        if not isinstance(other, PoliciesPeripheralsDriverInterfaceRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
