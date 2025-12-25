# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DpeCompareFunctionDetail:

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
        'classify': 'str',
        'description': 'str',
        'example': 'str',
        'comparefunc': 'str'
    }

    attribute_map = {
        'name': 'name',
        'classify': 'classify',
        'description': 'description',
        'example': 'example',
        'comparefunc': 'comparefunc'
    }

    def __init__(self, name=None, classify=None, description=None, example=None, comparefunc=None):
        r"""DpeCompareFunctionDetail

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param classify: NORMAL(通用方法), STRING(字符串方法), NUMBER(数字方法), DATE(时间方法)
        :type classify: str
        :param description: 描述
        :type description: str
        :param example: 示例
        :type example: str
        :param comparefunc: 比较方法Key
        :type comparefunc: str
        """
        
        

        self._name = None
        self._classify = None
        self._description = None
        self._example = None
        self._comparefunc = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if classify is not None:
            self.classify = classify
        if description is not None:
            self.description = description
        if example is not None:
            self.example = example
        if comparefunc is not None:
            self.comparefunc = comparefunc

    @property
    def name(self):
        r"""Gets the name of this DpeCompareFunctionDetail.

        名称

        :return: The name of this DpeCompareFunctionDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DpeCompareFunctionDetail.

        名称

        :param name: The name of this DpeCompareFunctionDetail.
        :type name: str
        """
        self._name = name

    @property
    def classify(self):
        r"""Gets the classify of this DpeCompareFunctionDetail.

        NORMAL(通用方法), STRING(字符串方法), NUMBER(数字方法), DATE(时间方法)

        :return: The classify of this DpeCompareFunctionDetail.
        :rtype: str
        """
        return self._classify

    @classify.setter
    def classify(self, classify):
        r"""Sets the classify of this DpeCompareFunctionDetail.

        NORMAL(通用方法), STRING(字符串方法), NUMBER(数字方法), DATE(时间方法)

        :param classify: The classify of this DpeCompareFunctionDetail.
        :type classify: str
        """
        self._classify = classify

    @property
    def description(self):
        r"""Gets the description of this DpeCompareFunctionDetail.

        描述

        :return: The description of this DpeCompareFunctionDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DpeCompareFunctionDetail.

        描述

        :param description: The description of this DpeCompareFunctionDetail.
        :type description: str
        """
        self._description = description

    @property
    def example(self):
        r"""Gets the example of this DpeCompareFunctionDetail.

        示例

        :return: The example of this DpeCompareFunctionDetail.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        r"""Sets the example of this DpeCompareFunctionDetail.

        示例

        :param example: The example of this DpeCompareFunctionDetail.
        :type example: str
        """
        self._example = example

    @property
    def comparefunc(self):
        r"""Gets the comparefunc of this DpeCompareFunctionDetail.

        比较方法Key

        :return: The comparefunc of this DpeCompareFunctionDetail.
        :rtype: str
        """
        return self._comparefunc

    @comparefunc.setter
    def comparefunc(self, comparefunc):
        r"""Sets the comparefunc of this DpeCompareFunctionDetail.

        比较方法Key

        :param comparefunc: The comparefunc of this DpeCompareFunctionDetail.
        :type comparefunc: str
        """
        self._comparefunc = comparefunc

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DpeCompareFunctionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
