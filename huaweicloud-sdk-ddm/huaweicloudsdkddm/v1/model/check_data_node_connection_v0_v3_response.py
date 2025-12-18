# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDataNodeConnectionV0V3Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rds_check_infos': 'list[CheckRdsConnectionResqVO]'
    }

    attribute_map = {
        'rds_check_infos': 'rds_check_infos'
    }

    def __init__(self, rds_check_infos=None):
        r"""CheckDataNodeConnectionV0V3Response

        The model defined in huaweicloud sdk

        :param rds_check_infos: **参数解释**：  rds测试连通性相关信息的集合。  **参数范围**：  不涉及。
        :type rds_check_infos: list[:class:`huaweicloudsdkddm.v1.CheckRdsConnectionResqVO`]
        """
        
        super().__init__()

        self._rds_check_infos = None
        self.discriminator = None

        if rds_check_infos is not None:
            self.rds_check_infos = rds_check_infos

    @property
    def rds_check_infos(self):
        r"""Gets the rds_check_infos of this CheckDataNodeConnectionV0V3Response.

        **参数解释**：  rds测试连通性相关信息的集合。  **参数范围**：  不涉及。

        :return: The rds_check_infos of this CheckDataNodeConnectionV0V3Response.
        :rtype: list[:class:`huaweicloudsdkddm.v1.CheckRdsConnectionResqVO`]
        """
        return self._rds_check_infos

    @rds_check_infos.setter
    def rds_check_infos(self, rds_check_infos):
        r"""Sets the rds_check_infos of this CheckDataNodeConnectionV0V3Response.

        **参数解释**：  rds测试连通性相关信息的集合。  **参数范围**：  不涉及。

        :param rds_check_infos: The rds_check_infos of this CheckDataNodeConnectionV0V3Response.
        :type rds_check_infos: list[:class:`huaweicloudsdkddm.v1.CheckRdsConnectionResqVO`]
        """
        self._rds_check_infos = rds_check_infos

    def to_dict(self):
        import warnings
        warnings.warn("CheckDataNodeConnectionV0V3Response.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckDataNodeConnectionV0V3Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
