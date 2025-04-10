# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApisRequest:

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
        'dlm_type': 'str',
        'x_return_publish_messages': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'description': 'str',
        'create_user': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'tags': 'list[str]',
        'api_type': 'str',
        'publish_status': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'x_return_publish_messages': 'x-return-publish-messages',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'description': 'description',
        'create_user': 'create_user',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'tags': 'tags',
        'api_type': 'api_type',
        'publish_status': 'publish_status',
        'table_name': 'table_name'
    }

    def __init__(self, workspace=None, dlm_type=None, x_return_publish_messages=None, offset=None, limit=None, name=None, description=None, create_user=None, start_time=None, end_time=None, tags=None, api_type=None, publish_status=None, table_name=None):
        r"""ListApisRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param x_return_publish_messages: 是否返回专享版API的发布信息。
        :type x_return_publish_messages: str
        :param offset: 查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。
        :type offset: int
        :param limit: 查询条数, 即查询Y条数据。
        :type limit: int
        :param name: 根据API名称模糊查询。
        :type name: str
        :param description: 根据API描述信息模糊查询。
        :type description: str
        :param create_user: 根据API创建用户模糊查询。
        :type create_user: str
        :param start_time: 根据API创建时间过滤，开始时间，如2024-02-24T16:00:00.000Z。
        :type start_time: str
        :param end_time: 根据API创建时间过滤，结束时间，如2024-04-05T15:59:59.998Z。
        :type end_time: str
        :param tags: 标签。
        :type tags: list[str]
        :param api_type: API类型。
        :type api_type: str
        :param publish_status: API发布状态。
        :type publish_status: str
        :param table_name: 根据API用到的数据库表名模糊查询。
        :type table_name: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._x_return_publish_messages = None
        self._offset = None
        self._limit = None
        self._name = None
        self._description = None
        self._create_user = None
        self._start_time = None
        self._end_time = None
        self._tags = None
        self._api_type = None
        self._publish_status = None
        self._table_name = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        if x_return_publish_messages is not None:
            self.x_return_publish_messages = x_return_publish_messages
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_user is not None:
            self.create_user = create_user
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if tags is not None:
            self.tags = tags
        if api_type is not None:
            self.api_type = api_type
        if publish_status is not None:
            self.publish_status = publish_status
        if table_name is not None:
            self.table_name = table_name

    @property
    def workspace(self):
        r"""Gets the workspace of this ListApisRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListApisRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListApisRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListApisRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this ListApisRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this ListApisRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this ListApisRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this ListApisRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def x_return_publish_messages(self):
        r"""Gets the x_return_publish_messages of this ListApisRequest.

        是否返回专享版API的发布信息。

        :return: The x_return_publish_messages of this ListApisRequest.
        :rtype: str
        """
        return self._x_return_publish_messages

    @x_return_publish_messages.setter
    def x_return_publish_messages(self, x_return_publish_messages):
        r"""Sets the x_return_publish_messages of this ListApisRequest.

        是否返回专享版API的发布信息。

        :param x_return_publish_messages: The x_return_publish_messages of this ListApisRequest.
        :type x_return_publish_messages: str
        """
        self._x_return_publish_messages = x_return_publish_messages

    @property
    def offset(self):
        r"""Gets the offset of this ListApisRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :return: The offset of this ListApisRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListApisRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :param offset: The offset of this ListApisRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListApisRequest.

        查询条数, 即查询Y条数据。

        :return: The limit of this ListApisRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApisRequest.

        查询条数, 即查询Y条数据。

        :param limit: The limit of this ListApisRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListApisRequest.

        根据API名称模糊查询。

        :return: The name of this ListApisRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListApisRequest.

        根据API名称模糊查询。

        :param name: The name of this ListApisRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListApisRequest.

        根据API描述信息模糊查询。

        :return: The description of this ListApisRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListApisRequest.

        根据API描述信息模糊查询。

        :param description: The description of this ListApisRequest.
        :type description: str
        """
        self._description = description

    @property
    def create_user(self):
        r"""Gets the create_user of this ListApisRequest.

        根据API创建用户模糊查询。

        :return: The create_user of this ListApisRequest.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ListApisRequest.

        根据API创建用户模糊查询。

        :param create_user: The create_user of this ListApisRequest.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def start_time(self):
        r"""Gets the start_time of this ListApisRequest.

        根据API创建时间过滤，开始时间，如2024-02-24T16:00:00.000Z。

        :return: The start_time of this ListApisRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListApisRequest.

        根据API创建时间过滤，开始时间，如2024-02-24T16:00:00.000Z。

        :param start_time: The start_time of this ListApisRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListApisRequest.

        根据API创建时间过滤，结束时间，如2024-04-05T15:59:59.998Z。

        :return: The end_time of this ListApisRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListApisRequest.

        根据API创建时间过滤，结束时间，如2024-04-05T15:59:59.998Z。

        :param end_time: The end_time of this ListApisRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def tags(self):
        r"""Gets the tags of this ListApisRequest.

        标签。

        :return: The tags of this ListApisRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListApisRequest.

        标签。

        :param tags: The tags of this ListApisRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def api_type(self):
        r"""Gets the api_type of this ListApisRequest.

        API类型。

        :return: The api_type of this ListApisRequest.
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this ListApisRequest.

        API类型。

        :param api_type: The api_type of this ListApisRequest.
        :type api_type: str
        """
        self._api_type = api_type

    @property
    def publish_status(self):
        r"""Gets the publish_status of this ListApisRequest.

        API发布状态。

        :return: The publish_status of this ListApisRequest.
        :rtype: str
        """
        return self._publish_status

    @publish_status.setter
    def publish_status(self, publish_status):
        r"""Sets the publish_status of this ListApisRequest.

        API发布状态。

        :param publish_status: The publish_status of this ListApisRequest.
        :type publish_status: str
        """
        self._publish_status = publish_status

    @property
    def table_name(self):
        r"""Gets the table_name of this ListApisRequest.

        根据API用到的数据库表名模糊查询。

        :return: The table_name of this ListApisRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListApisRequest.

        根据API用到的数据库表名模糊查询。

        :param table_name: The table_name of this ListApisRequest.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, ListApisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
