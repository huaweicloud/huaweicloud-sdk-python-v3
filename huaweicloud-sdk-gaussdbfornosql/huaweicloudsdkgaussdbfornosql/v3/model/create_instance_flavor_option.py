# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceFlavorOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'str',
        'storage': 'str',
        'size': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'num': 'num',
        'storage': 'storage',
        'size': 'size',
        'spec_code': 'spec_code'
    }

    def __init__(self, num=None, storage=None, size=None, spec_code=None):
        """CreateInstanceFlavorOption

        The model defined in huaweicloud sdk

        :param num: 节点数量。   - GeminiDB Cassandra实例的节点数量可取3~12。   - GeminiDB Mongo4.0版本副本集实例的节点数量可取3。   - GeminiDB Influx实例的节点数量可取3~16。
        :type num: str
        :param storage: 磁盘类型。 取值为“ULTRAHIGH”，表示SSD盘。
        :type storage: str
        :param size: 磁盘大小。必须为10的整数倍。单位为GB。最小磁盘容量100GB，最大磁盘容量与实例的性能规格有关，详见数据库实例规格。
        :type size: str
        :param spec_code: 资源规格编码。获取方法请参见查询所有实例规格信息中响应参数“spec_code”的值。
        :type spec_code: str
        """
        
        

        self._num = None
        self._storage = None
        self._size = None
        self._spec_code = None
        self.discriminator = None

        self.num = num
        self.storage = storage
        self.size = size
        self.spec_code = spec_code

    @property
    def num(self):
        """Gets the num of this CreateInstanceFlavorOption.

        节点数量。   - GeminiDB Cassandra实例的节点数量可取3~12。   - GeminiDB Mongo4.0版本副本集实例的节点数量可取3。   - GeminiDB Influx实例的节点数量可取3~16。

        :return: The num of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this CreateInstanceFlavorOption.

        节点数量。   - GeminiDB Cassandra实例的节点数量可取3~12。   - GeminiDB Mongo4.0版本副本集实例的节点数量可取3。   - GeminiDB Influx实例的节点数量可取3~16。

        :param num: The num of this CreateInstanceFlavorOption.
        :type num: str
        """
        self._num = num

    @property
    def storage(self):
        """Gets the storage of this CreateInstanceFlavorOption.

        磁盘类型。 取值为“ULTRAHIGH”，表示SSD盘。

        :return: The storage of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this CreateInstanceFlavorOption.

        磁盘类型。 取值为“ULTRAHIGH”，表示SSD盘。

        :param storage: The storage of this CreateInstanceFlavorOption.
        :type storage: str
        """
        self._storage = storage

    @property
    def size(self):
        """Gets the size of this CreateInstanceFlavorOption.

        磁盘大小。必须为10的整数倍。单位为GB。最小磁盘容量100GB，最大磁盘容量与实例的性能规格有关，详见数据库实例规格。

        :return: The size of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateInstanceFlavorOption.

        磁盘大小。必须为10的整数倍。单位为GB。最小磁盘容量100GB，最大磁盘容量与实例的性能规格有关，详见数据库实例规格。

        :param size: The size of this CreateInstanceFlavorOption.
        :type size: str
        """
        self._size = size

    @property
    def spec_code(self):
        """Gets the spec_code of this CreateInstanceFlavorOption.

        资源规格编码。获取方法请参见查询所有实例规格信息中响应参数“spec_code”的值。

        :return: The spec_code of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this CreateInstanceFlavorOption.

        资源规格编码。获取方法请参见查询所有实例规格信息中响应参数“spec_code”的值。

        :param spec_code: The spec_code of this CreateInstanceFlavorOption.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, CreateInstanceFlavorOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
