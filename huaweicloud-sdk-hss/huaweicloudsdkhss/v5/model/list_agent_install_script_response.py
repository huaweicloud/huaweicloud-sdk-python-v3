# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentInstallScriptResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'install_script_list': 'list[AgentInstallScriptResponseInfo]'
    }

    attribute_map = {
        'install_script_list': 'install_script_list'
    }

    def __init__(self, install_script_list=None):
        r"""ListAgentInstallScriptResponse

        The model defined in huaweicloud sdk

        :param install_script_list: 安装脚本列表
        :type install_script_list: list[:class:`huaweicloudsdkhss.v5.AgentInstallScriptResponseInfo`]
        """
        
        super(ListAgentInstallScriptResponse, self).__init__()

        self._install_script_list = None
        self.discriminator = None

        if install_script_list is not None:
            self.install_script_list = install_script_list

    @property
    def install_script_list(self):
        r"""Gets the install_script_list of this ListAgentInstallScriptResponse.

        安装脚本列表

        :return: The install_script_list of this ListAgentInstallScriptResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AgentInstallScriptResponseInfo`]
        """
        return self._install_script_list

    @install_script_list.setter
    def install_script_list(self, install_script_list):
        r"""Sets the install_script_list of this ListAgentInstallScriptResponse.

        安装脚本列表

        :param install_script_list: The install_script_list of this ListAgentInstallScriptResponse.
        :type install_script_list: list[:class:`huaweicloudsdkhss.v5.AgentInstallScriptResponseInfo`]
        """
        self._install_script_list = install_script_list

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
        if not isinstance(other, ListAgentInstallScriptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
