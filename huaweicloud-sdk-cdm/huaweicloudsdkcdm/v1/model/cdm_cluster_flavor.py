# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmClusterFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'ram': 'int',
        'name': 'str',
        'region': 'str',
        'typename': 'str',
        'cluster_mode': 'str',
        'status': 'str',
        'str_id': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'ram': 'ram',
        'name': 'name',
        'region': 'region',
        'typename': 'typename',
        'cluster_mode': 'clusterMode',
        'status': 'status',
        'str_id': 'str_id'
    }

    def __init__(self, cpu=None, ram=None, name=None, region=None, typename=None, cluster_mode=None, status=None, str_id=None):
        r"""CdmClusterFlavor

        The model defined in huaweicloud sdk

        :param cpu: CPU。
        :type cpu: int
        :param ram: 内存。
        :type ram: int
        :param name: 规格名称。
        :type name: str
        :param region: region。
        :type region: str
        :param typename: 类型名称。
        :type typename: str
        :param cluster_mode: 集群模式。
        :type cluster_mode: str
        :param status: 规格状态。
        :type status: str
        :param str_id: 规格ID。
        :type str_id: str
        """
        
        

        self._cpu = None
        self._ram = None
        self._name = None
        self._region = None
        self._typename = None
        self._cluster_mode = None
        self._status = None
        self._str_id = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if typename is not None:
            self.typename = typename
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if status is not None:
            self.status = status
        if str_id is not None:
            self.str_id = str_id

    @property
    def cpu(self):
        r"""Gets the cpu of this CdmClusterFlavor.

        CPU。

        :return: The cpu of this CdmClusterFlavor.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this CdmClusterFlavor.

        CPU。

        :param cpu: The cpu of this CdmClusterFlavor.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        r"""Gets the ram of this CdmClusterFlavor.

        内存。

        :return: The ram of this CdmClusterFlavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this CdmClusterFlavor.

        内存。

        :param ram: The ram of this CdmClusterFlavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def name(self):
        r"""Gets the name of this CdmClusterFlavor.

        规格名称。

        :return: The name of this CdmClusterFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CdmClusterFlavor.

        规格名称。

        :param name: The name of this CdmClusterFlavor.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this CdmClusterFlavor.

        region。

        :return: The region of this CdmClusterFlavor.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CdmClusterFlavor.

        region。

        :param region: The region of this CdmClusterFlavor.
        :type region: str
        """
        self._region = region

    @property
    def typename(self):
        r"""Gets the typename of this CdmClusterFlavor.

        类型名称。

        :return: The typename of this CdmClusterFlavor.
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        r"""Sets the typename of this CdmClusterFlavor.

        类型名称。

        :param typename: The typename of this CdmClusterFlavor.
        :type typename: str
        """
        self._typename = typename

    @property
    def cluster_mode(self):
        r"""Gets the cluster_mode of this CdmClusterFlavor.

        集群模式。

        :return: The cluster_mode of this CdmClusterFlavor.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        r"""Sets the cluster_mode of this CdmClusterFlavor.

        集群模式。

        :param cluster_mode: The cluster_mode of this CdmClusterFlavor.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def status(self):
        r"""Gets the status of this CdmClusterFlavor.

        规格状态。

        :return: The status of this CdmClusterFlavor.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CdmClusterFlavor.

        规格状态。

        :param status: The status of this CdmClusterFlavor.
        :type status: str
        """
        self._status = status

    @property
    def str_id(self):
        r"""Gets the str_id of this CdmClusterFlavor.

        规格ID。

        :return: The str_id of this CdmClusterFlavor.
        :rtype: str
        """
        return self._str_id

    @str_id.setter
    def str_id(self, str_id):
        r"""Sets the str_id of this CdmClusterFlavor.

        规格ID。

        :param str_id: The str_id of this CdmClusterFlavor.
        :type str_id: str
        """
        self._str_id = str_id

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
        if not isinstance(other, CdmClusterFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
