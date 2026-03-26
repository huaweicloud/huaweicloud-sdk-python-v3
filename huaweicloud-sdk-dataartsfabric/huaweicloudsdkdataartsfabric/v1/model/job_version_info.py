# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobVersionInfo:

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
        'cap_white_list': 'list[str]',
        'description': 'str',
        'config': 'JobConfig',
        'dependence_framework': 'list[Framework]',
        'id': 'str',
        'create_user': 'User',
        'create_time': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'cap_white_list': 'cap_white_list',
        'description': 'description',
        'config': 'config',
        'dependence_framework': 'dependence_framework',
        'id': 'id',
        'create_user': 'create_user',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, cap_white_list=None, description=None, config=None, dependence_framework=None, id=None, create_user=None, create_time=None):
        r"""JobVersionInfo

        The model defined in huaweicloud sdk

        :param name: 作业版本名称,只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param cap_white_list: cap白名单
        :type cap_white_list: list[str]
        :param description: 描述信息
        :type description: str
        :param config: 
        :type config: :class:`huaweicloudsdkdataartsfabric.v1.JobConfig`
        :param dependence_framework: Framework列表信息
        :type dependence_framework: list[:class:`huaweicloudsdkdataartsfabric.v1.Framework`]
        :param id: 作业版本Id
        :type id: str
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        :param create_time: 创建时间
        :type create_time: datetime
        """
        
        

        self._name = None
        self._cap_white_list = None
        self._description = None
        self._config = None
        self._dependence_framework = None
        self._id = None
        self._create_user = None
        self._create_time = None
        self.discriminator = None

        self.name = name
        if cap_white_list is not None:
            self.cap_white_list = cap_white_list
        if description is not None:
            self.description = description
        self.config = config
        if dependence_framework is not None:
            self.dependence_framework = dependence_framework
        if id is not None:
            self.id = id
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this JobVersionInfo.

        作业版本名称,只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this JobVersionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobVersionInfo.

        作业版本名称,只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this JobVersionInfo.
        :type name: str
        """
        self._name = name

    @property
    def cap_white_list(self):
        r"""Gets the cap_white_list of this JobVersionInfo.

        cap白名单

        :return: The cap_white_list of this JobVersionInfo.
        :rtype: list[str]
        """
        return self._cap_white_list

    @cap_white_list.setter
    def cap_white_list(self, cap_white_list):
        r"""Sets the cap_white_list of this JobVersionInfo.

        cap白名单

        :param cap_white_list: The cap_white_list of this JobVersionInfo.
        :type cap_white_list: list[str]
        """
        self._cap_white_list = cap_white_list

    @property
    def description(self):
        r"""Gets the description of this JobVersionInfo.

        描述信息

        :return: The description of this JobVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this JobVersionInfo.

        描述信息

        :param description: The description of this JobVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def config(self):
        r"""Gets the config of this JobVersionInfo.

        :return: The config of this JobVersionInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.JobConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this JobVersionInfo.

        :param config: The config of this JobVersionInfo.
        :type config: :class:`huaweicloudsdkdataartsfabric.v1.JobConfig`
        """
        self._config = config

    @property
    def dependence_framework(self):
        r"""Gets the dependence_framework of this JobVersionInfo.

        Framework列表信息

        :return: The dependence_framework of this JobVersionInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.Framework`]
        """
        return self._dependence_framework

    @dependence_framework.setter
    def dependence_framework(self, dependence_framework):
        r"""Sets the dependence_framework of this JobVersionInfo.

        Framework列表信息

        :param dependence_framework: The dependence_framework of this JobVersionInfo.
        :type dependence_framework: list[:class:`huaweicloudsdkdataartsfabric.v1.Framework`]
        """
        self._dependence_framework = dependence_framework

    @property
    def id(self):
        r"""Gets the id of this JobVersionInfo.

        作业版本Id

        :return: The id of this JobVersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobVersionInfo.

        作业版本Id

        :param id: The id of this JobVersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def create_user(self):
        r"""Gets the create_user of this JobVersionInfo.

        :return: The create_user of this JobVersionInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this JobVersionInfo.

        :param create_user: The create_user of this JobVersionInfo.
        :type create_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        self._create_user = create_user

    @property
    def create_time(self):
        r"""Gets the create_time of this JobVersionInfo.

        创建时间

        :return: The create_time of this JobVersionInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobVersionInfo.

        创建时间

        :param create_time: The create_time of this JobVersionInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
