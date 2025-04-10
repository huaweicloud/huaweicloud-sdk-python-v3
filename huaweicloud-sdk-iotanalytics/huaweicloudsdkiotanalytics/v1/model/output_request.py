# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputRequest:

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
        'output_static_asset_id': 'str',
        'output_dynamic_asset_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'output_static_asset_id': 'output_static_asset_id',
        'output_dynamic_asset_id': 'output_dynamic_asset_id'
    }

    def __init__(self, name=None, output_static_asset_id=None, output_dynamic_asset_id=None):
        r"""OutputRequest

        The model defined in huaweicloud sdk

        :param name: 输出参数名称,formulas中定义的name
        :type name: str
        :param output_static_asset_id: 输出资产ID，填写模型中定义的输出模型对应的某资产ID；创建资产时，如果是输出到本资产的模型，且output_static_asset_id和output_dynamic_asset_id都未配置，则后台自动配置output_static_asset_id为本资产ID；修改资产时，如果output_static_asset_id为null则表示置空
        :type output_static_asset_id: str
        :param output_dynamic_asset_id: 输出资产ID，填写公式动态生成资产ID，可根据入参获取资产ID，如：GetAssetId(\&quot;assetmodelName1\&quot;,\&quot;staticPropertyName1\&quot;,paramA)；修改资产时，如果output_static_asset_id为null则表示置空
        :type output_dynamic_asset_id: str
        """
        
        

        self._name = None
        self._output_static_asset_id = None
        self._output_dynamic_asset_id = None
        self.discriminator = None

        self.name = name
        if output_static_asset_id is not None:
            self.output_static_asset_id = output_static_asset_id
        if output_dynamic_asset_id is not None:
            self.output_dynamic_asset_id = output_dynamic_asset_id

    @property
    def name(self):
        r"""Gets the name of this OutputRequest.

        输出参数名称,formulas中定义的name

        :return: The name of this OutputRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OutputRequest.

        输出参数名称,formulas中定义的name

        :param name: The name of this OutputRequest.
        :type name: str
        """
        self._name = name

    @property
    def output_static_asset_id(self):
        r"""Gets the output_static_asset_id of this OutputRequest.

        输出资产ID，填写模型中定义的输出模型对应的某资产ID；创建资产时，如果是输出到本资产的模型，且output_static_asset_id和output_dynamic_asset_id都未配置，则后台自动配置output_static_asset_id为本资产ID；修改资产时，如果output_static_asset_id为null则表示置空

        :return: The output_static_asset_id of this OutputRequest.
        :rtype: str
        """
        return self._output_static_asset_id

    @output_static_asset_id.setter
    def output_static_asset_id(self, output_static_asset_id):
        r"""Sets the output_static_asset_id of this OutputRequest.

        输出资产ID，填写模型中定义的输出模型对应的某资产ID；创建资产时，如果是输出到本资产的模型，且output_static_asset_id和output_dynamic_asset_id都未配置，则后台自动配置output_static_asset_id为本资产ID；修改资产时，如果output_static_asset_id为null则表示置空

        :param output_static_asset_id: The output_static_asset_id of this OutputRequest.
        :type output_static_asset_id: str
        """
        self._output_static_asset_id = output_static_asset_id

    @property
    def output_dynamic_asset_id(self):
        r"""Gets the output_dynamic_asset_id of this OutputRequest.

        输出资产ID，填写公式动态生成资产ID，可根据入参获取资产ID，如：GetAssetId(\"assetmodelName1\",\"staticPropertyName1\",paramA)；修改资产时，如果output_static_asset_id为null则表示置空

        :return: The output_dynamic_asset_id of this OutputRequest.
        :rtype: str
        """
        return self._output_dynamic_asset_id

    @output_dynamic_asset_id.setter
    def output_dynamic_asset_id(self, output_dynamic_asset_id):
        r"""Sets the output_dynamic_asset_id of this OutputRequest.

        输出资产ID，填写公式动态生成资产ID，可根据入参获取资产ID，如：GetAssetId(\"assetmodelName1\",\"staticPropertyName1\",paramA)；修改资产时，如果output_static_asset_id为null则表示置空

        :param output_dynamic_asset_id: The output_dynamic_asset_id of this OutputRequest.
        :type output_dynamic_asset_id: str
        """
        self._output_dynamic_asset_id = output_dynamic_asset_id

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
        if not isinstance(other, OutputRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
