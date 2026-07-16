# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeconfigSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'object'
    }

    attribute_map = {
        'configs': 'configs'
    }

    def __init__(self, configs=None):
        r"""NodeconfigSpec

        The model defined in huaweicloud sdk

        :param configs: **参数解释**： 节点自定义配置；当前支持节点绑核、是否启用缓存清理、是否启用透明大页。 \&quot;configs\&quot;: {    \&quot;cpu_manager\&quot;: {     \&quot;mode\&quot;: \&quot;static/none\&quot; //static为启用绑核, none为不启用绑核    },    \&quot;drop_cache\&quot;: {     \&quot;mode\&quot;: \&quot;enable/disable\&quot; // enable启用缓存清理    },    \&quot;transparent_hugepage\&quot;: {     \&quot;mode\&quot;: \&quot;always/madvise/never\&quot; // always为启用透明大页，never为关闭透明大页，madvice交给系统选择。    } }
        :type configs: object
        """
        
        

        self._configs = None
        self.discriminator = None

        self.configs = configs

    @property
    def configs(self):
        r"""Gets the configs of this NodeconfigSpec.

        **参数解释**： 节点自定义配置；当前支持节点绑核、是否启用缓存清理、是否启用透明大页。 \"configs\": {    \"cpu_manager\": {     \"mode\": \"static/none\" //static为启用绑核, none为不启用绑核    },    \"drop_cache\": {     \"mode\": \"enable/disable\" // enable启用缓存清理    },    \"transparent_hugepage\": {     \"mode\": \"always/madvise/never\" // always为启用透明大页，never为关闭透明大页，madvice交给系统选择。    } }

        :return: The configs of this NodeconfigSpec.
        :rtype: object
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this NodeconfigSpec.

        **参数解释**： 节点自定义配置；当前支持节点绑核、是否启用缓存清理、是否启用透明大页。 \"configs\": {    \"cpu_manager\": {     \"mode\": \"static/none\" //static为启用绑核, none为不启用绑核    },    \"drop_cache\": {     \"mode\": \"enable/disable\" // enable启用缓存清理    },    \"transparent_hugepage\": {     \"mode\": \"always/madvise/never\" // always为启用透明大页，never为关闭透明大页，madvice交给系统选择。    } }

        :param configs: The configs of this NodeconfigSpec.
        :type configs: object
        """
        self._configs = configs

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeconfigSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
