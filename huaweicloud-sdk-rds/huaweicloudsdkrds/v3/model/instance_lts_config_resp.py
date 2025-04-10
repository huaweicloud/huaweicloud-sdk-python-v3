# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceLtsConfigResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lts_configs': 'list[InstanceLtsConfigDetailResp]',
        'instance': 'InstanceLtsBasicInfoResp'
    }

    attribute_map = {
        'lts_configs': 'lts_configs',
        'instance': 'instance'
    }

    def __init__(self, lts_configs=None, instance=None):
        r"""InstanceLtsConfigResp

        The model defined in huaweicloud sdk

        :param lts_configs: LTS配置信息
        :type lts_configs: list[:class:`huaweicloudsdkrds.v3.InstanceLtsConfigDetailResp`]
        :param instance: 
        :type instance: :class:`huaweicloudsdkrds.v3.InstanceLtsBasicInfoResp`
        """
        
        

        self._lts_configs = None
        self._instance = None
        self.discriminator = None

        if lts_configs is not None:
            self.lts_configs = lts_configs
        if instance is not None:
            self.instance = instance

    @property
    def lts_configs(self):
        r"""Gets the lts_configs of this InstanceLtsConfigResp.

        LTS配置信息

        :return: The lts_configs of this InstanceLtsConfigResp.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InstanceLtsConfigDetailResp`]
        """
        return self._lts_configs

    @lts_configs.setter
    def lts_configs(self, lts_configs):
        r"""Sets the lts_configs of this InstanceLtsConfigResp.

        LTS配置信息

        :param lts_configs: The lts_configs of this InstanceLtsConfigResp.
        :type lts_configs: list[:class:`huaweicloudsdkrds.v3.InstanceLtsConfigDetailResp`]
        """
        self._lts_configs = lts_configs

    @property
    def instance(self):
        r"""Gets the instance of this InstanceLtsConfigResp.

        :return: The instance of this InstanceLtsConfigResp.
        :rtype: :class:`huaweicloudsdkrds.v3.InstanceLtsBasicInfoResp`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this InstanceLtsConfigResp.

        :param instance: The instance of this InstanceLtsConfigResp.
        :type instance: :class:`huaweicloudsdkrds.v3.InstanceLtsBasicInfoResp`
        """
        self._instance = instance

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
        if not isinstance(other, InstanceLtsConfigResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
