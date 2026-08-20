# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkSqlStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statement_id': 'str',
        'state': 'str'
    }

    attribute_map = {
        'statement_id': 'statement_id',
        'state': 'state'
    }

    def __init__(self, statement_id=None, state=None):
        r"""ShowSparkSqlStateResponse

        The model defined in huaweicloud sdk

        :param statement_id: **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。
        :type statement_id: str
        :param state: **参数解释**：SparkSql作业的执行状态。 **取值范围**：   - QUEUED：排队中。   - RUNNING：运行中。   - CANCELING：取消中。   - CANCELED：已取消。   - FAILED：运行失败。   - QUEUED_TIMEOUT：排队超时。   - RUNNING_TIMEOUT：运行超时。   - SUCCEED：运行成功。
        :type state: str
        """
        
        super().__init__()

        self._statement_id = None
        self._state = None
        self.discriminator = None

        if statement_id is not None:
            self.statement_id = statement_id
        if state is not None:
            self.state = state

    @property
    def statement_id(self):
        r"""Gets the statement_id of this ShowSparkSqlStateResponse.

        **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。

        :return: The statement_id of this ShowSparkSqlStateResponse.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this ShowSparkSqlStateResponse.

        **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。

        :param statement_id: The statement_id of this ShowSparkSqlStateResponse.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def state(self):
        r"""Gets the state of this ShowSparkSqlStateResponse.

        **参数解释**：SparkSql作业的执行状态。 **取值范围**：   - QUEUED：排队中。   - RUNNING：运行中。   - CANCELING：取消中。   - CANCELED：已取消。   - FAILED：运行失败。   - QUEUED_TIMEOUT：排队超时。   - RUNNING_TIMEOUT：运行超时。   - SUCCEED：运行成功。

        :return: The state of this ShowSparkSqlStateResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowSparkSqlStateResponse.

        **参数解释**：SparkSql作业的执行状态。 **取值范围**：   - QUEUED：排队中。   - RUNNING：运行中。   - CANCELING：取消中。   - CANCELED：已取消。   - FAILED：运行失败。   - QUEUED_TIMEOUT：排队超时。   - RUNNING_TIMEOUT：运行超时。   - SUCCEED：运行成功。

        :param state: The state of this ShowSparkSqlStateResponse.
        :type state: str
        """
        self._state = state

    def to_dict(self):
        import warnings
        warnings.warn("ShowSparkSqlStateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSparkSqlStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
