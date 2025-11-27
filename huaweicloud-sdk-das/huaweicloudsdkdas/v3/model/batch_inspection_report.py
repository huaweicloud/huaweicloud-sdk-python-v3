# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchInspectionReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'cpu': 'int',
        'mem': 'int',
        'disk_size': 'int',
        'create_at': 'int',
        'start_at': 'int',
        'end_at': 'int',
        'health_rank': 'str',
        'score': 'float',
        'lost_points_detail_list': 'list[BatchInspectionLostPointsDetail]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'cpu': 'cpu',
        'mem': 'mem',
        'disk_size': 'disk_size',
        'create_at': 'create_at',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'health_rank': 'health_rank',
        'score': 'score',
        'lost_points_detail_list': 'lost_points_detail_list'
    }

    def __init__(self, task_id=None, instance_id=None, instance_name=None, cpu=None, mem=None, disk_size=None, create_at=None, start_at=None, end_at=None, health_rank=None, score=None, lost_points_detail_list=None):
        r"""BatchInspectionReport

        The model defined in huaweicloud sdk

        :param task_id: 报告ID
        :type task_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param cpu: CPU大小
        :type cpu: int
        :param mem: 内存大小（单位:GB）
        :type mem: int
        :param disk_size: 磁盘大小（单位:GB）
        :type disk_size: int
        :param create_at: 诊断报告生成时间（Unix timestamp），单位：毫秒。
        :type create_at: int
        :param start_at: 诊断起始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 诊断终止时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param health_rank: 健康等级
        :type health_rank: str
        :param score: 评分
        :type score: float
        :param lost_points_detail_list: 扣分详情
        :type lost_points_detail_list: list[:class:`huaweicloudsdkdas.v3.BatchInspectionLostPointsDetail`]
        """
        
        

        self._task_id = None
        self._instance_id = None
        self._instance_name = None
        self._cpu = None
        self._mem = None
        self._disk_size = None
        self._create_at = None
        self._start_at = None
        self._end_at = None
        self._health_rank = None
        self._score = None
        self._lost_points_detail_list = None
        self.discriminator = None

        self.task_id = task_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if disk_size is not None:
            self.disk_size = disk_size
        if create_at is not None:
            self.create_at = create_at
        self.start_at = start_at
        self.end_at = end_at
        if health_rank is not None:
            self.health_rank = health_rank
        if score is not None:
            self.score = score
        if lost_points_detail_list is not None:
            self.lost_points_detail_list = lost_points_detail_list

    @property
    def task_id(self):
        r"""Gets the task_id of this BatchInspectionReport.

        报告ID

        :return: The task_id of this BatchInspectionReport.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this BatchInspectionReport.

        报告ID

        :param task_id: The task_id of this BatchInspectionReport.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchInspectionReport.

        实例ID

        :return: The instance_id of this BatchInspectionReport.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchInspectionReport.

        实例ID

        :param instance_id: The instance_id of this BatchInspectionReport.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this BatchInspectionReport.

        实例名称

        :return: The instance_name of this BatchInspectionReport.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this BatchInspectionReport.

        实例名称

        :param instance_name: The instance_name of this BatchInspectionReport.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def cpu(self):
        r"""Gets the cpu of this BatchInspectionReport.

        CPU大小

        :return: The cpu of this BatchInspectionReport.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this BatchInspectionReport.

        CPU大小

        :param cpu: The cpu of this BatchInspectionReport.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this BatchInspectionReport.

        内存大小（单位:GB）

        :return: The mem of this BatchInspectionReport.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this BatchInspectionReport.

        内存大小（单位:GB）

        :param mem: The mem of this BatchInspectionReport.
        :type mem: int
        """
        self._mem = mem

    @property
    def disk_size(self):
        r"""Gets the disk_size of this BatchInspectionReport.

        磁盘大小（单位:GB）

        :return: The disk_size of this BatchInspectionReport.
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        r"""Sets the disk_size of this BatchInspectionReport.

        磁盘大小（单位:GB）

        :param disk_size: The disk_size of this BatchInspectionReport.
        :type disk_size: int
        """
        self._disk_size = disk_size

    @property
    def create_at(self):
        r"""Gets the create_at of this BatchInspectionReport.

        诊断报告生成时间（Unix timestamp），单位：毫秒。

        :return: The create_at of this BatchInspectionReport.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this BatchInspectionReport.

        诊断报告生成时间（Unix timestamp），单位：毫秒。

        :param create_at: The create_at of this BatchInspectionReport.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def start_at(self):
        r"""Gets the start_at of this BatchInspectionReport.

        诊断起始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this BatchInspectionReport.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this BatchInspectionReport.

        诊断起始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this BatchInspectionReport.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this BatchInspectionReport.

        诊断终止时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this BatchInspectionReport.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this BatchInspectionReport.

        诊断终止时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this BatchInspectionReport.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def health_rank(self):
        r"""Gets the health_rank of this BatchInspectionReport.

        健康等级

        :return: The health_rank of this BatchInspectionReport.
        :rtype: str
        """
        return self._health_rank

    @health_rank.setter
    def health_rank(self, health_rank):
        r"""Sets the health_rank of this BatchInspectionReport.

        健康等级

        :param health_rank: The health_rank of this BatchInspectionReport.
        :type health_rank: str
        """
        self._health_rank = health_rank

    @property
    def score(self):
        r"""Gets the score of this BatchInspectionReport.

        评分

        :return: The score of this BatchInspectionReport.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this BatchInspectionReport.

        评分

        :param score: The score of this BatchInspectionReport.
        :type score: float
        """
        self._score = score

    @property
    def lost_points_detail_list(self):
        r"""Gets the lost_points_detail_list of this BatchInspectionReport.

        扣分详情

        :return: The lost_points_detail_list of this BatchInspectionReport.
        :rtype: list[:class:`huaweicloudsdkdas.v3.BatchInspectionLostPointsDetail`]
        """
        return self._lost_points_detail_list

    @lost_points_detail_list.setter
    def lost_points_detail_list(self, lost_points_detail_list):
        r"""Sets the lost_points_detail_list of this BatchInspectionReport.

        扣分详情

        :param lost_points_detail_list: The lost_points_detail_list of this BatchInspectionReport.
        :type lost_points_detail_list: list[:class:`huaweicloudsdkdas.v3.BatchInspectionLostPointsDetail`]
        """
        self._lost_points_detail_list = lost_points_detail_list

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
        if not isinstance(other, BatchInspectionReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
