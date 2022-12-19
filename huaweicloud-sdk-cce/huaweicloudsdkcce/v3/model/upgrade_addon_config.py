# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeAddonConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addon_template_name': 'str',
        'operation': 'str',
        'version': 'str',
        'values': 'object'
    }

    attribute_map = {
        'addon_template_name': 'addonTemplateName',
        'operation': 'operation',
        'version': 'version',
        'values': 'values'
    }

    def __init__(self, addon_template_name=None, operation=None, version=None, values=None):
        """UpgradeAddonConfig

        The model defined in huaweicloud sdk

        :param addon_template_name: 插件名称
        :type addon_template_name: str
        :param operation: 执行动作，当前升级场景支持操作为\&quot;patch\&quot;
        :type operation: str
        :param version: 目标插件版本号
        :type version: str
        :param values: 插件参数列表，Key:Value格式
        :type values: object
        """
        
        

        self._addon_template_name = None
        self._operation = None
        self._version = None
        self._values = None
        self.discriminator = None

        self.addon_template_name = addon_template_name
        self.operation = operation
        self.version = version
        if values is not None:
            self.values = values

    @property
    def addon_template_name(self):
        """Gets the addon_template_name of this UpgradeAddonConfig.

        插件名称

        :return: The addon_template_name of this UpgradeAddonConfig.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        """Sets the addon_template_name of this UpgradeAddonConfig.

        插件名称

        :param addon_template_name: The addon_template_name of this UpgradeAddonConfig.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def operation(self):
        """Gets the operation of this UpgradeAddonConfig.

        执行动作，当前升级场景支持操作为\"patch\"

        :return: The operation of this UpgradeAddonConfig.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this UpgradeAddonConfig.

        执行动作，当前升级场景支持操作为\"patch\"

        :param operation: The operation of this UpgradeAddonConfig.
        :type operation: str
        """
        self._operation = operation

    @property
    def version(self):
        """Gets the version of this UpgradeAddonConfig.

        目标插件版本号

        :return: The version of this UpgradeAddonConfig.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpgradeAddonConfig.

        目标插件版本号

        :param version: The version of this UpgradeAddonConfig.
        :type version: str
        """
        self._version = version

    @property
    def values(self):
        """Gets the values of this UpgradeAddonConfig.

        插件参数列表，Key:Value格式

        :return: The values of this UpgradeAddonConfig.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this UpgradeAddonConfig.

        插件参数列表，Key:Value格式

        :param values: The values of this UpgradeAddonConfig.
        :type values: object
        """
        self._values = values

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
        if not isinstance(other, UpgradeAddonConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
