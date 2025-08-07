# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryPendingItemsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'submit_user_name': 'str',
        'item_name': 'str',
        'update_type': 'str',
        'task_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'submit_user_name': 'submit_user_name',
        'item_name': 'item_name',
        'update_type': 'update_type',
        'task_type': 'task_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, x_project_id=None, submit_user_name=None, item_name=None, update_type=None, task_type=None, start_time=None, end_time=None, limit=None, offset=None):
        r"""ListFactoryPendingItemsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param submit_user_name: 提交人。
        :type submit_user_name: str
        :param item_name: 任务名称。
        :type item_name: str
        :param update_type: 变更类型。
        :type update_type: str
        :param task_type: 任务类型。
        :type task_type: str
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param limit: 分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10
        :type limit: int
        :param offset: 分页列表的页数，默认值为0。取值范围大于等于0。
        :type offset: int
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._submit_user_name = None
        self._item_name = None
        self._update_type = None
        self._task_type = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if submit_user_name is not None:
            self.submit_user_name = submit_user_name
        if item_name is not None:
            self.item_name = item_name
        if update_type is not None:
            self.update_type = update_type
        if task_type is not None:
            self.task_type = task_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        r"""Gets the workspace of this ListFactoryPendingItemsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListFactoryPendingItemsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListFactoryPendingItemsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListFactoryPendingItemsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListFactoryPendingItemsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListFactoryPendingItemsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def submit_user_name(self):
        r"""Gets the submit_user_name of this ListFactoryPendingItemsRequest.

        提交人。

        :return: The submit_user_name of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._submit_user_name

    @submit_user_name.setter
    def submit_user_name(self, submit_user_name):
        r"""Sets the submit_user_name of this ListFactoryPendingItemsRequest.

        提交人。

        :param submit_user_name: The submit_user_name of this ListFactoryPendingItemsRequest.
        :type submit_user_name: str
        """
        self._submit_user_name = submit_user_name

    @property
    def item_name(self):
        r"""Gets the item_name of this ListFactoryPendingItemsRequest.

        任务名称。

        :return: The item_name of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        r"""Sets the item_name of this ListFactoryPendingItemsRequest.

        任务名称。

        :param item_name: The item_name of this ListFactoryPendingItemsRequest.
        :type item_name: str
        """
        self._item_name = item_name

    @property
    def update_type(self):
        r"""Gets the update_type of this ListFactoryPendingItemsRequest.

        变更类型。

        :return: The update_type of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this ListFactoryPendingItemsRequest.

        变更类型。

        :param update_type: The update_type of this ListFactoryPendingItemsRequest.
        :type update_type: str
        """
        self._update_type = update_type

    @property
    def task_type(self):
        r"""Gets the task_type of this ListFactoryPendingItemsRequest.

        任务类型。

        :return: The task_type of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListFactoryPendingItemsRequest.

        任务类型。

        :param task_type: The task_type of this ListFactoryPendingItemsRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListFactoryPendingItemsRequest.

        开始时间。

        :return: The start_time of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListFactoryPendingItemsRequest.

        开始时间。

        :param start_time: The start_time of this ListFactoryPendingItemsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListFactoryPendingItemsRequest.

        结束时间。

        :return: The end_time of this ListFactoryPendingItemsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListFactoryPendingItemsRequest.

        结束时间。

        :param end_time: The end_time of this ListFactoryPendingItemsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListFactoryPendingItemsRequest.

        分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10

        :return: The limit of this ListFactoryPendingItemsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFactoryPendingItemsRequest.

        分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10

        :param limit: The limit of this ListFactoryPendingItemsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListFactoryPendingItemsRequest.

        分页列表的页数，默认值为0。取值范围大于等于0。

        :return: The offset of this ListFactoryPendingItemsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFactoryPendingItemsRequest.

        分页列表的页数，默认值为0。取值范围大于等于0。

        :param offset: The offset of this ListFactoryPendingItemsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListFactoryPendingItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
