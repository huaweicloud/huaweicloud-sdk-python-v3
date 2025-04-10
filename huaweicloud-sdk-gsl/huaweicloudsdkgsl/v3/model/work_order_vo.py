# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkOrderVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'sim_type': 'int',
        'work_order_type': 'int',
        'req_detail': 'str',
        'total_count': 'int',
        'success_count': 'int',
        'fail_count': 'int',
        'process_count': 'int',
        'status': 'int',
        'create_time': 'datetime',
        'finish_time': 'datetime',
        'fail_reason': 'str',
        'response': 'str',
        'work_order_source': 'int',
        'work_order_source_desc': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sim_type': 'sim_type',
        'work_order_type': 'work_order_type',
        'req_detail': 'req_detail',
        'total_count': 'total_count',
        'success_count': 'success_count',
        'fail_count': 'fail_count',
        'process_count': 'process_count',
        'status': 'status',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'fail_reason': 'fail_reason',
        'response': 'response',
        'work_order_source': 'work_order_source',
        'work_order_source_desc': 'work_order_source_desc'
    }

    def __init__(self, id=None, sim_type=None, work_order_type=None, req_detail=None, total_count=None, success_count=None, fail_count=None, process_count=None, status=None, create_time=None, finish_time=None, fail_reason=None, response=None, work_order_source=None, work_order_source_desc=None):
        r"""WorkOrderVo

        The model defined in huaweicloud sdk

        :param id: 业务受理ID
        :type id: int
        :param sim_type: SIM卡类型:3.实体卡
        :type sim_type: int
        :param work_order_type: 业务受理类型：1.批量激活实体卡 2.批量转移实体卡 3.创建流量池 4.实体卡复机 5.实体卡停机 6.批量启用或复机 7.批量停用或停机 8.批量订购 9.批量退订 10.实体卡激活 11.申请断网 12.达量断网 13.机卡重绑 14.实名制信息清除 15.实体卡限速 16.批量补卡 17.批量机卡重绑 18.重启已废弃后向流量池 19.批量达量断网 20断网恢复 21取消达量断网 22批量取消达量断网 23批量拆机
        :type work_order_type: int
        :param req_detail: 请求详情
        :type req_detail: str
        :param total_count: 业务受理明细总数
        :type total_count: int
        :param success_count: 业务受理明细成功数
        :type success_count: int
        :param fail_count: 业务受理明细失败数
        :type fail_count: int
        :param process_count: 业务受理明细处理中数
        :type process_count: int
        :param status: 业务受理状态：1审核中、2已审核、3处理中、4已完成、5已取消、6失败、7 审核不通过
        :type status: int
        :param create_time: 创建时间
        :type create_time: datetime
        :param finish_time: 完成时间
        :type finish_time: datetime
        :param fail_reason: 失败原因
        :type fail_reason: str
        :param response: 响应内容
        :type response: str
        :param work_order_source: 业务受理单来源,1:运营人员生成,2:用户操作生成(console),3:自动化规则生成,4:后向流量池超阈值停用次月自动复机任务,5:单卡没流量停机定时任务,6:SIM卡到期自动停机定时任务,7:流量池停机定时任务,8:用户操作生成(api)
        :type work_order_source: int
        :param work_order_source_desc: 业务受理单来源描述
        :type work_order_source_desc: str
        """
        
        

        self._id = None
        self._sim_type = None
        self._work_order_type = None
        self._req_detail = None
        self._total_count = None
        self._success_count = None
        self._fail_count = None
        self._process_count = None
        self._status = None
        self._create_time = None
        self._finish_time = None
        self._fail_reason = None
        self._response = None
        self._work_order_source = None
        self._work_order_source_desc = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sim_type is not None:
            self.sim_type = sim_type
        if work_order_type is not None:
            self.work_order_type = work_order_type
        if req_detail is not None:
            self.req_detail = req_detail
        if total_count is not None:
            self.total_count = total_count
        if success_count is not None:
            self.success_count = success_count
        if fail_count is not None:
            self.fail_count = fail_count
        if process_count is not None:
            self.process_count = process_count
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if response is not None:
            self.response = response
        if work_order_source is not None:
            self.work_order_source = work_order_source
        if work_order_source_desc is not None:
            self.work_order_source_desc = work_order_source_desc

    @property
    def id(self):
        r"""Gets the id of this WorkOrderVo.

        业务受理ID

        :return: The id of this WorkOrderVo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkOrderVo.

        业务受理ID

        :param id: The id of this WorkOrderVo.
        :type id: int
        """
        self._id = id

    @property
    def sim_type(self):
        r"""Gets the sim_type of this WorkOrderVo.

        SIM卡类型:3.实体卡

        :return: The sim_type of this WorkOrderVo.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        r"""Sets the sim_type of this WorkOrderVo.

        SIM卡类型:3.实体卡

        :param sim_type: The sim_type of this WorkOrderVo.
        :type sim_type: int
        """
        self._sim_type = sim_type

    @property
    def work_order_type(self):
        r"""Gets the work_order_type of this WorkOrderVo.

        业务受理类型：1.批量激活实体卡 2.批量转移实体卡 3.创建流量池 4.实体卡复机 5.实体卡停机 6.批量启用或复机 7.批量停用或停机 8.批量订购 9.批量退订 10.实体卡激活 11.申请断网 12.达量断网 13.机卡重绑 14.实名制信息清除 15.实体卡限速 16.批量补卡 17.批量机卡重绑 18.重启已废弃后向流量池 19.批量达量断网 20断网恢复 21取消达量断网 22批量取消达量断网 23批量拆机

        :return: The work_order_type of this WorkOrderVo.
        :rtype: int
        """
        return self._work_order_type

    @work_order_type.setter
    def work_order_type(self, work_order_type):
        r"""Sets the work_order_type of this WorkOrderVo.

        业务受理类型：1.批量激活实体卡 2.批量转移实体卡 3.创建流量池 4.实体卡复机 5.实体卡停机 6.批量启用或复机 7.批量停用或停机 8.批量订购 9.批量退订 10.实体卡激活 11.申请断网 12.达量断网 13.机卡重绑 14.实名制信息清除 15.实体卡限速 16.批量补卡 17.批量机卡重绑 18.重启已废弃后向流量池 19.批量达量断网 20断网恢复 21取消达量断网 22批量取消达量断网 23批量拆机

        :param work_order_type: The work_order_type of this WorkOrderVo.
        :type work_order_type: int
        """
        self._work_order_type = work_order_type

    @property
    def req_detail(self):
        r"""Gets the req_detail of this WorkOrderVo.

        请求详情

        :return: The req_detail of this WorkOrderVo.
        :rtype: str
        """
        return self._req_detail

    @req_detail.setter
    def req_detail(self, req_detail):
        r"""Sets the req_detail of this WorkOrderVo.

        请求详情

        :param req_detail: The req_detail of this WorkOrderVo.
        :type req_detail: str
        """
        self._req_detail = req_detail

    @property
    def total_count(self):
        r"""Gets the total_count of this WorkOrderVo.

        业务受理明细总数

        :return: The total_count of this WorkOrderVo.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this WorkOrderVo.

        业务受理明细总数

        :param total_count: The total_count of this WorkOrderVo.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def success_count(self):
        r"""Gets the success_count of this WorkOrderVo.

        业务受理明细成功数

        :return: The success_count of this WorkOrderVo.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this WorkOrderVo.

        业务受理明细成功数

        :param success_count: The success_count of this WorkOrderVo.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def fail_count(self):
        r"""Gets the fail_count of this WorkOrderVo.

        业务受理明细失败数

        :return: The fail_count of this WorkOrderVo.
        :rtype: int
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        r"""Sets the fail_count of this WorkOrderVo.

        业务受理明细失败数

        :param fail_count: The fail_count of this WorkOrderVo.
        :type fail_count: int
        """
        self._fail_count = fail_count

    @property
    def process_count(self):
        r"""Gets the process_count of this WorkOrderVo.

        业务受理明细处理中数

        :return: The process_count of this WorkOrderVo.
        :rtype: int
        """
        return self._process_count

    @process_count.setter
    def process_count(self, process_count):
        r"""Sets the process_count of this WorkOrderVo.

        业务受理明细处理中数

        :param process_count: The process_count of this WorkOrderVo.
        :type process_count: int
        """
        self._process_count = process_count

    @property
    def status(self):
        r"""Gets the status of this WorkOrderVo.

        业务受理状态：1审核中、2已审核、3处理中、4已完成、5已取消、6失败、7 审核不通过

        :return: The status of this WorkOrderVo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkOrderVo.

        业务受理状态：1审核中、2已审核、3处理中、4已完成、5已取消、6失败、7 审核不通过

        :param status: The status of this WorkOrderVo.
        :type status: int
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this WorkOrderVo.

        创建时间

        :return: The create_time of this WorkOrderVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WorkOrderVo.

        创建时间

        :param create_time: The create_time of this WorkOrderVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this WorkOrderVo.

        完成时间

        :return: The finish_time of this WorkOrderVo.
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this WorkOrderVo.

        完成时间

        :param finish_time: The finish_time of this WorkOrderVo.
        :type finish_time: datetime
        """
        self._finish_time = finish_time

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this WorkOrderVo.

        失败原因

        :return: The fail_reason of this WorkOrderVo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this WorkOrderVo.

        失败原因

        :param fail_reason: The fail_reason of this WorkOrderVo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def response(self):
        r"""Gets the response of this WorkOrderVo.

        响应内容

        :return: The response of this WorkOrderVo.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        r"""Sets the response of this WorkOrderVo.

        响应内容

        :param response: The response of this WorkOrderVo.
        :type response: str
        """
        self._response = response

    @property
    def work_order_source(self):
        r"""Gets the work_order_source of this WorkOrderVo.

        业务受理单来源,1:运营人员生成,2:用户操作生成(console),3:自动化规则生成,4:后向流量池超阈值停用次月自动复机任务,5:单卡没流量停机定时任务,6:SIM卡到期自动停机定时任务,7:流量池停机定时任务,8:用户操作生成(api)

        :return: The work_order_source of this WorkOrderVo.
        :rtype: int
        """
        return self._work_order_source

    @work_order_source.setter
    def work_order_source(self, work_order_source):
        r"""Sets the work_order_source of this WorkOrderVo.

        业务受理单来源,1:运营人员生成,2:用户操作生成(console),3:自动化规则生成,4:后向流量池超阈值停用次月自动复机任务,5:单卡没流量停机定时任务,6:SIM卡到期自动停机定时任务,7:流量池停机定时任务,8:用户操作生成(api)

        :param work_order_source: The work_order_source of this WorkOrderVo.
        :type work_order_source: int
        """
        self._work_order_source = work_order_source

    @property
    def work_order_source_desc(self):
        r"""Gets the work_order_source_desc of this WorkOrderVo.

        业务受理单来源描述

        :return: The work_order_source_desc of this WorkOrderVo.
        :rtype: str
        """
        return self._work_order_source_desc

    @work_order_source_desc.setter
    def work_order_source_desc(self, work_order_source_desc):
        r"""Sets the work_order_source_desc of this WorkOrderVo.

        业务受理单来源描述

        :param work_order_source_desc: The work_order_source_desc of this WorkOrderVo.
        :type work_order_source_desc: str
        """
        self._work_order_source_desc = work_order_source_desc

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
        if not isinstance(other, WorkOrderVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
