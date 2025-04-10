# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryInstanceSimplify:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_type': 'str',
        'instance_id': 'str',
        'name': 'str',
        'charge_mode': 'str',
        'flavor': 'Flavor',
        'status': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'instance_id': 'instance_id',
        'name': 'name',
        'charge_mode': 'charge_mode',
        'flavor': 'flavor',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, instance_type=None, instance_id=None, name=None, charge_mode=None, flavor=None, status=None, create_time=None, update_time=None, enterprise_project_id=None):
        r"""QueryInstanceSimplify

        The model defined in huaweicloud sdk

        :param instance_type: **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 
        :type instance_type: str
        :param instance_id: **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 
        :type instance_id: str
        :param name: **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 
        :type name: str
        :param charge_mode: **参数说明**：实例的付费方式。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费 
        :type charge_mode: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        :param status: **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 
        :type status: str
        :param create_time: **参数说明**：实例的创建时间。时间格式例如：2023-01-28T06:57:52Z 
        :type create_time: str
        :param update_time: **参数说明**：实例的最近一次更新的时间。时间格式例如：2023-01-28T06:57:52Z 
        :type update_time: str
        :param enterprise_project_id: **参数说明**：企业项目Id。
        :type enterprise_project_id: str
        """
        
        

        self._instance_type = None
        self._instance_id = None
        self._name = None
        self._charge_mode = None
        self._flavor = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._enterprise_project_id = None
        self.discriminator = None

        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this QueryInstanceSimplify.

        **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :return: The instance_type of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this QueryInstanceSimplify.

        **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :param instance_type: The instance_type of this QueryInstanceSimplify.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this QueryInstanceSimplify.

        **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :return: The instance_id of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this QueryInstanceSimplify.

        **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :param instance_id: The instance_id of this QueryInstanceSimplify.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this QueryInstanceSimplify.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :return: The name of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryInstanceSimplify.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :param name: The name of this QueryInstanceSimplify.
        :type name: str
        """
        self._name = name

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this QueryInstanceSimplify.

        **参数说明**：实例的付费方式。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费 

        :return: The charge_mode of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this QueryInstanceSimplify.

        **参数说明**：实例的付费方式。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费 

        :param charge_mode: The charge_mode of this QueryInstanceSimplify.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def flavor(self):
        r"""Gets the flavor of this QueryInstanceSimplify.

        :return: The flavor of this QueryInstanceSimplify.
        :rtype: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this QueryInstanceSimplify.

        :param flavor: The flavor of this QueryInstanceSimplify.
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        self._flavor = flavor

    @property
    def status(self):
        r"""Gets the status of this QueryInstanceSimplify.

        **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 

        :return: The status of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryInstanceSimplify.

        **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 

        :param status: The status of this QueryInstanceSimplify.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this QueryInstanceSimplify.

        **参数说明**：实例的创建时间。时间格式例如：2023-01-28T06:57:52Z 

        :return: The create_time of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QueryInstanceSimplify.

        **参数说明**：实例的创建时间。时间格式例如：2023-01-28T06:57:52Z 

        :param create_time: The create_time of this QueryInstanceSimplify.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this QueryInstanceSimplify.

        **参数说明**：实例的最近一次更新的时间。时间格式例如：2023-01-28T06:57:52Z 

        :return: The update_time of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this QueryInstanceSimplify.

        **参数说明**：实例的最近一次更新的时间。时间格式例如：2023-01-28T06:57:52Z 

        :param update_time: The update_time of this QueryInstanceSimplify.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this QueryInstanceSimplify.

        **参数说明**：企业项目Id。

        :return: The enterprise_project_id of this QueryInstanceSimplify.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this QueryInstanceSimplify.

        **参数说明**：企业项目Id。

        :param enterprise_project_id: The enterprise_project_id of this QueryInstanceSimplify.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, QueryInstanceSimplify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
