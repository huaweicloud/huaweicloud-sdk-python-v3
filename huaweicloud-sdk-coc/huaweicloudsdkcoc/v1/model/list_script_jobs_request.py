# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'creator': 'str',
        'status': 'str',
        'x_language': 'str',
        'x_project_id': 'str',
        'x_user_profile': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'creator': 'creator',
        'status': 'status',
        'x_language': 'X-Language',
        'x_project_id': 'x-project-id',
        'x_user_profile': 'x-user-profile'
    }

    def __init__(self, limit=None, marker=None, start_time=None, end_time=None, creator=None, status=None, x_language=None, x_project_id=None, x_user_profile=None):
        r"""ListScriptJobsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页参数
        :type limit: int
        :param marker: 分页参数
        :type marker: int
        :param start_time: 创建时间开始
        :type start_time: int
        :param end_time: 创建时间结束
        :type end_time: int
        :param creator: 创建人
        :type creator: str
        :param status: 工单状态 PROCESSING：执行中 ABNORMAL：异常 PAUSED：暂停 CANCELED：已取消 FINISHED：成功
        :type status: str
        :param x_language: 国际化标记，zh-cn表示中文，en-us或不传表示英文
        :type x_language: str
        :param x_project_id: 项目ID，一个项目对应一个region
        :type x_project_id: str
        :param x_user_profile: IAM5.0用户信息
        :type x_user_profile: str
        """
        
        

        self._limit = None
        self._marker = None
        self._start_time = None
        self._end_time = None
        self._creator = None
        self._status = None
        self._x_language = None
        self._x_project_id = None
        self._x_user_profile = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if creator is not None:
            self.creator = creator
        if status is not None:
            self.status = status
        if x_language is not None:
            self.x_language = x_language
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_user_profile is not None:
            self.x_user_profile = x_user_profile

    @property
    def limit(self):
        r"""Gets the limit of this ListScriptJobsRequest.

        分页参数

        :return: The limit of this ListScriptJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScriptJobsRequest.

        分页参数

        :param limit: The limit of this ListScriptJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListScriptJobsRequest.

        分页参数

        :return: The marker of this ListScriptJobsRequest.
        :rtype: int
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListScriptJobsRequest.

        分页参数

        :param marker: The marker of this ListScriptJobsRequest.
        :type marker: int
        """
        self._marker = marker

    @property
    def start_time(self):
        r"""Gets the start_time of this ListScriptJobsRequest.

        创建时间开始

        :return: The start_time of this ListScriptJobsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListScriptJobsRequest.

        创建时间开始

        :param start_time: The start_time of this ListScriptJobsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListScriptJobsRequest.

        创建时间结束

        :return: The end_time of this ListScriptJobsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListScriptJobsRequest.

        创建时间结束

        :param end_time: The end_time of this ListScriptJobsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def creator(self):
        r"""Gets the creator of this ListScriptJobsRequest.

        创建人

        :return: The creator of this ListScriptJobsRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListScriptJobsRequest.

        创建人

        :param creator: The creator of this ListScriptJobsRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def status(self):
        r"""Gets the status of this ListScriptJobsRequest.

        工单状态 PROCESSING：执行中 ABNORMAL：异常 PAUSED：暂停 CANCELED：已取消 FINISHED：成功

        :return: The status of this ListScriptJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScriptJobsRequest.

        工单状态 PROCESSING：执行中 ABNORMAL：异常 PAUSED：暂停 CANCELED：已取消 FINISHED：成功

        :param status: The status of this ListScriptJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def x_language(self):
        r"""Gets the x_language of this ListScriptJobsRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :return: The x_language of this ListScriptJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListScriptJobsRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :param x_language: The x_language of this ListScriptJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListScriptJobsRequest.

        项目ID，一个项目对应一个region

        :return: The x_project_id of this ListScriptJobsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListScriptJobsRequest.

        项目ID，一个项目对应一个region

        :param x_project_id: The x_project_id of this ListScriptJobsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_user_profile(self):
        r"""Gets the x_user_profile of this ListScriptJobsRequest.

        IAM5.0用户信息

        :return: The x_user_profile of this ListScriptJobsRequest.
        :rtype: str
        """
        return self._x_user_profile

    @x_user_profile.setter
    def x_user_profile(self, x_user_profile):
        r"""Sets the x_user_profile of this ListScriptJobsRequest.

        IAM5.0用户信息

        :param x_user_profile: The x_user_profile of this ListScriptJobsRequest.
        :type x_user_profile: str
        """
        self._x_user_profile = x_user_profile

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
        if not isinstance(other, ListScriptJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
