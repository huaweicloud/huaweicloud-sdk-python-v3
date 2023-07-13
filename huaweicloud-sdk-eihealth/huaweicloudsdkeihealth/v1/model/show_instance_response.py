# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceResponse(SdkResponse):

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
        'name': 'str',
        'description': 'str',
        'template': 'TemplateRsp',
        'creator': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'data_count': 'int',
        'source_project_name': 'str',
        'source_project_id': 'str',
        'source_id': 'str',
        'is_prefab': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'template': 'template',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'data_count': 'data_count',
        'source_project_name': 'source_project_name',
        'source_project_id': 'source_project_id',
        'source_id': 'source_id',
        'is_prefab': 'is_prefab'
    }

    def __init__(self, id=None, name=None, description=None, template=None, creator=None, create_time=None, update_time=None, data_count=None, source_project_name=None, source_project_id=None, source_id=None, is_prefab=None):
        """ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param name: 实例名称
        :type name: str
        :param description: 描述
        :type description: str
        :param template: 
        :type template: :class:`huaweicloudsdkeihealth.v1.TemplateRsp`
        :param creator: 创建者
        :type creator: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param data_count: 数据条目
        :type data_count: int
        :param source_project_name: 源项目名
        :type source_project_name: str
        :param source_project_id: 源项目id
        :type source_project_id: str
        :param source_id: 源实例id
        :type source_id: str
        :param is_prefab: 是否为预置实例
        :type is_prefab: bool
        """
        
        super(ShowInstanceResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._template = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._data_count = None
        self._source_project_name = None
        self._source_project_id = None
        self._source_id = None
        self._is_prefab = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if template is not None:
            self.template = template
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if data_count is not None:
            self.data_count = data_count
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if source_id is not None:
            self.source_id = source_id
        if is_prefab is not None:
            self.is_prefab = is_prefab

    @property
    def id(self):
        """Gets the id of this ShowInstanceResponse.

        实例id

        :return: The id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowInstanceResponse.

        实例id

        :param id: The id of this ShowInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowInstanceResponse.

        实例名称

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowInstanceResponse.

        实例名称

        :param name: The name of this ShowInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowInstanceResponse.

        描述

        :return: The description of this ShowInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowInstanceResponse.

        描述

        :param description: The description of this ShowInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def template(self):
        """Gets the template of this ShowInstanceResponse.

        :return: The template of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TemplateRsp`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ShowInstanceResponse.

        :param template: The template of this ShowInstanceResponse.
        :type template: :class:`huaweicloudsdkeihealth.v1.TemplateRsp`
        """
        self._template = template

    @property
    def creator(self):
        """Gets the creator of this ShowInstanceResponse.

        创建者

        :return: The creator of this ShowInstanceResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowInstanceResponse.

        创建者

        :param creator: The creator of this ShowInstanceResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this ShowInstanceResponse.

        创建时间

        :return: The create_time of this ShowInstanceResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowInstanceResponse.

        创建时间

        :param create_time: The create_time of this ShowInstanceResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowInstanceResponse.

        更新时间

        :return: The update_time of this ShowInstanceResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowInstanceResponse.

        更新时间

        :param update_time: The update_time of this ShowInstanceResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def data_count(self):
        """Gets the data_count of this ShowInstanceResponse.

        数据条目

        :return: The data_count of this ShowInstanceResponse.
        :rtype: int
        """
        return self._data_count

    @data_count.setter
    def data_count(self, data_count):
        """Sets the data_count of this ShowInstanceResponse.

        数据条目

        :param data_count: The data_count of this ShowInstanceResponse.
        :type data_count: int
        """
        self._data_count = data_count

    @property
    def source_project_name(self):
        """Gets the source_project_name of this ShowInstanceResponse.

        源项目名

        :return: The source_project_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        """Sets the source_project_name of this ShowInstanceResponse.

        源项目名

        :param source_project_name: The source_project_name of this ShowInstanceResponse.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_project_id(self):
        """Gets the source_project_id of this ShowInstanceResponse.

        源项目id

        :return: The source_project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this ShowInstanceResponse.

        源项目id

        :param source_project_id: The source_project_id of this ShowInstanceResponse.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_id(self):
        """Gets the source_id of this ShowInstanceResponse.

        源实例id

        :return: The source_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ShowInstanceResponse.

        源实例id

        :param source_id: The source_id of this ShowInstanceResponse.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def is_prefab(self):
        """Gets the is_prefab of this ShowInstanceResponse.

        是否为预置实例

        :return: The is_prefab of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._is_prefab

    @is_prefab.setter
    def is_prefab(self, is_prefab):
        """Sets the is_prefab of this ShowInstanceResponse.

        是否为预置实例

        :param is_prefab: The is_prefab of this ShowInstanceResponse.
        :type is_prefab: bool
        """
        self._is_prefab = is_prefab

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
        if not isinstance(other, ShowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
