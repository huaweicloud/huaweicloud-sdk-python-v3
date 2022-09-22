# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogTargetInfo:

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
        'label': 'str',
        'description': 'str',
        'provider_type': 'str',
        'parameters': 'list[object]',
        'created_time': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'label': 'label',
        'description': 'description',
        'provider_type': 'provider_type',
        'parameters': 'parameters',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, name=None, label=None, description=None, provider_type=None, parameters=None, created_time=None, updated_time=None):
        """CatalogTargetInfo

        The model defined in huaweicloud sdk

        :param id: 事件目标分类ID
        :type id: str
        :param name: 事件目标分类名称
        :type name: str
        :param label: 事件目标分类名称展示说明
        :type label: str
        :param description: 事件目标分类描述
        :type description: str
        :param provider_type: 提供方类型，OFFICIAL：官方云服务事件目标；CUSTOM：第三方事件目标
        :type provider_type: str
        :param parameters: 
        :type parameters: list[object]
        :param created_time: 创建UTC时间
        :type created_time: str
        :param updated_time: 更新UTC时间
        :type updated_time: str
        """
        
        

        self._id = None
        self._name = None
        self._label = None
        self._description = None
        self._provider_type = None
        self._parameters = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if provider_type is not None:
            self.provider_type = provider_type
        if parameters is not None:
            self.parameters = parameters
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        """Gets the id of this CatalogTargetInfo.

        事件目标分类ID

        :return: The id of this CatalogTargetInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CatalogTargetInfo.

        事件目标分类ID

        :param id: The id of this CatalogTargetInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CatalogTargetInfo.

        事件目标分类名称

        :return: The name of this CatalogTargetInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CatalogTargetInfo.

        事件目标分类名称

        :param name: The name of this CatalogTargetInfo.
        :type name: str
        """
        self._name = name

    @property
    def label(self):
        """Gets the label of this CatalogTargetInfo.

        事件目标分类名称展示说明

        :return: The label of this CatalogTargetInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CatalogTargetInfo.

        事件目标分类名称展示说明

        :param label: The label of this CatalogTargetInfo.
        :type label: str
        """
        self._label = label

    @property
    def description(self):
        """Gets the description of this CatalogTargetInfo.

        事件目标分类描述

        :return: The description of this CatalogTargetInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CatalogTargetInfo.

        事件目标分类描述

        :param description: The description of this CatalogTargetInfo.
        :type description: str
        """
        self._description = description

    @property
    def provider_type(self):
        """Gets the provider_type of this CatalogTargetInfo.

        提供方类型，OFFICIAL：官方云服务事件目标；CUSTOM：第三方事件目标

        :return: The provider_type of this CatalogTargetInfo.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this CatalogTargetInfo.

        提供方类型，OFFICIAL：官方云服务事件目标；CUSTOM：第三方事件目标

        :param provider_type: The provider_type of this CatalogTargetInfo.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def parameters(self):
        """Gets the parameters of this CatalogTargetInfo.


        :return: The parameters of this CatalogTargetInfo.
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CatalogTargetInfo.


        :param parameters: The parameters of this CatalogTargetInfo.
        :type parameters: list[object]
        """
        self._parameters = parameters

    @property
    def created_time(self):
        """Gets the created_time of this CatalogTargetInfo.

        创建UTC时间

        :return: The created_time of this CatalogTargetInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CatalogTargetInfo.

        创建UTC时间

        :param created_time: The created_time of this CatalogTargetInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this CatalogTargetInfo.

        更新UTC时间

        :return: The updated_time of this CatalogTargetInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this CatalogTargetInfo.

        更新UTC时间

        :param updated_time: The updated_time of this CatalogTargetInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, CatalogTargetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
