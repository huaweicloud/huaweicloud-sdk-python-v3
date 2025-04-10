# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicScriptPropertiesModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_level': 'str',
        'version': 'str'
    }

    attribute_map = {
        'risk_level': 'risk_level',
        'version': 'version'
    }

    def __init__(self, risk_level=None, version=None):
        r"""PublicScriptPropertiesModel

        The model defined in huaweicloud sdk

        :param risk_level: 风险等级 LOW:低风险 MEDIUM:中风险 HIGH:高风险
        :type risk_level: str
        :param version: 脚本版本号
        :type version: str
        """
        
        

        self._risk_level = None
        self._version = None
        self.discriminator = None

        self.risk_level = risk_level
        self.version = version

    @property
    def risk_level(self):
        r"""Gets the risk_level of this PublicScriptPropertiesModel.

        风险等级 LOW:低风险 MEDIUM:中风险 HIGH:高风险

        :return: The risk_level of this PublicScriptPropertiesModel.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this PublicScriptPropertiesModel.

        风险等级 LOW:低风险 MEDIUM:中风险 HIGH:高风险

        :param risk_level: The risk_level of this PublicScriptPropertiesModel.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def version(self):
        r"""Gets the version of this PublicScriptPropertiesModel.

        脚本版本号

        :return: The version of this PublicScriptPropertiesModel.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PublicScriptPropertiesModel.

        脚本版本号

        :param version: The version of this PublicScriptPropertiesModel.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, PublicScriptPropertiesModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
