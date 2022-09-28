# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'complete_data': 'list[str]',
        'running_data': 'list[str]',
        'creator': 'str',
        'source_project_id': 'str',
        'source_project_name': 'str',
        'id': 'str',
        'name': 'str',
        'sources': 'list[str]',
        'create_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'destinations': 'list[str]',
        'type': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'complete_data': 'complete_data',
        'running_data': 'running_data',
        'creator': 'creator',
        'source_project_id': 'source_project_id',
        'source_project_name': 'source_project_name',
        'id': 'id',
        'name': 'name',
        'sources': 'sources',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'status': 'status',
        'destinations': 'destinations',
        'type': 'type',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, complete_data=None, running_data=None, creator=None, source_project_id=None, source_project_name=None, id=None, name=None, sources=None, create_time=None, end_time=None, status=None, destinations=None, type=None, failed_reason=None):
        """ShowDataJobResponse

        The model defined in huaweicloud sdk

        :param complete_data: 已完成的数据列表
        :type complete_data: list[str]
        :param running_data: 正在执行的数据列表
        :type running_data: list[str]
        :param creator: 数据作业创建者
        :type creator: str
        :param source_project_id: 非本项目操作场景下源项目名称
        :type source_project_id: str
        :param source_project_name: 非本项目操作场景下源项目名称
        :type source_project_name: str
        :param id: 数据作业ID
        :type id: str
        :param name: 数据作业名称
        :type name: str
        :param sources: 数据列表
        :type sources: list[str]
        :param create_time: 数据作业创建时间
        :type create_time: str
        :param end_time: 数据作业结束时间
        :type end_time: str
        :param status: 数据作业状态
        :type status: str
        :param destinations: 数据列表
        :type destinations: list[str]
        :param type: 数据作业类型
        :type type: str
        :param failed_reason: 数据作业失败原因
        :type failed_reason: str
        """
        
        super(ShowDataJobResponse, self).__init__()

        self._complete_data = None
        self._running_data = None
        self._creator = None
        self._source_project_id = None
        self._source_project_name = None
        self._id = None
        self._name = None
        self._sources = None
        self._create_time = None
        self._end_time = None
        self._status = None
        self._destinations = None
        self._type = None
        self._failed_reason = None
        self.discriminator = None

        if complete_data is not None:
            self.complete_data = complete_data
        if running_data is not None:
            self.running_data = running_data
        if creator is not None:
            self.creator = creator
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if sources is not None:
            self.sources = sources
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if destinations is not None:
            self.destinations = destinations
        if type is not None:
            self.type = type
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def complete_data(self):
        """Gets the complete_data of this ShowDataJobResponse.

        已完成的数据列表

        :return: The complete_data of this ShowDataJobResponse.
        :rtype: list[str]
        """
        return self._complete_data

    @complete_data.setter
    def complete_data(self, complete_data):
        """Sets the complete_data of this ShowDataJobResponse.

        已完成的数据列表

        :param complete_data: The complete_data of this ShowDataJobResponse.
        :type complete_data: list[str]
        """
        self._complete_data = complete_data

    @property
    def running_data(self):
        """Gets the running_data of this ShowDataJobResponse.

        正在执行的数据列表

        :return: The running_data of this ShowDataJobResponse.
        :rtype: list[str]
        """
        return self._running_data

    @running_data.setter
    def running_data(self, running_data):
        """Sets the running_data of this ShowDataJobResponse.

        正在执行的数据列表

        :param running_data: The running_data of this ShowDataJobResponse.
        :type running_data: list[str]
        """
        self._running_data = running_data

    @property
    def creator(self):
        """Gets the creator of this ShowDataJobResponse.

        数据作业创建者

        :return: The creator of this ShowDataJobResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowDataJobResponse.

        数据作业创建者

        :param creator: The creator of this ShowDataJobResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def source_project_id(self):
        """Gets the source_project_id of this ShowDataJobResponse.

        非本项目操作场景下源项目名称

        :return: The source_project_id of this ShowDataJobResponse.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this ShowDataJobResponse.

        非本项目操作场景下源项目名称

        :param source_project_id: The source_project_id of this ShowDataJobResponse.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_project_name(self):
        """Gets the source_project_name of this ShowDataJobResponse.

        非本项目操作场景下源项目名称

        :return: The source_project_name of this ShowDataJobResponse.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        """Sets the source_project_name of this ShowDataJobResponse.

        非本项目操作场景下源项目名称

        :param source_project_name: The source_project_name of this ShowDataJobResponse.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def id(self):
        """Gets the id of this ShowDataJobResponse.

        数据作业ID

        :return: The id of this ShowDataJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDataJobResponse.

        数据作业ID

        :param id: The id of this ShowDataJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowDataJobResponse.

        数据作业名称

        :return: The name of this ShowDataJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDataJobResponse.

        数据作业名称

        :param name: The name of this ShowDataJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def sources(self):
        """Gets the sources of this ShowDataJobResponse.

        数据列表

        :return: The sources of this ShowDataJobResponse.
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this ShowDataJobResponse.

        数据列表

        :param sources: The sources of this ShowDataJobResponse.
        :type sources: list[str]
        """
        self._sources = sources

    @property
    def create_time(self):
        """Gets the create_time of this ShowDataJobResponse.

        数据作业创建时间

        :return: The create_time of this ShowDataJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDataJobResponse.

        数据作业创建时间

        :param create_time: The create_time of this ShowDataJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDataJobResponse.

        数据作业结束时间

        :return: The end_time of this ShowDataJobResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDataJobResponse.

        数据作业结束时间

        :param end_time: The end_time of this ShowDataJobResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ShowDataJobResponse.

        数据作业状态

        :return: The status of this ShowDataJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDataJobResponse.

        数据作业状态

        :param status: The status of this ShowDataJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def destinations(self):
        """Gets the destinations of this ShowDataJobResponse.

        数据列表

        :return: The destinations of this ShowDataJobResponse.
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this ShowDataJobResponse.

        数据列表

        :param destinations: The destinations of this ShowDataJobResponse.
        :type destinations: list[str]
        """
        self._destinations = destinations

    @property
    def type(self):
        """Gets the type of this ShowDataJobResponse.

        数据作业类型

        :return: The type of this ShowDataJobResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowDataJobResponse.

        数据作业类型

        :param type: The type of this ShowDataJobResponse.
        :type type: str
        """
        self._type = type

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ShowDataJobResponse.

        数据作业失败原因

        :return: The failed_reason of this ShowDataJobResponse.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ShowDataJobResponse.

        数据作业失败原因

        :param failed_reason: The failed_reason of this ShowDataJobResponse.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, ShowDataJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
