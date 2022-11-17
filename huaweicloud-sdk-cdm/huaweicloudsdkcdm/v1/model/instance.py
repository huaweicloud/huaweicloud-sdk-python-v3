# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Instance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'nics': 'list[Nics]',
        'flavor_ref': 'str',
        'type': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'nics': 'nics',
        'flavor_ref': 'flavorRef',
        'type': 'type'
    }

    def __init__(self, availability_zone=None, nics=None, flavor_ref=None, type=None):
        """Instance

        The model defined in huaweicloud sdk

        :param availability_zone: 集群的可用分区
        :type availability_zone: str
        :param nics: 网卡列表，最多两个网卡。请参见•nics参数说明
        :type nics: list[:class:`huaweicloudsdkcdm.v1.Nics`]
        :param flavor_ref: 实例规格： - a79fd5ae-1833-448a-88e8-3ea2b913e1f6：表示cdm.small规格，2核CPU、4G内存的虚拟机。适合PoC验证和开发测试。 - fb8fe666-6734-4b11-bc6c-43d11db3c745：表示cdm.medium规格，4核CPU、8G内存的虚拟机适合单张表规模&lt;1000万条的场景。 - 5ddb1071-c5d7-40e0-a874-8a032e81a697：表示cdm.large规格，8核CPU、16G内存的虚拟机。适合单张表规模≥1000万条的场景。 - 6ddb1072-c5d7-40e0-a874-8a032e81a698：表示cdm.xlarge规格，16核CPU、32G内存的虚拟机。需要10GE高速带宽进行TB以上的数据量迁移时使用
        :type flavor_ref: str
        :param type: 节点类型，当前只有“cdm”一种类型
        :type type: str
        """
        
        

        self._availability_zone = None
        self._nics = None
        self._flavor_ref = None
        self._type = None
        self.discriminator = None

        self.availability_zone = availability_zone
        self.nics = nics
        self.flavor_ref = flavor_ref
        self.type = type

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Instance.

        集群的可用分区

        :return: The availability_zone of this Instance.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Instance.

        集群的可用分区

        :param availability_zone: The availability_zone of this Instance.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def nics(self):
        """Gets the nics of this Instance.

        网卡列表，最多两个网卡。请参见•nics参数说明

        :return: The nics of this Instance.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this Instance.

        网卡列表，最多两个网卡。请参见•nics参数说明

        :param nics: The nics of this Instance.
        :type nics: list[:class:`huaweicloudsdkcdm.v1.Nics`]
        """
        self._nics = nics

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this Instance.

        实例规格： - a79fd5ae-1833-448a-88e8-3ea2b913e1f6：表示cdm.small规格，2核CPU、4G内存的虚拟机。适合PoC验证和开发测试。 - fb8fe666-6734-4b11-bc6c-43d11db3c745：表示cdm.medium规格，4核CPU、8G内存的虚拟机适合单张表规模<1000万条的场景。 - 5ddb1071-c5d7-40e0-a874-8a032e81a697：表示cdm.large规格，8核CPU、16G内存的虚拟机。适合单张表规模≥1000万条的场景。 - 6ddb1072-c5d7-40e0-a874-8a032e81a698：表示cdm.xlarge规格，16核CPU、32G内存的虚拟机。需要10GE高速带宽进行TB以上的数据量迁移时使用

        :return: The flavor_ref of this Instance.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this Instance.

        实例规格： - a79fd5ae-1833-448a-88e8-3ea2b913e1f6：表示cdm.small规格，2核CPU、4G内存的虚拟机。适合PoC验证和开发测试。 - fb8fe666-6734-4b11-bc6c-43d11db3c745：表示cdm.medium规格，4核CPU、8G内存的虚拟机适合单张表规模<1000万条的场景。 - 5ddb1071-c5d7-40e0-a874-8a032e81a697：表示cdm.large规格，8核CPU、16G内存的虚拟机。适合单张表规模≥1000万条的场景。 - 6ddb1072-c5d7-40e0-a874-8a032e81a698：表示cdm.xlarge规格，16核CPU、32G内存的虚拟机。需要10GE高速带宽进行TB以上的数据量迁移时使用

        :param flavor_ref: The flavor_ref of this Instance.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def type(self):
        """Gets the type of this Instance.

        节点类型，当前只有“cdm”一种类型

        :return: The type of this Instance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Instance.

        节点类型，当前只有“cdm”一种类型

        :param type: The type of this Instance.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
