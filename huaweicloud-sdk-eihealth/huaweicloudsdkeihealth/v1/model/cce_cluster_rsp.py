# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CceClusterRsp:

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
        'status': 'str',
        'version': 'str',
        'flavor': 'str',
        'category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'version': 'version',
        'flavor': 'flavor',
        'category': 'category'
    }

    def __init__(self, id=None, name=None, status=None, version=None, flavor=None, category=None):
        r"""CceClusterRsp

        The model defined in huaweicloud sdk

        :param id: 计算集群ID。
        :type id: str
        :param name: 计算集群名称。
        :type name: str
        :param status: 计算集群状态。
        :type status: str
        :param version: 计算集群版本。
        :type version: str
        :param flavor: 计算集群规格。
        :type flavor: str
        :param category: 计算集群类别。CCE代表CCE集群，Turbo代表CCE Turbo集群。
        :type category: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._version = None
        self._flavor = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if flavor is not None:
            self.flavor = flavor
        if category is not None:
            self.category = category

    @property
    def id(self):
        r"""Gets the id of this CceClusterRsp.

        计算集群ID。

        :return: The id of this CceClusterRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CceClusterRsp.

        计算集群ID。

        :param id: The id of this CceClusterRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CceClusterRsp.

        计算集群名称。

        :return: The name of this CceClusterRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CceClusterRsp.

        计算集群名称。

        :param name: The name of this CceClusterRsp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this CceClusterRsp.

        计算集群状态。

        :return: The status of this CceClusterRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CceClusterRsp.

        计算集群状态。

        :param status: The status of this CceClusterRsp.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        r"""Gets the version of this CceClusterRsp.

        计算集群版本。

        :return: The version of this CceClusterRsp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CceClusterRsp.

        计算集群版本。

        :param version: The version of this CceClusterRsp.
        :type version: str
        """
        self._version = version

    @property
    def flavor(self):
        r"""Gets the flavor of this CceClusterRsp.

        计算集群规格。

        :return: The flavor of this CceClusterRsp.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CceClusterRsp.

        计算集群规格。

        :param flavor: The flavor of this CceClusterRsp.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def category(self):
        r"""Gets the category of this CceClusterRsp.

        计算集群类别。CCE代表CCE集群，Turbo代表CCE Turbo集群。

        :return: The category of this CceClusterRsp.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CceClusterRsp.

        计算集群类别。CCE代表CCE集群，Turbo代表CCE Turbo集群。

        :param category: The category of this CceClusterRsp.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, CceClusterRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
