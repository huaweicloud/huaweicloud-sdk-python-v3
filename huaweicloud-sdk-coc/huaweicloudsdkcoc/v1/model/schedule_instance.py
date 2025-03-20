# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_selection': 'str',
        'target_resource': 'TargetResource',
        'target_instances': 'str',
        'order_no': 'int',
        'batch_strategy': 'str',
        'sub_target_instances': 'list[ScheduleInstance]'
    }

    attribute_map = {
        'target_selection': 'target_selection',
        'target_resource': 'target_resource',
        'target_instances': 'target_instances',
        'order_no': 'order_no',
        'batch_strategy': 'batch_strategy',
        'sub_target_instances': 'sub_target_instances'
    }

    def __init__(self, target_selection=None, target_resource=None, target_instances=None, order_no=None, batch_strategy=None, sub_target_instances=None):
        """ScheduleInstance

        The model defined in huaweicloud sdk

        :param target_selection: 目标选择方式，枚举值：ALL 全部实例，MANUAL 手动选择, NONE
        :type target_selection: str
        :param target_resource: 
        :type target_resource: :class:`huaweicloudsdkcoc.v1.TargetResource`
        :param target_instances: 实例信息
        :type target_instances: str
        :param order_no: 步骤号
        :type order_no: int
        :param batch_strategy: 实例分批策略(AUTO_BATCH,MANUAL_BATCH,NONE)
        :type batch_strategy: str
        :param sub_target_instances: 目标实例
        :type sub_target_instances: list[:class:`huaweicloudsdkcoc.v1.ScheduleInstance`]
        """
        
        

        self._target_selection = None
        self._target_resource = None
        self._target_instances = None
        self._order_no = None
        self._batch_strategy = None
        self._sub_target_instances = None
        self.discriminator = None

        self.target_selection = target_selection
        if target_resource is not None:
            self.target_resource = target_resource
        if target_instances is not None:
            self.target_instances = target_instances
        self.order_no = order_no
        if batch_strategy is not None:
            self.batch_strategy = batch_strategy
        if sub_target_instances is not None:
            self.sub_target_instances = sub_target_instances

    @property
    def target_selection(self):
        """Gets the target_selection of this ScheduleInstance.

        目标选择方式，枚举值：ALL 全部实例，MANUAL 手动选择, NONE

        :return: The target_selection of this ScheduleInstance.
        :rtype: str
        """
        return self._target_selection

    @target_selection.setter
    def target_selection(self, target_selection):
        """Sets the target_selection of this ScheduleInstance.

        目标选择方式，枚举值：ALL 全部实例，MANUAL 手动选择, NONE

        :param target_selection: The target_selection of this ScheduleInstance.
        :type target_selection: str
        """
        self._target_selection = target_selection

    @property
    def target_resource(self):
        """Gets the target_resource of this ScheduleInstance.

        :return: The target_resource of this ScheduleInstance.
        :rtype: :class:`huaweicloudsdkcoc.v1.TargetResource`
        """
        return self._target_resource

    @target_resource.setter
    def target_resource(self, target_resource):
        """Sets the target_resource of this ScheduleInstance.

        :param target_resource: The target_resource of this ScheduleInstance.
        :type target_resource: :class:`huaweicloudsdkcoc.v1.TargetResource`
        """
        self._target_resource = target_resource

    @property
    def target_instances(self):
        """Gets the target_instances of this ScheduleInstance.

        实例信息

        :return: The target_instances of this ScheduleInstance.
        :rtype: str
        """
        return self._target_instances

    @target_instances.setter
    def target_instances(self, target_instances):
        """Sets the target_instances of this ScheduleInstance.

        实例信息

        :param target_instances: The target_instances of this ScheduleInstance.
        :type target_instances: str
        """
        self._target_instances = target_instances

    @property
    def order_no(self):
        """Gets the order_no of this ScheduleInstance.

        步骤号

        :return: The order_no of this ScheduleInstance.
        :rtype: int
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this ScheduleInstance.

        步骤号

        :param order_no: The order_no of this ScheduleInstance.
        :type order_no: int
        """
        self._order_no = order_no

    @property
    def batch_strategy(self):
        """Gets the batch_strategy of this ScheduleInstance.

        实例分批策略(AUTO_BATCH,MANUAL_BATCH,NONE)

        :return: The batch_strategy of this ScheduleInstance.
        :rtype: str
        """
        return self._batch_strategy

    @batch_strategy.setter
    def batch_strategy(self, batch_strategy):
        """Sets the batch_strategy of this ScheduleInstance.

        实例分批策略(AUTO_BATCH,MANUAL_BATCH,NONE)

        :param batch_strategy: The batch_strategy of this ScheduleInstance.
        :type batch_strategy: str
        """
        self._batch_strategy = batch_strategy

    @property
    def sub_target_instances(self):
        """Gets the sub_target_instances of this ScheduleInstance.

        目标实例

        :return: The sub_target_instances of this ScheduleInstance.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScheduleInstance`]
        """
        return self._sub_target_instances

    @sub_target_instances.setter
    def sub_target_instances(self, sub_target_instances):
        """Sets the sub_target_instances of this ScheduleInstance.

        目标实例

        :param sub_target_instances: The sub_target_instances of this ScheduleInstance.
        :type sub_target_instances: list[:class:`huaweicloudsdkcoc.v1.ScheduleInstance`]
        """
        self._sub_target_instances = sub_target_instances

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
        if not isinstance(other, ScheduleInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
