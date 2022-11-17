# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipPoolShowResp:

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
        'status': 'str',
        'type': 'str',
        'description': 'str',
        'project_id': 'str',
        'size': 'int',
        'used': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'billing_info': 'BillingInfoDict',
        'public_border_group': 'str',
        'shared': 'bool',
        'is_common': 'bool',
        'tags': 'list[TagsInfo]',
        'enterprise_project_id': 'str',
        'allow_share_bandwidth_types': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'description': 'description',
        'project_id': 'project_id',
        'size': 'size',
        'used': 'used',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'billing_info': 'billing_info',
        'public_border_group': 'public_border_group',
        'shared': 'shared',
        'is_common': 'is_common',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'allow_share_bandwidth_types': 'allow_share_bandwidth_types'
    }

    def __init__(self, id=None, name=None, status=None, type=None, description=None, project_id=None, size=None, used=None, created_at=None, updated_at=None, billing_info=None, public_border_group=None, shared=None, is_common=None, tags=None, enterprise_project_id=None, allow_share_bandwidth_types=None):
        """PublicipPoolShowResp

        The model defined in huaweicloud sdk

        :param id: 公网IP池id
        :type id: str
        :param name: 公网IP池名字
        :type name: str
        :param status: 状态
        :type status: str
        :param type: 取值, spec_bgp(专属离散动态), spec_sbgp(专属离散静态)
        :type type: str
        :param description: 描述
        :type description: str
        :param project_id: 租户id
        :type project_id: str
        :param size: 池子大小
        :type size: int
        :param used: 已经使用的ip数量
        :type used: int
        :param created_at: 公网IP池创建时间
        :type created_at: str
        :param updated_at: 公网IP池更新时间
        :type updated_at: str
        :param billing_info: 
        :type billing_info: :class:`huaweicloudsdkeip.v3.BillingInfoDict`
        :param public_border_group: 功能说明：中心还是边缘。公网IP池取值为center
        :type public_border_group: str
        :param shared: 功能说明：是否共享
        :type shared: bool
        :param is_common: 功能说明：是否公共池
        :type is_common: bool
        :param tags: 默认不显示。用户标签
        :type tags: list[:class:`huaweicloudsdkeip.v3.TagsInfo`]
        :param enterprise_project_id: 功能说明：企业项目ID。最大长度36字节,带“-”连字符的UUID格式,或者是字符串“0”。创建弹性公网IP时,给弹性公网IP绑定企业项目ID。
        :type enterprise_project_id: str
        :param allow_share_bandwidth_types: 功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中
        :type allow_share_bandwidth_types: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._type = None
        self._description = None
        self._project_id = None
        self._size = None
        self._used = None
        self._created_at = None
        self._updated_at = None
        self._billing_info = None
        self._public_border_group = None
        self._shared = None
        self._is_common = None
        self._tags = None
        self._enterprise_project_id = None
        self._allow_share_bandwidth_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if size is not None:
            self.size = size
        if used is not None:
            self.used = used
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if billing_info is not None:
            self.billing_info = billing_info
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if shared is not None:
            self.shared = shared
        if is_common is not None:
            self.is_common = is_common
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if allow_share_bandwidth_types is not None:
            self.allow_share_bandwidth_types = allow_share_bandwidth_types

    @property
    def id(self):
        """Gets the id of this PublicipPoolShowResp.

        公网IP池id

        :return: The id of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicipPoolShowResp.

        公网IP池id

        :param id: The id of this PublicipPoolShowResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PublicipPoolShowResp.

        公网IP池名字

        :return: The name of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicipPoolShowResp.

        公网IP池名字

        :param name: The name of this PublicipPoolShowResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this PublicipPoolShowResp.

        状态

        :return: The status of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicipPoolShowResp.

        状态

        :param status: The status of this PublicipPoolShowResp.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this PublicipPoolShowResp.

        取值, spec_bgp(专属离散动态), spec_sbgp(专属离散静态)

        :return: The type of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicipPoolShowResp.

        取值, spec_bgp(专属离散动态), spec_sbgp(专属离散静态)

        :param type: The type of this PublicipPoolShowResp.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this PublicipPoolShowResp.

        描述

        :return: The description of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublicipPoolShowResp.

        描述

        :param description: The description of this PublicipPoolShowResp.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this PublicipPoolShowResp.

        租户id

        :return: The project_id of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PublicipPoolShowResp.

        租户id

        :param project_id: The project_id of this PublicipPoolShowResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def size(self):
        """Gets the size of this PublicipPoolShowResp.

        池子大小

        :return: The size of this PublicipPoolShowResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PublicipPoolShowResp.

        池子大小

        :param size: The size of this PublicipPoolShowResp.
        :type size: int
        """
        self._size = size

    @property
    def used(self):
        """Gets the used of this PublicipPoolShowResp.

        已经使用的ip数量

        :return: The used of this PublicipPoolShowResp.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this PublicipPoolShowResp.

        已经使用的ip数量

        :param used: The used of this PublicipPoolShowResp.
        :type used: int
        """
        self._used = used

    @property
    def created_at(self):
        """Gets the created_at of this PublicipPoolShowResp.

        公网IP池创建时间

        :return: The created_at of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublicipPoolShowResp.

        公网IP池创建时间

        :param created_at: The created_at of this PublicipPoolShowResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PublicipPoolShowResp.

        公网IP池更新时间

        :return: The updated_at of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PublicipPoolShowResp.

        公网IP池更新时间

        :param updated_at: The updated_at of this PublicipPoolShowResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def billing_info(self):
        """Gets the billing_info of this PublicipPoolShowResp.

        :return: The billing_info of this PublicipPoolShowResp.
        :rtype: :class:`huaweicloudsdkeip.v3.BillingInfoDict`
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this PublicipPoolShowResp.

        :param billing_info: The billing_info of this PublicipPoolShowResp.
        :type billing_info: :class:`huaweicloudsdkeip.v3.BillingInfoDict`
        """
        self._billing_info = billing_info

    @property
    def public_border_group(self):
        """Gets the public_border_group of this PublicipPoolShowResp.

        功能说明：中心还是边缘。公网IP池取值为center

        :return: The public_border_group of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this PublicipPoolShowResp.

        功能说明：中心还是边缘。公网IP池取值为center

        :param public_border_group: The public_border_group of this PublicipPoolShowResp.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def shared(self):
        """Gets the shared of this PublicipPoolShowResp.

        功能说明：是否共享

        :return: The shared of this PublicipPoolShowResp.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this PublicipPoolShowResp.

        功能说明：是否共享

        :param shared: The shared of this PublicipPoolShowResp.
        :type shared: bool
        """
        self._shared = shared

    @property
    def is_common(self):
        """Gets the is_common of this PublicipPoolShowResp.

        功能说明：是否公共池

        :return: The is_common of this PublicipPoolShowResp.
        :rtype: bool
        """
        return self._is_common

    @is_common.setter
    def is_common(self, is_common):
        """Sets the is_common of this PublicipPoolShowResp.

        功能说明：是否公共池

        :param is_common: The is_common of this PublicipPoolShowResp.
        :type is_common: bool
        """
        self._is_common = is_common

    @property
    def tags(self):
        """Gets the tags of this PublicipPoolShowResp.

        默认不显示。用户标签

        :return: The tags of this PublicipPoolShowResp.
        :rtype: list[:class:`huaweicloudsdkeip.v3.TagsInfo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PublicipPoolShowResp.

        默认不显示。用户标签

        :param tags: The tags of this PublicipPoolShowResp.
        :type tags: list[:class:`huaweicloudsdkeip.v3.TagsInfo`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PublicipPoolShowResp.

        功能说明：企业项目ID。最大长度36字节,带“-”连字符的UUID格式,或者是字符串“0”。创建弹性公网IP时,给弹性公网IP绑定企业项目ID。

        :return: The enterprise_project_id of this PublicipPoolShowResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PublicipPoolShowResp.

        功能说明：企业项目ID。最大长度36字节,带“-”连字符的UUID格式,或者是字符串“0”。创建弹性公网IP时,给弹性公网IP绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this PublicipPoolShowResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def allow_share_bandwidth_types(self):
        """Gets the allow_share_bandwidth_types of this PublicipPoolShowResp.

        功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :return: The allow_share_bandwidth_types of this PublicipPoolShowResp.
        :rtype: list[str]
        """
        return self._allow_share_bandwidth_types

    @allow_share_bandwidth_types.setter
    def allow_share_bandwidth_types(self, allow_share_bandwidth_types):
        """Sets the allow_share_bandwidth_types of this PublicipPoolShowResp.

        功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :param allow_share_bandwidth_types: The allow_share_bandwidth_types of this PublicipPoolShowResp.
        :type allow_share_bandwidth_types: list[str]
        """
        self._allow_share_bandwidth_types = allow_share_bandwidth_types

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
        if not isinstance(other, PublicipPoolShowResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
