# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkspaceResponse(SdkResponse):

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
        'create_time': 'datetime',
        'create_domain_name': 'str',
        'create_user_name': 'str',
        'metastore_id': 'str',
        'access_url': 'str',
        'enterprise_project_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'create_domain_name': 'create_domain_name',
        'create_user_name': 'create_user_name',
        'metastore_id': 'metastore_id',
        'access_url': 'access_url',
        'enterprise_project_id': 'enterprise_project_id',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, name=None, description=None, create_time=None, create_domain_name=None, create_user_name=None, metastore_id=None, access_url=None, enterprise_project_id=None, x_request_id=None):
        r"""UpdateWorkspaceResponse

        The model defined in huaweicloud sdk

        :param id: 工作空间ID。
        :type id: str
        :param name: 工作空间名称。
        :type name: str
        :param description: 描述。用户输入的描述，最长为255个字符。
        :type description: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param create_domain_name: 创建账号名称。
        :type create_domain_name: str
        :param create_user_name: 创建用户名称。
        :type create_user_name: str
        :param metastore_id: Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。
        :type metastore_id: str
        :param access_url: 访问资源地址
        :type access_url: str
        :param enterprise_project_id: 企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。默认是0，即default
        :type enterprise_project_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateWorkspaceResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._create_time = None
        self._create_domain_name = None
        self._create_user_name = None
        self._metastore_id = None
        self._access_url = None
        self._enterprise_project_id = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if create_domain_name is not None:
            self.create_domain_name = create_domain_name
        if create_user_name is not None:
            self.create_user_name = create_user_name
        if metastore_id is not None:
            self.metastore_id = metastore_id
        if access_url is not None:
            self.access_url = access_url
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this UpdateWorkspaceResponse.

        工作空间ID。

        :return: The id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateWorkspaceResponse.

        工作空间ID。

        :param id: The id of this UpdateWorkspaceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateWorkspaceResponse.

        工作空间名称。

        :return: The name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateWorkspaceResponse.

        工作空间名称。

        :param name: The name of this UpdateWorkspaceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateWorkspaceResponse.

        描述。用户输入的描述，最长为255个字符。

        :return: The description of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateWorkspaceResponse.

        描述。用户输入的描述，最长为255个字符。

        :param description: The description of this UpdateWorkspaceResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateWorkspaceResponse.

        创建时间

        :return: The create_time of this UpdateWorkspaceResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateWorkspaceResponse.

        创建时间

        :param create_time: The create_time of this UpdateWorkspaceResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_domain_name(self):
        r"""Gets the create_domain_name of this UpdateWorkspaceResponse.

        创建账号名称。

        :return: The create_domain_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._create_domain_name

    @create_domain_name.setter
    def create_domain_name(self, create_domain_name):
        r"""Sets the create_domain_name of this UpdateWorkspaceResponse.

        创建账号名称。

        :param create_domain_name: The create_domain_name of this UpdateWorkspaceResponse.
        :type create_domain_name: str
        """
        self._create_domain_name = create_domain_name

    @property
    def create_user_name(self):
        r"""Gets the create_user_name of this UpdateWorkspaceResponse.

        创建用户名称。

        :return: The create_user_name of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._create_user_name

    @create_user_name.setter
    def create_user_name(self, create_user_name):
        r"""Sets the create_user_name of this UpdateWorkspaceResponse.

        创建用户名称。

        :param create_user_name: The create_user_name of this UpdateWorkspaceResponse.
        :type create_user_name: str
        """
        self._create_user_name = create_user_name

    @property
    def metastore_id(self):
        r"""Gets the metastore_id of this UpdateWorkspaceResponse.

        Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。

        :return: The metastore_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        r"""Sets the metastore_id of this UpdateWorkspaceResponse.

        Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。

        :param metastore_id: The metastore_id of this UpdateWorkspaceResponse.
        :type metastore_id: str
        """
        self._metastore_id = metastore_id

    @property
    def access_url(self):
        r"""Gets the access_url of this UpdateWorkspaceResponse.

        访问资源地址

        :return: The access_url of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._access_url

    @access_url.setter
    def access_url(self, access_url):
        r"""Sets the access_url of this UpdateWorkspaceResponse.

        访问资源地址

        :param access_url: The access_url of this UpdateWorkspaceResponse.
        :type access_url: str
        """
        self._access_url = access_url

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateWorkspaceResponse.

        企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。默认是0，即default

        :return: The enterprise_project_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateWorkspaceResponse.

        企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。默认是0，即default

        :param enterprise_project_id: The enterprise_project_id of this UpdateWorkspaceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateWorkspaceResponse.

        :return: The x_request_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateWorkspaceResponse.

        :param x_request_id: The x_request_id of this UpdateWorkspaceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateWorkspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
