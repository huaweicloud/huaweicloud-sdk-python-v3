# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullStagesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_stages': 'dict(str, BuildStageRecord)'
    }

    attribute_map = {
        'build_stages': 'build_stages'
    }

    def __init__(self, build_stages=None):
        r"""FullStagesResult

        The model defined in huaweicloud sdk

        :param build_stages: 构建步骤
        :type build_stages: dict(str, BuildStageRecord)
        """
        
        

        self._build_stages = None
        self.discriminator = None

        if build_stages is not None:
            self.build_stages = build_stages

    @property
    def build_stages(self):
        r"""Gets the build_stages of this FullStagesResult.

        构建步骤

        :return: The build_stages of this FullStagesResult.
        :rtype: dict(str, BuildStageRecord)
        """
        return self._build_stages

    @build_stages.setter
    def build_stages(self, build_stages):
        r"""Sets the build_stages of this FullStagesResult.

        构建步骤

        :param build_stages: The build_stages of this FullStagesResult.
        :type build_stages: dict(str, BuildStageRecord)
        """
        self._build_stages = build_stages

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
        if not isinstance(other, FullStagesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
