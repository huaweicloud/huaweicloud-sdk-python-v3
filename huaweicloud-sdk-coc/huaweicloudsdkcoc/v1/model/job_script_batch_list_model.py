# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScriptBatchListModel:

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
        'total_instances': 'int',
        'rotation_strategy': 'str',
        'properties': 'str'
    }

    attribute_map = {
        'batch_index': 'batch_index',
        'total_instances': 'total_instances',
        'rotation_strategy': 'rotation_strategy',
        'properties': 'properties'
    }

    def __init__(self, batch_index=None, total_instances=None, rotation_strategy=None, properties=None):
        r"""JobScriptBatchListModel

        The model defined in huaweicloud sdk

        :param batch_index: 批次索引，从1开始
        :type batch_index: int
        :param total_instances: 批次内实例节点数量
        :type total_instances: int
        :param rotation_strategy: 暂停继续策略
        :type rotation_strategy: str
        :param properties: 批次标签：
        :type properties: str
        """
        
        

        self._batch_index = None
        self._total_instances = None
        self._rotation_strategy = None
        self._properties = None
        self.discriminator = None

        if batch_index is not None:
            self.batch_index = batch_index
        if total_instances is not None:
            self.total_instances = total_instances
        if rotation_strategy is not None:
            self.rotation_strategy = rotation_strategy
        if properties is not None:
            self.properties = properties

    @property
    def batch_index(self):
        r"""Gets the batch_index of this JobScriptBatchListModel.

        批次索引，从1开始

        :return: The batch_index of this JobScriptBatchListModel.
        :rtype: int
        """
        return self._batch_index

    @batch_index.setter
    def batch_index(self, batch_index):
        r"""Sets the batch_index of this JobScriptBatchListModel.

        批次索引，从1开始

        :param batch_index: The batch_index of this JobScriptBatchListModel.
        :type batch_index: int
        """
        self._batch_index = batch_index

    @property
    def total_instances(self):
        r"""Gets the total_instances of this JobScriptBatchListModel.

        批次内实例节点数量

        :return: The total_instances of this JobScriptBatchListModel.
        :rtype: int
        """
        return self._total_instances

    @total_instances.setter
    def total_instances(self, total_instances):
        r"""Sets the total_instances of this JobScriptBatchListModel.

        批次内实例节点数量

        :param total_instances: The total_instances of this JobScriptBatchListModel.
        :type total_instances: int
        """
        self._total_instances = total_instances

    @property
    def rotation_strategy(self):
        r"""Gets the rotation_strategy of this JobScriptBatchListModel.

        暂停继续策略

        :return: The rotation_strategy of this JobScriptBatchListModel.
        :rtype: str
        """
        return self._rotation_strategy

    @rotation_strategy.setter
    def rotation_strategy(self, rotation_strategy):
        r"""Sets the rotation_strategy of this JobScriptBatchListModel.

        暂停继续策略

        :param rotation_strategy: The rotation_strategy of this JobScriptBatchListModel.
        :type rotation_strategy: str
        """
        self._rotation_strategy = rotation_strategy

    @property
    def properties(self):
        r"""Gets the properties of this JobScriptBatchListModel.

        批次标签：

        :return: The properties of this JobScriptBatchListModel.
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this JobScriptBatchListModel.

        批次标签：

        :param properties: The properties of this JobScriptBatchListModel.
        :type properties: str
        """
        self._properties = properties

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
        if not isinstance(other, JobScriptBatchListModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
