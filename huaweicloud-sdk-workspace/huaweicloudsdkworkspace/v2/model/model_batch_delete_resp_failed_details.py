# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelBatchDeleteRespFailedDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'model_id': 'model_id',
        'reason': 'reason'
    }

    def __init__(self, model_id=None, reason=None):
        r"""ModelBatchDeleteRespFailedDetails

        The model defined in huaweicloud sdk

        :param model_id: 模型id。
        :type model_id: str
        :param reason: 失败原因。
        :type reason: str
        """
        
        

        self._model_id = None
        self._reason = None
        self.discriminator = None

        if model_id is not None:
            self.model_id = model_id
        if reason is not None:
            self.reason = reason

    @property
    def model_id(self):
        r"""Gets the model_id of this ModelBatchDeleteRespFailedDetails.

        模型id。

        :return: The model_id of this ModelBatchDeleteRespFailedDetails.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ModelBatchDeleteRespFailedDetails.

        模型id。

        :param model_id: The model_id of this ModelBatchDeleteRespFailedDetails.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def reason(self):
        r"""Gets the reason of this ModelBatchDeleteRespFailedDetails.

        失败原因。

        :return: The reason of this ModelBatchDeleteRespFailedDetails.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ModelBatchDeleteRespFailedDetails.

        失败原因。

        :param reason: The reason of this ModelBatchDeleteRespFailedDetails.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, ModelBatchDeleteRespFailedDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
