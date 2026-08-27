# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelBatchDeleteReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_ids': 'list[str]'
    }

    attribute_map = {
        'model_ids': 'model_ids'
    }

    def __init__(self, model_ids=None):
        r"""ModelBatchDeleteReq

        The model defined in huaweicloud sdk

        :param model_ids: 模型id列表。
        :type model_ids: list[str]
        """
        
        

        self._model_ids = None
        self.discriminator = None

        self.model_ids = model_ids

    @property
    def model_ids(self):
        r"""Gets the model_ids of this ModelBatchDeleteReq.

        模型id列表。

        :return: The model_ids of this ModelBatchDeleteReq.
        :rtype: list[str]
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        r"""Sets the model_ids of this ModelBatchDeleteReq.

        模型id列表。

        :param model_ids: The model_ids of this ModelBatchDeleteReq.
        :type model_ids: list[str]
        """
        self._model_ids = model_ids

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
        if not isinstance(other, ModelBatchDeleteReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
