# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomIngressPortDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'ingress_port_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'domain_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'ingress_port_id': 'ingress_port_id',
        'offset': 'offset',
        'limit': 'limit',
        'domain_name': 'domain_name'
    }

    def __init__(self, instance_id=None, ingress_port_id=None, offset=None, limit=None, domain_name=None):
        r"""ListCustomIngressPortDomainsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param ingress_port_id: 实例自定义入方向端口ID。
        :type ingress_port_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param domain_name: 使用入方向端口的域名。
        :type domain_name: str
        """
        
        

        self._instance_id = None
        self._ingress_port_id = None
        self._offset = None
        self._limit = None
        self._domain_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.ingress_port_id = ingress_port_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListCustomIngressPortDomainsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListCustomIngressPortDomainsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListCustomIngressPortDomainsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListCustomIngressPortDomainsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def ingress_port_id(self):
        r"""Gets the ingress_port_id of this ListCustomIngressPortDomainsRequest.

        实例自定义入方向端口ID。

        :return: The ingress_port_id of this ListCustomIngressPortDomainsRequest.
        :rtype: str
        """
        return self._ingress_port_id

    @ingress_port_id.setter
    def ingress_port_id(self, ingress_port_id):
        r"""Sets the ingress_port_id of this ListCustomIngressPortDomainsRequest.

        实例自定义入方向端口ID。

        :param ingress_port_id: The ingress_port_id of this ListCustomIngressPortDomainsRequest.
        :type ingress_port_id: str
        """
        self._ingress_port_id = ingress_port_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCustomIngressPortDomainsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListCustomIngressPortDomainsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCustomIngressPortDomainsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListCustomIngressPortDomainsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCustomIngressPortDomainsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListCustomIngressPortDomainsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCustomIngressPortDomainsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListCustomIngressPortDomainsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListCustomIngressPortDomainsRequest.

        使用入方向端口的域名。

        :return: The domain_name of this ListCustomIngressPortDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListCustomIngressPortDomainsRequest.

        使用入方向端口的域名。

        :param domain_name: The domain_name of this ListCustomIngressPortDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, ListCustomIngressPortDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
