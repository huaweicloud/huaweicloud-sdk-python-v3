# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlossaryInfo:

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
        'guid': 'str',
        'create_user': 'str',
        'create_time': 'float'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'guid': 'guid',
        'create_user': 'create_user',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, description=None, guid=None, create_user=None, create_time=None):
        """GlossaryInfo

        The model defined in huaweicloud sdk

        :param name: 标签名称
        :type name: str
        :param description: 描述
        :type description: str
        :param guid: 标签的guid
        :type guid: str
        :param create_user: 创建用户
        :type create_user: str
        :param create_time: 创建时间
        :type create_time: float
        """
        
        

        self._name = None
        self._description = None
        self._guid = None
        self._create_user = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if guid is not None:
            self.guid = guid
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        """Gets the name of this GlossaryInfo.

        标签名称

        :return: The name of this GlossaryInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlossaryInfo.

        标签名称

        :param name: The name of this GlossaryInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this GlossaryInfo.

        描述

        :return: The description of this GlossaryInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GlossaryInfo.

        描述

        :param description: The description of this GlossaryInfo.
        :type description: str
        """
        self._description = description

    @property
    def guid(self):
        """Gets the guid of this GlossaryInfo.

        标签的guid

        :return: The guid of this GlossaryInfo.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GlossaryInfo.

        标签的guid

        :param guid: The guid of this GlossaryInfo.
        :type guid: str
        """
        self._guid = guid

    @property
    def create_user(self):
        """Gets the create_user of this GlossaryInfo.

        创建用户

        :return: The create_user of this GlossaryInfo.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this GlossaryInfo.

        创建用户

        :param create_user: The create_user of this GlossaryInfo.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        """Gets the create_time of this GlossaryInfo.

        创建时间

        :return: The create_time of this GlossaryInfo.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GlossaryInfo.

        创建时间

        :param create_time: The create_time of this GlossaryInfo.
        :type create_time: float
        """
        self._create_time = create_time

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
        if not isinstance(other, GlossaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
