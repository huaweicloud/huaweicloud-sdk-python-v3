# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRsuRequest:

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
        'rsu_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'rsu_id': 'rsu_id'
    }

    def __init__(self, instance_id=None, rsu_id=None):
        r"""DeleteRsuRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param rsu_id: **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。
        :type rsu_id: str
        """
        
        

        self._instance_id = None
        self._rsu_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.rsu_id = rsu_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteRsuRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this DeleteRsuRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteRsuRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this DeleteRsuRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def rsu_id(self):
        r"""Gets the rsu_id of this DeleteRsuRequest.

        **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。

        :return: The rsu_id of this DeleteRsuRequest.
        :rtype: str
        """
        return self._rsu_id

    @rsu_id.setter
    def rsu_id(self, rsu_id):
        r"""Sets the rsu_id of this DeleteRsuRequest.

        **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。

        :param rsu_id: The rsu_id of this DeleteRsuRequest.
        :type rsu_id: str
        """
        self._rsu_id = rsu_id

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
        if not isinstance(other, DeleteRsuRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
