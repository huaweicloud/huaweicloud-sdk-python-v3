# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentResponse(SdkResponse):

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
        'id': 'str',
        'modified_time': 'str',
        'modifier': 'str',
        'name': 'str',
        'register_type': 'str',
        'sub_app_id': 'str'
    }

    attribute_map = {
        'aom_id': 'aom_id',
        'app_id': 'app_id',
        'create_time': 'create_time',
        'creator': 'creator',
        'description': 'description',
        'id': 'id',
        'modified_time': 'modified_time',
        'modifier': 'modifier',
        'name': 'name',
        'register_type': 'register_type',
        'sub_app_id': 'sub_app_id'
    }

    def __init__(self, aom_id=None, app_id=None, create_time=None, creator=None, description=None, id=None, modified_time=None, modifier=None, name=None, register_type=None, sub_app_id=None):
        r"""ShowComponentResponse

        The model defined in huaweicloud sdk

        :param aom_id: aomId
        :type aom_id: str
        :param app_id: 应用id
        :type app_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator: 创建者
        :type creator: str
        :param description: 描述
        :type description: str
        :param id: 组件Id
        :type id: str
        :param modified_time: 修改时间
        :type modified_time: str
        :param modifier: 修改者
        :type modifier: str
        :param name: 组件名称
        :type name: str
        :param register_type: 注册方式
        :type register_type: str
        :param sub_app_id: 子应用id
        :type sub_app_id: str
        """
        
        super(ShowComponentResponse, self).__init__()

        self._aom_id = None
        self._app_id = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._id = None
        self._modified_time = None
        self._modifier = None
        self._name = None
        self._register_type = None
        self._sub_app_id = None
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
        if id is not None:
            self.id = id
        if modified_time is not None:
            self.modified_time = modified_time
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if register_type is not None:
            self.register_type = register_type
        if sub_app_id is not None:
            self.sub_app_id = sub_app_id

    @property
    def aom_id(self):
        r"""Gets the aom_id of this ShowComponentResponse.

        aomId

        :return: The aom_id of this ShowComponentResponse.
        :rtype: str
        """
        return self._aom_id

    @aom_id.setter
    def aom_id(self, aom_id):
        r"""Sets the aom_id of this ShowComponentResponse.

        aomId

        :param aom_id: The aom_id of this ShowComponentResponse.
        :type aom_id: str
        """
        self._aom_id = aom_id

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowComponentResponse.

        应用id

        :return: The app_id of this ShowComponentResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowComponentResponse.

        应用id

        :param app_id: The app_id of this ShowComponentResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowComponentResponse.

        创建时间

        :return: The create_time of this ShowComponentResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowComponentResponse.

        创建时间

        :param create_time: The create_time of this ShowComponentResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this ShowComponentResponse.

        创建者

        :return: The creator of this ShowComponentResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowComponentResponse.

        创建者

        :param creator: The creator of this ShowComponentResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        r"""Gets the description of this ShowComponentResponse.

        描述

        :return: The description of this ShowComponentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowComponentResponse.

        描述

        :param description: The description of this ShowComponentResponse.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this ShowComponentResponse.

        组件Id

        :return: The id of this ShowComponentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowComponentResponse.

        组件Id

        :param id: The id of this ShowComponentResponse.
        :type id: str
        """
        self._id = id

    @property
    def modified_time(self):
        r"""Gets the modified_time of this ShowComponentResponse.

        修改时间

        :return: The modified_time of this ShowComponentResponse.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this ShowComponentResponse.

        修改时间

        :param modified_time: The modified_time of this ShowComponentResponse.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def modifier(self):
        r"""Gets the modifier of this ShowComponentResponse.

        修改者

        :return: The modifier of this ShowComponentResponse.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this ShowComponentResponse.

        修改者

        :param modifier: The modifier of this ShowComponentResponse.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        r"""Gets the name of this ShowComponentResponse.

        组件名称

        :return: The name of this ShowComponentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowComponentResponse.

        组件名称

        :param name: The name of this ShowComponentResponse.
        :type name: str
        """
        self._name = name

    @property
    def register_type(self):
        r"""Gets the register_type of this ShowComponentResponse.

        注册方式

        :return: The register_type of this ShowComponentResponse.
        :rtype: str
        """
        return self._register_type

    @register_type.setter
    def register_type(self, register_type):
        r"""Sets the register_type of this ShowComponentResponse.

        注册方式

        :param register_type: The register_type of this ShowComponentResponse.
        :type register_type: str
        """
        self._register_type = register_type

    @property
    def sub_app_id(self):
        r"""Gets the sub_app_id of this ShowComponentResponse.

        子应用id

        :return: The sub_app_id of this ShowComponentResponse.
        :rtype: str
        """
        return self._sub_app_id

    @sub_app_id.setter
    def sub_app_id(self, sub_app_id):
        r"""Sets the sub_app_id of this ShowComponentResponse.

        子应用id

        :param sub_app_id: The sub_app_id of this ShowComponentResponse.
        :type sub_app_id: str
        """
        self._sub_app_id = sub_app_id

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
        if not isinstance(other, ShowComponentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
