# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetAddRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_model_id': 'str',
        'name': 'str',
        'display_name': 'str',
        'parent': 'str',
        'properties': 'list[PropertyRequest]',
        'analyses': 'list[AnalysisRequest]'
    }

    attribute_map = {
        'asset_model_id': 'asset_model_id',
        'name': 'name',
        'display_name': 'display_name',
        'parent': 'parent',
        'properties': 'properties',
        'analyses': 'analyses'
    }

    def __init__(self, asset_model_id=None, name=None, display_name=None, parent=None, properties=None, analyses=None):
        r"""AssetAddRequest

        The model defined in huaweicloud sdk

        :param asset_model_id: 资产模型ID
        :type asset_model_id: str
        :param name: 资产名称，正则：\&quot;^[a-zA-Z][a-zA-Z0-9_-]{0,63}$\&quot;
        :type name: str
        :param display_name: 资产显示名称，修改资产时，\&quot;\&quot;代表配置为空、null或不携带代表不修改，正则：\&quot;^[\\\\u4E-\\\\u9FA5A-Za-z0-9_@#.-]{0,64}$\&quot;
        :type display_name: str
        :param parent: 父资产ID，根资产的父资产ID为null，修改资产时，null或不携带代表不修改
        :type parent: str
        :param properties: 属性集，最多200个
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyRequest`]
        :param analyses: 分析任务集，最多50个
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisRequest`]
        """
        
        

        self._asset_model_id = None
        self._name = None
        self._display_name = None
        self._parent = None
        self._properties = None
        self._analyses = None
        self.discriminator = None

        self.asset_model_id = asset_model_id
        self.name = name
        if display_name is not None:
            self.display_name = display_name
        if parent is not None:
            self.parent = parent
        if properties is not None:
            self.properties = properties
        if analyses is not None:
            self.analyses = analyses

    @property
    def asset_model_id(self):
        r"""Gets the asset_model_id of this AssetAddRequest.

        资产模型ID

        :return: The asset_model_id of this AssetAddRequest.
        :rtype: str
        """
        return self._asset_model_id

    @asset_model_id.setter
    def asset_model_id(self, asset_model_id):
        r"""Sets the asset_model_id of this AssetAddRequest.

        资产模型ID

        :param asset_model_id: The asset_model_id of this AssetAddRequest.
        :type asset_model_id: str
        """
        self._asset_model_id = asset_model_id

    @property
    def name(self):
        r"""Gets the name of this AssetAddRequest.

        资产名称，正则：\"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$\"

        :return: The name of this AssetAddRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssetAddRequest.

        资产名称，正则：\"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$\"

        :param name: The name of this AssetAddRequest.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this AssetAddRequest.

        资产显示名称，修改资产时，\"\"代表配置为空、null或不携带代表不修改，正则：\"^[\\\\u4E-\\\\u9FA5A-Za-z0-9_@#.-]{0,64}$\"

        :return: The display_name of this AssetAddRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this AssetAddRequest.

        资产显示名称，修改资产时，\"\"代表配置为空、null或不携带代表不修改，正则：\"^[\\\\u4E-\\\\u9FA5A-Za-z0-9_@#.-]{0,64}$\"

        :param display_name: The display_name of this AssetAddRequest.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def parent(self):
        r"""Gets the parent of this AssetAddRequest.

        父资产ID，根资产的父资产ID为null，修改资产时，null或不携带代表不修改

        :return: The parent of this AssetAddRequest.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        r"""Sets the parent of this AssetAddRequest.

        父资产ID，根资产的父资产ID为null，修改资产时，null或不携带代表不修改

        :param parent: The parent of this AssetAddRequest.
        :type parent: str
        """
        self._parent = parent

    @property
    def properties(self):
        r"""Gets the properties of this AssetAddRequest.

        属性集，最多200个

        :return: The properties of this AssetAddRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyRequest`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this AssetAddRequest.

        属性集，最多200个

        :param properties: The properties of this AssetAddRequest.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyRequest`]
        """
        self._properties = properties

    @property
    def analyses(self):
        r"""Gets the analyses of this AssetAddRequest.

        分析任务集，最多50个

        :return: The analyses of this AssetAddRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisRequest`]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        r"""Sets the analyses of this AssetAddRequest.

        分析任务集，最多50个

        :param analyses: The analyses of this AssetAddRequest.
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisRequest`]
        """
        self._analyses = analyses

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
        if not isinstance(other, AssetAddRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
