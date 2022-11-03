# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AcceleratorDetail:

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
        'status': 'ConfigStatus',
        'ip_sets': 'list[AccelerateIp]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'enterprise_project_id': 'str',
        'flavor_id': 'str',
        'frozen_info': 'FrozenInfo',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'ip_sets': 'ip_sets',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'enterprise_project_id': 'enterprise_project_id',
        'flavor_id': 'flavor_id',
        'frozen_info': 'frozen_info',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, status=None, ip_sets=None, created_at=None, updated_at=None, domain_id=None, enterprise_project_id=None, flavor_id=None, frozen_info=None, tags=None):
        """AcceleratorDetail

        The model defined in huaweicloud sdk

        :param id: 全球加速器ID。
        :type id: str
        :param name: 全球加速器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 全球加速器描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param status: 
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        :param ip_sets: 全球加速器IP列表。
        :type ip_sets: list[:class:`huaweicloudsdkga.v1.AccelerateIp`]
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        :param domain_id: 租户ID。
        :type domain_id: str
        :param enterprise_project_id: 租户的企业项目ID。
        :type enterprise_project_id: str
        :param flavor_id: 规格ID。
        :type flavor_id: str
        :param frozen_info: 
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._ip_sets = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._enterprise_project_id = None
        self._flavor_id = None
        self._frozen_info = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if ip_sets is not None:
            self.ip_sets = ip_sets
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if domain_id is not None:
            self.domain_id = domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if frozen_info is not None:
            self.frozen_info = frozen_info
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this AcceleratorDetail.

        全球加速器ID。

        :return: The id of this AcceleratorDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AcceleratorDetail.

        全球加速器ID。

        :param id: The id of this AcceleratorDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AcceleratorDetail.

        全球加速器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this AcceleratorDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AcceleratorDetail.

        全球加速器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this AcceleratorDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AcceleratorDetail.

        全球加速器描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this AcceleratorDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AcceleratorDetail.

        全球加速器描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this AcceleratorDetail.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this AcceleratorDetail.


        :return: The status of this AcceleratorDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AcceleratorDetail.


        :param status: The status of this AcceleratorDetail.
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        self._status = status

    @property
    def ip_sets(self):
        """Gets the ip_sets of this AcceleratorDetail.

        全球加速器IP列表。

        :return: The ip_sets of this AcceleratorDetail.
        :rtype: list[:class:`huaweicloudsdkga.v1.AccelerateIp`]
        """
        return self._ip_sets

    @ip_sets.setter
    def ip_sets(self, ip_sets):
        """Sets the ip_sets of this AcceleratorDetail.

        全球加速器IP列表。

        :param ip_sets: The ip_sets of this AcceleratorDetail.
        :type ip_sets: list[:class:`huaweicloudsdkga.v1.AccelerateIp`]
        """
        self._ip_sets = ip_sets

    @property
    def created_at(self):
        """Gets the created_at of this AcceleratorDetail.

        创建时间。

        :return: The created_at of this AcceleratorDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AcceleratorDetail.

        创建时间。

        :param created_at: The created_at of this AcceleratorDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AcceleratorDetail.

        更新时间。

        :return: The updated_at of this AcceleratorDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AcceleratorDetail.

        更新时间。

        :param updated_at: The updated_at of this AcceleratorDetail.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this AcceleratorDetail.

        租户ID。

        :return: The domain_id of this AcceleratorDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AcceleratorDetail.

        租户ID。

        :param domain_id: The domain_id of this AcceleratorDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AcceleratorDetail.

        租户的企业项目ID。

        :return: The enterprise_project_id of this AcceleratorDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AcceleratorDetail.

        租户的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this AcceleratorDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this AcceleratorDetail.

        规格ID。

        :return: The flavor_id of this AcceleratorDetail.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this AcceleratorDetail.

        规格ID。

        :param flavor_id: The flavor_id of this AcceleratorDetail.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def frozen_info(self):
        """Gets the frozen_info of this AcceleratorDetail.


        :return: The frozen_info of this AcceleratorDetail.
        :rtype: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        return self._frozen_info

    @frozen_info.setter
    def frozen_info(self, frozen_info):
        """Sets the frozen_info of this AcceleratorDetail.


        :param frozen_info: The frozen_info of this AcceleratorDetail.
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        self._frozen_info = frozen_info

    @property
    def tags(self):
        """Gets the tags of this AcceleratorDetail.

        标签列表。

        :return: The tags of this AcceleratorDetail.
        :rtype: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AcceleratorDetail.

        标签列表。

        :param tags: The tags of this AcceleratorDetail.
        :type tags: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, AcceleratorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
