# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskByServerSources:

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
        'name': 'str',
        'type': 'str',
        'state': 'str',
        'estimate_complete_time': 'int',
        'start_date': 'int',
        'speed_limit': 'int',
        'migrate_speed': 'float',
        'compress_rate': 'float',
        'start_target_server': 'bool',
        'vm_template_id': 'str',
        'region_id': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'target_server': 'TargetServerById',
        'log_collect_status': 'str',
        'exist_server': 'bool',
        'use_public_ip': 'bool',
        'clone_server': 'CloneServer',
        'remain_seconds': 'int',
        'log_bucket': 'str',
        'log_expire': 'int',
        'log_upload_time': 'int',
        'log_share_url': 'str',
        'subtask_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'state': 'state',
        'estimate_complete_time': 'estimate_complete_time',
        'start_date': 'start_date',
        'speed_limit': 'speed_limit',
        'migrate_speed': 'migrate_speed',
        'compress_rate': 'compress_rate',
        'start_target_server': 'start_target_server',
        'vm_template_id': 'vm_template_id',
        'region_id': 'region_id',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'target_server': 'target_server',
        'log_collect_status': 'log_collect_status',
        'exist_server': 'exist_server',
        'use_public_ip': 'use_public_ip',
        'clone_server': 'clone_server',
        'remain_seconds': 'remain_seconds',
        'log_bucket': 'log_bucket',
        'log_expire': 'log_expire',
        'log_upload_time': 'log_upload_time',
        'log_share_url': 'log_share_url',
        'subtask_info': 'subtask_info'
    }

    def __init__(self, id=None, name=None, type=None, state=None, estimate_complete_time=None, start_date=None, speed_limit=None, migrate_speed=None, compress_rate=None, start_target_server=None, vm_template_id=None, region_id=None, project_name=None, project_id=None, target_server=None, log_collect_status=None, exist_server=None, use_public_ip=None, clone_server=None, remain_seconds=None, log_bucket=None, log_expire=None, log_upload_time=None, log_share_url=None, subtask_info=None):
        r"""TaskByServerSources

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param name: 任务名称
        :type name: str
        :param type: 任务类型
        :type type: str
        :param state: 任务状态
        :type state: str
        :param estimate_complete_time: 预估结束时间
        :type estimate_complete_time: int
        :param start_date: 开始时间
        :type start_date: int
        :param speed_limit: 限速
        :type speed_limit: int
        :param migrate_speed: 迁移速率
        :type migrate_speed: float
        :param compress_rate: 压缩率
        :type compress_rate: float
        :param start_target_server: 是否启动虚拟机
        :type start_target_server: bool
        :param vm_template_id: 虚拟机模板ID
        :type vm_template_id: str
        :param region_id: region_id
        :type region_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param target_server: 
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServerById`
        :param log_collect_status: 日志收集状态
        :type log_collect_status: str
        :param exist_server: 是否使用已有虚拟机
        :type exist_server: bool
        :param use_public_ip: 是否使用公网IP
        :type use_public_ip: bool
        :param clone_server: 
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        :param remain_seconds: 已迁移时长
        :type remain_seconds: int
        :param log_bucket: 上传日志指定桶名称
        :type log_bucket: str
        :param log_expire: 分享链接有效期
        :type log_expire: int
        :param log_upload_time: 日志上传时间
        :type log_upload_time: int
        :param log_share_url: 分享链接url
        :type log_share_url: str
        :param subtask_info: 当前子任务及进度
        :type subtask_info: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._state = None
        self._estimate_complete_time = None
        self._start_date = None
        self._speed_limit = None
        self._migrate_speed = None
        self._compress_rate = None
        self._start_target_server = None
        self._vm_template_id = None
        self._region_id = None
        self._project_name = None
        self._project_id = None
        self._target_server = None
        self._log_collect_status = None
        self._exist_server = None
        self._use_public_ip = None
        self._clone_server = None
        self._remain_seconds = None
        self._log_bucket = None
        self._log_expire = None
        self._log_upload_time = None
        self._log_share_url = None
        self._subtask_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if estimate_complete_time is not None:
            self.estimate_complete_time = estimate_complete_time
        if start_date is not None:
            self.start_date = start_date
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if compress_rate is not None:
            self.compress_rate = compress_rate
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if vm_template_id is not None:
            self.vm_template_id = vm_template_id
        if region_id is not None:
            self.region_id = region_id
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if target_server is not None:
            self.target_server = target_server
        if log_collect_status is not None:
            self.log_collect_status = log_collect_status
        if exist_server is not None:
            self.exist_server = exist_server
        if use_public_ip is not None:
            self.use_public_ip = use_public_ip
        if clone_server is not None:
            self.clone_server = clone_server
        if remain_seconds is not None:
            self.remain_seconds = remain_seconds
        if log_bucket is not None:
            self.log_bucket = log_bucket
        if log_expire is not None:
            self.log_expire = log_expire
        if log_upload_time is not None:
            self.log_upload_time = log_upload_time
        if log_share_url is not None:
            self.log_share_url = log_share_url
        if subtask_info is not None:
            self.subtask_info = subtask_info

    @property
    def id(self):
        r"""Gets the id of this TaskByServerSources.

        任务ID

        :return: The id of this TaskByServerSources.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskByServerSources.

        任务ID

        :param id: The id of this TaskByServerSources.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TaskByServerSources.

        任务名称

        :return: The name of this TaskByServerSources.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskByServerSources.

        任务名称

        :param name: The name of this TaskByServerSources.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this TaskByServerSources.

        任务类型

        :return: The type of this TaskByServerSources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TaskByServerSources.

        任务类型

        :param type: The type of this TaskByServerSources.
        :type type: str
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this TaskByServerSources.

        任务状态

        :return: The state of this TaskByServerSources.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TaskByServerSources.

        任务状态

        :param state: The state of this TaskByServerSources.
        :type state: str
        """
        self._state = state

    @property
    def estimate_complete_time(self):
        r"""Gets the estimate_complete_time of this TaskByServerSources.

        预估结束时间

        :return: The estimate_complete_time of this TaskByServerSources.
        :rtype: int
        """
        return self._estimate_complete_time

    @estimate_complete_time.setter
    def estimate_complete_time(self, estimate_complete_time):
        r"""Sets the estimate_complete_time of this TaskByServerSources.

        预估结束时间

        :param estimate_complete_time: The estimate_complete_time of this TaskByServerSources.
        :type estimate_complete_time: int
        """
        self._estimate_complete_time = estimate_complete_time

    @property
    def start_date(self):
        r"""Gets the start_date of this TaskByServerSources.

        开始时间

        :return: The start_date of this TaskByServerSources.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this TaskByServerSources.

        开始时间

        :param start_date: The start_date of this TaskByServerSources.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def speed_limit(self):
        r"""Gets the speed_limit of this TaskByServerSources.

        限速

        :return: The speed_limit of this TaskByServerSources.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        r"""Sets the speed_limit of this TaskByServerSources.

        限速

        :param speed_limit: The speed_limit of this TaskByServerSources.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def migrate_speed(self):
        r"""Gets the migrate_speed of this TaskByServerSources.

        迁移速率

        :return: The migrate_speed of this TaskByServerSources.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        r"""Sets the migrate_speed of this TaskByServerSources.

        迁移速率

        :param migrate_speed: The migrate_speed of this TaskByServerSources.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def compress_rate(self):
        r"""Gets the compress_rate of this TaskByServerSources.

        压缩率

        :return: The compress_rate of this TaskByServerSources.
        :rtype: float
        """
        return self._compress_rate

    @compress_rate.setter
    def compress_rate(self, compress_rate):
        r"""Sets the compress_rate of this TaskByServerSources.

        压缩率

        :param compress_rate: The compress_rate of this TaskByServerSources.
        :type compress_rate: float
        """
        self._compress_rate = compress_rate

    @property
    def start_target_server(self):
        r"""Gets the start_target_server of this TaskByServerSources.

        是否启动虚拟机

        :return: The start_target_server of this TaskByServerSources.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        r"""Sets the start_target_server of this TaskByServerSources.

        是否启动虚拟机

        :param start_target_server: The start_target_server of this TaskByServerSources.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def vm_template_id(self):
        r"""Gets the vm_template_id of this TaskByServerSources.

        虚拟机模板ID

        :return: The vm_template_id of this TaskByServerSources.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        r"""Sets the vm_template_id of this TaskByServerSources.

        虚拟机模板ID

        :param vm_template_id: The vm_template_id of this TaskByServerSources.
        :type vm_template_id: str
        """
        self._vm_template_id = vm_template_id

    @property
    def region_id(self):
        r"""Gets the region_id of this TaskByServerSources.

        region_id

        :return: The region_id of this TaskByServerSources.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this TaskByServerSources.

        region_id

        :param region_id: The region_id of this TaskByServerSources.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_name(self):
        r"""Gets the project_name of this TaskByServerSources.

        项目名称

        :return: The project_name of this TaskByServerSources.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this TaskByServerSources.

        项目名称

        :param project_name: The project_name of this TaskByServerSources.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        r"""Gets the project_id of this TaskByServerSources.

        项目ID

        :return: The project_id of this TaskByServerSources.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TaskByServerSources.

        项目ID

        :param project_id: The project_id of this TaskByServerSources.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def target_server(self):
        r"""Gets the target_server of this TaskByServerSources.

        :return: The target_server of this TaskByServerSources.
        :rtype: :class:`huaweicloudsdksms.v3.TargetServerById`
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        r"""Sets the target_server of this TaskByServerSources.

        :param target_server: The target_server of this TaskByServerSources.
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServerById`
        """
        self._target_server = target_server

    @property
    def log_collect_status(self):
        r"""Gets the log_collect_status of this TaskByServerSources.

        日志收集状态

        :return: The log_collect_status of this TaskByServerSources.
        :rtype: str
        """
        return self._log_collect_status

    @log_collect_status.setter
    def log_collect_status(self, log_collect_status):
        r"""Sets the log_collect_status of this TaskByServerSources.

        日志收集状态

        :param log_collect_status: The log_collect_status of this TaskByServerSources.
        :type log_collect_status: str
        """
        self._log_collect_status = log_collect_status

    @property
    def exist_server(self):
        r"""Gets the exist_server of this TaskByServerSources.

        是否使用已有虚拟机

        :return: The exist_server of this TaskByServerSources.
        :rtype: bool
        """
        return self._exist_server

    @exist_server.setter
    def exist_server(self, exist_server):
        r"""Sets the exist_server of this TaskByServerSources.

        是否使用已有虚拟机

        :param exist_server: The exist_server of this TaskByServerSources.
        :type exist_server: bool
        """
        self._exist_server = exist_server

    @property
    def use_public_ip(self):
        r"""Gets the use_public_ip of this TaskByServerSources.

        是否使用公网IP

        :return: The use_public_ip of this TaskByServerSources.
        :rtype: bool
        """
        return self._use_public_ip

    @use_public_ip.setter
    def use_public_ip(self, use_public_ip):
        r"""Sets the use_public_ip of this TaskByServerSources.

        是否使用公网IP

        :param use_public_ip: The use_public_ip of this TaskByServerSources.
        :type use_public_ip: bool
        """
        self._use_public_ip = use_public_ip

    @property
    def clone_server(self):
        r"""Gets the clone_server of this TaskByServerSources.

        :return: The clone_server of this TaskByServerSources.
        :rtype: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        r"""Sets the clone_server of this TaskByServerSources.

        :param clone_server: The clone_server of this TaskByServerSources.
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        self._clone_server = clone_server

    @property
    def remain_seconds(self):
        r"""Gets the remain_seconds of this TaskByServerSources.

        已迁移时长

        :return: The remain_seconds of this TaskByServerSources.
        :rtype: int
        """
        return self._remain_seconds

    @remain_seconds.setter
    def remain_seconds(self, remain_seconds):
        r"""Sets the remain_seconds of this TaskByServerSources.

        已迁移时长

        :param remain_seconds: The remain_seconds of this TaskByServerSources.
        :type remain_seconds: int
        """
        self._remain_seconds = remain_seconds

    @property
    def log_bucket(self):
        r"""Gets the log_bucket of this TaskByServerSources.

        上传日志指定桶名称

        :return: The log_bucket of this TaskByServerSources.
        :rtype: str
        """
        return self._log_bucket

    @log_bucket.setter
    def log_bucket(self, log_bucket):
        r"""Sets the log_bucket of this TaskByServerSources.

        上传日志指定桶名称

        :param log_bucket: The log_bucket of this TaskByServerSources.
        :type log_bucket: str
        """
        self._log_bucket = log_bucket

    @property
    def log_expire(self):
        r"""Gets the log_expire of this TaskByServerSources.

        分享链接有效期

        :return: The log_expire of this TaskByServerSources.
        :rtype: int
        """
        return self._log_expire

    @log_expire.setter
    def log_expire(self, log_expire):
        r"""Sets the log_expire of this TaskByServerSources.

        分享链接有效期

        :param log_expire: The log_expire of this TaskByServerSources.
        :type log_expire: int
        """
        self._log_expire = log_expire

    @property
    def log_upload_time(self):
        r"""Gets the log_upload_time of this TaskByServerSources.

        日志上传时间

        :return: The log_upload_time of this TaskByServerSources.
        :rtype: int
        """
        return self._log_upload_time

    @log_upload_time.setter
    def log_upload_time(self, log_upload_time):
        r"""Sets the log_upload_time of this TaskByServerSources.

        日志上传时间

        :param log_upload_time: The log_upload_time of this TaskByServerSources.
        :type log_upload_time: int
        """
        self._log_upload_time = log_upload_time

    @property
    def log_share_url(self):
        r"""Gets the log_share_url of this TaskByServerSources.

        分享链接url

        :return: The log_share_url of this TaskByServerSources.
        :rtype: str
        """
        return self._log_share_url

    @log_share_url.setter
    def log_share_url(self, log_share_url):
        r"""Sets the log_share_url of this TaskByServerSources.

        分享链接url

        :param log_share_url: The log_share_url of this TaskByServerSources.
        :type log_share_url: str
        """
        self._log_share_url = log_share_url

    @property
    def subtask_info(self):
        r"""Gets the subtask_info of this TaskByServerSources.

        当前子任务及进度

        :return: The subtask_info of this TaskByServerSources.
        :rtype: str
        """
        return self._subtask_info

    @subtask_info.setter
    def subtask_info(self, subtask_info):
        r"""Sets the subtask_info of this TaskByServerSources.

        当前子任务及进度

        :param subtask_info: The subtask_info of this TaskByServerSources.
        :type subtask_info: str
        """
        self._subtask_info = subtask_info

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
        if not isinstance(other, TaskByServerSources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
