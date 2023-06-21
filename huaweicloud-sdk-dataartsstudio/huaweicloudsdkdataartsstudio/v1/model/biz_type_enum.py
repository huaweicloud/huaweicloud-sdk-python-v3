# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizTypeEnum:
    """
    allowed enum values
    """
    ATOMIC_INDEX = "ATOMIC_INDEX"
    DERIVATIVE_INDEX = "DERIVATIVE_INDEX"
    DIMENSION = "DIMENSION"
    DIMENSION_ATTRIBUTE = "DIMENSION_ATTRIBUTE"
    DIMENSION_HIERARCHIES = "DIMENSION_HIERARCHIES"
    CONDITION_GROUP = "CONDITION_GROUP"
    TIME_CONDITION = "TIME_CONDITION"
    COMMON_CONDITION = "COMMON_CONDITION"
    FACT_LOGIC_TABLE = "FACT_LOGIC_TABLE"
    TABLE_MODEL = "TABLE_MODEL"
    DIMENSION_LOGIC_TABLE = "DIMENSION_LOGIC_TABLE"
    STANDARD_ELEMENT = "STANDARD_ELEMENT"
    AGGREGATION_LOGIC_TABLE = "AGGREGATION_LOGIC_TABLE"
    TAG = "TAG"
    CODE_TABLE = "CODE_TABLE"
    TABLE_MODEL_ATTRIBUTE = "TABLE_MODEL_ATTRIBUTE"
    FACT_DIMENSION = "FACT_DIMENSION"
    FACT_ATTRIBUTE = "FACT_ATTRIBUTE"
    FACT_MEASURE = "FACT_MEASURE"
    SUMMARY_DIMENSION_ATTRIBUTE = "SUMMARY_DIMENSION_ATTRIBUTE"
    SUMMARY_TIME = "SUMMARY_TIME"
    DIMENSION_TABLE_ATTRIBUTE = "DIMENSION_TABLE_ATTRIBUTE"
    QUALITY_RULE = "QUALITY_RULE"
    BIZ_METRIC = "BIZ_METRIC"
    COMPOUND_METRIC = "COMPOUND_METRIC"
    INFO_ARCH = "INFO_ARCH"
    DEGENERATE_DIMENSION = "DEGENERATE_DIMENSION"
    TABLE_MODEL_LOGIC = "TABLE_MODEL_LOGIC"
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):
        """BizTypeEnum

        The model defined in huaweicloud sdk

        """
        
        
        self.discriminator = None

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
        if not isinstance(other, BizTypeEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
