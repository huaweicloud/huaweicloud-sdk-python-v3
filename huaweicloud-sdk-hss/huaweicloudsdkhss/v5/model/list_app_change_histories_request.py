# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppChangeHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_ip': 'str',
        'host_name': 'str',
        'app_name': 'str',
        'variation_type': 'str',
        'enterprise_project_id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'host_name': 'host_name',
        'app_name': 'app_name',
        'variation_type': 'variation_type',
        'enterprise_project_id': 'enterprise_project_id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, host_id=None, host_ip=None, host_name=None, app_name=None, variation_type=None, enterprise_project_id=None, sort_key=None, sort_dir=None, limit=None, offset=None, start_time=None, end_time=None):
        """ListAppChangeHistoriesRequest

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param host_name: 主机名称
        :type host_name: str
        :param app_name: 软件名称
        :type app_name: str
        :param variation_type: 变更类型:   - add ：新建   - delete ：删除   - modify ：修改
        :type variation_type: str
        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param sort_key: 排序的key值
        :type sort_key: str
        :param sort_dir: 升序还是降序，默认升序，asc
        :type sort_dir: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认是0
        :type offset: int
        :param start_time: 变更开始时间，13位时间戳
        :type start_time: int
        :param end_time: 变更结束时间，13位时间戳
        :type end_time: int
        """
        
        

        self._host_id = None
        self._host_ip = None
        self._host_name = None
        self._app_name = None
        self._variation_type = None
        self._enterprise_project_id = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
        if host_name is not None:
            self.host_name = host_name
        if app_name is not None:
            self.app_name = app_name
        if variation_type is not None:
            self.variation_type = variation_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def host_id(self):
        """Gets the host_id of this ListAppChangeHistoriesRequest.

        主机id

        :return: The host_id of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListAppChangeHistoriesRequest.

        主机id

        :param host_id: The host_id of this ListAppChangeHistoriesRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        """Gets the host_ip of this ListAppChangeHistoriesRequest.

        主机ip

        :return: The host_ip of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListAppChangeHistoriesRequest.

        主机ip

        :param host_ip: The host_ip of this ListAppChangeHistoriesRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_name(self):
        """Gets the host_name of this ListAppChangeHistoriesRequest.

        主机名称

        :return: The host_name of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListAppChangeHistoriesRequest.

        主机名称

        :param host_name: The host_name of this ListAppChangeHistoriesRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def app_name(self):
        """Gets the app_name of this ListAppChangeHistoriesRequest.

        软件名称

        :return: The app_name of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListAppChangeHistoriesRequest.

        软件名称

        :param app_name: The app_name of this ListAppChangeHistoriesRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def variation_type(self):
        """Gets the variation_type of this ListAppChangeHistoriesRequest.

        变更类型:   - add ：新建   - delete ：删除   - modify ：修改

        :return: The variation_type of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._variation_type

    @variation_type.setter
    def variation_type(self, variation_type):
        """Sets the variation_type of this ListAppChangeHistoriesRequest.

        变更类型:   - add ：新建   - delete ：删除   - modify ：修改

        :param variation_type: The variation_type of this ListAppChangeHistoriesRequest.
        :type variation_type: str
        """
        self._variation_type = variation_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAppChangeHistoriesRequest.

        企业项目

        :return: The enterprise_project_id of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAppChangeHistoriesRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ListAppChangeHistoriesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sort_key(self):
        """Gets the sort_key of this ListAppChangeHistoriesRequest.

        排序的key值

        :return: The sort_key of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListAppChangeHistoriesRequest.

        排序的key值

        :param sort_key: The sort_key of this ListAppChangeHistoriesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListAppChangeHistoriesRequest.

        升序还是降序，默认升序，asc

        :return: The sort_dir of this ListAppChangeHistoriesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListAppChangeHistoriesRequest.

        升序还是降序，默认升序，asc

        :param sort_dir: The sort_dir of this ListAppChangeHistoriesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListAppChangeHistoriesRequest.

        默认10

        :return: The limit of this ListAppChangeHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppChangeHistoriesRequest.

        默认10

        :param limit: The limit of this ListAppChangeHistoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppChangeHistoriesRequest.

        默认是0

        :return: The offset of this ListAppChangeHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppChangeHistoriesRequest.

        默认是0

        :param offset: The offset of this ListAppChangeHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def start_time(self):
        """Gets the start_time of this ListAppChangeHistoriesRequest.

        变更开始时间，13位时间戳

        :return: The start_time of this ListAppChangeHistoriesRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAppChangeHistoriesRequest.

        变更开始时间，13位时间戳

        :param start_time: The start_time of this ListAppChangeHistoriesRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAppChangeHistoriesRequest.

        变更结束时间，13位时间戳

        :return: The end_time of this ListAppChangeHistoriesRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAppChangeHistoriesRequest.

        变更结束时间，13位时间戳

        :param end_time: The end_time of this ListAppChangeHistoriesRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListAppChangeHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
