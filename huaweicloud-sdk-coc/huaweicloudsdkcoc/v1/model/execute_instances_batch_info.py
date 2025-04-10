# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteInstancesBatchInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_index': 'int',
        'target_instances': 'list[ExecuteResourceInstance]',
        'rotation_strategy': 'str'
    }

    attribute_map = {
        'batch_index': 'batch_index',
        'target_instances': 'target_instances',
        'rotation_strategy': 'rotation_strategy'
    }

    def __init__(self, batch_index=None, target_instances=None, rotation_strategy=None):
        r"""ExecuteInstancesBatchInfo

        The model defined in huaweicloud sdk

        :param batch_index: 批次索引，从1开始，未校验：最大值
        :type batch_index: int
        :param target_instances: 目标节点列表
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.ExecuteResourceInstance`]
        :param rotation_strategy: 暂停继续策略
        :type rotation_strategy: str
        """
        
        

        self._batch_index = None
        self._target_instances = None
        self._rotation_strategy = None
        self.discriminator = None

        self.batch_index = batch_index
        self.target_instances = target_instances
        self.rotation_strategy = rotation_strategy

    @property
    def batch_index(self):
        r"""Gets the batch_index of this ExecuteInstancesBatchInfo.

        批次索引，从1开始，未校验：最大值

        :return: The batch_index of this ExecuteInstancesBatchInfo.
        :rtype: int
        """
        return self._batch_index

    @batch_index.setter
    def batch_index(self, batch_index):
        r"""Sets the batch_index of this ExecuteInstancesBatchInfo.

        批次索引，从1开始，未校验：最大值

        :param batch_index: The batch_index of this ExecuteInstancesBatchInfo.
        :type batch_index: int
        """
        self._batch_index = batch_index

    @property
    def target_instances(self):
        r"""Gets the target_instances of this ExecuteInstancesBatchInfo.

        目标节点列表

        :return: The target_instances of this ExecuteInstancesBatchInfo.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExecuteResourceInstance`]
        """
        return self._target_instances

    @target_instances.setter
    def target_instances(self, target_instances):
        r"""Sets the target_instances of this ExecuteInstancesBatchInfo.

        目标节点列表

        :param target_instances: The target_instances of this ExecuteInstancesBatchInfo.
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.ExecuteResourceInstance`]
        """
        self._target_instances = target_instances

    @property
    def rotation_strategy(self):
        r"""Gets the rotation_strategy of this ExecuteInstancesBatchInfo.

        暂停继续策略

        :return: The rotation_strategy of this ExecuteInstancesBatchInfo.
        :rtype: str
        """
        return self._rotation_strategy

    @rotation_strategy.setter
    def rotation_strategy(self, rotation_strategy):
        r"""Sets the rotation_strategy of this ExecuteInstancesBatchInfo.

        暂停继续策略

        :param rotation_strategy: The rotation_strategy of this ExecuteInstancesBatchInfo.
        :type rotation_strategy: str
        """
        self._rotation_strategy = rotation_strategy

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
        if not isinstance(other, ExecuteInstancesBatchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
