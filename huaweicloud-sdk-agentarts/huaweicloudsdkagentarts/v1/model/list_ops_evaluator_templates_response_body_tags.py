# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorTemplatesResponseBodyTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zh_cn': 'ListOpsEvaluatorTemplatesResponseBodyTagsZhCN'
    }

    attribute_map = {
        'zh_cn': 'zh-CN'
    }

    def __init__(self, zh_cn=None):
        r"""ListOpsEvaluatorTemplatesResponseBodyTags

        The model defined in huaweicloud sdk

        :param zh_cn: 
        :type zh_cn: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyTagsZhCN`
        """
        
        

        self._zh_cn = None
        self.discriminator = None

        if zh_cn is not None:
            self.zh_cn = zh_cn

    @property
    def zh_cn(self):
        r"""Gets the zh_cn of this ListOpsEvaluatorTemplatesResponseBodyTags.

        :return: The zh_cn of this ListOpsEvaluatorTemplatesResponseBodyTags.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyTagsZhCN`
        """
        return self._zh_cn

    @zh_cn.setter
    def zh_cn(self, zh_cn):
        r"""Sets the zh_cn of this ListOpsEvaluatorTemplatesResponseBodyTags.

        :param zh_cn: The zh_cn of this ListOpsEvaluatorTemplatesResponseBodyTags.
        :type zh_cn: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyTagsZhCN`
        """
        self._zh_cn = zh_cn

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
        if not isinstance(other, ListOpsEvaluatorTemplatesResponseBodyTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
