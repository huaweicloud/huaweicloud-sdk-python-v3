# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'name_hash': 'str',
        'node_count': 'int',
        'status': 'str',
        'status_detail': 'str'
    }

    attribute_map = {
        'name': 'name',
        'name_hash': 'name_hash',
        'node_count': 'node_count',
        'status': 'status',
        'status_detail': 'status_detail'
    }

    def __init__(self, name=None, name_hash=None, node_count=None, status=None, status_detail=None):
        """OrganizationV2

        The model defined in huaweicloud sdk

        :param name: 组织名称
        :type name: str
        :param name_hash: 组织hash
        :type name_hash: str
        :param node_count: 组织节点
        :type node_count: int
        :param status: 状态
        :type status: str
        :param status_detail: 状态描述
        :type status_detail: str
        """
        
        

        self._name = None
        self._name_hash = None
        self._node_count = None
        self._status = None
        self._status_detail = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if name_hash is not None:
            self.name_hash = name_hash
        if node_count is not None:
            self.node_count = node_count
        if status is not None:
            self.status = status
        if status_detail is not None:
            self.status_detail = status_detail

    @property
    def name(self):
        """Gets the name of this OrganizationV2.

        组织名称

        :return: The name of this OrganizationV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationV2.

        组织名称

        :param name: The name of this OrganizationV2.
        :type name: str
        """
        self._name = name

    @property
    def name_hash(self):
        """Gets the name_hash of this OrganizationV2.

        组织hash

        :return: The name_hash of this OrganizationV2.
        :rtype: str
        """
        return self._name_hash

    @name_hash.setter
    def name_hash(self, name_hash):
        """Sets the name_hash of this OrganizationV2.

        组织hash

        :param name_hash: The name_hash of this OrganizationV2.
        :type name_hash: str
        """
        self._name_hash = name_hash

    @property
    def node_count(self):
        """Gets the node_count of this OrganizationV2.

        组织节点

        :return: The node_count of this OrganizationV2.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this OrganizationV2.

        组织节点

        :param node_count: The node_count of this OrganizationV2.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def status(self):
        """Gets the status of this OrganizationV2.

        状态

        :return: The status of this OrganizationV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrganizationV2.

        状态

        :param status: The status of this OrganizationV2.
        :type status: str
        """
        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this OrganizationV2.

        状态描述

        :return: The status_detail of this OrganizationV2.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this OrganizationV2.

        状态描述

        :param status_detail: The status_detail of this OrganizationV2.
        :type status_detail: str
        """
        self._status_detail = status_detail

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
        if not isinstance(other, OrganizationV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
