# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkerGroupSpec:

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
        'spec_code': 'str',
        'min_replicas': 'int',
        'max_replicas': 'int'
    }

    attribute_map = {
        'name': 'name',
        'spec_code': 'spec_code',
        'min_replicas': 'min_replicas',
        'max_replicas': 'max_replicas'
    }

    def __init__(self, name=None, spec_code=None, min_replicas=None, max_replicas=None):
        r"""WorkerGroupSpec

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param spec_code: 资源规格，从规格列表查询获取。
        :type spec_code: str
        :param min_replicas: 最小副本数
        :type min_replicas: int
        :param max_replicas: 最大副本数
        :type max_replicas: int
        """
        
        

        self._name = None
        self._spec_code = None
        self._min_replicas = None
        self._max_replicas = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if spec_code is not None:
            self.spec_code = spec_code
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_replicas is not None:
            self.max_replicas = max_replicas

    @property
    def name(self):
        r"""Gets the name of this WorkerGroupSpec.

        名称

        :return: The name of this WorkerGroupSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkerGroupSpec.

        名称

        :param name: The name of this WorkerGroupSpec.
        :type name: str
        """
        self._name = name

    @property
    def spec_code(self):
        r"""Gets the spec_code of this WorkerGroupSpec.

        资源规格，从规格列表查询获取。

        :return: The spec_code of this WorkerGroupSpec.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this WorkerGroupSpec.

        资源规格，从规格列表查询获取。

        :param spec_code: The spec_code of this WorkerGroupSpec.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def min_replicas(self):
        r"""Gets the min_replicas of this WorkerGroupSpec.

        最小副本数

        :return: The min_replicas of this WorkerGroupSpec.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        r"""Sets the min_replicas of this WorkerGroupSpec.

        最小副本数

        :param min_replicas: The min_replicas of this WorkerGroupSpec.
        :type min_replicas: int
        """
        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        r"""Gets the max_replicas of this WorkerGroupSpec.

        最大副本数

        :return: The max_replicas of this WorkerGroupSpec.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        r"""Sets the max_replicas of this WorkerGroupSpec.

        最大副本数

        :param max_replicas: The max_replicas of this WorkerGroupSpec.
        :type max_replicas: int
        """
        self._max_replicas = max_replicas

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
        if not isinstance(other, WorkerGroupSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
