# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteHbaConfRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hba_confs': 'list[HbaConfOption]'
    }

    attribute_map = {
        'hba_confs': 'hba_confs'
    }

    def __init__(self, hba_confs=None):
        r"""DeleteHbaConfRequestBody

        The model defined in huaweicloud sdk

        :param hba_confs: **参数解释**: 需要删除的hba配置信息。 **取值范围**: 不涉及。
        :type hba_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfOption`]
        """
        
        

        self._hba_confs = None
        self.discriminator = None

        self.hba_confs = hba_confs

    @property
    def hba_confs(self):
        r"""Gets the hba_confs of this DeleteHbaConfRequestBody.

        **参数解释**: 需要删除的hba配置信息。 **取值范围**: 不涉及。

        :return: The hba_confs of this DeleteHbaConfRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfOption`]
        """
        return self._hba_confs

    @hba_confs.setter
    def hba_confs(self, hba_confs):
        r"""Sets the hba_confs of this DeleteHbaConfRequestBody.

        **参数解释**: 需要删除的hba配置信息。 **取值范围**: 不涉及。

        :param hba_confs: The hba_confs of this DeleteHbaConfRequestBody.
        :type hba_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfOption`]
        """
        self._hba_confs = hba_confs

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
        if not isinstance(other, DeleteHbaConfRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
