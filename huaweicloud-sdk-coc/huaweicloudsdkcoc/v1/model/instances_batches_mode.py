# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstancesBatchesMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_strategy': 'str',
        'target_instances': 'list[ResourceInstance]'
    }

    attribute_map = {
        'batch_strategy': 'batch_strategy',
        'target_instances': 'target_instances'
    }

    def __init__(self, batch_strategy=None, target_instances=None):
        r"""InstancesBatchesMode

        The model defined in huaweicloud sdk

        :param batch_strategy: 分批策略：只支持自动分批
        :type batch_strategy: str
        :param target_instances: 目标主机实例
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.ResourceInstance`]
        """
        
        

        self._batch_strategy = None
        self._target_instances = None
        self.discriminator = None

        self.batch_strategy = batch_strategy
        self.target_instances = target_instances

    @property
    def batch_strategy(self):
        r"""Gets the batch_strategy of this InstancesBatchesMode.

        分批策略：只支持自动分批

        :return: The batch_strategy of this InstancesBatchesMode.
        :rtype: str
        """
        return self._batch_strategy

    @batch_strategy.setter
    def batch_strategy(self, batch_strategy):
        r"""Sets the batch_strategy of this InstancesBatchesMode.

        分批策略：只支持自动分批

        :param batch_strategy: The batch_strategy of this InstancesBatchesMode.
        :type batch_strategy: str
        """
        self._batch_strategy = batch_strategy

    @property
    def target_instances(self):
        r"""Gets the target_instances of this InstancesBatchesMode.

        目标主机实例

        :return: The target_instances of this InstancesBatchesMode.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ResourceInstance`]
        """
        return self._target_instances

    @target_instances.setter
    def target_instances(self, target_instances):
        r"""Sets the target_instances of this InstancesBatchesMode.

        目标主机实例

        :param target_instances: The target_instances of this InstancesBatchesMode.
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.ResourceInstance`]
        """
        self._target_instances = target_instances

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
        if not isinstance(other, InstancesBatchesMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
