# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHarvestTaskInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'event_name': 'str',
        'task_desc': 'str',
        'package_info': 'VodPackageInfo'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'event_name': 'event_name',
        'task_desc': 'task_desc',
        'package_info': 'package_info'
    }

    def __init__(self, domain=None, app_name=None, id=None, start_time=None, end_time=None, event_name=None, task_desc=None, package_info=None):
        r"""CreateHarvestTaskInfoReq

        The model defined in huaweicloud sdk

        :param domain: 频道推流域名
        :type domain: str
        :param app_name: 组名或应用名
        :type app_name: str
        :param id: 频道ID。频道唯一标识，为必填项。
        :type id: str
        :param start_time: 开始时间。Unix时间戳：单位是秒
        :type start_time: int
        :param end_time: 结束时间。Unix时间戳：单位是秒
        :type end_time: int
        :param event_name: 事件名称。必选配置
        :type event_name: str
        :param task_desc: 任务描述，可选配置
        :type task_desc: str
        :param package_info: 
        :type package_info: :class:`huaweicloudsdklive.v1.VodPackageInfo`
        """
        
        

        self._domain = None
        self._app_name = None
        self._id = None
        self._start_time = None
        self._end_time = None
        self._event_name = None
        self._task_desc = None
        self._package_info = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.event_name = event_name
        if task_desc is not None:
            self.task_desc = task_desc
        if package_info is not None:
            self.package_info = package_info

    @property
    def domain(self):
        r"""Gets the domain of this CreateHarvestTaskInfoReq.

        频道推流域名

        :return: The domain of this CreateHarvestTaskInfoReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CreateHarvestTaskInfoReq.

        频道推流域名

        :param domain: The domain of this CreateHarvestTaskInfoReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this CreateHarvestTaskInfoReq.

        组名或应用名

        :return: The app_name of this CreateHarvestTaskInfoReq.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this CreateHarvestTaskInfoReq.

        组名或应用名

        :param app_name: The app_name of this CreateHarvestTaskInfoReq.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this CreateHarvestTaskInfoReq.

        频道ID。频道唯一标识，为必填项。

        :return: The id of this CreateHarvestTaskInfoReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateHarvestTaskInfoReq.

        频道ID。频道唯一标识，为必填项。

        :param id: The id of this CreateHarvestTaskInfoReq.
        :type id: str
        """
        self._id = id

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateHarvestTaskInfoReq.

        开始时间。Unix时间戳：单位是秒

        :return: The start_time of this CreateHarvestTaskInfoReq.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateHarvestTaskInfoReq.

        开始时间。Unix时间戳：单位是秒

        :param start_time: The start_time of this CreateHarvestTaskInfoReq.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CreateHarvestTaskInfoReq.

        结束时间。Unix时间戳：单位是秒

        :return: The end_time of this CreateHarvestTaskInfoReq.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CreateHarvestTaskInfoReq.

        结束时间。Unix时间戳：单位是秒

        :param end_time: The end_time of this CreateHarvestTaskInfoReq.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def event_name(self):
        r"""Gets the event_name of this CreateHarvestTaskInfoReq.

        事件名称。必选配置

        :return: The event_name of this CreateHarvestTaskInfoReq.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this CreateHarvestTaskInfoReq.

        事件名称。必选配置

        :param event_name: The event_name of this CreateHarvestTaskInfoReq.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def task_desc(self):
        r"""Gets the task_desc of this CreateHarvestTaskInfoReq.

        任务描述，可选配置

        :return: The task_desc of this CreateHarvestTaskInfoReq.
        :rtype: str
        """
        return self._task_desc

    @task_desc.setter
    def task_desc(self, task_desc):
        r"""Sets the task_desc of this CreateHarvestTaskInfoReq.

        任务描述，可选配置

        :param task_desc: The task_desc of this CreateHarvestTaskInfoReq.
        :type task_desc: str
        """
        self._task_desc = task_desc

    @property
    def package_info(self):
        r"""Gets the package_info of this CreateHarvestTaskInfoReq.

        :return: The package_info of this CreateHarvestTaskInfoReq.
        :rtype: :class:`huaweicloudsdklive.v1.VodPackageInfo`
        """
        return self._package_info

    @package_info.setter
    def package_info(self, package_info):
        r"""Sets the package_info of this CreateHarvestTaskInfoReq.

        :param package_info: The package_info of this CreateHarvestTaskInfoReq.
        :type package_info: :class:`huaweicloudsdklive.v1.VodPackageInfo`
        """
        self._package_info = package_info

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
        if not isinstance(other, CreateHarvestTaskInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
