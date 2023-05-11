# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_name': 'str',
        'detail': 'list[Detail]',
        'id': 'str',
        'datastore_type': 'str',
        'available_zones': 'list[NodeTypeAvailableZones]',
        'ram': 'int',
        'vcpus': 'int',
        'datastores': 'list[NodeTypeDatastores]',
        'volume': 'VolumeResp',
        'elastic_volume_specs': 'list[NodeTypeElasticVolumeSpecs]'
    }

    attribute_map = {
        'spec_name': 'spec_name',
        'detail': 'detail',
        'id': 'id',
        'datastore_type': 'datastore_type',
        'available_zones': 'available_zones',
        'ram': 'ram',
        'vcpus': 'vcpus',
        'datastores': 'datastores',
        'volume': 'volume',
        'elastic_volume_specs': 'elastic_volume_specs'
    }

    def __init__(self, spec_name=None, detail=None, id=None, datastore_type=None, available_zones=None, ram=None, vcpus=None, datastores=None, volume=None, elastic_volume_specs=None):
        """NodeTypes

        The model defined in huaweicloud sdk

        :param spec_name: 节点类型名称。
        :type spec_name: str
        :param detail: 节点类型详细。
        :type detail: list[:class:`huaweicloudsdkdws.v2.Detail`]
        :param id: 节点类型ID。
        :type id: str
        :param datastore_type: 产品类型 - dws：云数仓。 - hybrid：实时数仓。 - stream：IoT数仓。
        :type datastore_type: str
        :param available_zones: 支持的可用区及状态信息。
        :type available_zones: list[:class:`huaweicloudsdkdws.v2.NodeTypeAvailableZones`]
        :param ram: 内存大小。
        :type ram: int
        :param vcpus: CPU数量。
        :type vcpus: int
        :param datastores: 内核版本信息。
        :type datastores: list[:class:`huaweicloudsdkdws.v2.NodeTypeDatastores`]
        :param volume: 
        :type volume: :class:`huaweicloudsdkdws.v2.VolumeResp`
        :param elastic_volume_specs: 如果规格为弹性容量规格，则该属性为规格典配的弹性容量信息，包括存储类型、最小容量、最大容量以及步长信息，如果为固定存储规格，则该属性为null。
        :type elastic_volume_specs: list[:class:`huaweicloudsdkdws.v2.NodeTypeElasticVolumeSpecs`]
        """
        
        

        self._spec_name = None
        self._detail = None
        self._id = None
        self._datastore_type = None
        self._available_zones = None
        self._ram = None
        self._vcpus = None
        self._datastores = None
        self._volume = None
        self._elastic_volume_specs = None
        self.discriminator = None

        self.spec_name = spec_name
        self.detail = detail
        self.id = id
        self.datastore_type = datastore_type
        self.available_zones = available_zones
        self.ram = ram
        self.vcpus = vcpus
        self.datastores = datastores
        self.volume = volume
        self.elastic_volume_specs = elastic_volume_specs

    @property
    def spec_name(self):
        """Gets the spec_name of this NodeTypes.

        节点类型名称。

        :return: The spec_name of this NodeTypes.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        """Sets the spec_name of this NodeTypes.

        节点类型名称。

        :param spec_name: The spec_name of this NodeTypes.
        :type spec_name: str
        """
        self._spec_name = spec_name

    @property
    def detail(self):
        """Gets the detail of this NodeTypes.

        节点类型详细。

        :return: The detail of this NodeTypes.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Detail`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this NodeTypes.

        节点类型详细。

        :param detail: The detail of this NodeTypes.
        :type detail: list[:class:`huaweicloudsdkdws.v2.Detail`]
        """
        self._detail = detail

    @property
    def id(self):
        """Gets the id of this NodeTypes.

        节点类型ID。

        :return: The id of this NodeTypes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeTypes.

        节点类型ID。

        :param id: The id of this NodeTypes.
        :type id: str
        """
        self._id = id

    @property
    def datastore_type(self):
        """Gets the datastore_type of this NodeTypes.

        产品类型 - dws：云数仓。 - hybrid：实时数仓。 - stream：IoT数仓。

        :return: The datastore_type of this NodeTypes.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this NodeTypes.

        产品类型 - dws：云数仓。 - hybrid：实时数仓。 - stream：IoT数仓。

        :param datastore_type: The datastore_type of this NodeTypes.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def available_zones(self):
        """Gets the available_zones of this NodeTypes.

        支持的可用区及状态信息。

        :return: The available_zones of this NodeTypes.
        :rtype: list[:class:`huaweicloudsdkdws.v2.NodeTypeAvailableZones`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this NodeTypes.

        支持的可用区及状态信息。

        :param available_zones: The available_zones of this NodeTypes.
        :type available_zones: list[:class:`huaweicloudsdkdws.v2.NodeTypeAvailableZones`]
        """
        self._available_zones = available_zones

    @property
    def ram(self):
        """Gets the ram of this NodeTypes.

        内存大小。

        :return: The ram of this NodeTypes.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this NodeTypes.

        内存大小。

        :param ram: The ram of this NodeTypes.
        :type ram: int
        """
        self._ram = ram

    @property
    def vcpus(self):
        """Gets the vcpus of this NodeTypes.

        CPU数量。

        :return: The vcpus of this NodeTypes.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this NodeTypes.

        CPU数量。

        :param vcpus: The vcpus of this NodeTypes.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def datastores(self):
        """Gets the datastores of this NodeTypes.

        内核版本信息。

        :return: The datastores of this NodeTypes.
        :rtype: list[:class:`huaweicloudsdkdws.v2.NodeTypeDatastores`]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """Sets the datastores of this NodeTypes.

        内核版本信息。

        :param datastores: The datastores of this NodeTypes.
        :type datastores: list[:class:`huaweicloudsdkdws.v2.NodeTypeDatastores`]
        """
        self._datastores = datastores

    @property
    def volume(self):
        """Gets the volume of this NodeTypes.

        :return: The volume of this NodeTypes.
        :rtype: :class:`huaweicloudsdkdws.v2.VolumeResp`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this NodeTypes.

        :param volume: The volume of this NodeTypes.
        :type volume: :class:`huaweicloudsdkdws.v2.VolumeResp`
        """
        self._volume = volume

    @property
    def elastic_volume_specs(self):
        """Gets the elastic_volume_specs of this NodeTypes.

        如果规格为弹性容量规格，则该属性为规格典配的弹性容量信息，包括存储类型、最小容量、最大容量以及步长信息，如果为固定存储规格，则该属性为null。

        :return: The elastic_volume_specs of this NodeTypes.
        :rtype: list[:class:`huaweicloudsdkdws.v2.NodeTypeElasticVolumeSpecs`]
        """
        return self._elastic_volume_specs

    @elastic_volume_specs.setter
    def elastic_volume_specs(self, elastic_volume_specs):
        """Sets the elastic_volume_specs of this NodeTypes.

        如果规格为弹性容量规格，则该属性为规格典配的弹性容量信息，包括存储类型、最小容量、最大容量以及步长信息，如果为固定存储规格，则该属性为null。

        :param elastic_volume_specs: The elastic_volume_specs of this NodeTypes.
        :type elastic_volume_specs: list[:class:`huaweicloudsdkdws.v2.NodeTypeElasticVolumeSpecs`]
        """
        self._elastic_volume_specs = elastic_volume_specs

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
        if not isinstance(other, NodeTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
