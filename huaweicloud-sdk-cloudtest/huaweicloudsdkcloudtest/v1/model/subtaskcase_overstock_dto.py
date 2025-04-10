# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtaskcaseOverstockDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_time': 'datetime',
        'executor_type': 'str',
        'id': 'str',
        'label': 'str',
        'location_id': 'str',
        'subtaskcase_overstock_count': 'int',
        'test_service_id': 'str'
    }

    attribute_map = {
        'data_time': 'data_time',
        'executor_type': 'executor_type',
        'id': 'id',
        'label': 'label',
        'location_id': 'location_id',
        'subtaskcase_overstock_count': 'subtaskcase_overstock_count',
        'test_service_id': 'test_service_id'
    }

    def __init__(self, data_time=None, executor_type=None, id=None, label=None, location_id=None, subtaskcase_overstock_count=None, test_service_id=None):
        r"""SubtaskcaseOverstockDto

        The model defined in huaweicloud sdk

        :param data_time: 查询时间
        :type data_time: datetime
        :param executor_type: 执行机类型
        :type executor_type: str
        :param id: UUID
        :type id: str
        :param label: 执行机标签
        :type label: str
        :param location_id: 执行机所属区域
        :type location_id: str
        :param subtaskcase_overstock_count: 积压数量
        :type subtaskcase_overstock_count: int
        :param test_service_id: 服务ID
        :type test_service_id: str
        """
        
        

        self._data_time = None
        self._executor_type = None
        self._id = None
        self._label = None
        self._location_id = None
        self._subtaskcase_overstock_count = None
        self._test_service_id = None
        self.discriminator = None

        if data_time is not None:
            self.data_time = data_time
        if executor_type is not None:
            self.executor_type = executor_type
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if location_id is not None:
            self.location_id = location_id
        if subtaskcase_overstock_count is not None:
            self.subtaskcase_overstock_count = subtaskcase_overstock_count
        if test_service_id is not None:
            self.test_service_id = test_service_id

    @property
    def data_time(self):
        r"""Gets the data_time of this SubtaskcaseOverstockDto.

        查询时间

        :return: The data_time of this SubtaskcaseOverstockDto.
        :rtype: datetime
        """
        return self._data_time

    @data_time.setter
    def data_time(self, data_time):
        r"""Sets the data_time of this SubtaskcaseOverstockDto.

        查询时间

        :param data_time: The data_time of this SubtaskcaseOverstockDto.
        :type data_time: datetime
        """
        self._data_time = data_time

    @property
    def executor_type(self):
        r"""Gets the executor_type of this SubtaskcaseOverstockDto.

        执行机类型

        :return: The executor_type of this SubtaskcaseOverstockDto.
        :rtype: str
        """
        return self._executor_type

    @executor_type.setter
    def executor_type(self, executor_type):
        r"""Sets the executor_type of this SubtaskcaseOverstockDto.

        执行机类型

        :param executor_type: The executor_type of this SubtaskcaseOverstockDto.
        :type executor_type: str
        """
        self._executor_type = executor_type

    @property
    def id(self):
        r"""Gets the id of this SubtaskcaseOverstockDto.

        UUID

        :return: The id of this SubtaskcaseOverstockDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubtaskcaseOverstockDto.

        UUID

        :param id: The id of this SubtaskcaseOverstockDto.
        :type id: str
        """
        self._id = id

    @property
    def label(self):
        r"""Gets the label of this SubtaskcaseOverstockDto.

        执行机标签

        :return: The label of this SubtaskcaseOverstockDto.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this SubtaskcaseOverstockDto.

        执行机标签

        :param label: The label of this SubtaskcaseOverstockDto.
        :type label: str
        """
        self._label = label

    @property
    def location_id(self):
        r"""Gets the location_id of this SubtaskcaseOverstockDto.

        执行机所属区域

        :return: The location_id of this SubtaskcaseOverstockDto.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        r"""Sets the location_id of this SubtaskcaseOverstockDto.

        执行机所属区域

        :param location_id: The location_id of this SubtaskcaseOverstockDto.
        :type location_id: str
        """
        self._location_id = location_id

    @property
    def subtaskcase_overstock_count(self):
        r"""Gets the subtaskcase_overstock_count of this SubtaskcaseOverstockDto.

        积压数量

        :return: The subtaskcase_overstock_count of this SubtaskcaseOverstockDto.
        :rtype: int
        """
        return self._subtaskcase_overstock_count

    @subtaskcase_overstock_count.setter
    def subtaskcase_overstock_count(self, subtaskcase_overstock_count):
        r"""Sets the subtaskcase_overstock_count of this SubtaskcaseOverstockDto.

        积压数量

        :param subtaskcase_overstock_count: The subtaskcase_overstock_count of this SubtaskcaseOverstockDto.
        :type subtaskcase_overstock_count: int
        """
        self._subtaskcase_overstock_count = subtaskcase_overstock_count

    @property
    def test_service_id(self):
        r"""Gets the test_service_id of this SubtaskcaseOverstockDto.

        服务ID

        :return: The test_service_id of this SubtaskcaseOverstockDto.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        r"""Sets the test_service_id of this SubtaskcaseOverstockDto.

        服务ID

        :param test_service_id: The test_service_id of this SubtaskcaseOverstockDto.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

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
        if not isinstance(other, SubtaskcaseOverstockDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
