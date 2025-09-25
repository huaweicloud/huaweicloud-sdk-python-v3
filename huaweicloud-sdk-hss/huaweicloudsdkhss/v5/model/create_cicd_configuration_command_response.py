# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCicdConfigurationCommandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cicd_command': 'str'
    }

    attribute_map = {
        'cicd_command': 'cicd_command'
    }

    def __init__(self, cicd_command=None):
        r"""CreateCicdConfigurationCommandResponse

        The model defined in huaweicloud sdk

        :param cicd_command: **参数解释**： cicd接入配置命令 **取值范围**： 字符长度1-1024位 
        :type cicd_command: str
        """
        
        super(CreateCicdConfigurationCommandResponse, self).__init__()

        self._cicd_command = None
        self.discriminator = None

        if cicd_command is not None:
            self.cicd_command = cicd_command

    @property
    def cicd_command(self):
        r"""Gets the cicd_command of this CreateCicdConfigurationCommandResponse.

        **参数解释**： cicd接入配置命令 **取值范围**： 字符长度1-1024位 

        :return: The cicd_command of this CreateCicdConfigurationCommandResponse.
        :rtype: str
        """
        return self._cicd_command

    @cicd_command.setter
    def cicd_command(self, cicd_command):
        r"""Sets the cicd_command of this CreateCicdConfigurationCommandResponse.

        **参数解释**： cicd接入配置命令 **取值范围**： 字符长度1-1024位 

        :param cicd_command: The cicd_command of this CreateCicdConfigurationCommandResponse.
        :type cicd_command: str
        """
        self._cicd_command = cicd_command

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
        if not isinstance(other, CreateCicdConfigurationCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
