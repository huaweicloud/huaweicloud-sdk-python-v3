# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateModelDefinitionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'visibility': 'str',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'type': 'ModelType',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'current_version': 'ModelVersionInfo',
        'create_user': 'User',
        'update_user': 'User'
    }

    attribute_map = {
        'visibility': 'visibility',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'current_version': 'current_version',
        'create_user': 'create_user',
        'update_user': 'update_user'
    }

    def __init__(self, visibility=None, id=None, name=None, description=None, type=None, create_time=None, update_time=None, current_version=None, create_user=None, update_user=None):
        r"""UpdateModelDefinitionResponse

        The model defined in huaweicloud sdk

        :param visibility: 可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE
        :type visibility: str
        :param id: 模型ID，32~36位的英文、数字、短横组合
        :type id: str
        :param name: 一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.ModelType`
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param current_version: 
        :type current_version: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInfo`
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        :param update_user: 
        :type update_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        
        super(UpdateModelDefinitionResponse, self).__init__()

        self._visibility = None
        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._create_time = None
        self._update_time = None
        self._current_version = None
        self._create_user = None
        self._update_user = None
        self.discriminator = None

        if visibility is not None:
            self.visibility = visibility
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if current_version is not None:
            self.current_version = current_version
        if create_user is not None:
            self.create_user = create_user
        if update_user is not None:
            self.update_user = update_user

    @property
    def visibility(self):
        r"""Gets the visibility of this UpdateModelDefinitionResponse.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :return: The visibility of this UpdateModelDefinitionResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this UpdateModelDefinitionResponse.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :param visibility: The visibility of this UpdateModelDefinitionResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def id(self):
        r"""Gets the id of this UpdateModelDefinitionResponse.

        模型ID，32~36位的英文、数字、短横组合

        :return: The id of this UpdateModelDefinitionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateModelDefinitionResponse.

        模型ID，32~36位的英文、数字、短横组合

        :param id: The id of this UpdateModelDefinitionResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateModelDefinitionResponse.

        一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this UpdateModelDefinitionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateModelDefinitionResponse.

        一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this UpdateModelDefinitionResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateModelDefinitionResponse.

        描述信息

        :return: The description of this UpdateModelDefinitionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateModelDefinitionResponse.

        描述信息

        :param description: The description of this UpdateModelDefinitionResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this UpdateModelDefinitionResponse.

        :return: The type of this UpdateModelDefinitionResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ModelType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateModelDefinitionResponse.

        :param type: The type of this UpdateModelDefinitionResponse.
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.ModelType`
        """
        self._type = type

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateModelDefinitionResponse.

        创建时间

        :return: The create_time of this UpdateModelDefinitionResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateModelDefinitionResponse.

        创建时间

        :param create_time: The create_time of this UpdateModelDefinitionResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateModelDefinitionResponse.

        更新时间

        :return: The update_time of this UpdateModelDefinitionResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateModelDefinitionResponse.

        更新时间

        :param update_time: The update_time of this UpdateModelDefinitionResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def current_version(self):
        r"""Gets the current_version of this UpdateModelDefinitionResponse.

        :return: The current_version of this UpdateModelDefinitionResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInfo`
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this UpdateModelDefinitionResponse.

        :param current_version: The current_version of this UpdateModelDefinitionResponse.
        :type current_version: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInfo`
        """
        self._current_version = current_version

    @property
    def create_user(self):
        r"""Gets the create_user of this UpdateModelDefinitionResponse.

        :return: The create_user of this UpdateModelDefinitionResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this UpdateModelDefinitionResponse.

        :param create_user: The create_user of this UpdateModelDefinitionResponse.
        :type create_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        self._create_user = create_user

    @property
    def update_user(self):
        r"""Gets the update_user of this UpdateModelDefinitionResponse.

        :return: The update_user of this UpdateModelDefinitionResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this UpdateModelDefinitionResponse.

        :param update_user: The update_user of this UpdateModelDefinitionResponse.
        :type update_user: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        self._update_user = update_user

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
        if not isinstance(other, UpdateModelDefinitionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
