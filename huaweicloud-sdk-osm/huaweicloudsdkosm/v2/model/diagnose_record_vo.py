# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnoseRecordVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'params': 'dict(str, str)',
        'domain_id': 'str',
        'create_time': 'int',
        'job_id': 'str',
        'abnormal_items': 'list[str]',
        'red_count': 'int',
        'region': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'params': 'params',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'job_id': 'job_id',
        'abnormal_items': 'abnormal_items',
        'red_count': 'red_count',
        'region': 'region'
    }

    def __init__(self, id=None, status=None, params=None, domain_id=None, create_time=None, job_id=None, abnormal_items=None, red_count=None, region=None):
        """DiagnoseRecordVo

        The model defined in huaweicloud sdk

        :param id: ID 
        :type id: str
        :param status: 状态
        :type status: str
        :param params: 不同诊断定独有的属性
        :type params: dict(str, str)
        :param domain_id: 创建人
        :type domain_id: str
        :param create_time: 创建时间戳
        :type create_time: int
        :param job_id: 任务ID 
        :type job_id: str
        :param abnormal_items: 异常项id列表
        :type abnormal_items: list[str]
        :param red_count: 异常项数量
        :type red_count: int
        :param region: 区域
        :type region: str
        """
        
        

        self._id = None
        self._status = None
        self._params = None
        self._domain_id = None
        self._create_time = None
        self._job_id = None
        self._abnormal_items = None
        self._red_count = None
        self._region = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if params is not None:
            self.params = params
        if domain_id is not None:
            self.domain_id = domain_id
        if create_time is not None:
            self.create_time = create_time
        if job_id is not None:
            self.job_id = job_id
        if abnormal_items is not None:
            self.abnormal_items = abnormal_items
        if red_count is not None:
            self.red_count = red_count
        if region is not None:
            self.region = region

    @property
    def id(self):
        """Gets the id of this DiagnoseRecordVo.

        ID 

        :return: The id of this DiagnoseRecordVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiagnoseRecordVo.

        ID 

        :param id: The id of this DiagnoseRecordVo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this DiagnoseRecordVo.

        状态

        :return: The status of this DiagnoseRecordVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiagnoseRecordVo.

        状态

        :param status: The status of this DiagnoseRecordVo.
        :type status: str
        """
        self._status = status

    @property
    def params(self):
        """Gets the params of this DiagnoseRecordVo.

        不同诊断定独有的属性

        :return: The params of this DiagnoseRecordVo.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this DiagnoseRecordVo.

        不同诊断定独有的属性

        :param params: The params of this DiagnoseRecordVo.
        :type params: dict(str, str)
        """
        self._params = params

    @property
    def domain_id(self):
        """Gets the domain_id of this DiagnoseRecordVo.

        创建人

        :return: The domain_id of this DiagnoseRecordVo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DiagnoseRecordVo.

        创建人

        :param domain_id: The domain_id of this DiagnoseRecordVo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        """Gets the create_time of this DiagnoseRecordVo.

        创建时间戳

        :return: The create_time of this DiagnoseRecordVo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DiagnoseRecordVo.

        创建时间戳

        :param create_time: The create_time of this DiagnoseRecordVo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def job_id(self):
        """Gets the job_id of this DiagnoseRecordVo.

        任务ID 

        :return: The job_id of this DiagnoseRecordVo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DiagnoseRecordVo.

        任务ID 

        :param job_id: The job_id of this DiagnoseRecordVo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def abnormal_items(self):
        """Gets the abnormal_items of this DiagnoseRecordVo.

        异常项id列表

        :return: The abnormal_items of this DiagnoseRecordVo.
        :rtype: list[str]
        """
        return self._abnormal_items

    @abnormal_items.setter
    def abnormal_items(self, abnormal_items):
        """Sets the abnormal_items of this DiagnoseRecordVo.

        异常项id列表

        :param abnormal_items: The abnormal_items of this DiagnoseRecordVo.
        :type abnormal_items: list[str]
        """
        self._abnormal_items = abnormal_items

    @property
    def red_count(self):
        """Gets the red_count of this DiagnoseRecordVo.

        异常项数量

        :return: The red_count of this DiagnoseRecordVo.
        :rtype: int
        """
        return self._red_count

    @red_count.setter
    def red_count(self, red_count):
        """Sets the red_count of this DiagnoseRecordVo.

        异常项数量

        :param red_count: The red_count of this DiagnoseRecordVo.
        :type red_count: int
        """
        self._red_count = red_count

    @property
    def region(self):
        """Gets the region of this DiagnoseRecordVo.

        区域

        :return: The region of this DiagnoseRecordVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DiagnoseRecordVo.

        区域

        :param region: The region of this DiagnoseRecordVo.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, DiagnoseRecordVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
