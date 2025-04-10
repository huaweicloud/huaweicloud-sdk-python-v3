# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLtsConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'instance_lts_configs': 'list[InstanceLogConfig]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'instance_lts_configs': 'instance_lts_configs'
    }

    def __init__(self, total_count=None, instance_lts_configs=None):
        r"""ListLtsConfigsResponse

        The model defined in huaweicloud sdk

        :param total_count: 实例总记录数。
        :type total_count: int
        :param instance_lts_configs: 实例-LTS日志配置信息列表。
        :type instance_lts_configs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceLogConfig`]
        """
        
        super(ListLtsConfigsResponse, self).__init__()

        self._total_count = None
        self._instance_lts_configs = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if instance_lts_configs is not None:
            self.instance_lts_configs = instance_lts_configs

    @property
    def total_count(self):
        r"""Gets the total_count of this ListLtsConfigsResponse.

        实例总记录数。

        :return: The total_count of this ListLtsConfigsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListLtsConfigsResponse.

        实例总记录数。

        :param total_count: The total_count of this ListLtsConfigsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def instance_lts_configs(self):
        r"""Gets the instance_lts_configs of this ListLtsConfigsResponse.

        实例-LTS日志配置信息列表。

        :return: The instance_lts_configs of this ListLtsConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceLogConfig`]
        """
        return self._instance_lts_configs

    @instance_lts_configs.setter
    def instance_lts_configs(self, instance_lts_configs):
        r"""Sets the instance_lts_configs of this ListLtsConfigsResponse.

        实例-LTS日志配置信息列表。

        :param instance_lts_configs: The instance_lts_configs of this ListLtsConfigsResponse.
        :type instance_lts_configs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceLogConfig`]
        """
        self._instance_lts_configs = instance_lts_configs

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
        if not isinstance(other, ListLtsConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
