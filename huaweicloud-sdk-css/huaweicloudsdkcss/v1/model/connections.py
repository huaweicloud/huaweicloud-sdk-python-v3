# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Connections:

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
        'status': 'str',
        'max_session': 'str',
        'specification_name': 'str',
        'created_at': 'str',
        'update_at': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'max_session': 'maxSession',
        'specification_name': 'specificationName',
        'created_at': 'created_at',
        'update_at': 'update_at',
        'domain_id': 'domain_id'
    }

    def __init__(self, id=None, status=None, max_session=None, specification_name=None, created_at=None, update_at=None, domain_id=None):
        """Connections

        The model defined in huaweicloud sdk

        :param id: 终端节点ID。
        :type id: str
        :param status: 终端节点状态。 - accepted：允许该终端节点连接。 - rejected：拒绝该终端节点连接。
        :type status: str
        :param max_session: 最大连接数。
        :type max_session: str
        :param specification_name: 终端节点名称。
        :type specification_name: str
        :param created_at: 创建时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。
        :type created_at: str
        :param update_at: 更新时间。默认为null。
        :type update_at: str
        :param domain_id: 拥有者。
        :type domain_id: str
        """
        
        

        self._id = None
        self._status = None
        self._max_session = None
        self._specification_name = None
        self._created_at = None
        self._update_at = None
        self._domain_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if max_session is not None:
            self.max_session = max_session
        if specification_name is not None:
            self.specification_name = specification_name
        if created_at is not None:
            self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def id(self):
        """Gets the id of this Connections.

        终端节点ID。

        :return: The id of this Connections.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Connections.

        终端节点ID。

        :param id: The id of this Connections.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this Connections.

        终端节点状态。 - accepted：允许该终端节点连接。 - rejected：拒绝该终端节点连接。

        :return: The status of this Connections.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Connections.

        终端节点状态。 - accepted：允许该终端节点连接。 - rejected：拒绝该终端节点连接。

        :param status: The status of this Connections.
        :type status: str
        """
        self._status = status

    @property
    def max_session(self):
        """Gets the max_session of this Connections.

        最大连接数。

        :return: The max_session of this Connections.
        :rtype: str
        """
        return self._max_session

    @max_session.setter
    def max_session(self, max_session):
        """Sets the max_session of this Connections.

        最大连接数。

        :param max_session: The max_session of this Connections.
        :type max_session: str
        """
        self._max_session = max_session

    @property
    def specification_name(self):
        """Gets the specification_name of this Connections.

        终端节点名称。

        :return: The specification_name of this Connections.
        :rtype: str
        """
        return self._specification_name

    @specification_name.setter
    def specification_name(self, specification_name):
        """Sets the specification_name of this Connections.

        终端节点名称。

        :param specification_name: The specification_name of this Connections.
        :type specification_name: str
        """
        self._specification_name = specification_name

    @property
    def created_at(self):
        """Gets the created_at of this Connections.

        创建时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。

        :return: The created_at of this Connections.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Connections.

        创建时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。

        :param created_at: The created_at of this Connections.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def update_at(self):
        """Gets the update_at of this Connections.

        更新时间。默认为null。

        :return: The update_at of this Connections.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this Connections.

        更新时间。默认为null。

        :param update_at: The update_at of this Connections.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def domain_id(self):
        """Gets the domain_id of this Connections.

        拥有者。

        :return: The domain_id of this Connections.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Connections.

        拥有者。

        :param domain_id: The domain_id of this Connections.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, Connections):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
