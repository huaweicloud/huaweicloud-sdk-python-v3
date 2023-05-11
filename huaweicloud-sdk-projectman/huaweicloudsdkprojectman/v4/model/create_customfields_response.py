# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomfieldsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'options': 'str',
        'region': 'str',
        'id': 'int',
        'identifier': 'str',
        'project_id': 'int',
        'tracker_id': 'int',
        'custom_field': 'str',
        'type': 'str',
        'name': 'str',
        'sort': 'int',
        'memo': 'str',
        'created': 'str',
        'modified': 'str',
        'is_delete': 'bool'
    }

    attribute_map = {
        'options': 'options',
        'region': 'region',
        'id': 'id',
        'identifier': 'identifier',
        'project_id': 'project_id',
        'tracker_id': 'tracker_id',
        'custom_field': 'custom_field',
        'type': 'type',
        'name': 'name',
        'sort': 'sort',
        'memo': 'memo',
        'created': 'created',
        'modified': 'modified',
        'is_delete': 'is_delete'
    }

    def __init__(self, options=None, region=None, id=None, identifier=None, project_id=None, tracker_id=None, custom_field=None, type=None, name=None, sort=None, memo=None, created=None, modified=None, is_delete=None):
        """CreateCustomfieldsResponse

        The model defined in huaweicloud sdk

        :param options: 字段选项
        :type options: str
        :param region: 系统字段
        :type region: str
        :param id: 字段ID
        :type id: int
        :param identifier: 字段ID
        :type identifier: str
        :param project_id: 项目ID
        :type project_id: int
        :param tracker_id: 工作项类型id 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story
        :type tracker_id: int
        :param custom_field: 系统字段名
        :type custom_field: str
        :param type: 字段类型
        :type type: str
        :param name: 字段名称
        :type name: str
        :param sort: 系统字段
        :type sort: int
        :param memo: 字段描述
        :type memo: str
        :param created: 创建时间
        :type created: str
        :param modified: 修改时间
        :type modified: str
        :param is_delete: 是否被删除
        :type is_delete: bool
        """
        
        super(CreateCustomfieldsResponse, self).__init__()

        self._options = None
        self._region = None
        self._id = None
        self._identifier = None
        self._project_id = None
        self._tracker_id = None
        self._custom_field = None
        self._type = None
        self._name = None
        self._sort = None
        self._memo = None
        self._created = None
        self._modified = None
        self._is_delete = None
        self.discriminator = None

        if options is not None:
            self.options = options
        if region is not None:
            self.region = region
        if id is not None:
            self.id = id
        if identifier is not None:
            self.identifier = identifier
        if project_id is not None:
            self.project_id = project_id
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if custom_field is not None:
            self.custom_field = custom_field
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if sort is not None:
            self.sort = sort
        if memo is not None:
            self.memo = memo
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if is_delete is not None:
            self.is_delete = is_delete

    @property
    def options(self):
        """Gets the options of this CreateCustomfieldsResponse.

        字段选项

        :return: The options of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CreateCustomfieldsResponse.

        字段选项

        :param options: The options of this CreateCustomfieldsResponse.
        :type options: str
        """
        self._options = options

    @property
    def region(self):
        """Gets the region of this CreateCustomfieldsResponse.

        系统字段

        :return: The region of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateCustomfieldsResponse.

        系统字段

        :param region: The region of this CreateCustomfieldsResponse.
        :type region: str
        """
        self._region = region

    @property
    def id(self):
        """Gets the id of this CreateCustomfieldsResponse.

        字段ID

        :return: The id of this CreateCustomfieldsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateCustomfieldsResponse.

        字段ID

        :param id: The id of this CreateCustomfieldsResponse.
        :type id: int
        """
        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this CreateCustomfieldsResponse.

        字段ID

        :return: The identifier of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this CreateCustomfieldsResponse.

        字段ID

        :param identifier: The identifier of this CreateCustomfieldsResponse.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def project_id(self):
        """Gets the project_id of this CreateCustomfieldsResponse.

        项目ID

        :return: The project_id of this CreateCustomfieldsResponse.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateCustomfieldsResponse.

        项目ID

        :param project_id: The project_id of this CreateCustomfieldsResponse.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def tracker_id(self):
        """Gets the tracker_id of this CreateCustomfieldsResponse.

        工作项类型id 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story

        :return: The tracker_id of this CreateCustomfieldsResponse.
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this CreateCustomfieldsResponse.

        工作项类型id 2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story

        :param tracker_id: The tracker_id of this CreateCustomfieldsResponse.
        :type tracker_id: int
        """
        self._tracker_id = tracker_id

    @property
    def custom_field(self):
        """Gets the custom_field of this CreateCustomfieldsResponse.

        系统字段名

        :return: The custom_field of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this CreateCustomfieldsResponse.

        系统字段名

        :param custom_field: The custom_field of this CreateCustomfieldsResponse.
        :type custom_field: str
        """
        self._custom_field = custom_field

    @property
    def type(self):
        """Gets the type of this CreateCustomfieldsResponse.

        字段类型

        :return: The type of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCustomfieldsResponse.

        字段类型

        :param type: The type of this CreateCustomfieldsResponse.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this CreateCustomfieldsResponse.

        字段名称

        :return: The name of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCustomfieldsResponse.

        字段名称

        :param name: The name of this CreateCustomfieldsResponse.
        :type name: str
        """
        self._name = name

    @property
    def sort(self):
        """Gets the sort of this CreateCustomfieldsResponse.

        系统字段

        :return: The sort of this CreateCustomfieldsResponse.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this CreateCustomfieldsResponse.

        系统字段

        :param sort: The sort of this CreateCustomfieldsResponse.
        :type sort: int
        """
        self._sort = sort

    @property
    def memo(self):
        """Gets the memo of this CreateCustomfieldsResponse.

        字段描述

        :return: The memo of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this CreateCustomfieldsResponse.

        字段描述

        :param memo: The memo of this CreateCustomfieldsResponse.
        :type memo: str
        """
        self._memo = memo

    @property
    def created(self):
        """Gets the created of this CreateCustomfieldsResponse.

        创建时间

        :return: The created of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreateCustomfieldsResponse.

        创建时间

        :param created: The created of this CreateCustomfieldsResponse.
        :type created: str
        """
        self._created = created

    @property
    def modified(self):
        """Gets the modified of this CreateCustomfieldsResponse.

        修改时间

        :return: The modified of this CreateCustomfieldsResponse.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this CreateCustomfieldsResponse.

        修改时间

        :param modified: The modified of this CreateCustomfieldsResponse.
        :type modified: str
        """
        self._modified = modified

    @property
    def is_delete(self):
        """Gets the is_delete of this CreateCustomfieldsResponse.

        是否被删除

        :return: The is_delete of this CreateCustomfieldsResponse.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        """Sets the is_delete of this CreateCustomfieldsResponse.

        是否被删除

        :param is_delete: The is_delete of this CreateCustomfieldsResponse.
        :type is_delete: bool
        """
        self._is_delete = is_delete

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
        if not isinstance(other, CreateCustomfieldsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
