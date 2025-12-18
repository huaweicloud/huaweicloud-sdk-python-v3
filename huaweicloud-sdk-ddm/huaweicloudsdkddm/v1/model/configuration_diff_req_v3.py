# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationDiffReqV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diff_para': 'ParaGroupDiff'
    }

    attribute_map = {
        'diff_para': 'diff_para'
    }

    def __init__(self, diff_para=None):
        r"""ConfigurationDiffReqV3

        The model defined in huaweicloud sdk

        :param diff_para: 
        :type diff_para: :class:`huaweicloudsdkddm.v1.ParaGroupDiff`
        """
        
        

        self._diff_para = None
        self.discriminator = None

        if diff_para is not None:
            self.diff_para = diff_para

    @property
    def diff_para(self):
        r"""Gets the diff_para of this ConfigurationDiffReqV3.

        :return: The diff_para of this ConfigurationDiffReqV3.
        :rtype: :class:`huaweicloudsdkddm.v1.ParaGroupDiff`
        """
        return self._diff_para

    @diff_para.setter
    def diff_para(self, diff_para):
        r"""Sets the diff_para of this ConfigurationDiffReqV3.

        :param diff_para: The diff_para of this ConfigurationDiffReqV3.
        :type diff_para: :class:`huaweicloudsdkddm.v1.ParaGroupDiff`
        """
        self._diff_para = diff_para

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
        if not isinstance(other, ConfigurationDiffReqV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
