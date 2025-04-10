# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vertices:

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
        'display_name': 'str',
        'build_duration': 'int',
        'start_time': 'str',
        'finish_time': 'str',
        'build_no': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'display_name': 'display_name',
        'build_duration': 'build_duration',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'build_no': 'build_no'
    }

    def __init__(self, id=None, status=None, display_name=None, build_duration=None, start_time=None, finish_time=None, build_no=None):
        r"""Vertices

        The model defined in huaweicloud sdk

        :param id: 子任务构建记录ID
        :type id: str
        :param status: 子任务执行状态
        :type status: str
        :param display_name: 子任务名称
        :type display_name: str
        :param build_duration: 子任务构建耗时
        :type build_duration: int
        :param start_time: 子任务开始时间
        :type start_time: str
        :param finish_time: 子任务结束时间
        :type finish_time: str
        :param build_no: 子任务构建编号
        :type build_no: str
        """
        
        

        self._id = None
        self._status = None
        self._display_name = None
        self._build_duration = None
        self._start_time = None
        self._finish_time = None
        self._build_no = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if display_name is not None:
            self.display_name = display_name
        if build_duration is not None:
            self.build_duration = build_duration
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if build_no is not None:
            self.build_no = build_no

    @property
    def id(self):
        r"""Gets the id of this Vertices.

        子任务构建记录ID

        :return: The id of this Vertices.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Vertices.

        子任务构建记录ID

        :param id: The id of this Vertices.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this Vertices.

        子任务执行状态

        :return: The status of this Vertices.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Vertices.

        子任务执行状态

        :param status: The status of this Vertices.
        :type status: str
        """
        self._status = status

    @property
    def display_name(self):
        r"""Gets the display_name of this Vertices.

        子任务名称

        :return: The display_name of this Vertices.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this Vertices.

        子任务名称

        :param display_name: The display_name of this Vertices.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def build_duration(self):
        r"""Gets the build_duration of this Vertices.

        子任务构建耗时

        :return: The build_duration of this Vertices.
        :rtype: int
        """
        return self._build_duration

    @build_duration.setter
    def build_duration(self, build_duration):
        r"""Sets the build_duration of this Vertices.

        子任务构建耗时

        :param build_duration: The build_duration of this Vertices.
        :type build_duration: int
        """
        self._build_duration = build_duration

    @property
    def start_time(self):
        r"""Gets the start_time of this Vertices.

        子任务开始时间

        :return: The start_time of this Vertices.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this Vertices.

        子任务开始时间

        :param start_time: The start_time of this Vertices.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this Vertices.

        子任务结束时间

        :return: The finish_time of this Vertices.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this Vertices.

        子任务结束时间

        :param finish_time: The finish_time of this Vertices.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def build_no(self):
        r"""Gets the build_no of this Vertices.

        子任务构建编号

        :return: The build_no of this Vertices.
        :rtype: str
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this Vertices.

        子任务构建编号

        :param build_no: The build_no of this Vertices.
        :type build_no: str
        """
        self._build_no = build_no

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
        if not isinstance(other, Vertices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
