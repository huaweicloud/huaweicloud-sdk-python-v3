# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportOpsResultsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_id': 'str'
    }

    attribute_map = {
        'dataset_id': 'dataset_id'
    }

    def __init__(self, dataset_id=None):
        r"""ImportOpsResultsResponse

        The model defined in huaweicloud sdk

        :param dataset_id: **参数解释：** 数据导入完成后承载结果的目标评测集ID。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 
        :type dataset_id: str
        """
        
        super().__init__()

        self._dataset_id = None
        self.discriminator = None

        if dataset_id is not None:
            self.dataset_id = dataset_id

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this ImportOpsResultsResponse.

        **参数解释：** 数据导入完成后承载结果的目标评测集ID。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The dataset_id of this ImportOpsResultsResponse.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this ImportOpsResultsResponse.

        **参数解释：** 数据导入完成后承载结果的目标评测集ID。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :param dataset_id: The dataset_id of this ImportOpsResultsResponse.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    def to_dict(self):
        import warnings
        warnings.warn("ImportOpsResultsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ImportOpsResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
