# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRedirectPoolsExtendConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rewrite_url_enable': 'bool',
        'rewrite_url_config': 'CreateRewriteUrlConfig'
    }

    attribute_map = {
        'rewrite_url_enable': 'rewrite_url_enable',
        'rewrite_url_config': 'rewrite_url_config'
    }

    def __init__(self, rewrite_url_enable=None, rewrite_url_config=None):
        """CreateRedirectPoolsExtendConfig

        The model defined in huaweicloud sdk

        :param rewrite_url_enable: url重写的开关
        :type rewrite_url_enable: bool
        :param rewrite_url_config: 
        :type rewrite_url_config: :class:`huaweicloudsdkelb.v3.CreateRewriteUrlConfig`
        """
        
        

        self._rewrite_url_enable = None
        self._rewrite_url_config = None
        self.discriminator = None

        if rewrite_url_enable is not None:
            self.rewrite_url_enable = rewrite_url_enable
        if rewrite_url_config is not None:
            self.rewrite_url_config = rewrite_url_config

    @property
    def rewrite_url_enable(self):
        """Gets the rewrite_url_enable of this CreateRedirectPoolsExtendConfig.

        url重写的开关

        :return: The rewrite_url_enable of this CreateRedirectPoolsExtendConfig.
        :rtype: bool
        """
        return self._rewrite_url_enable

    @rewrite_url_enable.setter
    def rewrite_url_enable(self, rewrite_url_enable):
        """Sets the rewrite_url_enable of this CreateRedirectPoolsExtendConfig.

        url重写的开关

        :param rewrite_url_enable: The rewrite_url_enable of this CreateRedirectPoolsExtendConfig.
        :type rewrite_url_enable: bool
        """
        self._rewrite_url_enable = rewrite_url_enable

    @property
    def rewrite_url_config(self):
        """Gets the rewrite_url_config of this CreateRedirectPoolsExtendConfig.

        :return: The rewrite_url_config of this CreateRedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateRewriteUrlConfig`
        """
        return self._rewrite_url_config

    @rewrite_url_config.setter
    def rewrite_url_config(self, rewrite_url_config):
        """Sets the rewrite_url_config of this CreateRedirectPoolsExtendConfig.

        :param rewrite_url_config: The rewrite_url_config of this CreateRedirectPoolsExtendConfig.
        :type rewrite_url_config: :class:`huaweicloudsdkelb.v3.CreateRewriteUrlConfig`
        """
        self._rewrite_url_config = rewrite_url_config

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
        if not isinstance(other, CreateRedirectPoolsExtendConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
