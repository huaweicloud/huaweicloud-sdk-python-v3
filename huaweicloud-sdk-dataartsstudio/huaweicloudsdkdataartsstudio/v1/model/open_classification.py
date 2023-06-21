# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenClassification:

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
        'description': 'str',
        'create_user': 'str',
        'create_time': 'float',
        'update_time': 'float',
        'update_user': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'guid': 'guid'
    }

    def __init__(self, name=None, description=None, create_user=None, create_time=None, update_time=None, update_user=None, guid=None):
        """OpenClassification

        The model defined in huaweicloud sdk

        :param name: 分类名称
        :type name: str
        :param description: 分类描述
        :type description: str
        :param create_user: 分类创建者
        :type create_user: str
        :param create_time: 分类创建时间
        :type create_time: float
        :param update_time: 分类更新时间
        :type update_time: float
        :param update_user: 分类更新者
        :type update_user: str
        :param guid: 分类的guid标志
        :type guid: str
        """
        
        

        self._name = None
        self._description = None
        self._create_user = None
        self._create_time = None
        self._update_time = None
        self._update_user = None
        self._guid = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if guid is not None:
            self.guid = guid

    @property
    def name(self):
        """Gets the name of this OpenClassification.

        分类名称

        :return: The name of this OpenClassification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenClassification.

        分类名称

        :param name: The name of this OpenClassification.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this OpenClassification.

        分类描述

        :return: The description of this OpenClassification.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenClassification.

        分类描述

        :param description: The description of this OpenClassification.
        :type description: str
        """
        self._description = description

    @property
    def create_user(self):
        """Gets the create_user of this OpenClassification.

        分类创建者

        :return: The create_user of this OpenClassification.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this OpenClassification.

        分类创建者

        :param create_user: The create_user of this OpenClassification.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        """Gets the create_time of this OpenClassification.

        分类创建时间

        :return: The create_time of this OpenClassification.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this OpenClassification.

        分类创建时间

        :param create_time: The create_time of this OpenClassification.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this OpenClassification.

        分类更新时间

        :return: The update_time of this OpenClassification.
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this OpenClassification.

        分类更新时间

        :param update_time: The update_time of this OpenClassification.
        :type update_time: float
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this OpenClassification.

        分类更新者

        :return: The update_user of this OpenClassification.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this OpenClassification.

        分类更新者

        :param update_user: The update_user of this OpenClassification.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def guid(self):
        """Gets the guid of this OpenClassification.

        分类的guid标志

        :return: The guid of this OpenClassification.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this OpenClassification.

        分类的guid标志

        :param guid: The guid of this OpenClassification.
        :type guid: str
        """
        self._guid = guid

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
        if not isinstance(other, OpenClassification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
