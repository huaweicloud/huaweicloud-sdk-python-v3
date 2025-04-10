# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageDetailRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'type': 'str',
        'chip_type': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'source_project_name': 'str',
        'source_project_id': 'str',
        'source_resource_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'chip_type': 'chip_type',
        'description': 'description',
        'tags': 'tags',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'source_project_name': 'source_project_name',
        'source_project_id': 'source_project_id',
        'source_resource_id': 'source_resource_id'
    }

    def __init__(self, name=None, id=None, type=None, chip_type=None, description=None, tags=None, create_time=None, update_time=None, source_project_name=None, source_project_id=None, source_resource_id=None):
        r"""ImageDetailRsp

        The model defined in huaweicloud sdk

        :param name: 镜像名称
        :type name: str
        :param id: 镜像ID
        :type id: str
        :param type: 镜像类型
        :type type: str
        :param chip_type: 镜像芯片类型
        :type chip_type: str
        :param description: 镜像描述
        :type description: str
        :param tags: 镜像版本列表
        :type tags: list[str]
        :param create_time: 镜像创建时间
        :type create_time: str
        :param update_time: 镜像更新时间
        :type update_time: str
        :param source_project_name: 源项目名称
        :type source_project_name: str
        :param source_project_id: 源项目id
        :type source_project_id: str
        :param source_resource_id: 源资源id
        :type source_resource_id: str
        """
        
        

        self._name = None
        self._id = None
        self._type = None
        self._chip_type = None
        self._description = None
        self._tags = None
        self._create_time = None
        self._update_time = None
        self._source_project_name = None
        self._source_project_id = None
        self._source_resource_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if chip_type is not None:
            self.chip_type = chip_type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if source_resource_id is not None:
            self.source_resource_id = source_resource_id

    @property
    def name(self):
        r"""Gets the name of this ImageDetailRsp.

        镜像名称

        :return: The name of this ImageDetailRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageDetailRsp.

        镜像名称

        :param name: The name of this ImageDetailRsp.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ImageDetailRsp.

        镜像ID

        :return: The id of this ImageDetailRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageDetailRsp.

        镜像ID

        :param id: The id of this ImageDetailRsp.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ImageDetailRsp.

        镜像类型

        :return: The type of this ImageDetailRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ImageDetailRsp.

        镜像类型

        :param type: The type of this ImageDetailRsp.
        :type type: str
        """
        self._type = type

    @property
    def chip_type(self):
        r"""Gets the chip_type of this ImageDetailRsp.

        镜像芯片类型

        :return: The chip_type of this ImageDetailRsp.
        :rtype: str
        """
        return self._chip_type

    @chip_type.setter
    def chip_type(self, chip_type):
        r"""Sets the chip_type of this ImageDetailRsp.

        镜像芯片类型

        :param chip_type: The chip_type of this ImageDetailRsp.
        :type chip_type: str
        """
        self._chip_type = chip_type

    @property
    def description(self):
        r"""Gets the description of this ImageDetailRsp.

        镜像描述

        :return: The description of this ImageDetailRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageDetailRsp.

        镜像描述

        :param description: The description of this ImageDetailRsp.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this ImageDetailRsp.

        镜像版本列表

        :return: The tags of this ImageDetailRsp.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ImageDetailRsp.

        镜像版本列表

        :param tags: The tags of this ImageDetailRsp.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def create_time(self):
        r"""Gets the create_time of this ImageDetailRsp.

        镜像创建时间

        :return: The create_time of this ImageDetailRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ImageDetailRsp.

        镜像创建时间

        :param create_time: The create_time of this ImageDetailRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ImageDetailRsp.

        镜像更新时间

        :return: The update_time of this ImageDetailRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ImageDetailRsp.

        镜像更新时间

        :param update_time: The update_time of this ImageDetailRsp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def source_project_name(self):
        r"""Gets the source_project_name of this ImageDetailRsp.

        源项目名称

        :return: The source_project_name of this ImageDetailRsp.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        r"""Sets the source_project_name of this ImageDetailRsp.

        源项目名称

        :param source_project_name: The source_project_name of this ImageDetailRsp.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_project_id(self):
        r"""Gets the source_project_id of this ImageDetailRsp.

        源项目id

        :return: The source_project_id of this ImageDetailRsp.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        r"""Sets the source_project_id of this ImageDetailRsp.

        源项目id

        :param source_project_id: The source_project_id of this ImageDetailRsp.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_resource_id(self):
        r"""Gets the source_resource_id of this ImageDetailRsp.

        源资源id

        :return: The source_resource_id of this ImageDetailRsp.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        r"""Sets the source_resource_id of this ImageDetailRsp.

        源资源id

        :param source_resource_id: The source_resource_id of this ImageDetailRsp.
        :type source_resource_id: str
        """
        self._source_resource_id = source_resource_id

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
        if not isinstance(other, ImageDetailRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
