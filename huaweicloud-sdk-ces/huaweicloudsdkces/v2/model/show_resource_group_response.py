# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'create_time': 'datetime',
        'enterprise_project_id': 'str',
        'type': 'str',
        'association_ep_ids': 'list[str]',
        'tags': 'list[ResourceGroupTagRelation]',
        'instances': 'list[Instance]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'association_ep_ids': 'association_ep_ids',
        'tags': 'tags',
        'instances': 'instances'
    }

    def __init__(self, group_name=None, group_id=None, create_time=None, enterprise_project_id=None, type=None, association_ep_ids=None, tags=None, instances=None):
        r"""ShowResourceGroupResponse

        The model defined in huaweicloud sdk

        :param group_name: 资源分组的名称
        :type group_name: str
        :param group_id: 资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串
        :type group_id: str
        :param create_time: 资源分组的创建时间
        :type create_time: datetime
        :param enterprise_project_id: 资源分组归属企业项目ID
        :type enterprise_project_id: str
        :param type: 资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加）
        :type type: str
        :param association_ep_ids: 该资源分组内包含的资源来源的企业项目ID，type为EPS时必传
        :type association_ep_ids: list[str]
        :param tags: 标签动态匹配时的关联标签,type为TAG时该字段不为空
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        :param instances: 实例名称匹配参数
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        
        super(ShowResourceGroupResponse, self).__init__()

        self._group_name = None
        self._group_id = None
        self._create_time = None
        self._enterprise_project_id = None
        self._type = None
        self._association_ep_ids = None
        self._tags = None
        self._instances = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if association_ep_ids is not None:
            self.association_ep_ids = association_ep_ids
        if tags is not None:
            self.tags = tags
        if instances is not None:
            self.instances = instances

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowResourceGroupResponse.

        资源分组的名称

        :return: The group_name of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowResourceGroupResponse.

        资源分组的名称

        :param group_name: The group_name of this ShowResourceGroupResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowResourceGroupResponse.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :return: The group_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowResourceGroupResponse.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :param group_id: The group_id of this ShowResourceGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowResourceGroupResponse.

        资源分组的创建时间

        :return: The create_time of this ShowResourceGroupResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowResourceGroupResponse.

        资源分组的创建时间

        :param create_time: The create_time of this ShowResourceGroupResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowResourceGroupResponse.

        资源分组归属企业项目ID

        :return: The enterprise_project_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowResourceGroupResponse.

        资源分组归属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowResourceGroupResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ShowResourceGroupResponse.

        资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加）

        :return: The type of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowResourceGroupResponse.

        资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加）

        :param type: The type of this ShowResourceGroupResponse.
        :type type: str
        """
        self._type = type

    @property
    def association_ep_ids(self):
        r"""Gets the association_ep_ids of this ShowResourceGroupResponse.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :return: The association_ep_ids of this ShowResourceGroupResponse.
        :rtype: list[str]
        """
        return self._association_ep_ids

    @association_ep_ids.setter
    def association_ep_ids(self, association_ep_ids):
        r"""Sets the association_ep_ids of this ShowResourceGroupResponse.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :param association_ep_ids: The association_ep_ids of this ShowResourceGroupResponse.
        :type association_ep_ids: list[str]
        """
        self._association_ep_ids = association_ep_ids

    @property
    def tags(self):
        r"""Gets the tags of this ShowResourceGroupResponse.

        标签动态匹配时的关联标签,type为TAG时该字段不为空

        :return: The tags of this ShowResourceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowResourceGroupResponse.

        标签动态匹配时的关联标签,type为TAG时该字段不为空

        :param tags: The tags of this ShowResourceGroupResponse.
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        self._tags = tags

    @property
    def instances(self):
        r"""Gets the instances of this ShowResourceGroupResponse.

        实例名称匹配参数

        :return: The instances of this ShowResourceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ShowResourceGroupResponse.

        实例名称匹配参数

        :param instances: The instances of this ShowResourceGroupResponse.
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        self._instances = instances

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
        if not isinstance(other, ShowResourceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
