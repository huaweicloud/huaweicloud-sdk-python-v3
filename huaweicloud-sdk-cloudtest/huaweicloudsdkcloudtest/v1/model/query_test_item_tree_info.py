# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTestItemTreeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'stage': 'str',
        'activity': 'str',
        'version_uri': 'str',
        'task_uri': 'str',
        'service_type': 'str',
        'contain_total': 'bool',
        'project_uuid': 'str',
        'sort_type': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'owner': 'owner',
        'stage': 'stage',
        'activity': 'activity',
        'version_uri': 'version_uri',
        'task_uri': 'task_uri',
        'service_type': 'service_type',
        'contain_total': 'contain_total',
        'project_uuid': 'project_uuid',
        'sort_type': 'sort_type',
        'page_number': 'page_number',
        'page_size': 'page_size'
    }

    def __init__(self, owner=None, stage=None, activity=None, version_uri=None, task_uri=None, service_type=None, contain_total=None, project_uuid=None, sort_type=None, page_number=None, page_size=None):
        r"""QueryTestItemTreeInfo

        The model defined in huaweicloud sdk

        :param owner: 责任人
        :type owner: str
        :param stage: 阶段
        :type stage: str
        :param activity: 活动
        :type activity: str
        :param version_uri: 版本URI
        :type version_uri: str
        :param task_uri: 任务uri
        :type task_uri: str
        :param service_type: 用例服务类型
        :type service_type: str
        :param contain_total: 是否包含用例数
        :type contain_total: bool
        :param project_uuid: 项目id
        :type project_uuid: str
        :param sort_type: 排序类型
        :type sort_type: str
        :param page_number: 页码
        :type page_number: int
        :param page_size: 每页数量
        :type page_size: int
        """
        
        

        self._owner = None
        self._stage = None
        self._activity = None
        self._version_uri = None
        self._task_uri = None
        self._service_type = None
        self._contain_total = None
        self._project_uuid = None
        self._sort_type = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if stage is not None:
            self.stage = stage
        if activity is not None:
            self.activity = activity
        if version_uri is not None:
            self.version_uri = version_uri
        if task_uri is not None:
            self.task_uri = task_uri
        if service_type is not None:
            self.service_type = service_type
        if contain_total is not None:
            self.contain_total = contain_total
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if sort_type is not None:
            self.sort_type = sort_type
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def owner(self):
        r"""Gets the owner of this QueryTestItemTreeInfo.

        责任人

        :return: The owner of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this QueryTestItemTreeInfo.

        责任人

        :param owner: The owner of this QueryTestItemTreeInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def stage(self):
        r"""Gets the stage of this QueryTestItemTreeInfo.

        阶段

        :return: The stage of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this QueryTestItemTreeInfo.

        阶段

        :param stage: The stage of this QueryTestItemTreeInfo.
        :type stage: str
        """
        self._stage = stage

    @property
    def activity(self):
        r"""Gets the activity of this QueryTestItemTreeInfo.

        活动

        :return: The activity of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        r"""Sets the activity of this QueryTestItemTreeInfo.

        活动

        :param activity: The activity of this QueryTestItemTreeInfo.
        :type activity: str
        """
        self._activity = activity

    @property
    def version_uri(self):
        r"""Gets the version_uri of this QueryTestItemTreeInfo.

        版本URI

        :return: The version_uri of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this QueryTestItemTreeInfo.

        版本URI

        :param version_uri: The version_uri of this QueryTestItemTreeInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def task_uri(self):
        r"""Gets the task_uri of this QueryTestItemTreeInfo.

        任务uri

        :return: The task_uri of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this QueryTestItemTreeInfo.

        任务uri

        :param task_uri: The task_uri of this QueryTestItemTreeInfo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def service_type(self):
        r"""Gets the service_type of this QueryTestItemTreeInfo.

        用例服务类型

        :return: The service_type of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this QueryTestItemTreeInfo.

        用例服务类型

        :param service_type: The service_type of this QueryTestItemTreeInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def contain_total(self):
        r"""Gets the contain_total of this QueryTestItemTreeInfo.

        是否包含用例数

        :return: The contain_total of this QueryTestItemTreeInfo.
        :rtype: bool
        """
        return self._contain_total

    @contain_total.setter
    def contain_total(self, contain_total):
        r"""Sets the contain_total of this QueryTestItemTreeInfo.

        是否包含用例数

        :param contain_total: The contain_total of this QueryTestItemTreeInfo.
        :type contain_total: bool
        """
        self._contain_total = contain_total

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this QueryTestItemTreeInfo.

        项目id

        :return: The project_uuid of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this QueryTestItemTreeInfo.

        项目id

        :param project_uuid: The project_uuid of this QueryTestItemTreeInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def sort_type(self):
        r"""Gets the sort_type of this QueryTestItemTreeInfo.

        排序类型

        :return: The sort_type of this QueryTestItemTreeInfo.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this QueryTestItemTreeInfo.

        排序类型

        :param sort_type: The sort_type of this QueryTestItemTreeInfo.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def page_number(self):
        r"""Gets the page_number of this QueryTestItemTreeInfo.

        页码

        :return: The page_number of this QueryTestItemTreeInfo.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this QueryTestItemTreeInfo.

        页码

        :param page_number: The page_number of this QueryTestItemTreeInfo.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        r"""Gets the page_size of this QueryTestItemTreeInfo.

        每页数量

        :return: The page_size of this QueryTestItemTreeInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this QueryTestItemTreeInfo.

        每页数量

        :param page_size: The page_size of this QueryTestItemTreeInfo.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, QueryTestItemTreeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
