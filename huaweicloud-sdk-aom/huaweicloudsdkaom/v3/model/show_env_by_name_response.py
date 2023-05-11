# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEnvByNameResponse(SdkResponse):

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
        'component_id': 'str',
        'create_time': 'str',
        'creator': 'str',
        'description': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'env_tags': 'list[TagNameAndIdVo]',
        'env_type': 'str',
        'eps_id': 'str',
        'modified_time': 'str',
        'modifier': 'str',
        'os_type': 'str',
        'region': 'str',
        'register_type': 'str'
    }

    attribute_map = {
        'aom_id': 'aom_id',
        'component_id': 'component_id',
        'create_time': 'create_time',
        'creator': 'creator',
        'description': 'description',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'env_tags': 'env_tags',
        'env_type': 'env_type',
        'eps_id': 'eps_id',
        'modified_time': 'modified_time',
        'modifier': 'modifier',
        'os_type': 'os_type',
        'region': 'region',
        'register_type': 'register_type'
    }

    def __init__(self, aom_id=None, component_id=None, create_time=None, creator=None, description=None, env_id=None, env_name=None, env_tags=None, env_type=None, eps_id=None, modified_time=None, modifier=None, os_type=None, region=None, register_type=None):
        """ShowEnvByNameResponse

        The model defined in huaweicloud sdk

        :param aom_id: aomId
        :type aom_id: str
        :param component_id: 组件Id
        :type component_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator: 创建者
        :type creator: str
        :param description: 描述
        :type description: str
        :param env_id: 环境Id
        :type env_id: str
        :param env_name: 环境名称
        :type env_name: str
        :param env_tags: 环境标签
        :type env_tags: list[:class:`huaweicloudsdkaom.v3.TagNameAndIdVo`]
        :param env_type: 环境类型
        :type env_type: str
        :param eps_id: 企业项目Id
        :type eps_id: str
        :param modified_time: 修改时间
        :type modified_time: str
        :param modifier: 修改者
        :type modifier: str
        :param os_type: os类型
        :type os_type: str
        :param region: 区域
        :type region: str
        :param register_type: 注册方式
        :type register_type: str
        """
        
        super(ShowEnvByNameResponse, self).__init__()

        self._aom_id = None
        self._component_id = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._env_id = None
        self._env_name = None
        self._env_tags = None
        self._env_type = None
        self._eps_id = None
        self._modified_time = None
        self._modifier = None
        self._os_type = None
        self._region = None
        self._register_type = None
        self.discriminator = None

        if aom_id is not None:
            self.aom_id = aom_id
        if component_id is not None:
            self.component_id = component_id
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if env_tags is not None:
            self.env_tags = env_tags
        if env_type is not None:
            self.env_type = env_type
        if eps_id is not None:
            self.eps_id = eps_id
        if modified_time is not None:
            self.modified_time = modified_time
        if modifier is not None:
            self.modifier = modifier
        if os_type is not None:
            self.os_type = os_type
        if region is not None:
            self.region = region
        if register_type is not None:
            self.register_type = register_type

    @property
    def aom_id(self):
        """Gets the aom_id of this ShowEnvByNameResponse.

        aomId

        :return: The aom_id of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._aom_id

    @aom_id.setter
    def aom_id(self, aom_id):
        """Sets the aom_id of this ShowEnvByNameResponse.

        aomId

        :param aom_id: The aom_id of this ShowEnvByNameResponse.
        :type aom_id: str
        """
        self._aom_id = aom_id

    @property
    def component_id(self):
        """Gets the component_id of this ShowEnvByNameResponse.

        组件Id

        :return: The component_id of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ShowEnvByNameResponse.

        组件Id

        :param component_id: The component_id of this ShowEnvByNameResponse.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowEnvByNameResponse.

        创建时间

        :return: The create_time of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowEnvByNameResponse.

        创建时间

        :param create_time: The create_time of this ShowEnvByNameResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this ShowEnvByNameResponse.

        创建者

        :return: The creator of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowEnvByNameResponse.

        创建者

        :param creator: The creator of this ShowEnvByNameResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        """Gets the description of this ShowEnvByNameResponse.

        描述

        :return: The description of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowEnvByNameResponse.

        描述

        :param description: The description of this ShowEnvByNameResponse.
        :type description: str
        """
        self._description = description

    @property
    def env_id(self):
        """Gets the env_id of this ShowEnvByNameResponse.

        环境Id

        :return: The env_id of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ShowEnvByNameResponse.

        环境Id

        :param env_id: The env_id of this ShowEnvByNameResponse.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this ShowEnvByNameResponse.

        环境名称

        :return: The env_name of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this ShowEnvByNameResponse.

        环境名称

        :param env_name: The env_name of this ShowEnvByNameResponse.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def env_tags(self):
        """Gets the env_tags of this ShowEnvByNameResponse.

        环境标签

        :return: The env_tags of this ShowEnvByNameResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v3.TagNameAndIdVo`]
        """
        return self._env_tags

    @env_tags.setter
    def env_tags(self, env_tags):
        """Sets the env_tags of this ShowEnvByNameResponse.

        环境标签

        :param env_tags: The env_tags of this ShowEnvByNameResponse.
        :type env_tags: list[:class:`huaweicloudsdkaom.v3.TagNameAndIdVo`]
        """
        self._env_tags = env_tags

    @property
    def env_type(self):
        """Gets the env_type of this ShowEnvByNameResponse.

        环境类型

        :return: The env_type of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        """Sets the env_type of this ShowEnvByNameResponse.

        环境类型

        :param env_type: The env_type of this ShowEnvByNameResponse.
        :type env_type: str
        """
        self._env_type = env_type

    @property
    def eps_id(self):
        """Gets the eps_id of this ShowEnvByNameResponse.

        企业项目Id

        :return: The eps_id of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        """Sets the eps_id of this ShowEnvByNameResponse.

        企业项目Id

        :param eps_id: The eps_id of this ShowEnvByNameResponse.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def modified_time(self):
        """Gets the modified_time of this ShowEnvByNameResponse.

        修改时间

        :return: The modified_time of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this ShowEnvByNameResponse.

        修改时间

        :param modified_time: The modified_time of this ShowEnvByNameResponse.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def modifier(self):
        """Gets the modifier of this ShowEnvByNameResponse.

        修改者

        :return: The modifier of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this ShowEnvByNameResponse.

        修改者

        :param modifier: The modifier of this ShowEnvByNameResponse.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def os_type(self):
        """Gets the os_type of this ShowEnvByNameResponse.

        os类型

        :return: The os_type of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ShowEnvByNameResponse.

        os类型

        :param os_type: The os_type of this ShowEnvByNameResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def region(self):
        """Gets the region of this ShowEnvByNameResponse.

        区域

        :return: The region of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowEnvByNameResponse.

        区域

        :param region: The region of this ShowEnvByNameResponse.
        :type region: str
        """
        self._region = region

    @property
    def register_type(self):
        """Gets the register_type of this ShowEnvByNameResponse.

        注册方式

        :return: The register_type of this ShowEnvByNameResponse.
        :rtype: str
        """
        return self._register_type

    @register_type.setter
    def register_type(self, register_type):
        """Sets the register_type of this ShowEnvByNameResponse.

        注册方式

        :param register_type: The register_type of this ShowEnvByNameResponse.
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
        if not isinstance(other, ShowEnvByNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
