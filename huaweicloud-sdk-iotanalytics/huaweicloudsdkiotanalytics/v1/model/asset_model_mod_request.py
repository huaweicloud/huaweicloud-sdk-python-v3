# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetModelModRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'properties': 'list[PropertyModelRequest]',
        'analyses': 'list[AnalysisModelRequest]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'properties': 'properties',
        'analyses': 'analyses'
    }

    def __init__(self, display_name=None, properties=None, analyses=None):
        r"""AssetModelModRequest

        The model defined in huaweicloud sdk

        :param display_name: 模型显示名称，正则：\&quot;^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\&quot;
        :type display_name: str
        :param properties: 属性集，最多200个
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyModelRequest`]
        :param analyses: 分析任务集，最多50个
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisModelRequest`]
        """
        
        

        self._display_name = None
        self._properties = None
        self._analyses = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if properties is not None:
            self.properties = properties
        if analyses is not None:
            self.analyses = analyses

    @property
    def display_name(self):
        r"""Gets the display_name of this AssetModelModRequest.

        模型显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :return: The display_name of this AssetModelModRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this AssetModelModRequest.

        模型显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :param display_name: The display_name of this AssetModelModRequest.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def properties(self):
        r"""Gets the properties of this AssetModelModRequest.

        属性集，最多200个

        :return: The properties of this AssetModelModRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyModelRequest`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this AssetModelModRequest.

        属性集，最多200个

        :param properties: The properties of this AssetModelModRequest.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyModelRequest`]
        """
        self._properties = properties

    @property
    def analyses(self):
        r"""Gets the analyses of this AssetModelModRequest.

        分析任务集，最多50个

        :return: The analyses of this AssetModelModRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisModelRequest`]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        r"""Sets the analyses of this AssetModelModRequest.

        分析任务集，最多50个

        :param analyses: The analyses of this AssetModelModRequest.
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisModelRequest`]
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
        if not isinstance(other, AssetModelModRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
