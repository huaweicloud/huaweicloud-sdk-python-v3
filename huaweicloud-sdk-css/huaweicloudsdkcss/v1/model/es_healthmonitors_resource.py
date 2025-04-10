# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsHealthmonitorsResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'protocol_port': 'str',
        'ipgroup': 'EsHealthIpgroupResource'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'protocol_port': 'protocol_port',
        'ipgroup': 'ipgroup'
    }

    def __init__(self, id=None, name=None, protocol_port=None, ipgroup=None):
        r"""EsHealthmonitorsResource

        The model defined in huaweicloud sdk

        :param id: 后端服务器ID。
        :type id: str
        :param name: 后端服务器的名称。
        :type name: str
        :param protocol_port: 后端服务的前端监听端口。
        :type protocol_port: str
        :param ipgroup: 
        :type ipgroup: :class:`huaweicloudsdkcss.v1.EsHealthIpgroupResource`
        """
        
        

        self._id = None
        self._name = None
        self._protocol_port = None
        self._ipgroup = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if ipgroup is not None:
            self.ipgroup = ipgroup

    @property
    def id(self):
        r"""Gets the id of this EsHealthmonitorsResource.

        后端服务器ID。

        :return: The id of this EsHealthmonitorsResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EsHealthmonitorsResource.

        后端服务器ID。

        :param id: The id of this EsHealthmonitorsResource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EsHealthmonitorsResource.

        后端服务器的名称。

        :return: The name of this EsHealthmonitorsResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EsHealthmonitorsResource.

        后端服务器的名称。

        :param name: The name of this EsHealthmonitorsResource.
        :type name: str
        """
        self._name = name

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this EsHealthmonitorsResource.

        后端服务的前端监听端口。

        :return: The protocol_port of this EsHealthmonitorsResource.
        :rtype: str
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this EsHealthmonitorsResource.

        后端服务的前端监听端口。

        :param protocol_port: The protocol_port of this EsHealthmonitorsResource.
        :type protocol_port: str
        """
        self._protocol_port = protocol_port

    @property
    def ipgroup(self):
        r"""Gets the ipgroup of this EsHealthmonitorsResource.

        :return: The ipgroup of this EsHealthmonitorsResource.
        :rtype: :class:`huaweicloudsdkcss.v1.EsHealthIpgroupResource`
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        r"""Sets the ipgroup of this EsHealthmonitorsResource.

        :param ipgroup: The ipgroup of this EsHealthmonitorsResource.
        :type ipgroup: :class:`huaweicloudsdkcss.v1.EsHealthIpgroupResource`
        """
        self._ipgroup = ipgroup

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
        if not isinstance(other, EsHealthmonitorsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
