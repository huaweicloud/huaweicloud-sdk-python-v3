# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePoolRequestBody:

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
        'region': 'str',
        'type': 'str',
        'vpc_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'region': 'region',
        'type': 'type',
        'vpc_id': 'vpc_id',
        'description': 'description'
    }

    def __init__(self, name=None, region=None, type=None, vpc_id=None, description=None):
        r"""CreatePoolRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 实例组名称，用于标识实例组，便于管理和识别。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字、下划线、中划线和点组成，且长度为1~256个字符 **默认取值：** 不涉及
        :type name: str
        :param region: **参数解释：** 实例组所在的区域（Region）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type region: str
        :param type: **参数解释：** 实例组类型 **约束限制：** 不涉及 **取值范围：** - elb: 基础elb类型 - elb-v2: elb-v2类型 - elb-shadow: saas化elb类型 - standard-container: 反向代理独享引擎组（云内，承载租户专用） - standard-cloud: 反向代理独享引擎组（云内） - standard: 反向代理独享引擎组（云外） - detector-cloud: 旁路检测独享引擎组（云内） - detector: 旁路检测独享引擎组（云外） **默认取值：** 不涉及
        :type type: str
        :param vpc_id: **参数解释：** 实例组关联的VPC ID（通过调用虚拟私有云ListVpcs接口获取所有的VPC列表查询VPC的ID） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type vpc_id: str
        :param description: **参数解释：** 实例组描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        """
        
        

        self._name = None
        self._region = None
        self._type = None
        self._vpc_id = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.region = region
        self.type = type
        self.vpc_id = vpc_id
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this CreatePoolRequestBody.

        **参数解释：** 实例组名称，用于标识实例组，便于管理和识别。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字、下划线、中划线和点组成，且长度为1~256个字符 **默认取值：** 不涉及

        :return: The name of this CreatePoolRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePoolRequestBody.

        **参数解释：** 实例组名称，用于标识实例组，便于管理和识别。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字、下划线、中划线和点组成，且长度为1~256个字符 **默认取值：** 不涉及

        :param name: The name of this CreatePoolRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this CreatePoolRequestBody.

        **参数解释：** 实例组所在的区域（Region）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The region of this CreatePoolRequestBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreatePoolRequestBody.

        **参数解释：** 实例组所在的区域（Region）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param region: The region of this CreatePoolRequestBody.
        :type region: str
        """
        self._region = region

    @property
    def type(self):
        r"""Gets the type of this CreatePoolRequestBody.

        **参数解释：** 实例组类型 **约束限制：** 不涉及 **取值范围：** - elb: 基础elb类型 - elb-v2: elb-v2类型 - elb-shadow: saas化elb类型 - standard-container: 反向代理独享引擎组（云内，承载租户专用） - standard-cloud: 反向代理独享引擎组（云内） - standard: 反向代理独享引擎组（云外） - detector-cloud: 旁路检测独享引擎组（云内） - detector: 旁路检测独享引擎组（云外） **默认取值：** 不涉及

        :return: The type of this CreatePoolRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreatePoolRequestBody.

        **参数解释：** 实例组类型 **约束限制：** 不涉及 **取值范围：** - elb: 基础elb类型 - elb-v2: elb-v2类型 - elb-shadow: saas化elb类型 - standard-container: 反向代理独享引擎组（云内，承载租户专用） - standard-cloud: 反向代理独享引擎组（云内） - standard: 反向代理独享引擎组（云外） - detector-cloud: 旁路检测独享引擎组（云内） - detector: 旁路检测独享引擎组（云外） **默认取值：** 不涉及

        :param type: The type of this CreatePoolRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreatePoolRequestBody.

        **参数解释：** 实例组关联的VPC ID（通过调用虚拟私有云ListVpcs接口获取所有的VPC列表查询VPC的ID） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The vpc_id of this CreatePoolRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreatePoolRequestBody.

        **参数解释：** 实例组关联的VPC ID（通过调用虚拟私有云ListVpcs接口获取所有的VPC列表查询VPC的ID） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param vpc_id: The vpc_id of this CreatePoolRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        r"""Gets the description of this CreatePoolRequestBody.

        **参数解释：** 实例组描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this CreatePoolRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePoolRequestBody.

        **参数解释：** 实例组描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this CreatePoolRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreatePoolRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
