# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceCheckResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'instance_num': 'int',
        'mode': 'str',
        'availability_zone_mode': 'str',
        'fe_node_num': 'int',
        'be_node_num': 'int',
        'fe_flavor_ref': 'str',
        'be_flavor_ref': 'str',
        'availability_zone': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'instance_num': 'instance_num',
        'mode': 'mode',
        'availability_zone_mode': 'availability_zone_mode',
        'fe_node_num': 'fe_node_num',
        'be_node_num': 'be_node_num',
        'fe_flavor_ref': 'fe_flavor_ref',
        'be_flavor_ref': 'be_flavor_ref',
        'availability_zone': 'availability_zone',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, enterprise_project_id=None, instance_num=None, mode=None, availability_zone_mode=None, fe_node_num=None, be_node_num=None, fe_flavor_ref=None, be_flavor_ref=None, availability_zone=None, subnet_id=None):
        r"""ResourceCheckResource

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param instance_num: 实例数量。
        :type instance_num: int
        :param mode: 实例部署模式。
        :type mode: str
        :param availability_zone_mode: 可用区类型，目前仅支持single。
        :type availability_zone_mode: str
        :param fe_node_num: FE节点数量。
        :type fe_node_num: int
        :param be_node_num: BE节点数量。
        :type be_node_num: int
        :param fe_flavor_ref: FE规格码。
        :type fe_flavor_ref: str
        :param be_flavor_ref: BE规格码。
        :type be_flavor_ref: str
        :param availability_zone: 可用区码。选填，校验可用区码是否正确。
        :type availability_zone: str
        :param subnet_id: HTAP实例子网即TaurusDB实例子网。 获取方法请参见[获取子网ID](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。
        :type subnet_id: str
        """
        
        

        self._enterprise_project_id = None
        self._instance_num = None
        self._mode = None
        self._availability_zone_mode = None
        self._fe_node_num = None
        self._be_node_num = None
        self._fe_flavor_ref = None
        self._be_flavor_ref = None
        self._availability_zone = None
        self._subnet_id = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.instance_num = instance_num
        self.mode = mode
        self.availability_zone_mode = availability_zone_mode
        self.fe_node_num = fe_node_num
        self.be_node_num = be_node_num
        self.fe_flavor_ref = fe_flavor_ref
        self.be_flavor_ref = be_flavor_ref
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.subnet_id = subnet_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ResourceCheckResource.

        企业项目ID。

        :return: The enterprise_project_id of this ResourceCheckResource.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ResourceCheckResource.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ResourceCheckResource.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_num(self):
        r"""Gets the instance_num of this ResourceCheckResource.

        实例数量。

        :return: The instance_num of this ResourceCheckResource.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this ResourceCheckResource.

        实例数量。

        :param instance_num: The instance_num of this ResourceCheckResource.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def mode(self):
        r"""Gets the mode of this ResourceCheckResource.

        实例部署模式。

        :return: The mode of this ResourceCheckResource.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ResourceCheckResource.

        实例部署模式。

        :param mode: The mode of this ResourceCheckResource.
        :type mode: str
        """
        self._mode = mode

    @property
    def availability_zone_mode(self):
        r"""Gets the availability_zone_mode of this ResourceCheckResource.

        可用区类型，目前仅支持single。

        :return: The availability_zone_mode of this ResourceCheckResource.
        :rtype: str
        """
        return self._availability_zone_mode

    @availability_zone_mode.setter
    def availability_zone_mode(self, availability_zone_mode):
        r"""Sets the availability_zone_mode of this ResourceCheckResource.

        可用区类型，目前仅支持single。

        :param availability_zone_mode: The availability_zone_mode of this ResourceCheckResource.
        :type availability_zone_mode: str
        """
        self._availability_zone_mode = availability_zone_mode

    @property
    def fe_node_num(self):
        r"""Gets the fe_node_num of this ResourceCheckResource.

        FE节点数量。

        :return: The fe_node_num of this ResourceCheckResource.
        :rtype: int
        """
        return self._fe_node_num

    @fe_node_num.setter
    def fe_node_num(self, fe_node_num):
        r"""Sets the fe_node_num of this ResourceCheckResource.

        FE节点数量。

        :param fe_node_num: The fe_node_num of this ResourceCheckResource.
        :type fe_node_num: int
        """
        self._fe_node_num = fe_node_num

    @property
    def be_node_num(self):
        r"""Gets the be_node_num of this ResourceCheckResource.

        BE节点数量。

        :return: The be_node_num of this ResourceCheckResource.
        :rtype: int
        """
        return self._be_node_num

    @be_node_num.setter
    def be_node_num(self, be_node_num):
        r"""Sets the be_node_num of this ResourceCheckResource.

        BE节点数量。

        :param be_node_num: The be_node_num of this ResourceCheckResource.
        :type be_node_num: int
        """
        self._be_node_num = be_node_num

    @property
    def fe_flavor_ref(self):
        r"""Gets the fe_flavor_ref of this ResourceCheckResource.

        FE规格码。

        :return: The fe_flavor_ref of this ResourceCheckResource.
        :rtype: str
        """
        return self._fe_flavor_ref

    @fe_flavor_ref.setter
    def fe_flavor_ref(self, fe_flavor_ref):
        r"""Sets the fe_flavor_ref of this ResourceCheckResource.

        FE规格码。

        :param fe_flavor_ref: The fe_flavor_ref of this ResourceCheckResource.
        :type fe_flavor_ref: str
        """
        self._fe_flavor_ref = fe_flavor_ref

    @property
    def be_flavor_ref(self):
        r"""Gets the be_flavor_ref of this ResourceCheckResource.

        BE规格码。

        :return: The be_flavor_ref of this ResourceCheckResource.
        :rtype: str
        """
        return self._be_flavor_ref

    @be_flavor_ref.setter
    def be_flavor_ref(self, be_flavor_ref):
        r"""Sets the be_flavor_ref of this ResourceCheckResource.

        BE规格码。

        :param be_flavor_ref: The be_flavor_ref of this ResourceCheckResource.
        :type be_flavor_ref: str
        """
        self._be_flavor_ref = be_flavor_ref

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ResourceCheckResource.

        可用区码。选填，校验可用区码是否正确。

        :return: The availability_zone of this ResourceCheckResource.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ResourceCheckResource.

        可用区码。选填，校验可用区码是否正确。

        :param availability_zone: The availability_zone of this ResourceCheckResource.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ResourceCheckResource.

        HTAP实例子网即TaurusDB实例子网。 获取方法请参见[获取子网ID](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :return: The subnet_id of this ResourceCheckResource.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ResourceCheckResource.

        HTAP实例子网即TaurusDB实例子网。 获取方法请参见[获取子网ID](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :param subnet_id: The subnet_id of this ResourceCheckResource.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, ResourceCheckResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
