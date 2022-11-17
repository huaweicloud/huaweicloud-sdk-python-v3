# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetModelResponse:

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
        'properties': 'list[PropertyModelResponse]',
        'analyses': 'list[AnalysisModelResponse]',
        'created_time': 'str',
        'modified_time': 'str'
    }

    attribute_map = {
        'asset_model_id': 'asset_model_id',
        'name': 'name',
        'display_name': 'display_name',
        'properties': 'properties',
        'analyses': 'analyses',
        'created_time': 'created_time',
        'modified_time': 'modified_time'
    }

    def __init__(self, asset_model_id=None, name=None, display_name=None, properties=None, analyses=None, created_time=None, modified_time=None):
        """AssetModelResponse

        The model defined in huaweicloud sdk

        :param asset_model_id: 模型ID
        :type asset_model_id: str
        :param name: 模型名称
        :type name: str
        :param display_name: 模型显示名称
        :type display_name: str
        :param properties: 属性集
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyModelResponse`]
        :param analyses: 分析任务集
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisModelResponse`]
        :param created_time: 创建时间
        :type created_time: str
        :param modified_time: 修改时间
        :type modified_time: str
        """
        
        

        self._asset_model_id = None
        self._name = None
        self._display_name = None
        self._properties = None
        self._analyses = None
        self._created_time = None
        self._modified_time = None
        self.discriminator = None

        if asset_model_id is not None:
            self.asset_model_id = asset_model_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if properties is not None:
            self.properties = properties
        if analyses is not None:
            self.analyses = analyses
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time

    @property
    def asset_model_id(self):
        """Gets the asset_model_id of this AssetModelResponse.

        模型ID

        :return: The asset_model_id of this AssetModelResponse.
        :rtype: str
        """
        return self._asset_model_id

    @asset_model_id.setter
    def asset_model_id(self, asset_model_id):
        """Sets the asset_model_id of this AssetModelResponse.

        模型ID

        :param asset_model_id: The asset_model_id of this AssetModelResponse.
        :type asset_model_id: str
        """
        self._asset_model_id = asset_model_id

    @property
    def name(self):
        """Gets the name of this AssetModelResponse.

        模型名称

        :return: The name of this AssetModelResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetModelResponse.

        模型名称

        :param name: The name of this AssetModelResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AssetModelResponse.

        模型显示名称

        :return: The display_name of this AssetModelResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AssetModelResponse.

        模型显示名称

        :param display_name: The display_name of this AssetModelResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def properties(self):
        """Gets the properties of this AssetModelResponse.

        属性集

        :return: The properties of this AssetModelResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyModelResponse`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AssetModelResponse.

        属性集

        :param properties: The properties of this AssetModelResponse.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyModelResponse`]
        """
        self._properties = properties

    @property
    def analyses(self):
        """Gets the analyses of this AssetModelResponse.

        分析任务集

        :return: The analyses of this AssetModelResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisModelResponse`]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        """Sets the analyses of this AssetModelResponse.

        分析任务集

        :param analyses: The analyses of this AssetModelResponse.
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisModelResponse`]
        """
        self._analyses = analyses

    @property
    def created_time(self):
        """Gets the created_time of this AssetModelResponse.

        创建时间

        :return: The created_time of this AssetModelResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AssetModelResponse.

        创建时间

        :param created_time: The created_time of this AssetModelResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this AssetModelResponse.

        修改时间

        :return: The modified_time of this AssetModelResponse.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this AssetModelResponse.

        修改时间

        :param modified_time: The modified_time of this AssetModelResponse.
        :type modified_time: str
        """
        self._modified_time = modified_time

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
        if not isinstance(other, AssetModelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
