# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstallCmdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cmd': 'str'
    }

    attribute_map = {
        'cmd': 'cmd'
    }

    def __init__(self, cmd=None):
        """CreateInstallCmdResponse

        The model defined in huaweicloud sdk

        :param cmd: 标准版节点安装/升级命令
        :type cmd: str
        """
        
        super(CreateInstallCmdResponse, self).__init__()

        self._cmd = None
        self.discriminator = None

        if cmd is not None:
            self.cmd = cmd

    @property
    def cmd(self):
        """Gets the cmd of this CreateInstallCmdResponse.

        标准版节点安装/升级命令

        :return: The cmd of this CreateInstallCmdResponse.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        """Sets the cmd of this CreateInstallCmdResponse.

        标准版节点安装/升级命令

        :param cmd: The cmd of this CreateInstallCmdResponse.
        :type cmd: str
        """
        self._cmd = cmd

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
        if not isinstance(other, CreateInstallCmdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
