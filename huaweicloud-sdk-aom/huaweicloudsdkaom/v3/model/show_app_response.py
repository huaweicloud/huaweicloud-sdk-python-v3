# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aom_id': 'str',
        'app_id': 'str',
        'create_time': 'str',
        'creator': 'str',
        'description': 'str',
        'display_name': 'str',
        'eps_id': 'str',
        'modified_time': 'str',
        'modifier': 'str',
        'name': 'str',
        'register_type': 'str'
    }

    attribute_map = {
        'aom_id': 'aom_id',
        'app_id': 'app_id',
        'create_time': 'create_time',
        'creator': 'creator',
        'description': 'description',
        'display_name': 'display_name',
        'eps_id': 'eps_id',
        'modified_time': 'modified_time',
        'modifier': 'modifier',
        'name': 'name',
        'register_type': 'register_type'
    }

    def __init__(self, aom_id=None, app_id=None, create_time=None, creator=None, description=None, display_name=None, eps_id=None, modified_time=None, modifier=None, name=None, register_type=None):
        """ShowAppResponse

        The model defined in huaweicloud sdk

        :param aom_id: aomId，如果为空则不显示
        :type aom_id: str
        :param app_id: 应用ID
        :type app_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator: 创建人
        :type creator: str
        :param description: 描述
        :type description: str
        :param display_name: 应用名称
        :type display_name: str
        :param eps_id: 企业项目id
        :type eps_id: str
        :param modified_time: 修改时间
        :type modified_time: str
        :param modifier: 修改人
        :type modifier: str
        :param name: 唯一标识
        :type name: str
        :param register_type: 注册方式
        :type register_type: str
        """
        
        super(ShowAppResponse, self).__init__()

        self._aom_id = None
        self._app_id = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._display_name = None
        self._eps_id = None
        self._modified_time = None
        self._modifier = None
        self._name = None
        self._register_type = None
        self.discriminator = None

        if aom_id is not None:
            self.aom_id = aom_id
        if app_id is not None:
            self.app_id = app_id
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if eps_id is not None:
            self.eps_id = eps_id
        if modified_time is not None:
            self.modified_time = modified_time
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if register_type is not None:
            self.register_type = register_type

    @property
    def aom_id(self):
        """Gets the aom_id of this ShowAppResponse.

        aomId，如果为空则不显示

        :return: The aom_id of this ShowAppResponse.
        :rtype: str
        """
        return self._aom_id

    @aom_id.setter
    def aom_id(self, aom_id):
        """Sets the aom_id of this ShowAppResponse.

        aomId，如果为空则不显示

        :param aom_id: The aom_id of this ShowAppResponse.
        :type aom_id: str
        """
        self._aom_id = aom_id

    @property
    def app_id(self):
        """Gets the app_id of this ShowAppResponse.

        应用ID

        :return: The app_id of this ShowAppResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowAppResponse.

        应用ID

        :param app_id: The app_id of this ShowAppResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowAppResponse.

        创建时间

        :return: The create_time of this ShowAppResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAppResponse.

        创建时间

        :param create_time: The create_time of this ShowAppResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this ShowAppResponse.

        创建人

        :return: The creator of this ShowAppResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowAppResponse.

        创建人

        :param creator: The creator of this ShowAppResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        """Gets the description of this ShowAppResponse.

        描述

        :return: The description of this ShowAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowAppResponse.

        描述

        :param description: The description of this ShowAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this ShowAppResponse.

        应用名称

        :return: The display_name of this ShowAppResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ShowAppResponse.

        应用名称

        :param display_name: The display_name of this ShowAppResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def eps_id(self):
        """Gets the eps_id of this ShowAppResponse.

        企业项目id

        :return: The eps_id of this ShowAppResponse.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        """Sets the eps_id of this ShowAppResponse.

        企业项目id

        :param eps_id: The eps_id of this ShowAppResponse.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def modified_time(self):
        """Gets the modified_time of this ShowAppResponse.

        修改时间

        :return: The modified_time of this ShowAppResponse.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this ShowAppResponse.

        修改时间

        :param modified_time: The modified_time of this ShowAppResponse.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def modifier(self):
        """Gets the modifier of this ShowAppResponse.

        修改人

        :return: The modifier of this ShowAppResponse.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this ShowAppResponse.

        修改人

        :param modifier: The modifier of this ShowAppResponse.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this ShowAppResponse.

        唯一标识

        :return: The name of this ShowAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAppResponse.

        唯一标识

        :param name: The name of this ShowAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def register_type(self):
        """Gets the register_type of this ShowAppResponse.

        注册方式

        :return: The register_type of this ShowAppResponse.
        :rtype: str
        """
        return self._register_type

    @register_type.setter
    def register_type(self, register_type):
        """Sets the register_type of this ShowAppResponse.

        注册方式

        :param register_type: The register_type of this ShowAppResponse.
        :type register_type: str
        """
        self._register_type = register_type

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
        if not isinstance(other, ShowAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
