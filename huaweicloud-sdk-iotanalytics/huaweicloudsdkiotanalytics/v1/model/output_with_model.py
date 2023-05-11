# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputWithModel:

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
        'output_asset_model_id': 'str',
        'output_asset_model_name': 'str',
        'output_property': 'str'
    }

    attribute_map = {
        'name': 'name',
        'output_asset_model_id': 'output_asset_model_id',
        'output_asset_model_name': 'output_asset_model_name',
        'output_property': 'output_property'
    }

    def __init__(self, name=None, output_asset_model_id=None, output_asset_model_name=None, output_property=None):
        """OutputWithModel

        The model defined in huaweicloud sdk

        :param name: 输出参数名称,formulas中定义的name
        :type name: str
        :param output_asset_model_id: 输出模型ID，如果输出到本模型可以不携带；使用导入模型和导出模型接口时，该字段无效
        :type output_asset_model_id: str
        :param output_asset_model_name: 输出模型名称，请求中携带该字段时可以不携带output_asset_model_id
        :type output_asset_model_name: str
        :param output_property: 输出属性名
        :type output_property: str
        """
        
        

        self._name = None
        self._output_asset_model_id = None
        self._output_asset_model_name = None
        self._output_property = None
        self.discriminator = None

        self.name = name
        if output_asset_model_id is not None:
            self.output_asset_model_id = output_asset_model_id
        if output_asset_model_name is not None:
            self.output_asset_model_name = output_asset_model_name
        self.output_property = output_property

    @property
    def name(self):
        """Gets the name of this OutputWithModel.

        输出参数名称,formulas中定义的name

        :return: The name of this OutputWithModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OutputWithModel.

        输出参数名称,formulas中定义的name

        :param name: The name of this OutputWithModel.
        :type name: str
        """
        self._name = name

    @property
    def output_asset_model_id(self):
        """Gets the output_asset_model_id of this OutputWithModel.

        输出模型ID，如果输出到本模型可以不携带；使用导入模型和导出模型接口时，该字段无效

        :return: The output_asset_model_id of this OutputWithModel.
        :rtype: str
        """
        return self._output_asset_model_id

    @output_asset_model_id.setter
    def output_asset_model_id(self, output_asset_model_id):
        """Sets the output_asset_model_id of this OutputWithModel.

        输出模型ID，如果输出到本模型可以不携带；使用导入模型和导出模型接口时，该字段无效

        :param output_asset_model_id: The output_asset_model_id of this OutputWithModel.
        :type output_asset_model_id: str
        """
        self._output_asset_model_id = output_asset_model_id

    @property
    def output_asset_model_name(self):
        """Gets the output_asset_model_name of this OutputWithModel.

        输出模型名称，请求中携带该字段时可以不携带output_asset_model_id

        :return: The output_asset_model_name of this OutputWithModel.
        :rtype: str
        """
        return self._output_asset_model_name

    @output_asset_model_name.setter
    def output_asset_model_name(self, output_asset_model_name):
        """Sets the output_asset_model_name of this OutputWithModel.

        输出模型名称，请求中携带该字段时可以不携带output_asset_model_id

        :param output_asset_model_name: The output_asset_model_name of this OutputWithModel.
        :type output_asset_model_name: str
        """
        self._output_asset_model_name = output_asset_model_name

    @property
    def output_property(self):
        """Gets the output_property of this OutputWithModel.

        输出属性名

        :return: The output_property of this OutputWithModel.
        :rtype: str
        """
        return self._output_property

    @output_property.setter
    def output_property(self, output_property):
        """Sets the output_property of this OutputWithModel.

        输出属性名

        :param output_property: The output_property of this OutputWithModel.
        :type output_property: str
        """
        self._output_property = output_property

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
        if not isinstance(other, OutputWithModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
