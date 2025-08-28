# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRedirectPoolsExtendConfig:

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
        'rewrite_url_config': 'UpdateRewriteUrlConfig',
        'insert_headers_config': 'UpdateInsertHeadersConfig',
        'remove_headers_config': 'UpdateRemoveHeadersConfig',
        'traffic_limit_config': 'UpdateTrafficLimitConfig',
        'cors_config': 'CreateCorsConfig',
        'traffic_mirror_config': 'CreateTrafficMirrorConfig'
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
        r"""UpdateRedirectPoolsExtendConfig

        The model defined in huaweicloud sdk

        :param rewrite_url_enable: **参数解释**：是否开启url重定向。  **约束限制**：不涉及  **取值范围**：true 开启，false 未开启。  **默认取值**：不涉及
        :type rewrite_url_enable: bool
        :param rewrite_url_config: 
        :type rewrite_url_config: :class:`huaweicloudsdkelb.v3.UpdateRewriteUrlConfig`
        :param insert_headers_config: 
        :type insert_headers_config: :class:`huaweicloudsdkelb.v3.UpdateInsertHeadersConfig`
        :param remove_headers_config: 
        :type remove_headers_config: :class:`huaweicloudsdkelb.v3.UpdateRemoveHeadersConfig`
        :param traffic_limit_config: 
        :type traffic_limit_config: :class:`huaweicloudsdkelb.v3.UpdateTrafficLimitConfig`
        :param cors_config: 
        :type cors_config: :class:`huaweicloudsdkelb.v3.CreateCorsConfig`
        :param traffic_mirror_config: 
        :type traffic_mirror_config: :class:`huaweicloudsdkelb.v3.CreateTrafficMirrorConfig`
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
        r"""Gets the rewrite_url_enable of this UpdateRedirectPoolsExtendConfig.

        **参数解释**：是否开启url重定向。  **约束限制**：不涉及  **取值范围**：true 开启，false 未开启。  **默认取值**：不涉及

        :return: The rewrite_url_enable of this UpdateRedirectPoolsExtendConfig.
        :rtype: bool
        """
        return self._rewrite_url_enable

    @rewrite_url_enable.setter
    def rewrite_url_enable(self, rewrite_url_enable):
        r"""Sets the rewrite_url_enable of this UpdateRedirectPoolsExtendConfig.

        **参数解释**：是否开启url重定向。  **约束限制**：不涉及  **取值范围**：true 开启，false 未开启。  **默认取值**：不涉及

        :param rewrite_url_enable: The rewrite_url_enable of this UpdateRedirectPoolsExtendConfig.
        :type rewrite_url_enable: bool
        """
        self._rewrite_url_enable = rewrite_url_enable

    @property
    def rewrite_url_config(self):
        r"""Gets the rewrite_url_config of this UpdateRedirectPoolsExtendConfig.

        :return: The rewrite_url_config of this UpdateRedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateRewriteUrlConfig`
        """
        return self._rewrite_url_config

    @rewrite_url_config.setter
    def rewrite_url_config(self, rewrite_url_config):
        r"""Sets the rewrite_url_config of this UpdateRedirectPoolsExtendConfig.

        :param rewrite_url_config: The rewrite_url_config of this UpdateRedirectPoolsExtendConfig.
        :type rewrite_url_config: :class:`huaweicloudsdkelb.v3.UpdateRewriteUrlConfig`
        """
        self._rewrite_url_config = rewrite_url_config

    @property
    def insert_headers_config(self):
        r"""Gets the insert_headers_config of this UpdateRedirectPoolsExtendConfig.

        :return: The insert_headers_config of this UpdateRedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateInsertHeadersConfig`
        """
        return self._insert_headers_config

    @insert_headers_config.setter
    def insert_headers_config(self, insert_headers_config):
        r"""Sets the insert_headers_config of this UpdateRedirectPoolsExtendConfig.

        :param insert_headers_config: The insert_headers_config of this UpdateRedirectPoolsExtendConfig.
        :type insert_headers_config: :class:`huaweicloudsdkelb.v3.UpdateInsertHeadersConfig`
        """
        self._insert_headers_config = insert_headers_config

    @property
    def remove_headers_config(self):
        r"""Gets the remove_headers_config of this UpdateRedirectPoolsExtendConfig.

        :return: The remove_headers_config of this UpdateRedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateRemoveHeadersConfig`
        """
        return self._remove_headers_config

    @remove_headers_config.setter
    def remove_headers_config(self, remove_headers_config):
        r"""Sets the remove_headers_config of this UpdateRedirectPoolsExtendConfig.

        :param remove_headers_config: The remove_headers_config of this UpdateRedirectPoolsExtendConfig.
        :type remove_headers_config: :class:`huaweicloudsdkelb.v3.UpdateRemoveHeadersConfig`
        """
        self._remove_headers_config = remove_headers_config

    @property
    def traffic_limit_config(self):
        r"""Gets the traffic_limit_config of this UpdateRedirectPoolsExtendConfig.

        :return: The traffic_limit_config of this UpdateRedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateTrafficLimitConfig`
        """
        return self._traffic_limit_config

    @traffic_limit_config.setter
    def traffic_limit_config(self, traffic_limit_config):
        r"""Sets the traffic_limit_config of this UpdateRedirectPoolsExtendConfig.

        :param traffic_limit_config: The traffic_limit_config of this UpdateRedirectPoolsExtendConfig.
        :type traffic_limit_config: :class:`huaweicloudsdkelb.v3.UpdateTrafficLimitConfig`
        """
        self._traffic_limit_config = traffic_limit_config

    @property
    def cors_config(self):
        r"""Gets the cors_config of this UpdateRedirectPoolsExtendConfig.

        :return: The cors_config of this UpdateRedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateCorsConfig`
        """
        return self._cors_config

    @cors_config.setter
    def cors_config(self, cors_config):
        r"""Sets the cors_config of this UpdateRedirectPoolsExtendConfig.

        :param cors_config: The cors_config of this UpdateRedirectPoolsExtendConfig.
        :type cors_config: :class:`huaweicloudsdkelb.v3.CreateCorsConfig`
        """
        self._cors_config = cors_config

    @property
    def traffic_mirror_config(self):
        r"""Gets the traffic_mirror_config of this UpdateRedirectPoolsExtendConfig.

        :return: The traffic_mirror_config of this UpdateRedirectPoolsExtendConfig.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateTrafficMirrorConfig`
        """
        return self._traffic_mirror_config

    @traffic_mirror_config.setter
    def traffic_mirror_config(self, traffic_mirror_config):
        r"""Sets the traffic_mirror_config of this UpdateRedirectPoolsExtendConfig.

        :param traffic_mirror_config: The traffic_mirror_config of this UpdateRedirectPoolsExtendConfig.
        :type traffic_mirror_config: :class:`huaweicloudsdkelb.v3.CreateTrafficMirrorConfig`
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
        if not isinstance(other, UpdateRedirectPoolsExtendConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
