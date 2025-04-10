# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppInfoResponse(SdkResponse):

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
        'app_key': 'str',
        'app_secret': 'str',
        'register_time': 'int',
        'update_time': 'int',
        'create_user': 'str',
        'update_user': 'str',
        'app_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'app_key': 'app_key',
        'app_secret': 'app_secret',
        'register_time': 'register_time',
        'update_time': 'update_time',
        'create_user': 'create_user',
        'update_user': 'update_user',
        'app_type': 'app_type'
    }

    def __init__(self, id=None, name=None, description=None, app_key=None, app_secret=None, register_time=None, update_time=None, create_user=None, update_user=None, app_type=None):
        r"""ShowAppInfoResponse

        The model defined in huaweicloud sdk

        :param id: 应用编号
        :type id: str
        :param name: 应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param app_key: 应用key
        :type app_key: str
        :param app_secret: 应用secret
        :type app_secret: str
        :param register_time: 创建时间
        :type register_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param create_user: 创建者
        :type create_user: str
        :param update_user: 更新者
        :type update_user: str
        :param app_type: 应用类型
        :type app_type: str
        """
        
        super(ShowAppInfoResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._app_key = None
        self._app_secret = None
        self._register_time = None
        self._update_time = None
        self._create_user = None
        self._update_user = None
        self._app_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if app_key is not None:
            self.app_key = app_key
        if app_secret is not None:
            self.app_secret = app_secret
        if register_time is not None:
            self.register_time = register_time
        if update_time is not None:
            self.update_time = update_time
        if create_user is not None:
            self.create_user = create_user
        if update_user is not None:
            self.update_user = update_user
        if app_type is not None:
            self.app_type = app_type

    @property
    def id(self):
        r"""Gets the id of this ShowAppInfoResponse.

        应用编号

        :return: The id of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAppInfoResponse.

        应用编号

        :param id: The id of this ShowAppInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowAppInfoResponse.

        应用名称

        :return: The name of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAppInfoResponse.

        应用名称

        :param name: The name of this ShowAppInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowAppInfoResponse.

        应用描述

        :return: The description of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowAppInfoResponse.

        应用描述

        :param description: The description of this ShowAppInfoResponse.
        :type description: str
        """
        self._description = description

    @property
    def app_key(self):
        r"""Gets the app_key of this ShowAppInfoResponse.

        应用key

        :return: The app_key of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this ShowAppInfoResponse.

        应用key

        :param app_key: The app_key of this ShowAppInfoResponse.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_secret(self):
        r"""Gets the app_secret of this ShowAppInfoResponse.

        应用secret

        :return: The app_secret of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        r"""Sets the app_secret of this ShowAppInfoResponse.

        应用secret

        :param app_secret: The app_secret of this ShowAppInfoResponse.
        :type app_secret: str
        """
        self._app_secret = app_secret

    @property
    def register_time(self):
        r"""Gets the register_time of this ShowAppInfoResponse.

        创建时间

        :return: The register_time of this ShowAppInfoResponse.
        :rtype: int
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        r"""Sets the register_time of this ShowAppInfoResponse.

        创建时间

        :param register_time: The register_time of this ShowAppInfoResponse.
        :type register_time: int
        """
        self._register_time = register_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAppInfoResponse.

        更新时间

        :return: The update_time of this ShowAppInfoResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAppInfoResponse.

        更新时间

        :param update_time: The update_time of this ShowAppInfoResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowAppInfoResponse.

        创建者

        :return: The create_user of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowAppInfoResponse.

        创建者

        :param create_user: The create_user of this ShowAppInfoResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_user(self):
        r"""Gets the update_user of this ShowAppInfoResponse.

        更新者

        :return: The update_user of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this ShowAppInfoResponse.

        更新者

        :param update_user: The update_user of this ShowAppInfoResponse.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def app_type(self):
        r"""Gets the app_type of this ShowAppInfoResponse.

        应用类型

        :return: The app_type of this ShowAppInfoResponse.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ShowAppInfoResponse.

        应用类型

        :param app_type: The app_type of this ShowAppInfoResponse.
        :type app_type: str
        """
        self._app_type = app_type

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
        if not isinstance(other, ShowAppInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
