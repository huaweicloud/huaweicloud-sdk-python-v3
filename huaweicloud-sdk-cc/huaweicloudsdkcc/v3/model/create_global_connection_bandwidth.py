# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalConnectionBandwidth:

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
        'bordercross': 'bool',
        'type': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'charge_mode': 'str',
        'size': 'int',
        'sla_level': 'str',
        'local_area': 'str',
        'remote_area': 'str',
        'spec_code_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'bordercross': 'bordercross',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'charge_mode': 'charge_mode',
        'size': 'size',
        'sla_level': 'sla_level',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'spec_code_id': 'spec_code_id'
    }

    def __init__(self, name=None, description=None, bordercross=None, type=None, enterprise_project_id=None, tags=None, charge_mode=None, size=None, sla_level=None, local_area=None, remote_area=None, spec_code_id=None):
        r"""CreateGlobalConnectionBandwidth

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param bordercross: 功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 
        :type bordercross: bool
        :param type: 功能说明：描述带宽类型，对应地理区间的城域、区域、大区、跨区四级： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽
        :type type: str
        :param enterprise_project_id: 实例所属企业项目ID。
        :type enterprise_project_id: str
        :param tags: 实例标签。
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        :param charge_mode: 功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费     95avr: 按传统型日95计费
        :type charge_mode: str
        :param size: 功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s
        :type size: int
        :param sla_level: 功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银
        :type sla_level: str
        :param local_area: 功能说明：本端接入点，配合remote_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 
        :type local_area: str
        :param remote_area: 功能说明：远端接入点，配合local_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 
        :type remote_area: str
        :param spec_code_id: 功能说明：线路规格编码UUID。
        :type spec_code_id: str
        """
        
        

        self._name = None
        self._description = None
        self._bordercross = None
        self._type = None
        self._enterprise_project_id = None
        self._tags = None
        self._charge_mode = None
        self._size = None
        self._sla_level = None
        self._local_area = None
        self._remote_area = None
        self._spec_code_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.bordercross = bordercross
        self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        self.charge_mode = charge_mode
        self.size = size
        if sla_level is not None:
            self.sla_level = sla_level
        if local_area is not None:
            self.local_area = local_area
        if remote_area is not None:
            self.remote_area = remote_area
        if spec_code_id is not None:
            self.spec_code_id = spec_code_id

    @property
    def name(self):
        r"""Gets the name of this CreateGlobalConnectionBandwidth.

        实例名称。

        :return: The name of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGlobalConnectionBandwidth.

        实例名称。

        :param name: The name of this CreateGlobalConnectionBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateGlobalConnectionBandwidth.

        实例描述。不支持 <>。

        :return: The description of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGlobalConnectionBandwidth.

        实例描述。不支持 <>。

        :param description: The description of this CreateGlobalConnectionBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def bordercross(self):
        r"""Gets the bordercross of this CreateGlobalConnectionBandwidth.

        功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 

        :return: The bordercross of this CreateGlobalConnectionBandwidth.
        :rtype: bool
        """
        return self._bordercross

    @bordercross.setter
    def bordercross(self, bordercross):
        r"""Sets the bordercross of this CreateGlobalConnectionBandwidth.

        功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 

        :param bordercross: The bordercross of this CreateGlobalConnectionBandwidth.
        :type bordercross: bool
        """
        self._bordercross = bordercross

    @property
    def type(self):
        r"""Gets the type of this CreateGlobalConnectionBandwidth.

        功能说明：描述带宽类型，对应地理区间的城域、区域、大区、跨区四级： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽

        :return: The type of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateGlobalConnectionBandwidth.

        功能说明：描述带宽类型，对应地理区间的城域、区域、大区、跨区四级： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽

        :param type: The type of this CreateGlobalConnectionBandwidth.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateGlobalConnectionBandwidth.

        实例所属企业项目ID。

        :return: The enterprise_project_id of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateGlobalConnectionBandwidth.

        实例所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateGlobalConnectionBandwidth.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateGlobalConnectionBandwidth.

        实例标签。

        :return: The tags of this CreateGlobalConnectionBandwidth.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateGlobalConnectionBandwidth.

        实例标签。

        :param tags: The tags of this CreateGlobalConnectionBandwidth.
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        self._tags = tags

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this CreateGlobalConnectionBandwidth.

        功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费     95avr: 按传统型日95计费

        :return: The charge_mode of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this CreateGlobalConnectionBandwidth.

        功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费     95avr: 按传统型日95计费

        :param charge_mode: The charge_mode of this CreateGlobalConnectionBandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def size(self):
        r"""Gets the size of this CreateGlobalConnectionBandwidth.

        功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s

        :return: The size of this CreateGlobalConnectionBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CreateGlobalConnectionBandwidth.

        功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s

        :param size: The size of this CreateGlobalConnectionBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def sla_level(self):
        r"""Gets the sla_level of this CreateGlobalConnectionBandwidth.

        功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银

        :return: The sla_level of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._sla_level

    @sla_level.setter
    def sla_level(self, sla_level):
        r"""Sets the sla_level of this CreateGlobalConnectionBandwidth.

        功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银

        :param sla_level: The sla_level of this CreateGlobalConnectionBandwidth.
        :type sla_level: str
        """
        self._sla_level = sla_level

    @property
    def local_area(self):
        r"""Gets the local_area of this CreateGlobalConnectionBandwidth.

        功能说明：本端接入点，配合remote_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :return: The local_area of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        r"""Sets the local_area of this CreateGlobalConnectionBandwidth.

        功能说明：本端接入点，配合remote_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :param local_area: The local_area of this CreateGlobalConnectionBandwidth.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        r"""Gets the remote_area of this CreateGlobalConnectionBandwidth.

        功能说明：远端接入点，配合local_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :return: The remote_area of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        r"""Sets the remote_area of this CreateGlobalConnectionBandwidth.

        功能说明：远端接入点，配合local_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :param remote_area: The remote_area of this CreateGlobalConnectionBandwidth.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def spec_code_id(self):
        r"""Gets the spec_code_id of this CreateGlobalConnectionBandwidth.

        功能说明：线路规格编码UUID。

        :return: The spec_code_id of this CreateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._spec_code_id

    @spec_code_id.setter
    def spec_code_id(self, spec_code_id):
        r"""Sets the spec_code_id of this CreateGlobalConnectionBandwidth.

        功能说明：线路规格编码UUID。

        :param spec_code_id: The spec_code_id of this CreateGlobalConnectionBandwidth.
        :type spec_code_id: str
        """
        self._spec_code_id = spec_code_id

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
        if not isinstance(other, CreateGlobalConnectionBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
