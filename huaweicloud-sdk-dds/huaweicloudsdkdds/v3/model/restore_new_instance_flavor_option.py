# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreNewInstanceFlavorOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'num': 'str',
        'size': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'type': 'type',
        'num': 'num',
        'size': 'size',
        'spec_code': 'spec_code'
    }

    def __init__(self, type=None, num=None, size=None, spec_code=None):
        """RestoreNewInstanceFlavorOption

        The model defined in huaweicloud sdk

        :param type: 节点类型。 取值：   - 集群实例包含mongos、shard和config节点，各节点下该参数取值分别为“mongos”、“shard”和“config”。   - 副本集实例下该参数取值为“replica”。   - 单节点实例下该参数取值为“single”。
        :type type: str
        :param num: 节点数量。 取值：   - 集群实例下“mongos”类型的节点数量可取2~16。   - 集群实例下“shard”类型的组数量可取2~16。   - “shard”类型的组数量可取2~16。   - “config”类型的组数量只能取1。   - “replica”类型的组数量只能取1。   - “single”类型的节点数量只能取1。
        :type num: str
        :param size: 磁盘大小。 取值：必须为10的整数倍。单位为GB。   - 对于集群实例，shard组可取10GB~2000GB，config组仅可取20GB。mongos节点不涉及选择磁盘，该参数无意义。   - 对于副本集实例，可取10GB~2000GB。   - 对于单节点实例，可取10GB~1000GB。
        :type size: str
        :param spec_code: 资源规格编码
        :type spec_code: str
        """
        
        

        self._type = None
        self._num = None
        self._size = None
        self._spec_code = None
        self.discriminator = None

        self.type = type
        self.num = num
        if size is not None:
            self.size = size
        self.spec_code = spec_code

    @property
    def type(self):
        """Gets the type of this RestoreNewInstanceFlavorOption.

        节点类型。 取值：   - 集群实例包含mongos、shard和config节点，各节点下该参数取值分别为“mongos”、“shard”和“config”。   - 副本集实例下该参数取值为“replica”。   - 单节点实例下该参数取值为“single”。

        :return: The type of this RestoreNewInstanceFlavorOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestoreNewInstanceFlavorOption.

        节点类型。 取值：   - 集群实例包含mongos、shard和config节点，各节点下该参数取值分别为“mongos”、“shard”和“config”。   - 副本集实例下该参数取值为“replica”。   - 单节点实例下该参数取值为“single”。

        :param type: The type of this RestoreNewInstanceFlavorOption.
        :type type: str
        """
        self._type = type

    @property
    def num(self):
        """Gets the num of this RestoreNewInstanceFlavorOption.

        节点数量。 取值：   - 集群实例下“mongos”类型的节点数量可取2~16。   - 集群实例下“shard”类型的组数量可取2~16。   - “shard”类型的组数量可取2~16。   - “config”类型的组数量只能取1。   - “replica”类型的组数量只能取1。   - “single”类型的节点数量只能取1。

        :return: The num of this RestoreNewInstanceFlavorOption.
        :rtype: str
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this RestoreNewInstanceFlavorOption.

        节点数量。 取值：   - 集群实例下“mongos”类型的节点数量可取2~16。   - 集群实例下“shard”类型的组数量可取2~16。   - “shard”类型的组数量可取2~16。   - “config”类型的组数量只能取1。   - “replica”类型的组数量只能取1。   - “single”类型的节点数量只能取1。

        :param num: The num of this RestoreNewInstanceFlavorOption.
        :type num: str
        """
        self._num = num

    @property
    def size(self):
        """Gets the size of this RestoreNewInstanceFlavorOption.

        磁盘大小。 取值：必须为10的整数倍。单位为GB。   - 对于集群实例，shard组可取10GB~2000GB，config组仅可取20GB。mongos节点不涉及选择磁盘，该参数无意义。   - 对于副本集实例，可取10GB~2000GB。   - 对于单节点实例，可取10GB~1000GB。

        :return: The size of this RestoreNewInstanceFlavorOption.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RestoreNewInstanceFlavorOption.

        磁盘大小。 取值：必须为10的整数倍。单位为GB。   - 对于集群实例，shard组可取10GB~2000GB，config组仅可取20GB。mongos节点不涉及选择磁盘，该参数无意义。   - 对于副本集实例，可取10GB~2000GB。   - 对于单节点实例，可取10GB~1000GB。

        :param size: The size of this RestoreNewInstanceFlavorOption.
        :type size: str
        """
        self._size = size

    @property
    def spec_code(self):
        """Gets the spec_code of this RestoreNewInstanceFlavorOption.

        资源规格编码

        :return: The spec_code of this RestoreNewInstanceFlavorOption.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this RestoreNewInstanceFlavorOption.

        资源规格编码

        :param spec_code: The spec_code of this RestoreNewInstanceFlavorOption.
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
        if not isinstance(other, RestoreNewInstanceFlavorOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
