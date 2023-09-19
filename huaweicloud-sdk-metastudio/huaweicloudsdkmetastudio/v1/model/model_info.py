# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_asset_id': 'str',
        'asset_name': 'str'
    }

    attribute_map = {
        'model_asset_id': 'model_asset_id',
        'asset_name': 'asset_name'
    }

    def __init__(self, model_asset_id=None, asset_name=None):
        """ModelInfo

        The model defined in huaweicloud sdk

        :param model_asset_id: 模型资产ID
        :type model_asset_id: str
        :param asset_name: 资产名称
        :type asset_name: str
        """
        
        

        self._model_asset_id = None
        self._asset_name = None
        self.discriminator = None

        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if asset_name is not None:
            self.asset_name = asset_name

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this ModelInfo.

        模型资产ID

        :return: The model_asset_id of this ModelInfo.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this ModelInfo.

        模型资产ID

        :param model_asset_id: The model_asset_id of this ModelInfo.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this ModelInfo.

        资产名称

        :return: The asset_name of this ModelInfo.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this ModelInfo.

        资产名称

        :param asset_name: The asset_name of this ModelInfo.
        :type asset_name: str
        """
        self._asset_name = asset_name

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
        if not isinstance(other, ModelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
