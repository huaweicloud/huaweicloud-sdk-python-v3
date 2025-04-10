# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataMaskParas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'algorithm_name': 'str',
        'algorithm_type': 'str',
        'en_name': 'str',
        'algorithm_parameters': 'str',
        'failure_policy': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'algorithm_name': 'algorithm_name',
        'algorithm_type': 'algorithm_type',
        'en_name': 'en_name',
        'algorithm_parameters': 'algorithm_parameters',
        'failure_policy': 'failure_policy'
    }

    def __init__(self, column_name=None, algorithm_name=None, algorithm_type=None, en_name=None, algorithm_parameters=None, failure_policy=None):
        r"""DataMaskParas

        The model defined in huaweicloud sdk

        :param column_name: 敏感字段。
        :type column_name: str
        :param algorithm_name: 算法名称。
        :type algorithm_name: str
        :param algorithm_type: 算法类型。
        :type algorithm_type: str
        :param en_name: 算法名称。
        :type en_name: str
        :param algorithm_parameters: 参数。
        :type algorithm_parameters: str
        :param failure_policy: 
        :type failure_policy: str
        """
        
        

        self._column_name = None
        self._algorithm_name = None
        self._algorithm_type = None
        self._en_name = None
        self._algorithm_parameters = None
        self._failure_policy = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if algorithm_type is not None:
            self.algorithm_type = algorithm_type
        if en_name is not None:
            self.en_name = en_name
        if algorithm_parameters is not None:
            self.algorithm_parameters = algorithm_parameters
        if failure_policy is not None:
            self.failure_policy = failure_policy

    @property
    def column_name(self):
        r"""Gets the column_name of this DataMaskParas.

        敏感字段。

        :return: The column_name of this DataMaskParas.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this DataMaskParas.

        敏感字段。

        :param column_name: The column_name of this DataMaskParas.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this DataMaskParas.

        算法名称。

        :return: The algorithm_name of this DataMaskParas.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this DataMaskParas.

        算法名称。

        :param algorithm_name: The algorithm_name of this DataMaskParas.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this DataMaskParas.

        算法类型。

        :return: The algorithm_type of this DataMaskParas.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this DataMaskParas.

        算法类型。

        :param algorithm_type: The algorithm_type of this DataMaskParas.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def en_name(self):
        r"""Gets the en_name of this DataMaskParas.

        算法名称。

        :return: The en_name of this DataMaskParas.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this DataMaskParas.

        算法名称。

        :param en_name: The en_name of this DataMaskParas.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def algorithm_parameters(self):
        r"""Gets the algorithm_parameters of this DataMaskParas.

        参数。

        :return: The algorithm_parameters of this DataMaskParas.
        :rtype: str
        """
        return self._algorithm_parameters

    @algorithm_parameters.setter
    def algorithm_parameters(self, algorithm_parameters):
        r"""Sets the algorithm_parameters of this DataMaskParas.

        参数。

        :param algorithm_parameters: The algorithm_parameters of this DataMaskParas.
        :type algorithm_parameters: str
        """
        self._algorithm_parameters = algorithm_parameters

    @property
    def failure_policy(self):
        r"""Gets the failure_policy of this DataMaskParas.

        :return: The failure_policy of this DataMaskParas.
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        r"""Sets the failure_policy of this DataMaskParas.

        :param failure_policy: The failure_policy of this DataMaskParas.
        :type failure_policy: str
        """
        self._failure_policy = failure_policy

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
        if not isinstance(other, DataMaskParas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
