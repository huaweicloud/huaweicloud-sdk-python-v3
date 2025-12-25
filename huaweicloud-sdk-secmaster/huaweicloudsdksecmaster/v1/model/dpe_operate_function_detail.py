# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DpeOperateFunctionDetail:

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
        'operationfunc': 'str',
        'params': 'list[Params]'
    }

    attribute_map = {
        'name': 'name',
        'classify': 'classify',
        'description': 'description',
        'example': 'example',
        'operationfunc': 'operationfunc',
        'params': 'params'
    }

    def __init__(self, name=None, classify=None, description=None, example=None, operationfunc=None, params=None):
        r"""DpeOperateFunctionDetail

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param classify: NORMAL(通用方法), STRING(字符串方法), NUMBER(数字方法), DATE(时间方法)
        :type classify: str
        :param description: 描述
        :type description: str
        :param example: 示例
        :type example: str
        :param operationfunc: 转换方法Key
        :type operationfunc: str
        :param params: 参数集合
        :type params: list[:class:`huaweicloudsdksecmaster.v1.Params`]
        """
        
        

        self._name = None
        self._classify = None
        self._description = None
        self._example = None
        self._operationfunc = None
        self._params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if classify is not None:
            self.classify = classify
        if description is not None:
            self.description = description
        if example is not None:
            self.example = example
        if operationfunc is not None:
            self.operationfunc = operationfunc
        if params is not None:
            self.params = params

    @property
    def name(self):
        r"""Gets the name of this DpeOperateFunctionDetail.

        名称

        :return: The name of this DpeOperateFunctionDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DpeOperateFunctionDetail.

        名称

        :param name: The name of this DpeOperateFunctionDetail.
        :type name: str
        """
        self._name = name

    @property
    def classify(self):
        r"""Gets the classify of this DpeOperateFunctionDetail.

        NORMAL(通用方法), STRING(字符串方法), NUMBER(数字方法), DATE(时间方法)

        :return: The classify of this DpeOperateFunctionDetail.
        :rtype: str
        """
        return self._classify

    @classify.setter
    def classify(self, classify):
        r"""Sets the classify of this DpeOperateFunctionDetail.

        NORMAL(通用方法), STRING(字符串方法), NUMBER(数字方法), DATE(时间方法)

        :param classify: The classify of this DpeOperateFunctionDetail.
        :type classify: str
        """
        self._classify = classify

    @property
    def description(self):
        r"""Gets the description of this DpeOperateFunctionDetail.

        描述

        :return: The description of this DpeOperateFunctionDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DpeOperateFunctionDetail.

        描述

        :param description: The description of this DpeOperateFunctionDetail.
        :type description: str
        """
        self._description = description

    @property
    def example(self):
        r"""Gets the example of this DpeOperateFunctionDetail.

        示例

        :return: The example of this DpeOperateFunctionDetail.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        r"""Sets the example of this DpeOperateFunctionDetail.

        示例

        :param example: The example of this DpeOperateFunctionDetail.
        :type example: str
        """
        self._example = example

    @property
    def operationfunc(self):
        r"""Gets the operationfunc of this DpeOperateFunctionDetail.

        转换方法Key

        :return: The operationfunc of this DpeOperateFunctionDetail.
        :rtype: str
        """
        return self._operationfunc

    @operationfunc.setter
    def operationfunc(self, operationfunc):
        r"""Sets the operationfunc of this DpeOperateFunctionDetail.

        转换方法Key

        :param operationfunc: The operationfunc of this DpeOperateFunctionDetail.
        :type operationfunc: str
        """
        self._operationfunc = operationfunc

    @property
    def params(self):
        r"""Gets the params of this DpeOperateFunctionDetail.

        参数集合

        :return: The params of this DpeOperateFunctionDetail.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Params`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this DpeOperateFunctionDetail.

        参数集合

        :param params: The params of this DpeOperateFunctionDetail.
        :type params: list[:class:`huaweicloudsdksecmaster.v1.Params`]
        """
        self._params = params

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
        if not isinstance(other, DpeOperateFunctionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
