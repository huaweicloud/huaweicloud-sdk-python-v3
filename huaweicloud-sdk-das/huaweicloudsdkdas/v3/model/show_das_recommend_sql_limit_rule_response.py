# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDasRecommendSqlLimitRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'sql_limit_infos': 'list[RecommendSqlLimitRuleRespSqlLimitInfos]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'sql_limit_infos': 'sql_limit_infos'
    }

    def __init__(self, instance_id=None, sql_limit_infos=None):
        r"""ShowDasRecommendSqlLimitRuleResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param sql_limit_infos: sql的限流信息
        :type sql_limit_infos: list[:class:`huaweicloudsdkdas.v3.RecommendSqlLimitRuleRespSqlLimitInfos`]
        """
        
        super().__init__()

        self._instance_id = None
        self._sql_limit_infos = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if sql_limit_infos is not None:
            self.sql_limit_infos = sql_limit_infos

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDasRecommendSqlLimitRuleResponse.

        实例id

        :return: The instance_id of this ShowDasRecommendSqlLimitRuleResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDasRecommendSqlLimitRuleResponse.

        实例id

        :param instance_id: The instance_id of this ShowDasRecommendSqlLimitRuleResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def sql_limit_infos(self):
        r"""Gets the sql_limit_infos of this ShowDasRecommendSqlLimitRuleResponse.

        sql的限流信息

        :return: The sql_limit_infos of this ShowDasRecommendSqlLimitRuleResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.RecommendSqlLimitRuleRespSqlLimitInfos`]
        """
        return self._sql_limit_infos

    @sql_limit_infos.setter
    def sql_limit_infos(self, sql_limit_infos):
        r"""Sets the sql_limit_infos of this ShowDasRecommendSqlLimitRuleResponse.

        sql的限流信息

        :param sql_limit_infos: The sql_limit_infos of this ShowDasRecommendSqlLimitRuleResponse.
        :type sql_limit_infos: list[:class:`huaweicloudsdkdas.v3.RecommendSqlLimitRuleRespSqlLimitInfos`]
        """
        self._sql_limit_infos = sql_limit_infos

    def to_dict(self):
        import warnings
        warnings.warn("ShowDasRecommendSqlLimitRuleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDasRecommendSqlLimitRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
