# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedirectPoolsExtendConfig:

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
        'rewrite_url_config': 'RewriteUrlConfig',
        'insert_headers_config': 'InsertHeadersConfig',
        'remove_headers_config': 'RemoveHeadersConfig',
        'traffic_limit_config': 'TrafficLimitConfig',
        'cors_config': 'CorsConfig',
        'traffic_mirror_config': 'TrafficMirrorConfig'
    }

    attribute_map = {
        'rewrite_url_enable': 'rewrite_url_enable',
        'rewrite_url_config': 'rewrite_url_config',
        'insert_headers_config': 'insert_headers_config',
        'remove_headers_config': 'remove_headers_config',
        'traffic_limit_config': 'traffic_limit_config',
        'cors_config': 'cors_config',
        'traffic_mirror_config': 'traffic_mirror_config'
    }

    def __init__(self, rewrite_url_enable=None, rewrite_url_config=None, insert_headers_config=None, remove_headers_config=None, traffic_limit_config=None, cors_config=None, traffic_mirror_config=None):
        r"""RedirectPoolsExtendConfig

        The model defined in huaweicloud sdk

        :param rewrite_url_enable: **参数解释**：是否开启url重定向。  **取值范围**：true 开启，false 未开启。
        :type rewrite_url_enable: bool
        :param rewrite_url_config: 
        :type rewrite_url_config: :class:`huaweicloudsdkelb.v3.RewriteUrlConfig`
        :param insert_headers_config: 
        :type insert_headers_config: :class:`huaweicloudsdkelb.v3.InsertHeadersConfig`
        :param remove_headers_config: 
        :type remove_headers_config: :class:`huaweicloudsdkelb.v3.RemoveHeadersConfig`
        :param traffic_limit_config: 
        :type traffic_limit_config: :class:`huaweicloudsdkelb.v3.TrafficLimitConfig`
        :param cors_config: 
        :type cors_config: :class:`huaweicloudsdkelb.v3.CorsConfig`
        :param traffic_mirror_config: 
        :type traffic_mirror_config: :class:`huaweicloudsdkelb.v3.TrafficMirrorConfig`
        """
        
        

        self._rewrite_url_enable = None
        self._rewrite_url_config = None
        self._insert_headers_config = None
        self._remove_headers_config = None
        self._traffic_limit_config = None
        self._cors_config = None
        self._traffic_mirror_config = None
        self.discriminator = None

        if rewrite_url_enable is not None:
            self.rewrite_url_enable = rewrite_url_enable
        if rewrite_url_config is not None:
            self.rewrite_url_config = rewrite_url_config
        if insert_headers_config is not None:
            self.insert_headers_config = insert_headers_config
        if remove_headers_config is not None:
            self.remove_headers_config = remove_headers_config
        if traffic_limit_config is not None:
            self.traffic_limit_config = traffic_limit_config
        if cors_config is not None:
            self.cors_config = cors_config
        if traffic_mirror_config is not None:
            self.traffic_mirror_config = traffic_mirror_config

    @property
    def rewrite_url_enable(self):
        r"""Gets the rewrite_url_enable of this RedirectPoolsExtendConfig.

        **参数解释**：是否开启url重定向。  **取值范围**：true 开启，false 未开启。

        :return: The rewrite_url_enable of this RedirectPoolsExtendConfig.
        :rtype: bool
        """
        return self._rewrite_url_enable

    @rewrite_url_enable.setter
    def rewrite_url_enable(self, rewrite_url_enable):
        r"""Sets the rewrite_url_enable of this RedirectPoolsExtendConfig.

        **参数解释**：是否开启url重定向。  **取值范围**：true 开启，false 未开启。

        :param rewrite_url_enable: The rewrite_url_enable of this RedirectPoolsExtendConfig.
        :type rewrite_url_enable: bool
        """
        self._rewrite_url_enable = rewrite_url_enable

    @property
    def rewrite_url_config(self):
        r"""Gets the rewrite_url_config of this RedirectPoolsExtendConfig.

        :return: The rewrite_url_config of this RedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.RewriteUrlConfig`
        """
        return self._rewrite_url_config

    @rewrite_url_config.setter
    def rewrite_url_config(self, rewrite_url_config):
        r"""Sets the rewrite_url_config of this RedirectPoolsExtendConfig.

        :param rewrite_url_config: The rewrite_url_config of this RedirectPoolsExtendConfig.
        :type rewrite_url_config: :class:`huaweicloudsdkelb.v3.RewriteUrlConfig`
        """
        self._rewrite_url_config = rewrite_url_config

    @property
    def insert_headers_config(self):
        r"""Gets the insert_headers_config of this RedirectPoolsExtendConfig.

        :return: The insert_headers_config of this RedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.InsertHeadersConfig`
        """
        return self._insert_headers_config

    @insert_headers_config.setter
    def insert_headers_config(self, insert_headers_config):
        r"""Sets the insert_headers_config of this RedirectPoolsExtendConfig.

        :param insert_headers_config: The insert_headers_config of this RedirectPoolsExtendConfig.
        :type insert_headers_config: :class:`huaweicloudsdkelb.v3.InsertHeadersConfig`
        """
        self._insert_headers_config = insert_headers_config

    @property
    def remove_headers_config(self):
        r"""Gets the remove_headers_config of this RedirectPoolsExtendConfig.

        :return: The remove_headers_config of this RedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.RemoveHeadersConfig`
        """
        return self._remove_headers_config

    @remove_headers_config.setter
    def remove_headers_config(self, remove_headers_config):
        r"""Sets the remove_headers_config of this RedirectPoolsExtendConfig.

        :param remove_headers_config: The remove_headers_config of this RedirectPoolsExtendConfig.
        :type remove_headers_config: :class:`huaweicloudsdkelb.v3.RemoveHeadersConfig`
        """
        self._remove_headers_config = remove_headers_config

    @property
    def traffic_limit_config(self):
        r"""Gets the traffic_limit_config of this RedirectPoolsExtendConfig.

        :return: The traffic_limit_config of this RedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.TrafficLimitConfig`
        """
        return self._traffic_limit_config

    @traffic_limit_config.setter
    def traffic_limit_config(self, traffic_limit_config):
        r"""Sets the traffic_limit_config of this RedirectPoolsExtendConfig.

        :param traffic_limit_config: The traffic_limit_config of this RedirectPoolsExtendConfig.
        :type traffic_limit_config: :class:`huaweicloudsdkelb.v3.TrafficLimitConfig`
        """
        self._traffic_limit_config = traffic_limit_config

    @property
    def cors_config(self):
        r"""Gets the cors_config of this RedirectPoolsExtendConfig.

        :return: The cors_config of this RedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.CorsConfig`
        """
        return self._cors_config

    @cors_config.setter
    def cors_config(self, cors_config):
        r"""Sets the cors_config of this RedirectPoolsExtendConfig.

        :param cors_config: The cors_config of this RedirectPoolsExtendConfig.
        :type cors_config: :class:`huaweicloudsdkelb.v3.CorsConfig`
        """
        self._cors_config = cors_config

    @property
    def traffic_mirror_config(self):
        r"""Gets the traffic_mirror_config of this RedirectPoolsExtendConfig.

        :return: The traffic_mirror_config of this RedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.TrafficMirrorConfig`
        """
        return self._traffic_mirror_config

    @traffic_mirror_config.setter
    def traffic_mirror_config(self, traffic_mirror_config):
        r"""Sets the traffic_mirror_config of this RedirectPoolsExtendConfig.

        :param traffic_mirror_config: The traffic_mirror_config of this RedirectPoolsExtendConfig.
        :type traffic_mirror_config: :class:`huaweicloudsdkelb.v3.TrafficMirrorConfig`
        """
        self._traffic_mirror_config = traffic_mirror_config

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
        if not isinstance(other, RedirectPoolsExtendConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
