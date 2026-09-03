# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlScriptingResultResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_format': 'str',
        'result_path': 'str'
    }

    attribute_map = {
        'result_format': 'result_format',
        'result_path': 'result_path'
    }

    def __init__(self, result_format=None, result_path=None):
        r"""SparkSqlScriptingResultResponse

        The model defined in huaweicloud sdk

        :param result_format: **参数解释**：查询类SQL结果格式，用于指定结果数据的输出格式。 **取值范围**：支持csv格式。 
        :type result_format: str
        :param result_path: **参数解释**：查询类SQL结果OBS路径，用于指定结果数据的存储位置。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/results/result.csv. 
        :type result_path: str
        """
        
        

        self._result_format = None
        self._result_path = None
        self.discriminator = None

        if result_format is not None:
            self.result_format = result_format
        if result_path is not None:
            self.result_path = result_path

    @property
    def result_format(self):
        r"""Gets the result_format of this SparkSqlScriptingResultResponse.

        **参数解释**：查询类SQL结果格式，用于指定结果数据的输出格式。 **取值范围**：支持csv格式。 

        :return: The result_format of this SparkSqlScriptingResultResponse.
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        r"""Sets the result_format of this SparkSqlScriptingResultResponse.

        **参数解释**：查询类SQL结果格式，用于指定结果数据的输出格式。 **取值范围**：支持csv格式。 

        :param result_format: The result_format of this SparkSqlScriptingResultResponse.
        :type result_format: str
        """
        self._result_format = result_format

    @property
    def result_path(self):
        r"""Gets the result_path of this SparkSqlScriptingResultResponse.

        **参数解释**：查询类SQL结果OBS路径，用于指定结果数据的存储位置。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/results/result.csv. 

        :return: The result_path of this SparkSqlScriptingResultResponse.
        :rtype: str
        """
        return self._result_path

    @result_path.setter
    def result_path(self, result_path):
        r"""Sets the result_path of this SparkSqlScriptingResultResponse.

        **参数解释**：查询类SQL结果OBS路径，用于指定结果数据的存储位置。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/results/result.csv. 

        :param result_path: The result_path of this SparkSqlScriptingResultResponse.
        :type result_path: str
        """
        self._result_path = result_path

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
        if not isinstance(other, SparkSqlScriptingResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
