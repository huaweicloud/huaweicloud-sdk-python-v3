# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonRisks:

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
        'alias': 'str'
    }

    attribute_map = {
        'addon_template_name': 'addonTemplateName',
        'alias': 'alias'
    }

    def __init__(self, addon_template_name=None, alias=None):
        """AddonRisks

        The model defined in huaweicloud sdk

        :param addon_template_name: 插件模板名称
        :type addon_template_name: str
        :param alias: 插件别名
        :type alias: str
        """
        
        

        self._addon_template_name = None
        self._alias = None
        self.discriminator = None

        if addon_template_name is not None:
            self.addon_template_name = addon_template_name
        if alias is not None:
            self.alias = alias

    @property
    def addon_template_name(self):
        """Gets the addon_template_name of this AddonRisks.

        插件模板名称

        :return: The addon_template_name of this AddonRisks.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        """Sets the addon_template_name of this AddonRisks.

        插件模板名称

        :param addon_template_name: The addon_template_name of this AddonRisks.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def alias(self):
        """Gets the alias of this AddonRisks.

        插件别名

        :return: The alias of this AddonRisks.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AddonRisks.

        插件别名

        :param alias: The alias of this AddonRisks.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, AddonRisks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
