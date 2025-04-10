# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelInfo:

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
        'provider_type': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'provider_type': 'provider_type',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, description=None, provider_type=None, created_time=None, updated_time=None, enterprise_project_id=None):
        r"""ChannelInfo

        The model defined in huaweicloud sdk

        :param id: 通道ID
        :type id: str
        :param name: 通道名称
        :type name: str
        :param description: 通道描述
        :type description: str
        :param provider_type: 通道提供方类型，OFFICIAL：官方事件通道；CUSTOM：自定义事件通道；PARTNER：伙伴事件通道
        :type provider_type: str
        :param created_time: 创建UTC时间
        :type created_time: str
        :param updated_time: 更新UTC时间
        :type updated_time: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._provider_type = None
        self._created_time = None
        self._updated_time = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if provider_type is not None:
            self.provider_type = provider_type
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ChannelInfo.

        通道ID

        :return: The id of this ChannelInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChannelInfo.

        通道ID

        :param id: The id of this ChannelInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ChannelInfo.

        通道名称

        :return: The name of this ChannelInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChannelInfo.

        通道名称

        :param name: The name of this ChannelInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ChannelInfo.

        通道描述

        :return: The description of this ChannelInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChannelInfo.

        通道描述

        :param description: The description of this ChannelInfo.
        :type description: str
        """
        self._description = description

    @property
    def provider_type(self):
        r"""Gets the provider_type of this ChannelInfo.

        通道提供方类型，OFFICIAL：官方事件通道；CUSTOM：自定义事件通道；PARTNER：伙伴事件通道

        :return: The provider_type of this ChannelInfo.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this ChannelInfo.

        通道提供方类型，OFFICIAL：官方事件通道；CUSTOM：自定义事件通道；PARTNER：伙伴事件通道

        :param provider_type: The provider_type of this ChannelInfo.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def created_time(self):
        r"""Gets the created_time of this ChannelInfo.

        创建UTC时间

        :return: The created_time of this ChannelInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ChannelInfo.

        创建UTC时间

        :param created_time: The created_time of this ChannelInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ChannelInfo.

        更新UTC时间

        :return: The updated_time of this ChannelInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ChannelInfo.

        更新UTC时间

        :param updated_time: The updated_time of this ChannelInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChannelInfo.

        企业项目id

        :return: The enterprise_project_id of this ChannelInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChannelInfo.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ChannelInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ChannelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
