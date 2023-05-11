# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'name': 'str',
        'description': 'str',
        'ref_count': 'int',
        'status': 'str'
    }

    attribute_map = {
        'set_id': 'set_id',
        'name': 'name',
        'description': 'description',
        'ref_count': 'ref_count',
        'status': 'status'
    }

    def __init__(self, set_id=None, name=None, description=None, ref_count=None, status=None):
        """ServiceSet

        The model defined in huaweicloud sdk

        :param set_id: 服务组id
        :type set_id: str
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param ref_count: 引用次数
        :type ref_count: int
        :param status: 状态
        :type status: str
        """
        
        

        self._set_id = None
        self._name = None
        self._description = None
        self._ref_count = None
        self._status = None
        self.discriminator = None

        if set_id is not None:
            self.set_id = set_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ref_count is not None:
            self.ref_count = ref_count
        if status is not None:
            self.status = status

    @property
    def set_id(self):
        """Gets the set_id of this ServiceSet.

        服务组id

        :return: The set_id of this ServiceSet.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this ServiceSet.

        服务组id

        :param set_id: The set_id of this ServiceSet.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def name(self):
        """Gets the name of this ServiceSet.

        名称

        :return: The name of this ServiceSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceSet.

        名称

        :param name: The name of this ServiceSet.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ServiceSet.

        描述

        :return: The description of this ServiceSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceSet.

        描述

        :param description: The description of this ServiceSet.
        :type description: str
        """
        self._description = description

    @property
    def ref_count(self):
        """Gets the ref_count of this ServiceSet.

        引用次数

        :return: The ref_count of this ServiceSet.
        :rtype: int
        """
        return self._ref_count

    @ref_count.setter
    def ref_count(self, ref_count):
        """Sets the ref_count of this ServiceSet.

        引用次数

        :param ref_count: The ref_count of this ServiceSet.
        :type ref_count: int
        """
        self._ref_count = ref_count

    @property
    def status(self):
        """Gets the status of this ServiceSet.

        状态

        :return: The status of this ServiceSet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServiceSet.

        状态

        :param status: The status of this ServiceSet.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ServiceSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
