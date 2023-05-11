# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDcPointReqDTO:

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
        'data_type': 'str',
        'collection_config': 'object',
        'device_id': 'str',
        '_property': 'str',
        'processing_config': 'ProcessingConfigDTO'
    }

    attribute_map = {
        'point_id': 'point_id',
        'name': 'name',
        'data_type': 'data_type',
        'collection_config': 'collection_config',
        'device_id': 'device_id',
        '_property': 'property',
        'processing_config': 'processing_config'
    }

    def __init__(self, point_id=None, name=None, data_type=None, collection_config=None, device_id=None, _property=None, processing_config=None):
        """CreateDcPointReqDTO

        The model defined in huaweicloud sdk

        :param point_id: 点位表id，数据源下唯一
        :type point_id: str
        :param name: 点位名称，允许中、数字、英文大小写、下划线、中划线、#%()*特殊字符
        :type name: str
        :param data_type: 点位数据类型
        :type data_type: str
        :param collection_config: 点位采集配置
        :type collection_config: object
        :param device_id: 设备id
        :type device_id: str
        :param _property: 属性，允许中、数字、英文大小写、下划线、中划线
        :type _property: str
        :param processing_config: 
        :type processing_config: :class:`huaweicloudsdkiotedge.v2.ProcessingConfigDTO`
        """
        
        

        self._point_id = None
        self._name = None
        self._data_type = None
        self._collection_config = None
        self._device_id = None
        self.__property = None
        self._processing_config = None
        self.discriminator = None

        self.point_id = point_id
        self.name = name
        if data_type is not None:
            self.data_type = data_type
        self.collection_config = collection_config
        self.device_id = device_id
        self._property = _property
        if processing_config is not None:
            self.processing_config = processing_config

    @property
    def point_id(self):
        """Gets the point_id of this CreateDcPointReqDTO.

        点位表id，数据源下唯一

        :return: The point_id of this CreateDcPointReqDTO.
        :rtype: str
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        """Sets the point_id of this CreateDcPointReqDTO.

        点位表id，数据源下唯一

        :param point_id: The point_id of this CreateDcPointReqDTO.
        :type point_id: str
        """
        self._point_id = point_id

    @property
    def name(self):
        """Gets the name of this CreateDcPointReqDTO.

        点位名称，允许中、数字、英文大小写、下划线、中划线、#%()*特殊字符

        :return: The name of this CreateDcPointReqDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDcPointReqDTO.

        点位名称，允许中、数字、英文大小写、下划线、中划线、#%()*特殊字符

        :param name: The name of this CreateDcPointReqDTO.
        :type name: str
        """
        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this CreateDcPointReqDTO.

        点位数据类型

        :return: The data_type of this CreateDcPointReqDTO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CreateDcPointReqDTO.

        点位数据类型

        :param data_type: The data_type of this CreateDcPointReqDTO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def collection_config(self):
        """Gets the collection_config of this CreateDcPointReqDTO.

        点位采集配置

        :return: The collection_config of this CreateDcPointReqDTO.
        :rtype: object
        """
        return self._collection_config

    @collection_config.setter
    def collection_config(self, collection_config):
        """Sets the collection_config of this CreateDcPointReqDTO.

        点位采集配置

        :param collection_config: The collection_config of this CreateDcPointReqDTO.
        :type collection_config: object
        """
        self._collection_config = collection_config

    @property
    def device_id(self):
        """Gets the device_id of this CreateDcPointReqDTO.

        设备id

        :return: The device_id of this CreateDcPointReqDTO.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this CreateDcPointReqDTO.

        设备id

        :param device_id: The device_id of this CreateDcPointReqDTO.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def _property(self):
        """Gets the _property of this CreateDcPointReqDTO.

        属性，允许中、数字、英文大小写、下划线、中划线

        :return: The _property of this CreateDcPointReqDTO.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this CreateDcPointReqDTO.

        属性，允许中、数字、英文大小写、下划线、中划线

        :param _property: The _property of this CreateDcPointReqDTO.
        :type _property: str
        """
        self.__property = _property

    @property
    def processing_config(self):
        """Gets the processing_config of this CreateDcPointReqDTO.

        :return: The processing_config of this CreateDcPointReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ProcessingConfigDTO`
        """
        return self._processing_config

    @processing_config.setter
    def processing_config(self, processing_config):
        """Sets the processing_config of this CreateDcPointReqDTO.

        :param processing_config: The processing_config of this CreateDcPointReqDTO.
        :type processing_config: :class:`huaweicloudsdkiotedge.v2.ProcessingConfigDTO`
        """
        self._processing_config = processing_config

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
        if not isinstance(other, CreateDcPointReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
