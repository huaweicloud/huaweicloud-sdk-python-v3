# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceRecycleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'status': 'str',
        'name': 'str',
        'engine': 'str',
        'in_recycle_time': 'int',
        'save_time': 'int',
        'auto_delete_time': 'int',
        'cost_per_hour': 'float',
        'error_message': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'status': 'status',
        'name': 'name',
        'engine': 'engine',
        'in_recycle_time': 'in_recycle_time',
        'save_time': 'save_time',
        'auto_delete_time': 'auto_delete_time',
        'cost_per_hour': 'cost_per_hour',
        'error_message': 'error_message',
        'product_id': 'product_id'
    }

    def __init__(self, instance_id=None, status=None, name=None, engine=None, in_recycle_time=None, save_time=None, auto_delete_time=None, cost_per_hour=None, error_message=None, product_id=None):
        r"""InstanceRecycleInfo

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param status: **参数解释**： 实例状态。  **取值范围**： 详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)。
        :type status: str
        :param name: **参数解释**： 实例名称。  **取值范围**： 不涉及。
        :type name: str
        :param engine: **参数解释**： 引擎。  **取值范围**： kafka。
        :type engine: str
        :param in_recycle_time: **参数解释**： 回收时间。  **取值范围**： 不涉及。
        :type in_recycle_time: int
        :param save_time: **参数解释**： 保留时间。  **取值范围**： 1~7天。
        :type save_time: int
        :param auto_delete_time: **参数解释**： 自动删除时间。  **取值范围**： 不涉及。
        :type auto_delete_time: int
        :param cost_per_hour: **参数解释**： 每小时的费用。  **取值范围**： 不涉及。
        :type cost_per_hour: float
        :param error_message: **参数解释**： 错误信息。  **取值范围**： 不涉及。
        :type error_message: str
        :param product_id: **参数解释**： 产品ID。 **取值范围**： 不涉及。
        :type product_id: str
        """
        
        

        self._instance_id = None
        self._status = None
        self._name = None
        self._engine = None
        self._in_recycle_time = None
        self._save_time = None
        self._auto_delete_time = None
        self._cost_per_hour = None
        self._error_message = None
        self._product_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if engine is not None:
            self.engine = engine
        if in_recycle_time is not None:
            self.in_recycle_time = in_recycle_time
        if save_time is not None:
            self.save_time = save_time
        if auto_delete_time is not None:
            self.auto_delete_time = auto_delete_time
        if cost_per_hour is not None:
            self.cost_per_hour = cost_per_hour
        if error_message is not None:
            self.error_message = error_message
        if product_id is not None:
            self.product_id = product_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceRecycleInfo.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this InstanceRecycleInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceRecycleInfo.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this InstanceRecycleInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this InstanceRecycleInfo.

        **参数解释**： 实例状态。  **取值范围**： 详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)。

        :return: The status of this InstanceRecycleInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceRecycleInfo.

        **参数解释**： 实例状态。  **取值范围**： 详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)。

        :param status: The status of this InstanceRecycleInfo.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this InstanceRecycleInfo.

        **参数解释**： 实例名称。  **取值范围**： 不涉及。

        :return: The name of this InstanceRecycleInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceRecycleInfo.

        **参数解释**： 实例名称。  **取值范围**： 不涉及。

        :param name: The name of this InstanceRecycleInfo.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        r"""Gets the engine of this InstanceRecycleInfo.

        **参数解释**： 引擎。  **取值范围**： kafka。

        :return: The engine of this InstanceRecycleInfo.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this InstanceRecycleInfo.

        **参数解释**： 引擎。  **取值范围**： kafka。

        :param engine: The engine of this InstanceRecycleInfo.
        :type engine: str
        """
        self._engine = engine

    @property
    def in_recycle_time(self):
        r"""Gets the in_recycle_time of this InstanceRecycleInfo.

        **参数解释**： 回收时间。  **取值范围**： 不涉及。

        :return: The in_recycle_time of this InstanceRecycleInfo.
        :rtype: int
        """
        return self._in_recycle_time

    @in_recycle_time.setter
    def in_recycle_time(self, in_recycle_time):
        r"""Sets the in_recycle_time of this InstanceRecycleInfo.

        **参数解释**： 回收时间。  **取值范围**： 不涉及。

        :param in_recycle_time: The in_recycle_time of this InstanceRecycleInfo.
        :type in_recycle_time: int
        """
        self._in_recycle_time = in_recycle_time

    @property
    def save_time(self):
        r"""Gets the save_time of this InstanceRecycleInfo.

        **参数解释**： 保留时间。  **取值范围**： 1~7天。

        :return: The save_time of this InstanceRecycleInfo.
        :rtype: int
        """
        return self._save_time

    @save_time.setter
    def save_time(self, save_time):
        r"""Sets the save_time of this InstanceRecycleInfo.

        **参数解释**： 保留时间。  **取值范围**： 1~7天。

        :param save_time: The save_time of this InstanceRecycleInfo.
        :type save_time: int
        """
        self._save_time = save_time

    @property
    def auto_delete_time(self):
        r"""Gets the auto_delete_time of this InstanceRecycleInfo.

        **参数解释**： 自动删除时间。  **取值范围**： 不涉及。

        :return: The auto_delete_time of this InstanceRecycleInfo.
        :rtype: int
        """
        return self._auto_delete_time

    @auto_delete_time.setter
    def auto_delete_time(self, auto_delete_time):
        r"""Sets the auto_delete_time of this InstanceRecycleInfo.

        **参数解释**： 自动删除时间。  **取值范围**： 不涉及。

        :param auto_delete_time: The auto_delete_time of this InstanceRecycleInfo.
        :type auto_delete_time: int
        """
        self._auto_delete_time = auto_delete_time

    @property
    def cost_per_hour(self):
        r"""Gets the cost_per_hour of this InstanceRecycleInfo.

        **参数解释**： 每小时的费用。  **取值范围**： 不涉及。

        :return: The cost_per_hour of this InstanceRecycleInfo.
        :rtype: float
        """
        return self._cost_per_hour

    @cost_per_hour.setter
    def cost_per_hour(self, cost_per_hour):
        r"""Sets the cost_per_hour of this InstanceRecycleInfo.

        **参数解释**： 每小时的费用。  **取值范围**： 不涉及。

        :param cost_per_hour: The cost_per_hour of this InstanceRecycleInfo.
        :type cost_per_hour: float
        """
        self._cost_per_hour = cost_per_hour

    @property
    def error_message(self):
        r"""Gets the error_message of this InstanceRecycleInfo.

        **参数解释**： 错误信息。  **取值范围**： 不涉及。

        :return: The error_message of this InstanceRecycleInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this InstanceRecycleInfo.

        **参数解释**： 错误信息。  **取值范围**： 不涉及。

        :param error_message: The error_message of this InstanceRecycleInfo.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def product_id(self):
        r"""Gets the product_id of this InstanceRecycleInfo.

        **参数解释**： 产品ID。 **取值范围**： 不涉及。

        :return: The product_id of this InstanceRecycleInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this InstanceRecycleInfo.

        **参数解释**： 产品ID。 **取值范围**： 不涉及。

        :param product_id: The product_id of this InstanceRecycleInfo.
        :type product_id: str
        """
        self._product_id = product_id

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
        if not isinstance(other, InstanceRecycleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
