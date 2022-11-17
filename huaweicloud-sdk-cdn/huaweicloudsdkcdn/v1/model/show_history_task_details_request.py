# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHistoryTaskDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'history_tasks_id': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'status': 'str',
        'url': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'history_tasks_id': 'history_tasks_id',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'status': 'status',
        'url': 'url',
        'create_time': 'create_time'
    }

    def __init__(self, enterprise_project_id=None, history_tasks_id=None, page_size=None, page_number=None, status=None, url=None, create_time=None):
        """ShowHistoryTaskDetailsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        :param history_tasks_id: 刷新任务ID。
        :type history_tasks_id: str
        :param page_size: 刷新预热的urls所显示单页最大数量，取值范围为1-10000。page_size和page_number必须同时传值。默认值30。
        :type page_size: int
        :param page_number: 刷新预热的urls当前查询为第几页，取值范围为1-65535。默认值1。
        :type page_number: int
        :param status: url的状态 processing 处理中，succeed 完成，failed 失败，waiting 等待，refreshing 刷新中，preheating 预热中。
        :type status: str
        :param url: url的地址。
        :type url: str
        :param create_time: 刷新预热任务的创建时间。不传参默认为查询7天内的任务。最长可查询15天内数据。
        :type create_time: int
        """
        
        

        self._enterprise_project_id = None
        self._history_tasks_id = None
        self._page_size = None
        self._page_number = None
        self._status = None
        self._url = None
        self._create_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.history_tasks_id = history_tasks_id
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if create_time is not None:
            self.create_time = create_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowHistoryTaskDetailsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this ShowHistoryTaskDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowHistoryTaskDetailsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ShowHistoryTaskDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def history_tasks_id(self):
        """Gets the history_tasks_id of this ShowHistoryTaskDetailsRequest.

        刷新任务ID。

        :return: The history_tasks_id of this ShowHistoryTaskDetailsRequest.
        :rtype: str
        """
        return self._history_tasks_id

    @history_tasks_id.setter
    def history_tasks_id(self, history_tasks_id):
        """Sets the history_tasks_id of this ShowHistoryTaskDetailsRequest.

        刷新任务ID。

        :param history_tasks_id: The history_tasks_id of this ShowHistoryTaskDetailsRequest.
        :type history_tasks_id: str
        """
        self._history_tasks_id = history_tasks_id

    @property
    def page_size(self):
        """Gets the page_size of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls所显示单页最大数量，取值范围为1-10000。page_size和page_number必须同时传值。默认值30。

        :return: The page_size of this ShowHistoryTaskDetailsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls所显示单页最大数量，取值范围为1-10000。page_size和page_number必须同时传值。默认值30。

        :param page_size: The page_size of this ShowHistoryTaskDetailsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls当前查询为第几页，取值范围为1-65535。默认值1。

        :return: The page_number of this ShowHistoryTaskDetailsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ShowHistoryTaskDetailsRequest.

        刷新预热的urls当前查询为第几页，取值范围为1-65535。默认值1。

        :param page_number: The page_number of this ShowHistoryTaskDetailsRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def status(self):
        """Gets the status of this ShowHistoryTaskDetailsRequest.

        url的状态 processing 处理中，succeed 完成，failed 失败，waiting 等待，refreshing 刷新中，preheating 预热中。

        :return: The status of this ShowHistoryTaskDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHistoryTaskDetailsRequest.

        url的状态 processing 处理中，succeed 完成，failed 失败，waiting 等待，refreshing 刷新中，preheating 预热中。

        :param status: The status of this ShowHistoryTaskDetailsRequest.
        :type status: str
        """
        self._status = status

    @property
    def url(self):
        """Gets the url of this ShowHistoryTaskDetailsRequest.

        url的地址。

        :return: The url of this ShowHistoryTaskDetailsRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowHistoryTaskDetailsRequest.

        url的地址。

        :param url: The url of this ShowHistoryTaskDetailsRequest.
        :type url: str
        """
        self._url = url

    @property
    def create_time(self):
        """Gets the create_time of this ShowHistoryTaskDetailsRequest.

        刷新预热任务的创建时间。不传参默认为查询7天内的任务。最长可查询15天内数据。

        :return: The create_time of this ShowHistoryTaskDetailsRequest.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowHistoryTaskDetailsRequest.

        刷新预热任务的创建时间。不传参默认为查询7天内的任务。最长可查询15天内数据。

        :param create_time: The create_time of this ShowHistoryTaskDetailsRequest.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowHistoryTaskDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
