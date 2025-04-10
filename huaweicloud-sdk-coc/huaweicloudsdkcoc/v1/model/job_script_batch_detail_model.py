# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScriptBatchDetailModel:

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
        'execute_instances': 'list[ExectionInstanceModel]'
    }

    attribute_map = {
        'batch_index': 'batch_index',
        'total_instances': 'total_instances',
        'execute_instances': 'execute_instances'
    }

    def __init__(self, batch_index=None, total_instances=None, execute_instances=None):
        r"""JobScriptBatchDetailModel

        The model defined in huaweicloud sdk

        :param batch_index: 批次索引，从1开始
        :type batch_index: int
        :param total_instances: 批次内执行实例数量
        :type total_instances: int
        :param execute_instances: 执行实例列表，分页
        :type execute_instances: list[:class:`huaweicloudsdkcoc.v1.ExectionInstanceModel`]
        """
        
        

        self._batch_index = None
        self._total_instances = None
        self._execute_instances = None
        self.discriminator = None

        if batch_index is not None:
            self.batch_index = batch_index
        if total_instances is not None:
            self.total_instances = total_instances
        if execute_instances is not None:
            self.execute_instances = execute_instances

    @property
    def batch_index(self):
        r"""Gets the batch_index of this JobScriptBatchDetailModel.

        批次索引，从1开始

        :return: The batch_index of this JobScriptBatchDetailModel.
        :rtype: int
        """
        return self._batch_index

    @batch_index.setter
    def batch_index(self, batch_index):
        r"""Sets the batch_index of this JobScriptBatchDetailModel.

        批次索引，从1开始

        :param batch_index: The batch_index of this JobScriptBatchDetailModel.
        :type batch_index: int
        """
        self._batch_index = batch_index

    @property
    def total_instances(self):
        r"""Gets the total_instances of this JobScriptBatchDetailModel.

        批次内执行实例数量

        :return: The total_instances of this JobScriptBatchDetailModel.
        :rtype: int
        """
        return self._total_instances

    @total_instances.setter
    def total_instances(self, total_instances):
        r"""Sets the total_instances of this JobScriptBatchDetailModel.

        批次内执行实例数量

        :param total_instances: The total_instances of this JobScriptBatchDetailModel.
        :type total_instances: int
        """
        self._total_instances = total_instances

    @property
    def execute_instances(self):
        r"""Gets the execute_instances of this JobScriptBatchDetailModel.

        执行实例列表，分页

        :return: The execute_instances of this JobScriptBatchDetailModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExectionInstanceModel`]
        """
        return self._execute_instances

    @execute_instances.setter
    def execute_instances(self, execute_instances):
        r"""Sets the execute_instances of this JobScriptBatchDetailModel.

        执行实例列表，分页

        :param execute_instances: The execute_instances of this JobScriptBatchDetailModel.
        :type execute_instances: list[:class:`huaweicloudsdkcoc.v1.ExectionInstanceModel`]
        """
        self._execute_instances = execute_instances

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
        if not isinstance(other, JobScriptBatchDetailModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
