# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportInstanceListNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'engine_group': 'str',
        'instance_status': 'str',
        'order_value': 'str',
        'metric_names': 'list[str]'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'engine_group': 'engine_group',
        'instance_status': 'instance_status',
        'order_value': 'order_value',
        'metric_names': 'metric_names'
    }

    def __init__(self, engine_type=None, engine_group=None, instance_status=None, order_value=None, metric_names=None):
        r"""ExportInstanceListNewRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param engine_group: 数据库引擎类型
        :type engine_group: str
        :param instance_status: 实例状态，取值范围：normal（正常）、abnormal（异常）、metricAbnormal（指标异常）、dataDiskFull（磁盘不足）、all（所有）
        :type instance_status: str
        :param order_value: 排序条件
        :type order_value: str
        :param metric_names: 指标名称
        :type metric_names: list[str]
        """
        
        

        self._engine_type = None
        self._engine_group = None
        self._instance_status = None
        self._order_value = None
        self._metric_names = None
        self.discriminator = None

        self.engine_type = engine_type
        self.engine_group = engine_group
        self.instance_status = instance_status
        if order_value is not None:
            self.order_value = order_value
        if metric_names is not None:
            self.metric_names = metric_names

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ExportInstanceListNewRequestBody.

        数据库引擎类型

        :return: The engine_type of this ExportInstanceListNewRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ExportInstanceListNewRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this ExportInstanceListNewRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def engine_group(self):
        r"""Gets the engine_group of this ExportInstanceListNewRequestBody.

        数据库引擎类型

        :return: The engine_group of this ExportInstanceListNewRequestBody.
        :rtype: str
        """
        return self._engine_group

    @engine_group.setter
    def engine_group(self, engine_group):
        r"""Sets the engine_group of this ExportInstanceListNewRequestBody.

        数据库引擎类型

        :param engine_group: The engine_group of this ExportInstanceListNewRequestBody.
        :type engine_group: str
        """
        self._engine_group = engine_group

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ExportInstanceListNewRequestBody.

        实例状态，取值范围：normal（正常）、abnormal（异常）、metricAbnormal（指标异常）、dataDiskFull（磁盘不足）、all（所有）

        :return: The instance_status of this ExportInstanceListNewRequestBody.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ExportInstanceListNewRequestBody.

        实例状态，取值范围：normal（正常）、abnormal（异常）、metricAbnormal（指标异常）、dataDiskFull（磁盘不足）、all（所有）

        :param instance_status: The instance_status of this ExportInstanceListNewRequestBody.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def order_value(self):
        r"""Gets the order_value of this ExportInstanceListNewRequestBody.

        排序条件

        :return: The order_value of this ExportInstanceListNewRequestBody.
        :rtype: str
        """
        return self._order_value

    @order_value.setter
    def order_value(self, order_value):
        r"""Sets the order_value of this ExportInstanceListNewRequestBody.

        排序条件

        :param order_value: The order_value of this ExportInstanceListNewRequestBody.
        :type order_value: str
        """
        self._order_value = order_value

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ExportInstanceListNewRequestBody.

        指标名称

        :return: The metric_names of this ExportInstanceListNewRequestBody.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ExportInstanceListNewRequestBody.

        指标名称

        :param metric_names: The metric_names of this ExportInstanceListNewRequestBody.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

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
        if not isinstance(other, ExportInstanceListNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
