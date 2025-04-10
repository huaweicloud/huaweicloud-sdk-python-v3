# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseEndpointConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_target_readonly': 'bool',
        'node_num': 'int'
    }

    attribute_map = {
        'is_target_readonly': 'is_target_readonly',
        'node_num': 'node_num'
    }

    def __init__(self, is_target_readonly=None, node_num=None):
        r"""BaseEndpointConfig

        The model defined in huaweicloud sdk

        :param is_target_readonly: 目标实例是否设置为为只读。 - MySQL迁移和灾备，且job_direction为up时设置有效。（灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true）。
        :type is_target_readonly: bool
        :param node_num: Redis集群到GeminiDB Redis迁移场景填写，连接源端Redis集群的子任务个数，输入值在1到16之间，且输入值不能大于源端Redis集群的分片个数，请根据源端Redis集群的规模合理选择。建议集群的每4个分片设置1个源端分片个数，即每1个子任务连接源端集群的4个分片。
        :type node_num: int
        """
        
        

        self._is_target_readonly = None
        self._node_num = None
        self.discriminator = None

        if is_target_readonly is not None:
            self.is_target_readonly = is_target_readonly
        if node_num is not None:
            self.node_num = node_num

    @property
    def is_target_readonly(self):
        r"""Gets the is_target_readonly of this BaseEndpointConfig.

        目标实例是否设置为为只读。 - MySQL迁移和灾备，且job_direction为up时设置有效。（灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true）。

        :return: The is_target_readonly of this BaseEndpointConfig.
        :rtype: bool
        """
        return self._is_target_readonly

    @is_target_readonly.setter
    def is_target_readonly(self, is_target_readonly):
        r"""Sets the is_target_readonly of this BaseEndpointConfig.

        目标实例是否设置为为只读。 - MySQL迁移和灾备，且job_direction为up时设置有效。（灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true）。

        :param is_target_readonly: The is_target_readonly of this BaseEndpointConfig.
        :type is_target_readonly: bool
        """
        self._is_target_readonly = is_target_readonly

    @property
    def node_num(self):
        r"""Gets the node_num of this BaseEndpointConfig.

        Redis集群到GeminiDB Redis迁移场景填写，连接源端Redis集群的子任务个数，输入值在1到16之间，且输入值不能大于源端Redis集群的分片个数，请根据源端Redis集群的规模合理选择。建议集群的每4个分片设置1个源端分片个数，即每1个子任务连接源端集群的4个分片。

        :return: The node_num of this BaseEndpointConfig.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this BaseEndpointConfig.

        Redis集群到GeminiDB Redis迁移场景填写，连接源端Redis集群的子任务个数，输入值在1到16之间，且输入值不能大于源端Redis集群的分片个数，请根据源端Redis集群的规模合理选择。建议集群的每4个分片设置1个源端分片个数，即每1个子任务连接源端集群的4个分片。

        :param node_num: The node_num of this BaseEndpointConfig.
        :type node_num: int
        """
        self._node_num = node_num

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
        if not isinstance(other, BaseEndpointConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
