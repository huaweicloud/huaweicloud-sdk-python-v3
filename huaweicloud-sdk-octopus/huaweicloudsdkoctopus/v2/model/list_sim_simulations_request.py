# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimSimulationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_name': 'str',
        'batch_id': 'int',
        'batch_name': 'str',
        'id': 'int',
        'label': 'float',
        'limit': 'int',
        'offset': 'int',
        'ordering': 'str',
        'scenario_resource_id': 'int',
        'scenario_resource_type': 'int',
        'status': 'int'
    }

    attribute_map = {
        'algorithm_name': 'algorithm_name',
        'batch_id': 'batch_id',
        'batch_name': 'batch_name',
        'id': 'id',
        'label': 'label',
        'limit': 'limit',
        'offset': 'offset',
        'ordering': 'ordering',
        'scenario_resource_id': 'scenario_resource_id',
        'scenario_resource_type': 'scenario_resource_type',
        'status': 'status'
    }

    def __init__(self, algorithm_name=None, batch_id=None, batch_name=None, id=None, label=None, limit=None, offset=None, ordering=None, scenario_resource_id=None, scenario_resource_type=None, status=None):
        r"""ListSimSimulationsRequest

        The model defined in huaweicloud sdk

        :param algorithm_name: 算法名称
        :type algorithm_name: str
        :param batch_id: 关联batch
        :type batch_id: int
        :param batch_name: 任务名称
        :type batch_name: str
        :param id: 
        :type id: int
        :param label: 场景标签
        :type label: float
        :param limit: 每页返回的结果数
        :type limit: int
        :param offset: 要从中返回结果的初始索引
        :type offset: int
        :param ordering: 使用哪个字段排序结果
        :type ordering: str
        :param scenario_resource_id: 场景资源id
        :type scenario_resource_id: int
        :param scenario_resource_type: 场景资源类型
        :type scenario_resource_type: int
        :param status: 子任务状态  * &#x60;0&#x60; - Success  成功 * &#x60;1&#x60; - Pending  等待中 * &#x60;2&#x60; - Scheduling  调度 * &#x60;3&#x60; - Running  运行 * &#x60;4&#x60; - Canceled  取消 * &#x60;10&#x60; - Prepare Fail  准备失败 * &#x60;11&#x60; - Controller Fail  控制失败 * &#x60;12&#x60; - License Fail  许可失效 * &#x60;13&#x60; - Simulator Fail  仿真器失败 * &#x60;14&#x60; - Algorithm Fail  算法失败 * &#x60;15&#x60; - Evaluation Fail  评测失败 * &#x60;16&#x60; - Evicted  丢失 * &#x60;31&#x60; - Timeout  超时 * &#x60;32&#x60; - Unknown  未知
        :type status: int
        """
        
        

        self._algorithm_name = None
        self._batch_id = None
        self._batch_name = None
        self._id = None
        self._label = None
        self._limit = None
        self._offset = None
        self._ordering = None
        self._scenario_resource_id = None
        self._scenario_resource_type = None
        self._status = None
        self.discriminator = None

        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if batch_id is not None:
            self.batch_id = batch_id
        if batch_name is not None:
            self.batch_name = batch_name
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if ordering is not None:
            self.ordering = ordering
        if scenario_resource_id is not None:
            self.scenario_resource_id = scenario_resource_id
        if scenario_resource_type is not None:
            self.scenario_resource_type = scenario_resource_type
        if status is not None:
            self.status = status

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this ListSimSimulationsRequest.

        算法名称

        :return: The algorithm_name of this ListSimSimulationsRequest.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this ListSimSimulationsRequest.

        算法名称

        :param algorithm_name: The algorithm_name of this ListSimSimulationsRequest.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

    @property
    def batch_id(self):
        r"""Gets the batch_id of this ListSimSimulationsRequest.

        关联batch

        :return: The batch_id of this ListSimSimulationsRequest.
        :rtype: int
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        r"""Sets the batch_id of this ListSimSimulationsRequest.

        关联batch

        :param batch_id: The batch_id of this ListSimSimulationsRequest.
        :type batch_id: int
        """
        self._batch_id = batch_id

    @property
    def batch_name(self):
        r"""Gets the batch_name of this ListSimSimulationsRequest.

        任务名称

        :return: The batch_name of this ListSimSimulationsRequest.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this ListSimSimulationsRequest.

        任务名称

        :param batch_name: The batch_name of this ListSimSimulationsRequest.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def id(self):
        r"""Gets the id of this ListSimSimulationsRequest.

        :return: The id of this ListSimSimulationsRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSimSimulationsRequest.

        :param id: The id of this ListSimSimulationsRequest.
        :type id: int
        """
        self._id = id

    @property
    def label(self):
        r"""Gets the label of this ListSimSimulationsRequest.

        场景标签

        :return: The label of this ListSimSimulationsRequest.
        :rtype: float
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ListSimSimulationsRequest.

        场景标签

        :param label: The label of this ListSimSimulationsRequest.
        :type label: float
        """
        self._label = label

    @property
    def limit(self):
        r"""Gets the limit of this ListSimSimulationsRequest.

        每页返回的结果数

        :return: The limit of this ListSimSimulationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimSimulationsRequest.

        每页返回的结果数

        :param limit: The limit of this ListSimSimulationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSimSimulationsRequest.

        要从中返回结果的初始索引

        :return: The offset of this ListSimSimulationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimSimulationsRequest.

        要从中返回结果的初始索引

        :param offset: The offset of this ListSimSimulationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def ordering(self):
        r"""Gets the ordering of this ListSimSimulationsRequest.

        使用哪个字段排序结果

        :return: The ordering of this ListSimSimulationsRequest.
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        r"""Sets the ordering of this ListSimSimulationsRequest.

        使用哪个字段排序结果

        :param ordering: The ordering of this ListSimSimulationsRequest.
        :type ordering: str
        """
        self._ordering = ordering

    @property
    def scenario_resource_id(self):
        r"""Gets the scenario_resource_id of this ListSimSimulationsRequest.

        场景资源id

        :return: The scenario_resource_id of this ListSimSimulationsRequest.
        :rtype: int
        """
        return self._scenario_resource_id

    @scenario_resource_id.setter
    def scenario_resource_id(self, scenario_resource_id):
        r"""Sets the scenario_resource_id of this ListSimSimulationsRequest.

        场景资源id

        :param scenario_resource_id: The scenario_resource_id of this ListSimSimulationsRequest.
        :type scenario_resource_id: int
        """
        self._scenario_resource_id = scenario_resource_id

    @property
    def scenario_resource_type(self):
        r"""Gets the scenario_resource_type of this ListSimSimulationsRequest.

        场景资源类型

        :return: The scenario_resource_type of this ListSimSimulationsRequest.
        :rtype: int
        """
        return self._scenario_resource_type

    @scenario_resource_type.setter
    def scenario_resource_type(self, scenario_resource_type):
        r"""Sets the scenario_resource_type of this ListSimSimulationsRequest.

        场景资源类型

        :param scenario_resource_type: The scenario_resource_type of this ListSimSimulationsRequest.
        :type scenario_resource_type: int
        """
        self._scenario_resource_type = scenario_resource_type

    @property
    def status(self):
        r"""Gets the status of this ListSimSimulationsRequest.

        子任务状态  * `0` - Success  成功 * `1` - Pending  等待中 * `2` - Scheduling  调度 * `3` - Running  运行 * `4` - Canceled  取消 * `10` - Prepare Fail  准备失败 * `11` - Controller Fail  控制失败 * `12` - License Fail  许可失效 * `13` - Simulator Fail  仿真器失败 * `14` - Algorithm Fail  算法失败 * `15` - Evaluation Fail  评测失败 * `16` - Evicted  丢失 * `31` - Timeout  超时 * `32` - Unknown  未知

        :return: The status of this ListSimSimulationsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSimSimulationsRequest.

        子任务状态  * `0` - Success  成功 * `1` - Pending  等待中 * `2` - Scheduling  调度 * `3` - Running  运行 * `4` - Canceled  取消 * `10` - Prepare Fail  准备失败 * `11` - Controller Fail  控制失败 * `12` - License Fail  许可失效 * `13` - Simulator Fail  仿真器失败 * `14` - Algorithm Fail  算法失败 * `15` - Evaluation Fail  评测失败 * `16` - Evicted  丢失 * `31` - Timeout  超时 * `32` - Unknown  未知

        :param status: The status of this ListSimSimulationsRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListSimSimulationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
