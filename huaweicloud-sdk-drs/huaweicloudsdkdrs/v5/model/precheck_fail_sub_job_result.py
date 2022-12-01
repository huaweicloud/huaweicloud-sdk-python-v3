# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrecheckFailSubJobResult:

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
        'check_result': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'check_result': 'check_result'
    }

    def __init__(self, id=None, name=None, check_result=None):
        """PrecheckFailSubJobResult

        The model defined in huaweicloud sdk

        :param id: 子任务ID。
        :type id: str
        :param name: 子任务名称。
        :type name: str
        :param check_result: 子任务检查结果。
        :type check_result: str
        """
        
        

        self._id = None
        self._name = None
        self._check_result = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if check_result is not None:
            self.check_result = check_result

    @property
    def id(self):
        """Gets the id of this PrecheckFailSubJobResult.

        子任务ID。

        :return: The id of this PrecheckFailSubJobResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrecheckFailSubJobResult.

        子任务ID。

        :param id: The id of this PrecheckFailSubJobResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PrecheckFailSubJobResult.

        子任务名称。

        :return: The name of this PrecheckFailSubJobResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrecheckFailSubJobResult.

        子任务名称。

        :param name: The name of this PrecheckFailSubJobResult.
        :type name: str
        """
        self._name = name

    @property
    def check_result(self):
        """Gets the check_result of this PrecheckFailSubJobResult.

        子任务检查结果。

        :return: The check_result of this PrecheckFailSubJobResult.
        :rtype: str
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this PrecheckFailSubJobResult.

        子任务检查结果。

        :param check_result: The check_result of this PrecheckFailSubJobResult.
        :type check_result: str
        """
        self._check_result = check_result

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
        if not isinstance(other, PrecheckFailSubJobResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
