# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SingleCreateSubscriptionReq:

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
        'description': 'str',
        'instance_type': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]',
        'source_endpoint_info': 'SubscriptionSourceEndpointInfo',
        'is_grant_new_agency': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'instance_type': 'instance_type',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'source_endpoint_info': 'source_endpoint_info',
        'is_grant_new_agency': 'is_grant_new_agency'
    }

    def __init__(self, name=None, description=None, instance_type=None, enterprise_project_id=None, tags=None, source_endpoint_info=None, is_grant_new_agency=None):
        r"""SingleCreateSubscriptionReq

        The model defined in huaweicloud sdk

        :param name: 任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50
        :type name: str
        :param description: 任务描述
        :type description: str
        :param instance_type: 实例类型，仅支持rds
        :type instance_type: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        :param source_endpoint_info: 
        :type source_endpoint_info: :class:`huaweicloudsdkdrs.v5.SubscriptionSourceEndpointInfo`
        :param is_grant_new_agency: 是否创建委托，取值： - true：创建 - false：不创建 默认为false
        :type is_grant_new_agency: bool
        """
        
        

        self._name = None
        self._description = None
        self._instance_type = None
        self._enterprise_project_id = None
        self._tags = None
        self._source_endpoint_info = None
        self._is_grant_new_agency = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if instance_type is not None:
            self.instance_type = instance_type
        self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        self.source_endpoint_info = source_endpoint_info
        if is_grant_new_agency is not None:
            self.is_grant_new_agency = is_grant_new_agency

    @property
    def name(self):
        r"""Gets the name of this SingleCreateSubscriptionReq.

        任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :return: The name of this SingleCreateSubscriptionReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SingleCreateSubscriptionReq.

        任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :param name: The name of this SingleCreateSubscriptionReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SingleCreateSubscriptionReq.

        任务描述

        :return: The description of this SingleCreateSubscriptionReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SingleCreateSubscriptionReq.

        任务描述

        :param description: The description of this SingleCreateSubscriptionReq.
        :type description: str
        """
        self._description = description

    @property
    def instance_type(self):
        r"""Gets the instance_type of this SingleCreateSubscriptionReq.

        实例类型，仅支持rds

        :return: The instance_type of this SingleCreateSubscriptionReq.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this SingleCreateSubscriptionReq.

        实例类型，仅支持rds

        :param instance_type: The instance_type of this SingleCreateSubscriptionReq.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SingleCreateSubscriptionReq.

        企业项目id

        :return: The enterprise_project_id of this SingleCreateSubscriptionReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SingleCreateSubscriptionReq.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this SingleCreateSubscriptionReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this SingleCreateSubscriptionReq.

        标签

        :return: The tags of this SingleCreateSubscriptionReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SingleCreateSubscriptionReq.

        标签

        :param tags: The tags of this SingleCreateSubscriptionReq.
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        self._tags = tags

    @property
    def source_endpoint_info(self):
        r"""Gets the source_endpoint_info of this SingleCreateSubscriptionReq.

        :return: The source_endpoint_info of this SingleCreateSubscriptionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.SubscriptionSourceEndpointInfo`
        """
        return self._source_endpoint_info

    @source_endpoint_info.setter
    def source_endpoint_info(self, source_endpoint_info):
        r"""Sets the source_endpoint_info of this SingleCreateSubscriptionReq.

        :param source_endpoint_info: The source_endpoint_info of this SingleCreateSubscriptionReq.
        :type source_endpoint_info: :class:`huaweicloudsdkdrs.v5.SubscriptionSourceEndpointInfo`
        """
        self._source_endpoint_info = source_endpoint_info

    @property
    def is_grant_new_agency(self):
        r"""Gets the is_grant_new_agency of this SingleCreateSubscriptionReq.

        是否创建委托，取值： - true：创建 - false：不创建 默认为false

        :return: The is_grant_new_agency of this SingleCreateSubscriptionReq.
        :rtype: bool
        """
        return self._is_grant_new_agency

    @is_grant_new_agency.setter
    def is_grant_new_agency(self, is_grant_new_agency):
        r"""Sets the is_grant_new_agency of this SingleCreateSubscriptionReq.

        是否创建委托，取值： - true：创建 - false：不创建 默认为false

        :param is_grant_new_agency: The is_grant_new_agency of this SingleCreateSubscriptionReq.
        :type is_grant_new_agency: bool
        """
        self._is_grant_new_agency = is_grant_new_agency

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
        if not isinstance(other, SingleCreateSubscriptionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
