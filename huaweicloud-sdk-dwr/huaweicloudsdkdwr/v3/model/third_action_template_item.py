# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThirdActionTemplateItem:

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
        'category': 'str',
        'register_status': 'PublicTemplateRegisterType',
        'provider_name': 'str',
        'description': 'str',
        'create_time': 'str',
        'last_modify_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'category': 'category',
        'register_status': 'register_status',
        'provider_name': 'provider_name',
        'description': 'description',
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time'
    }

    def __init__(self, name=None, category=None, register_status=None, provider_name=None, description=None, create_time=None, last_modify_time=None):
        """ThirdActionTemplateItem

        The model defined in huaweicloud sdk

        :param name: 名称。
        :type name: str
        :param category: 算子分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction
        :type category: str
        :param register_status: 
        :type register_status: :class:`huaweicloudsdkdwr.v3.PublicTemplateRegisterType`
        :param provider_name: 算子提供方
        :type provider_name: str
        :param description: 算子描述
        :type description: str
        :param create_time: 算子创建时间
        :type create_time: str
        :param last_modify_time: 最后修改时间
        :type last_modify_time: str
        """
        
        

        self._name = None
        self._category = None
        self._register_status = None
        self._provider_name = None
        self._description = None
        self._create_time = None
        self._last_modify_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if register_status is not None:
            self.register_status = register_status
        if provider_name is not None:
            self.provider_name = provider_name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time

    @property
    def name(self):
        """Gets the name of this ThirdActionTemplateItem.

        名称。

        :return: The name of this ThirdActionTemplateItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThirdActionTemplateItem.

        名称。

        :param name: The name of this ThirdActionTemplateItem.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        """Gets the category of this ThirdActionTemplateItem.

        算子分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction

        :return: The category of this ThirdActionTemplateItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ThirdActionTemplateItem.

        算子分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction

        :param category: The category of this ThirdActionTemplateItem.
        :type category: str
        """
        self._category = category

    @property
    def register_status(self):
        """Gets the register_status of this ThirdActionTemplateItem.

        :return: The register_status of this ThirdActionTemplateItem.
        :rtype: :class:`huaweicloudsdkdwr.v3.PublicTemplateRegisterType`
        """
        return self._register_status

    @register_status.setter
    def register_status(self, register_status):
        """Sets the register_status of this ThirdActionTemplateItem.

        :param register_status: The register_status of this ThirdActionTemplateItem.
        :type register_status: :class:`huaweicloudsdkdwr.v3.PublicTemplateRegisterType`
        """
        self._register_status = register_status

    @property
    def provider_name(self):
        """Gets the provider_name of this ThirdActionTemplateItem.

        算子提供方

        :return: The provider_name of this ThirdActionTemplateItem.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ThirdActionTemplateItem.

        算子提供方

        :param provider_name: The provider_name of this ThirdActionTemplateItem.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def description(self):
        """Gets the description of this ThirdActionTemplateItem.

        算子描述

        :return: The description of this ThirdActionTemplateItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThirdActionTemplateItem.

        算子描述

        :param description: The description of this ThirdActionTemplateItem.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this ThirdActionTemplateItem.

        算子创建时间

        :return: The create_time of this ThirdActionTemplateItem.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ThirdActionTemplateItem.

        算子创建时间

        :param create_time: The create_time of this ThirdActionTemplateItem.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        """Gets the last_modify_time of this ThirdActionTemplateItem.

        最后修改时间

        :return: The last_modify_time of this ThirdActionTemplateItem.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        """Sets the last_modify_time of this ThirdActionTemplateItem.

        最后修改时间

        :param last_modify_time: The last_modify_time of this ThirdActionTemplateItem.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

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
        if not isinstance(other, ThirdActionTemplateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
