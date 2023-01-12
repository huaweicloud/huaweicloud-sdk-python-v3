# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDatabaseDataResponse(SdkResponse):

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
        'end_time': 'str',
        'id': 'str',
        'name': 'str',
        'create_time': 'str',
        'status': 'str',
        'finish_count': 'int',
        'total_count': 'int',
        'type': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'end_time': 'end_time',
        'id': 'id',
        'name': 'name',
        'create_time': 'create_time',
        'status': 'status',
        'finish_count': 'finish_count',
        'total_count': 'total_count',
        'type': 'type',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, creator=None, end_time=None, id=None, name=None, create_time=None, status=None, finish_count=None, total_count=None, type=None, failed_reason=None):
        """ImportDatabaseDataResponse

        The model defined in huaweicloud sdk

        :param creator: 数据作业创建者
        :type creator: str
        :param end_time: 数据作业结束时间
        :type end_time: str
        :param id: 数据作业ID
        :type id: str
        :param name: 数据作业名称
        :type name: str
        :param create_time: 数据作业创建时间
        :type create_time: str
        :param status: 数据作业状态
        :type status: str
        :param finish_count: 数据作业完成数
        :type finish_count: int
        :param total_count: 数据作业总数
        :type total_count: int
        :param type: 数据作业类型
        :type type: str
        :param failed_reason: 数据作业失败原因
        :type failed_reason: str
        """
        
        super(ImportDatabaseDataResponse, self).__init__()

        self._creator = None
        self._end_time = None
        self._id = None
        self._name = None
        self._create_time = None
        self._status = None
        self._finish_count = None
        self._total_count = None
        self._type = None
        self._failed_reason = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if end_time is not None:
            self.end_time = end_time
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if finish_count is not None:
            self.finish_count = finish_count
        if total_count is not None:
            self.total_count = total_count
        if type is not None:
            self.type = type
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def creator(self):
        """Gets the creator of this ImportDatabaseDataResponse.

        数据作业创建者

        :return: The creator of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ImportDatabaseDataResponse.

        数据作业创建者

        :param creator: The creator of this ImportDatabaseDataResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def end_time(self):
        """Gets the end_time of this ImportDatabaseDataResponse.

        数据作业结束时间

        :return: The end_time of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ImportDatabaseDataResponse.

        数据作业结束时间

        :param end_time: The end_time of this ImportDatabaseDataResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this ImportDatabaseDataResponse.

        数据作业ID

        :return: The id of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportDatabaseDataResponse.

        数据作业ID

        :param id: The id of this ImportDatabaseDataResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ImportDatabaseDataResponse.

        数据作业名称

        :return: The name of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportDatabaseDataResponse.

        数据作业名称

        :param name: The name of this ImportDatabaseDataResponse.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        """Gets the create_time of this ImportDatabaseDataResponse.

        数据作业创建时间

        :return: The create_time of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ImportDatabaseDataResponse.

        数据作业创建时间

        :param create_time: The create_time of this ImportDatabaseDataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this ImportDatabaseDataResponse.

        数据作业状态

        :return: The status of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImportDatabaseDataResponse.

        数据作业状态

        :param status: The status of this ImportDatabaseDataResponse.
        :type status: str
        """
        self._status = status

    @property
    def finish_count(self):
        """Gets the finish_count of this ImportDatabaseDataResponse.

        数据作业完成数

        :return: The finish_count of this ImportDatabaseDataResponse.
        :rtype: int
        """
        return self._finish_count

    @finish_count.setter
    def finish_count(self, finish_count):
        """Sets the finish_count of this ImportDatabaseDataResponse.

        数据作业完成数

        :param finish_count: The finish_count of this ImportDatabaseDataResponse.
        :type finish_count: int
        """
        self._finish_count = finish_count

    @property
    def total_count(self):
        """Gets the total_count of this ImportDatabaseDataResponse.

        数据作业总数

        :return: The total_count of this ImportDatabaseDataResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ImportDatabaseDataResponse.

        数据作业总数

        :param total_count: The total_count of this ImportDatabaseDataResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def type(self):
        """Gets the type of this ImportDatabaseDataResponse.

        数据作业类型

        :return: The type of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImportDatabaseDataResponse.

        数据作业类型

        :param type: The type of this ImportDatabaseDataResponse.
        :type type: str
        """
        self._type = type

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ImportDatabaseDataResponse.

        数据作业失败原因

        :return: The failed_reason of this ImportDatabaseDataResponse.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ImportDatabaseDataResponse.

        数据作业失败原因

        :param failed_reason: The failed_reason of this ImportDatabaseDataResponse.
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
        if not isinstance(other, ImportDatabaseDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
