# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'life_cycle_state': 'str',
        'health_status': 'str',
        'protect_from_scaling_down': 'str',
        'start_number': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'life_cycle_state': 'life_cycle_state',
        'health_status': 'health_status',
        'protect_from_scaling_down': 'protect_from_scaling_down',
        'start_number': 'start_number',
        'limit': 'limit'
    }

    def __init__(self, scaling_group_id=None, life_cycle_state=None, health_status=None, protect_from_scaling_down=None, start_number=None, limit=None):
        r"""ListScalingInstancesRequest

        The model defined in huaweicloud sdk

        :param scaling_group_id: 伸缩组ID。
        :type scaling_group_id: str
        :param life_cycle_state: 实例在伸缩组中的生命周期状态：INSERVICE： 正在使用。PENDING：正在加入伸缩组。REMOVING：正在移出伸缩组。PENDING_WAIT：正在加入伸缩组：等待。REMOVING_WAIT：正在移出伸缩组：等待。
        :type life_cycle_state: str
        :param health_status: 实例健康状态：INITIALIZING：初始化。NORMAL：正常。ERROR：异常
        :type health_status: str
        :param protect_from_scaling_down: 实例保护状态：true：已设置实例保护。false：未设置实例保护。
        :type protect_from_scaling_down: str
        :param start_number: 查询的起始行号，默认为0。
        :type start_number: int
        :param limit: 查询的记录条数，默认为20。
        :type limit: int
        """
        
        

        self._scaling_group_id = None
        self._life_cycle_state = None
        self._health_status = None
        self._protect_from_scaling_down = None
        self._start_number = None
        self._limit = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if life_cycle_state is not None:
            self.life_cycle_state = life_cycle_state
        if health_status is not None:
            self.health_status = health_status
        if protect_from_scaling_down is not None:
            self.protect_from_scaling_down = protect_from_scaling_down
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit

    @property
    def scaling_group_id(self):
        r"""Gets the scaling_group_id of this ListScalingInstancesRequest.

        伸缩组ID。

        :return: The scaling_group_id of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        r"""Sets the scaling_group_id of this ListScalingInstancesRequest.

        伸缩组ID。

        :param scaling_group_id: The scaling_group_id of this ListScalingInstancesRequest.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def life_cycle_state(self):
        r"""Gets the life_cycle_state of this ListScalingInstancesRequest.

        实例在伸缩组中的生命周期状态：INSERVICE： 正在使用。PENDING：正在加入伸缩组。REMOVING：正在移出伸缩组。PENDING_WAIT：正在加入伸缩组：等待。REMOVING_WAIT：正在移出伸缩组：等待。

        :return: The life_cycle_state of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._life_cycle_state

    @life_cycle_state.setter
    def life_cycle_state(self, life_cycle_state):
        r"""Sets the life_cycle_state of this ListScalingInstancesRequest.

        实例在伸缩组中的生命周期状态：INSERVICE： 正在使用。PENDING：正在加入伸缩组。REMOVING：正在移出伸缩组。PENDING_WAIT：正在加入伸缩组：等待。REMOVING_WAIT：正在移出伸缩组：等待。

        :param life_cycle_state: The life_cycle_state of this ListScalingInstancesRequest.
        :type life_cycle_state: str
        """
        self._life_cycle_state = life_cycle_state

    @property
    def health_status(self):
        r"""Gets the health_status of this ListScalingInstancesRequest.

        实例健康状态：INITIALIZING：初始化。NORMAL：正常。ERROR：异常

        :return: The health_status of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        r"""Sets the health_status of this ListScalingInstancesRequest.

        实例健康状态：INITIALIZING：初始化。NORMAL：正常。ERROR：异常

        :param health_status: The health_status of this ListScalingInstancesRequest.
        :type health_status: str
        """
        self._health_status = health_status

    @property
    def protect_from_scaling_down(self):
        r"""Gets the protect_from_scaling_down of this ListScalingInstancesRequest.

        实例保护状态：true：已设置实例保护。false：未设置实例保护。

        :return: The protect_from_scaling_down of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._protect_from_scaling_down

    @protect_from_scaling_down.setter
    def protect_from_scaling_down(self, protect_from_scaling_down):
        r"""Sets the protect_from_scaling_down of this ListScalingInstancesRequest.

        实例保护状态：true：已设置实例保护。false：未设置实例保护。

        :param protect_from_scaling_down: The protect_from_scaling_down of this ListScalingInstancesRequest.
        :type protect_from_scaling_down: str
        """
        self._protect_from_scaling_down = protect_from_scaling_down

    @property
    def start_number(self):
        r"""Gets the start_number of this ListScalingInstancesRequest.

        查询的起始行号，默认为0。

        :return: The start_number of this ListScalingInstancesRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        r"""Sets the start_number of this ListScalingInstancesRequest.

        查询的起始行号，默认为0。

        :param start_number: The start_number of this ListScalingInstancesRequest.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        r"""Gets the limit of this ListScalingInstancesRequest.

        查询的记录条数，默认为20。

        :return: The limit of this ListScalingInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScalingInstancesRequest.

        查询的记录条数，默认为20。

        :param limit: The limit of this ListScalingInstancesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListScalingInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
