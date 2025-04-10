# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelVersionInfo:

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
        'cap_white_list': 'list[str]',
        'description': 'str',
        'config': 'ModelConfig',
        'create_time': 'datetime',
        'create_user': 'User'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cap_white_list': 'cap_white_list',
        'description': 'description',
        'config': 'config',
        'create_time': 'create_time',
        'create_user': 'create_user'
    }

    def __init__(self, id=None, name=None, cap_white_list=None, description=None, config=None, create_time=None, create_user=None):
        r"""ModelVersionInfo

        The model defined in huaweicloud sdk

        :param id: 模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。
        :type id: str
        :param name: 模型版本名称, 只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param cap_white_list: cap白名单
        :type cap_white_list: list[str]
        :param description: 描述信息
        :type description: str
        :param config: 
        :type config: :class:`huaweicloudsdkdataartsfabric.v1.ModelConfig`
        :param create_time: 创建时间
        :type create_time: datetime
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        
        

        self._id = None
        self._name = None
        self._cap_white_list = None
        self._description = None
        self._config = None
        self._create_time = None
        self._create_user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if cap_white_list is not None:
            self.cap_white_list = cap_white_list
        if description is not None:
            self.description = description
        self.config = config
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user

    @property
    def id(self):
        r"""Gets the id of this ModelVersionInfo.

        模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。

        :return: The id of this ModelVersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelVersionInfo.

        模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。

        :param id: The id of this ModelVersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModelVersionInfo.

        模型版本名称, 只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this ModelVersionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelVersionInfo.

        模型版本名称, 只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this ModelVersionInfo.
        :type name: str
        """
        self._name = name

    @property
    def cap_white_list(self):
        r"""Gets the cap_white_list of this ModelVersionInfo.

        cap白名单

        :return: The cap_white_list of this ModelVersionInfo.
        :rtype: list[str]
        """
        return self._cap_white_list

    @cap_white_list.setter
    def cap_white_list(self, cap_white_list):
        r"""Sets the cap_white_list of this ModelVersionInfo.

        cap白名单

        :param cap_white_list: The cap_white_list of this ModelVersionInfo.
        :type cap_white_list: list[str]
        """
        self._cap_white_list = cap_white_list

    @property
    def description(self):
        r"""Gets the description of this ModelVersionInfo.

        描述信息

        :return: The description of this ModelVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelVersionInfo.

        描述信息

        :param description: The description of this ModelVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def config(self):
        r"""Gets the config of this ModelVersionInfo.

        :return: The config of this ModelVersionInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ModelConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this ModelVersionInfo.

        :param config: The config of this ModelVersionInfo.
        :type config: :class:`huaweicloudsdkdataartsfabric.v1.ModelConfig`
        """
        self._config = config

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelVersionInfo.

        创建时间

        :return: The create_time of this ModelVersionInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelVersionInfo.

        创建时间

        :param create_time: The create_time of this ModelVersionInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ModelVersionInfo.

        :return: The create_user of this ModelVersionInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ModelVersionInfo.

        :param create_user: The create_user of this ModelVersionInfo.
        :type create_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        self._create_user = create_user

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
        if not isinstance(other, ModelVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
