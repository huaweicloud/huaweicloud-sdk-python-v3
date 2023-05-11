# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDcPointRespDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'point_id': 'str',
        'name': 'str',
        'collection_config': 'object',
        'device_id': 'str',
        '_property': 'str',
        'data_type': 'str',
        'ds_id': 'str',
        'processing_config': 'ProcessingConfigDTO',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'point_id': 'point_id',
        'name': 'name',
        'collection_config': 'collection_config',
        'device_id': 'device_id',
        '_property': 'property',
        'data_type': 'data_type',
        'ds_id': 'ds_id',
        'processing_config': 'processing_config',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, point_id=None, name=None, collection_config=None, device_id=None, _property=None, data_type=None, ds_id=None, processing_config=None, create_time=None, update_time=None):
        """CreateDcPointRespDTO

        The model defined in huaweicloud sdk

        :param point_id: 点位表id，数据源下唯一
        :type point_id: str
        :param name: 点位名称，允许中、数字、英文大小写、下划线、中划线、#%()*特殊字符
        :type name: str
        :param collection_config: 点位采集配置
        :type collection_config: object
        :param device_id: 设备id
        :type device_id: str
        :param _property: 属性，允许中、数字、英文大小写、下划线、中划线
        :type _property: str
        :param data_type: 点位数据类型
        :type data_type: str
        :param ds_id: 采集数据源id，节点下唯一
        :type ds_id: str
        :param processing_config: 
        :type processing_config: :class:`huaweicloudsdkiotedge.v2.ProcessingConfigDTO`
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        """
        
        

        self._point_id = None
        self._name = None
        self._collection_config = None
        self._device_id = None
        self.__property = None
        self._data_type = None
        self._ds_id = None
        self._processing_config = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if point_id is not None:
            self.point_id = point_id
        if name is not None:
            self.name = name
        if collection_config is not None:
            self.collection_config = collection_config
        if device_id is not None:
            self.device_id = device_id
        if _property is not None:
            self._property = _property
        if data_type is not None:
            self.data_type = data_type
        if ds_id is not None:
            self.ds_id = ds_id
        if processing_config is not None:
            self.processing_config = processing_config
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def point_id(self):
        """Gets the point_id of this CreateDcPointRespDTO.

        点位表id，数据源下唯一

        :return: The point_id of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        """Sets the point_id of this CreateDcPointRespDTO.

        点位表id，数据源下唯一

        :param point_id: The point_id of this CreateDcPointRespDTO.
        :type point_id: str
        """
        self._point_id = point_id

    @property
    def name(self):
        """Gets the name of this CreateDcPointRespDTO.

        点位名称，允许中、数字、英文大小写、下划线、中划线、#%()*特殊字符

        :return: The name of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDcPointRespDTO.

        点位名称，允许中、数字、英文大小写、下划线、中划线、#%()*特殊字符

        :param name: The name of this CreateDcPointRespDTO.
        :type name: str
        """
        self._name = name

    @property
    def collection_config(self):
        """Gets the collection_config of this CreateDcPointRespDTO.

        点位采集配置

        :return: The collection_config of this CreateDcPointRespDTO.
        :rtype: object
        """
        return self._collection_config

    @collection_config.setter
    def collection_config(self, collection_config):
        """Sets the collection_config of this CreateDcPointRespDTO.

        点位采集配置

        :param collection_config: The collection_config of this CreateDcPointRespDTO.
        :type collection_config: object
        """
        self._collection_config = collection_config

    @property
    def device_id(self):
        """Gets the device_id of this CreateDcPointRespDTO.

        设备id

        :return: The device_id of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this CreateDcPointRespDTO.

        设备id

        :param device_id: The device_id of this CreateDcPointRespDTO.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def _property(self):
        """Gets the _property of this CreateDcPointRespDTO.

        属性，允许中、数字、英文大小写、下划线、中划线

        :return: The _property of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this CreateDcPointRespDTO.

        属性，允许中、数字、英文大小写、下划线、中划线

        :param _property: The _property of this CreateDcPointRespDTO.
        :type _property: str
        """
        self.__property = _property

    @property
    def data_type(self):
        """Gets the data_type of this CreateDcPointRespDTO.

        点位数据类型

        :return: The data_type of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CreateDcPointRespDTO.

        点位数据类型

        :param data_type: The data_type of this CreateDcPointRespDTO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def ds_id(self):
        """Gets the ds_id of this CreateDcPointRespDTO.

        采集数据源id，节点下唯一

        :return: The ds_id of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        """Sets the ds_id of this CreateDcPointRespDTO.

        采集数据源id，节点下唯一

        :param ds_id: The ds_id of this CreateDcPointRespDTO.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def processing_config(self):
        """Gets the processing_config of this CreateDcPointRespDTO.

        :return: The processing_config of this CreateDcPointRespDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ProcessingConfigDTO`
        """
        return self._processing_config

    @processing_config.setter
    def processing_config(self, processing_config):
        """Sets the processing_config of this CreateDcPointRespDTO.

        :param processing_config: The processing_config of this CreateDcPointRespDTO.
        :type processing_config: :class:`huaweicloudsdkiotedge.v2.ProcessingConfigDTO`
        """
        self._processing_config = processing_config

    @property
    def create_time(self):
        """Gets the create_time of this CreateDcPointRespDTO.

        创建时间

        :return: The create_time of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateDcPointRespDTO.

        创建时间

        :param create_time: The create_time of this CreateDcPointRespDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateDcPointRespDTO.

        最后一次修改时间

        :return: The update_time of this CreateDcPointRespDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateDcPointRespDTO.

        最后一次修改时间

        :param update_time: The update_time of this CreateDcPointRespDTO.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, CreateDcPointRespDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
