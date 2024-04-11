# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CnInfoBeforeReduce:

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
        'availability_zone': 'str',
        'support_reduce': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'availability_zone': 'availability_zone',
        'support_reduce': 'support_reduce'
    }

    def __init__(self, id=None, name=None, status=None, availability_zone=None, support_reduce=None):
        """CnInfoBeforeReduce

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param status: 节点状态。 取值： 值为“normal”，表示节点正常。 值为“abnormal”，表示节点异常。 值为“creating”，表示节点正在创建。 值为“createfail”，表示节点创建失败。
        :type status: str
        :param availability_zone: 可用区。
        :type availability_zone: str
        :param support_reduce: 是否允许删除。
        :type support_reduce: bool
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._availability_zone = None
        self._support_reduce = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if support_reduce is not None:
            self.support_reduce = support_reduce

    @property
    def id(self):
        """Gets the id of this CnInfoBeforeReduce.

        节点ID。

        :return: The id of this CnInfoBeforeReduce.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CnInfoBeforeReduce.

        节点ID。

        :param id: The id of this CnInfoBeforeReduce.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CnInfoBeforeReduce.

        节点名称。

        :return: The name of this CnInfoBeforeReduce.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CnInfoBeforeReduce.

        节点名称。

        :param name: The name of this CnInfoBeforeReduce.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CnInfoBeforeReduce.

        节点状态。 取值： 值为“normal”，表示节点正常。 值为“abnormal”，表示节点异常。 值为“creating”，表示节点正在创建。 值为“createfail”，表示节点创建失败。

        :return: The status of this CnInfoBeforeReduce.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CnInfoBeforeReduce.

        节点状态。 取值： 值为“normal”，表示节点正常。 值为“abnormal”，表示节点异常。 值为“creating”，表示节点正在创建。 值为“createfail”，表示节点创建失败。

        :param status: The status of this CnInfoBeforeReduce.
        :type status: str
        """
        self._status = status

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CnInfoBeforeReduce.

        可用区。

        :return: The availability_zone of this CnInfoBeforeReduce.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CnInfoBeforeReduce.

        可用区。

        :param availability_zone: The availability_zone of this CnInfoBeforeReduce.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def support_reduce(self):
        """Gets the support_reduce of this CnInfoBeforeReduce.

        是否允许删除。

        :return: The support_reduce of this CnInfoBeforeReduce.
        :rtype: bool
        """
        return self._support_reduce

    @support_reduce.setter
    def support_reduce(self, support_reduce):
        """Sets the support_reduce of this CnInfoBeforeReduce.

        是否允许删除。

        :param support_reduce: The support_reduce of this CnInfoBeforeReduce.
        :type support_reduce: bool
        """
        self._support_reduce = support_reduce

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
        if not isinstance(other, CnInfoBeforeReduce):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
