# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterInstanceBody:

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
        'instance_num': 'int',
        'flavor': 'str',
        'volume_type': 'str',
        'volume_size': 'int',
        'flavor_type': 'str'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'instance_num': 'instance_num',
        'flavor': 'flavor',
        'volume_type': 'volume_type',
        'volume_size': 'volume_size',
        'flavor_type': 'flavor_type'
    }

    def __init__(self, instance_type=None, instance_num=None, flavor=None, volume_type=None, volume_size=None, flavor_type=None):
        r"""CreateClusterInstanceBody

        The model defined in huaweicloud sdk

        :param instance_type: 集群节点类型，hbase有regionserver，hmaster，opentsdb等，doris有be，fe节点，clickhouse有server（计算节点），zookeeper
        :type instance_type: str
        :param instance_num: 节点个数，hbase取值：2&lt;&#x3D;num&lt;&#x3D;10],偶数 doris取值：be[3,100] fe只能是3或5， clickhouse取值：计算节点[2,10000],取偶数，zookeeper节点固定为3
        :type instance_num: int
        :param flavor: 节点规格，doris集群、clickhouse集群必选
        :type flavor: str
        :param volume_type: 数据盘规格：COMMON、HIGH、ULTRAHIGH，NORMALHIGH, EXTREMEHIGH. doris集群、clickhouse集群必选
        :type volume_type: str
        :param volume_size: 数据盘大小，doris集群、clickhouse集群必选。 fe[200,2000] be[400,10000] server[500,10000] zookeeper[200,1000]
        :type volume_size: int
        :param flavor_type: 节点入参类型 0：flavor模式 ，1：cu模式，doris、hbase、clickhouse都是flavor模式
        :type flavor_type: str
        """
        
        

        self._instance_type = None
        self._instance_num = None
        self._flavor = None
        self._volume_type = None
        self._volume_size = None
        self._flavor_type = None
        self.discriminator = None

        self.instance_type = instance_type
        self.instance_num = instance_num
        if flavor is not None:
            self.flavor = flavor
        if volume_type is not None:
            self.volume_type = volume_type
        if volume_size is not None:
            self.volume_size = volume_size
        if flavor_type is not None:
            self.flavor_type = flavor_type

    @property
    def instance_type(self):
        r"""Gets the instance_type of this CreateClusterInstanceBody.

        集群节点类型，hbase有regionserver，hmaster，opentsdb等，doris有be，fe节点，clickhouse有server（计算节点），zookeeper

        :return: The instance_type of this CreateClusterInstanceBody.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this CreateClusterInstanceBody.

        集群节点类型，hbase有regionserver，hmaster，opentsdb等，doris有be，fe节点，clickhouse有server（计算节点），zookeeper

        :param instance_type: The instance_type of this CreateClusterInstanceBody.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_num(self):
        r"""Gets the instance_num of this CreateClusterInstanceBody.

        节点个数，hbase取值：2<=num<=10],偶数 doris取值：be[3,100] fe只能是3或5， clickhouse取值：计算节点[2,10000],取偶数，zookeeper节点固定为3

        :return: The instance_num of this CreateClusterInstanceBody.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this CreateClusterInstanceBody.

        节点个数，hbase取值：2<=num<=10],偶数 doris取值：be[3,100] fe只能是3或5， clickhouse取值：计算节点[2,10000],取偶数，zookeeper节点固定为3

        :param instance_num: The instance_num of this CreateClusterInstanceBody.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateClusterInstanceBody.

        节点规格，doris集群、clickhouse集群必选

        :return: The flavor of this CreateClusterInstanceBody.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateClusterInstanceBody.

        节点规格，doris集群、clickhouse集群必选

        :param flavor: The flavor of this CreateClusterInstanceBody.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def volume_type(self):
        r"""Gets the volume_type of this CreateClusterInstanceBody.

        数据盘规格：COMMON、HIGH、ULTRAHIGH，NORMALHIGH, EXTREMEHIGH. doris集群、clickhouse集群必选

        :return: The volume_type of this CreateClusterInstanceBody.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this CreateClusterInstanceBody.

        数据盘规格：COMMON、HIGH、ULTRAHIGH，NORMALHIGH, EXTREMEHIGH. doris集群、clickhouse集群必选

        :param volume_type: The volume_type of this CreateClusterInstanceBody.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_size(self):
        r"""Gets the volume_size of this CreateClusterInstanceBody.

        数据盘大小，doris集群、clickhouse集群必选。 fe[200,2000] be[400,10000] server[500,10000] zookeeper[200,1000]

        :return: The volume_size of this CreateClusterInstanceBody.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this CreateClusterInstanceBody.

        数据盘大小，doris集群、clickhouse集群必选。 fe[200,2000] be[400,10000] server[500,10000] zookeeper[200,1000]

        :param volume_size: The volume_size of this CreateClusterInstanceBody.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this CreateClusterInstanceBody.

        节点入参类型 0：flavor模式 ，1：cu模式，doris、hbase、clickhouse都是flavor模式

        :return: The flavor_type of this CreateClusterInstanceBody.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this CreateClusterInstanceBody.

        节点入参类型 0：flavor模式 ，1：cu模式，doris、hbase、clickhouse都是flavor模式

        :param flavor_type: The flavor_type of this CreateClusterInstanceBody.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

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
        if not isinstance(other, CreateClusterInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
