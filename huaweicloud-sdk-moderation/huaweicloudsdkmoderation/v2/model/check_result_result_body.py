# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckResultResultBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'status': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'items': 'list[CheckResultItemsBody]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'items': 'items'
    }

    def __init__(self, job_id=None, status=None, create_time=None, update_time=None, items=None):
        """CheckResultResultBody

        The model defined in huaweicloud sdk

        :param job_id: 任务标识。
        :type job_id: str
        :param status: 任务状态。  created：已创建  running：正在处理  finish：已完成  failed：处理失败 
        :type status: str
        :param create_time: 任务创建的时间。例如：2018-01-02T15:03:04Z
        :type create_time: str
        :param update_time: 任务最近更新的时间。例如：2018-01-02T15:03:04Z
        :type update_time: str
        :param items: 图片内容检测的结果列表。
        :type items: list[:class:`huaweicloudsdkmoderation.v2.CheckResultItemsBody`]
        """
        
        

        self._job_id = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._items = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if items is not None:
            self.items = items

    @property
    def job_id(self):
        """Gets the job_id of this CheckResultResultBody.

        任务标识。

        :return: The job_id of this CheckResultResultBody.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CheckResultResultBody.

        任务标识。

        :param job_id: The job_id of this CheckResultResultBody.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this CheckResultResultBody.

        任务状态。  created：已创建  running：正在处理  finish：已完成  failed：处理失败 

        :return: The status of this CheckResultResultBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckResultResultBody.

        任务状态。  created：已创建  running：正在处理  finish：已完成  failed：处理失败 

        :param status: The status of this CheckResultResultBody.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CheckResultResultBody.

        任务创建的时间。例如：2018-01-02T15:03:04Z

        :return: The create_time of this CheckResultResultBody.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CheckResultResultBody.

        任务创建的时间。例如：2018-01-02T15:03:04Z

        :param create_time: The create_time of this CheckResultResultBody.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CheckResultResultBody.

        任务最近更新的时间。例如：2018-01-02T15:03:04Z

        :return: The update_time of this CheckResultResultBody.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CheckResultResultBody.

        任务最近更新的时间。例如：2018-01-02T15:03:04Z

        :param update_time: The update_time of this CheckResultResultBody.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def items(self):
        """Gets the items of this CheckResultResultBody.

        图片内容检测的结果列表。

        :return: The items of this CheckResultResultBody.
        :rtype: list[:class:`huaweicloudsdkmoderation.v2.CheckResultItemsBody`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CheckResultResultBody.

        图片内容检测的结果列表。

        :param items: The items of this CheckResultResultBody.
        :type items: list[:class:`huaweicloudsdkmoderation.v2.CheckResultItemsBody`]
        """
        self._items = items

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
        if not isinstance(other, CheckResultResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
