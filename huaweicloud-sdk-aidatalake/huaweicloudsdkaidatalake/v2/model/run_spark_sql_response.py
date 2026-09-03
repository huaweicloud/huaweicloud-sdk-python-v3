# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSparkSqlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statement_id': 'str'
    }

    attribute_map = {
        'statement_id': 'statement_id'
    }

    def __init__(self, statement_id=None):
        r"""RunSparkSqlResponse

        The model defined in huaweicloud sdk

        :param statement_id: **参数解释**：作业ID，用于唯一标识本次执行的SparkSql作业。可通过此ID查询作业状态和执行结果。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。
        :type statement_id: str
        """
        
        super().__init__()

        self._statement_id = None
        self.discriminator = None

        if statement_id is not None:
            self.statement_id = statement_id

    @property
    def statement_id(self):
        r"""Gets the statement_id of this RunSparkSqlResponse.

        **参数解释**：作业ID，用于唯一标识本次执行的SparkSql作业。可通过此ID查询作业状态和执行结果。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。

        :return: The statement_id of this RunSparkSqlResponse.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this RunSparkSqlResponse.

        **参数解释**：作业ID，用于唯一标识本次执行的SparkSql作业。可通过此ID查询作业状态和执行结果。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。

        :param statement_id: The statement_id of this RunSparkSqlResponse.
        :type statement_id: str
        """
        self._statement_id = statement_id

    def to_dict(self):
        import warnings
        warnings.warn("RunSparkSqlResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, RunSparkSqlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
