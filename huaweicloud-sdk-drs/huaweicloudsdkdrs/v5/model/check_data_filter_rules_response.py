# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDataFilterRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None):
        r"""CheckDataFilterRulesResponse

        The model defined in huaweicloud sdk

        :param id: 异步校验任务的查询标识。提交数据过滤规则校验请求后返回的任务ID，用于后续通过查询/v5/{project_id}/job/{job_id}/data-filtering/result接口获取校验结果。
        :type id: str
        """
        
        super().__init__()

        self._id = None
        self.discriminator = None

        if id is not None:
            self.id = id

    @property
    def id(self):
        r"""Gets the id of this CheckDataFilterRulesResponse.

        异步校验任务的查询标识。提交数据过滤规则校验请求后返回的任务ID，用于后续通过查询/v5/{project_id}/job/{job_id}/data-filtering/result接口获取校验结果。

        :return: The id of this CheckDataFilterRulesResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CheckDataFilterRulesResponse.

        异步校验任务的查询标识。提交数据过滤规则校验请求后返回的任务ID，用于后续通过查询/v5/{project_id}/job/{job_id}/data-filtering/result接口获取校验结果。

        :param id: The id of this CheckDataFilterRulesResponse.
        :type id: str
        """
        self._id = id

    def to_dict(self):
        import warnings
        warnings.warn("CheckDataFilterRulesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckDataFilterRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
