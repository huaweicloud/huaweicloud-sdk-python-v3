# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetModRequest:

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
        'display_name': 'str',
        'parent': 'str',
        'properties': 'list[PropertyRequest]',
        'analyses': 'list[AnalysisRequest]'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'parent': 'parent',
        'properties': 'properties',
        'analyses': 'analyses'
    }

    def __init__(self, name=None, display_name=None, parent=None, properties=None, analyses=None):
        """AssetModRequest

        The model defined in huaweicloud sdk

        :param name: 资产名称，修改资产时，null或不携带代表不修改，正则：\&quot;^[a-zA-Z][a-zA-Z0-9_-]{0,63}$\&quot;
        :type name: str
        :param display_name: 资产显示名称，修改资产时，\&quot;\&quot;代表配置为空、null或不携带代表不修改，正则：\&quot;^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{0,64}$\&quot;
        :type display_name: str
        :param parent: 父资产ID，根资产的父资产ID为null，修改资产时，null或不携带代表不修改
        :type parent: str
        :param properties: 属性集，最多200个
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyRequest`]
        :param analyses: 分析任务集，最多50个
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisRequest`]
        """
        
        

        self._name = None
        self._display_name = None
        self._parent = None
        self._properties = None
        self._analyses = None
        self.discriminator = None

        if name is not None:
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
    def name(self):
        """Gets the name of this AssetModRequest.

        资产名称，修改资产时，null或不携带代表不修改，正则：\"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$\"

        :return: The name of this AssetModRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetModRequest.

        资产名称，修改资产时，null或不携带代表不修改，正则：\"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$\"

        :param name: The name of this AssetModRequest.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AssetModRequest.

        资产显示名称，修改资产时，\"\"代表配置为空、null或不携带代表不修改，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{0,64}$\"

        :return: The display_name of this AssetModRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AssetModRequest.

        资产显示名称，修改资产时，\"\"代表配置为空、null或不携带代表不修改，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{0,64}$\"

        :param display_name: The display_name of this AssetModRequest.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def parent(self):
        """Gets the parent of this AssetModRequest.

        父资产ID，根资产的父资产ID为null，修改资产时，null或不携带代表不修改

        :return: The parent of this AssetModRequest.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this AssetModRequest.

        父资产ID，根资产的父资产ID为null，修改资产时，null或不携带代表不修改

        :param parent: The parent of this AssetModRequest.
        :type parent: str
        """
        self._parent = parent

    @property
    def properties(self):
        """Gets the properties of this AssetModRequest.

        属性集，最多200个

        :return: The properties of this AssetModRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyRequest`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AssetModRequest.

        属性集，最多200个

        :param properties: The properties of this AssetModRequest.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyRequest`]
        """
        self._properties = properties

    @property
    def analyses(self):
        """Gets the analyses of this AssetModRequest.

        分析任务集，最多50个

        :return: The analyses of this AssetModRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisRequest`]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        """Sets the analyses of this AssetModRequest.

        分析任务集，最多50个

        :param analyses: The analyses of this AssetModRequest.
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
        if not isinstance(other, AssetModRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
