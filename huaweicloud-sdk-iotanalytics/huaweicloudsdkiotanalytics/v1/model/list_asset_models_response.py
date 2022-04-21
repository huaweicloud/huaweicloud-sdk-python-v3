# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetModelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'asset_models': 'list[AssetModelResponse]'
    }

    attribute_map = {
        'count': 'count',
        'asset_models': 'asset_models'
    }

    def __init__(self, count=None, asset_models=None):
        """ListAssetModelsResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param asset_models: 模型集，数量不超过limit
        :type asset_models: list[:class:`huaweicloudsdkiotanalytics.v1.AssetModelResponse`]
        """
        
        super(ListAssetModelsResponse, self).__init__()

        self._count = None
        self._asset_models = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if asset_models is not None:
            self.asset_models = asset_models

    @property
    def count(self):
        """Gets the count of this ListAssetModelsResponse.

        总数

        :return: The count of this ListAssetModelsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAssetModelsResponse.

        总数

        :param count: The count of this ListAssetModelsResponse.
        :type count: int
        """
        self._count = count

    @property
    def asset_models(self):
        """Gets the asset_models of this ListAssetModelsResponse.

        模型集，数量不超过limit

        :return: The asset_models of this ListAssetModelsResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.AssetModelResponse`]
        """
        return self._asset_models

    @asset_models.setter
    def asset_models(self, asset_models):
        """Sets the asset_models of this ListAssetModelsResponse.

        模型集，数量不超过limit

        :param asset_models: The asset_models of this ListAssetModelsResponse.
        :type asset_models: list[:class:`huaweicloudsdkiotanalytics.v1.AssetModelResponse`]
        """
        self._asset_models = asset_models

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
        if not isinstance(other, ListAssetModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
