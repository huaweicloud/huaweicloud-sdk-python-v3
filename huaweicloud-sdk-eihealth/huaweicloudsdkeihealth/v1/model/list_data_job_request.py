# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator': 'str',
        'eihealth_project_id': 'str',
        'from_time': 'int',
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'status': 'str',
        'to_time': 'int',
        'type': 'str',
        'finish_from_time': 'int',
        'finish_to_time': 'int',
        'sort_dir': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'eihealth_project_id': 'eihealth_project_id',
        'from_time': 'from_time',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'status': 'status',
        'to_time': 'to_time',
        'type': 'type',
        'finish_from_time': 'finish_from_time',
        'finish_to_time': 'finish_to_time',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key'
    }

    def __init__(self, creator=None, eihealth_project_id=None, from_time=None, limit=None, name=None, offset=None, status=None, to_time=None, type=None, finish_from_time=None, finish_to_time=None, sort_dir=None, sort_key=None):
        """ListDataJobRequest

        The model defined in huaweicloud sdk

        :param creator: 创建者名称
        :type creator: str
        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param from_time: 查询该时间之后创建的数据作业
        :type from_time: int
        :param limit: 查询条数
        :type limit: int
        :param name: 数据作业名称
        :type name: str
        :param offset: 查询偏移量
        :type offset: int
        :param status: 数据作业状态
        :type status: str
        :param to_time: 查询该时间之前创建的数据作业
        :type to_time: int
        :param type: 数据作业类型
        :type type: str
        :param finish_from_time: 查询该时间之后完成的数据作业
        :type finish_from_time: int
        :param finish_to_time: 查询该时间之前完成的数据作业
        :type finish_to_time: int
        :param sort_dir: 排序规则 目前默认时间降序
        :type sort_dir: str
        :param sort_key: 排序规则 目前默认时间降序，支持根据status,name,type,creator,create_time,end_time
        :type sort_key: str
        """
        
        

        self._creator = None
        self._eihealth_project_id = None
        self._from_time = None
        self._limit = None
        self._name = None
        self._offset = None
        self._status = None
        self._to_time = None
        self._type = None
        self._finish_from_time = None
        self._finish_to_time = None
        self._sort_dir = None
        self._sort_key = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        self.eihealth_project_id = eihealth_project_id
        if from_time is not None:
            self.from_time = from_time
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if to_time is not None:
            self.to_time = to_time
        if type is not None:
            self.type = type
        if finish_from_time is not None:
            self.finish_from_time = finish_from_time
        if finish_to_time is not None:
            self.finish_to_time = finish_to_time
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def creator(self):
        """Gets the creator of this ListDataJobRequest.

        创建者名称

        :return: The creator of this ListDataJobRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ListDataJobRequest.

        创建者名称

        :param creator: The creator of this ListDataJobRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ListDataJobRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListDataJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ListDataJobRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListDataJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def from_time(self):
        """Gets the from_time of this ListDataJobRequest.

        查询该时间之后创建的数据作业

        :return: The from_time of this ListDataJobRequest.
        :rtype: int
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this ListDataJobRequest.

        查询该时间之后创建的数据作业

        :param from_time: The from_time of this ListDataJobRequest.
        :type from_time: int
        """
        self._from_time = from_time

    @property
    def limit(self):
        """Gets the limit of this ListDataJobRequest.

        查询条数

        :return: The limit of this ListDataJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDataJobRequest.

        查询条数

        :param limit: The limit of this ListDataJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListDataJobRequest.

        数据作业名称

        :return: The name of this ListDataJobRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDataJobRequest.

        数据作业名称

        :param name: The name of this ListDataJobRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListDataJobRequest.

        查询偏移量

        :return: The offset of this ListDataJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDataJobRequest.

        查询偏移量

        :param offset: The offset of this ListDataJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        """Gets the status of this ListDataJobRequest.

        数据作业状态

        :return: The status of this ListDataJobRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDataJobRequest.

        数据作业状态

        :param status: The status of this ListDataJobRequest.
        :type status: str
        """
        self._status = status

    @property
    def to_time(self):
        """Gets the to_time of this ListDataJobRequest.

        查询该时间之前创建的数据作业

        :return: The to_time of this ListDataJobRequest.
        :rtype: int
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this ListDataJobRequest.

        查询该时间之前创建的数据作业

        :param to_time: The to_time of this ListDataJobRequest.
        :type to_time: int
        """
        self._to_time = to_time

    @property
    def type(self):
        """Gets the type of this ListDataJobRequest.

        数据作业类型

        :return: The type of this ListDataJobRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListDataJobRequest.

        数据作业类型

        :param type: The type of this ListDataJobRequest.
        :type type: str
        """
        self._type = type

    @property
    def finish_from_time(self):
        """Gets the finish_from_time of this ListDataJobRequest.

        查询该时间之后完成的数据作业

        :return: The finish_from_time of this ListDataJobRequest.
        :rtype: int
        """
        return self._finish_from_time

    @finish_from_time.setter
    def finish_from_time(self, finish_from_time):
        """Sets the finish_from_time of this ListDataJobRequest.

        查询该时间之后完成的数据作业

        :param finish_from_time: The finish_from_time of this ListDataJobRequest.
        :type finish_from_time: int
        """
        self._finish_from_time = finish_from_time

    @property
    def finish_to_time(self):
        """Gets the finish_to_time of this ListDataJobRequest.

        查询该时间之前完成的数据作业

        :return: The finish_to_time of this ListDataJobRequest.
        :rtype: int
        """
        return self._finish_to_time

    @finish_to_time.setter
    def finish_to_time(self, finish_to_time):
        """Sets the finish_to_time of this ListDataJobRequest.

        查询该时间之前完成的数据作业

        :param finish_to_time: The finish_to_time of this ListDataJobRequest.
        :type finish_to_time: int
        """
        self._finish_to_time = finish_to_time

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListDataJobRequest.

        排序规则 目前默认时间降序

        :return: The sort_dir of this ListDataJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListDataJobRequest.

        排序规则 目前默认时间降序

        :param sort_dir: The sort_dir of this ListDataJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListDataJobRequest.

        排序规则 目前默认时间降序，支持根据status,name,type,creator,create_time,end_time

        :return: The sort_key of this ListDataJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListDataJobRequest.

        排序规则 目前默认时间降序，支持根据status,name,type,creator,create_time,end_time

        :param sort_key: The sort_key of this ListDataJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

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
        if not isinstance(other, ListDataJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
