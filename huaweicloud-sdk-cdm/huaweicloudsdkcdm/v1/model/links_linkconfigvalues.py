# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinksLinkconfigvalues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'list[Configs]',
        'extended_configs': 'LinksLinkconfigvaluesExtendedconfigs',
        'validators': 'list[str]'
    }

    attribute_map = {
        'configs': 'configs',
        'extended_configs': 'extended-configs',
        'validators': 'validators'
    }

    def __init__(self, configs=None, extended_configs=None, validators=None):
        """LinksLinkconfigvalues

        The model defined in huaweicloud sdk

        :param configs: 连接配置参数数据结构，请参见configs参数说明。
        :type configs: list[:class:`huaweicloudsdkcdm.v1.Configs`]
        :param extended_configs: 
        :type extended_configs: :class:`huaweicloudsdkcdm.v1.LinksLinkconfigvaluesExtendedconfigs`
        :param validators: 校验器
        :type validators: list[str]
        """
        
        

        self._configs = None
        self._extended_configs = None
        self._validators = None
        self.discriminator = None

        self.configs = configs
        if extended_configs is not None:
            self.extended_configs = extended_configs
        if validators is not None:
            self.validators = validators

    @property
    def configs(self):
        """Gets the configs of this LinksLinkconfigvalues.

        连接配置参数数据结构，请参见configs参数说明。

        :return: The configs of this LinksLinkconfigvalues.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Configs`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this LinksLinkconfigvalues.

        连接配置参数数据结构，请参见configs参数说明。

        :param configs: The configs of this LinksLinkconfigvalues.
        :type configs: list[:class:`huaweicloudsdkcdm.v1.Configs`]
        """
        self._configs = configs

    @property
    def extended_configs(self):
        """Gets the extended_configs of this LinksLinkconfigvalues.

        :return: The extended_configs of this LinksLinkconfigvalues.
        :rtype: :class:`huaweicloudsdkcdm.v1.LinksLinkconfigvaluesExtendedconfigs`
        """
        return self._extended_configs

    @extended_configs.setter
    def extended_configs(self, extended_configs):
        """Sets the extended_configs of this LinksLinkconfigvalues.

        :param extended_configs: The extended_configs of this LinksLinkconfigvalues.
        :type extended_configs: :class:`huaweicloudsdkcdm.v1.LinksLinkconfigvaluesExtendedconfigs`
        """
        self._extended_configs = extended_configs

    @property
    def validators(self):
        """Gets the validators of this LinksLinkconfigvalues.

        校验器

        :return: The validators of this LinksLinkconfigvalues.
        :rtype: list[str]
        """
        return self._validators

    @validators.setter
    def validators(self, validators):
        """Sets the validators of this LinksLinkconfigvalues.

        校验器

        :param validators: The validators of this LinksLinkconfigvalues.
        :type validators: list[str]
        """
        self._validators = validators

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
        if not isinstance(other, LinksLinkconfigvalues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
