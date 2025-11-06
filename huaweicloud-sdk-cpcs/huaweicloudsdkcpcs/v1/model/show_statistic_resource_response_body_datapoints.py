# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticResourceResponseBodyDatapoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'int',
        'count': 'int',
        'api_name': 'str',
        'tenant_id': 'str',
        'cluster_id': 'str',
        'server_type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'count': 'count',
        'api_name': 'api_name',
        'tenant_id': 'tenant_id',
        'cluster_id': 'cluster_id',
        'server_type': 'server_type'
    }

    def __init__(self, data=None, count=None, api_name=None, tenant_id=None, cluster_id=None, server_type=None):
        r"""ShowStatisticResourceResponseBodyDatapoints

        The model defined in huaweicloud sdk

        :param data: 数据
        :type data: int
        :param count: 数量
        :type count: int
        :param api_name: 接口名称
        :type api_name: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param server_type: 服务类型
        :type server_type: str
        """
        
        

        self._data = None
        self._count = None
        self._api_name = None
        self._tenant_id = None
        self._cluster_id = None
        self._server_type = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if count is not None:
            self.count = count
        if api_name is not None:
            self.api_name = api_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if server_type is not None:
            self.server_type = server_type

    @property
    def data(self):
        r"""Gets the data of this ShowStatisticResourceResponseBodyDatapoints.

        数据

        :return: The data of this ShowStatisticResourceResponseBodyDatapoints.
        :rtype: int
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowStatisticResourceResponseBodyDatapoints.

        数据

        :param data: The data of this ShowStatisticResourceResponseBodyDatapoints.
        :type data: int
        """
        self._data = data

    @property
    def count(self):
        r"""Gets the count of this ShowStatisticResourceResponseBodyDatapoints.

        数量

        :return: The count of this ShowStatisticResourceResponseBodyDatapoints.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowStatisticResourceResponseBodyDatapoints.

        数量

        :param count: The count of this ShowStatisticResourceResponseBodyDatapoints.
        :type count: int
        """
        self._count = count

    @property
    def api_name(self):
        r"""Gets the api_name of this ShowStatisticResourceResponseBodyDatapoints.

        接口名称

        :return: The api_name of this ShowStatisticResourceResponseBodyDatapoints.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this ShowStatisticResourceResponseBodyDatapoints.

        接口名称

        :param api_name: The api_name of this ShowStatisticResourceResponseBodyDatapoints.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowStatisticResourceResponseBodyDatapoints.

        租户ID

        :return: The tenant_id of this ShowStatisticResourceResponseBodyDatapoints.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowStatisticResourceResponseBodyDatapoints.

        租户ID

        :param tenant_id: The tenant_id of this ShowStatisticResourceResponseBodyDatapoints.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowStatisticResourceResponseBodyDatapoints.

        集群ID

        :return: The cluster_id of this ShowStatisticResourceResponseBodyDatapoints.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowStatisticResourceResponseBodyDatapoints.

        集群ID

        :param cluster_id: The cluster_id of this ShowStatisticResourceResponseBodyDatapoints.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def server_type(self):
        r"""Gets the server_type of this ShowStatisticResourceResponseBodyDatapoints.

        服务类型

        :return: The server_type of this ShowStatisticResourceResponseBodyDatapoints.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ShowStatisticResourceResponseBodyDatapoints.

        服务类型

        :param server_type: The server_type of this ShowStatisticResourceResponseBodyDatapoints.
        :type server_type: str
        """
        self._server_type = server_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStatisticResourceResponseBodyDatapoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
