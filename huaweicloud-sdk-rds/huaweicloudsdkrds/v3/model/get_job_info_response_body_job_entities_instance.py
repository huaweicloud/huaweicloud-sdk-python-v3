# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetJobInfoResponseBodyJobEntitiesInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'type': 'str',
        'datastore': 'GetJobInfoResponseBodyJobEntitiesInstanceDatastore',
        'replica_of': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'type': 'type',
        'datastore': 'datastore',
        'replica_of': 'replica_of'
    }

    def __init__(self, endpoint=None, type=None, datastore=None, replica_of=None):
        r"""GetJobInfoResponseBodyJobEntitiesInstance

        The model defined in huaweicloud sdk

        :param endpoint: 实例的连接地址。
        :type endpoint: str
        :param type: 实例类型。
        :type type: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesInstanceDatastore`
        :param replica_of: 主实例ID，仅创建只读实例的时候返回。
        :type replica_of: str
        """
        
        

        self._endpoint = None
        self._type = None
        self._datastore = None
        self._replica_of = None
        self.discriminator = None

        if endpoint is not None:
            self.endpoint = endpoint
        if type is not None:
            self.type = type
        if datastore is not None:
            self.datastore = datastore
        if replica_of is not None:
            self.replica_of = replica_of

    @property
    def endpoint(self):
        r"""Gets the endpoint of this GetJobInfoResponseBodyJobEntitiesInstance.

        实例的连接地址。

        :return: The endpoint of this GetJobInfoResponseBodyJobEntitiesInstance.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this GetJobInfoResponseBodyJobEntitiesInstance.

        实例的连接地址。

        :param endpoint: The endpoint of this GetJobInfoResponseBodyJobEntitiesInstance.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def type(self):
        r"""Gets the type of this GetJobInfoResponseBodyJobEntitiesInstance.

        实例类型。

        :return: The type of this GetJobInfoResponseBodyJobEntitiesInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GetJobInfoResponseBodyJobEntitiesInstance.

        实例类型。

        :param type: The type of this GetJobInfoResponseBodyJobEntitiesInstance.
        :type type: str
        """
        self._type = type

    @property
    def datastore(self):
        r"""Gets the datastore of this GetJobInfoResponseBodyJobEntitiesInstance.

        :return: The datastore of this GetJobInfoResponseBodyJobEntitiesInstance.
        :rtype: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesInstanceDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this GetJobInfoResponseBodyJobEntitiesInstance.

        :param datastore: The datastore of this GetJobInfoResponseBodyJobEntitiesInstance.
        :type datastore: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesInstanceDatastore`
        """
        self._datastore = datastore

    @property
    def replica_of(self):
        r"""Gets the replica_of of this GetJobInfoResponseBodyJobEntitiesInstance.

        主实例ID，仅创建只读实例的时候返回。

        :return: The replica_of of this GetJobInfoResponseBodyJobEntitiesInstance.
        :rtype: str
        """
        return self._replica_of

    @replica_of.setter
    def replica_of(self, replica_of):
        r"""Sets the replica_of of this GetJobInfoResponseBodyJobEntitiesInstance.

        主实例ID，仅创建只读实例的时候返回。

        :param replica_of: The replica_of of this GetJobInfoResponseBodyJobEntitiesInstance.
        :type replica_of: str
        """
        self._replica_of = replica_of

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
        if not isinstance(other, GetJobInfoResponseBodyJobEntitiesInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
