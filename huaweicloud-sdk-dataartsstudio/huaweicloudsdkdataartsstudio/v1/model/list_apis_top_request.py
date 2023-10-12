# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApisTopRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'instance_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'time_unit': 'str',
        'top_num': 'int',
        'order_by': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_unit': 'time_unit',
        'top_num': 'top_num',
        'order_by': 'order_by'
    }

    def __init__(self, workspace=None, dlm_type=None, instance_id=None, start_time=None, end_time=None, time_unit=None, top_num=None, order_by=None):
        """ListApisTopRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param instance_id: 集群编号
        :type instance_id: str
        :param start_time: 开始时间（13位时间戳）
        :type start_time: int
        :param end_time: 结束时间（13位时间戳）
        :type end_time: int
        :param time_unit: 时间单位
        :type time_unit: str
        :param top_num: 前几名
        :type top_num: int
        :param order_by: 排序条件
        :type order_by: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._time_unit = None
        self._top_num = None
        self._order_by = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        if instance_id is not None:
            self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.time_unit = time_unit
        self.top_num = top_num
        self.order_by = order_by

    @property
    def workspace(self):
        """Gets the workspace of this ListApisTopRequest.

        工作空间id

        :return: The workspace of this ListApisTopRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListApisTopRequest.

        工作空间id

        :param workspace: The workspace of this ListApisTopRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ListApisTopRequest.

        dlm版本类型

        :return: The dlm_type of this ListApisTopRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ListApisTopRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this ListApisTopRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def instance_id(self):
        """Gets the instance_id of this ListApisTopRequest.

        集群编号

        :return: The instance_id of this ListApisTopRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListApisTopRequest.

        集群编号

        :param instance_id: The instance_id of this ListApisTopRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        """Gets the start_time of this ListApisTopRequest.

        开始时间（13位时间戳）

        :return: The start_time of this ListApisTopRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListApisTopRequest.

        开始时间（13位时间戳）

        :param start_time: The start_time of this ListApisTopRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListApisTopRequest.

        结束时间（13位时间戳）

        :return: The end_time of this ListApisTopRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListApisTopRequest.

        结束时间（13位时间戳）

        :param end_time: The end_time of this ListApisTopRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def time_unit(self):
        """Gets the time_unit of this ListApisTopRequest.

        时间单位

        :return: The time_unit of this ListApisTopRequest.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this ListApisTopRequest.

        时间单位

        :param time_unit: The time_unit of this ListApisTopRequest.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def top_num(self):
        """Gets the top_num of this ListApisTopRequest.

        前几名

        :return: The top_num of this ListApisTopRequest.
        :rtype: int
        """
        return self._top_num

    @top_num.setter
    def top_num(self, top_num):
        """Sets the top_num of this ListApisTopRequest.

        前几名

        :param top_num: The top_num of this ListApisTopRequest.
        :type top_num: int
        """
        self._top_num = top_num

    @property
    def order_by(self):
        """Gets the order_by of this ListApisTopRequest.

        排序条件

        :return: The order_by of this ListApisTopRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListApisTopRequest.

        排序条件

        :param order_by: The order_by of this ListApisTopRequest.
        :type order_by: str
        """
        self._order_by = order_by

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
        if not isinstance(other, ListApisTopRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
